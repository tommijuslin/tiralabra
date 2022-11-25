KOMENNOT = {
  "1:": "korjaa sana tai lause",
  "2:": "laske editointietäisyys",
  "3:": "lisää sana",
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
      komento = self._io.lue("komento: ")

      if komento == "x":
        break
      elif komento == "1":
        self._korjaa_lause()
      elif komento == "2":
        self._laske_etaisyys()
      elif komento == "3":
        self._lisaa_sana()

  def _tulosta_ohje(self):
    """Tulostaa käyttöohjeet."""

    for komento, kuvaus in KOMENNOT.items():
      print(komento, kuvaus)

  def _korjaa_lause(self):
    """Korjaa syötteen kirjoitusvirheet."""

    self._io.tulosta("Syötä sana tai lause (tyhjä lopettaa)")

    while True:
      syote = self._io.lue("> ").lower().split()
      if not syote:
        break
      korjattu_lause = self._service.korjaa_lause(syote)

      self._io.tulosta(f"==> {self._service.muotoile_tulostus(korjattu_lause)}")
  
  def _laske_etaisyys(self):
    """Laskee annettujen sanojen välisen etäisyyden."""

    sana1 = self._io.lue("1. sana: ")
    sana2 = self._io.lue("2. sana: ")

    self._io.tulosta(f"==> {self._service.laske_etaisyys(sana1, sana2)}")

  def _lisaa_sana(self):
    """Lisää sanan sanakirjaan"""

    sana = self._io.lue("sana: ")
    self._service.lisaa_sana(sana)
