import unittest
from job_status import summarise_jobs
class JobTests(unittest.TestCase):
    def test_counts(self):
        jobs=[{'status':s} for s in ('queued','starting','running','running','completed','blocked','failed')]
        self.assertEqual(summarise_jobs(jobs),{'queued':1,'starting':1,'active':2,'done':1,'attention':2})
    def test_empty_and_invalid(self):
        self.assertEqual(summarise_jobs([]),{'queued':0,'starting':0,'active':0,'done':0,'attention':0})
        with self.assertRaises(ValueError): summarise_jobs([{'status':'magically-working'}])
