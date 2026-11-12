"""Summarize simple 1–5 human evaluation scores.

Example:
python src/score_calculator.py \
  --input dataset/human-evaluations/sample_scores.json \
  --output results/summary.json
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path


def summarize(data):
    grouped = defaultdict(lambda: defaultdict(list))
    for record in data.get("records", []):
        model = record.get("model_label", "Unlabeled")
        for criterion, score in record.get("scores", {}).items():
            if isinstance(score, (int, float)) and 1 <= score <= 5:
                grouped[model][criterion].append(score)

    result = {}
    for model, criteria in grouped.items():
        result[model] = {
            criterion: {
                "mean": round(sum(values) / len(values), 2),
                "n": len(values),
            }
            for criterion, values in criteria.items()
        }
    return {
        "study_id": data.get("study_id"),
        "notice": "Descriptive summary only; example records may be placeholders.",
        "by_model": result,
    }


def main():
    parser = argparse.ArgumentParser(description="Summarize Aesthetic Lab scores.")
    parser.add_argument("--input", required=True, help="Path to evaluation JSON.")
    parser.add_argument("--output", required=True, help="Path for summary JSON.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    summary = summarize(data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Summary saved to: {output_path}")


if __name__ == "__main__":
    main()
