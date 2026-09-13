# LIVE NOVA ATTEMPT RECEIPT

**Date:** 2026-09-13  
**Status:** BLOCKED / EXTERNAL AWS ACCOUNT VERIFICATION  
**Deployment performed:** No

## Attempt

- Local AgentCore server started successfully at `http://localhost:8080/invocations`.
- Runtime: `GenieLite`
- Region: `us-east-1`
- Model: `amazon.nova-pro-v1:0`
- Input: frozen normal-trace request
- Local request ID: `0241be83-a0aa-492b-b22f-d6a4afd7be28`

## Observed result

The request reached the Strands/Bedrock model path, but the stream ended with
`AccessDeniedException`. AWS reported that the account is currently being
verified and that verification normally takes less than two hours.

This does **not** establish a completed Echo→CREATE live trace. It also does not
indicate a code, model-selection, AgentCore-validation, or deployment failure.

## Governance ruling

> Stop model retries. Preserve the local deterministic proof. Wait for AWS
> account verification, then retry the frozen normal trace once.

If the same verification message remains after the AWS-stated window, use the
support address provided in the AWS error. Do not change models, loosen IAM, or
deploy in an attempt to route around account verification.

## Still valid

- six deterministic tests pass without model calls
- AgentCore configuration validates
- Nova Pro is explicitly configured
- no AWS runtime has been deployed
