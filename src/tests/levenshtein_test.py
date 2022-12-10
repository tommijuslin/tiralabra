import unittest
from entities.levenshtein import Levenshtein
from entities.trie_solmu import TrieSolmu


class TestLevenshtein(unittest.TestCase):
    def setUp(self):
        sanakirja = TrieSolmu()
        sanasto = ["believe", "calendar", "caribbean"]
        for sana in sanasto:
            sanakirja.lisaa(sana)
        self.levenshtein = Levenshtein(sanakirja)

    def test_etaisyys_nolla_kun_sanat_samoja(self):
        etaisyys = self.levenshtein.etaisyys("eieroa", "eieroa")

        self.assertEqual(etaisyys, 0)

    def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksena_yksi_poisto(self):
        etaisyys = self.levenshtein.etaisyys("mornning", "morning")

        self.assertEqual(etaisyys, 1)

    def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksena_yksi_lisays(self):
        etaisyys = self.levenshtein.etaisyys("mornin", "morning")

        self.assertEqual(etaisyys, 1)

    def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksena_yksi_vaihto(self):
        etaisyys = self.levenshtein.etaisyys("morming", "morning")

        self.assertEqual(etaisyys, 1)

    def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksena_yksi_siirto(self):
        etaisyys = self.levenshtein.etaisyys("omrning", "morning")

        self.assertEqual(etaisyys, 1)

    def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_kaksi(self):
        etaisyys = self.levenshtein.etaisyys("mornnin", "morning")

        self.assertEqual(etaisyys, 2)

    def test_etaisyys_laskee_etaisyyden_oikein_kun_muutoksia_kolme(self):
        etaisyys = self.levenshtein.etaisyys("saturday", "sunday")

        self.assertEqual(etaisyys, 3)

    def test_etsi_ei_palauta_sanaa_jos_kohdesana_ei_sanakirjassa(self):
        sanat = self.levenshtein.etsi("cemetary")

        self.assertEqual(len(sanat), 0)

    def test_etsi_palauttaa_korjatun_sanan(self):
        sanat = self.levenshtein.etsi("beleive", 1)

        self.assertEqual(sanat[0][0], ("believe"))
