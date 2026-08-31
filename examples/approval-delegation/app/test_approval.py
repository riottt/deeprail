
import unittest
from datetime import datetime, timedelta, timezone
from approval import ProxyGrant, approve

class ApprovalTest(unittest.TestCase):
    def setUp(self):
        self.now=datetime(2026,8,29,tzinfo=timezone.utc)
        self.g=ProxyGrant("owner","proxy",self.now-timedelta(hours=1),self.now+timedelta(hours=1))
    def test_valid_proxy(self):
        r=approve(self.g,"proxy","owner",self.now)
        self.assertEqual(r["mode"],"proxy")
        self.assertEqual(r["on_behalf_of"],"owner")
    def test_unregistered_actor(self):
        with self.assertRaises(PermissionError): approve(self.g,"other","owner",self.now)
    def test_expired(self):
        with self.assertRaises(PermissionError): approve(self.g,"proxy","owner",self.now+timedelta(hours=2))
    def test_revoked(self):
        self.g.revoked=True
        with self.assertRaises(PermissionError): approve(self.g,"proxy","owner",self.now)

if __name__=="__main__": unittest.main()
