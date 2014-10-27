## WarModel.py
from google.appengine.ext import ndb
from protorpc import messages
from protorpc import message_types

class WarModel(ndb.Model):
  start_time = ndb.DateTimeProperty()
  end_time = ndb.DateTimeProperty()
  ## TODO: add all the stuff that a war needs

class WarMessage(messages.Message):
  start_time = message_types.DateTimeField(1)
  end_time = message_types.DateTimeField(2)
  ## TODO: add all the stuff that a war needs