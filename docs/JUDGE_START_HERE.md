# Judge Start Here

## Genie Lite in 30 seconds

**Track:** Professional Agents

Genie Lite is a human-led AI agent built with Strands Agents and deployed on Amazon Bedrock AgentCore.

It solves a coordination problem that appears as soon as AI work becomes multi-step: the human needs to know what they asked for, which specialist did the work, whether a correction changed the result, what authority still applies, and what remains unproved after interruption.

The core seam is:

> **HUMAN → ECHO → CREATE → ECHO → HUMAN**

- **Echo** receives and carries human intent.
- **CREATE** performs bounded specialist work.
- **Receipts** expose routing, return, authority state, and limits.
- **Recovery** restores useful state without silently restoring stale consequential authority.

## What is working

- six deterministic tests pass
- Echo→CREATE routing is visible
- correction changes the next specialist brief/artifact
- stale consequential authority expires after interruption
- AgentCore configuration validates
- AgentCore deployment completed successfully
- deployed runtime reports `READY`
- post-deploy diff is clean

## Current limitation

The first deployed Nova invocation reached the runtime but was throttled by the provider daily token quota. The project does not claim a successful deployed model conversation until that trace actually completes.

## Inspect in this order

1. [`README.md`](../README.md) — problem, product, setup, current status
2. [`ARCHITECTURE.md`](ARCHITECTURE.md) — system design
3. [`EVIDENCE_AND_CLAIM_FENCE.md`](EVIDENCE_AND_CLAIM_FENCE.md) — proved / blocked / not claimed
4. [`DEMO_SCRIPT_TWO_BRANCHES.md`](DEMO_SCRIPT_TWO_BRANCHES.md) — live-proof or provider-throttle demo path
5. [`DEVPOST_SUBMISSION_DRAFT.md`](DEVPOST_SUBMISSION_DRAFT.md) — contest narrative
6. [`evidence/DEPLOYED_RUNTIME_AND_THROTTLE_RECEIPT_2026-09-13.md`](evidence/DEPLOYED_RUNTIME_AND_THROTTLE_RECEIPT_2026-09-13.md) — deployment/runtime receipt

## The point

Genie Lite is not trying to make an agent look more autonomous.

It is trying to make delegated AI work **more inspectable, correctable, resumable, and human-led**.
