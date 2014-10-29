from google.appengine.ext import ndb
from protorpc import messages

class ItemModel(ndb.Model):
  """This class models an item for storage in the database."""
  ## Item information properties.
  item_type = ndb.StringProperty()
  item_rarity = ndb.StringProperty()
  item_name = ndb.StringProperty()
  item_level = ndb.IntegerProperty()

  ## weapon type properties
  action_point_cost = ndb.IntegerProperty()
  min_damage = ndb.IntegerProperty()
  max_damage = ndb.IntegerProperty()
  auto_attack_damage_type = ndb.StringProperty()

  ## armor type properties
  thrust_resist = ndb.IntegerProperty()
  slash_resist = ndb.IntegerProperty()
  crush_resist = ndb.IntegerProperty()
  lightning_resist = ndb.IntegerProperty()
  ice_resist = ndb.IntegerProperty()
  fire_resist = ndb.IntegerProperty()
  encumberance = ndb.IntegerProperty()

  ## other properties
  level_requirement = ndb.IntegerProperty()
  agility_requirement = ndb.IntegerProperty()
  strength_requirement = ndb.IntegerProperty()
  wisdom_requirement = ndb.IntegerProperty()

  ## Affixes are stored as python dictionaries that are pickled.
  ## See: https://wiki.python.org/moin/UsingPickle
  affixes = ndb.PickleProperty(repeated=True)
