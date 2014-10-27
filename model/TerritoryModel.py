## TerritoryModel.py
from google.appengine.ext import ndb
from protorpc import messages

class TerritoryModel(ndb.Model):
  territory_id = ndb.IntegerProperty(required=True)
  faction = ndb.KeyProperty(kind='FactionModel')
  claiming_guild = ndb.KeyProperty(kind='GuildModel')

  territory_type = ndb.StringProperty(required=True)
  upgrade_level = ndb.IntegerProperty() ## This may get split out into more specific properties.

  ## All of the heroes on the territory, from every faction.
  heroes = ndb.KeyProperty(kind='HeroModel', repeated=True)

class TerritoryMessage(messages.Message):
  territory_id = messages.IntegerField(1, required=True)
  faction = messages.MessageField('FactionMessage', 2)
  claiming_guild = messages.MessageField('GuildMessage', 3)

  territory_type = messages.StringField(4, required=True)
  upgrade_level = messages.IntegerField(5)

  ## All of the heroes on the territory, from every faction.
  heroes = messages.MessageField('HeroMessage', 6, repeated=True)