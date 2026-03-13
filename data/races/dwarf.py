# pyright: reportUndefinedVariable=false

name = 'Dwarf'

# Ability Scores
limits = ((8,18), (3,17), (11,18), (3,18), (3,18), (3,17))
adjust = (0, 0, 1, 0, -1, 0)

# Height
base_ht = (43, 41)
mod_ht = lambda: d10()

# Weight
base_wt = (130, 105)
mod_wt = lambda: sum(d10() for _ in range(4))

# Age
base_age = 40
mod_age = lambda: sum(d10() for _ in range(5))

# Maximum Age
max_age = lambda: 250 + sum(d100() for _ in range(2))

# Aging Thresholds
mdl_age, old_age, vnrbl_age = 125, 167, 250