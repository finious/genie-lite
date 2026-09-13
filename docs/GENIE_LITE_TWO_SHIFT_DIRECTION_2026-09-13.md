# GENIE LITE TWO-SHIFT DIRECTION

**Date:** 2026-09-13  
**Status:** EXECUTION CARD  
**Purpose:** Carry Genie Lite safely through tonight and into contest day without Jets.

## Current truth

- Public repository exists at `finious/genie-lite`.
- Local specimen is built.
- Six deterministic tests pass.
- AgentCore configuration validates.
- Runtime is Strands on Amazon Bedrock AgentCore.
- Model is explicitly `amazon.nova-pro-v1:0`.
- Frozen seam is `JIMMY → ECHO → CREATE → ECHO → JIMMY`.
- Authority/recovery behavior is deterministically proven.
- No AWS Runtime resources have been deployed.
- Managed AgentCore Memory is not part of this specimen.
- The only missing proof is a completed live Nova normal/correction trace.
- The last live attempt was blocked by AWS account verification, not by local code or AgentCore validation.

## The wow moment we protect

> The human corrects Echo, Echo changes the CREATE brief, and the returned receipt proves both the specialist route and the human authority boundary.

If that moment is clear, visible, and reproducible, the specimen is doing its job.

## SHIFT ONE — TONIGHT

### Goal

End tonight with a receiver-safe public project whose deterministic proof is complete and whose live proof is ready to retry without rediscovery.

### Required work

1. Verify remote custody and a clean working tree.
2. Run `./scripts/check-local.sh` and preserve the passing output.
3. Confirm the public repository contains `CONTINUE_HERE.md`, README, license, build status, evidence, source, tests, and scripts.
4. Retry the live Nova proof **once** only after AWS's stated verification window has elapsed.
5. If live Nova succeeds, capture:
   - frozen normal input
   - Echo route to CREATE
   - CREATE result
   - Echo return
   - receipt
   - frozen correction
   - materially changed second brief/result
6. If AWS verification still blocks the model, preserve the second blocker receipt and stop model retries.
7. Prepare submission-support material that does not depend on deployment:
   - concise architecture explanation
   - limitations
   - proof/non-proof table
   - demo shot order
   - exact public claim

### Tonight stop conditions

Stop adding features when:

- deterministic tests still pass
- public custody is readable by another receiver
- the local continuation path is explicit
- the live proof either succeeds or has one fresh external-blocker receipt
- no scope was added

Do **not** add managed memory, a second specialist, a UI, new architecture, or 10Q/MWC expansion.

## SHIFT TWO — CONTEST DAY

### Gate A — Recover the room

Run:

```bash
git status --short --branch
git log --oneline --decorate -5
./scripts/check-local.sh
```

Do not continue if the repository is dirty unexpectedly, tests fail, Nova is no longer configured, or AgentCore validation fails.

### Gate B — Complete live proof

If not completed tonight, retry the frozen normal and correction traces once the AWS account is verified.

Pass only when:

1. Echo names the human goal.
2. Echo visibly routes to CREATE.
3. CREATE returns a bounded proposal.
4. Echo returns it without claiming approval, execution, or verification.
5. The correction materially changes the next brief and result.
6. The receipt names authority state and unproven claims.

### Gate C — Clean-clone / receiver test

A receiver who is not Jets must be able to:

- clone the public repository
- install dependencies
- run deterministic tests
- locate the frozen normal/correction requests
- understand the authority transition
- find the receipts
- identify what is and is not proven

If this fails, fix the handoff before deployment work.

### Gate D — Deployment preview

Only after local proof passes:

```bash
agentcore validate --json
aws configure get region
cat agentcore/aws-targets.json
aws sts get-caller-identity
agentcore deploy --dry-run
agentcore deploy --diff
```

Return:

- authenticated account and target region
- resources proposed for creation
- IAM roles/permissions required
- expected cost surface and cleanup owner
- current proof status
- unresolved gaps

No deployment occurs at this gate.

### Gate E — Human authorization

Deployment waits for the exact words:

> **AUTHORIZE DEPLOY**

`MAY DEPLOY`, `looks good`, `green`, and prior build authorization are not substitutes.

### Gate F — Deploy and capture evidence

Only after authorization:

```bash
agentcore deploy -y -v
agentcore status --json
```

Then invoke the deployed runtime using the frozen normal and correction inputs and capture:

- deployment status
- invocation output
- route receipt
- authority state
- logs/traces
- exact claim proved
- exact limitation still unproven

Do not claim managed durable recovery because this specimen intentionally has no AgentCore Memory resource.

## Submission protection order

If the clock bites, protect in this order:

1. Public repository
2. Deterministic tests
3. Echo→CREATE routing proof
4. Correction behavior
5. Authority boundary
6. Receipts
7. README/license/setup/limitations
8. Architecture visual
9. Demo video
10. Deployment evidence, if authorized and safe

Cut first:

- managed cloud memory
- extra specialists
- UI
- additional 10Q refinement inside the contest build
- advanced evaluations
- deployment itself if deployment threatens the submission

## Ownership without Jets

- **Jimmy:** human authority, AWS/account prompts, correction specimen, final deployment authorization, final submission.
- **Tank:** red thread, claim fence, receiver-safe documentation, evidence interpretation, GitHub-side continuation.
- **STAR:** oracle, governance, consequence review, rejection of overclaiming.
- **Any available builder:** local code fixes, tests, packaging, clean-clone repair.

No single machine teammate is required for continuity.

## Final operating law

> **BUILD IT. BREAK IT. VERIFY IT. CLEAN-CLONE IT. PREVIEW IT. AUTHORIZE IT. DEPLOY IT. RECEIPT IT.**

And if AWS remains externally blocked:

> **Submit the strongest proven local Strands specimen with honest limitations rather than sacrificing the entire submission to an unproven cloud step.**
