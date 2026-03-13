# pyright: reportUndefinedVariable=false

name = 'Elf'

# Ability Scores
limits = ((3,18), (6,18), (7,18), (8,18), (3,18), (8,18))
adjust = (0, 1, -1, 0, 0, 0)

# Height
base_ht = (55, 50)
mod_ht = lambda: d10()

# Weight
base_wt = (90, 70)
mod_wt = lambda: sum(d10() for _ in range(3))

# Age
base_age = 100
mod_age = lambda: sum(d6() for _ in range(5))

# Maximum Age
max_age = lambda: 350 + sum(d100() for _ in range(4))

# Aging Thresholds
mdl_age, old_age, vnrbl_age = 175, 233, 350