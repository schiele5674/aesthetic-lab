# Aesthetic Lab

**Exploring Aesthetic Intelligence in AI**

A personal research and engineering project exploring how AI systems respond to human aesthetic preferences across visual, literary, and interaction tasks.

> Status: Early exploration · Version 0.1 · Started 2026-11-12

## Mission

Aesthetic Lab studies how to make aesthetic judgments about AI outputs more explicit, testable, and useful for model evaluation and improvement.

This project combines:
- **Aesthetic research:** define observable criteria for visual, literary, and interaction quality.
- **Human evaluation:** collect reasoned preferences and identify failure cases.
- **AI engineering:** use Python, model APIs, and coding agents to organize and analyze experiments.
- **Agent workflows:** gradually automate repeatable research tasks while keeping human judgment in the loop.

## Research questions

1. Which qualities make an AI-generated output feel aesthetically successful for a given task?
2. Can evaluators apply a shared rubric consistently?
3. Where do model outputs fail despite following the literal instruction?
4. Can structured feedback and better task specifications improve subsequent outputs?
5. Which parts of evaluation can be automated, and which require human judgment?

## Research tracks

| Track | Scope | Initial focus |
|---|---|---|
| Visual Intelligence | Composition, color, space, style, mood | Does an image satisfy a clearly stated visual intention? |
| Literary Intelligence | Rhythm, imagery, precision, originality, emotional effect | Does a text communicate with nuance rather than cliché? |
| Interaction Intelligence | Context, naturalness, tact, relevance, adaptability | Does a response fit the user's intent and conversational context? |
| Agent Engineering | Data collection, scoring, analysis, reproducibility | Can repeatable evaluation steps be safely automated? |

## Repository structure

```text
aesthetic-lab/
├── README.md
├── LICENSE
├── .gitignore
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
│   └── score_calculator.py
├── results/
├── agent/
│   └── README.md
└── journal/
    └── 2026-11-12-day-01.md
```

## First experiment: Aesthetic Benchmark 0.1

**Question:** Given the same task, how do two selected AI models differ in perceived quality and instruction fulfilment across visual, literary, and interaction outputs?

### Pilot protocol

- Prepare 15 tasks: 5 visual, 5 literary, 5 interaction.
- Run each task once on each of two selected models: 30 outputs total.
- Record exact prompt, model name/version, date, settings, and output.
- Randomize or conceal model identity during human evaluation where practical.
- Score each output on task-specific criteria using a 1–5 scale.
- Record a short reason and at least one concrete strength or failure case.
- Treat the first round as an exploratory pilot, not a general claim about model quality.

### Important methodological notes

- Do not compare image and text scores as if they were directly equivalent.
- Keep instruction-following separate from aesthetic quality.
- One evaluator's scores represent that evaluator's preferences, not universal human consensus.
- If multiple evaluators join, report agreement and disagreements rather than hiding them.
- Record model versions and generation settings. If they change, treat the run as a new condition.
- Do not claim that prompting has changed model weights. Prompt iteration is not model fine-tuning.

## Getting started

### 1. Open the project

Open this folder in VS Code or another code editor.

### 2. Start with the research documents

Read:
- `research/research-question.md`
- `research/evaluation-rubric.md`
- `journal/2026-11-12-day-01.md`

### 3. Add experimental data

Use the templates in `dataset/`. Keep raw outputs unchanged. Store evaluations separately.

### 4. Run the score calculator

Requires Python 3.10+.

```bash
python src/score_calculator.py --input dataset/human-evaluations/sample_scores.json --output results/summary.json
```

### 5. Version your work with Git

```bash
git init
git add .
git commit -m "Initialize Aesthetic Lab research project"
```

Create an empty GitHub repository named `aesthetic-lab`, then connect it:

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/aesthetic-lab.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Never put API keys, passwords, private data, or access tokens in this repository.

## Current status

- [x] Project scope and initial repository structure
- [x] First research journal entry
- [x] Initial rubric draft
- [ ] Select two accessible models and record exact versions
- [ ] Complete 15 benchmark prompts
- [ ] Collect 30 outputs
- [ ] Conduct human evaluation
- [ ] Analyze results and write the first report
- [ ] Build a repeatable evaluation workflow

## License and responsible use

This project is for research and learning. Respect model providers' terms, image and text copyrights, privacy, and dataset licenses. Obtain consent before collecting personal or sensitive conversation data. Document limitations and avoid presenting subjective judgments as objective facts.
