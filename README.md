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

### 视频与图片
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
- ☑️ [添加轨道](#多轨道操作)
- ☑️ 将片段添加到[指定轨道](#多轨道操作)
- ☑️ 自定义视频/滤镜/特效轨道的[层级关系](#多轨道操作)
### 特效、滤镜和转场
- ☑️ 位于**独立轨道的特效**
- ☑️ 位于**独立轨道的滤镜**
- ☑️ 添加[转场](#快速上手)
  - ☑️ 转场时长设置
### 文本及字幕
- ☑️ 添加[普通文本](#添加文本)
- ☑️ 设置基础[字体样式](#添加文本)
- ☑️ 文本[位置及旋转设置](#视频整体调节)
- ☑️ [导入`.srt`文件](#导入字幕)生成字幕
- ❔ 文本特效

# 用法速查
### 快速上手
下方的例子将创建包含音视频素材和一行字幕的剪映草稿文件，并且添加了音频淡入、视频入场动画和转场效果。

这个例子的操作方法如下：
1. 在剪映里**创建一个空草稿**，找到它对应的**文件夹路径**（类似`.../JianyingPro Drafts/9月5日`）
2. **返回剪映首页**或退出剪映
3. 将下方代码**保存到项目文件夹根目录**下（即与此`README.md`同级）
4. 将代码中最后一行`dump`的**保存路径改为草稿文件夹下的`draft_content.json`路径**，随后运行代码
```python
# 导入模块
import os
import pyJianYingDraft as draft
from pyJianYingDraft import Intro_type, Transition_type, trange

tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')

# 创建剪映草稿
script = draft.Script_file(1080, 1080) # 1080x1080分辨率

# 添加音频、视频和文本轨道
script.add_track(draft.Track_type.audio).add_track(draft.Track_type.video).add_track(draft.Track_type.text)

# 从本地读取音视频素材和一个gif表情包
audio_material = draft.Audio_material(os.path.join(tutorial_asset_dir, 'audio.mp3'))
video_material = draft.Video_material(os.path.join(tutorial_asset_dir, 'video.mp4'))
sticker_material = draft.Video_material(os.path.join(tutorial_asset_dir, 'sticker.gif'))
script.add_material(audio_material).add_material(video_material).add_material(sticker_material) # 随手添加素材是好习惯

# 创建音频片段
audio_segment = draft.Audio_segment(audio_material,
                                    trange("0s", "5s"), # 片段将位于轨道上的0s-5s（注意5s表示持续时长而非结束时间）
                                    volume=0.6)         # 音量设置为60%(-4.4dB)
audio_segment.add_fade("1s", "0s")                      # 增加一个1s的淡入

# 创建视频片段
video_segment = draft.Video_segment(video_material, trange("0s", "4.2s")) # 片段将位于轨道上的0s-4.2s（取素材前4.2s内容，注意此处4.2s表示持续时长）
video_segment.add_animation(Intro_type.斜切)                              # 添加一个入场动画“斜切”

sticker_segment = draft.Video_segment(sticker_material,
                                      trange(video_segment.end, sticker_material.duration)) # 紧跟上一片段，长度与gif一致

# 为二者添加一个转场
video_segment.add_transition(Transition_type.信号故障) # 注意转场添加在“前一个”视频片段上

# 将上述片段添加到轨道中
script.add_segment(audio_segment).add_segment(video_segment).add_segment(sticker_segment)

# 创建一行类似字幕的文本片段并添加到轨道中
text_segment = draft.Text_segment("据说pyJianYingDraft效果还不错?", trange(0, script.duration), # 文本将持续整个视频（注意script.duration在上方片段添加到轨道后才会自动更新）
                                  style=draft.Text_style(color=(1.0, 1.0, 0.0)),                # 设置字体颜色为黄色
                                  clip_settings=draft.Clip_settings(transform_y=-0.8))          # 模拟字幕的位置
script.add_segment(text_segment)

# 保存草稿（覆盖掉原有的draft_content.json）
script.dump("<你的草稿文件夹>/draft_content.json")
```
5. 现在在剪映中**重新打开这个草稿**，你应该看到如下时间轴：

![快速上手](readme_assets/快速上手.png)

你可以仔细检查音频片段的音量设置、淡入效果时长以及视频片段的入场动画效果，看看是否符合上述代码的设置

### 时间与轨道

#### 时间格式
**剪映（和本package）内部均采用微秒为单位保存时间**，但这不便于输入，故我们增加了一种“字符串形式”的时间，大部分时间参数均同时支持这两种形式：
- 微秒形式：用`int`表达，适于计算
- 字符串形式：用`str`表达，如`"1.5s"`、`"1h3m12s"`等，易于输入

如果你希望显式地将字符串形式转换为微秒形式，可以使用`tim`函数；`trange`函数则是支持字符串形式输入的`Timerange`便捷构造函数。

> ⚠️注意`trange`的第二个参数是**持续时长**，而不是结束时间

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
from pyJianYingDraft import trange, SEC

# 创建草稿文件及三个轨道
script = draft.Script_file(1080, 1080)
for i in range(3, 0, -1): # 倒序
    script.add_track(draft.Track_type.video, "%d" % i)

# 读取视频素材
tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
mat = draft.Video_material(os.path.join(tutorial_asset_dir, 'video.mp4'))
script.add_material(mat) # 随手添加素材是好习惯

# 视频素材长度为 5s
print("Video material length: %f s" % (mat.duration / SEC))

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

#### 多轨道操作
目前`Script_file.add_track`方法已支持创建多个同类型轨道，并支持自定义其顺序：
```python
script.add_track(draft.Track_type.video,
                 track_name="前景",       # 轨道名
                 relative_index=2)        # 在所有视频轨道中的相对位置
script.add_track(draft.Track_type.video,
                 track_name="背景",
                 relative_index=1)        # 由于1<2，所以前景轨道位于更上方
```

一旦创建了多个同类轨道，则在添加片段时必须指定目标轨道，例如：
```python
script.add_segment(video_segment, "背景")
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

更具体的参数说明可参见`Clip_settings`的构造函数。

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

### 片段特效和滤镜
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

### 文本及字幕
#### 添加文本
添加文本与添加视频/音频片段类似，只需创建`Text_segment`对象并利用`add_segment`添加到`Script_file`中即可。
其**文字样式**及**图像调节**设置可分别通过`style`和`clip_settings`参数设置。

例如：
```python
import pyJianYingDraft as draft
from pyJianYingDraft import Text_style, Clip_settings

# 带下划线、位置及大小类似字幕的浅蓝色文本
seg1 = draft.Text_segment("Subtitle", trange("0s", "10s"),
                          style=Text_style(size=5.0, color=(0.7, 0.7, 1.0), underline=True, align=1),
                          clip_settings=Clip_settings(transform_y=-0.8))
```

更具体的参数说明可参见`Text_style`和`Clip_settings`的构造函数。

#### 导入字幕
> ℹ 目前只支持导入**SRT格式**的字幕文件

导入字幕本质上是根据每条字幕的时间戳及内容创建一系列文本，并添加到轨道中。这一过程通过`Script_file.import_srt`来实现。
上述方法同样支持`text_style`和`clip_settings`参数，还支持指定`time_offset`参数来对字幕进行整体时间偏移。

例如：
```python
import pyJianYingDraft as draft

script = draft.Script_file(1080, 1080)

# 将字幕导入到名为"subtitle"的轨道中，若轨道不存在将自动创建
# 不指定style和clip_settings，则默认模拟剪映导入字幕时的样式
script.import_srt("subtitle.srt", track_name="subtitle")
```

`text_style`和`clip_settings`参数的意义与`Text_segment()`中的相同。
