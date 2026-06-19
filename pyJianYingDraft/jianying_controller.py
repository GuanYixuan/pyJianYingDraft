"""剪映自动化控制，主要与自动导出有关"""

from __future__ import annotations

import os
import time
import shutil

from enum import Enum
from pathlib import Path
from typing import Iterable, List, Optional, Literal, Callable

try:
    import uiautomation as uia
except ImportError:
    uia = None

from . import exceptions
from .exceptions import AutomationError

FULL_DESCRIPTION_PROPERTY = 30159
VIDEO_EXTENSIONS = (".mp4", ".mov", ".m4v", ".avi", ".mkv")
EXPORT_SHORTCUTS = ("{Ctrl}e", "{Ctrl}{Shift}e")
EXPORT_DIR_NAMES = ("JianyingPro", "Jianying", "剪映专业版", "剪映", "CapCut")

class ExportResolution(Enum):
    """导出分辨率"""
    RES_8K = "8K"
    RES_4K = "4K"
    RES_2K = "2K"
    RES_1080P = "1080P"
    RES_720P = "720P"
    RES_480P = "480P"

class ExportFramerate(Enum):
    """导出帧率"""
    FR_24 = "24fps"
    FR_25 = "25fps"
    FR_30 = "30fps"
    FR_50 = "50fps"
    FR_60 = "60fps"


def _dedupe_paths(paths: Iterable[Path]) -> List[Path]:
    ret: List[Path] = []
    seen = set()
    for path in paths:
        normalized = os.path.normcase(os.path.abspath(str(path)))
        if normalized in seen:
            continue
        seen.add(normalized)
        ret.append(path)
    return ret


def _candidate_export_dirs(output_path: Optional[str] = None) -> List[Path]:
    """返回剪映常见导出目录，用于新版隐藏控件时定位导出文件。"""
    candidates: List[Path] = []
    if output_path:
        target = Path(output_path).expanduser()
        candidates.append(target if target.exists() and target.is_dir() else target.parent)

    home = Path.home()
    common_roots = [
        home / "Videos",
        home / "Desktop",
        home / "Downloads",
        home / "Documents",
    ]
    for root in common_roots:
        candidates.append(root)
        candidates.extend(root / name for name in EXPORT_DIR_NAMES)

    return _dedupe_paths(candidates)


def _find_recent_video_file(candidate_dirs: Iterable[Path], started_at: float) -> Optional[str]:
    """在候选目录中寻找导出开始后生成/修改的最新视频文件。"""
    newest_file: Optional[Path] = None
    newest_mtime = started_at
    for directory in candidate_dirs:
        if not directory.exists() or not directory.is_dir():
            continue
        for path in directory.iterdir():
            if not path.is_file() or path.suffix.lower() not in VIDEO_EXTENSIONS:
                continue
            try:
                mtime = path.stat().st_mtime
            except OSError:
                continue
            if mtime >= newest_mtime:
                newest_file = path
                newest_mtime = mtime
    return str(newest_file) if newest_file is not None else None


def _find_exported_video_file(output_path: str, started_at: float) -> Optional[str]:
    candidate_dirs = _candidate_export_dirs(output_path)
    if not candidate_dirs:
        return None
    return (
        _find_recent_video_file(candidate_dirs[:1], started_at)
        or _find_recent_video_file(candidate_dirs[1:], started_at)
    )


class ControlFinder:
    """控件查找器，封装部分与控件查找相关的逻辑"""

    @staticmethod
    def desc_matcher(target_desc: str, depth: Optional[int] = 2, exact: bool = False) -> Callable[[uia.Control, int], bool]:
        """根据full_description查找控件的匹配器"""
        target_desc = target_desc.lower()
        def matcher(control: uia.Control, _depth: int) -> bool:
            if depth is not None and _depth != depth:
                return False
            full_desc: str = str(control.GetPropertyValue(FULL_DESCRIPTION_PROPERTY) or "").lower()
            return (target_desc == full_desc) if exact else (target_desc in full_desc)
        return matcher

    @staticmethod
    def class_name_matcher(class_name: str, depth: Optional[int] = 1, exact: bool = False) -> Callable[[uia.Control, int], bool]:
        """根据ClassName查找控件的匹配器"""
        class_name = class_name.lower()
        def matcher(control: uia.Control, _depth: int) -> bool:
            if depth is not None and _depth != depth:
                return False
            curr_class_name: str = str(control.ClassName or "").lower()
            return (class_name == curr_class_name) if exact else (class_name in curr_class_name)
        return matcher

    @staticmethod
    def text_matcher(target_text: str, depth: Optional[int] = None, exact: bool = False) -> Callable[[uia.Control, int], bool]:
        """根据Name或full_description查找控件。"""
        target_text = target_text.lower()
        def matcher(control: uia.Control, _depth: int) -> bool:
            if depth is not None and _depth != depth:
                return False
            name = str(getattr(control, "Name", "") or "").lower()
            full_desc = str(control.GetPropertyValue(FULL_DESCRIPTION_PROPERTY) or "").lower()
            if exact:
                return target_text in (name, full_desc)
            return target_text in name or target_text in full_desc
        return matcher

