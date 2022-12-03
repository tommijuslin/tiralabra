class Levenshtein:
  """Luokka kahden sanan välisen etäisyyden laskemiseen"""

  def __init__(self, sanakirja):
    """Luokan konstruktori.

    Parametrit:
      sanakirja: sanat, joihin käyttäjän syöttämiä sanoja verrataan
    """

    self.sanakirja = sanakirja

  def etsi(self, sana, max_etaisyys=2):
    """Etsii sanakirjasta sanat, joiden etäisyys annettuun sanaan
       on enintään annettu maksimietäisyys

    Parametrit:
      sana: sana, jolle korjausvaihtoehtoja etsitään
      max_etaisyys: sanojen maksimietäisyys etsittävästä sanasta

    Palauttaa:
      listan löydetyistä sanoista
    """

    sana = self._siisti_sana(sana)
    nykyinen_rivi = range(len(sana) + 1)

    sanat = []

    for kirjain in self.sanakirja.lapset:
      self._etsi_rekursiivisesti(self.sanakirja.lapset[kirjain], kirjain, None, sana,
        nykyinen_rivi, None, sanat, max_etaisyys)

    return sanat

  def _etsi_rekursiivisesti(self, solmu, kirjain, edellinen_kirjain, sana,
    edellinen_rivi, e_edellinen_rivi, sanat, max_etaisyys):
    """Sanojen etsimiseen käytettävä apufunktio

    Parametrit:
      solmu: trie-solmu, joka kuvaa yksittäistä kirjainta
      kirjain: seuraavaksi tarkasteltava kirjain
      edellinen_kirjain: viimeksi tarkasteltu kirjain
      sana: sana, jolle korjausvaihtoehtoja etsitään
      edellinen_rivi: Levenshtein-matriisin edellinen rivi
      e_edellinen_rivi: Levenshtein-matriisin edellisestä edellinen rivi
      sanat: lista mahdollisista korjausvaihtoehdoista
      max_etaisyys: sanojen maksimietäisyys etsittävästä sanasta
    """

    nykyinen_rivi = self._laske_etaisyys(sana, kirjain, edellinen_kirjain,
      edellinen_rivi, e_edellinen_rivi)

    if nykyinen_rivi[-1] <= max_etaisyys and solmu.sana is not None:
      sanat.append((solmu.sana, nykyinen_rivi[-1], solmu.frekvenssi))

    if min(nykyinen_rivi) <= max_etaisyys:
      edellinen_kirjain = kirjain
      for kirjain in solmu.lapset:
        self._etsi_rekursiivisesti(solmu.lapset[kirjain], kirjain, edellinen_kirjain, sana,
          nykyinen_rivi, edellinen_rivi, sanat, max_etaisyys)

  def _laske_etaisyys(self, sana, kirjain, edellinen_kirjain, edellinen_rivi, e_edellinen_rivi):
    """Laskee Levenshtein-matriisin yhden rivin

    Parametrit:
      sana: vertailtava sana
      kirjain: vertailukohteen seuraava kirjain
      edellinen_kirjain: viimeksi tarkasteltu kirjain
      edellinen_rivi: Levenshtein-matriisin edellinen rivi
      e_edellinen_rivi: Levenshtein-matriisin edellisestä edellinen rivi

    Palauttaa:
      Levenshtein-matriisin rivin
    """

    nykyinen_rivi = [edellinen_rivi[0] + 1]

    for sarake in range(1, len(sana) + 1):
      poisto = edellinen_rivi[sarake] + 1
      lisays = nykyinen_rivi[sarake - 1] + 1

      if sana[sarake - 1] == kirjain:
        vaihto = edellinen_rivi[sarake - 1]
      else:
        vaihto = edellinen_rivi[sarake - 1] + 1

      nykyinen_rivi.append(min(poisto, lisays, vaihto))

      # Damerau-Levenshtein
      if sarake > 1 and sana[sarake - 1] == edellinen_kirjain and sana[sarake - 2] == kirjain:
        nykyinen_rivi[sarake] = min(nykyinen_rivi[sarake],
                                    e_edellinen_rivi[sarake - 2] + 1)

    return nykyinen_rivi

  def etaisyys(self, sana1, sana2):
    """Palauttaa sanojen välisen etäisyyden

    Parametrit:
      sana1: vertailtava sana
      sana2: vertailtava sana

    Palauttaa:
      sanojen välisen etäisyyden
    """

    sana1 = self._siisti_sana(sana1)
    sana2 = self._siisti_sana(sana2)

    taulu = [range(len(sana1) + 1)]

    edellinen_kirjain = None
    e_edellinen_rivi = None
    rivi = 0
    for indeksi, kirjain in enumerate(sana2):
      if indeksi > 0:
        edellinen_kirjain = sana2[indeksi - 1]
        e_edellinen_rivi = taulu[rivi - 1]
      taulu.append(self._laske_etaisyys(sana1, kirjain, edellinen_kirjain,
        taulu[rivi], e_edellinen_rivi))
      rivi += 1

    return taulu[rivi][-1]

  def _siisti_sana(self, sana):
    return sana.strip().lower()
