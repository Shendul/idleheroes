## ItemModel.py
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

  ## Todo: determine if we want starting items to be marked as such (to prevent selling etc...)

class ItemMessage(messages.Message):
  ## Item information properties.
  item_type = messages.StringField(1)
  item_rarity = messages.StringField(2)
  item_name = messages.StringField(3)
  item_level = messages.IntegerField(4)

  ## weapon type properties
  weapon_type = messages.StringField(5)
  action_point_cost = messages.IntegerField(6)
  min_damage = messages.IntegerField(7)
  max_damage = messages.IntegerField(8)

  ## armor type properties
  armor_type = messages.StringField(9)
  thrust_resist = messages.IntegerField(10)
  slash_resist = messages.IntegerField(11)
  crush_resist = messages.IntegerField(12)
  lightning_resist = messages.IntegerField(13)
  fire_resist = messages.IntegerField(14)
  encumberance = messages.IntegerField(15)

  ## other properties
  level_requirement = messages.IntegerField(16)
  agility_requirement = messages.IntegerField(17)
  strength_requirement = messages.IntegerField(18)
  wisdom_requirement = messages.IntegerField(19)

  ## TODO:figure out if this will work.
  affixes = messages.MessageField('AffixMessage', 20, repeated=True)

class AffixMessage(messages.Message):
  affix_type = messages.StringField(1, required=True)
  min_value = messages.IntegerField(2)
  max_value = messages.IntegerField(3)