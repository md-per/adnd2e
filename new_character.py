import random as rand
from dice import d
from races import dwarf, elf, gnome, halfelf, halfling, human
RACES = (dwarf, elf, gnome, halfelf, halfling, human)
from tables import ability_tbls as tbl

# Player Character Generation Flowchart

# Step 1: Roll Ability Scores
# a) Indicade dice-rolling method
#   Method I
def method_i():
    scores = [sum(d(6) for _ in range(3)) for _ in range(6)]
    return scores
#   Method II - Method VI
#
# b) Record Generated Scores
new_scores = (method_i())
# Step 2: Chose a Race
# a) Requirements
#    Validate eligeble races
valid = [
    i for i, mod in enumerate(RACES) 
    if all(low <= val <= high for val, (low, high) in zip(new_scores, mod.limits))
]
#    Choosing a Race
race_idx = rand.choice(valid)
race = RACES[race_idx]
# b) Adjust Ability Scores
#    Adjustments    #
adj = race.adjust
mod_scores = [t + m for t, m in zip(new_scores, adj)]
# Default to modified (young) scores
fnl_scores = mod_scores.copy()

# c) Racial Abilities

# d) Determine Alignment, Gender, Height, Weight, age and aging effects

# di)
#   Alignment
order = ['Lawful','Neutral','Chaotic']
moral = ['Good','Neutral','Evil']
o_idx = rand.randrange(3)
m_idx = rand.randrange(3)
align_idx = (o_idx,m_idx)
if o_idx == 1 and m_idx == 1:
    align = 'True Neutral'
else:
    align = f'{order[o_idx]} {moral[m_idx]}'
# dii)
#   Gender
binary = ['Male','Female']
sex_idx = rand.randrange(len(binary))
gender = binary[sex_idx]
# diii)
#   Height
height = race.base_ht[sex_idx] + race.mod_ht
# div)
#   Weight
weight = race.base_wt[sex_idx] + race.mod_wt
# dv)
#   Age and Aging Effects
age = race.base_age + race.mod_age
#   Maximum Age
max_age = race.max_age
#   Middle Age
mdl_age = race.mdl_age
mdl_age_mod = [-1,0,-1,1,1,0]
mdl_age_scores = fnl_scores.copy()
for i in range(0,6):
    if i == 4:
        mdl_age_scores[i] += mdl_age_mod[i]
        continue
    low, high = race.limits[i]
    mdl_age_scores[i] += mdl_age_mod[i]
    mdl_age_scores[i] = max(low, min(high, mdl_age_scores[i]))
#   Old Age
old_age = race.old_age
old_age_mod = [-2,-2,-1,0,1,0]
old_age_scores = mdl_age_scores.copy()
for i in range(0,6):
    if i == 4:
        old_age_scores[i] += old_age_mod[i]
        continue
    low, high = race.limits[i]
    old_age_scores[i] += old_age_mod[i]
    old_age_scores[i] = max(low, min(high, old_age_scores[i]))
#   Venerable Age
vnrbl_age = race.vnrbl_age
vnrbl_age_mod = [-1,-1,-1,1,1,0]
vnrbl_age_scores = old_age_scores.copy()
for i in range(0,6):
    if i == 4:
        vnrbl_age_scores[i] += vnrbl_age_mod[i]
        continue
    low, high = race.limits[i]
    vnrbl_age_scores[i] += vnrbl_age_mod[i]
    vnrbl_age_scores[i] = max(low, min(high, vnrbl_age_scores[i]))
# Applying Age Effect Modifiers
life_stages = [
    (vnrbl_age, vnrbl_age_scores),
    (old_age, old_age_scores),
    (mdl_age, mdl_age_scores)
]
for threshold, stage_scores in life_stages:
    if age >= threshold:
        fnl_scores = stage_scores
        break
scores = tuple(fnl_scores)
# e) Determin Ability Tables
#   Strength Table
str_tbl = tbl.str_tbl(scores[0])
#   Dexterity Table
dex_tbl = tbl.dex_tbl(scores[1])
#   Constitution Table
con_tbl = tbl.con_tbl(scores[2])
#   Inteligence Table
int_tbl = tbl.int_tbl(scores[3])
#   Wisdom Table
wis_tbl = tbl.wis_tbl(scores[4])
#   Charisma Table
cha_tbl = tbl.cha_tbl(scores[5])
# Step 3: 


char = [race.race,gender,align,f"{age} years",f"{height}'",f"{weight} lbs.",scores,str_tbl,dex_tbl,con_tbl,int_tbl,wis_tbl,cha_tbl]
for i in char:
    print(i)