import endpoints

from google.appengine.ext import ndb
from protorpc import messages
from protorpc import message_types
from protorpc import remote

## models
from model import (
    BattleLogModel,
    FactionModel,
    GuildModel,
    HeroModel,
    ItemModel,
    PlayerModel,
    QuestModel,
    TerritoryModel,
    TerritoryPathModel,
    WarModel)


## TODO: Move this to it's own file
class CreateHeroCommandRequest(messages.Message):
  """
  This class contains the request data model that is sent to the API when the client wants to create
  a hero.
  """
  hero_name = messages.StringField(1, required=True)
  ## TODO: dreamlane figure out how to authenticate.
  player_key = messages.StringField(2, required=True)
  starting_passive_node = messages.IntegerField(3, required=True)
  class Weapon(messages.Enum):
    SWORD = 1
    BOW = 2
    WAND = 3
  starting_weapon = messages.EnumField(Weapon, 4, required=True)

class CreateHeroCommandResponse(messages.Message):
  """
  This class contains the response data model that is returned from the command used to create a
  hero.
  """
  result = messages.BooleanField(1) ## True if successful, false if unsuccessful
  ## Todo: add an error field, so that we can send back a useful error message to the client.

@endpoints.api(name='idle-heroes', version='v0.1',
               description='API for Idle Heroes')
class IdleHeroesApi(remote.Service):

  @endpoints.method(CreateHeroCommandRequest, CreateHeroCommandResponse,
                    name='hero.create',
                    path='hero',
                    http_method='POST')
  def create_hero(self, request):
    # Perform the hero creation.
    # Step 1: Get the right player model
    print request
    player = ndb.Key('PlayerModel', request.player_key)

    # Step 2: Set up the new hero model

    # Step 3: validate the data (name collision? hacks?)

    # Step 4: save the HeroModel and PlayerModel (make an entity group for 1 transaction?)

    # Step 5: return the successful result
    return False


application = endpoints.api_server([IdleHeroesApi])
