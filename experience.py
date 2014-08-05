hero_levels = [0, # 1
  500, # 2
  1100, # 3
  1800, # 4
  2550, # 5
  3500, # 6
  5000, # 7
  7000, # 8
  9500, # 9
  12000, # 10
  17000, # 11
  23000, # 12
  32500] # 13

def getHeroLevel(experience):
  """
  Determines the hero level given the experience points of that hero.
  """
  i = 0
  while hero_levels[i] <= experience:
    i += 1
  return i
