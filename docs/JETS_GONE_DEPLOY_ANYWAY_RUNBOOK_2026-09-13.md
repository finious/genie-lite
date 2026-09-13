# JETS GONE — DEPLOY ANYWAY

**Date:** 2026-09-13

**Status:** TEAM RUNBOOK / CURRENT CLI VERIFIED / DEPLOYMENT NOT YET AUTHORIZED

**Audience:** Jimmy / Tank / STAR / Jets / any replacement operator

**Source basis:** current Mac preflight + `JETS_DEPLOYMENT_APPROACH_RECEIPT_2026-09-13.md` + current Tank/CREATE coordination state

**Purpose:** Let the band finish Genie Lite without Jets, without repeating setup, guessing at AWS, or turning readiness into permission.

## THE RULING

> **The Mac is now deployment-capable. Genie Lite is not yet a deployable project.**

Jimmy and Tank closed the machine prerequisites:

- AWS account recovered.
- MFA registered.
- AWS CLI authenticated.
- STS identity proved.
- Region set to `us-east-1`.
- Node and npm installed.
- npm global prefix repaired.
- AgentCore CLI installed at `/Users/jimleyshon/.local/bin/agentcore`.

Independently rechecked from the Mac:

```text
agentcore 0.29.0
aws-cli 2.36.44
AWS region us-east-1
node v24.21.0
npm 11.19.0
uv 0.12.7
```

Do **not** reinstall or reconfigure these tools unless a preflight command proves one is broken.

The current blocking gap is:

> **No durable, team-owned `genie-lite` contest repository/project has been identified yet.**

Known non-contest surfaces:

- The hosted workshop is the fullest tutorial/reference surface, but it is not durable team custody.
- The downloaded Module 4 notebook proves Nova plus new-agent-instance recovery, but it is not a packaged application.
- The old Comic Agent is prior proof, not Genie Lite.

None is the contest project. Do not mutate the old Comic Agent into Genie Lite.

## ONE SOURCE OF TRUTH

Start in SHARED and pull before doing anything:

```bash
cd "/Users/jimleyshon/Desktop/01_THE_COMPLETE_WORKS_OF_JIM/03_MACHINE_ROOM/GRRL_OPS_SHARED_HUB"
git pull --ff-only origin main
```

Read, in order:

1. `docs/weekend/JETS_FULL_CONTEST_DEPLOYMENT_BAND_BRIEF_2026-09-13.md`
2. `docs/weekend/JETS_DEPLOYMENT_APPROACH_RECEIPT_2026-09-13.md`
3. `docs/weekend/JETS_GONE_DEPLOY_ANYWAY_RUNBOOK_2026-09-13.md`
4. `docs/weekend/JETS_10QSETUP_EXE_APPLICATION_HANDOFF_2026-09-12.md`
5. `docs/weekend/ECHO_RECOVERY_PROOF_EXECUTABLE_SPEC_v0.1_2026-09-12.md`

Do not reconstruct the build from chat if these objects are readable.

## BATON OWNERS

- **Jimmy:** names the public project, supplies the human request/correction, handles sign-in prompts, approves claims, and alone gives `AUTHORIZE DEPLOY`.
- **Tank:** protects the human meaning, demo language, README, and thirty-second claim.
- **STAR:** checks authority transitions, claim fences, evidence, and deployment consequences.
- **Operator:** scaffolds, codes, tests, previews, deploys only after authorization, and records receipts. The operator does not need to be Jets.

## PHASE 0 — CONFIRM THE MACHINE, NOT THE WHOLE HISTORY

```bash
agentcore --version
aws --version
aws configure get region
aws sts get-caller-identity
node --version
npm --version
uv --version
```

PASS:

- AgentCore is `0.29.0` or newer.
- AWS identity is Jimmy's intended contest account.
- Region is `us-east-1` unless Jimmy explicitly changes it.
- No credentials are copied into chat, source files, screenshots, or Git.

If identity or region is wrong: **STOP. Fix authentication before project work makes cloud calls.**

## PHASE 1 — CREATE OR RECOVER THE ACTUAL CONTEST PROJECT

First search for an existing durable project and remote. Do not create a duplicate because a chat said one should exist.

If the project exists:

```bash
git clone <GENIE_LITE_REMOTE>
cd <GENIE_LITE_CHECKOUT>
git pull --ff-only
```

If it does not exist, the current AgentCore `0.29.0` scaffold preview has been verified with:

```bash
agentcore create \
  --project-name genielite \
  --name GenieLite \
  --language Python \
  --framework Strands \
  --model-provider Bedrock \
  --memory none \
  --build CodeZip \
  --output-dir <TEAM_OWNED_PARENT> \
  --dry-run \
  --json
```

Important: `genielite` is the AgentCore project identifier because that field does not accept a hyphen. The public repository may still be named `genie-lite`.

The dry run should preview:

```text
agentcore/agentcore.json
agentcore/aws-targets.json
agentcore/.env.local
agentcore/cdk/
app/GenieLite/main.py
app/GenieLite/pyproject.toml
```

After Jimmy confirms the target directory/name, repeat the command without `--dry-run --json`. Publish the resulting project to the agreed public GitHub repository immediately. Confirm `.env.local`, credentials, generated sessions, and secrets are ignored before the first push.

Do not add `--model-id` to this agent-project command. AgentCore `0.29.0` rejects mixing that harness-only flag with `--framework`/`--language`. Configure Nova explicitly in the Strands Python code instead:

```python
from strands.models import BedrockModel

model = BedrockModel(model_id="amazon.nova-pro-v1:0")
```

