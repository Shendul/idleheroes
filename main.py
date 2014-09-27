import logging
import os
import urllib
import datetime
import json

from google.appengine.api import users
from model import *
from userutils import *
from heroclass import *
from itemutils import *
from battle import *
from monster import *
from experience import *

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
        ## TODO consider multiple heros
        quest_time = ih_user.hero[0].get().quest_time
        if quest_time != None:
          template_values['on_quest'] = True
          current_time = datetime.datetime.now()
          time_quested = current_time - quest_time
          template_values['time_quested'] = int(time_quested.total_seconds())

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

class Duel(webapp2.RequestHandler):
  ## TODO: make this a post?
  def get(self):
    ## get the hero actor
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    hero_actor = getBattleActorFromHero(hero)
    user_query = IHUser.query()
    users = user_query.fetch()
    heros = []
    for user in users:
      heros.append(user.hero[0].get())

    ## get the enemy hero actor
    ## Todo: make sure it's not you!
    hero2 = random.choice(heros)
    hero_actor2 = getBattleActorFromHero(hero2)

    ## simulate the battle (ignoring time)
    battle_result = getBattleResult(hero_actor, hero_actor2, False)
    template_values = {
      'pvp_victory': battle_result[0],
      'pvp_log': battle_result[1],
      'pvp_hero': hero_actor
    }
    if battle_result[0]:
      hero.fame += 5
      hero.put()
      template_values['fame_for_winning'] = '5'

    template = JINJA_ENVIRONMENT.get_template('duel.html')
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
  ## These should be post not get, because we are modifying the database.
  ## TODO: read up on post vs get.
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
          # take item base name, grade, and rarity to grab gold value.
          inventory.gold += GOLD_VALUES[item[0]][int(item[1])] * (int(item[2]) + 1)
    inventory.put()
    self.redirect('/items')

class SellCommonItems(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    inventory = hero.inventory.get()
    items = inventory.items
    ## This is probably not safe, but determine the gold ammount gained from selling.
    for item in items:
      if item[2] == '0':
        # Take item base name, grade, and rarity to grab gold value.
        inventory.gold += GOLD_VALUES[item[0]][int(item[1])] * (int(item[2]) + 1)
    ## Update the item list so that the sold items are gone.
    inventory.items = [item for item in items if item[2] != '0']
    ## Write to the data store.
    inventory.put()
    self.redirect('/items')

class SellUncommonItems(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    inventory = hero.inventory.get()
    items = inventory.items
    ## This is probably not safe, but determine the gold ammount gained from selling.
    for item in items:
      if item[2] == '1':
        # Take item base name, grade, and rarity to grab gold value.
        inventory.gold += GOLD_VALUES[item[0]][int(item[1])] * (int(item[2]) + 1)
    ## Update the item list so that the sold items are gone.
    inventory.items = [item for item in items if item[2] != '1']
    ## Write to the data store.
    inventory.put()
    self.redirect('/items')

class Items(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    hero_actor = getBattleActorFromHero(hero)
    inventory = hero.inventory.get()
    items = inventory.items
    display_stats = {
      'gold': inventory.gold, 'exp': hero.experience,
      'level': getHeroLevel(hero.experience), 'hero': hero_actor
    }
    display_items = []
    for item in items:
      display_items.append(getItemFromItemString(item))

    template = JINJA_ENVIRONMENT.get_template('items.html')
    template_values = {'items': display_items, 'stats': display_stats, 'hero': hero_actor}
    self.response.write(template.render(template_values))

class Leaderboard(webapp2.RequestHandler):
  def get(self):
    # Get the user and sort them by exp,lvl, ect
    user_query = IHUser.query()
    users = user_query.fetch()
    heros = []
    for user in users:
      heros.append(user.hero[0].get())
    experience = sorted(heros, key=lambda hero: hero.experience)
    fames = sorted(heros, key=lambda hero: hero.fame)
    gold_list = []
    for hero in heros:
      gold_list.append({'name': hero.name, 'gold': hero.inventory.get().gold})
    gold_list = sorted(gold_list, key=lambda hero: hero['gold'])
    template_values = {
      'heros': experience,
      'fames': fames,
      'gold_list': gold_list
    }
    template = JINJA_ENVIRONMENT.get_template('leaderboard.html')
    self.response.write(template.render(template_values))

class QuestLvlOne(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    current_time = datetime.datetime.now()
    logging.info(current_time)
    hero.quest_time = current_time
    hero.quest = 'A'
    hero.put()
    self.redirect('/')

class QuestLvlTwo(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    current_time = datetime.datetime.now()
    logging.info(current_time)
    hero.quest_time = current_time
    hero.quest = 'B'
    hero.put()
    self.redirect('/')

class QuestLvlThree(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    current_time = datetime.datetime.now()
    logging.info(current_time)
    hero.quest_time = current_time
    hero.quest = 'C'
    hero.put()
    self.redirect('/')

class EndQuest(webapp2.RequestHandler):
  def get(self):
    ih_user = getCurrentIdleHeroesUser(self)
    hero = ih_user.hero[0].get()
    current_time = datetime.datetime.now()
    time_quested = current_time - hero.quest_time
    battles_to_simulate = int(time_quested.total_seconds() / 30)
    hero_actor = getBattleActorFromHero(hero)
    inventory = hero.inventory.get()
    quest_lvl = hero.quest
    if quest_lvl == 'A':
      quest_lvl = LVL_ONE_MOBS
    elif quest_lvl == 'B':
      quest_lvl = LVL_TWO_MOBS
    elif quest_lvl == 'C':
      quest_lvl = LVL_THREE_MOBS
    else:
      quest_lvl = LVL_ONE_MOBS

    quest_log = {}
    quest_log['wins'] = 0
    quest_log['losses'] = 0
    quest_log['xp'] = 0
    quest_log['gold'] = 0

    while battles_to_simulate > 0:
      battles_to_simulate -= 1
      ## get the mob actor
      mob_actor = random.choice(quest_lvl)
      battle_result = getBattleResult(hero_actor, mob_actor, False)
      if battle_result[0]:
        ## victory, so get loot and xp.
        loot_item = generateRandomItem(hero_actor[ACTOR_STAT.MAGIC_FIND],
            mob_actor[ACTOR_STAT.ITEM_LEVEL])
        gold = mob_actor[ACTOR_STAT.GOLD] + hero_actor[ACTOR_STAT.GOLD_FIND]
        inventory.gold += gold
        inventory.items.append(loot_item)
        experience = (mob_actor[ACTOR_STAT.EXP_GAINED] +
            hero_actor[ACTOR_STAT.EXP_BONUS])
        hero.experience += experience
        ## Record victory stats
        quest_log['wins'] += 1
        quest_log['xp'] += experience
        quest_log['gold'] += gold
      else:
        quest_log['losses'] += 1
        ## Record loss stats

    hero.quest_time = None
    inventory.put()
    hero.put()
    template = JINJA_ENVIRONMENT.get_template('questlog.html')
    self.response.write(template.render(quest_log))



application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/banned', Banned),
    ('/heroCreation', CreateHero),
    ('/duel', Duel),
    ('/items', Items),
    ('/equip', EquipItem),
    ('/quest_lvl_one', QuestLvlOne),
    ('/quest_lvl_two', QuestLvlTwo),
    ('/quest_lvl_three', QuestLvlThree),
    ('/end_quest', EndQuest),
    ('/sell', SellItem),
    ('/sell_all_common', SellCommonItems),
    ('/sell_all_uncommon', SellUncommonItems),
    ('/leaderboard', Leaderboard),
], debug=True)