from operator import itemgetter

class LevenshteinService:
  def __init__(self, levenshtein):
    self._levenshtein = levenshtein

  def korjaa_lause(self, syote):
    lause = []

    for sana in syote:
      korjausvaihtoehdot = (self._levenshtein.etsi(sana))
      korjausvaihtoehdot.sort(key=itemgetter(2),reverse=True)
      korjausvaihtoehdot.sort(key=itemgetter(1))
      lause.append(korjausvaihtoehdot[0][0])

    lause = " ".join(lause)

    return lause
  
  def lisaa_sana(self, sana):
    self._levenshtein.sanakirja.lisaa(sana)
  
  def laske_etaisyys(self, sana1, sana2):
    return self._levenshtein.etaisyys(sana1, sana2)
