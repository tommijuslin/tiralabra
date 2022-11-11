class Levenshtein:
  def __init__(self, sanasto):
    self.sanasto = sanasto
    self.sana1 = ""
    self.sana2 = ""
    self.rivit = 0
    self.sarakkeet = 0
    self.taulu = []
  
  def etsi(self, syote, max_etaisyys):
    sanat = []

    for kohdesana in self.sanasto:
      etaisyys = self.etaisyys(syote, kohdesana)
      if etaisyys <= max_etaisyys:
        sanat.append([kohdesana, etaisyys])
      
    return sanat
  
  def etaisyys(self, sana1, sana2):
    self._alusta_ja_siivoa_sanat(sana1, sana2)
    self._alusta_taulu()

    return self._laske_etaisyys()
  
  def _alusta_ja_siivoa_sanat(self, sana1, sana2):
    self.sana1 = sana1.lower()
    self.sana2 = sana2.lower()
    self.rivit = len(sana1) + 1
    self.sarakkeet = len(sana2) + 1
  
  def _alusta_taulu(self):
    del self.taulu[:]

    self.taulu = [[0 for sarake in range(self.sarakkeet)] for rivi in range(self.rivit)]

    for rivi in range(1, self.rivit):
      self.taulu[rivi][0] = rivi
  
    for sarake in range(1, self.sarakkeet):
      self.taulu[0][sarake] = sarake

  def _laske_etaisyys(self):
    muutos = 0
    for sarake in range(1, self.sarakkeet):
      for rivi in range(1, self.rivit):
        if self.sana1[rivi-1] == self.sana2[sarake-1]:
          muutos = 0
        else:
          muutos = 1
        
        self.taulu[rivi][sarake] = min(self.taulu[rivi-1][sarake] + 1,
                                   self.taulu[rivi][sarake-1] + 1,
                                   self.taulu[rivi-1][sarake-1] + muutos)

    return self.taulu[rivi][sarake]
  