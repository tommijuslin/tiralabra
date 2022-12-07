import unittest
from entities.trie_solmu import TrieSolmu

class TestTrieSolmu(unittest.TestCase):
  def setUp(self):
    self.sanakirja = TrieSolmu()

  def test_lisatty_sana_loytyy(self):
    self.sanakirja.lisaa("sana")
    sana = self.sanakirja.etsi("sana")

    self.assertTrue(sana)

  def test_sanaa_jota_ei_ole_lisatty_ei_loydy(self):
    sana = self.sanakirja.etsi("sana")

    self.assertFalse(sana[0])

  def test_sanaa_ei_loydy_vaikka_sama_alkuosa(self):
    self.sanakirja.lisaa("sanakirja")
    sana = self.sanakirja.etsi("sana")

    self.assertFalse(sana[0])
