import unittest
from services.levenshtein_service import LevenshteinService
from entities.levenshtein import Levenshtein
from entities.trie_solmu import TrieSolmu

class StubIO:
  def __init__(self, inputs):
    self.inputs = inputs
    self.outputs = []

  def lue(self, teksti):
    return self.inputs.pop(0)

  def tulosta(self, teksti):
    self.outputs.append(teksti)

class TestLevenshteinService(unittest.TestCase):
  def setUp(self):
    io = StubIO([])
    sanakirja = TrieSolmu()
    self.sanasto = ["believe", "calendar", "caribbean", "fix", "these", "typos", "please"]
    for sana in self.sanasto:
      sanakirja.lisaa(sana)
    self.levenshtein = Levenshtein(sanakirja)
    self.service = LevenshteinService(io, self.levenshtein)

  def test_etaisyys_nolla_kun_sanat_samoja(self):
    etaisyys = self.service.etaisyys("samasana", "samasana")

    self.assertEqual(etaisyys, 0)

  def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_yksi(self):
    etaisyys = self.service.etaisyys("tyop", "typo")

    self.assertEqual(etaisyys, 1)

  def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_kolme(self):
    etaisyys = self.service.etaisyys("saturday", "sunday")

    self.assertEqual(etaisyys, 3)

  def test_lisaa_lisaa_sanan_sanakirjaan(self):
    self.service.lisaa("sana")
    sana = self.service._levenshtein.sanakirja.etsi("sana")

    self.assertTrue(sana)

  def test_korjaa_palauttaa_korjatun_lauseen(self):
    io = StubIO(["1", "1", "1"])
    self.service = LevenshteinService(io, self.levenshtein)
    lause = ["fix","tehse","typops","pleaee"]
    korjattu_lause = self.service.korjaa(lause)
    self.assertEqual(korjattu_lause, [("fix", 0), ("these", 1), ("typos", 1), ("please", 1)])

  def test_korjaa_palauttaa_lauseen_oikein_jos_kayttaja_ei_korjaa_sanoja(self):
    io = StubIO(["x", "x", "x"])
    self.service = LevenshteinService(io, self.levenshtein)
    lause = ["fix","tehse","typops","pleaee"]
    korjattu_lause = self.service.korjaa(lause)
    self.assertEqual(korjattu_lause, [("fix", 0), ("tehse", 0), ("typops", 0), ("pleaee", 0)])

  def test_korjaa_palauttaa_lauseen_sellaisenaan_jos_ei_korjausvaihtoehtoja(self):
    lause = ["juustopuuro", "painovoima", "pumputtaja"]
    korjattu_lause = self.service.korjaa(lause)
    self.assertEqual(korjattu_lause, [("juustopuuro", 0), ("painovoima", 0), ("pumputtaja", 0)])
