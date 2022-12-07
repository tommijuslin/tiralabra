class TrieSolmu:
  """Trie-tietorakenne, joka toimii sanakirjana"""

  def __init__(self):
    """Luokan konstruktori

    Parametrit:
      lapset: solmun lapset, tässä tapauksessa yksittäiset kirjaimet
      sana: määrittelee mihin solmuun (kirjaimeen) sana loppuu
    """

    self.lapset = {}
    self.sana = None
    self.frekvenssi = None

  def lisaa(self, sana, frekvenssi=1):
    """Lisää sanan sanakirjaan

    Parametri:
      sana: lisättävä sana
    """

    solmu = self

    for kirjain in sana:
      if kirjain not in solmu.lapset:
        solmu.lapset[kirjain] = TrieSolmu()
      solmu = solmu.lapset[kirjain]

    solmu.sana = sana
    solmu.frekvenssi = frekvenssi

  def etsi(self, sana):
    """Etsii sanan sanakirjasta

    Parametri:
      sana: etsittävä sana

    Palauttaa:
      totuusarvon sanan löytymisestä
    """

    solmu = self

    for kirjain in sana:
      if kirjain not in solmu.lapset:
        return False, 0
      solmu = solmu.lapset[kirjain]

    tulos = solmu.sana is not None
    if tulos:
      return True, solmu.frekvenssi

    return False, 0
