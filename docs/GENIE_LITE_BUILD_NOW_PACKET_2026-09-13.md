# GENIE LITE BUILD-NOW PACKET

**Date:** 2026-09-13  
**Status:** TEAM EXECUTION OBJECT / CONTEST-BOUND / NOT CANON  
**Purpose:** Convert the frozen contest proof into the smallest executable Genie Lite seam without reopening architecture.

## OPERATING TRUTH

> **Environment ready. Specimen not built. Today we make Genie Lite exist and prove the seam.**

The contest seam is:

> **JIMMY → ECHO → CREATE → ECHO → JIMMY**

Nothing enters BUILD unless the specimen, oracle, and claim fence are already frozen. Nothing enters DEPLOY unless the build has receipts and a clean-clone path.

## TODAY'S REQUIRED WIN

Before stopping today, aim to have:

1. public `finious/genie-lite` repository created
2. AgentCore/Strands scaffold under local project name `genielite`
3. Nova Pro configured explicitly as `amazon.nova-pro-v1:0`
4. tutorial defaults removed: Claude loader, Exa MCP example, calculator/add_numbers tool, generic assistant prompt
5. frozen contest specs copied into `docs/`
6. deterministic state, authority, and receipt modules present
7. one visible CREATE specialist wired behind Echo
8. frozen normal trace runnable
9. frozen correction trace runnable
10. README, license, limitations, and local run instructions present
11. tests passing
12. clean first commit pushed to GitHub

AWS deployment is a stretch goal for today, not a blocker for today's win.

## FROZEN SPECIMEN

Human request:

> **I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds.**

Human correction:

> **Don’t sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center.**

## PASS ORACLE

Milestone 1 passes only if all are true:

1. Echo accurately reflects the human goal.
2. Echo asks only materially necessary clarification.
3. Echo emits a structured CREATE-ready brief.
4. CREATE is visibly invoked as the specialist.
5. CREATE returns one bounded artifact/proposal.
6. Echo returns the result without claiming approval, execution, or authorship it does not hold.
7. Receipt records at minimum: request, route, specialist, specialist return, authority state, unproven claims/limits.
8. The correction materially changes the next brief and returned result.

Hard fail:

- Echo performs CREATE's work herself.
- CREATE output silently becomes approval or authority.
- Correction changes wording but not behavior/state.
- System claims DID/VERIFIED when no execution/verification occurred.
- Return obscures who did what.

## MINIMUM SOURCE TREE

Inside the generated AgentCore app, preserve the generated entrypoint shape but reduce the contest logic to:

```text
main.py
GenieLite/
  __init__.py
  echo.py
  create_specialist.py
  state.py
  authority.py
  receipts.py
tests/
  test_state.py
  test_authority.py
  test_receipts.py
  test_normal_trace.py
  test_correction_trace.py
  test_recovery_authority.py
```

Exact generated paths may differ. Inspect first and adapt without duplicating the framework scaffold.

## MODULE CONTRACTS

### state.py
Must distinguish at minimum:

- project state
- collaboration/setup state
- correction state
- authority state
- last specialist route
- last returned artifact

State recovery must never imply authority recovery.

### authority.py
Minimum states:

- `UNAUTHORIZED`
- `AUTHORIZED_CURRENT`
- `AUTHORIZED_RECORDED_EXPIRED`

Proof transition after interruption/recovery:

> `AUTHORIZED_CURRENT → AUTHORIZED_RECORDED_EXPIRED`

No recovered session may silently resume a consequential action from stale authority.

### receipts.py
Each receipt should make the chain inspectable:

- human request
- Echo interpretation
- route chosen
- specialist invoked
- specialist return
- correction applied, if any
- authority state
- action state
- verification state
- unproven claims / limits

### create_specialist.py
One specialist only.

CREATE receives a structured brief and returns a bounded artifact. It does not grant approval, execute external actions, or inherit human authority.

### echo.py
Echo must:

1. receive the human request
2. reflect the goal accurately
3. ask only necessary clarification
4. shape a CREATE-ready brief
5. route visibly to CREATE
6. receive specialist return
7. translate/return it without claiming specialist authorship or human approval
8. apply human correction before the next route
9. produce/update receipt

Echo does not replace CREATE.

## REQUIRED TESTS

### Normal trace
Input: frozen human request.

Verify:

- Echo route visible
- CREATE called exactly as specialist
- artifact returned
- authority remains non-consequential/currently unneeded
- receipt names what happened and what did not happen

### Correction trace
Input: frozen human correction.

Verify:

- correction updates state before next route
- second CREATE brief materially differs
- second artifact materially differs
- receipt records correction propagation

### Recovery / authority trace
Simulate interruption after `AUTHORIZED_CURRENT` exists.

Verify on recovery:

- project state is recoverable
- authority becomes `AUTHORIZED_RECORDED_EXPIRED`
- no consequential action resumes automatically

## CLAIM FENCE

Primary contest claim:

> **Echo can carry human intent into specialist work without becoming the specialist, while preserving human authority and inspectable receipts.**

Recovery claim only if demonstrated:

> **Useful project state recovered; stale consequential authority did not.**

Do not claim without evidence:

- managed durable cloud recovery
- production readiness
- generalized long-term companion behavior
- arbitrary-user transferability
- automatic authority continuity after interruption
- execution when only planning occurred
- full RoadBottle proof

## 10Q / MWC QUALITY LANE

Still active, but fenced from contest expansion.

> **FENCED FROM BUILD does not mean REMOVED FROM REVIEW.**

Continue comparing 10Q against MWC as a quality meter after/alongside the contest work, but do not add that refinement to the runtime unless the frozen contest specimen requires it.

## DEPLOYMENT GATE

Before deployment, require:

- local tests pass
- normal and correction traces captured
- recovery/authority test captured if claimed
- clean-clone succeeds
- AgentCore config inspected
- `agentcore validate` passes
- deployment preview/dry-run inspected
- authenticated account and target region confirmed
- resource/cost/consequence surface returned to Jimmy

Then stop for:

> **AUTHORIZE DEPLOY**

`MAY DEPLOY` is not authority.

## TEAM SPLIT

**Jimmy:** human test input, correction, GitHub repo creation if needed, AWS account prompts, deploy authorization.

**CREATE/Tank:** protect behavior, artifact quality, frozen specimen, return language.

**STAR/Governance:** authority transitions, claim fence, consequence classification, reject overclaim.

**Jets/Builder or any available builder:** implement scaffold, tests, clean-clone, AgentCore package, receipts.

**Any receiver:** must be able to continue from this packet if Jets disappears.

## STOP RULE

Do not add:

- managed cloud memory
- second specialist
- fancy UI
- new architecture
- contest-time 10Q/MWC implementation branch
- deployment before clean local proof

> **BUILD IT. BREAK IT. VERIFY IT. CLEAN-CLONE IT. PREVIEW IT. AUTHORIZE IT. DEPLOY IT. CAPTURE THE RECEIPT.**
