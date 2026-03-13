import random as rand
from rng.roll_dice import d4, d6, d8

# Method I
def mthd_1():
    return [sum(d6()for _ in range(3)) for _ in range(6)]

# Method II
def mthd_2():
    return [max(sum(d6()for _ in range(3)), sum(d6()for _ in range(3))) for _ in range(6)]

# Method III
def mthd_3():
    stats = [sum(d6()for _ in range(3)) for _ in range(6)]
    rand.shuffle(stats)
    return stats

# Method IV
def mthd_4():
    batch = [sum(d6()for _ in range(3)) for _ in range(12)]
    batch.sort(reverse=True)
    stats = batch[:-6]
    rand.shuffle(stats)
    return stats

# Method V
def mthd_5():
    stats = [sum(sorted([d6()for _ in range(4)])[1:]) for _ in range(6)]
    rand.shuffle(stats)
    return stats

# Method VI
def mthd_6():
    stats = [8]*6
    dice_pool = sorted([d6()for _ in range(7)], reverse=True)
    for die in dice_pool:
        for s in range(6):
            if stats[s] + die <= 18:
                stats[s] += die
                break
    rand.shuffle(stats)
    return stats

# Method VII
def mthd_7():
    stats=[8]*6
    pool=sum(d6()for _ in range(7))
    while True:
        cuts=sorted(rand.choices(range(pool+1),k=5))
        cuts=[0]+cuts+[pool]
        pnts=[cuts[i+1]-cuts[i] for i in range(6)]
        if all(val<=10 for val in pnts):
            return [s + p for s, p in zip(stats, pnts)]

# Method VIII
def mthd_8():
    stats = [8]*6
    pool = sum(d6()for _ in range(7)) + 30
    while True:
        cuts = sorted(rand.choices(range(pool+1),k=5))
        cuts = [0]+cuts+[pool]
        pnts = [(cuts[i+1] - cuts[i]) - 5 for i in range(6)]
        if all(val <= 10 for val in pnts):
            return [s + p for s, p in zip(stats, pnts)]

# Method IX
def mthd_9():
    stats = [3]*6
    pool = sum(d6()for _ in range(13))
    while True:
        cuts = sorted(rand.choices(range(pool+1),k=5))
        cuts = [0]+cuts+[pool]
        pnts = [cuts[i+1]-cuts[i] for i in range(6)]
        if all(val <= 15 for val in pnts):
            return [s + p for s, p in zip(stats, pnts)]

# Method X
def mthd_10():
    batch = [[sum(d6()for _ in range(3)) for _ in range(6)] for _ in range(12)]
    stats = max(batch, key=lambda x: (max(x), sum(x)))
    rand.shuffle(stats)
    return stats

# Method NPC - NOT FOR PLAYERS
# This method is only used on the back end as a population/personality interpreter
weights = {
    mthd_1: 8000, mthd_9: 1000, mthd_7: 500, 
    mthd_5: 250, mthd_2: 125, mthd_6: 60, 
    mthd_8: 30, mthd_4: 15, mthd_10: 5
}

def mthd_npc():
    options = list(weights.keys())
    counts = list(weights.values())
    stats = rand.choices(options, weights=counts, k=1)[0]
    return stats()
