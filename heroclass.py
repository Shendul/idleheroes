## heroclass.py This file is used to represent all hero class related data and
## functions.

import logging

from battle import *
from experience import *
from itemutils import *
from affixes import *

class HERO_CLASS:
  """
  This class is used to represent an enumlike object. Essentially it is a map
  of type to string. So you can do things like hero_class = HERO_CLASS.WARRIOR.
  hero_class will == "warrior" or HERO_CLASS.WARRIOR. It will be used to make 
  the code a little more readable. In the Hero.hero_class ndb StringProperty,
  warrior will be stored as "warrior".
  """
  NO_CLASS = "no_class"
  WARRIOR = "warrior"
  WIZARD = "wizard" # TODO: implement wizard.


class ATTRIBUTE:
  """
  This class is used to represent an enumlike object. Similar to the above
  class, this time for stats.
  """
  STRENGTH = 'strength'
  AGILITY = 'agility'
  WISDOM = 'wisdom'
  CONSTITUTION = 'constitution'


#Base Stats (level 0 stat, growth per level)
HERO_BASE_STATS = {
  HERO_CLASS.WARRIOR: {
    ATTRIBUTE.STRENGTH: (22, 3),
    ATTRIBUTE.AGILITY: (14, 1),
    ATTRIBUTE.WISDOM: (9, 1),
    ATTRIBUTE.CONSTITUTION: (22, 3)
  },
  HERO_CLASS.WIZARD: {
    ATTRIBUTE.STRENGTH: (9, 1),
    ATTRIBUTE.AGILITY: (23, 2),
    ATTRIBUTE.WISDOM: (22, 3),
    ATTRIBUTE.CONSTITUTION: (18, 2)
  }
}

## Function for adding two digit tuples.
def addDamages(base, change):
  result = (base[0] + change[0], base[1] + change[1])
  return result

equipped_item_keys = ['main_hand', 'off_hand', 'head', 'body', 'belt',
    'legs', 'feet', 'shoulders', 'hands', 'left_ring', 'right_ring',
    'left_earring', 'right_earring', 'necklace']

def getHeroValues(ih_hero_model):
  hero = {}
  hero['name'] = ih_hero_model.name
  level = getHeroLevel(ih_hero_model.experience)
  hero['level'] = level
  # Determine the stats of the hero
  hero['stats'] = getBaseStatsForHero(ih_hero_model.hero_class, level)
  # Check equipped items for basic stats
  # TODO(dreamlane): Error handling on the get. Build a model layer.
  inventory = ih_hero_model.inventory.get()
  for item_key in equipped_item_keys:
    logging.info(item_key)
    if getattr(inventory, item_key) != None:
      #TODO(dreamlane): Parse item string for base attributes.
      continue

  return hero

def getHeroGear(inventory):
  result = {
    'main_hand': None,
    'off_hand': None,
    'head': None,
    'body': None,
    'belt': None,
    'legs': None,
    'feet': None,
    'shoulders': None,
    'hands': None,
    # Accessory slots
    'left_ring': None,
    'right_ring': None,
    'left_earring': None,
    'right_earring': None,
    'necklace': None,
    # Special slots
    'back': None,
    'mount': None,
  }
  result['main_hand'] = getItemFromItemString(inventory.main_hand)
  result['off_hand'] = getItemFromItemString(inventory.off_hand)
  result['head'] = getItemFromItemString(inventory.head)
  result['body'] = getItemFromItemString(inventory.body)
  result['belt'] = getItemFromItemString(inventory.belt)
  result['legs'] = getItemFromItemString(inventory.legs)
  result['feet'] = getItemFromItemString(inventory.feet)
  result['shoulders'] = getItemFromItemString(inventory.shoulders)
  result['hands'] = getItemFromItemString(inventory.hands)
  result['left_ring'] = getItemFromItemString(inventory.left_ring)
  result['right_ring'] = getItemFromItemString(inventory.right_ring)
  result['left_earring'] = getItemFromItemString(inventory.left_earring)
  result['right_earring'] = getItemFromItemString(inventory.right_earring)
  result['necklace'] = getItemFromItemString(inventory.necklace)
  result['back'] = getItemFromItemString(inventory.back)
  result['mount'] = getItemFromItemString(inventory.mount)
  return result

