## team.py
from constants import *

class Team():
  """
    Represents a team as a 3x3 matrix
    The positions have the following indices (column, row):
      0,0  0,1  0,2
      1,0  1,1  1,2
      2,0  2,1  2,2
  """

  def __init__(self):
    """ Start the team off empty """
    self.actors = [[None, None, None], [None, None, None], [None, None, None]]

  def getTargets(self, target_type, target_root):
    """
      Gets the list of targets for the given type and root.
      target_type: integer from constants.py that represents a target type.
      target_root: pair of integers that index the position of the target.

      returns: a list of Actors
    """
    if target_root.length != 2:
      print "ERROR, getTargets called with a bad target_root"

    column = target_root[0]
    row = target_root[1]

    if row < 0 or column < 0 or row > 2 or column > 2:
      print "ERROR, getTargets called with an out of range target_root"

    actor_list = []
    # Single Target Types
    if target_type in SINGLE_TARGET_TYPES:
      return actor_list.append(getActorForPosition(target_root));
    # Row target types
    elif target_type in LINE_TARGET_TYPES:
      for i in range(0,2):
        actor_list.append(getActorForPosition(i, row))
    # Column target types
    elif target_type in COLUMN_TARGET_TYPES:
      for i in range(0,2):
        actor_list.append(getActorForPosition(column, i))
    # Full group target types
    elif target_type in FULL_GROUP_TARGET_TYPES:
      for i in range(0,2):
        for j in range(0,2):
          actor_list.append(getActorForPosition(i,j))

    return actor_list

  def getActorForPosition(self, column, row):
    return self.actors[column][row]

  def putActorInPosition(self, actor, column, row):
    self.actors[column][row] = actor

  def printTeam(self):
    print self.actors

team = Team()
# TODO: build actual actors.
team.putActorInPosition("A", 0, 0)
team.putActorInPosition("B", 0, 2)
team.putActorInPosition("C", 1, 0)
team.putActorInPosition("D", 2, 2)
team.printTeam()
