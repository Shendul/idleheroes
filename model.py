from google.appengine.ext import ndb

class Hero(ndb.Model):
  """
  Models an individual Hero. Heroes, have many stats not shown here, but many
  of the attributes are calculated rather than stored.
  Heros have a name, experience number, inventory, hero_class,
  hero_settings.
  """
  name = ndb.StringProperty()
  experience = ndb.IntegerProperty(default=0) # See experience.py
  inventory = ndb.KeyProperty(kind='Inventory')
  hero_class = ndb.IntegerProperty(default=-1) # See heroclass.py HERO_CLASS
  hero_settings = ndb.KeyProperty(kind="HeroSettings")
  battle_history = ndb.KeyProperty(kind="BattleOutcome", repeated=True)


  class Battler(ndb.Model):
  """
  Models the parent of both Monster and Champion classes. to be used in combat to calculate
  true stats and determine the outcome of a battle.
  """
  level = ndb.IntegerProperty(default=1)
  damage = ndb.IntegerProperty()
  health_points = ndb.IntegerProperty()
  ice_resistance = ndb.IntegerProperty()


class User(ndb.Model):
  """
  Models an individual User entry with user_id, display_name, heroes, and
  game_settings.
  """
  user_id = ndb.StringProperty()  # Matches google user ID
  display_name = ndb.StringProperty()
  hero = ndb.KeyProperty(kind='Hero', repeated=True)
  ##game_settings = ndb.KeyProperty(kind='GameSettings')

class Inventory(ndb.Model):
  """
  Models a player's inventory. An inventory is a list of items, and a gold
  count. Items are encoded strings. See item.py.
  """
  items = ndb.StringProperty(repeated=True)
  gold = ndb.IntegerProperty(default=0)

class BattleOutcome(ndb.Model):
  """
  Models a battle outcome. A battle outcome has hero hp, enemy hp, enemy type,
  starttime, rewardExp, rewardGold, rewardItems.
  """
  hero_hp = ndb.IntegerProperty()
  enemy_hp = ndb.IntegerProperty()
  enemy_type = ndb.StringProperty()
  start_time = ndb.DateTimeProperty()
  reward_exp = ndb.IntegerProperty(default=0)
  reward_gold = ndb.IntegerProperty(default=0)
  reward_items = ndb.StringProperty(repeated=True)


##class GameSettings(ndb.Model):
##  """
##  Stores the User's game settings. This will be for global settings across all
##  heros. Currently Unused.
##  """  

##class HeroSettings(ndb.Model):
##  """
##  Stores the Hero's game settings. This will be for settings for a single hero.
##  Currently Unused.
##  """  
