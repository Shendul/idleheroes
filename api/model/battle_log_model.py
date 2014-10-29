from google.appengine.ext import ndb
from protorpc import messages

class BattleLogModel(ndb.Model):
  """The model for a battle log."""
  events = ndb.StringProperty(repeated=True) 
