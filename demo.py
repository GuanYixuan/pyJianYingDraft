# 导入模块
import os
import pyJianYingDraft as draft
from pyJianYingDraft import IntroType, TransitionType, trange, tim

# 设置草稿文件夹
draft_folder = draft.DraftFolder(r"<你的草稿文件夹>")

tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
assert os.path.exists(tutorial_asset_dir), f"未找到例程素材文件夹{os.path.abspath(tutorial_asset_dir)}"

# 创建剪映草稿
script = draft_folder.create_draft("demo", 1920, 1080)  # 1920x1080分辨率

# 添加音频、视频和文本轨道
script.add_track(draft.TrackType.audio).add_track(draft.TrackType.video).add_track(draft.TrackType.text)

# 创建音频片段（使用便捷构造，直接传入素材路径）
audio_segment = draft.AudioSegment(os.path.join(tutorial_asset_dir, 'audio.mp3'),
                                   trange("0s", "5s"),  # 片段将位于轨道上的0s-5s（注意5s表示持续时长而非结束时间）
                                   volume=0.6)          # 音量设置为60%(-4.4dB)
audio_segment.add_fade("1s", "0s")                      # 增加一个1s的淡入

# 创建视频片段（使用便捷构造，直接传入素材路径）
video_segment = draft.VideoSegment(os.path.join(tutorial_asset_dir, 'video.mp4'),
                                   trange("0s", "4.2s"))  # 片段将位于轨道上的0s-4.2s（取素材前4.2s内容，注意此处4.2s表示持续时长）
video_segment.add_animation(IntroType.斜切)               # 添加一个入场动画"斜切"

# 创建贴纸片段，由于需要读取素材长度，先创建素材实例
gif_material = draft.VideoMaterial(os.path.join(tutorial_asset_dir, 'sticker.gif'))
gif_segment = draft.VideoSegment(gif_material,
                                 trange(video_segment.end, gif_material.duration))  # 紧跟上一片段，长度与gif一致
gif_segment.add_background_filling("blur", 0.0625)  # 添加一个模糊背景填充效果, 模糊程度等同于剪映中第一档

# 为二者添加一个转场
video_segment.add_transition(TransitionType.信号故障)  # 注意转场添加在“前一个”视频片段上

# 将上述片段添加到轨道中
script.add_segment(audio_segment).add_segment(video_segment).add_segment(gif_segment)

# 创建一个带气泡效果的文本片段并添加到轨道中
text_segment = draft.TextSegment(
    "据说pyJianYingDraft效果还不错?", video_segment.target_timerange,  # 文本片段的首尾与上方视频片段一致
    font=draft.FontType.文轩体,                                       # 设置字体为文轩体
    style=draft.TextStyle(color=(1.0, 1.0, 0.0)),                    # 字体颜色为黄色
    clip_settings=draft.ClipSettings(transform_y=-0.8)               # 位置在屏幕下方
)
text_segment.add_animation(draft.TextOutro.故障闪动, duration=tim("1s"))  # 添加出场动画“故障闪动”, 设置时长为1s
text_segment.add_bubble("361595", "6742029398926430728")                  # 添加文本气泡效果, 相应素材元数据的获取参见readme中"提取素材元数据"部分
text_segment.add_effect("7296357486490144036")                            # 添加花字效果, 相应素材元数据的获取参见readme中"提取素材元数据"部分
script.add_segment(text_segment)

# 保存草稿
script.save()
