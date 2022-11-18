class TrieSolmu:
  def __init__(self):
    self.lapset = {}
    self.sana = None
  
  def lisaa_sana(self, sana):
    solmu = self

    for kirjain in sana:
      if kirjain not in solmu.lapset:
        solmu.lapset[kirjain] = TrieSolmu()
      solmu = solmu.lapset[kirjain]

    solmu.sana = sana
