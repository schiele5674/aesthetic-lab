# Evaluation Rubric
## Aesthetic Lab: Goal-Oriented Aesthetic Judgment

**Version:** 1.0  
**Evaluation Type:** Exploratory Human-AI Evaluation

## 1. Purpose

This rubric provides a standardized framework for evaluating whether a visual design is appropriate for a specific design goal.

The evaluation focuses on goal alignment rather than general visual attractiveness.

AI and human evaluators should use the same criteria whenever possible.

## 2. Evaluation Dimensions

Each design will be evaluated across four dimensions.

### Dimension 1 — Goal Alignment

Does the visual design match its intended purpose, audience, and emotional direction?

| Score | Description |
|---|---|
| 1 | Very poor: The design clearly conflicts with the intended goal. |
| 2 | Poor: The design shows little alignment with the goal. |
| 3 | Moderate: The design partially supports the goal but has noticeable mismatches. |
| 4 | Good: The design generally supports the goal, with minor weaknesses. |
| 5 | Excellent: The design strongly and consistently supports the goal. |

### Dimension 2 — Visual Evidence

Does the evaluator support the judgment with specific visual evidence?

| Score | Description |
|---|---|
| 1 | No meaningful visual evidence is provided. |
| 2 | Evidence is vague or weakly connected to the image. |
| 3 | Some relevant visual elements are identified. |
| 4 | Several specific elements clearly support the judgment. |
| 5 | Detailed and convincing evidence connects visual elements to the design goal. |

Examples of visual evidence include:
- Color palette
- Typography
- Composition
- Visual hierarchy
- Image and illustration style
- Negative space
- Shape and form
- Overall visual atmosphere

### Dimension 3 — Style Recognition

Can the evaluator correctly identify the dominant visual style?

Choose one category:

- S01 — Minimalism
- S02 — Expressive Design
- S03 — Swiss Modernism
- S04 — Hand-drawn Art
- Uncertain / Mixed Style

Record a short explanation of the visual characteristics supporting the classification.

### Dimension 4 — Revision Effectiveness

Are the suggested improvements relevant to the design goal?

| Score | Description |
|---|---|
| 1 | Suggestions are irrelevant or may weaken the design. |
| 2 | Suggestions have limited relevance to the goal. |
| 3 | Suggestions are partly useful but lack clear direction. |
| 4 | Suggestions are relevant and actionable. |
| 5 | Suggestions are specific, actionable, and likely to improve goal alignment. |

## 3. Instruction Following

Record whether the evaluator follows the evaluation instructions.

- Pass — All required questions are answered.
- Partial — Some requirements are missing.
- Fail — Major instructions are ignored.

This result is recorded separately and is not included in the four dimension scores.

## 4. Standard Evaluation Record

For every image, record:

| Field | Description |
|---|---|
| Image ID | Unique image identifier |
| Design Goal | Intended design context |
| Visual Style | S01 / S02 / S03 / S04 |
| Goal Alignment | Score from 1 to 5 |
| Visual Evidence | Score from 1 to 5 |
| Style Recognition | Selected category |
| Revision Effectiveness | Score from 1 to 5 |
| Instruction Following | Pass / Partial / Fail |
| Explanation | Short reasoning |
| Revision Suggestions | Suggested improvements |

## 5. Human Evaluation Protocol

To reduce evaluation bias:

1. Human evaluators should review the image and design goal independently.
2. They should not read the AI evaluation before submitting their own scores.
3. Evaluators should use the same scoring rubric.
4. Each evaluator should provide a short explanation for the goal alignment score.
5. Disagreements should be preserved rather than automatically averaged away.

If multiple human evaluators participate, their individual scores should be retained.

## 6. AI Evaluation Protocol

AI evaluations should use:

- The same image shown to human evaluators.
- The same design goal and evaluation criteria.
- A standardized prompt.
- The same scoring scale.

Original AI responses should be saved without editing.

Any missing answers or instruction-following problems should be documented.

## 7. Analysis Framework

The pilot study will examine:

**A. Goal Alignment**

Compare AI and human goal alignment scores for each image.

**B. Style Recognition**

Check whether the evaluator correctly identifies the intended visual style category.

**C. Style Preference Patterns**

Compare scores across different visual styles and design goals.

A recurring preference for one style may indicate a pattern worth investigating, but it does not automatically prove bias.

**D. Human-AI Judgment Gap**

For each image, calculate:

`Score Difference = AI Score - Human Score`

Positive values indicate higher AI scores; negative values indicate higher human scores.

When multiple human evaluators are available, their average score may be used as a comparison reference, while individual differences remain documented.

## 8. Methodological Limitations

- The initial dataset is small and exploratory.
- Existing design works may not have been created for the experimental design goals.
- Image quality, subject matter, and other visual factors may influence scores.
- Human judgments are subjective.
- Small samples cannot establish universal model behavior.

The results should be interpreted as preliminary observations rather than definitive conclusions.

## 9. Research Principle

The central principle of Aesthetic Lab is:

**A visually attractive design is not necessarily an effective design.**

Aesthetic evaluation should consider whether visual choices serve the intended design goal, rather than rewarding a fixed visual style.
