## heroclass.py This file is used to represent all hero class related data and
## functions.

import logging

from battlestats import *
from experience import *

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


class STAT_TYPE:
  """
  This class is used to represent an enumlike object. Similar to the above
  class, this time for stats.
  """
  STRENGTH = 'strength'
  AGILITY = 'agility'
  WISDOM = 'wisdom'
  CONSTITUTION = 'constitution'


#Base Stats (level 0 stat, growth per level)
base_stats = {
  HERO_CLASS.WARRIOR: {
    STAT_TYPE.STRENGTH: (22, 3),
    STAT_TYPE.AGILITY: (14, 1),
    STAT_TYPE.WISDOM: (9, 1),
    STAT_TYPE.CONSTITUTION: (22, 3)
  },
  HERO_CLASS.WIZARD: {
    STAT_TYPE.STRENGTH: (9, 1),
    STAT_TYPE.AGILITY: (23, 2),
    STAT_TYPE.WISDOM: (22, 3),
    STAT_TYPE.CONSTITUTION: (18, 2)
  }
}

def getBaseStatsForHero(hero_class, level):
  """
  Given a HERO_CLASS and level, return the base stats for that hero.
  """
  return {
  # Get the four base stats.
    STAT_TYPE.STRENGTH: base_stats[hero_class][STAT_TYPE.STRENGTH][0] +
        base_stats[hero_class][STAT_TYPE.STRENGTH][1]*level,
    STAT_TYPE.AGILITY: base_stats[hero_class][STAT_TYPE.AGILITY][0] +
        base_stats[hero_class][STAT_TYPE.AGILITY][1]*level,
    STAT_TYPE.WISDOM: base_stats[hero_class][STAT_TYPE.WISDOM][0] +
        base_stats[hero_class][STAT_TYPE.WISDOM][1]*level,
    STAT_TYPE.CONSTITUTION: base_stats[hero_class][STAT_TYPE.CONSTITUTION][0] +
        base_stats[hero_class][STAT_TYPE.CONSTITUTION][1]*level,
  # Get the base stats that are calculated from the four base stats above.
    BATTLE_STATS.HEALTH: base_stats[hero_class][STAT_TYPE.STRENGTH][0] +
        base_stats[hero_class][STAT_TYPE.STRENGTH][1]*level + 
        base_stats[hero_class][STAT_TYPE.CONSTITUTION][0] +
        base_stats[hero_class][STAT_TYPE.CONSTITUTION][1]*level*3,
    BATTLE_STATS.FIRE_RESISTANCE: base_stats[hero_class][STAT_TYPE.WISDOM][0] +
        base_stats[hero_class][STAT_TYPE.WISDOM][1]*level,
    BATTLE_STATS.ICE_RESISTANCE: base_stats[hero_class][STAT_TYPE.WISDOM][0] +
        base_stats[hero_class][STAT_TYPE.WISDOM][1]*level,
  # Defence here below is also to have a random chance of being 75-125% of base.
    BATTLE_STATS.DEFENCE: base_stats[hero_class][STAT_TYPE.CONSTITUTION][0] +
        base_stats[hero_class][STAT_TYPE.CONSTITUTION][1]*level + 
        base_stats[hero_class][STAT_TYPE.AGILITY][0] +
        base_stats[hero_class][STAT_TYPE.AGILITY][1]*level,
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
