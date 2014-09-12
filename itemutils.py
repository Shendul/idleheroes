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
## 6. Suffix Count: This is the number of suffix modifiers the item has.
## 6 through (6+7*Prefix Count). The prefix properties:
##    0. Type: The prefix type.
##    1 through 3. Min Value: The min value for the prefix.
##    4 through 7. Max Value: The max value for the prefix.
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
##     A110811H0002002a0004008
##     The first char (0) tells us it is a a Tunic (A = TUNIC)
##     The second char (1) tells us its grade is 1 (Shirt).
##     The next char (1) tells us that the item is Uncommon (Blue)
##     The next 2 chars (08) tell us the item level is 8.
##     The next char (1) tells us that there are 1 prefixes.
##     The next char (1) tells us that there are 1 suffixes.
##     The next 8 chars (H0010010) describe the first prefix.
##        H = physical resist.
##        0 = grade 0
##        002 = 10 min physical resist,
##        002 = 10 max physical resist. (resists don't have ranges so min == max)
##     The next 8 chars (a0004008) describe the first suffix.
##        a = thorns.
##        0 = grade 0
##        004 = 4 min thorns,
##        008 = 8 max thorns.
##     So the item is an Uncommon (Blue) Reinforced Cloth Armor of the Porcupine.
from affixes import *
from items import *
import random
import math

def getItemFromItemString(itemString):
  item = {}
  base_item_key = itemString[0]
  grade_index = int(itemString[1], 16) # We use hex value in this position.
  rarity_key = itemString[2]
  item['rarity'] = ITEM_RARITY_DISPLAY_NAME[rarity_key]

  ## Build the list of prefixes and suffixes
  item_affix_class_key = ITEM_AFFIX_CLASS[base_item_key] 
  prefixes = []
  suffixes = []
  suffix_count = int(itemString[6])
  index = 7
  for i in range(int(itemString[5])):
    prefix = {}
    prefix['affix_type'] = itemString[index]
    prefix['affix_grade'] = itemString[index + 1]
    if AFFIX_HAS_VALUE_RANGE[prefix['affix_type']]:
      prefix['has_value_range'] = True
      prefix['min_value'] = int(itemString[index+2:index+5])
      prefix['max_value'] = int(itemString[index+5:index+8])
    else:
      prefix['has_value_range'] = False
      prefix['value'] = int(itemString[index+2:index+8])
    index += 8
    prefixes.append(prefix)

  for i in range(int(itemString[6])):
    suffix = {}
    suffix['affix_type'] = itemString[index]
    suffix['affix_grade'] = itemString[index + 1]
    if AFFIX_HAS_VALUE_RANGE[suffix['affix_type']]:
      suffix['has_value_range'] = True
      suffix['min_value'] = int(itemString[index+2:index+5])
      suffix['max_value'] = int(itemString[index+5:index+8])
    else:
      suffix['has_value_range'] = False
      suffix['value'] = int(itemString[index+2:index+8])
    index += 8
    prefixes.append(suffix)

  ## Get Item Display Name
  display_name = ITEM_DISPLAY_NAME[base_item_key][grade_index]
  if rarity_key == ITEM_RARITY.UNCOMMON:
    # Not the worse time in the world to do a sanity check here.
    if len(prefixes) > 1 or len(suffixes) > 1:
      print 'Somehow a magic item has more than 1 prefix or suffix'
      return None
    ## Use the prefix and suffix names
    if len(prefixes) == 1:
      affix_type = [prefixes[0]['affix_type']]
      affix_grade = [prefixes[0]['affix_grade']]
      prefix_name = AFFIX_GRADES[item_affix_class_key][affix_type][affix_grade][0]
      display_name = prefix_name + ' ' + display_name
    if len(suffixes) == 1:
      affix_type = [suffixes[0]['affix_type']]
      affix_grade = [suffixes[0]['affix_grade']]
      suffix_name = AFFIX_GRADES[item_affix_class_key][affix_type][affix_grade][1]
      display_name = display_name + ' ' + suffix_name

  elif rarity_key == ITEM_RARITY.RARE:
    ## TODO: Make a rare name generator to replace this nonsense.
    display_name = 'Rare ' + display_name

  item['display_name'] = display_name
  item['item_level'] = int(itemString[3:5])

  ## Handle Weapon case
  if base_item_key in WEAPONS:
    damages = []
    ## Get the base damage type
    base_damage = {}
    base_damage['type'] = WEAPON_DAMAGE_TYPE[base_item_key]
    base_damage['damage_range'] = WEAPON_DAMAGE_RANGE[base_item_key][grade_index]

  elif base_item_key in ARMORS:
    item['defense'] = ARMOR_DEFENSE[base_item_key]
    ## TODO: consider the case of shield, which needs a block value.

  ## Add properties for all of the affixes, for now just make

  ## We're all done building the item object, return it.
  return item

