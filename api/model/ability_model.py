from google.appengine.ext import ndb
from protorpc import messages

class AbilityModel(ndb.Model):
  # Which ability it is. Note that this is an integer used like an enum.
  ability_type = ndb.IntegerProperty()
  # What level the ability is.
  level = ndb.IntegerProperty()

  ## TODO... add ability details

