from operator import itemgetter
from colorama import Fore

VAIHTOEHTOJEN_MAARA = 3

class LevenshteinService:
  """Välittää pyynnöt Levenshtein-luokalle."""

  def __init__(self, io, levenshtein):
    """Luokan konstruktori.

    Parametrit:
      levenshtein: Levenshtein-etäisyyksien laskemiseen käytettävä luokka
    """

    self._io = io
    self._levenshtein = levenshtein

  def korjaa(self, lause):
    """Korjaa syötteen kirjoitusvirheet.

    Parametrit:
      lause: Käyttäjän syöttämä lause

    Palauttaa:
      Listan korjatuista sanoista
    """

    korjattu_lause = []

    for sana in lause:
      on_sanakirjassa = self._levenshtein.sanakirja.etsi(sana)
      if not sana.isalpha() or on_sanakirjassa[0]:
        # Tuplen toinen alkio merkkaa sanan muokatuksi. 1 = muokattu
        korjattu_lause.append((sana, False))
        continue

      vaihtoehdot = self.etsi_korjausvaihtoehdot(sana)

      if not vaihtoehdot:
        korjattu_lause.append((sana, False))
      else:
        korjattu_sana = self._korjaa_sana(sana, vaihtoehdot)
        korjattu_lause.append((korjattu_sana[0], korjattu_sana[1]))

    return korjattu_lause

  def etsi_korjausvaihtoehdot(self, sana):
    """Etsii korjausvaihtoehdot annetulle sanalle ja järjestää ne todennäköisyyden mukaan"""
    vaihtoehdot = (self._levenshtein.etsi(sana))
    # Järjestää sanat 1. etäisyyden mukaan ja 2. frekvenssin mukaan
    vaihtoehdot.sort(key=itemgetter(2),reverse=True)
    vaihtoehdot.sort(key=itemgetter(1))

    return vaihtoehdot

  def _korjaa_sana(self, sana, vaihtoehdot):
    sanat = iter(vaihtoehdot)
    self._io.tulosta(f"-> {Fore.RED}{sana}{Fore.RESET} <-")

    indeksi = 0
    while True:
      self.tulosta_vaihtoehdot(sanat)
      valinta = self._io.lue("> ")
      if valinta == "x" or indeksi > len(vaihtoehdot):
        return sana, False
      if not valinta:
        indeksi += VAIHTOEHTOJEN_MAARA
        continue

      return vaihtoehdot[int(valinta) + indeksi - 1][0], 1

  def tulosta_vaihtoehdot(self, vaihtoehdot):
    """Tulostaa korjausvaihtoehdot
    Kerralla tulostettavien vaihtoehtojen määrän voi vaihtaa VAIHTOEHTOJEN_MAARA-muuttujan avulla
    """

    indeksi = 1
    while indeksi <= VAIHTOEHTOJEN_MAARA:
      try:
        self._io.tulosta(f"{indeksi}: {next(vaihtoehdot)[0]}")
      except StopIteration:
        self._io.tulosta(f"{Fore.RED}Ei enempää vaihtoehtoja{Fore.RESET}")
        break
      indeksi += 1
    self._io.tulosta("(x: lopeta etsiminen)")
    if indeksi == VAIHTOEHTOJEN_MAARA + 1:
      self._io.tulosta("(tyhjä: lisää vaihtoehtoja)")

  def lisaa(self, sana):
    """Lisää sanan sanakirjaan

    Parametrit:
      sana: lisättävä sana
    """

    self._levenshtein.sanakirja.lisaa(sana)

  def etaisyys(self, sana1, sana2):
    """Laskee sanaparin välisen editointietäisyyden

    Parametrit:
      sana1: vertailtava sana
      sana2: vertailtava sana

    Palauttaa:
      sanaparin välisen editointietäisyyden
    """

    return self._levenshtein.etaisyys(sana1, sana2)
