from google.appengine.ext import ndb
from protorpc import messages

from ability_model import *
class HeroModel(ndb.Model):
  player = ndb.KeyProperty(kind='PlayerModel')

  ## Meta attributes ##
  # The name of the hero.
  hero_name = ndb.StringProperty()
  # How many experience points the hero has.
  experience = ndb.IntegerProperty(default=0)
  # What Class the Hero is, see constants.py for the enum.
  hero_class = ndb.IntegerProperty()
  # How much currency this hero gets paid per day.
  salary = ndb.IntegerProperty()
  # How happy the hero is in the service of the player.
  morale = ndb.IntegerProperty()
  # How famous this hero is among their kingdom.
  fame = ndb.IntegerProperty()
  # How infamous this hero is among kingdoms other than their own.
  infamy = ndb.IntegerProperty()

  ## Status ##
  # Whether or not this hero is currently alive.
  ## TODO: Maybe replace this with an enum state for current state, with DEAD.
  is_alive = ndb.BooleanProperty()
  # TODO: figure out how wold map will work and add a property for position.

  ## Hero Intrinsic Attributes ##
  strength = ndb.IntegerProperty()
  constitution = ndb.IntegerProperty()
  agility = ndb.IntegerProperty()
  wisdom = ndb.IntegerProperty()
  movement_speed = ndb.IntegerProperty()

  ## Abilities ##
  ability_list = ndb.StructuredProperty(AbilityModel, repeated=True)

  ## Equipped Gear ##
  # TODO: consider using an InventoryModel or something like that.
  head_armor = ndb.KeyProperty(kind='ItemModel')
  body_armor = ndb.KeyProperty(kind='ItemModel')
  legs_armor = ndb.KeyProperty(kind='ItemModel')
  gloves = ndb.KeyProperty(kind='ItemModel')
  boots = ndb.KeyProperty(kind='ItemModel')
  # back = ndb.KeyProperty(kind='ItemModel')
  # neck = ndb.KeyProperty(kind='ItemModel')
  # left_finger = ndb.KeyProperty(kind='ItemModel')
  # right_finger = ndb.KeyProperty(kind='ItemModel')
  main_hand = ndb.KeyProperty(kind='ItemModel')
  off_hand = ndb.KeyProperty(kind='ItemModel')

  ## Items in the hero's inventory ##
  backpack = ndb.KeyProperty(kind='ItemModel', repeated=True)

  ## Hero artwork assets ##
  # TODO: figure out how to do sprites and stuff.

