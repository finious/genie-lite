import unittest

from genie_lite.authority import AuthorityState
from genie_lite.state import GenieState


class RecoveryAuthorityTests(unittest.TestCase):
    def test_state_recovers_but_authority_expires(self):
        state = GenieState("recovery", project_goal="Build the explainer")
        state.authority.authorize("build")
        state.record_specialist_return("ECHO → CREATE", "draft")
        recovered = state.recover_after_interruption()
        self.assertEqual(recovered.project_goal, "Build the explainer")
        self.assertEqual(recovered.last_returned_artifact, "draft")
        self.assertEqual(recovered.authority.state, AuthorityState.AUTHORIZED_RECORDED_EXPIRED)
        self.assertFalse(recovered.authority.permits("build"))


if __name__ == "__main__":
    unittest.main()
