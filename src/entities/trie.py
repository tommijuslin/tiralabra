from trie_solmu import TrieSolmu

class Trie:
  def __init__(self):
    self.juuri = TrieSolmu()

  def lisaa_sana(self, sana):
    solmu = self.juuri

    for kirjain in sana:
      if kirjain not in solmu.lapset:
        solmu.lapset[kirjain] = TrieSolmu()
      solmu = solmu.lapset[kirjain]

    solmu.sana = sana
