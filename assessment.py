"""Validate a simple readiness assessment and produce a Markdown gap report."""
import argparse
import json
from pathlib import Path

DOMAINS = {
    "cloud_migration": "Cloud migration",
    "application_modernization": "Application modernization",
    "custom_software": "Custom software development",
    "ai_infrastructure": "AI server infrastructure",
    "network_optimization": "Network optimization",
}


def validate(data):
    if not isinstance(data, dict) or not isinstance(data.get("organization"), str):
        raise ValueError("Input needs an organization string")
    domains = data.get("domains")
    if not isinstance(domains, dict) or set(domains) != set(DOMAINS):
        raise ValueError("domains must contain exactly the five documented workstreams")
    for key, items in domains.items():
        if not isinstance(items, list) or not items:
            raise ValueError(f"{key} must contain at least one assessment item")
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get("question"), str) or not item["question"].strip():
                raise ValueError(f"{key}: each item requires a question")
            score = item.get("score")
            if type(score) is not int or score not in range(4):
                raise ValueError(f"{key}: score must be an integer from 0 to 3")
            for optional in ("owner", "evidence"):
                if optional in item and not isinstance(item[optional], str):
                    raise ValueError(f"{key}: {optional} must be text")
    return data


def report(data):
    validate(data)
    lines = [f"# Readiness action plan — {data['organization']}", "", "Self-assessed planning gaps, not a production certification.", ""]
    ranked = []
    for key, label in DOMAINS.items():
        items = data["domains"][key]
        gap = sum(3 - item["score"] for item in items)
        maximum = 3 * len(items)
        ranked.append((gap / maximum, key, label, items, gap, maximum))
    lines += ["## Workstream overview", "", "| Workstream | Gap points | Gap ratio |", "| --- | ---: | ---: |"]
    for ratio, _, label, _, gap, maximum in sorted(ranked, reverse=True):
        lines.append(f"| {label} | {gap}/{maximum} | {ratio:.0%} |")
    lines += ["", "## Prioritized follow-ups", ""]
    count = 0
    for _, _, label, items, _, _ in sorted(ranked, reverse=True):
        for item in sorted(items, key=lambda i: i["score"]):
            if item["score"] == 3:
                continue
            count += 1
            owner = item.get("owner") or "Unassigned"
            evidence = item.get("evidence") or "Not provided"
            lines.append(f"{count}. **{label} — {item['question']}** (score {item['score']}/3; owner: {owner}; evidence: {evidence})")
    if count == 0:
        lines.append("All items are self-reported as operational. Independently validate evidence and revisit periodically.")
    lines += ["", "## Suggested next steps", "", "1. Verify each low-scoring item against actual evidence.", "2. Identify dependencies, security constraints, and rollback requirements.", "3. Assign accountable owners and target dates in your delivery tracker.", "4. Reassess after each migration or deployment milestone.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("action-plan.md"))
    args = parser.parse_args()
    result = report(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.write_text(result, encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
