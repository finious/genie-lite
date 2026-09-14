# CONTINUE GENIE LITE WITHOUT JETS

This is the shortest safe path from the current repository to final contest submission. Start here if the prior operator is unavailable.

## Current truth

- Public repository: **PROVEN** at `finious/genie-lite`
- Local specimen: built
- Runtime: Strands on Amazon Bedrock AgentCore
- Model: `amazon.nova-pro-v1:0`
- Build type: CodeZip
- Frozen seam: `JIMMY → ECHO → CREATE → ECHO → JIMMY`
- Credit-free tests: six passing
- AgentCore configuration: valid
- AWS deployment: **COMPLETED**
- Runtime state: **DEPLOYED / READY** in `us-east-1`
- Post-deploy diff: no differences
- Repeat deploy: no changes
- Managed memory: not added
- First deployed Nova invocation: provider daily-token throttling
- Successful deployed normal/correction trace: not yet proved

Primary release packet:

`docs/SUBMISSION_RELEASE_PACKET_2026-09-14.md`

Public truth table:

`docs/EVIDENCE_AND_CLAIM_FENCE.md`

Deployment + throttle receipt:

`docs/evidence/DEPLOYED_RUNTIME_AND_THROTTLE_RECEIPT_2026-09-13.md`

## 1. Recover the room

From the repository root:

```bash
git status --short --branch
git log --oneline --decorate -5
./scripts/check-local.sh
agentcore status --json
```

Expected result: clean working tree, six tests pass, AgentCore validation passes, Nova Pro is configured, tutorial defaults are absent, and the deployed GenieLite runtime reports READY.

If any of those facts materially changed, stop and inspect before making new claims.

## 2. Lock the submission surface first

Before any provider retry, confirm these files tell the same story:

- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/BUILD_STATUS_2026-09-13.md`
- `docs/EVIDENCE_AND_CLAIM_FENCE.md`
- `docs/DEVPOST_SUBMISSION_DRAFT.md`
- `docs/DEMO_SCRIPT_TWO_BRANCHES.md`
- `docs/SUBMISSION_RELEASE_PACKET_2026-09-14.md`

The governing distinction is:

> **The submission is already real. Live invocation is an evidence upgrade.**

## 3. Give Bedrock one clean evidence-upgrade attempt

Use:

`docs/ONE_SHOT_LIVE_PROOF_RUN_CARD.md`

Run the frozen deployed normal request once.

If it succeeds, immediately run the frozen correction in the same session and capture:

- returned text
- session ID
- route / receipt evidence
- the materially changed result
- relevant logs / traces if available

If provider throttling repeats, preserve the exact error and stop model retries. Do not switch model, region, architecture, or redeploy merely to manufacture a green result.

## 4. Choose the demo branch

Use `docs/DEMO_SCRIPT_TWO_BRANCHES.md`.

- **Branch A** only if deployed normal + correction both complete successfully.
- **Branch B** if the provider still throttles.

Branch B is not a failure narrative. It shows the deployed READY runtime, deterministic mechanism proof, authority/recovery receipts, and the provider limitation honestly.

## 5. Final submission pass

Use the Devpost draft and release packet.

Ask:

> **Can every sentence in the submission be traced to evidence?**

If not, cut it.

Jimmy's role at this stage is:

> **PROOF OWNER → RELEASE AUTHORITY → SUBMITTER**

## Stop rules

Do not add managed memory, a second specialist, a UI, a new architecture, or 10Q/MWC implementation before submission.

Do not repeatedly redeploy a READY runtime with a clean diff.

Do not confuse deployment with successful model behavior, execution with verification, or recovered state with current authority.

> **LOCK PACKAGE → ONE LIVE ATTEMPT → VERIFY → RECEIPT → CHOOSE DEMO BRANCH → CLAIM CHECK → SUBMIT.**
