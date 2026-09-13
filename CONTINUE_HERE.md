# CONTINUE GENIE LITE WITHOUT JETS

This is the shortest safe path from the current repository to a contest
submission. Start here if the prior operator is unavailable.

## Current truth

- Local specimen: built
- Runtime: Strands on Amazon Bedrock AgentCore
- Model: `amazon.nova-pro-v1:0`
- Build type: CodeZip
- Frozen seam: `JIMMY → ECHO → CREATE → ECHO → JIMMY`
- Credit-free tests: six passing
- AgentCore configuration: valid
- AWS deployment: not performed
- Managed memory: not added
- Last live attempt: blocked by AWS account verification
- Remote custody: **PROVEN** at public repository `finious/genie-lite`
- Two-shift execution card: `docs/GENIE_LITE_TWO_SHIFT_DIRECTION_2026-09-13.md`

The detailed blocker receipt is
`docs/evidence/LIVE_NOVA_ATTEMPT_2026-09-13.md`.

## 1. Recover the room

From the repository root:

```bash
git status --short --branch
git log --oneline --decorate -5
./scripts/check-local.sh
```

Expected result: clean working tree, all six tests pass, AgentCore validation
returns success, Nova Pro is found, and tutorial defaults are absent.

If any expected result fails, stop and fix that result before making model
calls or touching deployment.

## 2. Establish GitHub custody

Public GitHub custody is now established at:

`https://github.com/finious/genie-lite`

Before continuing after any handoff, a receiver should independently open the
repository and confirm the README heading, current commit, and
`docs/BUILD_STATUS_2026-09-13.md`. Access is not knowledge until a receiver
reads the object.

## 3. Retry the live Nova proof once

Do not retry until AWS account verification has had the window stated in the
captured AWS error. Do not change models or regions to route around verification.

Terminal A:

```bash
agentcore dev --logs --no-traces
```

Terminal B, frozen normal trace:

```bash
agentcore dev --stream "I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds."
```

Then the frozen correction in the same local session:

```bash
agentcore dev --stream "Don't sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center."
```

Capture the returned text and server log. The live proof passes only when:

1. Echo names the human goal.
2. The route to CREATE is visible.
3. CREATE returns a bounded proposal.
4. Echo returns it without claiming approval, execution, or verification.
5. The correction materially changes the next brief and result.
6. The receipt names authority and unproven claims.

If AWS repeats the account-verification error, stop model calls and preserve the
new receipt. If the stated verification window has elapsed, use the support
route named in AWS's error.

## 4. Preflight deployment without deploying

Only after the local live proof passes:

```bash
agentcore validate --json
aws configure get region
cat agentcore/aws-targets.json
aws sts get-caller-identity
aws bedrock list-foundation-models --region us-east-1 --query 'modelSummaries[?modelLifecycle.status==`ACTIVE`].modelId' --output table
agentcore deploy --dry-run
agentcore deploy --diff
```

Stop if the authenticated account, configured region, deployment target, or
Nova availability do not align. The current application code expects
`us-east-1`; the operator must not silently deploy into the Ohio console region
shown during setup.

Return the dry-run/diff with these consequences:

- exact AWS account and region
- resources AgentCore/CDK proposes to create
- IAM roles or permissions required
- expected cost surface and cleanup owner
- current tests and live-trace evidence
- unresolved gaps

## 5. Human gate

Do not deploy on phrases such as “may deploy,” “looks good,” or “green.” Stop
for the exact authorization:

> **AUTHORIZE DEPLOY**

Only after that authorization:

```bash
agentcore deploy -y -v
agentcore status --json
```

Invoke the deployed runtime with the frozen normal and correction inputs,
capture the receipts, and update the build-status document. Do not claim managed
durable recovery because this contest specimen intentionally has no AgentCore
Memory resource.

## 6. Submission evidence

The minimum package is:

- public repository and receiver-read receipt
- passing credit-free test output
- successful normal and correction live traces
- recovery/authority deterministic trace
- deployment dry-run/diff receipt
- deployed status and invocation receipt, if deployment was authorized
- honest limitations and unproven claims
- short demo showing `human → Echo → CREATE → Echo → human`

## Stop rules

Do not add managed memory, a second specialist, a UI, a new architecture, or
10Q/MWC expansion before the contest proof is complete. Do not confuse useful
state with continuing authority.

> **VERIFY IT. PUBLISH IT. RUN IT. PREVIEW IT. AUTHORIZE IT. DEPLOY IT. RECEIPT IT.**
