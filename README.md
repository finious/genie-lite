# Genie Lite

Genie Lite is a contest-sized proof of one claim:

> Echo can carry human intent into specialist work without becoming the
> specialist, while preserving human authority and inspectable receipts.

The frozen seam is **JIMMY → ECHO → CREATE → ECHO → JIMMY**.

This Strands application is scaffolded for Amazon Bedrock AgentCore. Echo is
the conversational bridge. CREATE is one bounded specialist behind a visible
tool boundary. The runtime explicitly uses `amazon.nova-pro-v1:0` for the
AWS-sponsored workshop credit path.

## Demonstrated by the credit-free tests

- visible Echo-to-CREATE routing
- correction propagation into the next brief and artifact
- explicit authority state and claim limits in receipts
- useful state recovery with stale consequential authority expired

## Not claimed

- production readiness or managed cloud memory
- generalized long-term companionship
- automatic continuation of authority after interruption
- deployment or verification when only a proposal was produced

## Test without model calls

```bash
cd app/GenieLite
python -m unittest discover -s tests -v
```

## Run locally with Nova

```bash
agentcore validate
agentcore dev
```

Then, in another terminal:

```bash
agentcore invoke --local '{"prompt":"I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds."}'
```

Follow with the frozen correction:

```bash
agentcore invoke --local '{"prompt":"Don’t sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center."}'
```

## Deployment gate

Local build authority is not deployment authority. Pass tests, capture the
normal/correction/recovery evidence, perform a clean-clone run, validate and
inspect the package and AWS target, return cost/IAM/region consequences to
Jimmy, then stop for the exact human gate: **AUTHORIZE DEPLOY**.

No AWS resources have been deployed by this build.
