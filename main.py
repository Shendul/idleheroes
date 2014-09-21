import logging
import os
import urllib

from google.appengine.api import users
from model import *
from userutils import *
from heroclass import *
from itemutils import *
from battle import *
from monster import *

import jinja2
import webapp2

import random


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
      ih_user = getCurrentIdleHeroesUser(self)
      # Check to see if the user has a hero
      if len(ih_user.hero) == 0:
        template_values['no_hero'] = True
      else:
        pass

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
    ih_user = getCurrentIdleHeroesUser(self)
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
    # TODO: Add the class selection to the form once we support other classes.
    hero.hero_class = HERO_CLASS.WARRIOR
    ih_user.hero.append(hero.put())
    ih_user.put()
    self.redirect("/")

class GenerateItem(webapp2.RequestHandler):
  def get(self):
    item = getItemFromItemString(generateRandomItem(0, 12))
    template = JINJA_ENVIRONMENT.get_template('itembutton.html')
    template_values = {'item': item}
    self.response.write(template.render(template_values))

class Battle(webapp2.RequestHandler):
  ## TODO: make this a post?
  def get(self):
    ## get the hero actor
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    hero_actor = getBattleActorFromHero(hero)

    ## get the mob actor
    mob_actor = random.choice(ALL_MOBS)
    ## simulate the battle (ignoring time)
    battle_result = getBattleResult(hero_actor, mob_actor, False)
    template_values = {
      'victory': battle_result[0],
      'log': battle_result[1],
      'enemy': battle_result[2]
    }
    if battle_result[0]:
      ## victory, so get an item.
      loot_item = generateRandomItem(0, mob_actor[ACTOR_STAT.ITEM_LEVEL])
      template_values['item_for_winning'] = getItemFromItemString(loot_item)
      inventory = hero.inventory.get()
      inventory.items.append(loot_item)
      inventory.put()

    template = JINJA_ENVIRONMENT.get_template('home.html')
    self.response.write(template.render(template_values))

class EquipItem(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    inventory = hero.inventory.get()
    item = self.request.get('item')
    if item != None:
      # NOTE: because this is a prototype, we leave the item in the inventory.
      equipItem(inventory, item)
    self.redirect('/items')

class SellItem(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    inventory = hero.inventory.get()
    items = inventory.items
    sell_item = self.request.get('item')
    if sell_item != None:
      for item in items:
        if sell_item == item:
          items.remove(item)
          inventory.items = items
          inventory.put()
    self.redirect('/items')


class Items(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    inventory = hero.inventory.get()
    items = inventory.items
    display_items = []
    for item in items:
      display_items.append(getItemFromItemString(item))

    template = JINJA_ENVIRONMENT.get_template('items.html')
    template_values = {'items': display_items}
    self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/banned', Banned),
    ('/heroCreation', CreateHero),
    ('/generateItem', GenerateItem),
    ('/battle', Battle),
    ('/items', Items),
    ('/equip', EquipItem),
    ('/sell', SellItem),
], debug=True)