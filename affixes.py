## affixes.py
## This file represents all of the data associated with affixes
class AFFIX:
  """
  This class maps the base affix type to a character that will be used in the
  item string.
  Uncomment each affix after implementation for the affix is completed.
  The section comments are basic seperators. When implementing each affix,
  decisions will need to be made regarding which affixes can be used on which
  items.
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

## TODO(shendul): Finish names
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
  # AFFIX.PHYSICAL_RESISTANCE: 'Reinforced',
  # AFFIX.ELEMENTAL_RESISTANCE: 'Weathered',
  # AFFIX.THRUST_RESISTANCE: 'Shelled',
  # AFFIX.SLASH_RESISTANCE: 'Hardened',
  # AFFIX.CRUSH_RESISTANCE: 'Padded',
  # AFFIX.LIGHTNING_RESISTANCE: 'Rubber',
  # AFFIX.FIRE_RESISTANCE: 'Flame Retardant',
  # AFFIX.COLD_RESISTANCE: 'Heated',
  # AFFIX.POISON_RESISTANCE: 'Alchemist's,
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

## TODO(shendul): Finish names
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






