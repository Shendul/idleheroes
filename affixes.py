## affixes.py
## This file represents all of the data associated with affixes.

from items import *

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
  # HEALTH = 'A'
  # MANA = 'B' ## TODO: Implement Mana
  # STRENGTH = 'C'
  # AGILITY = 'D'
  # WISDOM = 'E'
  # CONSTITUTION = 'F'

  ## Armor Specific
  # DEFENSE = 'G'
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
  # WEAPON_DAMAGE_PERCENTAGE = 'Q'
  # WEAPON_DAMAGE_FLAT = 'R'
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
}

## Ranges of possible rolls for affixes, for given item types.
## Each grade of affix for each item type has a min range and a max range,
##   or if the value is not a range each grade will simply have a single
##   range of possible values.
## The lowest number of the max range must be >= highest number of min range.
class ITEM_AFFIX_CLASS:
  ##TODO: Consider differentiating between light and heavy armor for affixes.
  BODY_ARMOR = [
    ITEM.TUNIC, ITEM.PANTS, ITEM.MANTEL, ITEM.CHESTPLATE, ITEM.FAULDS,
    ITEM.PAULDRONS, ITEM.GREAVES, ITEM.BOOTS
  ]
  HELMETS = [ITEM.HAT, ITEM.HELMET]
  GLOVES = [ITEM.GLOVES, ITEM.GUANTLETS]
  ACCESSORIES = [ITEM.RING, ITEM.AMULET, ITEM.EARRING]
  ONE_HANDED_MELEE_WEAPONS = [
    ITEM.ONE_HANDED_SWORD, ITEM.ONE_HANDED_AXE, ITEM.ONE_HANDED_MACE, ITEM.CLAW
  ]
  SHIELDS = [ITEM.SHIELD]
  ORBS = [ITEM.ORB]
  TWO_HANDED_MELEE_WEAPONS = [
    ITEM.TWO_HANDED_SWORD, ITEM.TWO_HANDED_MACE, ITEM.QUARTERSTAFF,
    ITEM.POLEARM, ITEM.SPEAR
  ]
  ONE_HANDED_RANGED_WEAPONS = [
    ITEM.SLING, ITEM.JAVELIN, ITEM.WAND
  ]
  TWO_HANDED_RANGED_WEAPONS = [
    ITEM.BOW, ITEM.CROSSBOW
  ]

