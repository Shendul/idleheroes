from google.appengine.ext import ndb
from protorpc import messages
from protorpc import message_types

class QuestModel(ndb.Model):
  quest_type = ndb.StringProperty(required=True)

  ## This is like a tier level, no related to hero level etc.
  quest_level = ndb.IntegerProperty(required=True)

  staging_start_time = ndb.DateTimeProperty(required=True)
  quest_start_time = ndb.DateTimeProperty(required=True)

  ## The quest end time is optional, since some quests do not have set end times.
  quest_end_time = ndb.DateTimeProperty()

  max_heroes = ndb.IntegerProperty()
  heroes = ndb.KeyProperty(kind='HeroModel')

  ## Todo: determine if the model needs to know about fame requirements...
