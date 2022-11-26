from operator import itemgetter

class LevenshteinService:
  """Välittää pyynnöt Levenshtein-luokalle."""

  def __init__(self, levenshtein):
    """Luokan konstruktori.

    Parametrit:
      levenshtein: Levenshtein-etäisyyksien laskemiseen käytettävä luokka
    """

    self._levenshtein = levenshtein

  def korjaa_lause(self, syote):
    """Korjaa syötteen kirjoitusvirheet.

    Palauttaa:
      Listan korjatuista sanoista
    """

    lause = []

    for sana in syote:
      sanat = (self._levenshtein.etsi(sana))
      # Järjestää sanat 1. etäisyyden mukaan ja 2. frekvenssin mukaan
      sanat.sort(key=itemgetter(2),reverse=True)
      sanat.sort(key=itemgetter(1))

      # Tuplen toinen alkio merkkaa sanan muokatuksi. 1 = muokattu
      if not sanat or sanat[0][0] == sana:
        lause.append((sana, 0))
      else:
        lause.append((sanat[0][0], 1))

    return lause

  def lisaa_sana(self, sana):
    """Lisää sanan sanakirjaan

    Parametrit:
      sana: lisättävä sana
    """

    self._levenshtein.sanakirja.lisaa(sana)

  def laske_etaisyys(self, sana1, sana2):
    """Laskee sanaparin välisen editointietäisyyden

    Parametrit:
      sana1: vertailtava sana
      sana2: vertailtava sana

    Palauttaa:
      sanaparin välisen editointietäisyyden
    """

    return self._levenshtein.etaisyys(sana1, sana2)
