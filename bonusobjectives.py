## bonusobjectives.py
## This file represents all of the data associated with bonus objectives.

from quest import *
import random
import math

class OBJECTIVE:
  """
  This class maps the base bonus objective type to a character that will be 
  used in the quest string.
  Uncomment each objective after implementation for the objective is completed.
  NEXT AVAILABLE CHAR: 'D'
  """
  ## quests with mobs
  DONT_DIE = 'A' ## stay under certain amount of deaths, or health loss.
  FAST_COMPLETION = 'B' ## Complete the quest within a time limit.
  STRONGER_MOBS = 'D' ## increases max mob level that can spawn.
  MORE_MOBS = 'E' ## increase the amount of monsters that can spawn.

  ## quests without mobs
  LONGER_JOB = 'C' ## add time req to complete the quest

QUEST_OBJECTIVE_CLASS = {
  QUEST.RESCUE_MISSION: 'mob',
  QUEST.TRAIN: 'mob',
  QUEST.SLAY_THE_BOSS: 'mob' ,
  QUEST.ARREST_CRIMINAL: 'mob',
  QUEST.DEFEND_THE_CARAVAN: 'mob',
  QUEST.CLEAR_OUT_MONSTER_NEST: 'mob',
  QUEST.DUNGEON_CRAWL:  'mob',
  QUEST.FIND_RARE_MATERIAL:  'mob',
  QUEST.RAID_NEUTRAL:  'mob',
  QUEST.ATTRACT_MONSTERS: 'mob',
  QUEST.SUMMON_ENEMIES: 'mob',

  QUEST.BEG_FOR_LOOT: 'non_mob',
  QUEST.STEAL: 'non_mob'
}

def quest_objective_grade(
    objective_discription, fame):
  return {
    'objective_discription': objective_discription,
    'fame': fame
    # TODO: Add rewards somehow
  }

OBJECTIVE_GRADES = {
  'mob': {
    OBJECTIVE.DONT_DIE: [
      quest_objective_grade('Less Than Five Deaths', 1), # Grade 0
      quest_objective_grade('Less Than Three Deaths', 50)  # Grade 1
    ],
    OBJECTIVE.FAST_COMPLETION: [
      quest_objective_grade('Like a Turtle', 1), # Grade 0 (75%)
      quest_objective_grade('Like a Wolf', 50)  # Grade 1 (60%)
    ],
    OBJECTIVE.STRONGER_MOBS: [
      quest_objective_grade('+2 to mob level', 1), # Grade 0
      quest_objective_grade('+4 to mob level', 50)  # Grade 1
    ],
    OBJECTIVE.MORE_MOBS: [
      quest_objective_grade('25% more mobs', 1), # Grade 0
      quest_objective_grade('50% more mobs', 50)  # Grade 1
    ]
  },

  'non_mob': {
    OBJECTIVE.LONGER_JOB: [
      quest_objective_grade('30 more minutes!', 1), # Grade 0
      quest_objective_grade('Give me another hour!', 50)  # Grade 1
    ]
  }

}

def generateBonusObjective(fame, base_quest):
  """
  This function is used to generate an objective based on fame.
  It returns a string representation of the objective
  """
  if fame < 1:
    print 'error generating objective, fame must be greater than 0'
    return None
  result = ''
  # Get the quest objective class for this quest
  quest_objective_class_key = QUEST_OBJECTIVE_CLASS[base_quest]
  quest_objective_class = OBJECTIVE_GRADES[quest_objective_class_key]
  ## Get the objective and grade.
  while True:
    objective = random.choice(list(quest_objective_class.keys()))
    highest_grade = -1
    for objective_grade in quest_objective_class[objective]:
      if fame >= objective_grade['fame']:
        highest_grade += 1
    if highest_grade > -1:
      result = objective # Set the first char of the string.
      break;
    else:
      continue
  
  ## pick the grade
  objective_grade_index = random.randint(0, highest_grade)
  result += format(objective_grade_index, 'x') # 2nd char of the objective = grade.
  return result  