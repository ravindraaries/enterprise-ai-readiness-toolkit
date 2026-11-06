# Enterprise AI Readiness Toolkit

A lightweight, vendor-neutral **assessment toolkit** for planning cloud migration, application modernization, custom integrations, AI serving infrastructure, and network optimization.

> This is a planning aid, not a security audit, production deployment blueprint, or validated cost model. The sample data is fictional.

## What is included

- `assessment.py` — a dependency-free Python CLI that validates an assessment JSON and produces a prioritized Markdown action plan.
- `examples/sample_assessment.json` — fictional input covering all five domains.
- `docs/assessment-checklist.md` — review questions for architects and IT leaders.
- `docs/architecture.md` — Mermaid reference architecture and deployment considerations.
- `tests/test_assessment.py` — basic automated checks.

## Quick start

Requires Python 3.10+; no third-party packages.

```bash
python assessment.py examples/sample_assessment.json --output action-plan.md
python -m unittest discover -s tests -v
```

The tool scores **readiness gaps** on a 0–3 scale per question (`0` = not started, `1` = planned, `2` = partly implemented, `3` = operational and verified). Scores are *self-reported* and only indicate where a team should investigate next. A higher gap score means more attention is needed; this is not a certification or an objective benchmark.

## Five workstreams

| Workstream | What to assess | Related market context |
| --- | --- | --- |
| Cloud migration | Workload inventory, dependencies, migration and rollback plans | [Cloud Migration Services](https://www.kbvresearch.com/cloud-migration-services-market/) |
| Application modernization | Service boundaries, progressive cutover, testing | [Application Modernization Services](https://www.kbvresearch.com/application-modernization-services-market/) |
| Custom software development | API contracts, integration, CI/CD | [Custom Software Development](https://www.kbvresearch.com/custom-software-development-market/) |
| AI server infrastructure | Model requirements, serving capacity, observability | [AI Server](https://www.kbvresearch.com/ai-server-market/) |
| Network optimization | Latency budgets, connectivity, resilience | [Network Optimization Services](https://www.kbvresearch.com/network-optimization-services-market/) |

The KBV links are optional background reading about the corresponding markets; they do not provide evidence for the toolkit's scoring rubric.

## How to adapt

Copy `examples/sample_assessment.json`, replace the fictional organization name, and edit each item's `score`, `owner`, and `evidence`. Avoid entering secrets, personal data, or confidential infrastructure details into public repositories. Run the CLI against your private copy.

## Engineering references

- [AWS Prescriptive Guidance: seven migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html)
- [Microsoft: Strangler Fig pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)
- [NVIDIA Triton Inference Server documentation](https://docs.nvidia.com/triton-inference-server/index.html)

## License

MIT — see `LICENSE`.
