KOMENNOT = {
  "1:": "tarkista sanan oikeinkirjoitus",
  "2:": "laske Levenshtein-etäisyys",
  "x:": "lopeta",
}

class App():
  def __init__(self, io, levenshtein):
    self._io = io
    self._levenshtein = levenshtein

  def kaynnista(self):
    while True:
      self._tulosta_ohje()
      komento = self._io.lue("komento: ")

      if komento == "x":
        break
      elif komento == "1":
        self._tarkista_oikeinkirjoitus()
      elif komento == "2":
        self._laske_etaisyys()

  def _tulosta_ohje(self):
    for komento, kuvaus in KOMENNOT.items():
      print(komento, kuvaus)

  def _laske_etaisyys(self):
    sana1 = self._io.lue("ensimmäinen sana: ")
    sana2 = self._io.lue("toinen sana: ")

    self._io.tulosta(f"\nEditointietäisyys: {self._levenshtein.etaisyys(sana1, sana2)}.\n")

  def _tarkista_oikeinkirjoitus(self):
    sana = self._io.lue("sana: ")
    max_etaisyys = int(self._io.lue("maksimietäisyys: "))
    sanat = self._levenshtein.etsi(sana, max_etaisyys)

    for sana in sanat:
      self._io.tulosta(f"{sana[0]}, {sana[1]}")
