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
  
  def lisaa(self, sana):
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
        return False
      solmu = solmu.lapset[kirjain]
    
    if solmu.sana != None:
      return True
    else:
      return False
