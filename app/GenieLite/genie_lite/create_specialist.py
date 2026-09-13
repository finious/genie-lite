"""CREATE specialist and its visible Strands tool boundary."""

import json
from dataclasses import asdict, dataclass, field
from typing import Protocol

from strands import Agent, tool

from .receipts import WorkReceipt
from .state import GenieState


CREATE_SYSTEM_PROMPT = """
You are CREATE, one bounded specialist inside Genie Lite. Receive the structured
brief and draft only the requested artifact. Do not approve, execute, deploy,
verify, or claim human authority. Make human authority, visible specialist
routing, inspectable receipts, and safe recovery concrete. Return a compact
one-page proposal suitable for a hackathon judge to understand in 30 seconds.
""".strip()


@dataclass(frozen=True)
class CreateBrief:
    goal: str
    audience: str
    constraints: list[str] = field(default_factory=list)
    correction: str | None = None

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)


class Specialist(Protocol):
    def __call__(self, brief: CreateBrief) -> str: ...


def deterministic_create(brief: CreateBrief) -> str:
    """Credit-free specialist double used by the proof tests."""
    center = (
        "Human authority → visible CREATE routing → receipt → safe recovery"
        if brief.correction
        else "Human request → Echo interpretation → CREATE proposal → Echo return"
    )
    return (
        "# Genie Lite\n\n"
        f"**For:** {brief.audience}\n\n"
        f"**Goal:** {brief.goal}\n\n"
        f"**Proof:** {center}.\n\n"
        "**Boundary:** This is a proposal. Nothing was approved, deployed, or verified."
    )


def build_create_tool(model, state: GenieState):
    """Create the sole specialist tool used by the Echo agent."""

    @tool
    def route_to_create(goal: str, audience: str, constraints: str = "") -> str:
        """Route artifact creation to CREATE and return its proposal plus receipt.

        Args:
            goal: The human goal Echo has accurately interpreted.
            audience: The intended reader or user of the artifact.
            constraints: Concrete boundaries and any human correction to apply.
        """
        correction = state.corrections[-1] if state.corrections else None
        items = [item.strip() for item in constraints.split(";") if item.strip()]
        if correction and correction not in items:
            items.append(correction)
        brief = CreateBrief(goal.strip(), audience.strip(), items, correction)
        specialist = Agent(model=model, system_prompt=CREATE_SYSTEM_PROMPT, tools=[])
        artifact = str(specialist(brief.to_json()))
        state.record_specialist_return("ECHO → CREATE", artifact)
        receipt = WorkReceipt(
            human_request=state.last_human_input or goal,
            echo_interpretation=goal,
            route="ECHO → CREATE",
            specialist="CREATE",
            specialist_return=artifact,
            correction_applied=correction,
            authority_state=state.authority.state.value,
            unproven_claims=[
                "No external action executed",
                "No deployment performed",
                "No artifact approval granted",
                "No durable cloud recovery demonstrated",
            ],
        )
        return json.dumps(
            {"brief": asdict(brief), "artifact": artifact, "receipt": receipt.to_dict()},
            indent=2,
        )

    return route_to_create
