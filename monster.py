## monster.py This file is used to represent all monster related data and
## functions.

from battlestats import *

class MONSTERS:
  """
  This class is used to represent an enumlike object. All monster data will be
  held here.
  """
  RAT = makeMob(100,0,25,5,5,0,0,0,0,0,0,0,2,5,"Thrust",1,1,"rat",None)



"""
The below dictionaries are the hardcoded data for certain monsters.
"""

def makeMob(health, mana, defense, physical_resistance, elemental_resistance,
  thrust_resistance, slash_resistance, crush_resistance, lightning_resistance,
  fire_resistance, cold_resistance, poison_resistance, minimum_damage,
  maximum_damage, damage_type, level, rarity_level, name, loot_table):
  return {
    BATTLESTATS.HEALTH: health,
    BATTLESTATS.MANA: mana,
    BATTLESTATS.DEFENSE: defense,
    BATTLESTATS.PHYSICAL_RESISTANCE: physical_resistance,
    BATTLESTATS.ELEMENTAL_RESISTANCE: elemental_resistance,
    BATTLESTATS.THRUST_RESISTANCE: thrust_resistance,
    BATTLESTATS.SLASH_RESISTANCE: slash_resistance,
    BATTLESTATS.CRUSH_RESISTANCE: crush_resistance,
    BATTLESTATS.LIGHTNING_RESISTANCE: lightning_resistance,
    BATTLESTATS.FIRE_RESISTANCE: fire_resistance,
    BATTLESTATS.COLD_RESISTANCE: cold_resistance,
    BATTLESTATS.POISON_RESISTANCE: poison_resistance,
    BATTLESTATS.MINIMUM_DAMAGE: minimum_damage,
    BATTLESTATS.MAXIMUM_DAMAGE: maximum_damage,
    BATTLESTATS.DAMAGE_TYPE: damage_type,
    BATTLESTATS.LEVEL: level,
    BATTLESTATS.RARITY_LEVEL: rarity_level,
    BATTLESTATS.NAME: name,
    BATTLESTATS.LOOT_TABLE: loot_table
  }