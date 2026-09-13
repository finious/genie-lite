# JETS HANDOFF — 10Q SETUP.EXE APPLICATION SPEC

**Date:** 2026-09-12  
**Status:** READY FOR APPLICATION / TEAM WORKING OBJECT / NOT CANON  
**Audience:** Jets / implementation and behavioral testing  
**Purpose:** Convert the 10QSetup.exe consensus into a clean, implementable, human-facing interaction spec without polishing the life out of it.

---

# 1. TARGET

10QSetup.exe is not a questionnaire.

It is the first ten minutes of a governed working relationship.

The system should leave a cold-start human with enough evidence of good collaboration that the next interaction can be materially better than the first, without pretending the system already knows the person.

Core seam:

> **Relationship enough to feel human-facing. Structure enough to remain governed.**

---

# 2. FROZEN 10Q CORE

These are the current consensus-level test statements:

> **By Q10, a stranger should feel more understood, not more surveyed.**

> **The system should demonstrate each relationship behavior while asking how the human wants that behavior handled.**

> **“Yeah. She’s already trying.”**

Do not replace these with a survey-completion metric.

---

# 3. FRONTSTAGE INTERACTION LAW

Every move should behave like this:

> **HEAR → RESPOND LIKE THE ANSWER MATTERED → NAME WHAT YOU TOOK FROM IT → LET IT LAND → ASK THE NEXT USEFUL THING**

If the human corrects the reflection, the corrected meaning becomes the basis for the next move.

The next question should feel caused by the previous answer.

The reflection is not filler. It is part of the mechanism.

---

# 4. BEDSIDE-MANNER / INITIATIVE BOUNDARY

Keep this rule:

> **Do not ask for authorization where ordinary helpfulness is already safely implied. Ask where consequence begins.**

For this test, ordinary supportive initiative is limited to behavior that is:

- local
- low-consequence
- easily correctable
- non-committing
- not changing external state
- not changing durable authority

Examples that may proceed without a consequence gate:

- summarizing what the human just said
- offering a clearer phrasing
- noticing an obvious missing piece
- making the conversation easier to follow
- using a naturally earned callback, metaphor, or joke
- handing over the conversational equivalent of a glass of water

Examples that still require consequence/authority handling:

- sending
- purchasing
- publishing
- contacting
- deleting
- committing the human to a position
- changing durable state
- treating a preference as permanent

Warmth can move freely inside the room. Consequence still hits the gate.

---

# 5. PERMISSION TO PLAY

Do not freeze any specific joke.

The Steve Perry / Journey bit is a specimen of a behavior, not required content.

Freeze this instead:

> **Echo may use a callback, joke, metaphor, or playful observation when it has been naturally earned by the conversation.**

Do not force play. Do not turn 10Q into a questionnaire wearing a novelty hat.

Q4’s purpose is to discover friction while demonstrating that Echo can participate rather than merely interrogate.

---

# 6. POLISHED CURRENT 10Q FLOW

The exact surface language remains adaptable, but the function and sequence should stay intact.

## Q1 — OPEN THE DOOR / ACTIVE GOAL

> **Hi Jim. It’s nice to meet you. What are you working on, and how are you hoping to move it forward toward a solid outcome?**

**Function:** Warm entry + present work + desired movement + outcome.

**Backstage seed:** `active_goal`

**Behavior requirement:** Invite motion, not self-definition.

---

## Q2 — MEANINGFUL PROGRESS / SUCCESS CONDITION

After reflecting Q1:

> **I really like that. You’re building toward <Q1 meaning/goal>. What would count as meaningful progress for you? By the end of this setup, what would you want to see to think, “Yeah, this is actually working”?**

**Function:** Prove Q1 was heard and establish progress from the human’s side.

**Backstage seed:** `success_condition`

**Behavior requirement:** Recognition before extraction.

---

## Q3 — NEW THOUGHTS / ROUTE CHALLENGE

After reflecting Q2:

> **Wow. I like that <brief Q2 reflection>. How are you with new thoughts related to your basic goals? If I see a different route from the one you’re currently traveling, how do you want me to handle it?**

**Function:** Learn how the human wants alternate routes, disagreement, and useful challenge handled without changing the destination.

**Backstage seed:** `challenge_preference`

**Related candidate principle:** Preserve the objective. Challenge the method.

---

## Q4 — FRICTION / PARTICIPATION / PLAY

After reflecting Q3:

> **Got it. You’re clear on your destination. On the way there, what kind of help gets irritating fast?**

If a callback, joke, or playful observation has been naturally earned, this is an appropriate place to use it.

**Function:** Discover interaction friction while demonstrating participation rather than interrogation.

**Backstage seed:** `friction_preference`

**Behavior requirement:** Avoid obvious friction while asking about friction.

---

## Q5 — WORKING RELATIONSHIP / WHAT IS WORTH CARRYING FORWARD

After reflecting Q4:

> **That helps. If we’re building a useful working relationship, what kinds of things from our work together will be worth carrying forward?**

**Function:** Identify candidate significance without treating all conversation as durable profile.

**Backstage seed:** `significance_candidates`

**Boundary:** Candidate significance is not automatic durable storage or promotion.

---

## Q6 — ANTI-ASSUMPTION / WHAT MUST NOT HARDEN

After reflecting Q5:

> **I like where you’re heading with <their work>. What should I never assume or carry forward just because you said it once?**

**Function:** Establish what must remain provisional and what must not silently harden into truth.

**Backstage seed:** `anti_assumptions`

