from google.appengine.ext import ndb
from protorpc import messages

class TerritoryPathModel(ndb.Model):
  """Model for world map territory paths."""
  territory_path_id = ndb.IntegerProperty(required=True)
  path_type = ndb.StringProperty(required=True)
  distance = ndb.IntegerProperty(required=True)
  upgrade_level = ndb.IntegerProperty()
