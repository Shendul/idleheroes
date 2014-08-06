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


class STAT_TYPE:
  """
  This class is used to represent an enumlike object. Similar to the above
  class, this time for stats.
  """
  STRENGTH = 1
  AGILITY = 2
  WISDOM = 3
  CONSTITUTION = 4


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
    STAT_TYPE.STRENGTH: base_stats[hero_class][STAT_TYPE.STRENGTH][0] +
        base_stats[hero_class][STAT_TYPE.STRENGTH][1]*level,
    STAT_TYPE.AGILITY: base_stats[hero_class][STAT_TYPE.AGILITY][0] +
        base_stats[hero_class][STAT_TYPE.AGILITY][1]*level,
    STAT_TYPE.WISDOM: base_stats[hero_class][STAT_TYPE.WISDOM][0] +
        base_stats[hero_class][STAT_TYPE.WISDOM][1]*level,
    STAT_TYPE.CONSTITUTION: base_stats[hero_class][STAT_TYPE.CONSTITUTION][0] +
        base_stats[hero_class][STAT_TYPE.CONSTITUTION][1]*level,
  }


