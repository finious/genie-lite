import unittest

from genie_lite.create_specialist import deterministic_create
from genie_lite.echo import EchoCoordinator
from genie_lite.state import GenieState


REQUEST = "I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds."
CORRECTION = "Don't sell it as an AI friend. Make human authority, specialist routing, receipts, and recovery the center."


class CorrectionTraceTests(unittest.TestCase):
    def test_correction_changes_brief_and_artifact(self):
        coordinator = EchoCoordinator(GenieState("correction"), deterministic_create)
        first = coordinator.handle(REQUEST)
        second = coordinator.handle(CORRECTION)
        self.assertNotEqual(first.artifact, second.artifact)
        self.assertEqual(second.receipt.correction_applied, CORRECTION)
        self.assertIn("Human authority", second.artifact)


if __name__ == "__main__":
    unittest.main()
