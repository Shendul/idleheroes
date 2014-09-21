## heroclass.py This file is used to represent all hero class related data and
## functions.

import logging

from battle import *
from experience import *
from itemutils import *
from items import *
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

def getHeroGear(inventory):
  logging.info(inventory)
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

  for item in gear.values():
    if item != None:
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
  getHeroDamages(hero, agility, level, gear, actor)
  getHeroMetaStats(hero, level, gear, actor)
  return actor

def getHeroHealth(strength, constitution, level, gear, actor):
  ## Get base health
  actor[ACTOR_STAT.HEALTH] = strength*level + constitution*level
  ## Add hp from items.
  for item in gear.values():
    if item != None:
      if len(item['affixes']) > 0:
        for affix in item['affixes']:
          if affix['affix_type'] == AFFIX.HEALTH:
            actor[ACTOR_STAT.HEALTH] += affix['value']

def getHeroDefense(agility, constitution, level, gear, actor):
  ## Get base defense
  actor[ACTOR_STAT.DEFENSE] = agility*level + constitution*level / 4
  ## Add def from items.
  for item in gear.values():
    if item != None and item['item_type'] in ARMORS:
      actor[ACTOR_STAT.DEFENSE] += item[ACTOR_STAT.DEFENSE]
      if len(item['affixes']) > 0:
        for affix in item['affixes']:

          if affix['affix_type'] == AFFIX.DEFENSE:
            actor[ACTOR_STAT.DEFENSE] += affix['value']

          elif affix['affix_type'] == AFFIX.DEFENSE_PERCENTAGE:
            actor[ACTOR_STAT.DEFENSE] += (affix['value']/100.0)*actor[ACTOR_STAT.DEFENSE]

def getHeroResists(wisdom, constitution, level, gear, actor):
  ## Get base resists
  actor[ACTOR_STAT.THRUST_RESISTANCE] = constitution*level
  actor[ACTOR_STAT.SLASH_RESISTANCE] = constitution*level
  actor[ACTOR_STAT.CRUSH_RESISTANCE] = constitution*level
  actor[ACTOR_STAT.LIGHTNING_RESISTANCE] = wisdom*level
  actor[ACTOR_STAT.FIRE_RESISTANCE] = wisdom*level
  actor[ACTOR_STAT.COLD_RESISTANCE] = wisdom*level
  actor[ACTOR_STAT.POISON_RESISTANCE] = wisdom*level
  ## Add resists from items.
  for item in gear.values():
    if item != None:
      if len(item['affixes']) > 0:
        for affix in item['affixes']:

          if affix['affix_type'] == AFFIX.THRUST_RESISTANCE:
            actor[ACTOR_STAT.THRUST_RESISTANCE] += affix['value']

          elif affix['affix_type'] == AFFIX.SLASH_RESISTANCE:
            actor[ACTOR_STAT.SLASH_RESISTANCE] += affix['value']

          elif affix['affix_type'] == AFFIX.CRUSH_RESISTANCE:
            actor[ACTOR_STAT.CRUSH_RESISTANCE] += affix['value']

          elif affix['affix_type'] == AFFIX.LIGHTNING_RESISTANCE:
            actor[ACTOR_STAT.LIGHTNING_RESISTANCE] += affix['value']

          elif affix['affix_type'] == AFFIX.FIRE_RESISTANCE:
            actor[ACTOR_STAT.FIRE_RESISTANCE] += affix['value']

          elif affix['affix_type'] == AFFIX.COLD_RESISTANCE:
            actor[ACTOR_STAT.COLD_RESISTANCE] += affix['value']

          elif affix['affix_type'] == AFFIX.POISON_RESISTANCE:
            actor[ACTOR_STAT.POISON_RESISTANCE] += affix['value']

          elif affix['affix_type'] == AFFIX.PHYSICAL_RESISTANCE:
            actor[ACTOR_STAT.THRUST_RESISTANCE] += affix['value']
            actor[ACTOR_STAT.SLASH_RESISTANCE] += affix['value']
            actor[ACTOR_STAT.CRUSH_RESISTANCE] += affix['value']

          elif affix['affix_type'] == AFFIX.ELEMENTAL_RESISTANCE:
            actor[ACTOR_STAT.LIGHTNING_RESISTANCE] += affix['value']
            actor[ACTOR_STAT.FIRE_RESISTANCE] += affix['value']
            actor[ACTOR_STAT.COLD_RESISTANCE] += affix['value']
            actor[ACTOR_STAT.POISON_RESISTANCE] += affix['value']