class JianyingController:
    """剪映控制器"""

    app: object
    """剪映窗口"""
    app_status: Literal["home", "edit", "pre_export"]

    def __init__(self):
        """初始化剪映控制器, 此时剪映应该处于目录页"""
        if uia is None:
            raise AutomationError("自动导出需要在Windows环境安装uiautomation库")
        self.get_window()

    def export_draft(self, draft_name: str, output_path: Optional[str] = None, *,
                     resolution: Optional[ExportResolution] = None,
                     framerate: Optional[ExportFramerate] = None,
                     timeout: float = 1200) -> None:
        """导出指定的剪映草稿。

        **注意: 需要确认有导出草稿的权限(不使用VIP功能或已开通VIP), 否则可能陷入死循环**

        Args:
            draft_name (`str`): 要导出的剪映草稿名称
            output_path (`str`, optional): 导出路径, 支持指向文件夹或直接指向文件, 不指定则使用剪映默认路径.
            resolution (`Export_resolution`, optional): 导出分辨率, 默认不改变剪映导出窗口中的设置.
            framerate (`Export_framerate`, optional): 导出帧率, 默认不改变剪映导出窗口中的设置.
            timeout (`float`, optional): 导出超时时间(秒), 默认为20分钟.

        Raises:
            `DraftNotFound`: 未找到指定名称的剪映草稿
            `AutomationError`: 剪映操作失败
        """
        print(f"开始导出 {draft_name} 至 {output_path}")
        export_started_at = time.time()
        self.get_window()
        self.switch_to_home()

        # 点击对应草稿
        draft_name_text = self._find_text_by_desc(f"HomePageDraftTitle:{draft_name}", exact=True)
        if not draft_name_text.Exists(0):
            raise exceptions.DraftNotFound(f"未找到名为{draft_name}的剪映草稿")
        draft_btn = draft_name_text.GetParentControl()
        assert draft_btn is not None
        draft_btn.Click(simulateMove=False)
        time.sleep(10)
        self.get_window()

        # 点击导出按钮
        self._open_export_window()

        # 获取原始导出路径（带后缀名）
        export_path = self._get_export_path()

        # 设置分辨率
        if resolution is not None:
            self._select_export_option("ExportSharpnessInput", resolution.value, "导出分辨率")

        # 设置帧率
        if framerate is not None:
            self._select_export_option("FrameRateInput", framerate.value, "导出帧率")

        # 点击导出
        self._confirm_export()

        # 等待导出完成
        self._wait_export_done(timeout)
        time.sleep(2)

        # 回到目录页
        self.get_window()
        self.switch_to_home()
        time.sleep(2)

        # 复制导出的文件到指定目录
        if output_path is not None:
            if export_path is None:
                export_path = _find_exported_video_file(output_path, export_started_at)
            if export_path is None:
                raise AutomationError("未能定位导出后的视频文件，请检查剪映默认导出目录")
            shutil.move(export_path, output_path)

        print(f"导出 {draft_name} 至 {output_path} 完成")

    def _find_text_by_desc(self, desc: str, *, exact: bool = False, search_depth: int = 8):
        return self.app.TextControl(
            searchDepth=search_depth,
            Compare=ControlFinder.desc_matcher(desc, depth=None, exact=exact),
        )

    def _find_text(self, text: str, *, exact: bool = False, search_depth: int = 8):
        return self.app.TextControl(
            searchDepth=search_depth,
            Compare=ControlFinder.text_matcher(text, exact=exact),
        )

    def _find_button(self, text: str, *, exact: bool = False, search_depth: int = 8):
        return self.app.ButtonControl(
            searchDepth=search_depth,
            Compare=ControlFinder.text_matcher(text, exact=exact),
        )

    def _first_existing(self, *controls):
        for control in controls:
            if control.Exists(0):
                return control
        return controls[0]

    def _click_window_relative(self, x_ratio: float, y_ratio: float) -> None:
        rect = self.app.BoundingRectangle
        x = int(rect.left + (rect.right - rect.left) * x_ratio)
        y = int(rect.top + (rect.bottom - rect.top) * y_ratio)
        uia.Click(x, y)

    def _click_and_wait_export_window(self, control, wait_seconds: float = 10) -> bool:
        control.Click(simulateMove=False)
        time.sleep(wait_seconds)
        self.get_window()
        return self.app_status == "pre_export"

    def _open_export_window(self) -> None:
        export_btn = self._find_text_by_desc("MainWindowTitleBarExportBtn")
        if export_btn.Exists(0) and self._click_and_wait_export_window(export_btn):
            return

        visible_export_btn = self._first_existing(self._find_button("导出"), self._find_text("导出"))
        if visible_export_btn.Exists(0) and self._click_and_wait_export_window(visible_export_btn):
            return

        for shortcut in EXPORT_SHORTCUTS:
            uia.SendKeys(shortcut)
            time.sleep(3)
            self.get_window()
            if self.app_status == "pre_export":
                return

        self._click_window_relative(0.94, 0.045)
        time.sleep(10)
        self.get_window()
        if self.app_status != "pre_export":
            raise AutomationError("未在编辑窗口中找到导出按钮")

    def _get_export_path(self) -> Optional[str]:
        export_path_sib = self._find_text_by_desc("ExportPath")
        if not export_path_sib.Exists(0):
            return None
        export_path_text = export_path_sib.GetSiblingControl(lambda ctrl: True)
        if export_path_text is None:
            return None
        export_path = export_path_text.GetPropertyValue(FULL_DESCRIPTION_PROPERTY)
        return str(export_path) if export_path else None

    def _select_export_option(self, input_desc: str, option_text: str, label: str) -> None:
        setting_group = self.app.GroupControl(
            searchDepth=3,
            Compare=ControlFinder.class_name_matcher("PanelSettingsGroup_QMLTYPE", depth=None),
        )
        search_root = setting_group if setting_group.Exists(0.5) else self.app
        option_btn = search_root.TextControl(
            searchDepth=8,
            Compare=ControlFinder.desc_matcher(input_desc, depth=None),
        )
        if not option_btn.Exists(0.5):
            option_btn = self._find_text(label)
        if not option_btn.Exists(0.5):
            raise AutomationError(f"未找到{label}下拉框")

        option_btn.Click(simulateMove=False)
        time.sleep(0.5)
        option_item = self._find_text(option_text)
        if not option_item.Exists(0.5):
            raise AutomationError(f"未找到{option_text}{label}选项")
        option_item.Click(simulateMove=False)
        time.sleep(0.5)

    def _confirm_export(self) -> None:
        export_btn = self._find_text_by_desc("ExportOkBtn", exact=True)
        if not export_btn.Exists(0):
            export_btn = self._find_button("导出", exact=True)
        if export_btn.Exists(0):
            export_btn.Click(simulateMove=False)
        else:
            uia.SendKeys("{Enter}")
        time.sleep(5)

    def _wait_export_done(self, timeout: float) -> None:
        st = time.time()
        while True:
            self.get_window()
            if self.app_status != "pre_export":
                time.sleep(1)
                continue

            succeed_close_btn = self._find_text_by_desc("ExportSucceedCloseBtn")
            if not succeed_close_btn.Exists(0):
                succeed_close_btn = self._first_existing(self._find_button("完成"), self._find_button("关闭"))
            if succeed_close_btn.Exists(0):
                succeed_close_btn.Click(simulateMove=False)
                break

            if time.time() - st > timeout:
                raise AutomationError("导出超时, 时限为%d秒" % timeout)

            time.sleep(1)

    def switch_to_home(self) -> None:
        """切换到剪映主页"""
        if self.app_status == "home":
            return
        if self.app_status != "edit":
            raise AutomationError("仅支持从编辑模式切换到主页")
        close_btn = self.app.GroupControl(searchDepth=1, ClassName="TitleBarButton", foundIndex=3)
        close_btn.Click(simulateMove=False)
        time.sleep(2)
        self.get_window()

    def get_window(self) -> None:
        """寻找剪映窗口并置顶"""
        if hasattr(self, "app") and self.app.Exists(0):
            self.app.SetTopmost(False)

        self.app = uia.WindowControl(searchDepth=1, Compare=self.__jianying_window_cmp)
        if not self.app.Exists(0):
            raise AutomationError("剪映窗口未找到")

        # 寻找可能存在的导出窗口
        export_window = self.app.WindowControl(searchDepth=1, Name="导出")
        if export_window.Exists(0):
            self.app = export_window
            self.app_status = "pre_export"

        self.app.SetActive()
        self.app.SetTopmost()

    def __jianying_window_cmp(self, control: uia.WindowControl, depth: int) -> bool:
        if control.Name != "剪映专业版":
            return False
        if "HomePage".lower() in control.ClassName.lower():
            self.app_status = "home"
            return True
        if "MainWindow".lower() in control.ClassName.lower():
            self.app_status = "edit"
            return True
        return False
