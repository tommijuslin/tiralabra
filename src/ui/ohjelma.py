from operator import itemgetter

KOMENNOT = {
  "1:": "tarkista sanan oikeinkirjoitus",
  "2:": "lisää sana",
  "3:": "laske Levenshtein-etäisyys",
  "x:": "lopeta",
}

class Ohjelma():
  """Pääohjelma."""

  def __init__(self, io, levenshtein):
    """Luokan konstruktori.
    
    Parametrit:
      io: lukemiseen ja tulostamiseen käytettävä apuluokka
      levenshtein: editointietäisyyksien laskemiseen käytettävä luokka
    """

    self._io = io
    self._levenshtein = levenshtein

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
        self._tarkista_oikeinkirjoitus()
      elif komento == "2":
        self._lisaa_sana()
      elif komento == "3":
        self._laske_etaisyys()

  def _tulosta_ohje(self):
    """Tulostaa käyttöohjeet."""

    for komento, kuvaus in KOMENNOT.items():
      print(komento, kuvaus)

  def _tarkista_oikeinkirjoitus(self):
    """Tulostaa annetun sanan todennäköisimmät korjausvaihtoehdot."""

    sana = self._io.lue("sana: ")
    # max_etaisyys = int(self._io.lue("maksimietäisyys: "))
    sanat = self._levenshtein.etsi(sana)

    sanat.sort(key=itemgetter(2),reverse=True)
    sanat.sort(key=itemgetter(1))

    self._io.tulosta(f"==> {sanat[0][0]}")
  
  def _lisaa_sana(self):
    sana = self._io.lue("sana: ")
    self._levenshtein.sanakirja.lisaa(sana)

  def _laske_etaisyys(self):
    """Laskee annettujen sanojen välisen etäisyyden."""

    sana1 = self._io.lue("ensimmäinen sana: ")
    sana2 = self._io.lue("toinen sana: ")

    self._io.tulosta(f"==> {self._levenshtein.etaisyys(sana1, sana2)}")
