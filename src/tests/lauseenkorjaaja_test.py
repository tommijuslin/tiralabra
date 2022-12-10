import unittest
from entities.lauseenkorjaaja import Lauseenkorjaaja
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

class TestLauseenkorjaaja(unittest.TestCase):
  def setUp(self):
    io = StubIO([])
    sanakirja = TrieSolmu()
    self.sanasto = ["believe", "calendar", "caribbean", "fix", "these", "typos", "please"]
    for sana in self.sanasto:
      sanakirja.lisaa(sana)
    self.levenshtein = Levenshtein(sanakirja)
    self.lauseenkorjaaja = Lauseenkorjaaja(self.levenshtein, io)

  def test_korjaa_palauttaa_korjatun_lauseen(self):
    io = StubIO(["1", "1", "1"])
    self.lauseenkorjaaja = Lauseenkorjaaja(self.levenshtein, io)
    lause = ["fix","tehse","typops","pleaee"]
    korjattu_lause = self.lauseenkorjaaja.korjaa(lause)

    self.assertEqual(korjattu_lause,
      [("fix", False), ("these", True), ("typos", True), ("please", True)]
    )

  def test_korjaa_palauttaa_lauseen_oikein_jos_kayttaja_ei_korjaa_sanoja(self):
    io = StubIO(["q", "q", "q"])
    self.lauseenkorjaaja = Lauseenkorjaaja(self.levenshtein, io)
    lause = ["fix","tehse","typops","pleaee"]
    korjattu_lause = self.lauseenkorjaaja.korjaa(lause)

    self.assertEqual(korjattu_lause,
      [("fix", False), ("tehse", False), ("typops", False), ("pleaee", False)]
    )

  def test_korjaa_palauttaa_lauseen_sellaisenaan_jos_ei_korjausvaihtoehtoja(self):
    lause = ["juustopuuro", "painovoima", "pumputtaja"]
    korjattu_lause = self.lauseenkorjaaja.korjaa(lause)

    self.assertEqual(korjattu_lause,
      [("juustopuuro", False), ("painovoima", False), ("pumputtaja", False)]
    )

  def test_korjaa_palauttaa_lauseen_jos_ei_enempaa_vaihtoehtoja(self):
    io = StubIO(["", ""])
    self.lauseenkorjaaja = Lauseenkorjaaja(self.levenshtein, io)
    lause = ["pleaee"]
    korjattu_lause = self.lauseenkorjaaja.korjaa(lause)

    self.assertEqual(korjattu_lause,
      [("pleaee", False)]
    )
