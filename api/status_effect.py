## status_effect.py

class StatusEffect():
  """
    This class represents a status effect that applies to an actor and modifies
    thier stats over time.
    Attributes:
      type: HoT/DoT, AttributeModifier, etc...
      primary_type: what type of damage/heal it does per tick.
      primary_range: what the min and max amount to apply per tick are.
      effect: function to perform on the actor TODO: think about this more.
  """

