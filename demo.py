# 导入模块
import os
import pyJianYingDraft as draft
from pyJianYingDraft import Intro_type, Transition_type, trange

# 保存路径
DUMP_PATH = r"<你的草稿文件夹>/draft_content.json"
assert os.path.exists(DUMP_PATH), f"未找到草稿文件{os.path.abspath(DUMP_PATH)}"

tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
assert os.path.exists(tutorial_asset_dir), f"未找到例程素材文件夹{os.path.abspath(tutorial_asset_dir)}"

# 创建剪映草稿
script = draft.Script_file(1920, 1080)  # 1920x1080分辨率

# 添加音频、视频和文本轨道
script.add_track(draft.Track_type.audio).add_track(draft.Track_type.video).add_track(draft.Track_type.text)

# 从本地读取音视频素材和一个gif表情包
audio_material = draft.Audio_material(os.path.join(tutorial_asset_dir, 'audio.mp3'))
video_material = draft.Video_material(os.path.join(tutorial_asset_dir, 'video.mp4'))
sticker_material = draft.Video_material(os.path.join(tutorial_asset_dir, 'sticker.gif'))

# 创建音频片段
audio_segment = draft.Audio_segment(audio_material,
                                    trange("0s", "5s"),  # 片段将位于轨道上的0s-5s（注意5s表示持续时长而非结束时间）
                                    volume=0.6)          # 音量设置为60%(-4.4dB)
audio_segment.add_fade("1s", "0s")                       # 增加一个1s的淡入

# 创建视频片段
video_segment = draft.Video_segment(video_material, trange("0s", "4.2s"))  # 片段将位于轨道上的0s-4.2s（取素材前4.2s内容，注意此处4.2s表示持续时长）
video_segment.add_animation(Intro_type.斜切)                               # 添加一个入场动画“斜切”

sticker_segment = draft.Video_segment(sticker_material,
                                      trange(video_segment.end, sticker_material.duration))  # 紧跟上一片段，长度与gif一致

# 为二者添加一个转场
video_segment.add_transition(Transition_type.信号故障)  # 注意转场添加在“前一个”视频片段上

# 将上述片段添加到轨道中
script.add_segment(audio_segment).add_segment(video_segment).add_segment(sticker_segment)

# 创建一行类似字幕的文本片段并添加到轨道中
text_segment = draft.Text_segment("据说pyJianYingDraft效果还不错?", trange(0, script.duration),  # 文本将持续整个视频（注意script.duration在上方片段添加到轨道后才会自动更新）
                                  font=draft.Font_type.文轩体,                                  # 设置字体为文轩体
                                  style=draft.Text_style(color=(1.0, 1.0, 0.0)),                # 设置字体颜色为黄色
                                  clip_settings=draft.Clip_settings(transform_y=-0.8))          # 模拟字幕的位置
script.add_segment(text_segment)

# 保存草稿（覆盖掉原有的draft_content.json）
script.dump(DUMP_PATH)
