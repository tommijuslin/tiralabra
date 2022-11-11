import unittest
from levenshtein import Levenshtein

class TestLevenshtein(unittest.TestCase):
  def setUp(self):
    self.levenshtein = Levenshtein()
  
  def test_etaisyys_nolla_kun_sanat_samoja(self):
    etaisyys = self.levenshtein.etaisyys("eieroa", "eieroa")

    self.assertEqual(etaisyys, 0)

  def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_yksi(self):
    etaisyys = self.levenshtein.etaisyys("typi", "typo")

    self.assertEqual(etaisyys, 1)
  
  def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_kolme(self):
    etaisyys = self.levenshtein.etaisyys("saturday", "sunday")

    self.assertEqual(etaisyys, 3)
