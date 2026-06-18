<!-- Generated from README.md by tools/generate_pypi_readme.py. Do not edit directly. -->

# pyJianYingDraft
### 轻量、灵活、易上手的Python剪映草稿生成及导出工具，构建全自动视频剪辑/混剪流水线！

> 🧪 本项目的**CapCut版本**正在开发中，欢迎关注[CapCut版本仓库](https://github.com/GuanYixuan/pyCapCut)

> 📢 欢迎加入[Discord服务器](https://discord.gg/WfHgGQvhyW)进行用法或新功能的讨论

## 使用思路
![使用思路](https://github.com/GuanYixuan/pyJianYingDraft/raw/main/readme_assets/%E4%BD%BF%E7%94%A8%E6%80%9D%E8%B7%AF.jpg)

# 功能清单
> ℹ 如未额外注明，一般仅在5.9版本上测试过

> 标注☑️的特性**已实现**，标注⬜的特性**待实现**

### 模板模式
> ⚠️ 剪映6+版本对`draft_content.json`文件进行了加密；当前已内置本地解密逻辑，会在加载模板时自动尝试解密。

> ℹ 本地解密依赖`cryptography`。若遇到暂不兼容的新格式，仍可传入自定义解密器或第三方解密接口API Key作为兜底；使用第三方接口会上传草稿文件内容，请确认数据风险后再启用。

- ☑️ 加载未加密或剪映6+加密的`draft_content.json`文件作为模板
- ☑️ 替换音视频片段的素材
- ☑️ 修改文本片段的文本内容
- ☑️ 将模板草稿中的音视频/文本轨道整体导入到另一草稿中
- ☑️ 提取模板中出现的贴纸/气泡/花字等元信息

### 批量导出
> ⚠️ 剪映7+版本隐藏了控件，故**本系列功能目前仅支持剪映6及以下版本**

- ☑️ 控制剪映打开指定草稿
- ☑️ 导出草稿至指定位置
- ☑️ 调节导出分辨率和帧率

### 视频与图片
> ℹ 以下草稿生成功能（音视频、贴纸、文本、特效等）**支持剪映5及以上的所有版本**

- ☑️ 添加本地视频/图片素材，并自定义片段的时间、持续时长或播放速度
- ☑️ 视频片段的音频淡入淡出效果
- ☑️ 视频整体调节（旋转、缩放、亮度等）以及关键帧生成
- ☑️ 视频片段的入场/出场/组合动画
- ☑️ 添加蒙版、片段特效和滤镜
- ☑️ （项目700⭐️回馈功能）视频背景填充[(示例代码)](https://github.com/GuanYixuan/pyJianYingDraft/blob/main/demo.py)
- ☑️ （项目2k⭐️回馈功能）视频混合模式（正片叠底、滤色、叠加等）
### 贴纸
- ☑️ 根据元信息添加贴纸
- ☑️ 贴纸的关键帧生成
### 音频
- ☑️ 添加本地音频素材，并自定义片段的时间、持续时长或播放速度
- ☑️ 调整淡入淡出时长[(示例代码)](https://github.com/GuanYixuan/pyJianYingDraft/blob/main/demo.py)，调整音量[(示例代码)](https://github.com/GuanYixuan/pyJianYingDraft/blob/main/demo.py)及其关键帧
- ☑️ 添加音频片段的场景音效果，并设置参数
### 轨道
- ☑️ 添加轨道以及将片段添加到指定轨道
- ☑️ 自定义视频/滤镜/特效轨道的层级关系
### 特效、滤镜和转场
- ☑️ 吸附于片段上的特效、滤镜和动画
- ☑️ 位于独立轨道的特效和滤镜
- ☑️ 添加转场[(示例代码)](https://github.com/GuanYixuan/pyJianYingDraft/blob/main/demo.py)，并自定义其时长
### 文本及字幕
- ☑️ 添加文本、设置字体及样式、修改文本片段的位置及旋转设置
- ☑️ 文本的关键帧以及动画
- ☑️ 文字描边、背景和阴影
- ☑️ 文字气泡效果和花字效果[(示例代码)](https://github.com/GuanYixuan/pyJianYingDraft/blob/main/demo.py)
- ☑️ 文本自动换行，支持设置最大行宽
- ☑️ 导入`.srt`文件生成字幕并批量设置格式

# 安装
pyJianYingDraft现已支持pip安装（不含demo），推荐使用开发时测试的Python版本3.8或3.11
```
pip install pyJianYingDraft
```

> ℹ 关于剪映5.9版本的自动升级问题，可参见[相关issue](https://github.com/GuanYixuan/pyJianYingDraft/issues/115)

### 跨平台兼容性
- **Windows**：支持包括草稿生成、模板模式和自动导出在内的所有功能（具体可能受到剪映版本限制）
- **Linux/MacOS**：支持草稿生成和模板模式，但**不支持自动导出**，且注意**生成的草稿仍然需要在Windows版剪映下导出**。
