# Devpost Submission Draft — Genie Lite

## Track

**Professional Agents**

## Tagline

Human-led specialist routing with explicit authority, correction, recovery, and receipts.

## One-line summary

Genie Lite is a Strands-based professional agent that carries human intent into specialist work without silently transferring human authority.

## The problem

As professionals use AI for more than one-shot answers, the coordination burden grows fast. A person has to remember what they asked for, which capability did the work, whether a correction actually changed the work, what is safe to resume after interruption, and what the system has or has not actually proved.

Most agent experiences optimize for capability. Genie Lite focuses on **inspectability under delegation**.

## Who it is for

Professionals, makers, creators, and small teams using AI across multi-step or specialist work where correction, handoff, recovery, and human authority matter.

## What Genie Lite does

A human speaks to **Echo**, the conversational bridge. Echo carries the request to **CREATE**, one bounded specialist. CREATE returns specialist work through Echo. If the human corrects the direction, the next specialist brief and result must materially change. Receipts expose the route, return, authority state, and claim limits.

The contest seam is:

> **HUMAN → ECHO → CREATE → ECHO → HUMAN**

Recovery restores useful state, but stale consequential authority does not silently resume.

## Why it matters

The human should be able to carry less operational complexity without surrendering the decisions that matter.

Genie Lite makes four distinctions visible:

> Conversation does not equal authority.  
> Routing does not equal execution.  
> Execution does not equal verification.  
> Recovery does not equal permission to resume.

## Built with

- Strands Agents
- Amazon Bedrock AgentCore
- Amazon Nova Pro (`amazon.nova-pro-v1:0`)
- Python
- AgentCore CodeZip deployment

## Technical implementation

Genie Lite uses a Strands/AgentCore runtime with one visible specialist route. The implementation includes explicit state, authority, correction, recovery, and receipt behavior rather than burying those boundaries in the system prompt.

The project is deployed to Amazon Bedrock AgentCore in `us-east-1`; AgentCore reports the runtime as deployed and `READY`. A post-deploy diff reports no infrastructure drift.

## What is proved

- six deterministic credit-free tests pass
- Echo→CREATE routing is visible
- correction changes the next specialist brief/artifact
- receipts expose route, return, authority state, and limits
- stale consequential authority expires after interruption/recovery
- AgentCore configuration validates
- public repository is receiver-readable
- AgentCore deployment completed successfully
- runtime reports deployed / `READY`
- post-deploy diff reports no differences

## Current live-provider limitation

The first deployed Amazon Nova Pro invocation reached the runtime but returned a provider daily-token `ThrottlingException`.

We preserved that as an inspectable limitation instead of changing models, regions, or architecture to manufacture a green result. If the quota clears before submission close, the deployed normal/correction trace will be added as an evidence upgrade.

Until then, we do **not** claim a successful deployed model conversation.

## What we do not claim

Genie Lite is not presented as production-ready, managed long-term memory, a generalized AI companion, or managed durable recovery. It does not automatically continue human authority after interruption.

## What we learned

A useful human-led agent system needs more than capability. It needs boundaries that survive correction, handoff, and interruption.

The most important design lesson was:

> **The human can carry less complexity without giving the system more authority.**

## Repository

https://github.com/finious/genie-lite

## Judge path

https://github.com/finious/genie-lite/blob/main/docs/JUDGE_START_HERE.md
