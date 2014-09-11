## affixes.py
## This file represents all of the data associated with affixes.

from items import *
import random
import math

class AFFIX:
  """
  This class maps the base affix type to a character that will be used in the
  item string.
  Uncomment each affix after implementation for the affix is completed.
  The section comments are basic seperators. When implementing each affix,
  decisions will need to be made regarding which affixes can be used on which
  items.
  NEXT AVAILABLE CHAR: 'c'
  """
  ## Attributes
  HEALTH = 'A'
  # MANA = 'B' ## TODO: Implement Mana
  STRENGTH = 'C'
  # AGILITY = 'D'
  # WISDOM = 'E'
  # CONSTITUTION = 'F'

  ## Armor Specific
  DEFENSE = 'G'
  # DEFENSE_PERCENTAGE = 'b'
  # PHYSICAL_RESISTANCE = 'H'
  # ELEMENTAL_RESISTANCE = 'I'
  # THRUST_RESISTANCE = 'J'
  # SLASH_RESISTANCE = 'K'
  # CRUSH_RESISTANCE = 'L'
  # LIGHTNING_RESISTANCE = 'M'
  # FIRE_RESISTANCE = 'N'
  # COLD_RESISTANCE = 'O'
  # POISON_RESISTANCE = 'P'
  # THORNS = 'a' ## Returns damage to melee attackers.

  ## Weapon Specific
  WEAPON_DAMAGE_PERCENTAGE = 'Q'
  WEAPON_DAMAGE_FLAT = 'R'
  # LIGHTNING_DAMAGE = 'S'
  # FIRE_DAMAGE = 'T'
  # COLD_DAMAGE = 'U'
  # POISON_DAMAGE = 'V'
  ## TODO: insert monster slaying damage boosts.

  ## Accessory Specific
  # GOLD_FIND = 'W'
  # MAGIC_FIND = 'X'
  # EXP_GAIN = 'Y'

  ## Other
  # REDUCED_REQUIREMENTS = 'Z'

