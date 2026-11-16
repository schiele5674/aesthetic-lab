# Style Preference Bias Framework v0.1

## 1. Research Purpose

This framework is designed to investigate whether multimodal AI models demonstrate recurring preferences for particular visual styles when evaluating images under different design goals.

The purpose is to distinguish general aesthetic preference from goal-oriented visual judgment.

## 2. Operational Definition

Style Preference Bias refers to a potential tendency of an AI model to repeatedly favor or reject certain visual styles without sufficient consideration of the specified design goal.

A negative evaluation of a particular style does not automatically indicate bias.

A potential bias should be considered only when the model's judgments repeatedly show insufficient goal sensitivity or rely on unsupported assumptions about visual quality.

## 3. Candidate Bias Categories

The following categories are exploratory coding categories, not confirmed model defects.

| Category | Description |
|---|---|
| Minimalism Bias | Excessive preference for minimalist visual compositions |
| Low-saturation Bias | Excessive preference for muted or low-saturation colors |
| Symmetry Bias | Excessive preference for symmetrical compositions |
| Typography Bias | Excessive preference for particular typography styles |
| Complexity Aversion | Unjustified rejection of complex visual compositions |

## 4. Coding Procedure

For each AI evaluation response, record:

1. Image ID
2. Design Goal
3. Model Name
4. Observed Visual Style
5. Model's Positive or Negative Style Judgment
6. Visual Evidence Provided by the Model
7. Whether the Judgment Is Supported by the Design Goal
8. Potential Bias Category
9. Coding Confidence

## 5. Bias Indicator

Use the following preliminary coding scale:

- 0 — No observable bias indicator
- 1 — Possible bias indicator; insufficient evidence
- 2 — Clear bias indicator in this individual response

A score of 2 indicates a clear indicator in one response, not proof of a stable model-level bias.

## 6. Evidence Requirements

A potential bias indicator should be supported by observable evidence in the model's response.

Examples:

- Rejecting high-saturation colors without explaining their conflict with the design goal.
- Treating complex compositions as inherently inferior.
- Recommending minimalist design regardless of the specified audience or communication objective.

The researcher must distinguish unsupported aesthetic assumptions from justified design criticism.

## 7. Cross-Case Analysis

Potential recurring bias patterns should be examined across:

- Different images
- Different design goals
- Different models

Repeated patterns across multiple independent cases may provide preliminary evidence of a style preference tendency.

A small exploratory dataset cannot establish universal model behavior.

## 8. Research Limitations

- The original design intention of selected images may be unknown.
- Visual style classifications are preliminary.
- Human evaluation may be affected by individual aesthetic preferences.
- Model responses may be influenced by prompt wording and task interpretation.
- Observed output patterns do not reveal the model's internal training mechanism.

## 9. Current Research Status

This framework defines a preliminary method for investigating Style Preference Bias.

No stable model-level bias has been established at this stage.

Findings will be updated only after sufficient experimental records have been collected and analyzed.
