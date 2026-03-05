import rng.pc_character as c

keys = ['Race:','Gender:','Alignment:','Age:','Height:','Weight:','Stats:\tMethod I']
values = []
for i in range(0,7):
    values += [c.char[i]]
char = dict(zip(keys,values))
for key, value in char.items():
    print(f"{key}\n {value}")

import tables.ability_score_tables as tbl

str_tbl = tbl.str_tbl(c.stats[0])
dex_tbl = tbl.dex_tbl(c.stats[1])
con_tbl = tbl.con_tbl(c.stats[2])
# int_tbl = tbl.int_tbl(c.stats[3])
# wis_tbl = tbl.wis_tbl(c.stats[4])
# cha_tbl = tbl.cha_tbl(c.stats[5])
# tables = [str_tbl,dex_tbl,con_tbl,int_tbl,wis_tbl,cha_tbl]
