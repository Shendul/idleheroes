## items.py This file is used to represent all items related data.
## See itemutils.py for all item related functions.

class ITEM:
  """
  This class maps the base item types to their item model characters.
  """
  ## Light Armors
  TUNIC = 'A'
  HAT = 'B'
  PANTS = 'C'
  BOOTS =  'D'
  MANTEL = 'E'
  GLOVES = 'F'
  ## Heavy Armors
  CHESTPLATE = 'G'
  HELMET = 'H'
  FAULDS = 'I'
  GREAVES = 'J'
  PAULDRONS = 'K'
  GAUNTLETS = 'L'
  ## Accessories
  RING = 'M'
  AMULET = 'N'
  EARRING = 'O'
  ## 1 Handed Weapons
  ONE_HANDED_SWORD = 'P'
  ONE_HANDED_AXE = 'Q'
  ONE_HANDED_MACE = 'R'
  # CLAW = 'S' ## TODO: Implement
  SHIELD = 'T'
  # ORB = 'U' ## TODO:  Implement
  ## 2 Handed Weapons
  TWO_HANDED_SWORD = 'V'
  QUARTERSTAFF = 'W'
  POLEARM = 'X'
  SPEAR = 'Y'
  TWO_HANDED_MACE = 'Z'
  ## 1 Handed Ranged Weapons
  SLING = 'a'
  # JAVELIN = 'b' ## TODO: Implement
  # WAND = 'c' ## TODO: Implement
  ## 2 Handed Ranged Weapons
  BOW = 'd'
  # CROSSBOW = 'e' ## TODO: Implement

class ITEM_SLOT:
  """
  This class maps the item slots.
  """

  MAIN_HAND = 'A'
  OFF_HAND = 'B'

  HEAD = 'C'
  BODY = 'D'
  BELT = 'E'
  LEGS = 'F'
  FEET = 'G'
  SHOULDERS = 'H'
  HANDS = 'I'

  LEFT_RING = 'J'
  RIGHT_RING = 'K'
  LEFT_EARRING = 'L'
  RIGHT_EARRING = 'M'
  NECKLACE = 'N'


ITEM_SLOT_MAP = {
  # Weapon slots
  ITEM.ONE_HANDED_SWORD : ITEM_SLOT.MAIN_HAND,
  ITEM.ONE_HANDED_MACE : ITEM_SLOT.MAIN_HAND,
  ITEM.ONE_HANDED_AXE : ITEM_SLOT.MAIN_HAND,
  #ITEM.CLAW : ITEM_SLOT.MAIN_HAND,
  ## 2 Handed Weapons
  ITEM.TWO_HANDED_SWORD: ITEM_SLOT.MAIN_HAND,
  ITEM.QUARTERSTAFF: ITEM_SLOT.MAIN_HAND,
  ITEM.POLEARM: ITEM_SLOT.MAIN_HAND,
  ITEM.SPEAR: ITEM_SLOT.MAIN_HAND,
  ITEM.TWO_HANDED_MACE: ITEM_SLOT.MAIN_HAND,
  ## 1 Handed Ranged Weapons
  ITEM.SLING: ITEM_SLOT.MAIN_HAND,
  # JAVELIN = 'b' ## TODO: Implement
  # WAND = 'c' ## TODO: Implement
  ## 2 Handed Ranged Weapons
  ITEM.BOW: ITEM_SLOT.MAIN_HAND,
  # CROSSBOW = 'e' ## TODO: Implement
  ITEM.SHIELD : ITEM_SLOT.OFF_HAND,
  #ITEM.ORB : ITEM_SLOT.OFF_HAND,
  # Armor
  ITEM.HAT : ITEM_SLOT.HEAD,
  ITEM.HELMET : ITEM_SLOT.HEAD,
  ITEM.TUNIC : ITEM_SLOT.BODY,
  ITEM.CHESTPLATE : ITEM_SLOT.BODY,
  ## TODO add belt
  ITEM.PANTS : ITEM_SLOT.LEGS,
  ITEM.FAULDS : ITEM_SLOT.LEGS,
  ITEM.BOOTS : ITEM_SLOT.FEET,
  ITEM.GREAVES : ITEM_SLOT.FEET,
  ITEM.MANTEL : ITEM_SLOT.SHOULDERS,
  ITEM.PAULDRONS : ITEM_SLOT.SHOULDERS,
  ITEM.GLOVES : ITEM_SLOT.HANDS,
  ITEM.GAUNTLETS : ITEM_SLOT.HANDS,
  # Accessory
  ITEM.RING : ITEM_SLOT.LEFT_RING, ## TODO add left and right for these v
  ITEM.EARRING : ITEM_SLOT.LEFT_EARRING,
  ITEM.AMULET : ITEM_SLOT.NECKLACE
}

