"""剪映自动化控制，主要与自动导出有关"""

import time
import shutil
import uiautomation as uia

from typing import Optional, Literal

from . import exceptions
from .exceptions import AutomationError

class Jianying_controller:
    """剪映控制器"""

    app: uia.WindowControl
    """剪映窗口"""
    app_status: Literal["home", "edit", "pre_export"]

    def __init__(self):
        """初始化剪映控制器, 此时剪映应该处于目录页"""
        self.get_window()

    def export_draft(self, draft_name: str, output_dir: Optional[str] = None, timeout: float = 1200) -> None:
        """导出指定的剪映草稿

        **注意: 需要确认有导出草稿的权限(不使用VIP功能或已开通VIP), 否则可能陷入死循环**

        Args:
            draft_name (`str`): 要导出的剪映草稿名称
            output_path (`str`, optional): 导出路径, 导出完成后会将文件剪切到此, 不指定则使用剪映默认路径.
            timeout (`float`, optional): 导出超时时间(秒), 默认为20分钟.

        Raises:
            `DraftNotFound`: 未找到指定名称的剪映草稿
            `AutomationError`: 剪映操作失败
        """
        print(f"开始导出 {draft_name} 至 {output_dir}")
        self.get_window()
        self.switch_to_home()

        # 点击对应草稿
        draft_name_text = self.app.TextControl(searchDepth=2,
                                               Compare=lambda ctrl, depth: self.__draft_name_cmp(draft_name, ctrl, depth))
        if not draft_name_text.Exists(0):
            raise exceptions.DraftNotFound(f"未找到名为{draft_name}的剪映草稿")
        draft_btn = draft_name_text.GetParentControl()
        assert draft_btn is not None
        draft_btn.Click(simulateMove=False)
        time.sleep(10)
        self.get_window()

        # 点击导出按钮
        export_btn = self.app.TextControl(searchDepth=2, Compare=self.__edit_page_export_cmp)
        if not export_btn.Exists(0):
            raise AutomationError("未找到导出按钮")
        export_btn.Click(simulateMove=False)
        time.sleep(10)
        self.get_window()

        # 获取原始导出路径
        export_path_sib = self.app.TextControl(searchDepth=2, Compare=self.__export_path_cmp)
        if not export_path_sib.Exists(0):
            raise AutomationError("未找到导出路径框")
        export_path_text = export_path_sib.GetSiblingControl(lambda ctrl: True)
        assert export_path_text is not None
        export_path = export_path_text.GetPropertyValue(30159)

        # 点击导出
        export_btn = self.app.TextControl(searchDepth=2, Compare=self.__export_btn_cmp)
        if not export_btn.Exists(0):
            raise AutomationError("未找到导出按钮")
        export_btn.Click(simulateMove=False)
        time.sleep(5)

        # 等待导出完成
        st = time.time()
        while True:
            self.get_window()
            if self.app_status != "pre_export": continue

            export_window = self.app.WindowControl(searchDepth=1, Name="JianyingPro")
            if export_window.Exists(0):
                close_btn = export_window.ButtonControl(Name="关闭")
                if close_btn.Exists(1):
                    close_btn.Click(simulateMove=False)
                break

            if time.time() - st > timeout:
                raise AutomationError("导出超时, 时限为%d秒" % timeout)

            time.sleep(1)
        time.sleep(2)

        # 回到目录页
        self.get_window()
        self.switch_to_home()
        time.sleep(2)

        # 复制导出的文件到指定目录
        if output_dir is not None:
            shutil.move(export_path, output_dir)

        print(f"导出 {draft_name} 至 {output_dir} 完成")

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

    @staticmethod
    def __draft_name_cmp(draft_name: str, control: uia.TextControl, depth: int) -> bool:
        if depth != 2:
            return False
        full_desc: str = control.GetPropertyValue(30159)
        return "Title:".lower() in full_desc.lower() and draft_name in full_desc

    @staticmethod
    def __edit_page_export_cmp(control: uia.TextControl, depth: int) -> bool:
        if depth != 2:
            return False
        full_desc: str = control.GetPropertyValue(30159).lower()
        return "title" in full_desc and "export" in full_desc

    @staticmethod
    def __export_btn_cmp(control: uia.TextControl, depth: int) -> bool:
        if depth != 2:
            return False
        full_desc: str = control.GetPropertyValue(30159).lower()
        return "ExportOkBtn".lower() == full_desc

    @staticmethod
    def __export_path_cmp(control: uia.TextControl, depth: int) -> bool:
        if depth != 2:
            return False
        full_desc: str = control.GetPropertyValue(30159).lower()
        return "ExportPath".lower() in full_desc