## Specifies whether or not the affix has a range value, or has a fixed value.
AFFIX_HAS_VALUE_RANGE = {
  ## Attributes
  # AFFIX.HEALTH: False,
  # AFFIX.MANA: False,
  # AFFIX.STRENGTH: False,
  # AFFIX.AGILITY: False,
  # AFFIX.WISDOM: False,
  # AFFIX.CONSTITUTION: False,

  ## Armor Specific
  # AFFIX.DEFENSE: False,
  # AFFIX.DEFENSE_PERCENTAGE: False,
  # AFFIX.PHYSICAL_RESISTANCE: False,
  # AFFIX.ELEMENTAL_RESISTANCE: False,
  # AFFIX.THRUST_RESISTANCE: False,
  # AFFIX.SLASH_RESISTANCE: False,
  # AFFIX.CRUSH_RESISTANCE: False,
  # AFFIX.LIGHTNING_RESISTANCE: False,
  # AFFIX.FIRE_RESISTANCE: False,
  # AFFIX.COLD_RESISTANCE: False,
  # AFFIX.POISON_RESISTANCE: False,
  # AFFIX.THORNS: True,

  ## Weapon Specific
  # AFFIX.WEAPON_DAMAGE_PERCENTAGE: False,
  # AFFIX.WEAPON_DAMAGE_FLAT: True,
  # AFFIX.LIGHTNING_DAMAGE: True,
  # AFFIX.FIRE_DAMAGE: True,
  # AFFIX.COLD_DAMAGE: True,
  # AFFIX.POISON_DAMAGE: True,

  ## Accessory Specific
  # AFFIX.GOLD_FIND: False,
  # AFFIX.MAGIC_FIND: False,
  # AFFIX.EXP_GAIN: False,  

  ## Other
  # AFFIX.REDUCED_REQUIREMENTS: False
  
PREFIX_DISPLAY_NAME = {
  ## TODO: Make different grades of names later.
  ## Attributes
  # AFFIX.HEALTH: 'Burly',
  # AFFIX.MANA: 'Mystic',
  # AFFIX.STRENGTH: 'Heavy',
  # AFFIX.AGILITY: 'Swift',
  # AFFIX.WISDOM: 'Ancient',
  # AFFIX.CONSTITUTION: 'Manly',

  ## Armor Specific
  # AFFIX.DEFENSE: 'Stalwart',
  # AFFIX.DEFENSE_PERCENTAGE: 'Vanguard'\s',
  # AFFIX.PHYSICAL_RESISTANCE: 'Reinforced',
  # AFFIX.ELEMENTAL_RESISTANCE: 'Weathered',
  # AFFIX.THRUST_RESISTANCE: 'Shelled',
  # AFFIX.SLASH_RESISTANCE: 'Hardened',
  # AFFIX.CRUSH_RESISTANCE: 'Padded',
  # AFFIX.LIGHTNING_RESISTANCE: 'Rubber',
  # AFFIX.FIRE_RESISTANCE: 'Flame Retardant',
  # AFFIX.COLD_RESISTANCE: 'Heated',
  # AFFIX.POISON_RESISTANCE: 'Alchemist'\s',
  # AFFIX.THORNS: 'Spiny',

  ## Weapon Specific
  # AFFIX.WEAPON_DAMAGE_PERCENTAGE: 'Precise',
  # AFFIX.WEAPON_DAMAGE_FLAT: 'Deadly',
  # AFFIX.LIGHTNING_DAMAGE: 'Conductive',
  # AFFIX.FIRE_DAMAGE: 'Fiery',
  # AFFIX.COLD_DAMAGE: 'Frozen',
  # AFFIX.POISON_DAMAGE: 'Poisoned',

  ## Accessory Specific
  # AFFIX.GOLD_FIND: 'Rich',
  # AFFIX.MAGIC_FIND: 'Lucky',
  # AFFIX.EXP_GAIN: 'Practice',

  ## Other
  # AFFIX.REDUCED_REQUIREMENTS: 'Simple'
}

SUFFIX_DISPLAY_NAME = {
  ## TODO: Make different grades of names later.
  ## Attributes
  # AFFIX.HEALTH: 'of Life',
  # AFFIX.MANA: 'of Energy',
  # AFFIX.STRENGTH: 'of the Hulk',
  # AFFIX.AGILITY: 'of the Wind',
  # AFFIX.WISDOM: 'of Wisdom',
  # AFFIX.CONSTITUTION: 'of the Bear',

  ## Armor Specific
  # AFFIX.DEFENSE: 'of Endurance',
  # AFFIX.DEFENSE_PERCENTAGE: 'of Protection',
  # AFFIX.PHYSICAL_RESISTANCE: 'of the Turtle',
  # AFFIX.ELEMENTAL_RESISTANCE: 'of Survival',
  # AFFIX.THRUST_RESISTANCE: 'of the Drake',
  # AFFIX.SLASH_RESISTANCE: 'of the Tree',
  # AFFIX.CRUSH_RESISTANCE: 'of Stone',
  # AFFIX.LIGHTNING_RESISTANCE: 'of the Earth',
  # AFFIX.FIRE_RESISTANCE: 'of the Firefighter',
  # AFFIX.COLD_RESISTANCE: 'of the Viking',
  # AFFIX.POISON_RESISTANCE: 'of Immunity',
  # AFFIX.THORNS: 'of the Porcupine',

  ## Weapon Specific
  # AFFIX.WEAPON_DAMAGE_PERCENTAGE: 'of Mutilation',
  # AFFIX.WEAPON_DAMAGE_FLAT: 'of Slaying',
  # AFFIX.LIGHTNING_DAMAGE: 'of Shocking',
  # AFFIX.FIRE_DAMAGE: 'of Flames',
  # AFFIX.COLD_DAMAGE: 'of the North',
  # AFFIX.POISON_DAMAGE: 'of the Viper',

  ## Accessory Specific
  # AFFIX.GOLD_FIND: 'of the Wealthy',
  # AFFIX.MAGIC_FIND: 'of Tracking',
  # AFFIX.EXP_GAIN: 'of Instructing',

  ## Other
  # AFFIX.REDUCED_REQUIREMENTS: 'of the Cadet'
}

ITEM_AFFIX_CLASS = {
  ##TODO: Consider differentiating between light and heavy armor for affixes.
  ITEM.TUNIC: 'body_armor',
  ITEM.PANTS: 'body_armor',
  ITEM.MANTEL: 'body_armor',
  ITEM.CHESTPLATE: 'body_armor',
  ITEM.FAULDS: 'body_armor',
  ITEM.PAULDRONS: 'body_armor',
  ITEM.GREAVES: 'body_armor',
  ITEM.BOOTS: 'body_armor',
   
  ITEM.HAT: 'helmets',
  ITEM.HELMET: 'helmets',
  
  ITEM.GLOVES: 'gloves',
  ITEM.GUANTLETS: 'gloves',

  ITEM.RING: 'accessories',
  ITEM.AMULET: 'accessories',
  ITEM.EARRING: 'accessories',

  ITEM.ONE_HANDED_SWORD: 'one_handed_melee_weapons',
  ITEM.ONE_HANDED_AXE: 'one_handed_melee_weapons',
  ITEM.ONE_HANDED_MACE: 'one_handed_melee_weapons',
  # ITEM.CLAW: 'one_handed_melee_weapons',

  ITEM.SHIELD: 'shields',
  # ITEM.ORB: 'orbs',

  ITEM.TWO_HANDED_SWORD: 'two_handed_melee_weapons',
  ITEM.TWO_HANDED_MACE: 'two_handed_melee_weapons',
  ITEM.QUARTERSTAFF: 'two_handed_melee_weapons',
  ITEM.POLEARM: 'two_handed_melee_weapons',
  ITEM.SPEAR: 'two_handed_melee_weapons',

  ITEM.SLING: 'one_handed_ranged_weapons',
  # ITEM.JAVELIN: 'one_handed_ranged_weapons',
  # ITEM.WAND: 'one_handed_ranged_weapons', 

  ITEM.BOW: 'two_handed_ranged_weapons',
  #ITEM.CROSSBOW: 'two_handed_ranged_weapons'
}


def item_affix_grade(
    prefix_name, suffix_name, item_level, minValueRange, maxValue):
  return {
    'prefix_name': prefix_name,
    'suffix_name': suffix_name,
    'item_level': item_level,
    'minValueRange': minValueRange, 
    'maxValue': maxValue # None, unless the affix is a damage affix.
  }

## Sadly, this is going to be a huge unreadable mess of data.
AFFIX_ROLL_RANGE_SETS = {
  ## TODO: Balance these
  'body_armor': {
    AFFIX.HEALTH: [                                         # BODY ARMOR SECTION
      item_affix_grade('Burly', 'of Life', 1, (5, 10), None), # Grade 0
      item_affix_grade('Burly', 'of Life', 8, (10, 25), None) # Grade 1
    ],
#     AFFIX.MANA: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.STRENGTH: [
      item_affix_grade('Heavy', 'of the Hulk', 1, (2, 8), None), # Grade 0
      item_affix_grade('Heavy', 'of the Hulk', 6, (7, 16), None) # Grade 1
    ],
#     AFFIX.AGILITY: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WISDOM: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CONSTITUTION: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.DEFENSE: [
      item_affix_grade('Stalwart', 'of Endurance', 1, (10, 25), None), # Grade 0
      item_affix_grade('Stalwart', 'of Endurance', 6, (25, 50), None) # Grade 1
    ],
#     AFFIX.DEFENSE_PERCENTAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.PHYSICAL_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.ELEMENTAL_RESISTANCE: [                    # BODY ARMOR SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THRUST_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.SLASH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CRUSH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.LIGHTNING_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THORNS: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.GOLD_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.MAGIC_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.EXP_GAIN: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.REDUCED_REQUIREMENTS: [                    # BODY ARMOR SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ]

  }, ## END 'body_armor'

  'helmets': {
    AFFIX.HEALTH: [                    # HELMET SECTION
      item_affix_grade('Burly', 'of Life', 1, (2, 6), None), # Grade 0
      item_affix_grade('Burly', 'of Life', 8, (6, 15), None) # Grade 1
    ],
#     AFFIX.MANA: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.STRENGTH: [
      item_affix_grade('Heavy', 'of the Hulk', 1, (1, 5), None), # Grade 0
      item_affix_grade('Heavy', 'of the Hulk', 6, (4, 10), None) # Grade 1
    ],
