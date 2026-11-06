import unittest
from recovery import review_recovery
class RecoveryTests(unittest.TestCase):
    def test_only_stale_starting(self):
        inp=[{'id':'a','status':'starting','started_at':10},{'id':'b','status':'starting','started_at':95},{'id':'c','status':'running','started_at':10}]
        got=review_recovery(inp,now=100,max_starting_seconds=30)
        self.assertEqual((got[0]['status'],got[0]['reason']),('attention','START_TIMEOUT'))
        self.assertEqual(got[1]['status'],'starting')
        self.assertEqual(got[2]['status'],'running')
        self.assertEqual(inp[0]['status'],'starting')
    def test_boundary_and_copy(self):
        jobs=[{'id':'a','status':'starting','started_at':70}]
        out=review_recovery(jobs,now=100,max_starting_seconds=30)
        self.assertEqual(out[0]['status'],'starting')
        self.assertIsNot(out[0],jobs[0])
