## monster.py This file is used to represent all monster related data and
## functions.

from battle import *

class MONSTER:
  """
  This class is used to represent an enumlike object. All monster data will be
  held here.
  """
  def makeMobActor(health, defense, accuracy, thrust_resistance, slash_resistance,
      crush_resistance, lightning_resistance, fire_resistance, cold_resistance,
      poison_resistance, thrust_damage, slash_damage, crush_damage, lightning_damage,
      fire_damage, cold_damage, poison_damage, thorns_damage, name, loot_table, item_level):
    """ Takes the mob parameters and returns a mob actor. """
    return {
      ACTOR_STAT.HEALTH: health,
      ACTOR_STAT.DEFENSE: defense,
      ACTOR_STAT.ACCURACY: accuracy,
      ACTOR_STAT.THRUST_RESISTANCE: thrust_resistance,
      ACTOR_STAT.SLASH_RESISTANCE: slash_resistance,
      ACTOR_STAT.CRUSH_RESISTANCE: crush_resistance,
      ACTOR_STAT.LIGHTNING_RESISTANCE: lightning_resistance,
      ACTOR_STAT.FIRE_RESISTANCE: fire_resistance,
      ACTOR_STAT.COLD_RESISTANCE: cold_resistance,
      ACTOR_STAT.POISON_RESISTANCE: poison_resistance,
      ACTOR_STAT.THRUST_DAMAGE: thrust_damage,
      ACTOR_STAT.SLASH_DAMAGE: slash_damage,
      ACTOR_STAT.CRUSH_DAMAGE: crush_damage,
      ACTOR_STAT.LIGHTNING_DAMAGE: lightning_damage,
      ACTOR_STAT.FIRE_DAMAGE: fire_damage,
      ACTOR_STAT.COLD_DAMAGE: cold_damage,
      ACTOR_STAT.POISON_DAMAGE: poison_damage,
      ACTOR_STAT.THORNS_DAMAGE: thorns_damage,
      ACTOR_STAT.NAME: name,
      # ACTOR_STAT.LOOT_TABLE: loot_table,
      ACTOR_STAT.ITEM_LEVEL: item_level,
    }

  RAT = makeMobActor(
      20, # Health
      20, # Defense
      20, # Accuracy
      0, # Thrust Resist
      5, # Slash Resist
      5, # Crush Resist
      0, # Lightning Resist
      0, # Fire Resist
      5, # Cold Resist
      10, # Poison Resist
      None, # Thrust Damage
      (2, 6), # Slash Damage
      None, # Crush Damage
      None, # Lightning Damage
      None, # Fire Damage
      None, # Cold Damage
      None, # Poison Damage
      None, # Thorns Damage
      "Rat", # Name
      None, # Loot Table
      2, # Item Level
  )
  SNAKE = makeMobActor(
      18, # Health
      30, # Defense
      45, # Accuracy
      5, # Thrust Resist
      0, # Slash Resist
      5, # Crush Resist
      0, # Lightning Resist
      0, # Fire Resist
      0, # Cold Resist
      10, # Poison Resist
      (1,3), # Thrust Damage
      None, # Slash Damage
      None, # Crush Damage
      None, # Lightning Damage
      None, # Fire Damage
      None, # Cold Damage
      (1, 3), # Poison Damage
      None, # Thorns Damage
      "Snake", # Name
      None, # Loot Table
      3, # Item Level
  )
  WOLF = makeMobActor(
      45, # Health
      30, # Defense
      45, # Accuracy
      0, # Thrust Resist
      0, # Slash Resist
      8, # Crush Resist
      0, # Lightning Resist
      0, # Fire Resist
      10, # Cold Resist
      20, # Poison Resist
      (2, 8), # Thrust Damage
      (1, 2), # Slash Damage
      (1, 4), # Crush Damage
      None, # Lightning Damage
      None, # Fire Damage
      None, # Cold Damage
      None, # Poison Damage
      None, # Thorns Damage
      "Wolf", # Name
      None, # Loot Table
      5, # Item Level
  )
  BEAR = makeMobActor(
      60, # Health
      25, # Defense
      45, # Accuracy
      0, # Thrust Resist
      0, # Slash Resist
      15, # Crush Resist
      0, # Lightning Resist
      0, # Fire Resist
      15, # Cold Resist
      10, # Poison Resist
      None, # Thrust Damage
      (5, 15), # Slash Damage
      (2, 6), # Crush Damage
      None, # Lightning Damage
      None, # Fire Damage
      None, # Cold Damage
      None, # Poison Damage
      None, # Thorns Damage
      "Bear", # Name
      None, # Loot Table
      8, # Item Level
  )

## TODO: Create lists of mobs to choose from, and figure out how to organize them.
ALL_MOBS = [MONSTER.RAT, MONSTER.SNAKE, MONSTER.WOLF, MONSTER.BEAR]
