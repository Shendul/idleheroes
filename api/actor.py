## actor.py
from constants import *
from model.hero_model import *

from battle_utils import *
from item_utils import createBaseItem

class Actor():
  """An actor used in the battle simulation.

  Attributes:
      max_hp: the max hp for this actor
      current_hp: the current hp for this actor

      --- Each of these attributes is represented by an AttributePair---
      block_chance: The likelihood that this actor will block an attack.
      dodge_rating: The likelihood that this actor will dodge an attack.
      --- Resists are in a map, with enum keys. ---
      fire_resist: How much fire damage is reduced against this actor.
      ice_resist: How much ice damage is reduced.
      lightning_resist: How much lightning damage is reduced.
      poison_resist: How much poison damage is reduced.
      crush_resist: How much crush damage is reduced.
      thrust_resist: How much thrust damage is reduced.
      slash_resist: How much slash damage is reduced.
      speed: How many action points this actor gets per tick.
      crit_chance: The chance this actor has to critical hit.
      crit_damage_multiplier: The multiplier applied to damage when critting.
      power: How much base damage this hero does.

      action_points: The current number of action points this actor has.
      abilities: A list of Ability objects.
      status_effects: A list of StatusEffect objects.

      name: The actor's name. TODO: Consider adding a unique ID.
      hero_class: The actor's hero class.
      position: The actor's position on the battlefield.

      TODO: Add sprites and other properties that the client will need.
  """

  def __init__(self, heroModel):
    """Creates an actor from a HeroModel"""

    self.hero_class = heroModel.hero_class
    ## Build up the initial attributes from the hero model.
    ## Initialize the intrinsic attributes.
    self.max_hp = heroModel.constitution * HEALTH_CONSTITUTION_MULTIPLIER
    self.current_hp = AttributePair(self.max_hp, self.max_hp)
    self.initializeSpeed()
    self.action_points = 0
    self.initializeCritChanceAndDamage(heroModel)

    ## Add Gear Attributes.
    self.initializeGearAttributes(heroModel)

    ## Build up the abilities list.
    for abilityModel in heroModel.ability_list:
      self.abilities.append(buildActorAbility(abilityModel))

  def applyDamage(self, damages):
    """ Called when the actor takes damage.
        damages: A list of Damage objects.

        This function will apply the appropriate resists and apply the final
        damage to the actor.

        TODO: Actually do the resists logic.
    """
    for damage in damages:
      ## TODO: Add resist logics here
      self.current_hp.current_value -= damage.amount

  def buildActorAbility(AbilityModel):
    """Generate the ActorAbility from the AbilityModel"""
    ## What we want to do here is
    return

  def initializeSpeed(self):
    key = class_properties[self.hero_class] + SPEED_KEY
    base_speed = class_properties[key]
    ## TODO: Error check the base_speed to make sure it got a value.
    self.speed = AttributePair(base_speed, base_speed)

  def initializeCritChanceAndDamage(self, heroModel):
    key = class_properties[self.hero_class] + CRIT_CHANCE_KEY
    crit_chance_multipliers = class_properties[key]
    crit_chance = crit_chance_multipliers[WISDOM] * heroModel.wisdom
    crit_chance += crit_chance_multipliers[AGILITY] * heroModel.agility
    crit_chance += crit_chance_multipliers[STRENGTH] * heroModel.strength
    self.crit_chance = AttributePair(crit_chance, crit_chance)

    crit_damage = BASE_CRIT_DAMAGE_MULTIPLIER
    self.crit_damage_multiplier = AttributePair(crit_damage, crit_damage)

  def initializeGearAttributes(self, heroModel):
    self.resists = {}
    gear_set = {}
    ## Main Hand and Offhand.
    if heroModel.main_hand:
      gear_set['main_hand'] = heroModel.main_hand.get()
      self.power = gear_set['main_hand'].power
    else:
      self.power = 1 # TODO: figure out base power?
    if heroModel.off_hand:
      gear_set['off_hand'] = (heroModel.off_hand.get())
      if gear_set['off_hand'].item_type == SHIELD:
        self.block_chance = off_hand.block_chance
      elif gear_set['off_hand'].item_type in WEAPON_ITEM_TYPES:
        self.power += gear_set['off_hand'].power

    ## Armor Pieces.
    for resist in RESIST_TYPE_LIST:
      self.resists[resist] = AttributePair(0, 0)
    if heroModel.head_armor:
      gear_set['head_armor'] = heroModel.head_armor.get()
    if heroModel.body_armor:
      gear_set['body_armor'] = heroModel.body_armor.get()
    if heroModel.legs_armor:
      gear_set['legs_armor'] = heroModel.legs_armor.get()
    if heroModel.gloves:
      gear_set['gloves'] = heroModel.gloves.get()
    if heroModel.boots:
      gear_set['boots'] = heroModel.boots.get()

    for item_key in gear_set:
      item = gear_set[item_key]
      if item.item_type in ARMOR_ITEM_TYPES:
        for resist in item.resist_list:
          self.resists[resist.resist_type].addToBase(item.resists.resist_amount)
    print 'RESISTS = ' + str(self.resists)


  def updateOffensiveAttributes(self, heroModel):
    pass
