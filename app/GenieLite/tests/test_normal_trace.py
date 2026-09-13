import unittest

from genie_lite.create_specialist import deterministic_create
from genie_lite.echo import EchoCoordinator
from genie_lite.state import GenieState


REQUEST = "I want to make a one-page public explainer for Genie Lite that a hackathon judge can understand in 30 seconds."


class NormalTraceTests(unittest.TestCase):
    def test_echo_routes_to_create_and_returns_a_receipt(self):
        result = EchoCoordinator(GenieState("normal"), deterministic_create).handle(REQUEST)
        self.assertEqual(result.route, "ECHO → CREATE")
        self.assertEqual(result.receipt.specialist, "CREATE")
        self.assertEqual(result.receipt.authority_state, "UNAUTHORIZED")
        self.assertIn("Nothing was approved, deployed, or verified", result.artifact)


if __name__ == "__main__":
    unittest.main()
