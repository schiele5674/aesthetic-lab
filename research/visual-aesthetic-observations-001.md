# Visual Aesthetic Observations 001

**Project:** Aesthetic Lab  
**Record type:** Human observation and preliminary research notes  
**Status:** Exploratory; not formal benchmark data  
**Date:** 2026-11-12

## 1. Purpose

This document records observations from the first five visual-aesthetic exercises. The goal is to turn intuitive aesthetic judgments into criteria that can be discussed, tested, and eventually used to evaluate AI-generated visual outputs.

These exercises are exploratory. They reflect one evaluator's judgments and should not be treated as representative human consensus or statistically validated results.

## 2. Observations from the exercises

### Exercise 1 — Composition, negative space, and rhythm

**Human observation**

The preferred poster had more negative space and a clearer rhythm. It did not feel overly dense or visually tiring.

**Concepts identified**

- Negative space
- Visual rhythm
- Visual load
- Spatial organization

**Preliminary implication**

A visual evaluation rubric should consider not only whether a composition contains attractive elements, but also how elements and empty space are organized.

### Exercise 2 — Matching visual language to the theme

**Human observation**

For the theme “the vitality of a city,” a richer composition could be more appropriate than a highly minimal one, provided the elements remain organized.

**Concepts identified**

- Task alignment
- Theme suitability
- Richness with order
- Distinction between personal preference and task requirements

**Preliminary implication**

Aesthetic evaluation should not reward minimalism by default. The visual approach should be judged in relation to the task and intended message.

### Exercise 3 — Multiple strategies for expressing an emotion

**Theme:** “Loneliness in spring”

**Human observation**

Both a sparse, quiet composition and a visually abundant composition could communicate loneliness through different expressive strategies. The evaluator did not consider one approach the only correct answer.

**Concepts identified**

- Emotional expression
- Expressive strategy
- Multiple valid interpretations
- Avoidance of a single-style bias

**Preliminary implication**

Evaluation tasks should allow more than one successful visual solution. The key question is whether the chosen strategy communicates the theme coherently.

### Exercise 4 — Evaluating “a quiet summer afternoon”

**Human observation**

A blue swimming pool, sunlight, and a quiet setting seemed more aligned with the theme than a crowded, colorful beach scene. The selected output received a theme-suitability score of 4/5.

**Important limitation**

The evaluator did not provide a complete explanation for why the score was 4 rather than 5. The reason should not be invented after the fact.

**Concepts identified**

- Theme suitability
- Visual competition
- Perceived busyness
- Mood and atmosphere

**Preliminary implication**

A future evaluation form should ask evaluators to provide brief evidence for numerical scores, especially when the score is not the maximum or minimum.

### Exercise 5 — Turning aesthetic judgment into actionable feedback

**Human feedback**

- Preserve: the blue swimming pool and sunlight.
- Reduce: unnecessary decorative elements.
- Strengthen: the tree shadows and layers of light.
- Target effect: quiet, slow, and a sense of time passing.

**Reconstructed editing instruction**

> Preserve the blue swimming pool and the sunlight as the main visual anchors. Remove unnecessary decorative elements that compete with the central scene. Strengthen the tree shadows and create more nuanced layers of light so that the passage of afternoon time becomes perceptible. Keep the overall atmosphere quiet and unhurried. Avoid adding new focal points or making the composition feel busier.

**Preliminary assessment**

The feedback is relatively actionable because it identifies what to preserve, what to reduce, what to strengthen, and the intended emotional result. It also gives the image-editing model a clear direction without prescribing every visual detail.

## 3. Emerging research principles

1. **Evaluate task alignment, not personal taste alone.** A visual style should be judged in relation to the theme and intended use.
2. **Allow multiple expressive strategies.** Different visual solutions may communicate the same theme successfully.
3. **Separate output quality from feedback quality.** A model may generate a strong image but give weak revision guidance, or vice versa.
4. **Require evidence for scores.** Numerical ratings should be accompanied by observable reasons.
5. **Test whether feedback is actionable.** Good feedback should specify what to preserve, reduce, strengthen, and what effect the revision should achieve.

## 4. Current evaluation dimensions

### Output quality

- Spatial organization and visual rhythm
- Color harmony
- Theme suitability
- Visual hierarchy and information organization
- Style coherence and completeness
- Emotional expression
- Reasonableness of expressive strategy

### Feedback quality

- Problem identification
- Actionability of revision suggestions
- Preservation of the original goal

### Instruction following

Record separately as **Pass / Partial / Fail**. Do not merge instruction-following scores into aesthetic-quality scores.

## 5. Questions for the next research stage

- Can different models identify the same visual problem in an output?
- Can they explain why a visual choice does or does not fit a theme?
- Can they propose concrete edits while preserving the user's intended effect?
- Can they support multiple valid visual styles rather than defaulting to one aesthetic?
- Do evaluators give consistent scores when they use the same rubric?

## 6. Methodological note

The observations above are qualitative notes from early practice exercises, not results from a controlled model comparison. A later pilot should use consistent prompts, preserve original outputs and settings, anonymize model identities during evaluation where practical, and record both numerical scores and written rationales.

Do not treat the example scores or illustrative judgments in this document as benchmark results.
