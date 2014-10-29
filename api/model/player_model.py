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
  premium_currency = ndb.IntegerProperty()
  total_premium_currency_obtained = ndb.IntegerProperty()

  ## TODO: add stuff for monetization, and seasons, and other stuff.
