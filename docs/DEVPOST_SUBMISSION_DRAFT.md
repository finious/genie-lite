# Devpost Submission Draft — Genie Lite

## One-line summary

Genie Lite is a human-led AI proof showing how conversational intent can route to specialist work without transferring human authority, with inspectable receipts for routing, correction, recovery, and limits.

## What it does

Genie Lite separates three things that AI systems often blur together: conversation, specialist work, and authority.

A human speaks to Echo. Echo carries the request to a bounded CREATE specialist. CREATE returns specialist work. Echo brings the result back without claiming authority it does not have. If the human corrects the direction, the next specialist brief/result must materially change. Receipts make the route, return, authority state, and unproven claims inspectable.

The frozen contest seam is:

> **JIMMY → ECHO → CREATE → ECHO → JIMMY**

## Why we built it

The central problem is not just whether an AI can do useful work. It is whether a human can tell what happened, who did what, what remains unproved, and whether old authority silently leaked across interruption or recovery.

Genie Lite treats those boundaries as part of the product.

## How it works

- **Echo** is the conversational bridge.
- **CREATE** is one visible specialist behind a bounded route.
- **Authority state** stays explicit instead of being inferred from conversational continuity.
- **Receipts** record request, route, specialist return, authority state, and claim limits.
- **Recovery** restores useful state without silently restoring stale consequential authority.

## Built with

- Strands Agents
- Amazon Bedrock AgentCore
- Amazon Nova Pro (`amazon.nova-pro-v1:0`)
- Python
- AgentCore CodeZip deployment

## What is proved

- six deterministic credit-free tests pass
- Echo→CREATE routing is visible
- correction changes the next specialist brief/artifact in deterministic proof
- stale consequential authority expires on recovery
- receipts expose authority state and claim limits
- AgentCore configuration validates
- the public repository is receiver-readable
- Genie Lite is deployed to AgentCore in `us-east-1`
- AgentCore reports the runtime as deployed and `READY`
- post-deploy diff reports no changes

## Current live-provider limitation

The first deployed Nova invocation reached the runtime but was blocked by a provider daily-token `ThrottlingException`. We preserved that as an inspectable limitation instead of changing models, regions, or architecture to manufacture a green result.

If the quota clears before judging/submission close, we will add the deployed normal/correction trace as an evidence upgrade. The deployed runtime and deterministic proof already exist independently of that provider quota.

## What we do not claim

Genie Lite is not presented as production-ready, as managed long-term memory, or as a generalized AI companion. It does not claim managed durable recovery or automatic continuation of authority after interruption.

## What we learned

A useful human-led agent system needs more than capability. It needs boundaries that survive handoffs and interruption:

> Conversation does not equal authority. Routing does not equal execution. Recovery does not equal permission to resume.

The design goal is to let the human carry less operational complexity without surrendering the decisions that matter.

## Repository

https://github.com/finious/genie-lite