## TODO: consider loot tables and stuff like that.
def generateRandomItem(magic_find, item_level):
  """
  Generates a random item, and returns the item's model string.
  """
  if item_level < 1:
    print 'error generating item, item level must be greater than 0'
    return None
  result = ''
  base_item = None
  possible_grades = []
  while True:
    base_item = random.choice(ALL_BASE_ITEMS)
    # Get the list of possible grades, if none, repick.
    highest_grade = -1
    for item_grade in ITEM_GRADES[base_item]:
      if item_level >= item_grade['item_level']:
       highest_grade += 1
    if highest_grade > -1:
      result = base_item # Set the first char of the string.
      break;
    else:
      continue

  ## Pick the base item grade
  item_grade = random.randint(0, highest_grade)
  result += format(item_grade, 'x') # Second character of the string = grade

  ## Determine rarity
  rarity_roll = math.pow(random.random(), getMagicFindFactor(magic_find))

  # TODO: adjust rarities, and add more rarities
  item_rarity = ITEM_RARITY.COMMON
  if rarity_roll > .90:
    item_rarity = ITEM_RARITY.RARE
  elif rarity_roll > .70:
    item_rarity = ITEM_RARITY.UNCOMMON
  result += item_rarity # Third Character of the string = rarity
  result += format(item_level, '02d') # 4th and 5th chars = iLvl

  ## Determine number of affixes on the item.
  prefix_count = 0
  suffix_count = 0
  if item_rarity == ITEM_RARITY.RARE:
    # TODO: Consider making a non uniform distribution here
    prefix_count = random.randint(1, 3)
    min_suffix_count = 1
    if prefix_count == 1:
      min_suffix_count = 2
    suffix_count = random.randint(min_suffix_count, 3)
  elif item_rarity == ITEM_RARITY.UNCOMMON:
    prefix_count = random.randint(0, 1)
    min_suffix_count = 0
    if prefix_count == 0:
      min_suffix_count = 1
    suffix_count = random.randint(min_suffix_count, 1)
  result += str(prefix_count) # 6th char of the string = prefix count
  result += str(suffix_count) # 7th char of the string = suffix count
  
  ## Generate the prefix strings
  prefixes = []
  while (prefix_count > 0):
    prefixes.append(generateAffix(item_level, base_item))
    prefix_count -= 1

  ## Generate the suffix strings
  suffixes = []
  while (suffix_count > 0):
    suffixes.append(generateAffix(item_level, base_item))
    suffix_count -= 1

  ## Build the affix strings into the item.
  for prefix in prefixes:
    result += prefix
  for suffix in suffixes:
    result += suffix
  return result


def getMagicFindFactor(magic_find):
  adjusted_magic_find = magic_find
  if adjusted_magic_find > 500:
    adjusted_magic_find = 500 + math.sqrt(magic_find - 500)
  if adjusted_magic_find > 700:
    adjusted_magic_find = 700
  return 1-(adjusted_magic_find/1000.00)


print generateRandomItem(0, 8)