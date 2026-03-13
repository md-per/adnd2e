from . import dwarf, elf, gnome, halfelf, halfling, human
from rng.roll_dice import d4, d6, d8, d10, d12, d20, d100

DICE_FUNCS = {
    'd4': d4,
    'd6': d6,
    'd8': d8,
    'd10': d10,
    'd12': d12,
    'd20': d20,
    'd100': d100}

RACES = [
    dwarf,
    elf,
    gnome,
    halfelf,
    halfling,
    human
]

for race in RACES:
    race.__dict__.update(DICE_FUNCS)