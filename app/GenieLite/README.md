# Genie Lite application

This directory contains the deployable Strands/AgentCore application for Genie Lite.

For the contest overview, architecture, evidence boundary, setup instructions, and judge path, start at the repository root:

- [`../../README.md`](../../README.md)
- [`../../docs/JUDGE_START_HERE.md`](../../docs/JUDGE_START_HERE.md)

## Deterministic tests

```bash
uv sync
uv run python -m unittest discover -s tests -v
```

## Runtime

- Strands Agents
- Amazon Bedrock AgentCore
- Amazon Nova Pro (`amazon.nova-pro-v1:0`)
- CodeZip deployment

The public evidence boundary is maintained in [`../../docs/EVIDENCE_AND_CLAIM_FENCE.md`](../../docs/EVIDENCE_AND_CLAIM_FENCE.md).
