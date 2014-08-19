import logging
import os
import urllib

from google.appengine.api import users
from model import *
from userutils import *
from heroclass import *

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

banlist = ['103099184899327574218', '103609145815541722591', '116366841012077067118',
    '102020407303120382619', '106902801820123927692']

"""
  The Request Handlers.
"""  
class MainPage(webapp2.RequestHandler):
  def get(self):
    if users.get_current_user():
      template_values = {}
      template_values['url_linktext'] = 'Logout'
      template_values['url'] = users.create_logout_url(self.request.uri)
      #Ignore the banned nerds
      if users.get_current_user().user_id() in banlist:
        return self.redirect('/banned')
      ih_user = getCurrentIdleHeroesUser()
      # Check to see if the user has a hero
      if len(ih_user.hero) == 0:
        template_values['no_hero'] = True
      else:
        # TODO(dreamlane): consider cases where the get fails.
        template_values['hero'] = getHeroValues(ih_user.hero[0].get())

      template_values['display_name'] = ih_user.display_name
      template = JINJA_ENVIRONMENT.get_template('home.html')
      self.response.write(template.render(template_values))

    else:
      # The user is not logged in, show a login button.
      login_url = users.create_login_url(self.request.uri)
      template_values = {'login_url': login_url}
      template = JINJA_ENVIRONMENT.get_template('login.html')
      self.response.write(template.render(template_values))

class Banned(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('banned.html')
    self.response.write(template.render())

class CreateHero(webapp2.RequestHandler):
  def post(self):
    ih_user = getCurrentIdleHeroesUser()
    if ih_user == None:
      # TODO(dreamlane): Redirect to a useful place.
      return self.redirect('/abyss')
      logging.exception('Could not get user on hero creation!')
    hero_name = self.request.get('hero_name')
    if hero_name:
      if len(hero_name) > 30:
        logging.exception("Garrett prolly tried to make a long name.")
        return self.redirect("/abyss")
    # Create the hero in the ndb
    inventory = Inventory()
    inventory.items = []
    hero = Hero()
    hero.name = hero_name
    hero.inventory = inventory.put()
    hero.battle_history = []
    ih_user.hero.append(hero.put())
    ih_user.put()
    self.redirect("/")


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/banned', Banned),
    ('/heroCreation', CreateHero)
], debug=True)