## itemutils.py
##
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
from items import *

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