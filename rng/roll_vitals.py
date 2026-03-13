import random as rand
from data.races import RACES

def get_vitals(race):
    sex_idx = rand.randrange(2)
    gender = ['Male', 'Female'][sex_idx]
    age = race.base_age + race.mod_age()
    death = race.max_age()
    height = race.base_ht[sex_idx] + race.mod_ht()
    weight = race.base_wt[sex_idx] + race.mod_wt()
    order = ['Lawful', 'Neutral', 'Chaotic']
    moral = ['Good', 'Neutral', 'Evil']
    o_idx, m_idx = rand.randrange(3), rand.randrange(3)
    align = 'True Neutral' if o_idx == 1 and m_idx == 1 else f'{order[o_idx]} {moral[m_idx]}'
    return gender, age, height, weight, align, death