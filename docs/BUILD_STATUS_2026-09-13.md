# Genie Lite Build Status

**Status:** deployed / runtime READY / deterministic proof passing / deployed Nova invocation throttled

## Verified state

- Runtime model configured as `amazon.nova-pro-v1:0`.
- Tutorial defaults and example MCP/calculator code are removed from the active application.
- Echo routes to one CREATE specialist inside one Strands/AgentCore runtime.
- State, authority, receipt, correction, and recovery behavior have deterministic tests.
- Six credit-free tests pass.
- AgentCore configuration validates.
- Public repository is readable at `https://github.com/finious/genie-lite`.
- CDK bootstrap completed.
- Deployment diff showed the expected AgentCore stack with execution role, policy, and runtime.
- CloudFormation deployment completed successfully.
- `agentcore status --json` reported `success: true`, `deploymentState: deployed`, and runtime detail `READY` in `us-east-1`.
- Follow-up diff reported no differences.
- Repeat deploy reported no changes.
- First deployed Nova invocation reached the model path but returned a provider daily-token `ThrottlingException`.

## Earned claim

> Echo can carry human intent into specialist work without becoming the specialist, while preserving human authority and inspectable receipts.

The deterministic suite supports the mechanism. The AgentCore deployment and READY runtime are proved.

## Evidence still available to upgrade

A successful deployed normal request followed by the correction in the same session would additionally prove the frozen behavior on the deployed Strands/AgentCore runtime.

Until that happens, the project does not claim successful deployed model behavior.

## Not claimed

- production readiness
- managed AgentCore Memory
- generalized long-term companion behavior
- managed durable recovery
- automatic continuation of authority after interruption

See [`EVIDENCE_AND_CLAIM_FENCE.md`](EVIDENCE_AND_CLAIM_FENCE.md) for the public truth table.
