# Visual Pilot Experiment Protocol
## Aesthetic Lab — V0.1

**Protocol Version:** 1.0  
**Study Type:** Exploratory Pilot Study  
**Research Focus:** Goal-Oriented Aesthetic Judgment in Multimodal AI

---

## 1. Research Objective

This pilot investigates whether a multimodal AI model can evaluate visual designs according to different design goals, rather than relying on a fixed preference for particular visual styles.

The study also compares AI judgments with independent human evaluations.

## 2. Experimental Design

The initial dataset is designed around:

- 2 design goals
- 4 visual styles
- 8 planned visual design works

### Design Goals

| ID | Design Context | Intended Impression |
|---|---|---|
| G01 | Contemporary Cultural Exhibition | Quiet, restrained, cultural |
| G02 | Urban Youth Music Festival | Energetic, youthful, exciting |

### Visual Styles

| ID | Style |
|---|---|
| S01 | Minimalism |
| S02 | Expressive Design |
| S03 | Swiss Modernism |
| S04 | Hand-drawn Art |

Each design goal is paired with all four visual styles.

The dataset may be reduced if suitable images or usage permissions cannot be confirmed. Any reduction must be documented.

## 3. Materials

The experiment requires:

1. Selected visual design images.
2. Completed image source records.
3. Standardized AI evaluation prompt.
4. Human evaluation template.
5. AI output records.
6. Human evaluation records.

The evaluation criteria must follow the project's evaluation rubric.

## 4. Experimental Procedure

### Step 1 — Select Images

Select existing visual design works that represent the four visual styles.

Record the original source, creator, usage rights, and selection rationale.

Assign each image a unique ID.

### Step 2 — Prepare Experimental Inputs

For each image, prepare:

- Image ID
- Design goal
- Target audience
- Desired emotional impression
- Image file or accessible image reference

Use the same design goal description for every image assigned to that goal.

### Step 3 — Conduct AI Evaluation

Submit each image to the selected multimodal AI model.

Use the standardized evaluation prompt without changing the scoring criteria.

Save the complete original response.

Record:

- Model name
- Model version, if available
- Evaluation date
- Prompt version
- Image ID
- Original response
- Any technical or instruction-following problems

Do not rewrite the original AI response.

### Step 4 — Conduct Human Evaluation

Human evaluators assess the same images using the human evaluation template.

They must not view AI evaluations before submitting their own scores.

Preserve individual scores and explanations.

### Step 5 — Organize Results

Match AI and human evaluations by image ID.

Check that all records are complete and that scores use the same five-point scale.

Do not invent missing scores or replace incomplete evaluations with estimated values.

## 5. Analysis Plan

### A. Goal Alignment Comparison

Compare AI and human goal alignment scores for each image.

### B. Style Recognition

Compare the identified visual style with the dataset's assigned style category.

### C. Style Preference Patterns

Examine whether the model repeatedly gives higher scores to a particular visual style across different design goals.

A style preference should be investigated in relation to the design goal, not interpreted from one isolated image.

### D. Human-AI Judgment Gap

Calculate:

`Score Difference = AI Goal Alignment Score - Human Goal Alignment Score`

Positive values indicate higher AI scores, while negative values indicate higher human scores.

If multiple human evaluators participate, retain individual scores and report how the comparison reference was calculated.

## 6. Basic Controls

To improve consistency:

- Use the same AI model throughout the pilot whenever possible.
- Use the same standardized prompt version.
- Keep the scoring scale unchanged.
- Provide consistent design goal descriptions.
- Use the same image for AI and human evaluation.
- Preserve original outputs and records.
- Document any deviations from the protocol.

## 7. Limitations

This is a small exploratory pilot, not a representative benchmark.

Existing design works may not have been created for the assigned experimental goals.

Differences in image quality, subject matter, and composition may influence evaluations.

The results cannot establish universal aesthetic preferences or prove systematic model bias.

## 8. Completion Checklist

- [ ] Research questions documented
- [ ] Evaluation rubric established
- [ ] Image sources recorded
- [ ] Image usage permissions checked
- [ ] Standardized AI prompt prepared
- [ ] Human evaluation template prepared
- [ ] Experimental images selected
- [ ] AI evaluations collected
- [ ] Human evaluations collected
- [ ] Results organized
- [ ] Limitations documented

## 9. Research Integrity

All results must come from actual evaluations.

Do not fabricate image sources, AI outputs, human scores, or experimental findings.

If the pilot is incomplete, report it as incomplete.

The purpose of this project is to build a transparent and reproducible evaluation process, not to produce a predetermined conclusion.
