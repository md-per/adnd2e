# pyright: reportUndefinedVariable=false

name = 'Gnome'

# Ability Scores
limits = ((6,18), (3,18), (8,18), (6,18), (3,18), (3,18))
adjust = (0, 0, 0, 1, -1, 0)

# Height
base_ht = (38, 36)
mod_ht = lambda: d6()

# Weight
base_wt = (72, 68)
mod_wt = lambda: sum(d4() for _ in range(5))

# Age
base_age = 60
mod_age = lambda: sum(d12() for _ in range(3))

# Maximum Age
max_age = lambda: 200 + sum(d100() for _ in range(3))

# Aging Thresholds
mdl_age, old_age, vnrbl_age = 100, 133, 200