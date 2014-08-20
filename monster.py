## monster.py This file is used to represent all monster related data and
## functions.

from battlestats import *

class MONSTERS:
  """
  This class is used to represent an enumlike object. All monster data will be
  held here.
  """
  RAT = make_mob(100,25,30,"normal",5,0,0,1,1,"rat",None)
  RED_SLIME = make_mob(5,2,5,"normal",1,2,0,1,1,"red_slime",None)
  NERD = make_mob(20,5,10,"normal",1,0,0,1,1,"nerd",None)




"""
The below dictionaries are the hardcoded data for certain monsters.
"""

def make_mob(health,minimum_damage,maximum_damage,damage_type,
    defence,fire_resistance,ice_resistance,level,rarity_level,name,loot_table):
  return {
    BATTLE_STATS.HEALTH: health,
    BATTLE_STATS.MINIMUM_DAMAGE: minimum_damage,
    BATTLE_STATS.MAXIMUM_DAMAGE: maximum_damage,
    BATTLE_STATS.DAMAGE_Type: damage_type,
    BATTLE_STATS.DEFENCE: defence,
    BATTLE_STATS.FIRE_RESISTANCE: fire_resistance,
    BATTLE_STATS.ICE_RESISTANCE: ice_resistance,
    BATTLE_STATS.LEVEL: level,
    BATTLE_STATS.RARITY_LEVEL: rarity_level,
    BATTLE_STATS.NAME: name,
    BATTLE_STATS.LOOT_TABLE: loot_table
  }