## A list of all of the armors
ARMORS = [
  ITEM.TUNIC, ITEM.HAT, ITEM.PANTS, ITEM.BOOTS,
  ITEM.MANTEL, ITEM.GLOVES, ITEM.CHESTPLATE, ITEM.HELMET,
  ITEM.FAULDS, ITEM.GREAVES, ITEM.PAULDRONS,
  ITEM.GAUNTLETS, ITEM.SHIELD
]

## A list of all the weapons
WEAPONS = [
  ITEM.ONE_HANDED_SWORD, ITEM.ONE_HANDED_MACE,
  ITEM.ONE_HANDED_AXE, #ITEM.CLAW, ITEM.ORB,
  ITEM.TWO_HANDED_SWORD, ITEM.QUARTERSTAFF, ITEM.POLEARM,
  ITEM.SPEAR, ITEM.TWO_HANDED_MACE, ITEM.SLING,
  #ITEM.JAVELIN, ITEM.WAND, ITEM.CROSSBOW,
  ITEM.BOW
]

## A list of the accessories
ACCESSORIES = [
  ITEM.RING, ITEM.AMULET, ITEM.EARRING
]

ALL_BASE_ITEMS = ARMORS + WEAPONS + ACCESSORIES

## Item grade dictionary contains item display names and iLvl requirements for
##     each base item and it's grades.
## TODO: roll the base ranges and attribute reqs into this.
def item_grade(name, item_level):
  return {'name': name, 'item_level': item_level}

ITEM_GRADES = {
  ITEM.TUNIC: [
    item_grade('Collar', 1), 
    item_grade('Shirt', 6)
  ],
  ITEM.HAT: [
    item_grade('Bandana', 2),
    item_grade('Cap', 8)
  ],
  ITEM.PANTS: [
    item_grade('Loin Cloth', 2),
    item_grade('Kilt', 8)
  ],
  ITEM.BOOTS: [
    item_grade('Sandals', 1),
    item_grade('Cloth Wrappings', 6)
  ],
  ITEM.MANTEL: [
    item_grade('Half Robe', 3), 
    item_grade('King\'s Mantel', 9)
  ],
  ITEM.GLOVES: [
    item_grade('Hand Wrappings', 1),
    item_grade('Cloth Gloves', 5)
  ],
  ITEM.CHESTPLATE: [
    item_grade('Bone Shirt', 1),
    item_grade('Metal Plate', 6)
  ],
  ITEM.HELMET: [
    item_grade('Skull Mask', 2),
    item_grade('Sallet', 8)
  ],
  ITEM.FAULDS: [
    item_grade('Bone Skirt', 2),
    item_grade('Metal Loincloth', 7)
  ],
  ITEM.GREAVES: [
    item_grade('Plated Boots', 1),
    item_grade('Copper Greaves', 7)
  ],
  ITEM.PAULDRONS: [
    item_grade('Shoulder Pads', 3),
    item_grade('Shoulder Guards', 9)
  ],
  ITEM.GAUNTLETS: [
    item_grade('Bone Studded Gloves', 1),
    item_grade('Copper Gauntlets', 6)
  ],
  ITEM.ONE_HANDED_SWORD: [
    item_grade('Knife', 1),
    item_grade('Dagger', 6),
    item_grade('Copper Sword', 12)
  ],
  ITEM.ONE_HANDED_MACE: [
    item_grade('Club', 1),
    item_grade('Mallet', 6)
  ],
  ITEM.ONE_HANDED_AXE: [
    item_grade('Stone Axe', 1),
    item_grade('Copper Axe', 6)
  ],
  # ITEM.CLAW: [
  #   '', ''
  # ],
  ITEM.SHIELD: [
    item_grade('Wooden Buckler', 1),
    item_grade('Round Shield', 6)
  ],
  # ITEM.ORB: [
  #   '', ''
  # ],  
  ITEM.TWO_HANDED_SWORD: [
    item_grade('Dull Longsword', 2),
    item_grade('Longsword', 8)
  ],
  ITEM.QUARTERSTAFF: [
    item_grade('Branch', 1),
    item_grade('Wooden Staff', 6)
  ],
  ITEM.POLEARM: [
    item_grade('Glave', 3),
    item_grade('Bardiche', 9)
  ],
  ITEM.SPEAR: [
    item_grade('Wooden Spear', 2),
    item_grade('Copper Spear', 8)
  ],
  ITEM.TWO_HANDED_MACE: [
    item_grade('Tree Branch', 2),
    item_grade('Maul', 9)
  ],
  ITEM.SLING: [
    item_grade('Rocks', 1),
    item_grade('Short Sling', 8),
    item_grade('Leather Sling', 15)
  ],
  # ITEM.JAVELIN: [
  #   '', ''
  # ],
  # ITEM.WAND: [
  #   '', ''
  # ],
  ITEM.BOW: [
    item_grade('Shortbow', 1),
    item_grade('Recurve Bow', 8)
  ],
  # ITEM.CROSSBOW: [
  #   '', ''
  # ],
  ITEM.RING: [
    item_grade('Ring', 2)
  ],
  ITEM.AMULET: [
    item_grade('Amulet', 6)
  ],
  ITEM.EARRING: [
    item_grade('Earring', 8)
  ],
}

