# Aesthetic Lab
### Evaluating Goal-Oriented Aesthetic Judgment in Multimodal AI

**Aesthetic Lab** is an exploratory research project investigating whether multimodal AI models can evaluate visual designs according to specific design goals, rather than relying on fixed aesthetic preferences.

The project focuses on one central question:

> Can AI recognize that different visual styles may be appropriate for different design goals?

## 1. Research Motivation

A visually attractive design is not necessarily an effective design.

For example, minimalist visual design may work well for a contemporary art exhibition, while a vibrant and expressive style may be more suitable for a youth music festival.

This project investigates whether AI models can distinguish between general aesthetic preference and goal-oriented aesthetic judgment.

## 2. Research Questions

- Can multimodal AI identify different visual styles?
- Can AI evaluate whether a design matches its intended goal?
- Does AI consistently favor certain visual styles across different design contexts?
- How do AI judgments differ from human evaluations?

## 3. Research Scope

The first version focuses on visual design evaluation.

Four design contexts:

| ID | Design Context | Desired Qualities |
|---|---|---|
| G01 | Contemporary Cultural Exhibition | Quiet, restrained, cultural |
| G02 | Urban Youth Music Festival | Energetic, youthful, expressive |
| G03 | Professional Technology Forum | Clear, credible, rational |
| G04 | Community Lifestyle Festival | Warm, friendly, approachable |

Four visual styles:

| ID | Visual Style | Key Characteristics |
|---|---|---|
| S01 | Minimalism | Negative space, simplicity, restraint |
| S02 | Expressive Design | Rich colors, visual layers, strong impact |
| S03 | Swiss Modernism | Grid systems, order, clear hierarchy |
| S04 | Hand-drawn Art | Visible strokes, personality, emotional expression |

## 4. Evaluation Framework

The project explores four evaluation dimensions:

1. **Style Recognition** — Can the model identify the visual style?
2. **Goal Alignment** — Does the design fit the intended design goal?
3. **Visual Evidence** — Can the model support its judgment with specific visual details?
4. **Revision Effectiveness** — Can the model suggest meaningful improvements?

A separate exploratory indicator, **Style Preference Bias**, will be used to investigate whether a model systematically favors particular visual styles.

## 5. Human-AI Comparison

Human evaluations will be collected independently and compared with AI outputs.

The comparison will examine:

- Differences in goal-alignment scores.
- Differences in visual evidence and reasoning.
- Potential systematic preferences for particular styles.
- Cases where AI and human judgments disagree.

Human evaluations will be treated as reference judgments, not as an absolute definition of aesthetic quality.

## 6. Research Method

The project follows an exploratory evaluation workflow:

1. Select existing visual design works.
2. Record image sources and relevant metadata.
3. Define standardized design goals and evaluation questions.
4. Collect AI evaluations.
5. Collect independent human evaluations.
6. Compare results and analyze disagreement cases.

The initial pilot will be used to refine the dataset and evaluation protocol before any larger-scale testing.

## 7. Project Status

**Current stage:** Research design and pilot dataset development.

This is an exploratory research project. Results will be reported only after experiments have been conducted. No model training or fine-tuning is claimed.

## 8. Repository Structure

```text
aesthetic-lab/
├── research/
│   ├── research-question.md
│   ├── evaluation-rubric.md
│   └── weekly-reports/
├── dataset/
│   ├── prompts/
│   ├── outputs/
│   └── human-evaluations/
├── experiments/
│   ├── visual/
│   ├── literary/
│   └── interaction/
├── src/
├── agent/
└── journal/
```

## 9. Research Inspiration

This project draws methodological inspiration from open research on multimodal aesthetic evaluation, including AesBench.

The project adapts these ideas to investigate goal-oriented aesthetic judgment and human-AI evaluation differences.

- [AesBench Project](https://aesbench.github.io/)
- [AesBench GitHub Repository](https://github.com/yipoh/AesBench)

## 10. Author's Role

This project explores the intersection of visual design, aesthetic evaluation, multimodal AI, and human feedback.

The research emphasizes task design, visual analysis, evaluation criteria, and qualitative interpretation.

---

*Version 1.0 — Exploratory Research Project*
