import random as rand
from data.races import RACES

def get_weighted_age(race):
    roll = rand.random()
    if roll < 0.35:
        y_roll = rand.random()
        if y_roll < 0.25: return rand.randint(1, int(race.base_age * 0.25))
        if y_roll < 0.75: return rand.randint(int(race.base_age * 0.25) + 1, int(race.base_age * 0.75))
        return rand.randint(int(race.base_age * 0.75) + 1, race.base_age - 1)
    
    if roll < 0.675: return rand.randint(race.base_age, race.mdl_age - 1)
    if roll < 0.8375: return rand.randint(race.mdl_age, race.old_age - 1)
    if roll < 0.935: return rand.randint(race.old_age, race.vnrbl_age - 1)
    return rand.randint(race.vnrbl_age, race.max_age() - 1)

def apply_aging(stats, age, race):
    mods = [0] * 6
    if age < race.base_age:
        mods = [0, 0, 0, -2, -1, -3]
        if age < (race.base_age * 0.75): mods = [sum(x) for x in zip(mods, [-3, -2, -2, 0, -2, 3])]
        if age < (race.base_age * 0.25): mods = [sum(x) for x in zip(mods, [-2, -2, -2, 0, -2, 3])]
    else:
        if age >= race.mdl_age: mods = [sum(x) for x in zip(mods, [-1, 0, -1, 1, 1, 0])]
        if age >= race.old_age: mods = [sum(x) for x in zip(mods, [-2, -2, -1, 0, 1, 0])]
        if age >= race.vnrbl_age: mods = [sum(x) for x in zip(mods, [-1, -1, -1, 1, 1, 0])]

    new_stats = []
    for i, s in enumerate(stats):
        low_lim, high_lim = race.limits[i]
        modified = s + mods[i]
        # Wisdom (index 4) doesn't have a floor of low_lim during aging for some AD&D 2E variants, 
        # but we follow your previous logic for consistency.
        val = max(0, modified) if i == 4 and age >= race.base_age else max(low_lim, min(high_lim, modified))
        if age < race.base_age: val = max(1, min(high_lim, modified))
        new_stats.append(val)
    return new_stats