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
  NEXT AVAILABLE CHAR: 'A'
  """

DONT_DIE = 'A'
FAST_COMPLETION = 'B'

def quest_objective_grade(
    objective_discription, fame):
  return {
    'objective_discription': objective_discription,
    'fame': fame
    # TODO: Add rewards somehow
  }

OBJECTIVE_GRADES = {
  ## TODO: Balance these
    OBJECTIVE.DONT_DIE: [
    quest_objective_grade('Less Than Five Deaths', 1) # Grade 0
    quest_objective_grade('Less Than Three Deaths', 50)  # Grade 1
    ]


  def rollForObjective():
  ## We use a power law here for the roll.
  ## Rather than a uniform distribution, high rolls are much harder to get.
  ## Increasing the power here decreases the strength of rolls.
  ## Example: if random() returns a .750000 (a highish roll) a power of 3
  ## reduces this roll to a .421875.
  ## Current rough distribution: 
  ##   0-.25: 63%
  ##   .25-.50: 16%
  ##   .50-.75: 11%
  ##   .75-.100: 9% (.95-.100: 1.7%)
  ## This means roughly 79% of rolls will be less than half of the possible
  ##     value on objectives, and only about 1 in 50 rolls will max an objective.
  ## This will make perfect quests extremely rare, and therefore we can make them
  ##     extremely powerful.
  ## If we increase from a power of three, we make lower rolls more common, and
  ##    higher rolls more rare.
  return math.pow(random.random(), 3)

def generateObjective(fame, base_quest):
  """
  This function is used to generate an objective based on fame.
  It returns a string representation of the objective
  """
  if fame < 1:
    print 'error generating objective, fame must be greater than 0'
    return None
  result = ''
  # Get the quest objective class for this quest
  quest_objective_class_key = base_quest
  quest_objective_class = AFFIX_GRADES[quest_objective_class_key]
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
  quest_objective_grade = quest_objective_class[objective][objective_grade_index]

  ## Roll for values
  roll = rollForObjective()
  minRoll, maxRoll = quest_objective_grade['minValueRange']
  # Two-Point form equation maps the rolled number to the objective value range.
  # We round the result to the nearest whole number.
  value = int(round((roll-0.0)*(maxRoll-minRoll) + minRoll, 0))
  if quest_objective_grade['maxValue'] != None:
    # Roll the max
    roll = rollForObjective()
    minRoll = value + 1
    maxRoll = quest_objective_grade['maxValue']
    maxValue = int(round((roll-0.0)*(maxRoll-minRoll) + minRoll, 0))
    result += format(value, "03d") + format(maxValue, "03d")
    return result
  else :
    result += format(value, "06d")
    return result  
