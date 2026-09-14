# Genie Lite Demo Script — Two Evidence Branches

**Target length:** 3–4 minutes  
**Goal:** demonstrate the working project, the problem, who it is for, and why it matters.

## Shared opening

**Say:**

“Genie Lite is a Professional Agents project built with Strands Agents and deployed on Amazon Bedrock AgentCore. It is for people doing multi-step AI work who need delegation without losing track of authority, correction, or evidence.”

Show the architecture:

> **HUMAN → ECHO → CREATE → ECHO → HUMAN**

Then say:

“Echo is the conversational bridge. CREATE is the specialist. Receipts show the route, return, authority state, and limits. Recovery can restore useful state, but it does not silently restore stale permission.”

**Why it matters:**

“Today, professionals often have to remember what they asked an AI to do, what actually happened, and whether a previous instruction is still safe to act on. Genie Lite makes those boundaries inspectable.”

Show briefly:

- public repo
- passing deterministic tests / evidence table
- AgentCore deployed runtime status `READY`

---

## Branch A — deployed invocation works

### Scene 1: normal request

Run:

```text
I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds.
```

Show:

1. Echo receives the human goal.
2. Echo visibly routes specialist work to CREATE.
3. CREATE returns bounded specialist work.
4. Echo returns it without claiming authority it does not own.
5. Receipt records the route and authority state.

### Scene 2: human correction

In the same session run:

```text
Don't sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center.
```

Show the changed result and receipt.

**Say:**

“The important thing is not that the wording changed. The specialist brief and resulting work changed because the human corrected the direction.”

### Scene 3: recovery / authority proof

Show the deterministic recovery test or receipt proving that useful state can return while stale consequential authority expires.

**Say:**

“Recovery is not permission. Genie Lite can remember where the work was without silently assuming it still has authority to continue consequential action.”

### Close

**Say:**

“That is Genie Lite: conversation carries complexity, specialist work stays attributable, and authority remains human.”

---

## Branch B — deployed invocation remains throttled

State the limitation once, then show the proof that does exist.

Show AgentCore status with runtime `READY` and the preserved deployed throttle receipt.

**Say:**

“The runtime is deployed and READY. The first deployed Nova invocation was blocked by the provider’s daily token quota. We preserved that as evidence rather than swapping models or architecture to manufacture a green result.”

Then show:

1. six deterministic tests passing
2. Echo→CREATE routing
3. correction materially changing the next brief/artifact
4. recovery expiring stale consequential authority
5. receipt fields and claim limits
6. successful AgentCore deployment and clean post-deploy diff

**Say:**

“So the deployment is real and the governed mechanism is proved. What we do not claim is a successful deployed model conversation while the provider throttle remains unresolved.”

### Close

**Say:**

“Genie Lite is designed around a simple idea: the human should carry less operational complexity without giving the system more authority.”

---

## Demo rule

Use **Branch A** only if the deployed normal and correction invocations actually complete successfully.

Otherwise use **Branch B** exactly as the evidence supports.

Do not add features for the video. The strongest presentation is the smallest one in which every sentence can be traced to evidence.
