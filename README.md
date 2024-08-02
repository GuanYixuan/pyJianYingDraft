# pyJianYingDraft
### 轻量化、易用的Python剪映草稿文件生成工具
> **关于6+版本**：尽管剪映对`draft_content.json`文件进行了加密，但仍能读取本程序生成的草稿文件(当然读取后即被加密)

# 特性清单
> 目前仅在5.9版本上进行测试
> 标注☑️的特性**已实现**，标注⬜的特性**待实现**，标注❔的特性**还要一段时间**

### 视频/图片
- ☑️ 添加本地视频/图片素材
- ❔ 添加**剪映提供的**视频/图片素材
- 将视频/图片素材添加至轨道
  - ☑️ 自定义放置在轨道上的**时间、持续时长或播放速度**
  - ☑️ 自定义**截取**其中某个片段
  - ☑️ 视频**整体调节**（裁剪、旋转、翻转、缩放、透明度、亮度等）
  - ☑️ 除裁剪外上述属性的**关键帧**生成
    - ❔ 关键帧曲线
  - ☑️ 视频片段的**入场/出场/组合动画**（剪映右上角菜单）添加及其时长修改
  - ☑️ 吸附在视频片段上的**特效**
    - ☑️ 特效的参数设置
    - ❔ 特效参数的关键帧
  - ⬜ 吸附在视频片段上的**滤镜**
    - ⬜ 滤镜参数设置
    - ❔ 滤镜参数的关键帧
### 音频
- ☑️ 添加本地音频素材
- ❔ 添加**剪映提供的**音频素材
- 将音频素材添加至轨道
  - ☑️ 自定义放置在轨道上的**时间、持续时长或播放速度**
  - ☑️ 自定义**截取**其中某个片段
  - ☑️ 调整**音量、淡入淡出**时长
  - ☑️ 音量的**关键帧**生成
  - ☑️ 音频片段的**音色、场景音**效果（剪映右上角菜单）添加
    - ☑️ 效果的参数设置
    - ❔ 效果参数的关键帧
  - ❔ 自动触发**声音成曲**效果的文件生成
### 轨道
- ☑️ 添加轨道
- ☑️ 将片段添加到指定轨道
  - 附带片段重叠检查
- ⬜ 完全自定义轨道**层级关系**
### 特效类
- ⬜ 位于**独立轨道的特效**
- ☑️ 位于**独立轨道的滤镜**
- ☑️ 添加**转场**
  - ☑️ 转场时长设置
### 文字
- ❔ 添加文字
- ❔ 文字特效
### ❔ 字幕

# 用法速查
### 快速上手
以下Python代码将创建包含音频素材和视频素材各一个的剪映草稿文件，并且添加了音频淡入效果和视频组合动画。
```python
# 导入模块
import os
import pyJianYingDraft as draft
from pyJianYingDraft import Group_animation_type, trange

tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')

# 创建剪映脚本
script = draft.Draft_file(1080, 1080) # 1080x1080分辨率

# 添加一个音频轨道和一个视频轨道
script.add_track(draft.Track_type.audio).add_track(draft.Track_type.video)

# 从本地读取一个音频素材和一个视频素材
audio_material = draft.Audio_material(os.path.join(tutorial_asset_dir, 'audio.mp3'))
video_material = draft.Video_material(os.path.join(tutorial_asset_dir, 'video.mp4'))
script.add_material(audio_material).add_material(video_material) # 随手添加素材是好习惯

# 用音频素材创建一个音频片段
audio_segment = draft.Audio_segment(audio_material,
                                    trange("0s", "5s"), # 片段将位于轨道上的0s-5s
                                    volume=0.6)         # 音量设置为60%(-4.4dB)
audio_segment.add_fade("1s", "0s") # 增加一个1s的淡入

# 用视频素材创建一个视频片段
video_segment = draft.Video_segment(video_material, trange("0s", "5s")) # 片段将位于轨道上的0s-5s
video_segment.add_animation(Group_animation_type.缩放)                  # 添加一个组合动画“缩放”

# 将两个片段添加到轨道中
script.add_segment(audio_segment).add_segment(video_segment)

# 保存草稿
script.dump("*你的草稿工程文件夹*/draft_content.json")
```
现在在剪映中打开草稿，你应该看到如下时间轴：
![快速上手](readme_assets/快速上手.png)
你可以仔细检查音频片段的音量设置、淡入效果时长以及视频片段的组合动画效果，看看是否符合上述代码的设置
