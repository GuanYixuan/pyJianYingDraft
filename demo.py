# 导入模块
import os
import pyJianYingDraft as draft
from pyJianYingDraft import IntroType, TransitionType, trange, trange_seconds, tim

# 设置草稿文件夹
draft_folder = draft.DraftFolder(r"<你的草稿文件夹>")

tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
assert os.path.exists(tutorial_asset_dir), f"未找到例程素材文件夹{os.path.abspath(tutorial_asset_dir)}"

# 创建剪映草稿
script = draft_folder.create_draft("demo", 1920, 1080, allow_replace=True)  # 1920x1080分辨率

# 按从背景到前景的顺序创建轨道；append_tracks 遵循“后来居上”
script.append_tracks([
    draft.TrackSpec(draft.TrackType.audio, "bgm"),          # 音频不参与视觉前后景，但也按追加顺序创建
    draft.TrackSpec(draft.TrackType.video, "main_video"),
    draft.TrackSpec(draft.TrackType.text, "caption"),
])

# 创建音频片段
audio_segment = draft.AudioSegment(os.path.join(tutorial_asset_dir, 'audio.mp3'),
                                   trange_seconds(0, duration=5),  # 片段将位于轨道上的0s-5s
                                   volume=0.6)          # 音量设置为60%(-4.4dB)
audio_segment.add_fade("1s", "0s")                      # 增加一个1s的淡入

# 创建视频片段
video_segment = draft.VideoSegment(os.path.join(tutorial_asset_dir, 'video.mp4'),
                                   trange_seconds(0, duration=4.2))  # 片段位于0s-4.2s，截取素材前4.2s内容
video_segment.add_animation(IntroType.斜切)               # 添加一个入场动画"斜切"

# 创建贴纸片段，由于需要读取素材长度，先创建素材实例
gif_material = draft.VideoMaterial(os.path.join(tutorial_asset_dir, 'sticker.gif'))
# video_segment.end和gif_material.duration均为内部微秒值，直接使用trange
gif_segment = draft.VideoSegment(gif_material,
                                 trange(video_segment.end, gif_material.duration))  # 紧跟上一片段，长度与gif一致
gif_segment.add_background_filling("blur", 0.0625)  # 添加一个模糊背景填充效果, 模糊程度等同于剪映中第一档

# 为二者添加一个转场
video_segment.add_transition(TransitionType.信号故障)  # 注意转场添加在“前一个”视频片段上

# 将上述片段添加到对应轨道中
script.add_segment(audio_segment, "bgm").add_segment(video_segment, "main_video").add_segment(gif_segment, "main_video")

# 创建一个带气泡效果的文本片段并添加到轨道中
text_segment = draft.TextSegment(
    "据说pyJianYingDraft效果还不错?", video_segment.target_timerange,  # 文本片段的首尾与主视频片段一致
    font=draft.FontType.文轩体,                                       # 设置字体为文轩体
    style=draft.TextStyle(color=(1.0, 1.0, 0.0)),                    # 字体颜色为黄色（实际上被花字覆盖）
    clip_settings=draft.ClipSettings(transform_y=-0.8)               # 位置在屏幕下方
)
text_segment.add_animation(draft.TextOutro.故障闪动, duration=tim("1s"))  # 添加出场动画“故障闪动”, 设置时长为1s
text_segment.add_bubble("361595", "6742029398926430728")                  # 添加文本气泡效果, 相应素材元数据的获取参见readme中"提取素材元数据"部分
text_segment.add_effect("7296357486490144036")                            # 添加花字效果, 相应素材元数据的获取参见readme中"提取素材元数据"部分
script.add_segment(text_segment, "caption")                               # 加到caption轨道中

# 保存草稿
script.save()
