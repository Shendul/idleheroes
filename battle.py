## battle.py This file is used to represent all battle related stat data
## and functions.
## Design Doc: https://docs.google.com/document/d/1EmIQz0fRDnnqGYtvmfnVC5c-eysI_uO8yo1zqyA_TY4/edit#heading=h.in14ampaoaji

import math
import random
import mathutils

class ACTOR_STAT:
  """
  This class is used to represent an enumlike object for stats, used by mobs
  and heroes, referred to in code as an actor.
  An actor is a participant of a battle.
  The main hero attributes are not shown here, because they are used to
  calculate some of the actor stats, but are not themselves stats that are
  needed bay an actor.
  """
  HEALTH = "health"
  # MANA = "mana" ## TODO: implement Mana
  # BLOCK = 'block' ## TODO: implement blocking
  DEFENSE = "defense" # Represents how easy you take a hit.
  ACCURACY = "accuracy" # Represents how easy you hit something.
  THRUST_RESISTANCE = "thrust_resistance"
  SLASH_RESISTANCE = "slash_resistance"
  CRUSH_RESISTANCE = "crush_resistance"
  LIGHTNING_RESISTANCE = "lightning_resistance"
  FIRE_RESISTANCE = "fire_resistance"
  COLD_RESISTANCE = "cold_resistance"
  POISON_RESISTANCE = "poison_resistance"

  ## Damages: Each will be a min-max tuple
  THRUST_DAMAGE = "thrust_damage"
  SLASH_DAMAGE = "slash_damage"
  CRUSH_DAMAGE = "crush_damage"
  LIGHTNING_DAMAGE = "lightning_damage"
  FIRE_DAMAGE = "fire_damage"
  COLD_DAMAGE = "cold_damage"
  POISON_DAMAGE = "poison_damage"
  THORNS_DAMAGE = "thorns_damage"

  ## Meta stats
  GOLD_FIND = "gold_find"  # Should be a multiplier (float)
  MAGIC_FIND = "magic_find"  # Should be an integer
  # KARMA = 'karma'
  # FAME = 'fame'
  # EXP_BONUS = "exp_bonus"  ## TODO: implement exp gain
  NAME = "name"
  # LOOT_TABLE = "loot_table" ## TODO: implement loot tables
  ITEM_LEVEL = "item_level"

  # ABILITIES ##TODO: Implement abilities

  # In Battle stats
  CURRENT_HP = "current_hp"

ATTACK_DAMAGE_LIST = [
  ACTOR_STAT.THRUST_DAMAGE, ACTOR_STAT.SLASH_DAMAGE,
  ACTOR_STAT.CRUSH_DAMAGE, ACTOR_STAT.LIGHTNING_DAMAGE,
  ACTOR_STAT.FIRE_DAMAGE, ACTOR_STAT.COLD_DAMAGE,
  ACTOR_STAT.POISON_DAMAGE]

DAMAGE_TYPE_TO_RESIST_MAP = {
  ACTOR_STAT.THRUST_DAMAGE: ACTOR_STAT.THRUST_RESISTANCE,
  ACTOR_STAT.SLASH_DAMAGE: ACTOR_STAT.SLASH_RESISTANCE,
  ACTOR_STAT.CRUSH_DAMAGE: ACTOR_STAT.CRUSH_RESISTANCE,
  ACTOR_STAT.LIGHTNING_DAMAGE: ACTOR_STAT.LIGHTNING_RESISTANCE,
  ACTOR_STAT.FIRE_DAMAGE: ACTOR_STAT.FIRE_RESISTANCE,
  ACTOR_STAT.COLD_DAMAGE: ACTOR_STAT.COLD_RESISTANCE,
  ACTOR_STAT.POISON_DAMAGE: ACTOR_STAT.POISON_RESISTANCE
}

def getBattleResult(hero_actor, mob_actor, debug_mode):
  """ Returns True if the player wins, or False if the player loses."""
  ## Initialize the actors' current HP
  hero_actor[ACTOR_STAT.CURRENT_HP] = hero_actor[ACTOR_STAT.HEALTH]
  mob_actor[ACTOR_STAT.CURRENT_HP] = mob_actor[ACTOR_STAT.HEALTH]
  battle_going = True
  turn = 0
  battle_log = []
  while battle_going:
    turn += 1
    battle_log.append("<br/>Turn number: " + str(turn))
    battle_log.append("------")
    ## Simulate Hero attack on Mob
    simulateAttack(hero_actor, mob_actor, battle_log)
    if mob_actor[ACTOR_STAT.CURRENT_HP] <= 0:
      ## TODO: Handle hero victory
      battle_going = False
      battle_log.append("HERO kills MOB")
      if debug_mode:
        print battle_log
      return (True, '<br/>'.join(battle_log), mob_actor[ACTOR_STAT.NAME])
    simulateAttack(mob_actor, hero_actor, battle_log)
    if hero_actor[ACTOR_STAT.CURRENT_HP] <= 0:
      battle_going = False
      battle_log.append("MOB kills HERO")
      if debug_mode:
        print battle_log
      return (False, '<br/>'.join(battle_log), mob_actor[ACTOR_STAT.NAME])


def simulateAttack(attacker, defender, battle_log):
  chance = getChanceToHit(attacker[ACTOR_STAT.ACCURACY], defender[ACTOR_STAT.DEFENSE])
  roll = random.random()
  if roll < chance:
    battle_log.append(attacker[ACTOR_STAT.NAME] + " has hit " + defender[ACTOR_STAT.NAME] +
        " Roll: " + str(roll) + " chance: " + str(chance))
    ## roll for raw damage
    damage_roll = random.random()
    damage = getHitDamage(attacker, defender, damage_roll, battle_log)
    battle_log.append(attacker[ACTOR_STAT.NAME] + " deals " + str(damage) + " damage to " + 
        defender[ACTOR_STAT.NAME])
    battle_log.append(defender[ACTOR_STAT.NAME] + " has " + 
        str(defender[ACTOR_STAT.CURRENT_HP] - damage) + " HP remaining")
    defender[ACTOR_STAT.CURRENT_HP] -= damage
  else:
    battle_log.append(attacker[ACTOR_STAT.NAME] + " has missed " + defender[ACTOR_STAT.NAME] + 
        ". Roll: " + str(roll) + " chance: " + str(chance))

def getChanceToHit(attack, defense):
  return attack/(attack+(math.pow(defense ,0.8)))

def getHitDamage(attacker, defender, damage_roll, battle_log):
  """ Determine hit damage using a damage roll, attacker stats, and defender resists. """
  result = 0
  for damage_type in ATTACK_DAMAGE_LIST:
    if attacker[damage_type] != None:
      raw = mathutils.getRollFromRange(damage_roll, attacker[damage_type])
      ## TODO: Determine actually resists equations, for now it's straight %.
      damage = int(round(raw - (raw * (defender[DAMAGE_TYPE_TO_RESIST_MAP[damage_type]]/100.0)), 0))
      result += damage
      battle_log.append("Attacker Deals: " + str(damage) + " " + damage_type)
  return result

