## item_bases.py

from damage_types import *
from item_types import *

"""
  The item base contains all of the base information for each item type.
"""

def getBaseItem(item_type, tier):
  return item_base[item_type][tier]

## The massive set of item bases.
item_base = {

  ## Begin Weapons
  ITEM_TYPE.ONE_HANDED_SWORD: {
    1: {
      'name': 'Wooden Sword',
      'action_point_cost': 40,
      'min_damage': 2,
      'max_damage': 6,
      'auto_attack_damage_type': DAMAGE_TYPE.SLASH,
    },
    2: {
      'name': 'Stone Sword',
      'action_point_cost': 40,
      'min_damage': 3,
      'max_damage': 10,
      'auto_attack_damage_type': DAMAGE_TYPE.SLASH,
    },
    3: {
      'name': 'Iron Sword',
      'action_point_cost': 40,
      'min_damage': 15,
      'max_damage': 20,
      'auto_attack_damage_type': DAMAGE_TYPE.SLASH,
    },
  },
  ## End 1h Swords

  ITEM_TYPE.ONE_HANDED_AXE: {
    1: {
      'name': 'Wooden Axe',
      'action_point_cost': 42,
      'min_damage': 3,
      'max_damage': 5,
      'auto_attack_damage_type': DAMAGE_TYPE.SLASH,
    },
    2: {
      'name': 'Stone Axe',
      'action_point_cost': 42,
      'min_damage': 4,
      'max_damage': 7,
      'auto_attack_damage_type': DAMAGE_TYPE.SLASH,
    },
  },
  ## End 1h Axes

  ITEM_TYPE.ONE_HANDED_MACE: {
    1: {
      'name': 'Club',
      'action_point_cost': 44,
      'min_damage': 4,
      'max_damage': 5,
      'auto_attack_damage_type': DAMAGE_TYPE.CRUSH,
    },
    2: {
      'name': 'Mallet',
      'action_point_cost': 44,
      'min_damage': 5,
      'max_damage': 6,
      'auto_attack_damage_type': DAMAGE_TYPE.CRUSH,
    },
  },
  ## End 1h Maces

  ITEM_TYPE.TWO_HANDED_SWORD: {
    1: {
      'name': 'Dull Longsword',
      'action_point_cost': 45,
      'min_damage': 5,
      'max_damage': 7,
      'auto_attack_damage_type': DAMAGE_TYPE.SLASH,
    },
    2: {
      'name': 'Longsword',
      'action_point_cost': 45,
      'min_damage': 7,
      'max_damage': 11,
      'auto_attack_damage_type': DAMAGE_TYPE.SLASH,
    },
  },
  ## End 2h Sword

  ITEM_TYPE.TWO_HANDED_MACE: {
    1: {
      'name': 'Tree Branch',
      'action_point_cost': 47,
      'min_damage': 6,
      'max_damage': 8,
      'auto_attack_damage_type': DAMAGE_TYPE.CRUSH,
    },
    2: {
      'name': 'Maul',
      'action_point_cost': 47,
      'min_damage': 8,
      'max_damage': 10,
      'auto_attack_damage_type': DAMAGE_TYPE.CRUSH,
    },
  },
  ## End 2h Mace

  ITEM_TYPE.SLING: {
    1: {
      'name': 'Bag of Rocks',
      'action_point_cost': 38,
      'min_damage': 3,
      'max_damage': 4,
      'auto_attack_damage_type': DAMAGE_TYPE.CRUSH,
    },
    2: {
      'name': 'Short Sling',
      'action_point_cost': 38,
      'min_damage': 5,
      'max_damage': 6,
      'auto_attack_damage_type': DAMAGE_TYPE.CRUSH,
    },
    3: {
      'name': 'Leather Sling',
      'action_point_cost': 38,
      'min_damage': 12,
      'max_damage': 13,
      'auto_attack_damage_type': DAMAGE_TYPE.CRUSH,
    },
  },
  ## End 1h Sling

  ITEM_TYPE.BOW: {
    1: {
      'name': 'Shortbow',
      'action_point_cost': 43,
      'min_damage': 4,
      'max_damage': 8,
      'auto_attack_damage_type': DAMAGE_TYPE.THRUST,
    },
    2: {
      'name': 'Recurvebow',
      'action_point_cost': 43,
      'min_damage': 6,
      'max_damage': 12,
      'auto_attack_damage_type': DAMAGE_TYPE.THRUST,
    },
  },
  ## End 2h Bow

  ## Begin Armors
  ITEM_TYPE.LIGHT_HELMET: {
    1: {
      'name': 'Cloth Cap',
      'slash_resist': 2,
      'thrust_resist': 2,
      'crush_resist': 2,
    },
  },
  ## End light helms
}

print getBaseItem(ITEM_TYPE.ONE_HANDED_SWORD, 1)
print getBaseItem(ITEM_TYPE.LIGHT_HELMET, 1)