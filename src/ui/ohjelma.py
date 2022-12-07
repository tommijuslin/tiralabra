import re
from colorama import Fore

KOMENNOT = {
  "1:": "korjaa sana tai lause",
  "2:": "lisää sana",
  "x:": "lopeta",
}

class Ohjelma():
  """Pääohjelma."""

  def __init__(self, io, service):
    """Luokan konstruktori.

    Parametrit:
      io: lukemiseen ja tulostamiseen käytettävä apuluokka
      service: editointietäisyyksien laskemiseen käytettävä luokka
    """

    self._io = io
    self._service = service

  def kaynnista(self):
    """Ohjelman pääsilmukka.
       Lukee syötteitä ja kutsuu metodeja.
    """

    while True:
      self._tulosta_ohje()
      komento = self._io.lue("> ")

      if komento == "x":
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
      syote = re.findall(r"\w+|[^\w\s]", self._io.lue("> ").lower())
      if not syote:
        break
      korjattu_lause = self._service.korjaa(syote)
      self._io.tulosta(f"==> {self._muotoile_tulostus(korjattu_lause)}")

  def _lisaa_sana(self):
    """Lisää sanan sanakirjaan"""

    sana = self._io.lue("sana: ")
    self._service.lisaa(sana)

  def _muotoile_tulostus(self, lause):
    tulos = ""
    for sana in lause:
      if sana[-1] == 0:
        tulos += f"{sana[0]} "
      else:
        tulos += f"{Fore.GREEN}{sana[0]}{Fore.RESET} "

    # välimerkkien kanssa kikkailua
    tulos = re.sub(r' (?=[.?!,])', '', tulos)

    return tulos
