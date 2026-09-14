# DEPLOYED RUNTIME AND THROTTLE RECEIPT

**Date:** 2026-09-13  
**Status:** DEPLOYED / READY / LIVE INVOCATION THROTTLED

## Deployment evidence

The authorized Genie Lite deployment completed successfully in Amazon Bedrock AgentCore in `us-east-1`.

Observed deployment sequence:

- CDK bootstrap completed.
- Deployment diff showed one expected AgentCore stack.
- The stack created the runtime execution role, execution policy, and `AWS::BedrockAgentCore::Runtime` resource.
- CloudFormation reached `CREATE_COMPLETE`.
- `agentcore status --json` returned `success: true`.
- The GenieLite runtime reported `deploymentState: deployed` and `detail: READY`.
- A follow-up `agentcore deploy --diff --yes` reported no differences.
- A repeat `agentcore deploy -y -v` reported no changes.

This proves deployment and runtime readiness. It does not by itself prove successful deployed model behavior.

## First deployed invocation

Frozen normal request:

> I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds.

Observed result:

- The deployed invocation reached the Nova model path.
- AWS returned `ThrottlingException` with the message that too many tokens had been used for the day and to wait before trying again.
- The CLI returned a session identifier for resumption.

## Governance ruling

> **DEPLOYMENT: PROVED**  
> **RUNTIME READY: PROVED**  
> **DEPLOYED MODEL RESPONSE: NOT YET PROVED**  
> **CURRENT BLOCKER: PROVIDER DAILY TOKEN QUOTA**

Do not redeploy, switch models, change regions, loosen the architecture, or make repeated quota retries merely to obtain a green result.

The next live-provider attempt is an evidence upgrade, not a prerequisite for the existence of the submission.

## Claim fence

Allowed now:

- Genie Lite is deployed to Amazon Bedrock AgentCore.
- The runtime reports READY.
- The deterministic specimen proves Echo→CREATE routing, correction propagation, explicit authority state, receipts, and stale-authority expiration.
- The first deployed Nova invocation was blocked by provider daily token throttling.

Not allowed yet:

- successful deployed normal/correction behavior
- successful deployed Nova conversation
- production readiness
- managed cloud memory
- managed durable recovery

> **THE SUBMISSION IS REAL. LIVE INVOCATION IS AN EVIDENCE UPGRADE.**