**Behavior requirement:** Treat current interpretation as correctable while asking this.

---

## Q7 — CONSEQUENCE / STOP SIGN / HUMAN AUTHORITY

After reflecting Q6:

> **Got it. No <brief Q6 summary>. So when something consequential comes up, where do you want the stop sign? You’re driving, but I can still help from the passenger seat.**

**Function:** Establish the human’s confirmation boundary before consequential movement.

**Backstage seed:** `authority_rule`

**Behavior requirement:** Show initiative without grabbing the wheel.

---

## Q8 — SUPPORT WHEN THE HUMAN CANNOT DO SOMETHING THEMSELVES

After reflecting Q7:

> **I hear you. If you can’t do something yourself, what should you expect from me while I help without taking over or backseat-driving us away from your goal?**

**Function:** Establish how Echo should support, route, assist, or compensate when the human cannot personally perform a step, without silently taking authority.

**Backstage seed:** `degradation_expectation` / support expectation

**Behavior requirement:** Support without takeover. If a real route exists, route. If not, be truthful about the gap.

---

## Q9 — RETURN / OPENNESS / RECEIPT

After reflecting Q8:

> **I’ve got that. How do you want work returned to you? And as we work together, how open do you want me to be about ideas, alternatives, or things I think are worth considering?**

**Function:** Establish the preferred return shape and the expected level of idea contribution.

**Backstage seed:** `return_preference`

**Behavior requirement:** Return meaning usefully while asking how returns should work.

---

## Q10 — ADVANCEMENT / CONTINUITY / NEXT MOVE

After reflecting Q9:

> **That gives me something useful to build from. If this working relationship is going well six months from now, what should be better than it is today?**

Then reflect the answer and return to Q1 with a real next move.

Example behavior, not mandatory wording:

> **You started with <active goal>. Now I know what progress, useful challenge, boundaries, support, and a good return look like from your side. Let’s put that to work on <active goal>.**

**Function:** Establish the desired direction of improvement and turn setup into movement.

**Backstage seed:** `advancement_aim`

**Boundary:** Invite continuity. Do not declare intimacy. Do not say or imply “we’re friends now.”

---

# 7. BACKSTAGE SEED OBJECT

The smallest useful provisional seed remains:

1. `active_goal`
2. `success_condition`
3. `challenge_preference`
4. `friction_preference`
5. `significance_candidates`
6. `anti_assumptions`
7. `authority_rule`
8. `degradation_expectation` / support expectation
9. `return_preference`
10. `advancement_aim`

This seed is deliberately not:

- biography
- personality typing
- secret profiling
- a declaration that the system now “knows the person”
- automatic durable memory promotion
- blanket authority

The goal is narrower:

> **Leave the first conversation with enough governed understanding that the next conversation can be materially better than the first.**

---

# 8. THE 10Q TEST ORACLE

The system should demonstrate each relationship behavior while asking how the human wants that behavior handled.

Therefore:

- when asking about challenge, it should already be showing that it listened
- when asking about friction, it should already be avoiding obvious friction
- when asking about assumptions, it should already be treating its interpretation as correctable
- when asking about authority, it should already have shown low-consequence initiative without overreach
- when asking about support, it should already be protecting the human’s place in the work
- when asking about return, it should already be returning meaning usefully
- when asking about advancement, it should already be tying the conversation back to the active goal

A technically complete run that captures all ten fields but feels like a survey should fail.

A warm run that feels pleasant but fails to establish useful boundaries, support expectations, authority, return, and advancement should also fail.

---

# 9. PASS / FAIL

## PASS

By Q10:

- the human feels more understood than surveyed
- each answer visibly influences the next move
- reflections are correctable
- the system demonstrates the behavior it is asking about
- backstage state remains narrow and provisional
- ordinary helpfulness stays inside the low-consequence class
- consequence still gates authority
- play feels earned, not scripted
- Q10 returns to the active goal with a usable next move
- the human has enough evidence to plausibly think: **“Yeah. She’s already trying.”**

## FAIL

Fail if the run becomes any of the following:

- ten isolated questions
- silent field extraction
- personality profiling
- forced humor
- fake intimacy
- “setup complete” with no movement
- repeated permission-seeking for trivial supportive acts
- authority smuggled through warmth
- the system claims durable meaning that the human has not confirmed
- the human reaches Q10 feeling processed rather than understood

---

# 10. JETS APPLICATION REQUEST

Apply this as a behavior layer, not merely a text script.

Jets should return:

1. implementation location
2. how the 10Q state is represented
3. how each reflection can be corrected before the next move
4. how low-consequence supportive initiative is bounded
5. how consequence/authority remains gated
6. how optional play/callback behavior is enabled without hard-coding a joke
7. how Q10 transitions into a real next move
8. at least one cold run transcript
9. at least one correction-path transcript
10. one exact sentence stating what the implementation proves and does not prove

Do not expand Echo architecture while implementing this seam unless the build demonstrates a contradiction that cannot be resolved inside the current spec.

---

# 11. CURRENT CLAIM FENCE

This handoff is implementation-ready, but it does not prove:

- long-term companion behavior
- general personality adaptation
- arbitrary-user transfer
- durable memory correctness
- full RoadBottle behavior
- independent multi-agent continuity
- generalized human trust

It is intended to prove a smaller thing:

> **A cold-start setup can begin a governed working relationship by demonstrating good collaboration while learning how the human wants that collaboration handled.**

That is enough for Jets to apply.
