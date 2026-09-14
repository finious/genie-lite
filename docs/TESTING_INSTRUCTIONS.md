# Testing Instructions

## Deterministic proof

From the repository root:

```bash
cd app/GenieLite
uv sync
uv run python -m unittest discover -s tests -v
```

Expected result: six tests pass.

These tests cover the contest mechanism without requiring model tokens:

- visible Echo → CREATE routing
- correction propagation
- explicit authority state and claim limits
- recovery of useful state with stale consequential authority expired
- inspectable receipts

## AgentCore validation

From the repository root:

```bash
agentcore validate --json
./scripts/check-local.sh
```

Expected result: AgentCore validation succeeds, Nova Pro is configured, and tutorial/example defaults are absent.

## Deployed runtime status

The project has been deployed to Amazon Bedrock AgentCore in `us-east-1`. The runtime has reported `deploymentState: deployed` and detail `READY`.

The first deployed Nova invocation returned a provider daily-token throttling error. Until a deployed normal/correction trace completes successfully, the project does not claim successful deployed model behavior.

See [`EVIDENCE_AND_CLAIM_FENCE.md`](EVIDENCE_AND_CLAIM_FENCE.md) for the exact evidence boundary.
