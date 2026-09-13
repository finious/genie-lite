"""Small, inspectable state model for the contest proof."""

from dataclasses import dataclass, field

from .authority import AuthorityRecord


@dataclass
class GenieState:
    session_id: str
    project_goal: str | None = None
    collaboration_seed: dict[str, str] = field(default_factory=dict)
    corrections: list[str] = field(default_factory=list)
    authority: AuthorityRecord = field(default_factory=AuthorityRecord)
    last_specialist_route: str | None = None
    last_returned_artifact: str | None = None
    last_human_input: str | None = None

    def record_human_input(self, text: str) -> None:
        cleaned = text.strip()
        self.last_human_input = cleaned
        markers = ("don't", "do not", "correction", "instead", "change")
        if any(marker in cleaned.lower() for marker in markers):
            self.apply_correction(cleaned)
        elif not self.project_goal:
            self.project_goal = cleaned

    def apply_correction(self, correction: str) -> None:
        cleaned = correction.strip()
        if cleaned and (not self.corrections or self.corrections[-1] != cleaned):
            self.corrections.append(cleaned)

    def record_specialist_return(self, route: str, artifact: str) -> None:
        self.last_specialist_route = route
        self.last_returned_artifact = artifact

    def recover_after_interruption(self) -> "GenieState":
        recovered = GenieState(
            session_id=self.session_id,
            project_goal=self.project_goal,
            collaboration_seed=dict(self.collaboration_seed),
            corrections=list(self.corrections),
            authority=AuthorityRecord(
                state=self.authority.state,
                scope=self.authority.scope,
                granted_by=self.authority.granted_by,
            ),
            last_specialist_route=self.last_specialist_route,
            last_returned_artifact=self.last_returned_artifact,
            last_human_input=self.last_human_input,
        )
        recovered.authority.expire_on_recovery()
        return recovered
