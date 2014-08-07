## monster.py This file is used to represent all monster related data and
## functions.

from battlestats import *

class MONSTERS:
  """
  This class is used to represent an enumlike object. All monster data will be
  held here.
  """
  RAT = make_mob(5,2,"normal",1,0,0,1,1,"rat",None)
  RED_SLIME = make_mob(5,2,"normal",1,2,0,1,1,"red_slime",None)
  NERD = make_mob(20,5,"normal",1,0,0,1,1,"nerd",None)




"""
The below dictionaries are the hardcoded data for certain monsters.
"""

def make_mob(hp,dmg,dmgt,defence,fr,ir,lvl,rlvl,name,loot_table):
  return {
    BATTLE_STATS.HP: hp,
    BATTLE_STATS.DMG: dmg,
    BATTLE_STATS.DMGT: dmgt,
    BATTLE_STATS.DEF: defence,
    BATTLE_STATS.FR: fr,
    BATTLE_STATS.IR: ir,
    BATTLE_STATS.LVL: lvl,
    BATTLE_STATS.RLVL: rlvl,
    BATTLE_STATS.NAME: name,
    BATTLE_STATS.LT: loot_table
  }