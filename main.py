import endpoints

## apis
from api import (
  guild_api,
  hero_api,
  player_api)

application = endpoints.api_server([
    guild_api.GuildApi,
    hero_api.HeroApi,
    player_api.PlayerApi
])
