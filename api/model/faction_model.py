## FactionModel.py
from google.appengine.ext import ndb
from protorpc import messages

class FactionModel(ndb.Model):
  guilds = ndb.KeyProperty(kind='GuildModel', repeated=True)
  leader = ndb.KeyProperty(kind='GuildModel', required=True)
  ## Todo: add properties for all other faction things (resources, territory, upgrades, etc)
