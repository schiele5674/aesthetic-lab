# Aesthetic Lab：AI 目标导向审美判断评测项目

**Project Type:** Independent Exploratory Research  
**Research Area:** Multimodal AI Evaluation / Visual Aesthetic Judgment  
**Project Status:** Exploratory Pilot Completed

---

## 1. 项目背景（Background）

在视觉设计中，一件作品是否合适，并不只取决于它是否具有某种普遍意义上的美感，还取决于它是否符合具体的设计目标。

例如，一张安静、克制的海报可能适合当代文化展览，却未必适合强调活力、参与感和年轻文化的音乐节。

这引出了我对多模态 AI 审美评测的兴趣：

**AI 模型能否根据不同的设计目标调整自己的审美判断，而不是始终偏好某一种视觉风格？**

Aesthetic Lab 是我围绕这一问题开展的独立探索性研究项目，尝试将视觉审美判断转化为可以观察、记录和比较的评测流程。

## 2. 核心研究问题（Research Questions）

项目围绕四个问题展开：

- **RQ1 — Style Recognition：** 模型能否识别作品的视觉风格及其主要特征？
- **RQ2 — Goal Alignment：** 模型能否判断作品是否符合指定的设计目标？
- **RQ3 — Style Preference Bias：** 模型是否表现出对某些视觉风格的固定偏好？
- **RQ4 — Human-AI Judgment Gap：** 模型的评价与人工评价之间存在哪些差异？

其中，第一版实验主要围绕风格识别、视觉证据和目标适配度开展评价，并对潜在风格偏好信号进行初步编码。

## 3. 实验设计（Experimental Design）

为了观察模型在不同设计目标下的判断变化，我建立了一个小规模视觉评测样本。

**实验样本：**

- 4 张视觉设计作品：IMG02、IMG05、IMG07、IMG08
- 2 种设计目标
- 2 个 AI 模型：GPT-6 和 DeepSeek
- 16 条 AI 评价记录
- 8 条人工评价记录

**两个设计目标：**

**G01 — Contemporary Cultural Exhibition**

当代文化展览海报。目标受众为年轻人和对文化感兴趣的观众，强调文化表达、思考和安静的精致感。期望呈现克制、沉静、有思想性和文化表达力的视觉效果。

**G02 — Urban Youth Music Festival**

城市青年音乐节海报。目标受众为年轻人及当代音乐文化群体，强调活力、兴奋感、年轻气息和参与感。期望呈现充满能量、大胆、富有表现力和动态感的视觉效果。

通过让同一作品分别面对两个设计目标，我希望观察模型是否能够区分视觉风格本身与风格对具体任务的适配程度。

## 4. 评测框架（Evaluation Framework）

我制定了 Visual Evaluation Prompt v0.1，并将评价组织为三个维度：

### A. Style Recognition — 风格识别

观察模型能否识别作品的视觉风格，以及字体、色彩、构图、图像等主要视觉特征。

### B. Visual Evidence — 视觉证据

要求模型根据作品中实际存在的视觉元素进行分析，包括：

- Typography：字体与文字排版
- Color：色彩关系
- Composition：构图
- Layout：版式
- Imagery：图像与视觉元素
- Visual Hierarchy：视觉层级

这一维度强调评价必须有作品中的具体证据支持，而不是只给出主观印象。

### C. Goal Alignment — 目标适配度

使用 1–5 分评价作品与指定设计目标的适配程度。

评价重点不是作品是否符合评价者个人喜好，也不是它是否具有普遍意义上的美感，而是它是否有效地服务于当前设计任务。

## 5. 数据与初步结果（Data and Preliminary Results）

### 5.1 AI 评价数据

本轮实验共完成 16 条 AI 评价。

| 指标 | GPT-6 | DeepSeek |
|---|---:|---:|
| 评价记录数 | 8 | 8 |
| 平均目标适配评分 | 3.50 | 2.875 |
| G01 平均评分 | 4.25 | 3.50 |
| G02 平均评分 | 2.75 | 2.25 |

在本轮样本中，GPT-6 的平均评分高于 DeepSeek。但由于实验规模较小，且没有独立专家共识作为准确性基准，这一结果只能说明两组模型输出在本轮实验中存在评分差异，不能据此判断哪个模型更准确。

### 5.2 不同设计目标下的评分

| 图片 | G01 平均分 | G02 平均分 |
|---|---:|---:|
| IMG02 | 3.5 | 2.0 |
| IMG05 | 4.0 | 2.5 |
| IMG07 | 4.0 | 3.0 |
| IMG08 | 4.0 | 2.5 |

四张图片在本轮实验中的 G01 平均评分均高于 G02。

这一现象可能与当前图片样本整体更适合文化展览目标有关，也可能与两个设计目标的具体要求和样本分布有关。因此，不能直接将其解释为模型普遍更擅长评价文化展览设计。

