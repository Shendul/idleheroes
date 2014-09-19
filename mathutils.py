## mathutils.py Contains useful math functions

def getRollFromRange(roll, value_range):
  """
  Takes a roll between 0.0 and 1.0 and gets back the cooresponding value from
  the range.
  Uses Two-Point for equation.
  """
  return int(round(roll*(value_range[1]-value_range[0]) + value_range[0], 0))
