from google.appengine.api import users
from model import *

def getCurrentIdleHeroesUser():
  #Make sure there is a user.
  if users.get_current_user():
    idle_heroes_user_query = IHUser.query(IHUser.user_id ==
        users.get_current_user().user_id())
    idle_heroes_user = None
    if idle_heroes_user_query.count() == 0:
      # The IHUser does not exist, so we make one.
      idle_heroes_user = IHUser()
      user = users.get_current_user()
      idle_heroes_user.user = user.user_id()
      idle_heroes_user.display_name = user.nickname()
      idle_heroes_user.put()
    else:
      idle_heroes_user = idle_heroes_user_query.fetch(1)[0]

    return idle_heroes_user
    
  # There is no currently logged in user. Fail. TODO: add grace!
  else:
    return None