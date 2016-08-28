## ability.py

class Ability():
  """An ability used in the battle simulation.

  Attributes:
    is_passive: whether or not the ability is a passive ability.
    cooldown: how many turns must pass between usages.
    remaining_cooldown: how many turns until this ability is usable again.
    applies_effects: whether or not the ability applies effects.
    can_miss: whether or not this ability needs to use the accuracy formula.
    accuracy_bonus: the value which is plugged into the accuracy formula to
        determine whether or not the attack is dodged or missed.
    primary_target_type: what the ability can target.
    primary_type: thrust, crush, slash, fire, poison, ice, heal, none, etc.
    primary_range: the min to max amount to apply.
    secondary_type: type of damage/heal for the secondary type.
    secondary_range: the min to max amount to apply.
    secondary_target_type: what the ability can target.
    status_effects: the list of StatusEffectToApply
  """

  buildAbilityForActor()

