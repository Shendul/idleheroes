import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from model.player_model import *

class CreatePlayerCommandRequest(messages.Message):
  """
  This class contains the request data model that is sent to the API when the client wants to create
  a player.
  """
  player_name = messages.StringField(1, required=True)
  ## TODO: dreamlane figure out how to authenticate.

class CreatePlayerCommandResponse(messages.Message):
  """
  This class contains the response data model that is returned from the command used to create a
  player.
  """
  success = messages.BooleanField(1) ## True if successful, false if unsuccessful
  error = messages.StringField(2)

@endpoints.api(name='player', version='v0.1',
               description='API for Players')
class PlayerApi(remote.Service):

  @endpoints.method(CreatePlayerCommandRequest, CreatePlayerCommandResponse,
                    name='player.create',
                    path='player',
                    http_method='POST')
  def create_player(self, request):
    # Check to see if the playername is valid
    ## TODO: Create common validators, don't make them inline here.
    ## TODO: Add bad_words name validation here.
    ## TODO: Add illegal_characters name validation here.
    ## TODO: Add name length validation here.
    players = PlayerModel.query()
    for p in players.fetch():
      if p.player_name == request.player_name:
        error_message = 'Could not create player, name already in use.'
        return CreatePlayerCommandResponse(success=False, error=error_message)

    # Perform the player creation.
    player = PlayerModel(player_name=request.player_name)
    player.put()
    ## Todo: validate that the put worked

    return CreatePlayerCommandResponse(success=True)
