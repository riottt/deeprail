
import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/"examples/approval-delegation/app"
sys.path.insert(0,str(APP))
from approval import ProxyGrant, approve
from datetime import datetime, timedelta, timezone

class ExampleAppTest(unittest.TestCase):
    def test_golden_behavior(self):
        now=datetime(2026,8,29,tzinfo=timezone.utc)
        g=ProxyGrant("owner","proxy",now-timedelta(minutes=1),now+timedelta(minutes=1))
        r=approve(g,"proxy","owner",now)
        self.assertEqual(r["on_behalf_of"],"owner")

if __name__=="__main__": unittest.main()
