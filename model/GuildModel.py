## GuildModel.py
from google.appengine.ext import ndb
from protorpc import messages

class GuildModel(ndb.Model):
  players = ndb.KeyProperty(kind='PlayerModel', repeated=True)
  leader = ndb.KeyProperty(kind='PlayerModel', required=True)
  ## Todo: add properties for anything that a guild might need (banner, claimed territory, etc)

class GuildMessage(messages.Message):
  players = messages.MessageField('PlayerMessage', 1, repeated=True)
  leader = messages.MessageField('PlayerMessage', 2, required=True)
  ## Todo: add messages for anything that a guild might need (banner, claimed territory, etc)
