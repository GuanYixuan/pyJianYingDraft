# pyJianYingDraft
### 轻量、灵活、易上手的Python剪映草稿文件生成工具
> **关于6+版本**：尽管剪映对`draft_content.json`文件进行了加密，但仍能正确读取本程序生成的草稿文件(当然读取后即被加密)

> 欢迎为本项目补充6+版本草稿文件的解密方式

# 特性清单
> 目前仅在5.9版本上进行测试

> 标注☑️的特性**已实现**，标注⬜的特性**待实现**，标注❔的特性**暂不在计划中**

### 模板模式
- ⬜ 加载（未加密的）`draft_content.json`文件作为模板
- ⬜ 替换音视频片段的素材

### 视频/图片
- ☑️ 添加本地视频/图片素材
- ❔ 添加**剪映提供的**视频/图片素材
- ☑️ 将视频/图片素材添加至轨道
  - ☑️ 截取素材中某部分，并自定义放置在轨道上的[时间、持续时长或播放速度](#素材截取与整体变速)
    - ❔ 曲线变速
- ☑️ [视频整体调节](#视频整体调节)（裁剪、旋转、翻转、缩放、透明度、亮度等）
- ☑️ 除裁剪外上述属性的[关键帧](#关键帧)生成
  - ❔ 关键帧曲线
- ☑️ 添加[蒙版](#蒙版)
  - ☑️ 蒙版参数
  - ❔ 蒙版参数的关键帧
- ☑️ 视频片段的[入场/出场/组合动画](#快速上手)（剪映右上角菜单）添加
- ☑️ 吸附在视频片段上的[特效](#片段特效滤镜)
  - ☑️ 特效参数
  - ❔ 特效参数的关键帧
- ☑️ 吸附在视频片段上的[滤镜](#片段特效滤镜)
  - ☑️ 滤镜强度
  - ❔ 滤镜强度的关键帧
### 贴纸
- ❔ 添加剪映的贴纸素材
### 音频
- ☑️ 添加本地音频素材
- ❔ 添加**剪映提供的**音频素材
- 将音频素材添加至轨道
  - ☑️ 截取素材中某部分，自定义放置在轨道上的[时间、持续时长或播放速度](#素材截取与整体变速)
    - ❔ 曲线变速
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
- ☑️ 位于**独立轨道的特效**
- ☑️ 位于**独立轨道的滤镜**
- ☑️ 添加[转场](#快速上手)
  - ☑️ 转场时长设置
### 文字
- ☑️ 添加普通文字
- ⬜ 设置一般文字格式
- ❔ 文字特效

# 用法速查
### 快速上手
下方的例子将创建包含音视频素材的剪映草稿文件，并且添加了音频淡入、视频入场动画和转场效果。
```python
# 导入模块
import os
import pyJianYingDraft as draft
from pyJianYingDraft import Intro_type, Transition_type, trange

tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')

# 创建剪映草稿
script = draft.Script_file(1080, 1080) # 1080x1080分辨率

# 添加一个音频轨道和一个视频轨道
script.add_track(draft.Track_type.audio).add_track(draft.Track_type.video)

# 从本地读取音视频素材和一个gif表情包
audio_material = draft.Audio_material(os.path.join(tutorial_asset_dir, 'audio.mp3'))
video_material = draft.Video_material(os.path.join(tutorial_asset_dir, 'video.mp4'))
sticker_material = draft.Video_material(os.path.join(tutorial_asset_dir, 'sticker.gif'))
script.add_material(audio_material).add_material(video_material).add_material(sticker_material) # 随手添加素材是好习惯

# 创建音频片段
audio_segment = draft.Audio_segment(audio_material,
                                    trange("0s", "5s"), # 片段将位于轨道上的0s-5s
                                    volume=0.6)         # 音量设置为60%(-4.4dB)
audio_segment.add_fade("1s", "0s")                      # 增加一个1s的淡入

# 创建视频片段
video_segment = draft.Video_segment(video_material, trange("0s", "4.2s")) # 片段将位于轨道上的0s-4.2s（取素材前4.2s内容）
video_segment.add_animation(Intro_type.斜切)                              # 添加一个入场动画“斜切”

sticker_segment = draft.Video_segment(sticker_material,
                                      trange(video_segment.end, sticker_material.duration)) # 紧跟上一片段，长度与gif一致

# 为二者添加一个转场
video_segment.add_transition(Transition_type.信号故障) # 注意转场添加在“前一个”视频片段上

# 将各片段添加到轨道中
script.add_segment(audio_segment).add_segment(video_segment).add_segment(sticker_segment)

# 保存草稿
script.dump("*你的草稿工程文件夹*/draft_content.json")
```
现在在剪映中打开草稿，你应该看到如下时间轴：

![快速上手](readme_assets/快速上手.png)

你可以仔细检查音频片段的音量设置、淡入效果时长以及视频片段的入场动画效果，看看是否符合上述代码的设置

### 时间相关设置

#### 时间格式
**剪映（和本package）内部均采用微秒为单位保存时间**，但这不便于输入，故我们增加了一种“字符串形式”的时间，大部分时间参数均同时支持这两种形式：
- 微秒形式：用`int`表达，适于计算
- 字符串形式：用`str`表达，如`"1.5s"`、`"1h3m12s"`等，易于输入

如果你希望显式地将字符串形式转换为微秒形式，可以使用`tim`函数；`trange`函数则是支持字符串形式输入的`Timerange`便捷构造函数。
例如：
```python
import pyJianYingDraft as draft
from pyJianYingDraft import SEC, tim, trange

# 1秒钟
assert 1000000 == SEC == tim("1s") == tim("0.01666667m")

# 0~1分钟
assert draft.Timerange(0, 60*SEC) == trange("0s", "1m") == trange("0s", "0.5m30s")

# 片段开始后2秒
seg: draft.Video_segment
assert seg.target_timerange.start + 2*SEC == seg.target_timerange.start + tim("2s")
```

#### 素材截取与整体变速
截取和变速均在`Segment`创建时设置完成，具体是通过`target_timerange`、`source_timerange`和`speed`参数来共同实现的。
> ℹ 目前暂不支持设置曲线变速

以下以`Video_segment`为例，`Audio_segment`的用法相同：
```python
import os
import pyJianYingDraft as draft
from pyJianYingDraft import trange

# 创建草稿文件及三个轨道
script = draft.Script_file(1080, 1080)
for i in range(3, 0, -1): # 倒序
    script.add_track(draft.Track_type.video, "%d" % i)

# 读取视频素材
tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
mat = draft.Video_material(os.path.join(tutorial_asset_dir, 'video.mp4'))
script.add_material(mat) # 随手添加素材是好习惯

# 视频素材长度为 5s
print("Video material length: %f s" % (mat.duration / 1e6))

# 不指定source_timerange，则自动从头截取素材等长片段
seg11 = draft.Video_segment(mat, trange("0s", "4s"))             # 自动截取素材的前4秒
seg2  = draft.Video_segment(mat, trange("0s", "4s"), speed=1.25) # 自动截取素材的前4*1.25=5秒
seg4  = draft.Video_segment(mat, trange("0s", "3s"), speed=3.0)  # 截取前3*3.0=9秒，素材不够长故报错

# 指定source_timerange，则截取素材的指定片段，自动设置速度
seg12 = draft.Video_segment(mat, trange("4s", "1s"),
                            source_timerange=trange(0, "4s"))    # 将素材在1s内放完，速度自动设置为5.0

# 同时指定source_timerange和speed，则截取素材的指定片段，并根据播放速度覆盖target_timerange的duration
seg3  = draft.Video_segment(mat, trange("1s", "66666h"),
                            source_timerange=trange(0, "5s"),
                            speed=2.0) # 将长5s的素材按2倍速放完，target_timerange的duration自动设为2.5s

# 将片段加入轨道
script.add_segment(seg11, "1").add_segment(seg12, "1")
script.add_segment(seg2, "2")
script.add_segment(seg3, "3")

# 保存草稿
script.dump("*你的草稿工程文件夹*/draft_content.json")
```

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
video_segment.add_keyframe(Keyframe_property.alpha, video_segment.duration - SEC, 1.0) # 结束前1s完全不透明
video_segment.add_keyframe(Keyframe_property.alpha, video_segment.duration, 0.0) # 片段结束时完全透明

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

### 蒙版
蒙版的添加非常简单：调用`Video_segment`的`add_mask`方法即可：
```python
from pyJianYingDraft import Mask_type

# 添加一个线性蒙版，中心点在素材的(100, 0)像素处，顺时针旋转45度
video_segment1.add_mask(Mask_type.线性, center_x=100, rotation=45)
# 添加一个圆形蒙版，直径占素材的50%
video_segment2.add_mask(Mask_type.圆形, size=0.5)
```
其中：
- `Mask_type`保存了剪映自带的蒙版类型
- `center_x`和`center_y`参数表示蒙版中心点的坐标，与剪映中意义一致
- `rotation`、`feather`、`round_corner`分别表示旋转、羽化、圆角参数，与剪映中意义一致
- `size`参数表示蒙版的“主要尺寸”（镜面的可视部分高度/圆形直径/爱心高度等）占素材的比例

更具体的参数说明请参见`add_mask`方法的注释。

### 片段特效/滤镜
> 本节介绍的是**吸附在音频/视频片段上**的特效及滤镜

#### 特效及滤镜类型
目前支持的特效类型由以下枚举类定义：
- 音频：`Audio_scene_effect_type`（场景音）、`Tone_effect_type`（音色）、`Speech_to_song_type`（声音成曲，此类效果**目前不能自动触发剪映生成相应文件**）
- 视频：`Video_scene_effect_type`（画面特效）、`Video_character_effect_type`（人物特效）

滤镜类型则保存在`Filter_type`中

枚举类中的成员（通常）直接**以特效或滤镜的名字命名**，并注释了相应参数，例如：

![特效类型](readme_assets/片段特效_annotation.jpg)

你也可以使用`from_name`方法来获取特效/滤镜成员，其忽略大小写、空格和下划线，例如：

```python
assert Video_scene_effect_type.from_name("__全息 扫描__") == Video_scene_effect_type.全息扫描
```

#### 添加特效
添加特效使用的方法是`add_effect`，它接受特效类型和一个参数数组，参数数组的顺序**与特效类型注释中的参数顺序一致**，但**不一定与剪映内的参数顺序一致**。

下方的例子为视频片段添加一个`全息扫描`特效，并且指定其`氛围`参数为（剪映中的）100，其余参数默认：
```python
from pyJianYingDraft import Video_scene_effect_type

video_segment.add_effect(Video_scene_effect_type.全息扫描,
                         [None, None, 100.0]) # 不设置前两个参数, 第三个参数（氛围）为100，其余参数也不设置
```
音频片段的特效添加方法与视频片段相似

#### 添加滤镜
滤镜的添加方法与特效类似，其使用的是`add_filter`方法。与特效不同的是，滤镜只支持一个“滤镜强度”参数，且**不是所有滤镜都支持设置强度**。

```python
from pyJianYingDraft import Filter_type

video_segment1.add_filter(Filter_type.原生肤, 10) # 设置"原生肤"强度为10
video_segment2.add_filter(Filter_type.冰雪世界, 50) # 这会产生一个警告，因为"冰雪世界"不支持设置强度
```
