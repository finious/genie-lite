# Agents for Humans Submission Checklist

This checklist mirrors the contest requirements and keeps the public submission surface focused on what judges need.

**Official deadline:** September 14, 2026 at 5:00 PM Pacific (`2026-09-15T00:00:00Z`).

**Current Devpost state:** the public Genie Lite project page exists, but the Agents for Humans entry has not been finally submitted (`submitted_at` is still empty). Publishing a project page is not the same as submitting it to the hackathon.

## Required submission pieces

- [x] **Text description** — draft in [`DEVPOST_SUBMISSION_DRAFT.md`](DEVPOST_SUBMISSION_DRAFT.md)
- [x] **Devpost project shell** — name, tagline, description, technologies, and repository link loaded
- [x] **Public code repository** — `https://github.com/finious/genie-lite`
- [x] **Source code and setup instructions** — root [`README.md`](../README.md)
- [x] **MIT license** — [`LICENSE`](../LICENSE)
- [x] **README** — judge-facing and reproducible
- [x] **Architecture description** — [`ARCHITECTURE.md`](ARCHITECTURE.md)
- [x] **Architecture diagram asset prepared** — [`assets/genie_lite_architecture.png`](assets/genie_lite_architecture.png)
- [ ] **Architecture diagram uploaded to Devpost** — upload the PNG to the required file field
- [ ] **Demo video (≤5 minutes)** — use [`DEMO_SCRIPT_TWO_BRANCHES.md`](DEMO_SCRIPT_TWO_BRANCHES.md)
- [ ] **AWS Builder ID** — enter in Devpost form
- [ ] **Required Devpost answers** — Submitter Type, Country, Professional Agents track, public repo URL, and AWS Builder ID
- [x] **GitHub About license** — GitHub detects the repository license as MIT
- [ ] **Final Devpost submit** — verify the preview, then submit before the official deadline

## Demo must cover

- the problem being solved
- who Genie Lite is for
- why the problem matters
- the working project / strongest available proof

## Judge-facing proof order

1. [`JUDGE_START_HERE.md`](JUDGE_START_HERE.md)
2. [`README.md`](../README.md)
3. [`ARCHITECTURE.md`](ARCHITECTURE.md)
4. [`EVIDENCE_AND_CLAIM_FENCE.md`](EVIDENCE_AND_CLAIM_FENCE.md)
5. deployment/runtime evidence in [`evidence/`](evidence/)

## Current evidence boundary

**Proved:** deterministic routing/correction/authority/receipt behavior, AgentCore deployment, runtime `READY`, clean post-deploy diff.

**Blocked:** first deployed Nova invocation hit provider daily-token throttling.

**Not claimed:** production readiness, managed memory, managed durable recovery, or successful deployed model behavior before a live trace completes.

## Submission rule

> Every sentence should be traceable to evidence.

If the live Nova trace completes, add it as stronger evidence. If it remains throttled, submit the deployed READY runtime plus the deterministic proof and explicit limitation.
