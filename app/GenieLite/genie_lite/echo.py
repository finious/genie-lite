"""Deterministic Echo coordinator used to prove routing and correction behavior."""

from dataclasses import dataclass

from .create_specialist import CreateBrief, Specialist
from .receipts import WorkReceipt
from .state import GenieState


@dataclass(frozen=True)
class EchoReturn:
    heard: str
    route: str
    artifact: str
    receipt: WorkReceipt


class EchoCoordinator:
    """Shape intent, invoke CREATE, and return authorship/authority honestly."""

    def __init__(self, state: GenieState, specialist: Specialist):
        self.state = state
        self.specialist = specialist

    def handle(self, human_input: str) -> EchoReturn:
        self.state.record_human_input(human_input)
        goal = self.state.project_goal or human_input.strip()
        correction = self.state.corrections[-1] if self.state.corrections else None
        constraints = ["one page", "judge understands it in 30 seconds", "proposal only"]
        if correction:
            constraints.extend(
                [correction, "center human authority, specialist routing, receipts, and recovery"]
            )
        brief = CreateBrief(goal, "hackathon judge", constraints, correction)
        artifact = self.specialist(brief)
        self.state.record_specialist_return("ECHO → CREATE", artifact)
        receipt = WorkReceipt(
            human_request=human_input,
            echo_interpretation=goal,
            route="ECHO → CREATE",
            specialist="CREATE",
            specialist_return=artifact,
            correction_applied=correction,
            authority_state=self.state.authority.state.value,
            unproven_claims=["No execution", "No deployment", "No approval"],
        )
        return EchoReturn(goal, "ECHO → CREATE", artifact, receipt)
