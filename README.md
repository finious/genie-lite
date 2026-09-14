# Genie Lite

**Agents for Humans Hackathon · Professional Agents**

Genie Lite is a human-led AI agent built with **Strands Agents** and deployed on **Amazon Bedrock AgentCore**. It tests a practical question:

> Can a conversational AI carry human intent into specialist work without becoming the specialist or silently inheriting human authority?

The contest seam is:

> **HUMAN → ECHO → CREATE → ECHO → HUMAN**

Echo is the conversational bridge. CREATE is the bounded specialist. Receipts make the route, return, authority state, correction, and limits inspectable.

## The problem

Professionals increasingly work through AI across multiple tasks and specialist capabilities. The hard part is not only getting useful output. It is keeping track of what the human asked for, which specialist did the work, whether a correction actually changed the work, what authority still applies, and what remains unproved after interruption.

Genie Lite reduces that coordination burden without turning conversational continuity into hidden permission.

## What it demonstrates

- visible Echo → CREATE specialist routing
- correction propagation into the next brief and artifact
- explicit authority state and claim limits in receipts
- recovery of useful state while stale consequential authority expires
- six deterministic, credit-free tests
- AgentCore validation
- successful AgentCore deployment in `us-east-1`
- deployed runtime state: `READY`
- clean post-deploy diff / no-change redeploy

## Current live-runtime limitation

The first deployed Nova invocation reached the runtime but returned a provider daily-token `ThrottlingException`. That limitation is preserved as evidence rather than hidden or routed around.

So the current evidence boundary is precise:

- **deployment:** proved
- **runtime READY:** proved
- **deterministic behavior:** proved
- **successful deployed Nova normal/correction trace:** not yet proved

See [`docs/EVIDENCE_AND_CLAIM_FENCE.md`](docs/EVIDENCE_AND_CLAIM_FENCE.md).

## Why it matters

Genie Lite separates things agent systems often blur together:

> **Conversation does not equal authority.**  
> **Routing does not equal execution.**  
> **Recovery does not equal permission to resume.**

The design goal is simple: let the human carry less operational complexity without surrendering the decisions that matter.

## Architecture

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Quick start

### Prerequisites

- Python 3.10+
- `uv`
- AWS CLI credentials for an account with Amazon Bedrock access
- AgentCore CLI
- access to `amazon.nova-pro-v1:0` in `us-east-1`

### Install and run deterministic tests

```bash
git clone https://github.com/finious/genie-lite.git
cd genie-lite/app/GenieLite
uv sync
uv run python -m unittest discover -s tests -v
```

### Validate the AgentCore project

From the repository root:

```bash
agentcore validate --json
./scripts/check-local.sh
```

### Local AgentCore development

```bash
agentcore dev
```

Then invoke locally with the frozen normal request:

```bash
agentcore invoke --local '{"prompt":"I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds."}'
```

Follow with the correction:

```bash
agentcore invoke --local '{"prompt":"Don’t sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center."}'
```

The proof passes only if the correction materially changes the next brief/result and the returned receipt preserves the human authority boundary.

## Built with

- Strands Agents
- Amazon Bedrock AgentCore
- Amazon Nova Pro (`amazon.nova-pro-v1:0`)
- Python
- AgentCore CodeZip deployment

## Judge path

Start with [`docs/JUDGE_START_HERE.md`](docs/JUDGE_START_HERE.md).

## License

MIT. See [`LICENSE`](LICENSE).
