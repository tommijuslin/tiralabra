class TrieSolmu:
  def __init__(self):
    self.lapset = {}
    self.sana = None
  
  def lisaa(self, sana):
    solmu = self

    for kirjain in sana:
      if kirjain not in solmu.lapset:
        solmu.lapset[kirjain] = TrieSolmu()
      solmu = solmu.lapset[kirjain]

    solmu.sana = sana

  def etsi(self, sana):
    solmu = self

    for kirjain in sana:
      if kirjain not in solmu.lapset:
        return False
      solmu = solmu.lapset[kirjain]
    
    if solmu.sana != None:
      return True
    else:
      return False