def getBattleActorFromHero(hero):
  ## TODO: Finish this function.
  actor = {}
  level = getHeroLevel(hero.experience)
  gear = getHeroGear(hero.inventory.get())
  hero_class = hero.hero_class
  ## base stats.
  strength = (HERO_BASE_STATS[hero_class][ATTRIBUTE.STRENGTH][0] + 
      HERO_BASE_STATS[hero_class][ATTRIBUTE.STRENGTH][1]*level)
  agility = (HERO_BASE_STATS[hero_class][ATTRIBUTE.AGILITY][0] +
      HERO_BASE_STATS[hero_class][ATTRIBUTE.AGILITY][1]*level)
  wisdom = (HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][0] +
      HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][1]*level)
  constitution = (HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][0] +
      HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][1]*level)

  for item in gear:
    if len(item['affixes']) > 0:
      for affix in item['affixes']:
        if affix['affix_type'] == AFFIX.STRENGTH:
          strength += affix['value']
        if affix['affix_type'] == AFFIX.AGILITY:
          agility += affix['value']
        if affix['affix_type'] == AFFIX.WISDOM:
          wisdom += affix['value']
        if affix['affix_type'] == AFFIX.CONSTITUTION:
          constitution += affix['value']
  
  getHeroHealth(strength, constitution, level, gear, actor)
  getHeroDefense(agility, constitution, level, gear, actor)
  getHeroResists(wisdom, constitution, level, gear, actor)
  getHeroDamages(hero, level, gear, actor)
  getHeroMetaStats(hero, actor)
  return actor

def getHeroHealth(strength, constitution, level, gear, actor):
  ## Get base health
  actor['health'] = strength*level + constitution*level
  ## Add hp from items.
  for item in gear:
    if len(item['affixes']) > 0:
      for affix in item['affixes']:
        if affix['affix_type'] == AFFIX.HEALTH:
          actor['health'] += affix['value']

def getHeroDefense(agility, constitution, level, gear, actor):
  ## Get base defense
  actor['defense'] = agility*level + constitution*level / 4
  ## Add def from items.
  for item in gear:
    actor['defence'] += item['defense']
    if len(item['affixes']) > 0:
      for affix in item['affixes']:

        if affix['affix_type'] == AFFIX.DEFENSE:
          actor['defense'] += affix['value']

        elif affix['affix_type'] == AFFIX.DEFENSE_PERCENTAGE:
          actor['defense'] += (affix['value']/100.0)*actor['defense']

def getHeroResists(wisdom, constitution, level, gear, actor):
  ## Get base resists
  actor['thrust_resistance'] = constitution*level
  actor['slash_resistance'] = constitution*level
  actor['crush_resistance'] = constitution*level
  actor['lightning_resistance'] = wisdom*level
  actor['fire_resistance'] = wisdom*level
  actor['cold_resistance'] = wisdom*level
  actor['poison_resistance'] = wisdom*level
  ## Add resists from items.
  for item in gear:
    if len(item['affixes']) > 0:
      for affix in item['affixes']:

        if affix['affix_type'] == AFFIX.THRUST_RESISTANCE:
          actor['thrust_resistance'] += affix['value']

        elif affix['affix_type'] == AFFIX.SLASH_RESISTANCE:
          actor['slash_resistance'] += affix['value']

        elif affix['affix_type'] == AFFIX.CRUSH_RESISTANCE:
          actor['crush_resistance'] += affix['value']

        elif affix['affix_type'] == AFFIX.LIGHTNING_RESISTANCE:
          actor['lightning_resistance'] += affix['value']

        elif affix['affix_type'] == AFFIX.FIRE_RESISTANCE:
          actor['fire_resistance'] += affix['value']

        elif affix['affix_type'] == AFFIX.COLD_RESISTANCE:
          actor['cold_resistance'] += affix['value']

        elif affix['affix_type'] == AFFIX.POISON_RESISTANCE:
          actor['poison_resistance'] += affix['value']

        elif affix['affix_type'] == AFFIX.PHYSICAL_RESISTANCE:
          actor['thrust_resistance'] += affix['value']
          actor['slash_resistance'] += affix['value']
          actor['crush_resistance'] += affix['value']

        elif affix['affix_type'] == AFFIX.ELEMENTAL_RESISTANCE:
          actor['lightning_resistance'] += affix['value']
          actor['fire_resistance'] += affix['value']
          actor['cold_resistance'] += affix['value']
          actor['poison_resistance'] += affix['value']

