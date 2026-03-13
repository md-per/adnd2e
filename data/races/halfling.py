# pyright: reportUndefinedVariable=false

name = 'Halfling'

# Ability Scores
limits = ((7,18), (7,18), (10,18), (6,18), (3,17), (3,18))
adjust = (-1, 1, 0, 0, 0, 0)

# Height
base_ht = (32, 30)
mod_ht = lambda: sum(d8() for _ in range(2))

# Weight
base_wt = (52, 48)
mod_wt = lambda: sum(d4() for _ in range(5))

# Age
base_age = 20
mod_range = 3
mod_age = lambda: sum(d4() for _ in range(3))

# Maximum Age
max_age = lambda: 100 + d100()

# Aging Thresholds
mdl_age, old_age, vnrbl_age = 50, 67, 100