class ITEM_RARITY:
  COMMON = '0'
  UNCOMMON = '1'
  RARE = '2'

ITEM_RARITY_DISPLAY_NAME = {
  '0': 'Common', # NO Affixes
  '1': 'Uncommon', # 1-2 Affixes
  '2': 'Rare' # 3-6 Affixes
  ## TODO: Add more rarities
}

class DAMAGE_TYPE:
  THRUST = 'thrust'
  SLASH = 'slash'
  CRUSH = 'crush'
  LIGHTING = 'lighting'
  FIRE = 'fire'
  COLD = 'cold'
  POISON = 'poison'

WEAPON_DAMAGE_TYPE = {
  ## Make sure each damage here is in the weapon damage affix to actor stat map.
  ITEM.ONE_HANDED_SWORD: DAMAGE_TYPE.SLASH,
  ITEM.ONE_HANDED_AXE: DAMAGE_TYPE.SLASH,
  ITEM.ONE_HANDED_MACE: DAMAGE_TYPE.CRUSH,
  # ITEM.CLAW: DAMAGE_TYPE.THRUST,
  ITEM.TWO_HANDED_SWORD: DAMAGE_TYPE.SLASH,
  ITEM.QUARTERSTAFF: DAMAGE_TYPE.CRUSH,
  ITEM.POLEARM: DAMAGE_TYPE.SLASH,
  ITEM.SPEAR: DAMAGE_TYPE.THRUST,
  ITEM.TWO_HANDED_MACE: DAMAGE_TYPE.CRUSH,
  ITEM.SLING: DAMAGE_TYPE.CRUSH,
  # ITEM.JAVELIN: DAMAGE_TYPE.THRUST,
  # ITEM.WAND: DAMAGE_TYPE.FIRE, # TODO: find out what to really put.
  ITEM.BOW: DAMAGE_TYPE.THRUST,
  # ITEM.CROSSBOW: DAMAGE_TYPE.THRUST
}