### 5.3 风格偏好偏差编码

我建立了五类潜在风格偏好观察维度：

- Minimalism Bias：极简主义偏好
- Low-saturation Bias：低饱和度偏好
- Symmetry Bias：对称偏好
- Typography Bias：字体偏好
- Complexity Aversion：复杂度回避

对 16 条 AI 评价进行编码，每条评价对应 5 个观察项，共计 80 个编码项。

编码结果：

- 79 项：0 — 未观察到明显证据
- 1 项：1 — 存在可能信号，但证据不足
- 0 项：2 — 明确证据

本轮实验没有发现能够确认的系统性风格偏好偏差。

## 6. 关键案例分析：AI-012（Case Analysis）

在全部 16 条 AI 评价中，AI-012 被标记为一个可能值得进一步观察的案例。

该记录对应 IMG07 × G02（Urban Youth Music Festival）× DeepSeek。

评价中提到了作品中单一黑色形状在复杂视觉环境下的识别与可读性问题。这个判断可能涉及对复杂度或视觉表现形式的偏好，但也可能只是针对具体传播环境提出的合理可读性考虑。

因此，我没有直接将其归类为明确的 Complexity Aversion。

**我的归因判断是：**

1. 识别潜在异常信号。
2. 回到原始评价文本检查具体证据。
3. 区分风格偏好与功能性设计判断。
4. 在证据不足时保留不确定性，不强行认定为 Badcase。

这一案例让我认识到，模型评测不能只寻找符合预期的错误，还需要判断现有证据是否真正支持某种问题归因。

## 7. 人机评价比较（Human-AI Comparison）

我将 8 条人工评价与对应的 AI 平均评分进行比较。

本轮人机评价的平均绝对差（Mean Absolute Difference, MAD）为：

**0.4375 分（1–5 分量表）**

在 IMG07 × G01 和 IMG08 × G01 两个案例中，人工评分比 AI 平均评分高 1 分。

这一结果说明，在当前小规模样本中，人机评价存在一定差异，但不能据此证明模型具有稳定的人类审美判断能力，也不能将单一人工评价者视为标准答案。

人工评价在本项目中主要作为参考判断，用于观察差异，而不是作为经过专家验证的 Gold Standard。

## 8. 研究局限与下一步方向（Limitations and Future Work）

本项目目前仍处于探索性研究阶段，存在以下局限：

1. **样本规模有限：** 仅包含 4 张图片和 2 种设计目标，无法代表丰富的视觉设计类型。
2. **人工评价者单一：** 当前人工评分来自一位评价者，缺少多评价者之间的一致性分析。
3. **缺少独立专家基准：** 当前没有专家共识或外部标准作为模型评价准确性的验证依据。
4. **偏差编码需要进一步验证：** 五类偏差观察维度仍属于初步框架，需要扩大样本并进行更严格的编码一致性检验。
5. **实验结果不能直接推广：** 当前结果仅适用于本轮样本和实验设置。

后续可以通过增加图片类型、设计目标和评价者数量，进一步检验模型是否存在稳定的风格偏好，以及其目标适配判断在不同任务中的表现。

## 9. 个人贡献与项目收获（My Contribution）

作为项目发起者和主要执行者，我完成了以下工作：

- 提出以目标导向审美判断为核心的研究问题。
- 设计实验结构，选择视觉样本并定义两种不同设计目标。
- 制定 Visual Evaluation Prompt v0.1 和视觉评价维度。
- 收集并整理 GPT-6 与 DeepSeek 的原始评价记录。
- 完成 8 条人工评价，并建立人机评价比较流程。
- 建立五类潜在风格偏好观察维度，完成 80 个编码项的初步检查。
- 回到原始评价文本分析潜在 Badcase，区分可能信号与明确证据。
- 整理实验数据、阶段性结果和研究局限。

这段经历让我逐渐形成了一种评测思路：

**先明确任务目标，再建立评价标准；先寻找具体证据，再进行问题归因；最后通过数据比较和局限分析，判断结论能够支持到什么程度。**

我希望将视觉设计训练中形成的观察能力、审美判断和目标意识，转化为多模态 AI 评测中的实际能力。

---

## Project Repository

GitHub: https://github.com/schiele5674/aesthetic-lab

Key Materials:

- `README.md` — 项目整体介绍
- `research/research-question.md` — 核心研究问题
- `research/evaluation-rubric.md` — 评价标准
- `research/style-preference-bias-framework-v0.1.md` — 风格偏好偏差框架
- `research/style-preference-bias-coding-v0.1.md` — 偏差编码记录
- `experiments/human-ai-comparison-v0.1.md` — 人机评价比较
- `dataset/experiment-progress.md` — 实验进度与结果记录

**Note:** Aesthetic Lab is an independent exploratory research project. The findings are preliminary and should not be interpreted as validated benchmark results or definitive claims about model capabilities.


