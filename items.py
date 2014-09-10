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
  GUANTLETS = 'L'
  ## Accesories
  RING = 'M'
  AMULET = 'N'
  EARRING = 'O'
  ## 1 Handed Weapons
  ONE_HANDED_SWORD = 'P'
  ONE_HANDED_AXE = 'Q' ## TODO: Implement
  ONE_HANDED_MACE = 'R' ## TODO: Implement
  CLAW = 'S' ## TODO: Implement
  SHIELD = 'T'
  ORB = 'U' ## TODO:  Implement
  ## 2 Handed Weapons
  TWO_HANDED_SWORD = 'V'
  QUARTERSTAFF = 'W'
  POLEARM = 'X'
  SPEAR = 'Y'
  TWO_HANDED_MACE = 'Z'
  ## 1 Handed Ranged Weapons
  SLING = 'a'
  JAVELIN = 'b'
  WAND = 'c'
  ## 2 Handed Ranged Weapons
  BOW = 'd'
  CROSSBOW = 'e' ## TODO: Implement

## A list of all of the armors
ARMORS = [
  ITEM.TUNIC, ITEM.HAT, ITEM.PANTS, ITEM.BOOTS,
  ITEM.MANTEL, ITEM.GLOVES, ITEM.CHESTPLATE, ITEM.HELMET,
  ITEM.FAULDS, ITEM.GREAVES, ITEM.PAULDRONS,
  ITEM.GUANTLETS, ITEM.SHIELD
]

## A list of all the weapons
WEAPONS = [
  ITEM.ONE_HANDED_SWORD, ITEM.ONE_HANDED_MACE,
  ITEM.ONE_HANDED_AXE, ITEM.CLAW, ITEM.ORB,
  ITEM.TWO_HANDED_SWORD, ITEM.QUARTERSTAFF, ITEM.POLEARM,
  ITEM.SPEAR, ITEM.TWO_HANDED_MACE, ITEM.SLING,
  ITEM.JAVELIN, ITEM.WAND, ITEM.BOW, ITEM.CROSSBOW
]

## A list of the accesories
ACCESORIES = [
  ITEM.RING, ITEM.AMULET, ITEM.EARRING
]

ITEM_DISPLAY_NAME = {
  ITEM.TUNIC: [
    'Collar', 'Shirt'
  ],
  ITEM.HAT: [
    'Bandana', 'Cap'
  ],
  ITEM.PANTS: [
    'Loin Cloth', 'Kilt'
  ],
  ITEM.BOOTS: [
    'Sandals', 'Cloth Wrappings'
  ],
  ITEM.MANTEL: [
    'Half Robe', 'King\'s Mantel'
  ],
  ITEM.GLOVES: [
    'Hand Wrappings', 'Cloth Gloves'
  ],
  ITEM.CHESTPLATE: [
    'Bone Shirt', 'Metal Plate'
  ],
  ITEM.HELMET: [
    'Skull Mask', 'Sallet'
  ],
  ITEM.FAULDS: [
    'Bone Skirt', 'Metal Loincloth'
  ],
  ITEM.GREAVES: [
    'Plated Boots', 'Copper Greaves'
  ],
  ITEM.PAULDRONS: [
    'Metal', 'Spiked'
  ],
  ITEM.GUANTLETS: [
    'Bone Studded Gloves', 'Copper Gauntlets'
  ],
  ITEM.ONE_HANDED_SWORD: [
    'Knife', 'Dagger'
  ],
  ITEM.ONE_HANDED_MACE: [
    '', ''
  ],
  ITEM.ONE_HANDED_AXE: [
    '', ''
  ],
  ITEM.CLAW: [
    '', ''
  ],
  ITEM.SHIELD: [
    '', ''
  ],
  ITEM.ORB: [
    '', ''
  ],  
  ITEM.TWO_HANDED_SWORD: [
    'Dull Longsword', 'Longsword'
  ],
  ITEM.QUARTERSTAFF: [
    'Branch', 'Wooden Staff'
  ],
  ITEM.POLEARM: [
    'Glave', 'Bardiche'
  ],
  ITEM.SPEAR: [
    'Wooden Spear', 'Metal Spear'
  ],
  ITEM.TWO_HANDED_MACE: [
    '', ''
  ],
  ITEM.SLING: [
    'Rocks', 'Sling'
  ],
  ITEM.JAVELIN: [
    '', ''
  ],
  ITEM.WAND: [
    '', ''
  ],
  ITEM.BOW: [
    'Shortbow', 'Recurve'
  ],
  ITEM.CROSSBOW: [
    '', ''
  ]
}

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
  ITEM.ONE_HANDED_SWORD: DAMAGE_TYPE.SLASH,
  ITEM.ONE_HANDED_AXE: DAMAGE_TYPE.SLASH,
  ITEM.ONE_HANDED_MACE: DAMAGE_TYPE.CRUSH,
  ITEM.CLAW: DAMAGE_TYPE.THRUST,
  ITEM.TWO_HANDED_SWORD: DAMAGE_TYPE.SLASH,
  ITEM.QUARTERSTAFF: DAMAGE_TYPE.CRUSH,
  ITEM.POLEARM: DAMAGE_TYPE.SLASH,
  ITEM.SPEAR: DAMAGE_TYPE.THRUST,
  ITEM.TWO_HANDED_MACE: DAMAGE_TYPE.CRUSH,
  ITEM.SLING: DAMAGE_TYPE.CRUSH,
  ITEM.JAVELIN: DAMAGE_TYPE.THRUST,
  ITEM.WAND: DAMAGE_TYPE.FIRE, # TODO: find out what to really put.
  ITEM.BOW: DAMAGE_TYPE.THRUST,
  ITEM.CROSSBOW: DAMAGE_TYPE.THRUST
}

WEAPON_DAMAGE_RANGE = {
  ITEM.ONE_HANDED_SWORD: [
    (1, 5), # Grade 0
    (2, 9) # Grade 1
  ],
  ITEM.ONE_HANDED_AXE: [
    (2, 4), # Grade 0
    (3, 7) # Grade 1
  ],
  ITEM.ONE_HANDED_MACE: [
    (3, 3), # Grade 0
    (4, 6) # Grade 1
  ],
  ITEM.CLAW: [
    (1, 5), # Grade 0
    (1, 10) # Grade 1
  ],
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
    (5, 5) # Grade 1
  ],
  ITEM.JAVELIN: [
    (1, 5), # Grade 0
    (2, 8) # Grade 1
  ],
  ITEM.WAND: [
    (2, 4), # Grade 0
    (3, 7) # Grade 1
  ],
  ITEM.BOW: [
    (3, 7), # Grade 0
    (5, 11) # Grade 1
  ],
  ITEM.CROSSBOW: [
    (4, 6), # Grade 0
    (7, 9) # Grade 1
  ]
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
  ITEM.GUANTLETS: [
    5, # Grade 0
    15 # Grade 1
  ],
  ITEM.SHIELD: [
    5, # Grade 0
    9 # Grade 1
  ]
}


