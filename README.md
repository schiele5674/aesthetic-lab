# Aesthetic Lab

### Evaluating Goal-Oriented Aesthetic Judgment in Multimodal AI

**Aesthetic Lab** is an exploratory research project investigating whether multimodal AI models can evaluate visual designs according to specific design goals, rather than relying on fixed aesthetic preferences.

The central research question is:

> Can AI recognize that different visual styles may be appropriate for different design goals?

The project explores the intersection of visual design, multimodal AI evaluation, aesthetic judgment, and human feedback.

---

## 1. Research Motivation

A visually attractive design is not necessarily an effective design.

For example, a restrained visual style may work well for a contemporary cultural exhibition, while a vibrant and expressive style may be more suitable for a youth music festival.

An AI model should not simply reward a design because it looks visually attractive or follows a familiar aesthetic convention. It should consider the intended audience, communication purpose, and design context.

This project investigates the distinction between **general aesthetic preference** and **goal-oriented aesthetic judgment**.

## 2. Research Questions

- **RQ1 — Style Recognition:** Can multimodal AI identify and describe different visual styles?
- **RQ2 — Goal Alignment:** Can AI evaluate whether a design is appropriate for a specific design goal?
- **RQ3 — Style Preference Bias:** Does AI consistently favor certain visual styles across different design contexts?
- **RQ4 — Human-AI Judgment Gap:** How do AI judgments differ from human evaluations?

## 3. Research Design

The first pilot focuses on two design contexts:

| ID | Design Context | Desired Qualities |
|---|---|---|
| G01 | Contemporary Cultural Exhibition | Quiet, restrained, thoughtful, culturally expressive |
| G02 | Urban Youth Music Festival | Energetic, youthful, expressive, dynamic |

Four visual design works were selected for evaluation:

- IMG02
- IMG05
- IMG07
- IMG08

The pilot uses two AI models: GPT-6 and DeepSeek.

### Experimental Structure

| Component | Quantity |
|---|---:|
| Selected visual works | 4 |
| Design goals | 2 |
| AI models | 2 |
| AI evaluation records | 16 |
| Human evaluation records | 8 |
| Bias coding categories | 5 |
| Total bias coding items | 80 |

The experimental structure is:

**4 images × 2 design goals × 2 AI models = 16 AI evaluations.**

This is a small exploratory pilot, not a large-scale benchmark.

## 4. Evaluation Framework

The project uses a standardized visual evaluation prompt, **Visual Evaluation Prompt v0.1**.

Each AI evaluation examines three dimensions:

1. **Style Recognition** — Identifies and describes the visual style.
2. **Visual Evidence** — Supports observations with specific visual details, including typography, color, composition, layout, imagery, and visual hierarchy.
3. **Goal Alignment** — Evaluates how well the design serves its specified communication goal, using a 1–5 scale.

The evaluation is goal-oriented rather than based on universal beauty or the model's personal aesthetic preference.

### Style Preference Bias Coding

A separate coding framework examines five potential bias categories:

- Minimalism Bias
- Low-saturation Bias
- Symmetry Bias
- Typography Bias
- Complexity Aversion

Each coding item is assigned one of three values:

| Score | Interpretation |
|---|---|
| 0 | No observable evidence of the bias |
| 1 | Possible evidence, but insufficient to confirm |
| 2 | Clear evidence of the bias in the evaluation |

A single occurrence does not establish a systematic model bias. Repeated patterns across different images and design goals require further investigation.

## 5. Preliminary Results

### 5.1 AI Evaluation Scores

| Model | Number of Evaluations | Mean Goal Alignment Score |
|---|---:|---:|
| GPT-6 | 8 | 3.50 |
| DeepSeek | 8 | 2.875 |

The following table summarizes the average AI scores across both models:

| Image | G01 Average | G02 Average |
|---|---:|---:|
| IMG02 | 3.5 | 2.0 |
| IMG05 | 4.0 | 2.5 |
| IMG07 | 4.0 | 3.0 |
| IMG08 | 4.0 | 2.5 |

In this pilot dataset, all four images received higher average scores for G01 than for G02.

This may indicate that the selected works are generally more aligned with the cultural exhibition context. However, the result may also reflect differences in how specifically the two design goals were defined. It does not establish that the models are inherently better at evaluating one design context.

### 5.2 Style Preference Bias Coding

