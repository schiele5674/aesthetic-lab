# Aesthetic Evaluation Rubric 0.1

Use a 1–5 scale for each criterion. Score only what is observable in the output relative to the task brief.

## Shared scale

| Score | Anchor |
|---|---|
| 1 | Major problems; does not meaningfully satisfy the criterion |
| 2 | Weak; several noticeable problems |
| 3 | Adequate; acceptable but inconsistent or generic |
| 4 | Strong; clear evidence of quality with minor weaknesses |
| 5 | Excellent; especially coherent, purposeful, and well-executed |

Do not use half-points in the first pilot. Add evidence for every score.

## Visual track

| Criterion | What to inspect |
|---|---|
| Composition | Hierarchy, balance, focal point, visual flow |
| Color | Palette relationships, contrast, saturation, harmony |
| Space | Negative space, depth, layering, spatial clarity |
| Style coherence | Consistency with the requested visual language |
| Mood | Whether the image communicates the intended atmosphere |

## Literary track

| Criterion | What to inspect |
|---|---|
| Precision | Word choice and clarity |
| Rhythm | Sentence variation, pacing, sound and flow |
| Imagery | Specific, meaningful images rather than generic decoration |
| Originality | Avoidance of predictable phrases and unnecessary imitation |
| Emotional effect | Whether the intended feeling emerges naturally |

## Interaction track

| Criterion | What to inspect |
|---|---|
| Intent understanding | Responds to what the user is likely asking or expressing |
| Naturalness | Conversational rather than formulaic |
| Tact | Appropriate warmth, restraint, and boundaries |
| Relevance and density | Useful detail without unnecessary length |
| Adaptability | Responds to context and stated constraints |

## Separate instruction-following check

Record whether the output followed the explicit task constraints. Use:
- `pass`
- `partial`
- `fail`

Do not merge this field into the aesthetic score. An output can be beautiful but fail the brief, or follow the brief but feel generic.

## Required evaluation record

For every output, record:
- task ID
- anonymized output ID
- evaluator ID or pseudonym
- five criterion scores
- instruction-following result
- preferred output in pairwise comparison, if applicable
- a short rationale with concrete evidence
- one strength and one weakness

## Bias and reliability notes

- Hide model names during scoring when practical.
- Randomize output order.
- Keep the prompt and generation conditions identical across models.
- Do not treat one person's ratings as consensus.
- If adding evaluators, report disagreement and consider an agreement statistic.
- Review whether a rubric criterion is ambiguous before interpreting low agreement as model failure.