def getHeroDamages(hero, agility, level, gear, actor):
  ## Get base damages
  actor[ACTOR_STAT.THRUST_DAMAGE] = (0,0)
  actor[ACTOR_STAT.SLASH_DAMAGE] = (0,0)
  actor[ACTOR_STAT.CRUSH_DAMAGE] = (0,0)
  actor[ACTOR_STAT.LIGHTNING_DAMAGE] = (0,0)
  actor[ACTOR_STAT.FIRE_DAMAGE] = (0,0)
  actor[ACTOR_STAT.COLD_DAMAGE] = (0,0)
  actor[ACTOR_STAT.POISON_DAMAGE] = (0,0)
  actor[ACTOR_STAT.THORNS_DAMAGE] = (0,0)
  actor[ACTOR_STAT.ACCURACY] = agility*level / 2
  base_damage = {}
  if gear['main_hand'] != None:
    base_damage = gear['main_hand']['base_damage']
  else:
    ## Fisting it.
    base_damage = {'type': DAMAGE_TYPE.CRUSH, 'damage_range': (1,3), 'accuracy': 20}

  ## Add dmg from items.
  for item in gear.values():
    if item != None:
      if len(item['affixes']) > 0:
        for affix in item['affixes']:

          ## Note that the order in which these affixes are applied actually matters, and is broken.
          if affix['affix_type'] == AFFIX.WEAPON_DAMAGE_FLAT:
            base_damage['damage_range'] = (base_damage['damage_range'][0] + affix['value'][0], base_damage['damage_range'][1] + affix['value'][1])

          if affix['affix_type'] == AFFIX.WEAPON_DAMAGE_PERCENTAGE:
            dmgPercent = 1 + (affix['value']/100.0)
            base_damage['damage_range'] = (base_damage['damage_range'][0] * dmgPercent, base_damage['damage_range'][1] * dmgPercent) 

          if affix['affix_type'] == AFFIX.LIGHTNING_DAMAGE:
            actor[ACTOR_STAT.LIGHTNING_DAMAGE] = addDamages(actor[ACTOR_STAT.LIGHTNING_DAMAGE], affix['value'])

          if affix['affix_type'] == AFFIX.FIRE_DAMAGE:
            actor[ACTOR_STAT.FIRE_DAMAGE] = addDamages(actor[ACTOR_STAT.FIRE_DAMAGE], affix['value'])

          if affix['affix_type'] == AFFIX.COLD_DAMAGE:
            actor[ACTOR_STAT.COLD_DAMAGE] = addDamages(actor[ACTOR_STAT.COLD_DAMAGE], affix['value'])

          if affix['affix_type'] == AFFIX.POISON_DAMAGE:
            actor[ACTOR_STAT.POISON_DAMAGE] = addDamages(actor[ACTOR_STAT.POISON_DAMAGE], affix['value'])

          if affix['affix_type'] == AFFIX.THORNS:
            actor[ACTOR_STAT.THORNS_DAMAGE] = addDamages(actor[ACTOR_STAT.THORNS_DAMAGE], affix['value'])

  if base_damage['type'] == DAMAGE_TYPE.THRUST:
    actor[ACTOR_STAT.THRUST_DAMAGE] = base_damage['damage_range']
  elif base_damage['type'] == DAMAGE_TYPE.SLASH:
    actor[ACTOR_STAT.SLASH_DAMAGE] = base_damage['damage_range']
  elif base_damage['type'] == DAMAGE_TYPE.CRUSH:
    actor[ACTOR_STAT.CRUSH_DAMAGE] = base_damage['damage_range']
  else:
    logging.error('item without thrust, slash, crush damage type equiped in main hand')
  actor[ACTOR_STAT.ACCURACY] += base_damage['accuracy']

def getHeroMetaStats(hero, level, gear, actor):
  actor[ACTOR_STAT.MAGIC_FIND] = 0
  actor[ACTOR_STAT.GOLD_FIND] = 0
  ## TODO: add remaining meta stats
  actor[ACTOR_STAT.NAME] = hero.name
  for item in gear.values():
    if item != None:
      if len(item['affixes']) > 0:
        for affix in item['affixes']:
          if affix['affix_type'] == AFFIX.GOLD_FIND:
            actor[ACTOR_STAT.GOLD_FIND] += affix['value']

          if affix['affix_type'] == AFFIX.MAGIC_FIND:
            actor[ACTOR_STAT.MAGIC_FIND] += affix['value']

def equipItem(inventory, item):
  item_object = getItemFromItemString(item)
  item_slot = ITEM_SLOT_MAP[item_object['item_type']]
  if item_slot == ITEM_SLOT.MAIN_HAND:
    inventory.main_hand = item 
  elif item_slot == ITEM_SLOT.OFF_HAND:
    inventory.off_hand = item
  elif item_slot == ITEM_SLOT.HEAD:
    inventory.head = item
  elif item_slot == ITEM_SLOT.BODY:
    inventory.body = item
  elif item_slot == ITEM_SLOT.BELT:
    inventory.belt = item
  elif item_slot == ITEM_SLOT.LEGS:
    inventory.legs = item
  elif item_slot == ITEM_SLOT.FEET:
    inventory.feet = item
  elif item_slot == ITEM_SLOT.SHOULDERS:
    inventory.shoulders = item
  elif item_slot == ITEM_SLOT.LEFT_RING:
    inventory.left_ring = item
  elif item_slot == ITEM_SLOT.RIGHT_RING:
    inventory.right_ring = item
  elif item_slot == ITEM_SLOT.LEFT_EARRING:
    inventory.left_earring = item
  elif item_slot == ITEM_SLOT.RIGHT_EARRING:
    inventory.right_earring = item
  elif item_slot == ITEM_SLOT.NECKLACE:
    inventory.necklace = item
  else:
    logging.error('No item slot for item: '+ item)
  inventory.put()
