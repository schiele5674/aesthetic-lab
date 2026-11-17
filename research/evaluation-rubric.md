# Evaluation Rubric
## Aesthetic Lab: Goal-Oriented Aesthetic Judgment

**Version:** 1.0  
**Evaluation Type:** Exploratory Human-AI Evaluation

## 1. Purpose

This rubric provides a standardized framework for evaluating whether a visual design is appropriate for a specific design goal.

The evaluation focuses on goal alignment rather than general visual attractiveness.

AI and human evaluators should use the same criteria whenever possible.

## 2. Evaluation Dimensions

Each design will be evaluated across three dimensions.

### Dimension 1 — Style Recognition

Identify and describe the dominant visual style of the design.

The evaluator should explain the visual characteristics supporting the style identification, rather than forcing the image into a fixed style category.

### Dimension 2 — Visual Evidence

Identify observable visual elements that support the evaluation.

Relevant elements may include:

- Typography
- Color palette
- Composition
- Layout
- Imagery and illustration
- Visual hierarchy
- Negative space
- Shape and form

This dimension focuses on evidence-based visual description. It is not assigned an independent numerical score.

### Dimension 3 — Goal Alignment

Evaluate how well the visual design supports the specified design goal, audience, and communication objective.

| Score | Description |
|---|---|
| 1 | Very poor: The design clearly conflicts with the intended goal. |
| 2 | Poor: The design shows little alignment with the goal. |
| 3 | Moderate: The design partially supports the goal but has noticeable mismatches. |
| 4 | Good: The design generally supports the goal, with minor weaknesses. |
| 5 | Excellent: The design strongly and consistently supports the goal. |

Evaluators should base their scores on observable visual evidence and the specified design goal, rather than personal aesthetic preference.
## 3. Instruction Following

Instruction following may be documented as a supplementary observation when relevant.

It is not a scored evaluation dimension and is not included in the Goal Alignment score.

Any missing answers, incomplete evaluations, or deviations from the evaluation prompt should be documented separately without changing the original model response.
## 4. Standard Evaluation Record

For every image-goal evaluation, record:

| Field | Description |
|---|---|
| Record ID | Unique evaluation identifier |
| Image ID | Unique image identifier |
| Design Goal | Intended design context |
| Model / Evaluator | AI model or human evaluator |
| Style Recognition | Description of the identified visual style |
| Visual Evidence | Observable visual elements supporting the evaluation |
| Goal Alignment | Score from 1 to 5 |
| Explanation | Reasoning supporting the evaluation |

Original AI responses and individual human evaluation records should be preserved separately.

The standard record reflects the three dimensions used in the completed pilot study.
## 5. Human Evaluation Protocol

Human evaluators should assess each image according to the specified design goal and the same three evaluation dimensions used in AI evaluation.

The preferred procedure is:

1. Review the image and design goal independently before reading AI evaluations.
2. Record the Style Recognition, Visual Evidence, and Goal Alignment judgments.
3. Provide a short explanation supporting the Goal Alignment score.
4. Preserve individual judgments rather than automatically averaging away disagreements.

In this pilot, one human evaluator completed eight image-goal evaluations.

The IMG02 human evaluations were submitted after exposure to AI evaluation outputs. The evaluations for IMG05, IMG07, and IMG08 were completed without prior exposure to the corresponding AI outputs.

This procedural difference is documented as a methodological limitation and should be considered when interpreting the Human-AI comparison.
## 6. AI Evaluation Protocol

AI evaluations were conducted using:

- The selected visual images.
- The corresponding design goal briefs.
- The standardized Visual Evaluation Prompt v0.1.
- The same three evaluation dimensions: Style Recognition, Visual Evidence, and Goal Alignment.

The pilot includes 16 AI evaluation records from two models: ChatGPT (GPT-6) and DeepSeek (DeepSeek-V4.1-Flash).

Original AI responses were preserved for subsequent analysis.

Goal Alignment scores were recorded as reported in each model response. No retrospective changes were made to the original scores.

Any missing answers or deviations from the evaluation prompt should be documented separately.

## 7. Analysis Framework

The completed pilot study examines four research dimensions:

**A. Goal-Oriented Aesthetic Judgment**

Analyze how well AI evaluations assess visual designs in relation to the specified design goals.

Compare Goal Alignment scores across images, goals, and models.

**B. Style Recognition and Visual Evidence**

Examine how models identify visual styles and whether their judgments are supported by observable visual evidence.

**C. Style Preference Bias**

Review AI responses across five candidate bias categories:

- Minimalism Bias
- Low-saturation Bias
- Symmetry Bias
- Typography Bias
- Complexity Aversion

Each response is examined using the preliminary coding scale:

- 0 — No observable bias indicator
- 1 — Possible bias indicator; insufficient evidence
- 2 — Clear bias indicator in this individual response

A score of 2 does not establish stable model-level bias.

**D. Human-AI Judgment Gap**

Compare AI and human Goal Alignment scores for each image-goal combination.

Calculate:

`Score Difference = AI Score - Human Score`

Positive values indicate higher AI scores; negative values indicate higher human scores.

The mean absolute difference may be used as a descriptive summary. Given the small dataset and single human evaluator, the results should be interpreted as exploratory observations rather than evidence of model accuracy or reliability.

The completed pilot also includes 80 bias coding items derived from the 16 AI evaluation responses, covering five candidate bias categories.

## 8. Methodological Limitations

The following limitations should be considered when interpreting the pilot findings:

- The dataset includes only four selected images, two design goals, and two AI models.
- The selected existing design works may not have been originally created for the experimental design goals.
- Only one human evaluator participated, so human judgments may reflect individual aesthetic preferences.
- The IMG02 human evaluations were submitted after exposure to AI evaluation outputs, which may have influenced those judgments.
- Visual style classifications and bias coding involve interpretive judgments.
- Model responses may be influenced by prompt wording and task interpretation.
- The absence of an independent expert reference standard limits conclusions about evaluation accuracy.
- Observed output patterns do not reveal the models' internal training mechanisms.

The findings should therefore be interpreted as preliminary observations within this exploratory pilot, not as definitive conclusions about general model behavior.

## 9. Research Principle

The central principle of Aesthetic Lab is:

**A visually attractive design is not necessarily an effective design.**

Aesthetic evaluation should consider whether visual choices serve the intended design goal, audience, and communication objective.

No single visual style should be treated as universally superior. A design should be evaluated in context, based on its visual characteristics and its ability to fulfill its intended purpose.

The goal of this research is not to identify one universally preferred aesthetic, but to examine whether multimodal AI models can make context-sensitive, evidence-based aesthetic judgments.
