# DEPLOYMENT AUTHORIZATION RECEIPT

**Date:** 2026-09-13  
**Authority:** Jimmy / human project owner  
**Status:** AUTHORIZED FOR CURRENT FROZEN DEPLOYMENT PLAN

## Exact authorization

> **AUTHORIZE DEPLOY**

The human project owner explicitly authorized deployment of the current Genie Lite contest specimen to AWS tonight.

## Scope of authorization

Authorization applies to the current frozen plan only:

- repository: `finious/genie-lite`
- runtime: Amazon Bedrock AgentCore
- framework: Strands
- build: CodeZip
- region target: `us-east-1`
- model: `amazon.nova-pro-v1:0`
- seam: `JIMMY → ECHO → CREATE → ECHO → JIMMY`
- no managed memory
- no second specialist
- no external publish/purchase/delete side effects

## Conditions that remain binding

Authorization does not erase technical preconditions or evidence requirements. Before live deployment, the operator must:

1. run the local verification script successfully;
2. confirm authenticated AWS account and target region;
3. inspect the AgentCore deployment dry-run/diff or equivalent preview available in the installed CLI;
4. confirm no materially different resource, permission, model, region, or cost surface has appeared;
5. preserve deployment output and post-deploy status/invocation receipts.

A material change to deployment scope requires a fresh human authorization.

## Current known gap

The last live Nova model attempt was blocked by AWS account verification. This authorization permits deployment once the current AWS account can execute the required AgentCore/Bedrock path; it does not convert that blocker into proof of live model behavior.

## Governing distinction

> **AUTHORIZED does not mean DID.**
>
> **DID does not mean VERIFIED.**

Deployment is only complete when AWS reports the runtime deployed and the band captures inspectable status and invocation evidence.
