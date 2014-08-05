## heroclass.py This file is used to represent all hero class related data and
## functions.

class HERO_CLASS:
  """
  This class is used to represent an enumlike object. Essentially it is a map
  of type to integer. So you can do things like hero_class = HERO_CLASS.WARRIOR.
  hero_class will == 1 or HERO_CLASS.WARRIOR. It will be used to make the code
  a little more readable. In the Hero.hero_class ndb IntegerProperty, warrior
  will be stored as 1.
  """
  WARRIOR = 1
  WIZARD = 2 # TODO: implement wizard.


#Base Stats (level 0 stat, growth per level)
base_attributes = {
  HERO_CLASS.WARRIOR: {
    'strength': (22, 3),
    'agility': (14, 1),
    'wisdom': (9, 1),
    'constitution': (22, 3)
  },
  HERO_CLASS.WIZARD: {
    'strength': (9, 1),
    'agility': (23, 2),
    'wisdom': (22, 3),
    'constitution': (18, 2)
  }
}

def getBaseAttributesForHero(hero_class, level):
  """
  Given a HERO_CLASS and level, return the base attributes for that hero.
  """
  return {
    'strength': base_attributes[hero_class]['strength'][0] +
        base_attributes[hero_class]['strength'][1]*level,
    'agility': base_attributes[hero_class]['agility'][0] +
        base_attributes[hero_class]['agility'][1]*level,
    'wisdom': base_attributes[hero_class]['wisdom'][0] +
        base_attributes[hero_class]['wisdom'][1]*level,
    'consitution': base_attributes[hero_class]['constitution'][0] +
        base_attributes[hero_class]['constitution'][1]*level,
  }