#     AFFIX.AGILITY: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WISDOM: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CONSTITUTION: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.DEFENSE: [
      item_affix_grade('Stalwart', 'of Endurance', 1, (10, 25), None), # Grade 0
      item_affix_grade('Stalwart', 'of Endurance', 6, (25, 50), None) # Grade 1
    ],
#     AFFIX.DEFENSE_PERCENTAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.PHYSICAL_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.ELEMENTAL_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THRUST_RESISTANCE: [                    # HELMET SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.SLASH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CRUSH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.LIGHTNING_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THORNS: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.GOLD_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.MAGIC_FIND: [                    # HELMET SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.EXP_GAIN: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.REDUCED_REQUIREMENTS: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ]

  }, ## END 'helmets'

  'gloves': {
    AFFIX.HEALTH: [                    # GLOVES SECTION
      item_affix_grade('Burly', 'of Life', 1, (2, 6), None), # Grade 0
      item_affix_grade('Burly', 'of Life', 8, (6, 15), None) # Grade 1
    ],
#     AFFIX.MANA: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.STRENGTH: [
      item_affix_grade('Heavy', 'of the Hulk', 1, (1, 5), None), # Grade 0
      item_affix_grade('Heavy', 'of the Hulk', 6, (4, 10), None) # Grade 1
    ],