A total of 80 coding items were examined across 16 AI evaluation records and five potential bias categories.

| Coding Result | Number of Items |
|---|---:|
| 0 — No observable evidence | 79 |
| 1 — Possible evidence | 1 |
| 2 — Clear evidence | 0 |
| **Total** | **80** |

One possible Complexity Aversion signal was identified in AI-012, involving a comment about visual simplicity and street-level readability.

After manual review, this case remained classified as possible evidence rather than a confirmed bias.

No systematic style preference bias can be established from the current sample.

## 6. Human-AI Comparison

Eight human evaluation records were compared with the average AI scores for the same image-goal pairs.

The mean absolute difference between human scores and AI average scores was **0.4375 points** on the 1–5 scale.

Two notable cases were:

- **IMG07 × G01:** Human score 5; AI average 4.0.
- **IMG08 × G01:** Human score 5; AI average 4.0.

These cases provide opportunities to investigate differences in how human and AI evaluators interpret cultural expression, visual atmosphere, and goal alignment.

The human evaluation is treated as a reference perspective, not an absolute definition of aesthetic quality.

Importantly, the human ratings for IMG02 were submitted after exposure to AI evaluations. Therefore, those two ratings cannot be considered fully independent or blind judgments.

## 7. Preliminary Findings

The first pilot provides several observations:

1. **Design context matters.** The same visual work can receive different goal-alignment scores depending on the intended communication purpose.
2. **Model judgments can differ.** GPT-6 and DeepSeek did not always assign the same score to the same image-goal pair.
3. **Potential bias requires careful interpretation.** A preference for simplicity or restrained colors should not automatically be classified as bias if it is justified by the design goal.
4. **Human-AI disagreement is worth investigating.** Numerical differences can point toward questions about visual evidence, interpretation, and evaluation criteria.

These findings are preliminary observations, not general conclusions about multimodal AI systems.

## 8. Limitations and Future Work

The current pilot has several limitations:

- Only four visual works were evaluated.
- Only two design goals were included in the completed experiment.
- Only one human evaluator participated.
- The human ratings for IMG02 were not fully blind to AI evaluations.
- The two AI models may use different internal scoring tendencies.
- There is no independent expert consensus benchmark.
- The bias coding framework requires further validation with a larger dataset.

### Future Work

The next research stage will focus on:

1. Expanding the image dataset and design contexts.
2. Recruiting additional independent human evaluators.
3. Improving blind evaluation procedures.
4. Refining the bias coding framework.
5. Investigating recurring differences between model evaluations and human judgments.
6. Exploring how evaluation findings can be translated into more actionable model feedback.

## 9. Repository Structure

The repository contains research documentation, evaluation prompts, experimental data, and analysis materials.

```text
aesthetic-lab/
├── research/
│   ├── research-question.md
│   ├── evaluation-rubric.md
│   ├── style-preference-bias-coding-v0.1.md
│   └── style-preference-bias-framework-v0.1.md
├── dataset/
│   ├── prompts/
│   ├── outputs/
│   ├── human-evaluations/
│   └── experiment-progress.md
├── experiments/
│   └── human-ai-comparison-v0.1.md
└── README.md
```

Additional research reports, original evaluation records, and data audit files are maintained in their corresponding project folders.

## 10. Research Inspiration

This project draws methodological inspiration from open research on multimodal aesthetic evaluation, including AesBench.

It adapts ideas from aesthetic evaluation research to investigate goal-oriented visual judgment, potential style preference bias, and human-AI evaluation differences.

- [AesBench Project](https://aesbench.github.io/)
- [AesBench GitHub Repository](https://github.com/yipoh/AesBench)

## 11. Author's Role

The project is an independent exploratory research effort.

My contributions include:

- Identifying the research problem and defining research questions.
- Designing image-goal evaluation scenarios.
- Developing a goal-oriented visual evaluation prompt.
- Organizing AI evaluation records and human feedback.
- Developing a preliminary style preference bias coding framework.
- Reviewing model outputs and examining potential evaluation inconsistencies.
- Comparing human and AI judgments.
- Documenting methodological limitations and future research directions.

The project emphasizes visual analysis, evaluation design, qualitative reasoning, data organization, and model behavior analysis.

No model training or fine-tuning is claimed.

---

*Version 2.0 — Completed Exploratory Pilot*  
*Research status: Preliminary analysis completed; further validation required.*
