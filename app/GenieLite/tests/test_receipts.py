import unittest

from genie_lite.receipts import WorkReceipt


class ReceiptTests(unittest.TestCase):
    def test_receipt_names_roles_and_limits(self):
        receipt = WorkReceipt(
            human_request="Make a page",
            echo_interpretation="Create a one-page explainer",
            route="ECHO → CREATE",
            specialist="CREATE",
            specialist_return="draft",
            authority_state="UNAUTHORIZED",
            unproven_claims=["No deployment"],
        ).to_dict()
        self.assertEqual(receipt["specialist"], "CREATE")
        self.assertEqual(receipt["action_state"], "PROPOSED_ONLY")
        self.assertIn("No deployment", receipt["unproven_claims"])


if __name__ == "__main__":
    unittest.main()