#     AFFIX.AGILITY: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WISDOM: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CONSTITUTION: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.DEFENSE: [
      item_affix_grade('Stalwart', 'of Endurance', 1, (10, 25), None), # Grade 0
      item_affix_grade('Stalwart', 'of Endurance', 6, (25, 50), None) # Grade 1
    ],
#     AFFIX.DEFENSE_PERCENTAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.PHYSICAL_RESISTANCE: [                    # GLOVES SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.ELEMENTAL_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THRUST_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.SLASH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CRUSH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.LIGHTNING_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_RESISTANCE: [                    # GLOVES SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THORNS: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.GOLD_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.MAGIC_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.EXP_GAIN: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.REDUCED_REQUIREMENTS: [                    # GLOVES SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ]

  }, ## END 'gloves'

  'accessories': {
    AFFIX.HEALTH: [                    # ACCESSORIES SECTION
      item_affix_grade('Burly', 'of Life', 1, (5, 12), None), # Grade 0
      item_affix_grade('Burly', 'of Life', 8, (10, 30), None) # Grade 1
    ],
#     AFFIX.MANA: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.STRENGTH: [
      item_affix_grade('Heavy', 'of the Hulk', 1, (2, 7), None), # Grade 0
      item_affix_grade('Heavy', 'of the Hulk', 6, (6, 16), None) # Grade 1
    ],
#     AFFIX.AGILITY: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WISDOM: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CONSTITUTION: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.DEFENSE: [
      item_affix_grade('Stalwart', 'of Endurance', 1, (10, 25), None), # Grade 0
      item_affix_grade('Stalwart', 'of Endurance', 6, (25, 50), None) # Grade 1
    ],
#     AFFIX.DEFENSE_PERCENTAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.PHYSICAL_RESISTANCE: [                  # ACCESSORIES SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.ELEMENTAL_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THRUST_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.SLASH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CRUSH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.LIGHTNING_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_RESISTANCE: [                  # ACCESSORIES SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THORNS: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WEAPON_DAMAGE_FLAT: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.LIGHTNING_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.GOLD_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.MAGIC_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.EXP_GAIN: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.REDUCED_REQUIREMENTS: [                  # ACCESSORIES SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ]

  }, ## END 'accessories'

  'one_handed_melee_weapons': {
    AFFIX.HEALTH: [                                   # ONE HANDED MELEE SECTION
      item_affix_grade('Burly', 'of Life', 1, (2, 6), None), # Grade 0
      item_affix_grade('Burly', 'of Life', 8, (6, 15), None) # Grade 1
    ],
#     AFFIX.MANA: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.STRENGTH: [
      item_affix_grade('Heavy', 'of the Hulk', 1, (2, 7), None), # Grade 0
      item_affix_grade('Heavy', 'of the Hulk', 6, (6, 16), None) # Grade 1
    ],
#     AFFIX.AGILITY: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WISDOM: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CONSTITUTION: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
      item_affix_grade('Precise', 'of Mutilation', 3, (5, 20), None), # Grade 0
      item_affix_grade('Precise', 'of Mutilation', 9, (20, 50), None) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_FLAT: [
      item_affix_grade('Deadly', 'of Slaying', 1, (1, 4), 8), # Grade 0
      item_affix_grade('Deadly', 'of Slaying', 6, (3, 6), 12) # Grade 1
    ],
#     AFFIX.LIGHTNING_DAMAGE: [              # ONE HANDED MELEE SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.GOLD_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.MAGIC_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.EXP_GAIN: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.REDUCED_REQUIREMENTS: [                  # ONE HANDED MELEE SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ]
#     ## TODO: Add all affixes that make sense for 1h melee

  }, ## END 'one_handed_melee_weapons'

  'shields': {
    AFFIX.HEALTH: [                                         # SHIELDS SECTION
      item_affix_grade('Burly', 'of Life', 1, (5, 10), None), # Grade 0
      item_affix_grade('Burly', 'of Life', 8, (10, 25), None) # Grade 1
    ],
#     AFFIX.MANA: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.STRENGTH: [
      item_affix_grade('Heavy', 'of the Hulk', 1, (2, 8), None), # Grade 0
      item_affix_grade('Heavy', 'of the Hulk', 6, (7, 16), None) # Grade 1
    ],
