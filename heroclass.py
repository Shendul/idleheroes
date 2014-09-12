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
base_stats = {
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
    ATTRIBUTE.STRENGTH: base_stats[hero_class][ATTRIBUTE.STRENGTH][0] +
        base_stats[hero_class][ATTRIBUTE.STRENGTH][1]*level,
    ATTRIBUTE.AGILITY: base_stats[hero_class][ATTRIBUTE.AGILITY][0] +
        base_stats[hero_class][ATTRIBUTE.AGILITY][1]*level,
    ATTRIBUTE.WISDOM: base_stats[hero_class][ATTRIBUTE.WISDOM][0] +
        base_stats[hero_class][ATTRIBUTE.WISDOM][1]*level,
    ATTRIBUTE.CONSTITUTION: base_stats[hero_class][ATTRIBUTE.CONSTITUTION][0] +
        base_stats[hero_class][ATTRIBUTE.CONSTITUTION][1]*level,
    # Get the base stats that are calculated from the four base stats above.
    ACTOR_STAT.HEALTH: base_stats[hero_class][ATTRIBUTE.STRENGTH][0] +
        base_stats[hero_class][ATTRIBUTE.STRENGTH][1]*level + 
        base_stats[hero_class][ATTRIBUTE.CONSTITUTION][0] +
        base_stats[hero_class][ATTRIBUTE.CONSTITUTION][1]*level*3,
    ACTOR_STAT.FIRE_RESISTANCE: base_stats[hero_class][ATTRIBUTE.WISDOM][0] +
        base_stats[hero_class][ATTRIBUTE.WISDOM][1]*level,
    ACTOR_STAT.ICE_RESISTANCE: base_stats[hero_class][ATTRIBUTE.WISDOM][0] +
        base_stats[hero_class][ATTRIBUTE.WISDOM][1]*level,
    # Defense here below is also to have a random chance of being 75-125% of base.
    ACTOR_STAT.DEFENSE: base_stats[hero_class][ATTRIBUTE.CONSTITUTION][0] +
        base_stats[hero_class][ATTRIBUTE.CONSTITUTION][1]*level + 
        base_stats[hero_class][ATTRIBUTE.AGILITY][0] +
        base_stats[hero_class][ATTRIBUTE.AGILITY][1]*level,
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
