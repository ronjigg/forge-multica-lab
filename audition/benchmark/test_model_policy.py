import unittest
from model_policy import choose_model
class ModelTests(unittest.TestCase):
    def setUp(self): self.cat={'muse':{'default':'spark','allowed':['spark','wonder']}}
    def test_default_and_explicit(self):
        self.assertEqual(choose_model('muse',self.cat),'spark')
        self.assertEqual(choose_model('muse',self.cat,'wonder'),'wonder')
    def test_no_unsafe_fallback(self):
        for w,req in [('unknown',None),('muse','unapproved')]:
            with self.assertRaises(ValueError): choose_model(w,self.cat,req)
        with self.assertRaises(ValueError): choose_model('muse',{'muse':{'default':'unapproved','allowed':['spark']}})
