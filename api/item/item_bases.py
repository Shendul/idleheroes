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
  ITEM_TYPE.ONE_HANDED_SWORD: {
    1: {
      'name': 'Wooden Sword',
      'action_point_cost': 40,
      'min_damage': 2,
      'max_damage': 6,
      'auto_attack_damage_type': DAMAGE_TYPE.SLASH,
    },
  },
  ## End 1h Swords

  ## Begin Armors
  ITEM_TYPE.LIGHT_HELMET: {
    1: {
      'name': 'Cloth Cap'
    },
  },
}

print getBaseItem(ITEM_TYPE.ONE_HANDED_SWORD, 1)
print getBaseItem(ITEM_TYPE.LIGHT_HELMET, 1)