## battlestats.py This file is used to represent all battle related stat data
## and functions.

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
  # EXP_BONUS = "exp_bonus"  ## TODO: implement exp gain
  NAME = "name"
  # LOOT_TABLE = "loot_table" ## TODO: implement loot tables

  # ABILITIES ##TODO: Implement abilities