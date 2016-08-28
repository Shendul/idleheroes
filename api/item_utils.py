## item_utils.py
from constants import *
from model.item_model import *

def createBaseItem(item_type, grade, quality, slot):
  item = ItemModel(
      item_slot = slot,
      item_type = item_type,
      grade = grade,
      quality = quality)
  base_stats = base_items_map[item_type,grade]
  if item_type in WEAPON_ITEM_TYPES:
    item.power = base_stats[POWER]
  elif item_type in ARMOR_ITEM_TYPES:
    item.resist_list = []
    for resist_type in RESIST_TYPE_LIST:
      resist = ResistModel(
          resist_type = resist_type,
          resist_amount = base_stats[resist_type])
      item.resist_list.append(resist)
  if item_type is SHIELD:
    item.block_chance = base_stats[BLOCK_CHANCE]
  return item

""" A map used for creating new items in the database.
    The key is a pair of integers (type, grade) found in constants.py.
    The value is a map of attribute enums to their values.
"""
base_items_map = {
  ## WEAPON BASES ##
  (TWO_HANDED_SWORD, COPPER): {
    WEAPON_POWER: 6
  },
  ## ARMOR BASES ###
  # LEATHER
  (HELMET, LEATHER): {
    THRUST_RESIST: 2,
    CRUSH_RESIST: 2,
    SLASH_RESIST: 2,
    FIRE_RESIST: 2,
    ICE_RESIST: 2,
    LIGHTING_RESIST: 2,
    POISON_RESIST: 0,
    DODGE_CHANCE_BONUS: 1
  },
  (BOOTS, LEATHER): {
    THRUST_RESIST: 2,
    CRUSH_RESIST: 1,
    SLASH_RESIST: 2,
    FIRE_RESIST: 1,
    ICE_RESIST: 1,
    LIGHTING_RESIST: 3,
    POISON_RESIST: 0,
    DODGE_CHANCE_BONUS: 2
  },
  (GLOVES, LEATHER): {
    THRUST_RESIST: 2,
    CRUSH_RESIST: 1,
    SLASH_RESIST: 3,
    FIRE_RESIST: 3,
    ICE_RESIST: 3,
    LIGHTING_RESIST: 1,
    POISON_RESIST: 0,
    DODGE_CHANCE_BONUS: 1
  },
  (CHESTPIECE, LEATHER): {
    THRUST_RESIST: 1,
    CRUSH_RESIST: 2,
    SLASH_RESIST: 3,
    FIRE_RESIST: 2,
    ICE_RESIST: 2,
    LIGHTING_RESIST: 2,
    POISON_RESIST: 0,
    DODGE_CHANCE_BONUS: 2
  },
  (LEGGINGS, LEATHER): {
    THRUST_RESIST: 2,
    CRUSH_RESIST: 2,
    SLASH_RESIST: 2,
    FIRE_RESIST: 2,
    ICE_RESIST: 2,
    LIGHTING_RESIST: 2,
    POISON_RESIST: 0,
    DODGE_CHANCE_BONUS: 1
  }
}

createBaseItem(LEGGINGS, LEATHER, 100, LEGS)
