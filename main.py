import endpoints

from google.appengine.ext import ndb
from protorpc import messages
from protorpc import message_types
from protorpc import remote

## apis
from api import (
  HeroApi,
  PlayerApi)


## TODO: Move this to it's own file



application = endpoints.api_server([
    HeroApi.HeroApi,
    PlayerApi.PlayerApi
])