#     AFFIX.AGILITY: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WISDOM: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CONSTITUTION: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.DEFENSE: [
      item_affix_grade('Stalwart', 'of Endurance', 1, (10, 25), None), # Grade 0
      item_affix_grade('Stalwart', 'of Endurance', 6, (25, 50), None) # Grade 1
    ],
#     AFFIX.DEFENSE_PERCENTAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.PHYSICAL_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.ELEMENTAL_RESISTANCE: [                    # SHIELDS SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THRUST_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.SLASH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CRUSH_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.LIGHTNING_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_RESISTANCE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.THORNS: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.GOLD_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.MAGIC_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.EXP_GAIN: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.REDUCED_REQUIREMENTS: [                    # SHIELDS SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ]

  }, ## END 'shields'

#   'orbs': {
#     ## TODO: Add all affixes that make sense for orbs

#   }, ## END 'orbs'

  'two_handed_melee_weapons': {
    AFFIX.HEALTH: [                                   # TWO HANDED MELEE SECTION
      item_affix_grade('Burly', 'of Life', 1, (4, 12), None), # Grade 0
      item_affix_grade('Burly', 'of Life', 8, (12, 30), None) # Grade 1
    ],
#     AFFIX.MANA: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.STRENGTH: [
      item_affix_grade('Heavy', 'of the Hulk', 1, (4, 14), None), # Grade 0
      item_affix_grade('Heavy', 'of the Hulk', 6, (12, 32), None) # Grade 1
    ],
#     AFFIX.AGILITY: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WISDOM: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CONSTITUTION: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
      item_affix_grade('Precise', 'of Mutilation', 3, (7, 30), None), # Grade 0
      item_affix_grade('Precise', 'of Mutilation', 9, (30, 75), None) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_FLAT: [
      item_affix_grade('Deadly', 'of Slaying', 1, (2, 8), 16), # Grade 0
      item_affix_grade('Deadly', 'of Slaying', 6, (6, 12), 24) # Grade 1
    ],
#     AFFIX.LIGHTNING_DAMAGE: [                  # TWO HANDED MELEE SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.GOLD_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.MAGIC_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.EXP_GAIN: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.REDUCED_REQUIREMENTS: [                  # TWO HANDED MELEE SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ]

  }, ## END 'two_handed_melee_weapons'

  'one_handed_ranged_weapons': {
    AFFIX.HEALTH: [                                  # ONE HANDED RANGED SECTION
      item_affix_grade('Burly', 'of Life', 1, (2, 6), None), # Grade 0
      item_affix_grade('Burly', 'of Life', 8, (6, 15), None) # Grade 1
    ],
#     AFFIX.MANA: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.STRENGTH: [
      item_affix_grade('Heavy', 'of the Hulk', 1, (2, 7), None), # Grade 0
      item_affix_grade('Heavy', 'of the Hulk', 6, (6, 16), None) # Grade 1
    ],
#     AFFIX.AGILITY: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WISDOM: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CONSTITUTION: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
      item_affix_grade('Precise', 'of Mutilation', 3, (5, 20), None), # Grade 0
      item_affix_grade('Precise', 'of Mutilation', 9, (20, 50), None) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_FLAT: [
      item_affix_grade('Deadly', 'of Slaying', 1, (1, 4), 8), # Grade 0
      item_affix_grade('Deadly', 'of Slaying', 6, (3, 6), 12) # Grade 1
    ],
#     AFFIX.LIGHTNING_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.GOLD_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.MAGIC_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.EXP_GAIN: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.REDUCED_REQUIREMENTS: [                  # ONE HANDED RANGED SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ]
#     ## TODO: Add all affixes that make sense for 1h ranged

  }, ## END 'one_handed_ranged_weapons'

  'two_handed_ranged_weapons': {
    AFFIX.HEALTH: [                                  # TWO HANDED RANGED SECTION
      item_affix_grade('Burly', 'of Life', 1, (4, 12), None), # Grade 0
      item_affix_grade('Burly', 'of Life', 8, (12, 30), None) # Grade 1
    ],
#     AFFIX.MANA: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.STRENGTH: [
      item_affix_grade('Heavy', 'of the Hulk', 1, (4, 14), None), # Grade 0
      item_affix_grade('Heavy', 'of the Hulk', 6, (12, 32), None) # Grade 1
    ],