def getHeroDamages(hero, level, gear, actor):
  ## Get base damages
  actor['thrust_damage'] = (0,0)
  actor['slash_damage'] = (0,0)
  actor['crush_damage'] = (0,0)
  actor['lightning_damage'] = (0,0)
  actor['fire_damage'] = (0,0)
  actor['cold_damage'] = (0,0)
  actor['poison_damage'] = (0,0)
  actor['thorns_damage'] = (0,0)
  ## Add dmg from items.
  for item in gear:
    ## TODO: account for duel wielding if we have it.
    if base_damage['type'] == 'thrust':
      actor['thrust_damage'] = base_damage['damage_range']

    elif base_damage['type'] == 'slash':
      actor['slash_damage'] = base_damage['damage_range']

    elif base_damage['type'] == 'crush':
      actor['crush_damage'] = base_damage['damage_range']

    if len(item['affixes']) > 0:
      for affix in item['affixes']:

        if affix['affix_type'] == AFFIX.WEAPON_DAMAGE_FLAT:
          if base_damage['type'] == 'thrust':
            actor['thrust_damage'] = addDamages(actor['thrust_damage'], affix['value'])
          elif base_damage['type'] == 'slash':
            actor['slash_damage'] = addDamages(actor['slash_damage'], affix['value'])
          elif base_damage['type'] == 'crush':
            actor['crush_damage'] = addDamages(actor['crush_damage'], affix['value'])

        if affix['affix_type'] == AFFIX.WEAPON_DAMAGE_PERCENTAGE:
          dmgPercent = affix['value']/100.0
          if base_damage['type'] == 'thrust':
            actor['thrust_damage'][0] += actor['thrust_damage'][0]*dmgPercent
            actor['thrust_damage'][1] += actor['thrust_damage'][1]*dmgPercent
          elif base_damage['type'] == 'slash':
            actor['slash_damage'][0] += actor['slash_damage'][0]*dmgPercent
            actor['slash_damage'][1] += actor['slash_damage'][1]*dmgPercent
          elif base_damage['type'] == 'crush':
            actor['crush_damage'][0] += actor['crush_damage'][0]*dmgPercent
            actor['crush_damage'][1] += actor['crush_damage'][1]*dmgPercent 

        if affix['affix_type'] == AFFIX.LIGHTNING_DAMAGE:
          actor['lightning_damage'] = addDamages(actor['lightning_damage'], affix['value'])

        if affix['affix_type'] == AFFIX.FIRE_DAMAGE:
          actor['fire_damage'] = addDamages(actor['fire_damage'], affix['value'])

        if affix['affix_type'] == AFFIX.COLD_DAMAGE:
          actor['cold_damage'] = addDamages(actor['cold_damage'], affix['value'])

        if affix['affix_type'] == AFFIX.POISON_DAMAGE:
          actor['poison_damage'] = addDamages(actor['poison_damage'], affix['value'])

        if affix['affix_type'] == AFFIX.THORNS_DAMAGE:
          actor['thorns_damage'] = addDamages(actor['thorns_damage'], affix['value'])

def getHeroMetaStats(hero, level, gear, actor):
  ## TODO: add remaining meta stats
  for item in gear:
    if len(item['affixes']) > 0:
      for affix in item['affixes']:
        if affix['affix_type'] == AFFIX.GOLD_FIND:
          actor['gold_find'] += affix['value']

        if affix['affix_type'] == AFFIX.MAGIC_FIND:
          actor['magic_find'] += affix['value']