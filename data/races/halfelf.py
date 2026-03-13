# pyright: reportUndefinedVariable=false

name = 'Half-Elf'

# Ability Scores
limits = ((3,18), (6,18), (6,18), (4,18), (3,18), (3,18))
adjust = (0, 0, 0, 0, 0, 0)

# Height
base_ht = (60, 58)
mod_ht = lambda: sum(d6() for _ in range(2))

# Weight
base_wt = (110, 85)
mod_wt = lambda: sum(d12() for _ in range(3))

# Age
base_age = 15
mod_age = lambda: d6()

# Maximum Age
max_age = lambda: 125 + sum(d20() for _ in range(3))

# Aging Thresholds
mdl_age, old_age, vnrbl_age = 62, 83, 125