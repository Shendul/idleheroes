## quest.py This file is used to store all quest data

class QUEST:
  """
  This class maps the base quest types to their quest model characters.
  """
  # Quests that increase Karma
  RESCUE_MISSION = 'A' ## Kill mobs to get to a person needing rescue.
  TRAIN = 'B' ## Timed mission, help train someone weaker than you.
  SLAY_THE_BOSS = 'C' ## Fight through mobs to get to BIG mob.
  ARREST_CRIMINAL =  'D' ## Timed mission based off of rolls to find person, fight
                         ## mobs as you go. Subdue enemy
  # Quests that are Neutral
  DEFEND_THE_CARAVAN = 'E' ## Timed mission, defend until destination reached.
  CLEAR_OUT_MONSTER_NEST = 'F' ## Kill certain amount of mobs.
  DUNGEON_CRAWL = 'G' ## Random amount of mobs/ time to complete. High loot.
  FIND_RARE_MATERIAL = 'H' ## search for material for a merchant, rare loot.
  # Quests that decrease Karma
  RAID_NEUTRAL = 'I' ## fight humans for loot.
  BEG_FOR_LOOT = 'J' ## timed: no fighting.
  STEAL = 'K' ## rolls based off of agility or something. No fighting.
  ATTRACT_MONSTERS = 'L' ## timed: fight mobs
  SUMMON_ENEMIES = 'M' ## same as above.

GOOD_QUESTS = [
  QUEST.RESCUE_MISSION, QUEST.TRAIN, QUEST.SLAY_THE_BOSS,
  QUEST.ARREST_CRIMINAL
]

NEUTRAL_QUESTS = [
  QUEST.DEFEND_THE_CARAVAN, QUEST.CLEAR_OUT_MONSTER_NEST, QUEST.DUNGEON_CRAWL,
  QUEST.FIND_RARE_MATERIAL
]

BAD_QUESTS = [
    QUEST.RAID_NEUTRAL, QUEST.BEG_FOR_LOOT, QUEST.STEAL, QUEST.ATTRACT_MONSTERS,
    QUEST.SUMMON_ENEMIES
  ]

ALL_QUEST_TYPES = GOOD_QUESTS + NEUTRAL_QUESTS + BAD_QUESTS

def quest_grade(name, fame):
  return {'name': name, 'fame': fame}

# TODO: add more grades.
QUEST_GRADES = {
  QUEST.RESCUE_MISSION: [
    quest_grade('Save The Town Idiot', 1), 
  ],
  QUEST.TRAIN: [
    quest_grade('Train Town Watchdog', 1), 
  ],
  QUEST.SLAY_THE_BOSS: [
    quest_grade('Kill Local Grizzly', 1), 
  ],
  QUEST.ARREST_CRIMINAL: [
    quest_grade('Catch a Thief', 1), 
  ],
  QUEST.DEFEND_THE_CARAVAN: [
    quest_grade('Accompany Local Merchant', 1), 
  ],
  QUEST.CLEAR_OUT_MONSTER_NEST: [
    quest_grade('Destroy Rat Nest', 1), 
  ],
  QUEST.DUNGEON_CRAWL: [
    quest_grade('Explore Cave', 1), 
  ],
  QUEST.FIND_RARE_MATERIAL: [
   quest_grade('Find Gold', 1), 
  ],
  QUEST.RAID_NEUTRAL: [
    quest_grade('Raid Farmer\'s Barn For Loot', 1), 
  ],
  QUEST.BEG_FOR_LOOT: [
    quest_grade('Beg Like a Homeless Man', 1), 
  ],
  QUEST.STEAL: [
    quest_grade('Steal From Beggars', 1), 
  ],
  QUEST.ATTRACT_MONSTERS: [
    quest_grade('Bait Rats Into The Town', 1), 
  ],
  QUEST.SUMMON_ENEMIES: [
    quest_grade('Attempt Demonic Ritual', 1), 
  ]
}

class QUEST_RARITY:
  COMMON = '0'
  UNCOMMON = '1'
  RARE = '2'

QUEST_RARITY_DISPLAY_NAME = {
  '0': 'Common', # NO Affixes
  '1': 'Uncommon', # 1-2 Affixes
  '2': 'Rare' # 3-6 Affixes
  ## TODO: Add more rarities
}