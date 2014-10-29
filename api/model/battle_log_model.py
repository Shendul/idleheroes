from google.appengine.ext import ndb
from protorpc import messages

class BattleLogModel(ndb.Model):
  """The model for a battle log."""
  events = ndb.StringProperty(repeated=True) 

class BattleLogMessage(messages.Message):
  """The message for the BattleLog model. """
  ## TODO(dreamlane): decide what an event really is.
  events = messages.StringField(1, repeated=True)
