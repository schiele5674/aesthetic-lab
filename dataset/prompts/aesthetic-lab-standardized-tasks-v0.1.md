# Aesthetic Lab — Standardized Evaluation Tasks v0.1

**Project:** Aesthetic Lab  
**Dataset:** Pilot task set 001  
**Status:** Draft for exploratory pilot  
**Date:** 2026-11-12  
**Task count:** 15 (5 visual, 5 literary, 5 interaction)

## 1. Purpose

This task set is designed to compare how different AI models interpret and respond to aesthetic requirements across visual, literary, and interaction-design tasks.

This is an exploratory pilot, not a validated benchmark. The tasks are intentionally varied and should not be used to claim broad model superiority from a small number of outputs.

## 2. Administration protocol

For every model being tested:

1. Use the exact task prompt below. Do not silently rewrite or shorten it.
2. Start a fresh conversation for each task, unless the task explicitly requires follow-up.
3. Record model name, model/version if available, date, interface/API, settings, and exact prompt.
4. Save the complete raw output. For image tasks, save the original generated image as well as the prompt.
5. Do not tell the model which answer or style is preferred.
6. Randomize and anonymize outputs before human scoring when practical.
7. Score each output independently. Record a short piece of observable evidence for every non-neutral score.
8. Do not treat one evaluator's score as general human consensus.

### Suggested pilot size

- 15 tasks × 2 models = 30 outputs.
- Run each task once per model for the first pilot.
- If time permits later, repeat selected tasks to examine output consistency.

## 3. Shared evaluation rules

Use the current Aesthetic Lab rubric. Keep these three records separate:

- **Output quality:** how well the produced image, text, or interaction solution meets the task.
- **Feedback quality:** how well the model diagnoses and proposes revisions, when the task asks for feedback.
- **Instruction following:** Pass / Partial / Fail. Do not merge this with aesthetic quality.

For 1–5 scores, add one or two sentences of evidence. If a criterion cannot be judged from the output, mark it `N/A` rather than guessing.

---

# Part A — Visual Aesthetic Tasks

## V01 — Negative space and visual rhythm

**Capability focus:** spatial organization, negative space, visual rhythm, visual hierarchy.

**Exact prompt**

> Create a visual concept for a minimalist cultural poster about “A quiet morning in the city.” Describe the composition in enough detail that an image-generation model could produce it. The design should use negative space intentionally and establish a calm visual rhythm. Include the main subject, placement, color palette, typography direction, and the relationship between filled and empty areas. Avoid relying on generic words such as “beautiful” or “high quality”; explain the visual decisions.

**What to observe**
- Does the model explain where and why it uses empty space?
- Is there a clear hierarchy rather than arbitrary sparsity?
- Does the rhythm support the quiet-morning theme?

## V02 — Richness with order

**Capability focus:** theme suitability, visual hierarchy, complexity management.

**Exact prompt**

> Create a visual concept for a poster themed “The vitality of a city.” The design should feel energetic and visually rich, but not chaotic. Describe the main elements, their grouping, the composition, color relationships, and how the viewer’s eye should move through the poster. Do not solve the task by making the design extremely minimal. Explain how you would preserve order while using multiple visual elements.

**What to observe**
- Does the model understand that richness can be appropriate to the theme?
- Does it organize complexity through grouping, hierarchy, or rhythm?
- Does it avoid equating “energetic” with random clutter?

## V03 — Multiple expressive strategies

**Capability focus:** emotional expression, expressive strategy, avoidance of single-style bias.

**Exact prompt**

> Develop two clearly different visual directions for the theme “Loneliness in spring.” Direction A should communicate the theme through restraint and sparse composition. Direction B should communicate it through visual abundance and contrast between the environment and the subject’s emotion. For each direction, describe composition, color, subject, atmosphere, and why the strategy can communicate loneliness. Then explain what would make each direction successful rather than merely decorative.

**What to observe**
- Are the two directions genuinely distinct?
- Can both plausibly express the same theme?
- Does the model explain the mechanism of emotional communication rather than just naming a mood?

## V04 — Mood and temporal atmosphere

**Capability focus:** theme alignment, atmosphere, light, visual competition.

**Exact prompt**

> Create a visual concept for “A quiet summer afternoon, when time seems to move slowly.” The scene may include a blue swimming pool, sunlight, tree shadows, and surrounding architecture or plants. Describe how light, shadow, spatial depth, color, and visual density create a quiet sense of time passing. Avoid adding people or decorative objects unless you can explain why they are necessary. Do not assume that a summer scene must feel lively or crowded.

