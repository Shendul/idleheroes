## monster.py This file is used to represent all monster related data and
## functions.

from battle import *

class MONSTERS:
  """
  This class is used to represent an enumlike object. All monster data will be
  held here.
  """
  RAT = makeMob(100,0,25,5,5,0,0,0,0,0,0,0,2,5,"Thrust",1,1,"rat",None)



"""
The below dictionaries are the hardcoded data for certain monsters.
"""

def makeMob(health, mana, defense, thrust_resistance, slash_resistance,
  crush_resistance, lightning_resistance, fire_resistance, cold_resistance,
  poison_resistance, minimum_damage, maximum_damage, damage_type, level,
  rarity_level, name, loot_table):
  return {
    ACTOR_STAT.HEALTH: health,
    ACTOR_STAT.MANA: mana,
    ACTOR_STAT.DEFENSE: defense,
    ACTOR_STAT.THRUST_RESISTANCE: thrust_resistance,
    ACTOR_STAT.SLASH_RESISTANCE: slash_resistance,
    ACTOR_STAT.CRUSH_RESISTANCE: crush_resistance,
    ACTOR_STAT.LIGHTNING_RESISTANCE: lightning_resistance,
    ACTOR_STAT.FIRE_RESISTANCE: fire_resistance,
    ACTOR_STAT.COLD_RESISTANCE: cold_resistance,
    ACTOR_STAT.POISON_RESISTANCE: poison_resistance,
    ACTOR_STAT.MINIMUM_DAMAGE: minimum_damage,
    ACTOR_STAT.MAXIMUM_DAMAGE: maximum_damage,
    ACTOR_STAT.DAMAGE_TYPE: damage_type,
    ACTOR_STAT.LEVEL: level,
    ACTOR_STAT.RARITY_LEVEL: rarity_level,
    ACTOR_STAT.NAME: name,
    ACTOR_STAT.LOOT_TABLE: loot_table
  }