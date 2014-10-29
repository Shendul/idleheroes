import endpoints

from google.appengine.ext import ndb

from protorpc import messages
from protorpc import message_types
from protorpc import remote

from model.hero_model import *
from model.item_model import *
from model.player_model import *

from item.item_rarities import *
from item.item_types import *
from item.item_bases import *

class CreateHeroCommandRequest(messages.Message):
  """
  This class contains the request data model that is sent to the API when the client wants to create
  a hero.
  """
  hero_name = messages.StringField(1, required=True)
  ## TODO: dreamlane figure out how to authenticate, and how to get the player_key.
  player_key = messages.StringField(2, required=True)
  starting_passive_node = messages.IntegerField(3, required=True)
  starting_weapon = messages.StringField(4, required=True)

class CreateHeroCommandResponse(messages.Message):
  """
  This class contains the response data model that is returned from the command used to create a
  hero.
  """
  success = messages.BooleanField(1) ## True if successful, false if unsuccessful
  error = messages.StringField(2)

@endpoints.api(name='hero', version='v0.1',
               description='API for Heroes')
class HeroApi(remote.Service):

  @endpoints.method(CreateHeroCommandRequest, CreateHeroCommandResponse,
                    name='hero.create',
                    path='hero',
                    http_method='POST')
  def create_hero(self, request):
    # Perform the hero creation.
    # Step 1: Get the right player model
    ## TODO figure out how to actually get the player_key and auth it.
    player = ndb.Key(urlsafe=request.player_key).get()

    # Step 2: validate the data (name collision? hacks?)
    ## TODO: Add bad_words name validation here.
    ## TODO: Add illegal_characters name validation here.
    ## TODO: Add name length validation here.
    for h in player.heroes:
      if h.get().hero_name == request.hero_name:
        error_message = 'Player already has a hero with that name.'
        return CreateHeroCommandResponse(success=False, error=error_message)
    ## todo: verify that the request.starting_weapon is a legit starting weapon.

    # Step 3: Set up the new hero model
    heroModel = HeroModel(
      hero_name=request.hero_name,
      passive_tree=[request.starting_passive_node],
      main_hand=createStartingWeapon(request.starting_weapon),
      player=player
    )

    # Step 4: save the HeroModel and PlayerModel.
    ## Todo: determine if HeroModel and PlayerModel should be in one entity group to allow for a
    ## single transaction.
    player.heroes.append(heroModel.put())
    player.put()

    # Step 5: return the successful result
    return CreateHeroCommandResponse(success=True)

def createStartingWeapon(item_type):
  """ Creates a starting weapon of the given type. """
  weapon = ItemModel()
  weapon.item_type = item_type
  weapon.item_rarity = ITEM_RARITY.COMMON

  weapon_base = getBaseItem(item_type, 1)
  weapon.item_name = weapon_base['name']
  weapon.action_point_cost = weapon_base['action_point_cost']
  weapon.min_damage = weapon_base['min_damage']
  weapon.max_damage = weapon_base['max_damage']
  weapon.auto_attack_damage_type = weapon_base['auto_attack_damage_type']
  weapon.item_level = 1

  return weapon.put()