## GuildModel.py
from google.appengine.ext import ndb
from protorpc import messages

class GuildModel(ndb.Model):
  players = ndb.KeyProperty(kind='PlayerModel', repeated=True)
  leader = ndb.KeyProperty(kind='PlayerModel', required=True)
  faction = ndb.KeyProperty(kind='FactionModel') ## Not required, just in case we want outlaw guilds
  guild_name = ndb.StringProperty(required=True)
  ## Todo: add properties for anything that a guild might need (banner, claimed territory, etc)
