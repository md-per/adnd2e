# pyright: reportUndefinedVariable=false

name = 'Human'

# Ability Scores
limits = ((3,18), (3,18), (3,18), (3,18), (3,18), (3,18))
adjust = (0, 0, 0, 0, 0, 0)

# Height
base_ht = (60, 59)
mod_ht = lambda: sum(d10() for _ in range(2))

# Weight
base_wt = (140, 100)
mod_wt = lambda: sum(d10() for _ in range(6))

# Age
base_age = 15
mod_age = lambda: d4()

# Maximum Age
max_age = lambda: 90 + sum(d20() for _ in range(2))

# Aging Thresholds
mdl_age, old_age, vnrbl_age = 45, 60, 90