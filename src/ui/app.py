from levenshtein import levenshtein

KOMENNOT = {
  "1": "laske Levenshtein-etäisyys",
  "x": "lopeta",
}

class App():
  def __init__(self, io):
    self._io = io

  def kaynnista(self):

    while True:
      self._tulosta_ohje()
      komento = self._io.lue("komento: ")

      if komento == "x":
        break
      elif komento == "1":
        self._laske_etaisyys()

  def _tulosta_ohje(self):
    for komento, kuvaus in KOMENNOT.items():
      print(komento, kuvaus)

  def _laske_etaisyys(self):
    sana1 = self._io.lue("ensimmäinen sana: ")
    sana2 = self._io.lue("toinen sana: ")
    self._io.tulosta(levenshtein(sana1, sana2))
