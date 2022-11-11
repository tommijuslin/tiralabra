import unittest
from levenshtein import Levenshtein

class TestLevenshtein(unittest.TestCase):
  def setUp(self):
    sanasto = ["believe", "calendar", "caribbean"]
    self.levenshtein = Levenshtein(sanasto)
  
  def test_etaisyys_nolla_kun_sanat_samoja(self):
    etaisyys = self.levenshtein.etaisyys("eieroa", "eieroa")

    self.assertEqual(etaisyys, 0)

  def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_yksi(self):
    etaisyys = self.levenshtein.etaisyys("typi", "typo")

    self.assertEqual(etaisyys, 1)
  
  def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_kolme(self):
    etaisyys = self.levenshtein.etaisyys("saturday", "sunday")

    self.assertEqual(etaisyys, 3)
  
  def test_etsi_ei_palauta_sanaa_jos_kohdesana_ei_sanastossa(self):
    sanat = self.levenshtein.etsi("cemetary", 1)

    self.assertEqual(len(sanat), 0)

  def test_etsi_palauttaa_oikeat_sanat_ja_etaisyydet_jos_kohdesana_sanastossa(self):
    sanat = self.levenshtein.etsi("beleive", 2)

    self.assertEqual(sanat[0], ["believe", 2])