**What to observe**
- Does the model translate “slow time” into observable visual choices?
- Does it manage visual density and focal competition?
- Does it avoid summer clichés that conflict with the requested mood?

## V05 — Actionable visual revision feedback

**Capability focus:** problem diagnosis, actionable revision, target preservation.

**Exact prompt**

> You are reviewing a generated poster for “A quiet summer afternoon.” The image contains a blue swimming pool and sunlight, but it feels generic and visually busy. The tree shadows are weak, and the sense of time passing is missing. Write a concise revision instruction for an image-generation or image-editing model. Organize your feedback into four parts: (1) what to preserve, (2) what to reduce or remove, (3) what to strengthen, and (4) the intended final effect. Be specific enough to guide revision, but do not dictate every pixel or introduce unrelated new elements.

**What to observe**
- Does the model preserve the useful existing elements?
- Does it diagnose concrete issues rather than saying “make it better”?
- Are the changes actionable and aligned with the target mood?

---

# Part B — Literary Aesthetic Tasks

## T01 — Rhythm and restraint

**Capability focus:** sentence rhythm, concision, tonal control.

**Exact prompt**

> Write a short literary paragraph (100–140 Chinese characters) about “A rainy window at dusk.” The tone should be restrained and quiet. Use sentence rhythm and carefully selected concrete details to create atmosphere. Avoid melodramatic emotion, familiar internet-style poetic phrases, and excessive adjectives. After the paragraph, briefly identify two language choices that help create its rhythm.

**What to observe**
- Does the prose use rhythm rather than simply short sentences?
- Are details specific and economical?
- Does the explanation accurately describe the produced text?

## T02 — Concrete imagery and originality

**Capability focus:** imagery, specificity, avoidance of cliché.

**Exact prompt**

> Write a short prose poem (8–12 lines in Chinese) on the theme “The smell of a library after rain.” Build the atmosphere through concrete sensory details. Avoid stock phrases such as “time stands still,” “the fragrance of books,” or “a sea of knowledge.” Do not explain the theme directly. Let the images carry the feeling.

**What to observe**
- Are images concrete and sensory?
- Does the writing avoid predictable metaphors?
- Do the images form a coherent atmosphere rather than a random list?

## T03 — Emotional expression through contrast

**Capability focus:** emotional nuance, indirect expression, expressive strategy.

**Exact prompt**

> Write two short versions (each 80–120 Chinese characters) around the theme “A celebration after someone has left.” Version A should express the emotion directly but subtly. Version B should use environmental details and contrast to imply the emotion without naming it. Keep both versions restrained. Afterward, explain the different expressive strategies in no more than three sentences.

**What to observe**
- Are the two strategies meaningfully different?
- Does the indirect version communicate through details and contrast?
- Is the explanation supported by the text?

## T04 — Style consistency under constraints

**Capability focus:** style coherence, constraint following, tone.

**Exact prompt**

> Write a short museum exhibition introduction in Chinese (120–160 characters) for an imaginary exhibition titled “Things That Almost Disappeared.” The voice should be contemporary, thoughtful, and accessible—not academic, promotional, or sentimental. Include what visitors may encounter and one question the exhibition invites them to consider. Avoid clichés such as “a dialogue between past and present.”

**What to observe**
- Is the tone consistent from beginning to end?
- Does it sound like a real exhibition introduction?
- Does it avoid promotional and academic filler?

## T05 — Quality of literary revision feedback

**Capability focus:** diagnosis, actionable editing, preserving authorial intent.

**Exact prompt**

> Review the following draft: “The night was very quiet. The moon was very bright. I felt very lonely, and the wind was very cold. I walked along the road and thought about many things.” The intended effect is restrained loneliness, not melodrama. First identify the two most important weaknesses in the writing. Then provide a revised version of 50–80 Chinese characters that preserves the original situation and emotional intention while improving rhythm and imagery. Finally, explain what you changed and why.

**What to observe**
- Does the model identify specific weaknesses rather than vague labels?
- Does the revision preserve the original scene and intention?
- Are the edits proportionate rather than overwriting the piece?

---

# Part C — Interaction Aesthetic Tasks

## I01 — Information hierarchy

**Capability focus:** hierarchy, scanability, grouping, clarity.

**Exact prompt**

