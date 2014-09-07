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
  # THRUST_RESITANCE = 'J'
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

## TODO(shendul): Fill these out
PREFIX_DISPLAY_NAME = {
  ## TODO: Make different grades of names later.
  ## Attributes
  # AFFIX.HEALTH: 'Burly',
  # AFFIX.STRENGTH: 'Heavy',

  ## Weapon Specific
  # AFFIX.WEAPON_DAMAGE_FLAT: 'Deadly',
}

## TODO(shendul): Fill these out
SUFFIX_DISPLAY_NAME = {
  ## TODO: Make different grades of names later.
  ## Attributes
  # AFFIX.HEALTH: 'of Life',
  # AFFIX.STRENGTH: 'of the Hulk',

  ## Weapon Specific
  # AFFIX.WEAPON_DAMAGE_FLAT: 'of Slaying',
}






