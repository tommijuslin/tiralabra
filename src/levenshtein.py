def levenshtein(sana1, sana2):
  rivit = len(sana1) + 1
  sarakkeet = len(sana2) + 1

  taulu = [[0 for sarake in range(sarakkeet)] for rivi in range(rivit)]

  for rivi in range(1, rivit):
    taulu[rivi][0] = rivi
  
  for sarake in range(1, sarakkeet):
    taulu[0][sarake] = sarake

  muutos = 0
  for sarake in range(1, sarakkeet):
    for rivi in range(1, rivit):
      if sana1[rivi-1] == sana2[sarake-1]:
        muutos = 0
      else:
        muutos = 1
      
      taulu[rivi][sarake] = min(taulu[rivi-1][sarake] + 1,
                                taulu[rivi][sarake-1] + 1,
                                taulu[rivi-1][sarake-1] + muutos)

  return taulu[rivi][sarake]
  