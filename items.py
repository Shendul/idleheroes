## items.py This file is used to represent all items related data and
## functions.
## The item model is as follows:
## A variable length case sensitive string where the first 6 characters give the
## overview of the item, and the following n*7 characters give mod information,
## where n == number of modifiers (affixes).
##
## The first 6 indices represent the following properties:
## 0. Item type: Ring, 1H Sword, 2H Mace, shield, chestpiece, ring, ammy, etc...
## 1. Grade: (1H Sword) Wooden Sword. Bronze Sword, Iron Sword, Scimitar, etc...
##     This will grow from 0 to E or something, where each grade represents a
##     new item of the same type. So for this example, 0 in this position means
##     Wooden Sword if the Item Type is 1H Sword.
## 2. Rarity: Common (White), Uncommon (Blue), Rare (Yellow), etc
## 3,4. Item Level: 00-99
## 5. Prefix Count: This is the number of prefix modifiers the item has.
## 6 through (6+7*Prefix Count). The prefix properties:
##    0. Type: The prefix type.
##    1 through 3. Min Value: The min value for the prefix.
##    4 through 7. Max Value: The max value for the prefix.
## 7 + PC*7. Suffix Count: This is the number of suffix modifiers the item has.
##    Same formatting applies from prefixes.  
##
## TODO: Update the examples to be a little more interesting.
## Here is an example Common (White) item:
##     A00040
##     The first char (0) tells us it is a Tunic (A = TUNIC)
##     The second char (0) tells us its grade is 0 (Collar).
##     The next char (0) tells us that the item is common (White)
##     The next 2 chars (04) tell us the item level is 4.
##     Finally the last char (0) tells us that there are no affixes.
##     So the item is a Common (White) Cloth Armor.
##
## Here is an example Uncommon (Blue) item:
##     A11081r0100101a004004
##     The first char (0) tells us it is a a Tunic (A = TUNIC)
##     The second char (1) tells us its grade is 1 (Shirt).
##     The next char (1) tells us that the item is Uncommon (Blue)
##     The next 2 chars (08) tell us the item level is 8.
##     The next char (1) tells us that there are 1 prefixes.
##     The next 7 chars (r010010) describe the first prefix.
##        r = fire resist.
##        010 = 10 min fire resist,
##        010 = 10 max fire resist. (resists don't have ranges so min == max)
##     The next char (1) tells us that there are 1 suffixes.
##     The next 7 chars (a004004) describe the first suffix.
##        a = strength.
##        004 = 4 min strength,
##        004 = 4 max strength. (attributes don't have ranges so min == max)
##     So the item is an Uncommon (Blue) Prefect's Cloth Armor of Strength.

from affixes import *

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

def getItemFromItemString(itemString):
  item = {}
  base_item_key = itemString[0]
  grade_index = int(itemString[1], 16) # We use hex value in this position.
  rarity_key = itemString[2]
  ## Get Item Base Display Name
  item['base_item_display_name'] = ITEM_DISPLAY_NAME[base_item_key][grade_index]
  item['rarity'] = ITEM_RARITY_DISPLAY_NAME[rarity_key]
  item['item_level'] = int(itemString[3:5])

  ## Handle Weapon case
  if base_item_key in WEAPONS:
    damages = []
    ## Get the base damage type
    base_damage = {}
    base_damage['type'] = WEAPON_DAMAGE_TYPE[base_item_key]
    base_damage['damage_range'] = WEAPON_DAMAGE_RANGE[base_item_key][grade_index]
    ## TODO(dreamlane): Check for affixes that affect weapon damage.
    damage['type'] = WEAPON_DAMAGE_TYPE
    item['damage'] = damage
    ## TODO(dreamlane): Add damages from weapon affixes.

  elif base_item_key in ARMORS:
    item['defense'] = ARMOR_DEFENSE[base_item_key]
    ## TODO(dreamlane): Add defenses from armor affixes.

  elif base_item_key in ACCESORIES:
    ## TODO(dreamlane): Parse through the affixes.
    pass


  ## We're all done building the item object, return it.
  return item


print getItemFromItemString('A11081r0100101a004004')