## Sadly, this is going to be a huge unreadable mess of data.
PREFIX_ROLL_RANGE_SETS = {
  ## TODO: Balance these
  'body_armor': {
    AFFIX.HEALTH: [                    # BODY ARMOR SECTION
      (5, 10), # Grade 0
      (10, 25) # Grade 1
    ],
    AFFIX.MANA: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.STRENGTH: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.AGILITY: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WISDOM: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CONSTITUTION: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.DEFENSE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.DEFENSE_PERCENTAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.PHYSICAL_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.ELEMENTAL_RESISTANCE: [                    # BODY ARMOR SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.THRUST_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.SLASH_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CRUSH_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.LIGHTNING_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.FIRE_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.COLD_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.POISON_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.THORNS: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.GOLD_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.MAGIC_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.EXP_GAIN: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.REDUCED_REQUIREMENTS: [                    # BODY ARMOR SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ]

  }, ## END 'body_armor'

  'helmets': {
    AFFIX.HEALTH: [                    # HELMET SECTION
      (2, 6), # Grade 0
      (6, 18) # Grade 1
    ],
    AFFIX.MANA: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.STRENGTH: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.AGILITY: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WISDOM: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CONSTITUTION: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.DEFENSE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.DEFENSE_PERCENTAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.PHYSICAL_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.ELEMENTAL_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.THRUST_RESISTANCE: [                    # HELMET SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.SLASH_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CRUSH_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.LIGHTNING_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.FIRE_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.COLD_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.POISON_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.THORNS: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.GOLD_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.MAGIC_FIND: [                    # HELMET SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.EXP_GAIN: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.REDUCED_REQUIREMENTS: [
      (, ), # Grade 0
      (, ) # Grade 1
    ]

  }, ## END 'helmets'

  'gloves': {
    AFFIX.HEALTH: [                    # GLOVES SECTION
      (2, 6), # Grade 0
      (6, 18) # Grade 1
    ],
    AFFIX.MANA: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.STRENGTH: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.AGILITY: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WISDOM: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CONSTITUTION: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.DEFENSE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.DEFENSE_PERCENTAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.PHYSICAL_RESISTANCE: [                    # GLOVES SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.ELEMENTAL_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.THRUST_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.SLASH_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CRUSH_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.LIGHTNING_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.FIRE_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.COLD_RESISTANCE: [                    # GLOVES SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.POISON_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.THORNS: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.GOLD_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.MAGIC_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.EXP_GAIN: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.REDUCED_REQUIREMENTS: [                    # GLOVES SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ]

  }, ## END 'gloves'

  'accessories': {
    AFFIX.HEALTH: [                  # ACCESSORIES SECTION
      (2, 6), # Grade 0
      (6, 18) # Grade 1
    ],
    AFFIX.MANA: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.STRENGTH: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.AGILITY: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WISDOM: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CONSTITUTION: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.DEFENSE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.DEFENSE_PERCENTAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.PHYSICAL_RESISTANCE: [                  # ACCESSORIES SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.ELEMENTAL_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.THRUST_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.SLASH_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CRUSH_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.LIGHTNING_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.FIRE_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.COLD_RESISTANCE: [                  # ACCESSORIES SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.POISON_RESISTANCE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.THORNS: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_FLAT: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.LIGHTNING_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.FIRE_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.COLD_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.POISON_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.GOLD_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.MAGIC_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.EXP_GAIN: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.REDUCED_REQUIREMENTS: [                  # ACCESSORIES SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ]

  }, ## END 'accessories'

  'one_handed_melee_weapons': {
    AFFIX.HEALTH: [                        # ONE HANDED MELEE SECTION             
      (2, 6), # Grade 0
      (6, 18) # Grade 1
    ],
    AFFIX.MANA: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.STRENGTH: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.AGILITY: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WISDOM: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CONSTITUTION: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
      (5, 20), # Grade 0
      (20, 50) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_FLAT: [
      [(1, 4), (4, 8)], # Grade 0
      [(3, 6), (6, 12)] # Grade 1
    ],
    AFFIX.LIGHTNING_DAMAGE: [              # ONE HANDED MELEE SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.FIRE_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.COLD_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.POISON_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.GOLD_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.MAGIC_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.EXP_GAIN: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.REDUCED_REQUIREMENTS: [                  # ONE HANDED MELEE SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ]
    ## TODO: Add all affixes that make sense for 1h melee

  }, ## END 'one_handed_melee_weapons'

  'shields': {
    ## TODO: Add all affixes that make sense for shields

  }, ## END 'shields'

  'orbs': {
    ## TODO: Add all affixes that make sense for orbs

  }, ## END 'orbs'

  'two_handed_melee_weapons': {
    AFFIX.HEALTH: [                    # TWO HANDED MELEE SECTION                
      (2, 6), # Grade 0
      (6, 18) # Grade 1
    ],
    AFFIX.MANA: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.STRENGTH: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.AGILITY: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WISDOM: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CONSTITUTION: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
      (5, 20), # Grade 0
      (20, 50) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_FLAT: [
      [(2, 6), (6, 14)], # Grade 0
      [(6, 10), (10, 24)] # Grade 1
    ],
    AFFIX.LIGHTNING_DAMAGE: [                  # TWO HANDED MELEE SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.FIRE_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.COLD_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.POISON_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.GOLD_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.MAGIC_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.EXP_GAIN: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.REDUCED_REQUIREMENTS: [                  # TWO HANDED MELEE SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ]
    ## TODO: Add all affixes that make sense for 2h melee

  }, ## END 'two_handed_melee_weapons'

  'one_handed_ranged_weapons': {
    AFFIX.HEALTH: [                        # ONE HANDED RANGED SECTION            
      (2, 6), # Grade 0
      (6, 18) # Grade 1
    ],
    AFFIX.MANA: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.STRENGTH: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.AGILITY: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WISDOM: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CONSTITUTION: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
      (5, 20), # Grade 0
      (20, 50) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_FLAT: [                  # ONE HANDED RANGED SECTION
      [(1, 4), (4, 8)], # Grade 0
      [(3, 6), (6, 12)] # Grade 1
    ],
    AFFIX.LIGHTNING_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.FIRE_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.COLD_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.POISON_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.GOLD_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.MAGIC_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.EXP_GAIN: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.REDUCED_REQUIREMENTS: [                  # ONE HANDED RANGED SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ]
    ## TODO: Add all affixes that make sense for 1h ranged

  }, ## END 'one_handed_ranged_weapons'

  'two_handed_ranged_weapons': {
    AFFIX.HEALTH: [                   # TWO HANDED RANGED SECTION                 
      (2, 6), # Grade 0
      (6, 18) # Grade 1
    ],
    AFFIX.MANA: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.STRENGTH: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.AGILITY: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WISDOM: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.CONSTITUTION: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_PERCENTAGE: [
      (5, 20), # Grade 0
      (20, 50) # Grade 1
    ],
    AFFIX.WEAPON_DAMAGE_FLAT: [                  # TWO HANDED RANGED SECTION
      [(2, 6), (6, 14)], # Grade 0
      [(6, 10), (10, 24)] # Grade 1
    ],
    AFFIX.LIGHTNING_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.FIRE_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.COLD_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.POISON_DAMAGE: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.GOLD_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.MAGIC_FIND: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.EXP_GAIN: [
      (, ), # Grade 0
      (, ) # Grade 1
    ],
    AFFIX.REDUCED_REQUIREMENTS: [                  # TWO HANDED RANGED SECTION
      (, ), # Grade 0
      (, ) # Grade 1
    ]
    ## TODO: Add all affixes that make sense for 2h ranged

  }, ## END 'two_handed_ranged_weapons'

}





