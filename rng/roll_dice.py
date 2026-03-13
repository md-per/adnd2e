import random as rand

def d(sides):
    return rand.randint(1,sides)

d4 = lambda: d(4)
d6 = lambda: d(6)
d8 = lambda: d(8)
d10 = lambda: d(10)
d12 = lambda: d(12)
d20 = lambda: d(20)
d100 = lambda: ((d10()-1)*10)+d10()