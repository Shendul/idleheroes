## monster.py This file is used to represent all monster related data and
## functions.

from battlestats import *

"""
The below dictionaries are the hardcoded data for certain monsters.
"""

def make_mob(hp,dmg,defence,fr,ir,lvl,rlvl,name,loot_table):
  return {
    BATTLE_STATS.HP: hp,
    BATTLE_STATS.DMG: dmg,
    BATTLE_STATS.DEF: defence,
    BATTLE_STATS.FR: fr,
    BATTLE_STATS.IR: ir,
    BATTLE_STATS.LVL: lvl,
    BATTLE_STATS.RLVL: rlvl,
    BATTLE_STATS.NAME: name,
    BATTLE_STATS.LT: loot_table
  }