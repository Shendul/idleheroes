from google.appengine.ext import ndb
from protorpc import messages

class TerritoryPathModel(ndb.Model):
  """Model for world map territory paths."""
  territory_path_id = ndb.IntegerProperty(required=True)
  path_type = ndb.StringProperty(required=True)
  distance = ndb.IntegerProperty(required=True)
  upgrade_level = ndb.IntegerProperty()

class TerritoryPathMessage(messages.Message):
  """Message for world map territory paths."""
  territory_path_id = messages.IntegerField(1, required=True)
  path_type = messages.StringField(2, required=True)
  distance = messages.IntegerField(3, required=True)
  upgrade_level = messages.IntegerField(4)
