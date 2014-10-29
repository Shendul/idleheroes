import endpoints

from google.appengine.ext import ndb

from protorpc import messages
from protorpc import message_types
from protorpc import remote

from model.guild_model import *
from model.player_model import *

class CreateGuildCommandRequest(messages.Message):
  """
  This class contains the request data model that is sent to the API when the client wants to create
  a Guild.
  """
  guild_name = messages.StringField(1, required=True)
  ## TODO: dreamlane figure out how to authenticate, and how to get the player_key.
  player_key = messages.StringField(2, required=True) ## This is the guild leader

class CreateGuildCommandResponse(messages.Message):
  """
  This class contains the response data model that is returned from the command used to create a
  Guild.
  """
  success = messages.BooleanField(1) ## True if successful, false if unsuccessful
  error = messages.StringField(2)

@endpoints.api(name='guild', version='v0.1',
               description='API for Guild')
class GuildApi(remote.Service):

  @endpoints.method(CreateGuildCommandRequest, CreateGuildCommandResponse,
                    name='guild.create',
                    path='guild',
                    http_method='POST')
  def create_guild(self, request):
    ## todo: Figure out the right way to get the player, I don't think ndb.Key is right?
    player = ndb.Key(urlsafe=request.player_key).get()

    ## Validate the name
    ## TODO: Add bad_words name validation here.
    ## TODO: Add illegal_characters name validation here.
    ## TODO: Add name length validation here.
    for guild in GuildModel.query().fetch(projection=[GuildModel.guild_name]):
      if guild.guild_name == request.guild_name:
        error_message = 'Guild name already taken.'
        return CreateGuildCommandResponse(success=False, error=error_message)

    ## todo: if there is a cost to create a guild, check to see if the player has enough gold.

    ## The name is valid so make the guild, and set the player's guild to the newly created one.
    ## TODO: Figure out how to determine the faction, should it be the player's faction, or should
    ## it be a field in the request?
    new_guild = GuildModel(
      players=[player.key],
      leader=player.key,
      guild_name=request.guild_name
    )

    ## todo: if there is a cost to create a guild, remove gold cost from player.

    ## This will replace their old guild if they have one.
    player.guild = new_guild.put()
    player.put()
    return CreateGuildCommandResponse(success=True)
