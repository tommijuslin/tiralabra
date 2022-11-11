class Levenshtein:
  def __init__(self):
    self.sana1 = ""
    self.sana2 = ""
    self.rivit = 0
    self.sarakkeet = 0
    self.taulu = []
  
  def etaisyys(self, sana1, sana2):
    self.sana1 = sana1
    self.sana2 = sana2
    self.rivit = len(sana1) + 1
    self.sarakkeet = len(sana2) + 1
    self.alusta_taulu()

    return self.laske_etaisyys()
  
  def alusta_taulu(self):
    del self.taulu[:]

    self.taulu = [[0 for sarake in range(self.sarakkeet)] for rivi in range(self.rivit)]

    for rivi in range(1, self.rivit):
      self.taulu[rivi][0] = rivi
  
    for sarake in range(1, self.sarakkeet):
      self.taulu[0][sarake] = sarake

  def laske_etaisyys(self):
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
  