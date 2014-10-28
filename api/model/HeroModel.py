## Hero.py
from google.appengine.ext import ndb
from protorpc import messages

class HeroModel(ndb.Model):
  player = ndb.KeyProperty(kind='PlayerModel')
  hero_name = ndb.StringProperty()

  experience = ndb.IntegerProperty(default=0)
  ## The passive tree is a list of passiveTreeNodes by ID.
  passive_tree = ndb.IntegerProperty(repeated=True)
  ## TODO(dreamlane): figure out how we will represent the ability tree? blob?
  
  ## Equipped gear
  head = ndb.KeyProperty(kind='ItemModel')
  chest = ndb.KeyProperty(kind='ItemModel')
  hands = ndb.KeyProperty(kind='ItemModel')
  feet = ndb.KeyProperty(kind='ItemModel')
  back = ndb.KeyProperty(kind='ItemModel')
  neck = ndb.KeyProperty(kind='ItemModel')
  left_finger = ndb.KeyProperty(kind='ItemModel')
  right_finger = ndb.KeyProperty(kind='ItemModel')
  main_hand = ndb.KeyProperty(kind='ItemModel')
  off_hand = ndb.KeyProperty(kind='ItemModel')

  ## Items in the hero's inventory
  backpack = ndb.KeyProperty(kind='ItemModel', repeated=True)

class HeroMessage(messages.Message):
  hero_name = messages.StringField(1)
  experience = messages.IntegerField(2)
  passive_tree = messages.IntegerField(3)
  ## TODO: figure out how to handle the ability tree

  ## Equipped gear
  head = messages.MessageField('ItemMessage', 4)
  chest = messages.MessageField('ItemMessage', 5)
  hands = messages.MessageField('ItemMessage', 6)
  feet = messages.MessageField('ItemMessage', 7)
  back = messages.MessageField('ItemMessage', 8)
  neck = messages.MessageField('ItemMessage', 9)
  left_finger = messages.MessageField('ItemMessage', 10)
  right_finger = messages.MessageField('ItemMessage', 11)

  backpack = messages.MessageField('ItemMessage', 12, repeated=True)