# pyJianYingDraft
### 轻量化、易用的Python剪映草稿文件生成工具
> **关于6+版本**：尽管剪映对`draft_content.json`文件进行了加密，但仍能正确读取本程序生成的草稿文件(当然读取后即被加密)

# 特性清单
> 目前仅在5.9版本上进行测试
> 标注☑️的特性**已实现**，标注⬜的特性**待实现**，标注❔的特性**还要一段时间**

### 视频/图片
- ☑️ 添加本地视频/图片素材
- ❔ 添加**剪映提供的**视频/图片素材
- 将视频/图片素材添加至轨道
  - ☑️ 自定义放置在轨道上的**时间、持续时长或播放速度**
  - ☑️ 自定义**截取**其中某个片段
  - ☑️ [视频整体调节](#视频整体调节)（裁剪、旋转、翻转、缩放、透明度、亮度等）
  - ☑️ 除裁剪外上述属性的[关键帧](#关键帧)生成
    - ❔ 关键帧曲线
  - ☑️ 视频片段的**入场/出场/组合动画**（剪映右上角菜单）添加及其时长修改
  - ☑️ 吸附在视频片段上的[特效](#片段特效)
    - ☑️ 特效的参数设置
    - ❔ 特效参数的关键帧
  - ⬜ 吸附在视频片段上的**滤镜**
    - ⬜ 滤镜参数设置
    - ❔ 滤镜参数的关键帧
### 贴纸
- ⬜ 添加剪映的贴纸素材
### 音频
- ☑️ 添加本地音频素材
- ❔ 添加**剪映提供的**音频素材
- 将音频素材添加至轨道
  - ☑️ 自定义放置在轨道上的**时间、持续时长或播放速度**
  - ☑️ 自定义**截取**其中某个片段
  - ☑️ 调整[音量、淡入淡出时长](#快速上手)
  - ☑️ 音量的[关键帧](#关键帧)生成
  - ☑️ 音频片段的[音色、场景音效果](#片段特效)（剪映右上角菜单）添加
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
### 字幕

# 用法速查
### 快速上手
下方的例子将创建包含音频素材和视频素材各一个的剪映草稿文件，并且添加了音频淡入效果和视频组合动画。
```python
# 导入模块
import os
import pyJianYingDraft as draft
from pyJianYingDraft import Group_animation_type, trange

tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')

# 创建剪映草稿
script = draft.Script_file(1080, 1080) # 1080x1080分辨率

# 添加一个音频轨道和一个视频轨道
script.add_track(draft.Track_type.audio).add_track(draft.Track_type.video)

# 从本地读取一个音频素材和一个视频素材
audio_material = draft.Audio_material(os.path.join(tutorial_asset_dir, 'audio.mp3'))
video_material = draft.Video_material(os.path.join(tutorial_asset_dir, 'video.mp4'))
script.add_material(audio_material).add_material(video_material) # 随手添加素材是好习惯

# 创建一个音频片段
audio_segment = draft.Audio_segment(audio_material,
                                    trange("0s", "5s"), # 片段将位于轨道上的0s-5s
                                    volume=0.6)         # 音量设置为60%(-4.4dB)
audio_segment.add_fade("1s", "0s") # 增加一个1s的淡入

# 创建一个视频片段
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

### 视频整体调节
每个视频片段都可以单独设置裁剪、旋转、翻转、缩放、透明度、亮度等属性，这些设置通过`Video_segment`构造函数中的`clip_settings`参数传入
> ℹ 关键帧的优先级高于整体调节，故前者会覆盖后者的相应设置

下方的例子将创建一个视频片段，并设置其不透明度为0.5、打开水平翻转：
```python
from pyJianYingDraft import Clip_settings
video_segment = draft.Video_segment(video_material,
                                    draft.Timerange(0, video_material.duration),      # 与素材等长
                                    clip_settings=Clip_settings(alpha=0.5,            # 不透明度为0.5
                                                                flip_horizontal=True) # 打开水平翻转
                                    )
```

### 关键帧
关键帧是吸附在**片段**上的“时刻-数值”对，所以创建关键帧只需要在`add_keyframe`方法中指定**相对片段头部的**时刻、数值以及控制的属性即可。
> ℹ 目前不支持设置特效或滤镜参数的关键帧

下方的例子尝试使用两个不透明度关键帧模拟视频的淡出效果：
```python
import os
import pyJianYingDraft as draft
from pyJianYingDraft import Keyframe_property, SEC

# 创建草稿及视频轨道
script = draft.Script_file(1080, 1080)
script.add_track(draft.Track_type.video)
tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')

# 创建视频片段
video_material = draft.Video_material(os.path.join(tutorial_asset_dir, 'video.mp4'))
video_segment = draft.Video_segment(video_material,
                                    draft.Timerange(0, video_material.duration)) # 与素材等长

# 添加两个不透明度关键帧形成1s的淡出效果
video_segment.add_keyframe(Keyframe_property.alpha, video_material.duration - SEC, 1.0) # 结束前1s完全不透明
video_segment.add_keyframe(Keyframe_property.alpha, video_material.duration, 0.0) # 片段结束时完全透明

# 添加素材及片段
script.add_material(video_material)
script.add_segment(video_segment)

# 保存草稿
script.dump("*你的草稿工程文件夹*/draft_content.json")
```

除了`alpha`外，`Keyframe_property`中还有平移、旋转、缩放、音量、饱和度等属性，它们都可以设置关键帧。

对音频片段，目前只能设置音量的关键帧，此时你不需要指定`Keyframe_property`
```python
audio_segment: draft.Audio_segment
audio_segment.add_keyframe("0s", 0.6) # 片段开始时的音量为60%
```

### 片段特效
> 本节介绍的是**吸附在音频/视频片段上**的特效

#### 特效类型
目前支持的特效类型由以下枚举类定义：
- 音频：`Audio_scene_effect_type`（场景音）、`Tone_effect_type`（音色）、`Speech_to_song_type`（声音成曲，此类效果目前不能自动触发剪映生成相应文件）
- 视频：`Video_scene_effect_type`（画面特效）、`Video_character_effect_type`（人物特效）

而枚举类中的成员（通常）直接**以特效的名字命名**，并注释了相应参数，例如：

![特效类型](readme_assets/片段特效_annotation.jpg)

你也可以使用`from_name`方法来获取特效类型，其忽略大小写、空格和下划线，例如：

```python
assert Video_scene_effect_type.from_name("__全息 扫描__") == Video_scene_effect_type.全息扫描
```

#### 为片段添加特效
添加特效使用的方法是`add_effect`，它接受特效类型和一个参数数组，参数数组的顺序**与特效类型注释中的参数顺序一致**，但**不一定与剪映内的参数顺序一致**。

下方的例子为视频片段添加一个`全息扫描`特效，并且指定其`氛围`参数为（剪映中的）100，其余参数默认：
```python
video_segment: draft.Video_segment
video_segment.add_effect(Video_scene_effect_type.全息扫描,
                         [None, None, 100.0]) # 不设置前两个参数, 第三个参数（氛围）为100，其余参数也不设置
```
音频片段的特效添加方法与视频片段相似
