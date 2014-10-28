## starting_items.py
from model import ItemModel

from weapon_bases import *
from item_rarities import *
from item_types import *

ItemModel = ItemModel.ItemModel

def createStartingWeapon(item_type):
  """ Creates a starting weapon of the given type. """
  weapon = ItemModel()
  weapon.item_type = item_type
  weapon.item_rarity = item_rarities.COMMON

  weapon_base = getBaseWeapon(item_type, 1)
  weapon.item_name = weapon_base[name]
  weapon.action_point_cost = weapon_base[action_point_cost]
  weapon.min_damage = weapon_base[min_damage]
  weapon.max_damage = weapon_base[max_damage]
  weapon.auto_attack_damage_type = weapon[auto_attack_damage_type]
  weapon.item_level = 1

  return weapon.put()