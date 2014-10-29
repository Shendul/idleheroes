## PlayerModel.py
from google.appengine.ext import ndb
from protorpc import messages

class PlayerModel(ndb.Model):
  ## TODO: figure out user login and authentication.
  player_name = ndb.StringProperty()
  heroes = ndb.KeyProperty(kind='HeroModel', repeated=True)

  guild = ndb.KeyProperty(kind='GuildModel')
  faction = ndb.KeyProperty(kind='FactionModel')

  stash = ndb.KeyProperty(kind='ItemModel', repeated=True)
  stash_capacity = ndb.IntegerProperty()

  gold = ndb.IntegerProperty()

  ## TODO: add stuff for monetization, and seasons, and other stuff.



class PlayerMessage(messages.Message):
  player_name = messages.StringField(1, required=True)
  heroes = messages.MessageField('HeroMessage', 2, repeated=True)

  guild = messages.MessageField('GuildMessage', 3)
  faction = messages.MessageField('FactionMessage', 4)

  stash = messages.MessageField('ItemMessage', 5, repeated=True)
  stash_capacity = messages.IntegerField(6)

  gold = messages.IntegerField(7)