#     AFFIX.AGILITY: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.WISDOM: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.CONSTITUTION: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
    AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
      item_affix_grade('Precise', 'of Mutilation', 3, (7, 30), None), # Grade 0
      item_affix_grade('Precise', 'of Mutilation', 9, (30, 75), None) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_FLAT: [
      item_affix_grade('Deadly', 'of Slaying', 1, (2, 8), 16), # Grade 0
      item_affix_grade('Deadly', 'of Slaying', 6, (6, 12), 24) # Grade 1
    ],
#     AFFIX.LIGHTNING_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.FIRE_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.COLD_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.POISON_DAMAGE: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.GOLD_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.MAGIC_FIND: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.EXP_GAIN: [
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ],
#     AFFIX.REDUCED_REQUIREMENTS: [                  # TWO HANDED RANGED SECTION
#       (, ), # Grade 0
#       (, ) # Grade 1
#     ]
#     ## TODO: Add all affixes that make sense for 2h ranged

  }, ## END 'two_handed_ranged_weapons'

}

def rollForAffix():
  ## We use a power law here for the roll.
  ## Rather than a uniform distribution, high rolls are much harder to get.
  ## Increasing the power here decreases the strength of rolls.
  ## Example: if random() returns a .750000 (a highish roll) a power of 3
  ## reduces this roll to a .421875.
  ## Current rough distribution: 
  ##   0-.25: 63%
  ##   .25-.50: 16%
  ##   .50-.75: 11%
  ##   .75-.100: 9% (.95-.100: 1.7%)
  ## This means roughly 79% of rolls will be less than half of the possible
  ##     value on affixes, and only about 1 in 50 rolls will max an affix.
  ## This will make perfect items extremely rare, and therefore we can make them
  ##     extremely powerful.
  ## If we increase from a power of three, we make lower rolls more common, and
  ##    higher rolls more rare.
  return math.pow(random.random(), 3)

# Use this helper function if you want to test a change the roll distribution.
def testAffixRollDistribution():
  counts = {
    '0-25': 0,
    '25-50': 0,
    '50-75': 0,
    '75-85': 0,
    '85-90': 0,
    '90-95': 0,
    '95-100': 0,
  }
  for i in xrange(100000):
    num = rollForAffix()
    if num <= .25:
      counts['0-25'] += 1
    elif num <= .50:
      counts['25-50'] += 1
    elif num <= .75:
      counts['50-75'] += 1
    elif num <= .85:
      counts['75-85'] += 1
    elif num <= .90:
      counts['85-90'] += 1
    elif num <= .95:
      counts['90-95'] += 1
    else:
      counts['95-100'] += 1

  print counts['0-25']
  print counts['25-50']
  print counts['50-75']
  print counts['75-85']
  print counts['85-90']
  print counts['90-95']
  print counts['95-100']
# testAffixRollDistribution()

## TODO: determine difference between prefixes and suffixes.
def generateAffix(item_level, base_item):
  """
  This function is used to generate an affix based on item level.
  It returns a string representation of the affix
  """
  if item_level < 1:
    print 'error generating affix, item level must be greater than 0'
    return None
  result = {}
  # Get the item affix class for this item
  item_affix_class_key = ITEM_AFFIX_CLASS[base_item]
  item_affix_class = AFFIX_ROLL_RANGE_SETS[item_affix_class_key]
  ## Get the affix and grade.
  while True:
    affix = random.choice(list(item_affix_class.keys()))
    possible_grades = []
    for affix_grade in item_affix_class[affix]:
      if item_level >= affix_grade['item_level']:
        possible_grades.append(affix_grade)
    if len(possible_grades) > 0:
      result = affix # Set the first char of the string.
      break;
    else:
      continue
  
  ## pick the grade
  item_affix_grade = random.choice(possible_grades)

  ## Roll for values
  roll = rollForAffix()
  minRoll, maxRoll = item_affix_grade['minValueRange']
  # Two-Point form equation maps the rolled number to the affix value range.
  # We round the result to the nearest whole number.
  value = int(round((roll-0.0)*(maxRoll-minRoll) + minRoll, 0))
  if item_affix_grade['maxValue'] != None:
    # Roll the max
    roll = rollForAffix()
    minRoll = value + 1
    maxRoll = item_affix_grade['maxValue']
    maxValue = int(round((roll-0.0)*(maxRoll-minRoll) + minRoll, 0))
    result += format(value, "03d") + format(maxValue, "03d")
    return result
  else :
    result += format(value, "06d")
    return result  