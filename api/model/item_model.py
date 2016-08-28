from google.appengine.ext import ndb
from protorpc import messages

class EnhancementModel(ndb.Model):
  """TODO"""

class ResistModel(ndb.Model):
  resist_type = ndb.IntegerProperty()
  resist_amount = ndb.IntegerProperty()

class ItemModel(ndb.Model):
  """This class models an item for storage in the database."""
  ## Item information properties.
  # Which slot(s) the item belongs to.
  item_slot = ndb.IntegerProperty()
  # Type is an integer from constants.py that maps to top level item types like Bow or Chestpiece.
  item_type = ndb.IntegerProperty()
  # Grade of item that cooresponds to a material grade, like Steel or Iron.
  grade = ndb.IntegerProperty()
  # The Quality of the item from 0% to 100%, where 100% is perfect condition, and 0% is broken.
  quality = ndb.IntegerProperty()

  ## weapon type properties
  ## How much damage the weapon does.
  power = ndb.IntegerProperty()

  ## armor type properties
  resist_list = ndb.StructuredProperty(ResistModel, repeated=True)
  block_chance = ndb.IntegerProperty()
  dodge_chance_bonus = ndb.IntegerProperty()

  ## other properties
  level_requirement = ndb.IntegerProperty()
  craftsman = ndb.KeyProperty(kind='HeroModel')
  enhancement_list = ndb.StructuredProperty(EnhancementModel, repeated=True)
