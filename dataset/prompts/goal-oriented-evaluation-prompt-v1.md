# Standardized AI Evaluation Prompt
## Aesthetic Lab — Goal-Oriented Visual Evaluation V1

**Version:** 1.0  
**Evaluation Type:** Multimodal AI Evaluation  
**Research Focus:** Goal-Oriented Aesthetic Judgment

---

## 1. Instructions

You are participating in an exploratory research project evaluating goal-oriented aesthetic judgment in multimodal AI.

Your task is to evaluate the provided visual design according to the specified design goal.

Do not judge the image only by whether it looks beautiful or visually attractive.

Instead, consider whether its visual choices effectively support the intended purpose, audience, and emotional direction.

Use only visual evidence that can reasonably be observed in the image.

Do not invent information about the designer, original brief, or intended audience beyond the information provided.

## 2. Experimental Input

**Image ID:** [INSERT IMAGE ID]

**Design Goal:** [INSERT DESIGN GOAL]

**Target Audience:** [INSERT TARGET AUDIENCE]

**Desired Emotional Impression:** [INSERT EMOTIONAL IMPRESSION]

**Image:** [ATTACH ONE IMAGE]

## 3. Evaluation Tasks

### Task 1 — Style Recognition

Identify the dominant visual style.

Choose one:

- S01 — Minimalism
- S02 — Expressive Design
- S03 — Swiss Modernism
- S04 — Hand-drawn Art
- Uncertain / Mixed Style

Explain your choice using observable visual characteristics.

### Task 2 — Visual Analysis

Describe the image's main visual characteristics.

Consider:

- Color palette
- Typography
- Composition
- Visual hierarchy
- Shapes and forms
- Illustration or photographic treatment
- Negative space
- Overall visual atmosphere

Focus on relevant evidence rather than listing every visible element.

### Task 3 — Goal Alignment Evaluation

Evaluate how effectively the image supports the specified design goal.

Provide:

**Goal Alignment Score:** 1–5

Use the following scale:

| Score | Meaning |
|---|---|
| 1 | Very poor alignment |
| 2 | Poor alignment |
| 3 | Moderate alignment |
| 4 | Good alignment |
| 5 | Excellent alignment |

Explain the score by connecting specific visual evidence to the design goal.

### Task 4 — Revision Suggestions

Suggest three specific improvements that could make the image more suitable for the given design goal.

Each suggestion must:

- Refer to an identifiable visual element.
- Explain what should be changed.
- Explain why the change would improve goal alignment.

Do not recommend changes merely because they match your preferred visual style.

### Task 5 — Overall Judgment

Answer the following questions:

1. What is the strongest aspect of this design?
2. What is its most important weakness in relation to the design goal?
3. Does the design successfully communicate the intended emotional impression? Why?

## 4. Required Output Format

Use the following structure:

### A. Style Recognition
- Selected Style:
- Confidence:
- Visual Evidence:

### B. Visual Analysis
- Color:
- Typography:
- Composition:
- Visual Hierarchy:
- Other Relevant Features:

### C. Goal Alignment
- Score:
- Explanation:
- Supporting Visual Evidence:

### D. Revision Suggestions
1.
2.
3.

### E. Overall Judgment
- Strongest Aspect:
- Main Weakness:
- Emotional Impression:
- Final Assessment:

## 5. Evaluation Rules

1. Evaluate the image in relation to the supplied design goal.
2. Do not automatically reward minimalism or visual simplicity.
3. Do not automatically reward complexity or decorative richness.
4. Different styles may be equally appropriate for different goals.
5. Explain judgments with observable visual evidence.
6. Keep the same evaluation criteria across all images.
7. Do not change the scoring scale.
8. If information is insufficient, explicitly state the uncertainty.

## 6. Research Integrity

This prompt is designed for exploratory evaluation, not for establishing universal aesthetic standards.

The AI's output must be saved in its original form.

Do not rewrite the AI's answer before analysis.

Record incomplete responses, unsupported claims, and instruction-following failures separately.

**End of Prompt**
