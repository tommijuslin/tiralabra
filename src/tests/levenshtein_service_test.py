import unittest
from services.levenshtein_service import LevenshteinService
from entities.levenshtein import Levenshtein
from entities.trie_solmu import TrieSolmu

class TestLevenshteinService(unittest.TestCase):
  def setUp(self):
    sanakirja = TrieSolmu()
    sanasto = ["believe", "calendar", "caribbean", "fix", "these", "typos", "please"]
    for sana in sanasto:
      sanakirja.lisaa(sana)
    levenshtein = Levenshtein(sanakirja)
    self.service = LevenshteinService(levenshtein)

  def test_etaisyys_nolla_kun_sanat_samoja(self):
    etaisyys = self.service.etaisyys("samasana", "samasana")

    self.assertEqual(etaisyys, 0)

  def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_yksi(self):
    etaisyys = self.service.etaisyys("tyop", "typo")

    self.assertEqual(etaisyys, 1)

  def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_kolme(self):
    etaisyys = self.service.etaisyys("saturday", "sunday")

    self.assertEqual(etaisyys, 3)

  def test_korjaa_lause_palauttaa_korjatun_lauseen(self):
    lause = ["fix","tehse","typops","pleaee"]
    korjattu_lause = self.service.korjaa(lause)

    self.assertEqual(korjattu_lause, [("fix", 0), ("these", 1), ("typos", 1), ("please", 1)])

  def test_lisaa_sana_lisaa_sanan_sanakirjaan(self):
    self.service.lisaa_sana("sana")
    sana = self.service._levenshtein.sanakirja.etsi("sana")

    self.assertTrue(sana)
