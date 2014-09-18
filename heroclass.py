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

def getBaseStatsForHero(hero_class, level):
  """
  Given a HERO_CLASS and level, return the base stats for that hero.
  """
  return {
    # Get the four base stats.
    ATTRIBUTE.STRENGTH: HERO_BASE_STATS[hero_class][ATTRIBUTE.STRENGTH][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.STRENGTH][1]*level,
    ATTRIBUTE.AGILITY: HERO_BASE_STATS[hero_class][ATTRIBUTE.AGILITY][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.AGILITY][1]*level,
    ATTRIBUTE.WISDOM: HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][1]*level,
    ATTRIBUTE.CONSTITUTION: HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][1]*level,
    # Get the base stats that are calculated from the four base stats above.
    ACTOR_STAT.HEALTH: HERO_BASE_STATS[hero_class][ATTRIBUTE.STRENGTH][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.STRENGTH][1]*level + 
        HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][1]*level*3,
    ACTOR_STAT.FIRE_RESISTANCE: HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][1]*level,
    ACTOR_STAT.COLD_RESISTANCE: HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][1]*level,
    # Defense here below is also to have a random chance of being 75-125% of base.
    ACTOR_STAT.DEFENSE: HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][1]*level + 
        HERO_BASE_STATS[hero_class][ATTRIBUTE.AGILITY][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.AGILITY][1]*level,
  }

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
  strength = (HERO_BASE_STATS[hero_class][ATTRIBUTE.STRENGTH][0] + 
      HERO_BASE_STATS[hero_class][ATTRIBUTE.STRENGTH][1]*level)
  agility = (HERO_BASE_STATS[hero_class][ATTRIBUTE.AGILITY][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.AGILITY][1]*level)
  wisdom = (HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.WISDOM][1]*level)
  constitution = (HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][0] +
        HERO_BASE_STATS[hero_class][ATTRIBUTE.CONSTITUTION][1]*level)
  getHeroHealth(strength, constitution, level, gear, actor)
  #getHeroDefense(agility, constitution, level, gear, actor)
  #getHeroResists(wisdom, level, gear, actor)
  #getHeroDamages(hero, actor)
  #getHeroMetaStats(hero, actor)
  return actor

def getHeroHealth(strength, constitution, level, gear, actor):
  ## Get base health
  actor['health'] = strength*level + constitution*level
  ## Add hp from items.
  for item in gear:
    if len(item['prefixes']) > 0:
      for prefix in prefixes:
        if prefix['affix_type'] == AFFIX.HEALTH:
          actor['health'] += prefix['value']
    if len(item['suffixes']) > 0:
      for suffix in suffixes:
        if suffix['affix_type'] == AFFIX.HEALTH:
          actor['health'] += prefix['value']

## TODO(shendul): make the other getHeroxxxx() functions.


