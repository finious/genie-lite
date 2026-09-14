# Genie Lite Demo Script — Two Branches

Target length: 2–4 minutes. This is proof, not a commercial.

## Shared opening

**Say:**

“Genie Lite tests one narrow claim: can a conversational AI carry human intent into specialist work without becoming the specialist or inheriting human authority?”

Show the architecture:

> **JIMMY → ECHO → CREATE → ECHO → JIMMY**

Then say:

“Echo is the conversational bridge. CREATE is the specialist. Receipts show the route, return, authority state, and limits. Recovery can restore useful state, but it does not silently restore stale permission.”

Show briefly:

- public repo
- passing deterministic tests / proof table
- AgentCore deployed runtime status `READY`

---

## Branch A — deployed invocation works

### Scene 1: normal request

Run the frozen normal request:

```text
I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds.
```

Show:

1. Echo receives/names the human goal.
2. Route to CREATE is visible.
3. CREATE returns bounded specialist work.
4. Echo returns it without claiming approval, execution, or verification it does not own.
5. Receipt records the route and authority state.

### Scene 2: correction

In the same session run:

```text
Don't sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center.
```

Show the changed result.

**Say:**

“The important thing is not that the wording changed. The specialist brief and resulting work changed because the human corrected the direction.”

Show the correction receipt.

### Close

**Say:**

“That is Genie Lite: conversation carries complexity, specialist work stays attributable, and authority remains human.”

---

## Branch B — deployed invocation is throttled

Do not spend the demo apologizing for AWS. State the limitation once and move to proof.

Show AgentCore status with runtime `READY`.

Show the preserved provider throttle receipt.

**Say:**

“The runtime is deployed and READY. The first deployed Nova invocation was blocked by the provider’s daily token quota. We preserved that as a limitation rather than swapping models, regions, or architecture to manufacture a green result.”

Then show the deterministic proof:

1. six tests passing
2. Echo→CREATE routing
3. correction materially changing the next brief/artifact
4. recovery expiring stale consequential authority
5. receipt fields / claim limits

**Say:**

“So the deployment is real and the mechanism is proved. What we do not claim is a successful deployed model conversation while the provider throttle remains unresolved.”

### Close

**Say:**

“The point of Genie Lite is not to hide failure. It is to make capability, authority, evidence, and limits inspectable.”

---

## Demo rule

Use Branch A if and only if the deployed normal and correction invocations actually complete successfully.

Otherwise use Branch B unchanged.

Do not reopen architecture or add features for the video.
