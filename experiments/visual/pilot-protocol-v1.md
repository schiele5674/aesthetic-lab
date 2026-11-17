# Visual Pilot Experiment Protocol

## Aesthetic Lab — Version 1.0

**Protocol Version:** 1.0  
**Study Type:** Exploratory Pilot Study  
**Research Focus:** Goal-Oriented Aesthetic Judgment in Multimodal AI

---

## 1. Research Objective

This pilot investigates whether multimodal AI models can evaluate visual designs according to different design goals, rather than relying on fixed preferences for particular visual styles.

The study also compares AI judgments with human evaluations and explores possible style preference patterns in model responses.

The purpose is to develop and examine a practical evaluation framework, not to establish a universal benchmark of aesthetic quality.

## 2. Initial Experimental Design

The initial experimental plan was designed around:

- 2 design goals
- 4 candidate visual style categories
- 8 planned visual design works

### Design Goals

| ID | Design Context | Intended Impression |
|---|---|---|
| G01 | Contemporary Cultural Exhibition | Quiet, restrained, thoughtful, culturally expressive |
| G02 | Urban Youth Music Festival | Energetic, youthful, expressive, dynamic |

### Initial Candidate Visual Style Categories

| ID | Candidate Style |
|---|---|
| S01 | Minimalism |
| S02 | Expressive Design |
| S03 | Swiss Modernism |
| S04 | Hand-drawn Art |

The initial plan aimed to include examples from these four candidate style categories under both design goals.

The dataset was subsequently reduced to four selected images because the pilot was refined around available visual materials and the feasibility of the evaluation process.

The four candidate style categories were part of the initial selection plan. They should not be treated as balanced experimental groups in the completed pilot.

## 3. Materials

The experiment uses:

1. Selected visual design images.
2. Image source and selection records.
3. Standardized AI evaluation prompt.
4. Human evaluation template.
5. Original AI evaluation responses.
6. Human evaluation records.
7. Evaluation rubric.
8. Style preference bias coding framework.

Image sources, creators, usage rights, and selection rationales should be documented in the corresponding dataset records.

## 4. Experimental Procedure

### Step 1 — Select Images

Select existing visual design works suitable for exploratory evaluation.

Record the original source, creator information when available, usage rights, and selection rationale.

Assign each selected image a unique ID.

The completed pilot uses four images:

- IMG02
- IMG05
- IMG07
- IMG08

### Step 2 — Prepare Experimental Inputs

For each image, prepare:

- Image ID
- Design goal
- Target audience
- Desired emotional atmosphere
- Communication purpose
- Image file or accessible image reference

Use the same design goal description for every image assigned to that goal.

### Step 3 — Conduct AI Evaluation

Submit each image under both design goals to the selected AI models.

The completed pilot includes two models:

- ChatGPT (GPT-6)
- DeepSeek (DeepSeek-V4.1-Flash)

Use the standardized Visual Evaluation Prompt v0.1.

Save the complete original response.

Record:

- Model name and version
- Evaluation date
- Prompt version
- Image ID
- Design goal
- Original response
- Any technical or instruction-following problems

The completed pilot contains 16 AI evaluation records:

4 images × 2 design goals × 2 AI models = 16 records.

Do not rewrite original AI responses or retrospectively change their reported scores.

### Step 4 — Conduct Human Evaluation

A single human evaluator assessed the same four images under both design goals, producing eight human evaluation records.

The intended procedure was to complete human evaluations before viewing AI outputs.

However, the actual procedure differed:

- IMG02 human evaluations were submitted after exposure to AI evaluation outputs.
- IMG05, IMG07, and IMG08 human evaluations were completed without prior exposure to the corresponding AI outputs.

This deviation is documented as a methodological limitation.

Human scores and explanations should be preserved individually rather than treated as independent expert consensus or a gold-standard reference.

### Step 5 — Organize Results

Match AI and human evaluations by image ID and design goal.

Check that all records are complete and that Goal Alignment scores use the same five-point scale.

Preserve original responses and individual evaluation records.

Do not invent missing scores or replace incomplete evaluations with estimated values.

## 5. Analysis Framework

### A. Goal Alignment Comparison

Compare AI Goal Alignment scores across images, design goals, and models.

Examine whether evaluations change when the same image is presented under different design goals.

### B. Style Recognition and Visual Evidence

Examine how models identify visual styles and whether their descriptions are supported by observable visual evidence.

The analysis is qualitative and does not assume that the initial candidate style categories provide definitive ground-truth labels.

### C. Style Preference Bias Coding

Review the 16 AI evaluation responses across five candidate bias categories:

- Minimalism Bias
- Low-saturation Bias
- Symmetry Bias
- Typography Bias
- Complexity Aversion

Each response is examined using the following preliminary coding scale:

| Score | Meaning |
|---|---|
| 0 | No observable bias indicator |
| 1 | Possible bias indicator; insufficient evidence |
| 2 | Clear bias indicator in this individual response |

The completed pilot contains 80 coding items:

16 AI responses × 5 candidate bias categories = 80 items.

A coding score of 2 does not establish stable model-level bias.

### D. Human-AI Judgment Gap

Calculate:

`Score Difference = AI Goal Alignment Score - Human Goal Alignment Score`

Positive values indicate higher AI scores, while negative values indicate higher human scores.

The mean absolute difference may be used as a descriptive summary.

Since only one human evaluator participated and IMG02 evaluations were submitted after exposure to AI outputs, comparisons should be interpreted cautiously.

## 6. Basic Controls

To improve consistency:

- Use the same standardized prompt version across AI evaluations whenever possible.
- Keep the Goal Alignment scoring scale unchanged.
- Provide consistent design goal descriptions.
- Use the same image for AI and human evaluation.
- Preserve original AI responses and human records.
- Record model names and versions.
- Document procedural deviations and limitations.
- Avoid treating subjective style judgments as objective ground truth.

## 7. Actual Pilot Scope and Completion

The completed pilot includes:

| Item | Actual Result |
|---|---|
| Selected images | 4 |
| Design goals | 2 |
| AI models | 2 |
| AI evaluation records | 16 |
| Human evaluation records | 8 |
| Human evaluators | 1 |
| Candidate bias categories | 5 |
| Bias coding items | 80 |

The initial plan of eight images was reduced to four selected images.

The completed pilot focuses on two design goals and two AI models. It is an exploratory study with a small sample, not a balanced benchmark across four visual style categories.

## 8. Limitations

This is a small exploratory pilot, not a representative benchmark.

The following limitations should be considered:

- Only four images, two design goals, and two AI models were included.
- Existing design works may not have been originally created for the assigned experimental goals.
- The initial four candidate style categories do not constitute balanced experimental groups in the completed dataset.
- Only one human evaluator participated.
- The IMG02 human evaluations were submitted after exposure to AI evaluation outputs.
- Visual style descriptions and bias coding involve interpretive judgments.
- Model responses may be influenced by prompt wording and task interpretation.
- No independent expert reference standard was established.
- Observed output patterns do not reveal the models' internal training mechanisms.

The findings should therefore be interpreted as preliminary observations rather than definitive conclusions about general model behavior.

## 9. Research Integrity

All results must come from actual evaluations.

Do not fabricate image sources, AI outputs, human scores, or experimental findings.

Preserve original AI responses and individual human evaluation records.

Distinguish the initial experimental plan from the completed pilot procedure.

Document changes, incomplete records, and methodological deviations transparently.

The purpose of this project is to build a transparent and reproducible evaluation process, not to produce a predetermined conclusion.
