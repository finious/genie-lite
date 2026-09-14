# One-Shot Live Proof Run Card

Purpose: upgrade evidence without allowing the provider to own the submission window.

## Before Bedrock gets a vote

Confirm the submission package is already viable:

- README aligned
- architecture published
- build status aligned
- evidence / claim fence aligned
- Devpost draft ready
- two-branch demo script ready

## One deliberate attempt window

Do not redeploy. Do not change model, region, IAM, memory, or architecture.

From the repository root:

```bash
agentcore status --json
```

Confirm the deployed runtime is still `READY`.

Then run the frozen normal request:

```bash
agentcore invoke "I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds."
```

### If it succeeds

Capture:

- output
- session ID
- timestamp
- status
- relevant logs/traces if available

Then immediately run the frozen correction in the same session:

```bash
agentcore invoke --session-id <SESSION_ID> "Don't sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center."
```

The upgrade passes only if the correction materially changes the next specialist brief/result and the receipt preserves the human authority boundary.

### If it throttles

Stop Bedrock work immediately.

Capture the exact error and session ID in:

`docs/evidence/DEPLOYED_INVOCATION_THROTTLE_2026-09-14.md`

Then continue packaging and submission using Demo Branch B.

## Stop rule

The provider gets one clean opportunity to upgrade the evidence. It does not get the afternoon.

> **Protect the 90% already earned from the last 10% still available.**
