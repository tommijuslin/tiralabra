import re
from colorama import Fore
from sanakirja import kirjoita_lisatyt_sanat_tiedostoon

KOMENNOT = {
    "1:": "korjaa sana tai lause",
    "2:": "lisää sana",
    "q:": "lopeta",
}


class Ohjelma():
    """Pääohjelma."""

    def __init__(self, io, levenshtein, lauseenkorjaaja):
        """Luokan konstruktori.

        Parametrit:
          io: lukemiseen ja tulostamiseen käytettävä apuluokka
          lauseenkorjaaja: lauseen korjaamiseen käytettävä luokka
        """

        self._io = io
        self._levenshtein = levenshtein
        self._lauseenkorjaaja = lauseenkorjaaja
        self._lisatyt_sanat = []

    def kaynnista(self):
        """Ohjelman pääsilmukka.
           Lukee syötteitä ja kutsuu metodeja.
        """

        while True:
            self._tulosta_ohje()
            komento = self._io.lue("> ")

            if komento == "q":
                if self._lisatyt_sanat:
                    kirjoita_lisatyt_sanat_tiedostoon(self._lisatyt_sanat)
                break
            if komento == "1":
                self._korjaa_lause()
            elif komento == "2":
                self._lisaa_sana()

    def _tulosta_ohje(self):
        """Tulostaa käyttöohjeet."""

        self._io.tulosta(24*"=")
        for komento, kuvaus in KOMENNOT.items():
            print(komento, kuvaus)
        self._io.tulosta(24*"=")

    def _korjaa_lause(self):
        """Korjaa syötteen kirjoitusvirheet."""

        self._io.tulosta("Syötä sana tai lause (tyhjä lopettaa):")

        while True:
            lause = re.findall(r"\w+|[^\w\s]", self._io.lue("> ").lower())
            if not lause:
                break
            korjattu_lause = self._lauseenkorjaaja.korjaa(lause)
            self._io.tulosta(f"==> {self._muotoile_tulostus(korjattu_lause)}")

    def _lisaa_sana(self):
        """Lisää sanan sanakirjaan"""

        sana = self._io.lue("sana: ")
        try:
            self._lisatyt_sanat.append(sana)
            self._levenshtein.sanakirja.lisaa(sana)
        except OSError:
            self._io.tulosta("Sanan lisääminen ei onnistunut")
        else:
            self._io.tulosta(f"{Fore.GREEN}{sana}{Fore.RESET} lisätty sanakirjaan")

    def _muotoile_tulostus(self, lause):
        tulos = ""
        for sana in lause:
            if sana[-1] == 0:
                tulos += f"{sana[0]} "
            else:
                tulos += f"{Fore.GREEN}{sana[0]}{Fore.RESET} "

        tulos = re.sub(r' (?=[.?!,])', '', tulos)

        return tulos
