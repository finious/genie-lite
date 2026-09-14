# Genie Lite

Genie Lite is a contest-sized proof of one claim:

> Echo can carry human intent into specialist work without becoming the specialist, while preserving human authority and inspectable receipts.

The frozen seam is **JIMMY → ECHO → CREATE → ECHO → JIMMY**.

Genie Lite is built with Strands and deployed to Amazon Bedrock AgentCore in `us-east-1` using `amazon.nova-pro-v1:0`.

## Current status

**PROVED**

- visible Echo-to-CREATE routing in the deterministic specimen
- correction propagation into the next brief and artifact
- explicit authority state and claim limits in receipts
- useful state recovery with stale consequential authority expired
- six credit-free deterministic tests passing
- AgentCore configuration validation
- public GitHub custody and receiver-readable handoff

**DEPLOYED**

- AgentCore stack deployed successfully
- GenieLite runtime reports `READY`
- follow-up CDK diff reports no differences
- repeated deploy reports no changes

**BLOCKED**

- the first deployed Nova invocation reached the runtime but was throttled by the provider daily token quota
- therefore the final deployed normal/correction live trace is not yet proved

**NOT CLAIMED**

- production readiness
- managed cloud memory
- generalized long-term companionship
- automatic continuation of authority after interruption
- managed durable recovery
- successful deployed model behavior until a live invocation completes

## Why this matters

Genie Lite separates conversational continuity from specialist work and from human authority.

Conversation does not equal authority. Routing does not equal execution. Recovery does not equal permission to resume. Receipts make those boundaries inspectable.

## Architecture

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Evidence

See [`docs/EVIDENCE_AND_CLAIM_FENCE.md`](docs/EVIDENCE_AND_CLAIM_FENCE.md) and [`docs/BUILD_STATUS_2026-09-13.md`](docs/BUILD_STATUS_2026-09-13.md).

## Test without model calls

```bash
cd app/GenieLite
python -m unittest discover -s tests -v
```

## Local validation

```bash
agentcore validate --json
./scripts/check-local.sh
```

## Frozen live proof inputs

Normal request:

```text
I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds.
```

Correction:

```text
Don't sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center.
```

The live proof passes only if the correction materially changes the next brief/result and the returned receipt preserves the human authority boundary.

## Deployment

Deployment was explicitly authorized and completed. The runtime is `READY` in AgentCore. The remaining live-model gap is provider throttling on Nova invocation, preserved as an external limitation rather than hidden or routed around.

## Continue safely

Start with [`CONTINUE_HERE.md`](CONTINUE_HERE.md).