Every `Agent(...)` constructor must receive `model=model`.

## PHASE 2 — BUILD ONLY THE FROZEN SEAM

Required application shape:

```text
app/GenieLite/main.py
app/GenieLite/genie_lite/echo.py
app/GenieLite/genie_lite/create_specialist.py
app/GenieLite/genie_lite/state.py
app/GenieLite/genie_lite/authority.py
app/GenieLite/genie_lite/receipts.py
app/GenieLite/tests/
docs/
README.md
LICENSE
```

Only this path is in contest scope:

> **JIMMY → ECHO → CREATE → ECHO → JIMMY**

Build order:

1. Deterministic relationship/project state.
2. Explicit authority states, including `AUTHORIZED_CURRENT → AUTHORIZED_RECORDED_EXPIRED` after interruption.
3. Inspectable receipt object.
4. Echo orchestrator.
5. CREATE specialist exposed as a visible Strands tool.
6. Normal request trace.
7. Human correction trace.
8. Interruption/recovery trace.

The frozen normal request is:

> “I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds.”

The frozen correction is:

> “Don’t sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center.”

Before any model call, verify Nova is explicitly configured. The AWS event-credit rule is why Claude/default-provider drift is a stop condition.

## PHASE 3 — LOCAL PASS AND ANTI-JETS TEST

Run deterministic tests first:

```bash
uv sync
uv run pytest -q
```

Then run the project locally using its generated instructions and, when configured:

```bash
agentcore dev
```

PASS only if:

- Echo visibly routes to CREATE instead of doing CREATE's work.
- CREATE returns an artifact/proposal, not authority.
- The correction materially changes the next brief/result.
- Consequential movement stops for authorization.
- A receipt distinguishes requested, routed, produced, authorized, executed, verified, and unproven.
- Restart restores useful state but does not restore live permission.

Then a non-Jets receiver performs a clean clone and repeats install, tests, and the two traces. If that receiver needs private instructions, Jets is still a dependency and the gate fails.

## PHASE 4 — PREVIEW AWS CONSEQUENCES

From the project root:

```bash
agentcore validate
agentcore deploy --target default --dry-run --json
agentcore deploy --target default --diff
```

Return a Deployment Preview Receipt to Jimmy and STAR containing:

- authenticated AWS account identity, redacted where shared publicly
- region
- resources to be created or changed
- execution role/IAM implications
- model and model ID
- build type
- expected endpoint/runtime
- estimated or unknown cost surface
- known limits and cleanup route
- current Git commit
- local test result

Then:

> **STOP. `MAY DEPLOY` IS NOT AUTHORITY. WAIT FOR THE EXACT WORDS `AUTHORIZE DEPLOY`.**

Build authorization does not roll forward into deployment authorization.

## PHASE 5 — DEPLOY AFTER AUTHORIZATION

Only after Jimmy says `AUTHORIZE DEPLOY`:

```bash
agentcore deploy --target default -y -v
agentcore status --target default --json
```

Invoke with a unique session ID, preferably UUID v4:

```bash
agentcore invoke \
  --target default \
  --session-id <UUID_V4> \
  --prompt-file docs/demo/normal-request.txt \
  --json
```

Run the correction with the same session ID. Run interruption/recovery only to the level actually supported by the deployed state implementation.

Capture immediately:

- deployment command/result
- deployed runtime/status
- exact Git commit
- invocation output
- Echo→CREATE route trace
- authority state before/after
- receipt
- screenshots/video clip
- exact claim proved
- exact limitation

Push the deployment receipt and evidence index to the public project and the team-readable SHARED location.

## CLAIM FENCE

Allowed only when proved:

- local session recovery survives a new agent instance
- Echo visibly routes to CREATE
- correction changes the work
- authority expires across interruption
- deployed AgentCore invocation succeeds

Do not claim:

- durable cloud recovery because local JSON survived
- managed long-term memory because a session ID was reused
- production readiness because one endpoint answered
- action occurred because an agent described action
- authorization persisted because conversation persisted

Managed AgentCore Memory or S3-backed state is a stretch gate. It is not allowed to block the minimum contest proof.

## FAILURE ROUTES

- **No contest repo:** stop deployment; scaffold/publish the durable project first.
- **Wrong AWS identity/region:** stop and re-authenticate.
- **Nova unavailable:** stop model calls; verify Bedrock access in `us-east-1` and keep the local deterministic proof intact.
- **AgentCore validation/dry run fails:** preserve output; repair the smallest named dependency. Do not jump to live deploy.
- **AgentCore deploy fails:** keep the locally runnable public Strands proof, README, architecture, video, and limitation. AgentCore strengthens the entry but is not permission to lose the whole submission.
- **Cloud memory fails:** submit only the local recovery claim.
- **Git push rejected:** `git pull --rebase origin main`, resolve deliberately, rerun tests, then push. Never force-push the shared main branch.
- **Jets disappears:** follow this file. Do not wait for her to translate her own work.

Cleanup changes or deletes AWS resources and requires its own explicit authorization. Never run `agentcore remove all -y` as an automatic recovery step.

## DONE MEANS

The team is no longer dependent on Jets when a non-Jets receiver can:

1. pull the public project
2. identify the frozen proof
3. install and test it
4. reproduce normal and correction traces
5. preview deployment consequences
6. obtain `AUTHORIZE DEPLOY`
7. deploy and invoke it
8. find every receipt and limitation
9. push the final Git state without Jets

> **MIND THE GAPS. BUILD SAFER. DO MUST BE AUTHORIZED.**