> Design the information structure for a mobile screen that helps a person choose one of three weekend art workshops. Each workshop has a title, date, duration, location, price, skill level, and a short description. Describe the order and grouping of information, the primary and secondary actions, and what should be visible before scrolling. Explain how the hierarchy helps a first-time visitor compare the options.

**What to observe**
- Is the most decision-relevant information easy to find?
- Are related details grouped logically?
- Is the primary action clear without competing actions?

## I02 — Clarity of action

**Capability focus:** affordance, labels, error prevention, task completion.

**Exact prompt**

> Improve the interaction flow for a simple form that lets a user register for an art workshop. The form asks for name, email, selected session, and payment confirmation. Describe the steps, button labels, field guidance, and what happens after submission. Make the flow clear for a first-time user. Include how the interface should prevent common mistakes without adding unnecessary steps.

**What to observe**
- Are labels and next steps unambiguous?
- Does the design prevent errors at the right moment?
- Does it avoid unnecessary friction?

## I03 — Feedback and reassurance

**Capability focus:** system feedback, status visibility, emotional tone.

**Exact prompt**

> A user has just submitted an application for a limited-capacity art workshop. Design the confirmation and follow-up feedback. Describe the immediate success message, what information should be shown, what happens if the application is waitlisted, and how the user can check status later. The tone should be calm and reassuring, but must not promise a place before it is confirmed.

**What to observe**
- Does the system clearly communicate the current status?
- Does it distinguish confirmed from waitlisted?
- Is the tone reassuring without making unsupported promises?

## I04 — Cognitive load and accessibility

**Capability focus:** cognitive load, accessibility, inclusive interaction.

**Exact prompt**

> Review a mobile event-discovery screen that shows 20 event cards, several filter controls, promotional banners, and multiple competing buttons. Propose a redesign that reduces cognitive load while preserving useful choice. Describe what to prioritize, group, hide until needed, or remove. Include at least three accessibility considerations. Explain the trade-offs of your redesign.

**What to observe**
- Does the model prioritize rather than merely remove everything?
- Are accessibility suggestions concrete?
- Does it explain trade-offs between simplicity and discoverability?

## I05 — Interaction revision feedback

**Capability focus:** issue diagnosis, revision specificity, user-goal preservation.

**Exact prompt**

> A prototype for booking an art workshop has received this feedback: “I cannot tell which session I selected, the payment button looks like a secondary link, and after submitting I do not know whether the booking succeeded.” Turn this feedback into a prioritized revision brief. For each issue, state the likely user problem, the proposed interface change, and how the change would improve the experience. Preserve the goal of a simple booking flow; do not add features unrelated to the problems.

**What to observe**
- Does the model connect interface symptoms to user problems?
- Are proposed changes concrete and prioritized?
- Does it preserve the simple booking goal?

---

## 4. Output recording template

Create one record for each model-task output. Suggested filename:

`dataset/outputs/<task-id>_<model-short-name>_<date>.md`

Copy this template:

```markdown
# Output Record

- Task ID:
- Model:
- Model/version:
- Date and time:
- Interface/API:
- Settings (if known):
- Run number:
- Exact prompt:
- Raw output or asset path:

## Instruction following
- Result: Pass / Partial / Fail
- Evidence:

## Human evaluation
| Dimension | Score (1–5 or N/A) | Evidence |
|---|---:|---|
| Task suitability | | |
| Clarity / organization | | |
| Style coherence | | |
| Emotional or experiential effect | | |
| Originality / specificity | | |

## Feedback quality (if applicable)
| Dimension | Score (1–5 or N/A) | Evidence |
|---|---:|---|
| Problem diagnosis | | |
| Actionability | | |
| Goal preservation | | |

## Notes
- Strong points:
- Weak points:
- Potential bias or uncertainty:
```

## 5. Important methodological cautions

- Do not compare raw scores across visual, literary, and interaction tasks as if they measured exactly the same ability.
- Do not change prompts halfway through a comparison. If a prompt is revised, assign a new version number.
- Keep model identity hidden from evaluators when practical.
- For image generation, note that random seeds, image dimensions, and generation settings can affect results. Record them when available.
- A single output is not enough to establish consistency.
- The task set reflects the project's current research questions and may contain evaluator bias. Revise it after the pilot and document every change.

## 6. Next step

Run V01 with two models first. Check whether the prompt is understandable and whether the output-record template is usable. If the procedure works, continue with the remaining 14 tasks.
