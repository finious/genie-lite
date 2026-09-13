import unittest

from genie_lite.authority import AuthorityRecord, AuthorityState


class AuthorityTests(unittest.TestCase):
    def test_authority_is_exact_and_expires_on_recovery(self):
        authority = AuthorityRecord()
        self.assertFalse(authority.permits("deploy"))
        authority.authorize("build")
        self.assertTrue(authority.permits("build"))
        self.assertFalse(authority.permits("deploy"))
        authority.expire_on_recovery()
        self.assertEqual(authority.state, AuthorityState.AUTHORIZED_RECORDED_EXPIRED)
        self.assertFalse(authority.permits("build"))


if __name__ == "__main__":
    unittest.main()
