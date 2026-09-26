from __future__ import annotations

from copy import deepcopy
from typing import Literal, List, Optional, Type, Union

from ._script_file_protocol import ScriptFileProtocol
from .audio_segment import AudioSegment
from .effect_segment import EffectSegment, FilterSegment
from .local_materials import AudioMaterial, VideoMaterial
from .metadata import FilterType, VideoCharacterEffectType, VideoSceneEffectType
from .segment import BaseSegment, ClipSettings
from .text_segment import TextSegment, TextStyle
from .time_util import Timerange, srt_tstamp, tim
from .track import Track, TrackRef, TrackSpec, TrackType
from .video_segment import StickerSegment, VideoSegment


class _ScriptFileSegmentOps:
    def _get_track(
        self: ScriptFileProtocol,
        segment_type: Type[BaseSegment],
        track: Optional[Union[str, TrackRef]],
    ) -> Track:
        if isinstance(track, TrackRef):
            return self._resolve_track_ref(track)
        if track is not None:
            if track not in self.tracks:
                raise NameError("不存在名为 '%s' 的轨道" % track)
            return self.tracks[track]

        count = sum(1 for current_track in self.tracks.values() if current_track.accept_segment_type == segment_type)
        if count == 0:
            raise NameError("不存在接受 '%s' 的轨道" % segment_type)
        if count > 1:
            raise NameError("存在多个接受 '%s' 的轨道, 请指定轨道名称" % segment_type)

        return next(current_track for current_track in self.tracks.values() if current_track.accept_segment_type == segment_type)

    def add_material(self: ScriptFileProtocol, material: Union[VideoMaterial, AudioMaterial]) -> "ScriptFile":
        """向草稿文件中添加一个素材"""
        if material in self.materials:
            return self
        if isinstance(material, VideoMaterial):
            self.materials.videos.append(material)
        elif isinstance(material, AudioMaterial):
            self.materials.audios.append(material)
        else:
            raise TypeError("错误的素材类型: '%s'" % type(material))
        return self

    def add_segment(
        self: ScriptFileProtocol,
        segment: Union[VideoSegment, StickerSegment, AudioSegment, TextSegment],
        track: Optional[Union[str, TrackRef]] = None,
    ) -> "ScriptFile":
        """向指定轨道中添加一个片段

        Args:
            segment (`VideoSegment`, `StickerSegment`, `AudioSegment`, or `TextSegment`): 要添加的片段
            track (`str` or `TrackRef`, optional): 添加到的轨道名称或轨道引用.
                当此类型的轨道仅有一条时可省略.

        Raises:
            `NameError`: 未找到指定名称的轨道, 或必须提供`track`参数时未提供
            `ValueError`: 提供的 `TrackRef` 不属于当前 `ScriptFile`
            `TypeError`: 片段类型不匹配轨道类型
            `SegmentOverlap`: 新片段与已有片段重叠
        """
        target = self._get_track(type(segment), track)

        target.add_segment(segment)
        self.duration = max(self.duration, segment.end)

        if isinstance(segment, VideoSegment):
            if segment.animations_instance is not None and segment.animations_instance not in self.materials:
                self.materials.animations.append(segment.animations_instance)
            if segment.fade is not None and segment.fade not in self.materials:
                self.materials.audio_fades.append(segment.fade)
            for effect in segment.effects:
                if effect not in self.materials:
                    self.materials.video_effects.append(effect)
            for filter_ in segment.filters:
                if filter_ not in self.materials:
                    self.materials.filters.append(filter_)
            if segment.mix_mode is not None and segment.mix_mode not in self.materials:
                self.materials.mix_modes.append(segment.mix_mode)
            if segment.mask is not None:
                self.materials.masks.append(segment.mask.export_json())
            if segment.transition is not None and segment.transition not in self.materials:
                self.materials.transitions.append(segment.transition)
            if segment.background_filling is not None:
                self.materials.canvases.append(segment.background_filling)
            if segment.chroma is not None and segment.chroma not in self.materials:
                self.materials.chromas.append(segment.chroma)
            self.materials.speeds.append(segment.speed)
        elif isinstance(segment, StickerSegment):
            self.materials.stickers.append(segment.export_material())
        elif isinstance(segment, AudioSegment):
            if segment.fade is not None and segment.fade not in self.materials:
                self.materials.audio_fades.append(segment.fade)
            for effect in segment.effects:
                if effect not in self.materials:
                    self.materials.audio_effects.append(effect)
            self.materials.speeds.append(segment.speed)
        elif isinstance(segment, TextSegment):
            if segment.animations_instance is not None and segment.animations_instance not in self.materials:
                self.materials.animations.append(segment.animations_instance)
            if segment.bubble is not None:
                self.materials.filters.append(segment.bubble)
            if segment.effect is not None:
                self.materials.filters.append(segment.effect)
            self.materials.texts.append(segment.export_material())

        if isinstance(segment, (VideoSegment, AudioSegment)):
            self.add_material(segment.material_instance)

        return self

    def add_effect(
        self: ScriptFileProtocol,
        effect: Union[VideoSceneEffectType, VideoCharacterEffectType],
        t_range: Timerange,
        track_name: Optional[str] = None,
        *,
        params: Optional[List[Optional[float]]] = None,
    ) -> "ScriptFile":
        """向指定的特效轨道中添加一个特效片段

        Args:
            effect (`VideoSceneEffectType` or `VideoCharacterEffectType`): 特效类型
            t_range (`Timerange`): 特效片段的时间范围
            track_name (`str`, optional): 添加到的轨道名称. 当特效轨道仅有一条时可省略.
            params (`List[Optional[float]]`, optional): 特效参数列表, 参数列表中未提供或为None的项使用默认值.
                参数取值范围(0~100)与剪映中一致. 某个特效类型有何参数以及具体参数顺序以枚举类成员的annotation为准.

        Raises:
            `NameError`: 未找到指定名称的轨道, 或必须提供`track_name`参数时未提供
            `TypeError`: 指定的轨道不是特效轨道
            `ValueError`: 新片段与已有片段重叠、提供的参数数量超过了该特效类型的参数数量, 或参数值超出范围.
        """
        target = self._get_track(EffectSegment, track_name)
        segment = EffectSegment(effect, t_range, params)
        target.add_segment(segment)
        self.duration = max(self.duration, t_range.start + t_range.duration)

        if segment.effect_inst not in self.materials:
            self.materials.video_effects.append(segment.effect_inst)
        return self

    def add_filter(
        self: ScriptFileProtocol,
        filter_meta: FilterType,
        t_range: Timerange,
        track_name: Optional[str] = None,
        intensity: float = 100.0,
    ) -> "ScriptFile":
        """向指定的滤镜轨道中添加一个滤镜片段

        Args:
            filter_meta (`FilterType`): 滤镜类型
            t_range (`Timerange`): 滤镜片段的时间范围
            track_name (`str`, optional): 添加到的轨道名称. 当滤镜轨道仅有一条时可省略.
            intensity (`float`, optional): 滤镜强度(0-100). 仅当所选滤镜能够调节强度时有效. 默认为100.

        Raises:
            `NameError`: 未找到指定名称的轨道, 或必须提供`track_name`参数时未提供
            `TypeError`: 指定的轨道不是滤镜轨道
            `ValueError`: 新片段与已有片段重叠
        """
        target = self._get_track(FilterSegment, track_name)
        segment = FilterSegment(filter_meta, t_range, intensity / 100.0)
        target.add_segment(segment)
        self.duration = max(self.duration, t_range.end)

        self.materials.filters.append(segment.material)
        return self

    def import_srt(
        self: ScriptFileProtocol,
        srt_path: str,
        track_name: str,
        *,
        time_offset: Union[str, float] = 0.0,
        style_reference: Optional[TextSegment] = None,
        text_style: TextStyle = TextStyle(size=5, align=1, auto_wrapping=True),
        clip_settings: Optional[ClipSettings] = ClipSettings(transform_y=-0.8),
    ) -> "ScriptFile":
        """从SRT文件中导入字幕, 支持传入一个`TextSegment`作为样式参考

        注意: 默认不会使用参考片段的`clip_settings`属性, 若需要请显式为此函数传入`clip_settings=None`

        Args:
            srt_path (`str`): SRT文件路径
            track_name (`str`): 导入到的文本轨道名称, 若不存在则自动创建并插入到当前视频/文本轨的前景侧
            style_reference (`TextSegment`, optional): 作为样式参考的文本片段, 若提供则使用其样式.
            time_offset (`Union[str, float]`, optional): 字幕整体时间偏移, 单位为微秒, 默认为0.
            text_style (`TextStyle`, optional): 字幕样式, 默认模仿剪映导入字幕时的样式, 会被`style_reference`覆盖.
            clip_settings (`ClipSettings`, optional): 图像调节设置, 默认模仿剪映导入字幕时的设置, 会覆盖`style_reference`的设置除非指定为`None`.

        Raises:
            `ValueError`: 未提供样式参考时缺少 `clip_settings`
            `NameError`: 已存在同名轨道
            `TypeError`: 轨道类型不匹配
        """
        if style_reference is None and clip_settings is None:
            raise ValueError("未提供样式参考时请提供`clip_settings`参数")

        time_offset = tim(time_offset)
        if track_name not in self.tracks:
            track_list = self._list_all_tracks_in_order()
            insert_after: Optional[int] = None
            for index in range(len(track_list) - 1, -1, -1):
                if track_list[index].track_type in [TrackType.video, TrackType.text]:
                    insert_after = index
                    break
            if insert_after is None:
                self.append_track(TrackSpec(TrackType.text, track_name))
            else:
                self.insert_track(TrackSpec(TrackType.text, track_name), at_index=insert_after + 1)

        with open(srt_path, "r", encoding="utf-8-sig") as srt_file:
            lines = srt_file.readlines()

        def __add_text_segment(text: str, t_range: Timerange) -> None:
            if style_reference:
                seg = TextSegment.create_from_template(text, t_range, style_reference)
                if clip_settings is not None:
                    seg.clip_settings = deepcopy(clip_settings)
            else:
                seg = TextSegment(text, t_range, style=text_style, clip_settings=clip_settings)
            self.add_segment(seg, track_name)

        index = 0
        text = ""
        text_trange: Timerange
        read_state: Literal["index", "timestamp", "content"] = "index"
        while index < len(lines):
            line = lines[index].strip()
            if read_state == "index":
                if len(line) == 0:
                    index += 1
                    continue
                if not line.isdigit():
                    raise ValueError("Expected a number at line %d, got '%s'" % (index + 1, line))
                index += 1
                read_state = "timestamp"
            elif read_state == "timestamp":
                start_str, end_str = line.split(" --> ")
                start, end = srt_tstamp(start_str), srt_tstamp(end_str)
                text_trange = Timerange(start + time_offset, end - start)
                index += 1
                read_state = "content"
            elif read_state == "content":
                if len(line) == 0:
                    __add_text_segment(text.strip(), text_trange)
                    text = ""
                    read_state = "index"
                else:
                    text += line + "\n"
                index += 1

        if len(text) > 0:
            __add_text_segment(text.strip(), text_trange)

        return self
