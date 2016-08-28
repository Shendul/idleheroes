## battle_utils.py
import constants

class AttributePair():
  """ A class to hold the current and base attribute values. """

  def __init__ (self, base, current):
    self.base_value = base
    self.current_value = current

  def addToBase(self, amount):
    """ To be used only when initializing values."""
    if (self.base_value != self.current_value):
      print "AddToBase WAS USED WHEN IT SHOULD NOT HAVE BEEN!"
      return
    self.base_value += amount
    self.current_value += amount

  def __str__(self):
    return "base: " + str(self.base_value) + ", current: " + str(self.current_value)

class Damage():
  """ A class to hold the damage type and amount. """

  def __init__ (self, damage_type, amount):
    self.damage_type = damage_type
    self.amount = amount
