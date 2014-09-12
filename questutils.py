## questutils.py
##
## The quest model is as follows:
## A variable length case sensitive string where the first 6 characters give the
## overview of the quest, and the following n*7 characters give mod information,
## where n == number of modifiers (affixes).
##
## The first 6 indices represent the following properties:
## 0. Quest type: Rescue mission, Dungeon Crawl, Raid, or whatever
## 1. Fame_grade: the grade of fame the player has.
##     This will grow from 0 to E or something, where each grade represents a
##     new quest of the same type.
## 2. Rarity: Common (White), Uncommon (Blue), Rare (Yellow), etc
## 3. Bonus_objective_count: The amount of bonus objectives the quest has.
##      These objectives will be things like "Die less than 5 times." or
##      "Complete within 30 mins" and so on.
## 4. TODO: Add rewards system
##
## Here is an example Common (White) quest:
##     A0001
##     The first char (A) tells us it is a Rescue Mission (A = RESCUE_MISSION)
##     The second char (0) tells us its grade is 0 (Save the Town Idiot).
##     The next char (0) tells us that the quest is common (White).
##     The next char (0) tells us that there are no bonus objectives.
##     This final char (1) TODO: set up rewards, should be loot drop amount
##     some of which are automatically uncommon or rare and some kind of gold roll.
##     So the quest is a Common (White) Rescue Mission.

from bonusobjectives import *
from quest import *
import random
import math

# TODO: make fame a requirement for higher grades.
def generateRandomQuest(fame):
  """
  Generates a random quest, and returns the quest's model string.
  """
  if fame < 1:
    print 'error generating quest, fame must be greater than 0'
    return None
  result = ''
  base_quest = None
  possible_grades = []
  while True:
    karma_roll = random.random()
    if karma_roll < .25:
      base_quest = random.choice(BAD_QUESTS)
    elif karma_roll > .75:
      base_quest = random.choice(GOOD_QUESTS)
    else:
      base_quest = random.choice(NEUTRAL_QUESTS)
    # Get the list of possible grades, if none, repick.
    highest_grade = -1
    for quest_grade in QUEST_GRADES[base_quest]:
      if fame >= quest_grade['fame']:
       highest_grade += 1
    if highest_grade > -1:
      result = base_quest # Set the first char of the string.
      break;
    else:
      continue

## Pick the base quest grade
  quest_grade = random.randint(0, highest_grade)
  result += format(quest_grade, 'x') # Second character of the string = grade

  ## Determine rarity
  rarity_roll = random.random()

  # TODO: adjust rarities, and add more rarities
  quest_rarity = QUEST_RARITY.COMMON
  if rarity_roll > .90:
    quest_rarity = QUEST_RARITY.RARE
  elif rarity_roll > .70:
    quest_rarity = QUEST_RARITY.UNCOMMON
  result += quest_rarity # Third Character of the string = rarity

  ## Determine number of bonus objectives on the quest.
  bonus_objective_count = 0
  if quest_rarity == QUEST_RARITY.RARE:
    bonus_objective_count = random.randint(2, 4)
  elif quest_rarity == QUEST_RARITY.UNCOMMON:
    bonus_objective_count = random.randint(1, 2)
  result += str(bonus_objective_count) # 4th char of the string = bonus obj num

  ## Generate the bonus objective strings
  bonus_objectives = []
  while (bonus_objective_count > 0):
    bonus_objectives.append(generateBonusObjective(fame, base_quest))
    bonus_objective_count -= 1

  ## Build the bonus objective strings into the quest.
  for objective in bonus_objectives:
    result += objective
  return result

print generateRandomQuest(1)
