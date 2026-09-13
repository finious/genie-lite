import unittest

from genie_lite.state import GenieState


class StateTests(unittest.TestCase):
    def test_goal_and_correction_are_distinct(self):
        state = GenieState("session-1")
        state.record_human_input("Build a one-page explainer")
        state.record_human_input("Don't sell it as an AI friend")
        self.assertEqual(state.project_goal, "Build a one-page explainer")
        self.assertEqual(state.corrections, ["Don't sell it as an AI friend"])


if __name__ == "__main__":
    unittest.main()