WEAPON_DAMAGE_RANGE = {
  ITEM.ONE_HANDED_SWORD: [
    (1, 5), # Grade 0
    (2, 9), # Grade 1
    (15, 20) # Grade 2
  ],
  ITEM.ONE_HANDED_AXE: [
    (2, 4), # Grade 0
    (3, 7) # Grade 1
  ],
  ITEM.ONE_HANDED_MACE: [
    (3, 3), # Grade 0
    (4, 6) # Grade 1
  ],
  # ITEM.CLAW: [
  #   (1, 5), # Grade 0
  #   (1, 10) # Grade 1
  # ],
  ITEM.TWO_HANDED_SWORD: [
    (3, 7), # Grade 0
    (5, 11) # Grade 1
  ],
  ITEM.QUARTERSTAFF: [
    (1, 9), # Grade 0
    (3, 12) # Grade 1
  ],
  ITEM.POLEARM: [
    (4, 6), # Grade 0
    (5, 9) # Grade 1
  ],
  ITEM.SPEAR: [
    (3, 7), # Grade 0
    (4, 11) # Grade 1
  ],
  ITEM.TWO_HANDED_MACE: [
    (5, 6), # Grade 0
    (6, 8) # Grade 1
  ],
  ITEM.SLING: [
    (3, 3), # Grade 0
    (5, 5), # Grade 1
    (12, 9000) # Grade 1
  ],
  # ITEM.JAVELIN: [
  #   (1, 5), # Grade 0
  #   (2, 8) # Grade 1
  # ],
  # ITEM.WAND: [
  #   (2, 4), # Grade 0
  #   (3, 7) # Grade 1
  # ],
  ITEM.BOW: [
    (3, 7), # Grade 0
    (5, 11) # Grade 1
  ],
  # ITEM.CROSSBOW: [
  #   (4, 6), # Grade 0
  #   (7, 9) # Grade 1
  # ]
}

WEAPON_ACCURACY = {
  ITEM.ONE_HANDED_SWORD: [
    20, # Grade 0
    45, # Grade 1
    100 # Grade 2
  ],
  ITEM.ONE_HANDED_AXE: [
    18, # Grade 0
    40 # Grade 1
  ],
  ITEM.ONE_HANDED_MACE: [
    22, # Grade 0
    50 # Grade 1
  ],
  # ITEM.CLAW: [
  #   (1, 5), # Grade 0
  #   (1, 10) # Grade 1
  # ],
  ITEM.TWO_HANDED_SWORD: [
    15, # Grade 0
    35 # Grade 1
  ],
  ITEM.QUARTERSTAFF: [
    25, # Grade 0
    65 # Grade 1
  ],
  ITEM.POLEARM: [
    12, # Grade 0
    30 # Grade 1
  ],
  ITEM.SPEAR: [
    15, # Grade 0
    35 # Grade 1
  ],
  ITEM.TWO_HANDED_MACE: [
    15, # Grade 0
    35 # Grade 1
  ],
  ITEM.SLING: [
    15, # Grade 0
    35, # Grade 1
    80 # Grade 1
  ],
  # ITEM.JAVELIN: [
  #   (1, 5), # Grade 0
  #   (2, 8) # Grade 1
  # ],
  # ITEM.WAND: [
  #   (2, 4), # Grade 0
  #   (3, 7) # Grade 1
  # ],
  ITEM.BOW: [
    20, # Grade 0
    45 # Grade 1
  ],
  # ITEM.CROSSBOW: [
  #   (4, 6), # Grade 0
  #   (7, 9) # Grade 1
  # ]
}

ARMOR_DEFENSE = {
  ITEM.TUNIC: [
    10, # Grade 0
    24 # Grade 1
  ],
  ITEM.HAT: [
    4, # Grade 0
    9 # Grade 1
  ],
  ITEM.PANTS: [
    8, # Grade 0
    18 # Grade 1
  ],
  ITEM.BOOTS: [
    5, # Grade 0
    10 # Grade 1
  ],
  ITEM.MANTEL: [
    2, # Grade 0
    5 # Grade 1
  ],
  ITEM.GLOVES: [
    3, # Grade 0
    8 # Grade 1
  ],
  ITEM.CHESTPLATE: [
    13, # Grade 0
    28 # Grade 1
  ],
  ITEM.HELMET: [
    6, # Grade 0
    13 # Grade 1
  ],
  ITEM.FAULDS: [
    10, # Grade 0
    24 # Grade 1
  ],
  ITEM.GREAVES: [
    7, # Grade 0
    15 # Grade 1
  ],
  ITEM.PAULDRONS: [
    5, # Grade 0
    7 # Grade 1
  ],
  ITEM.GAUNTLETS: [
    5, # Grade 0
    15 # Grade 1
  ],
  ITEM.SHIELD: [
    5, # Grade 0
    9 # Grade 1
  ]
}


