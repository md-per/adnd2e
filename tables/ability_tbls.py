# Strength Table
hitprob = (-5,-3,-3,-2,-1)+(0,)*5+(1,)*3+(2,)*3+(3,)*3+(4,4,5,6,7)
dmgadjust = (-4,-2,-1,-1)+(0,)*5+(1,1,2,3,3)+tuple(range(4,13))+(14,)
wghtallow = (1,1,5,10,20,35,40,45,55,70,85,110,135,160,185,235,335,485,535,635,785,935,1235,1535)
maxpress = (3,5,10,25,55,90,115,140,170,195,220,255,280,305,330,380,480,640,700,810,970,1130,1440,1750)
opendrs = ((1,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,3),(16,6),(16,8),(17,10),(17,12),(18,14),(18,16),(19,17),(19,18))
bndbarlftgate = (0,)*5+(1,2,4)+tuple(range(7,16,3))+(16,)+tuple(range(20,45,5))+tuple(range(50,100,10))+(95,99)
strength = (hitprob,dmgadjust,wghtallow,maxpress,opendrs,bndbarlftgate)
def str_tbl(stat):
    if isinstance(stat,int):
        if stat <= 3:
            pos = stat-1
        elif stat <= 15:
            pos = ((stat-4)//2)+3
        elif stat <= 18:
            pos = stat-7
        else:
            pos = stat-2
    else:
        perc = stat[1]
        if perc <= 50:
            pos = 12
        elif perc <= 75:
            pos = 13
        elif perc <= 90:
            pos = 14
        elif perc <= 99:
            pos = 15
        else:
            pos = 16
    return tuple(i[pos] for i in strength)

# Dexteritiy Table
react = (-6,-4,-3,-2,-1,0,0,0,1,2,2,3,3,4,4,4,5,5)
missile = react
defence = (5,5,4,3,2,1,0,-1,-2,-3,-4,-4,-4,-5,-5,-5,-6,-6)
dexterity = (react,missile,defence)
def dex_tbl(stat):
    if stat <= 6:
        pos = stat-1
    elif stat > 6 and stat <= 14:
        pos = 6
    else:
        pos = stat-8
    return tuple(i[pos] for i in dexterity)

# Constitution Table
hp_adj          = [-3,-2,-2]+[-1]*3+[0]*8+[1]+[2]*9
# if pc_class == 'Warrior':
#     hp_adj    = hp_adj[:16]+[3,4,5,5]+[6]*3+[7,7]
hp_adj          = tuple(hp_adj)
sys_shock       = tuple(x/100 for x in tuple(range(25,86,5))+(88,90,95,97)+(99,)*7+(100,))
res_survive     = tuple(x/100 for x in tuple(range(30,91,5))+tuple(range(92,99,2))+(100,)*8)
psn_save        = (-2,-1,)+(0,)*16+(1,1,2,2,3,3,4)
regen           = (0,)*19+tuple(range(6,0,-1))
constitution    = tuple(zip(hp_adj,sys_shock,res_survive,psn_save,regen))
def con_tbl(stat):
    return constitution[stat]

# Intelligence Table
numlang         = (0,0,0,0,1,1,1,1,1,2,2,2,3,3,4,4,5,6,7,8,9,10,11,12,15,20)
spllvl          = (0,0,0,0,0,0,0,0,0,4,5,5,6,6,7,7,8,8,9,9,9,9,9,9,9,9)
chnc2lrnspll    = (0,0,0,0,0,0,0,0,0,35,40,45,50,55,60,65,70,75,85,95,96,97,98,99,100,100)
max_spllvl      = (0,0,0,0,0,0,0,0,0,6,7,7,7,9,9,11,11,14,18,99,99,99,99,99,99,99) # 99 = All
spll_imm_int    = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7) # 1 = 1st level Illusions
intelligence    = tuple(zip(numlang,spllvl,chnc2lrnspll,max_spllvl,spll_imm_int))
def int_tbl(stat):
    return intelligence[stat]

# Wisdom Table
mdef_adj        = (0,0,0,-3,-2,-1,-1,-1,0,0,0,0,0,0,0,1,2,3,4,4,4,4,4,4,4,4)
spellfail       = (0,80,60,50,45,40,35,30,25,20,15,10,5,0,0,0,0,0,0,0,0,0,0,0,0,0)
# bns_spll stores the total number of bonus slots per level: (1st,2nd,3rd,4th,5th)
bns_spll        = (0,0,0,0,0,0,0,0,0,0,0,0,0,(1,0,0,0,0),(2,0,0,0,0),(2,1,0,0,0),(2,2,0,0,0),(2,2,1,0,0),(2,2,1,1,0),(3,2,1,1,1),(3,2,1,1,2,0,0),(3,2,1,1,2,1,0),(3,2,1,1,2,2,0),(3,2,1,1,2,2,1),(3,2,1,1,2,2,2),(3,2,1,1,2,2,3))
spll_imm        = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7) # 1 = Immunity to specific charms
wisdom          = tuple(zip(mdef_adj,spellfail,bns_spll,spll_imm))
def wis_tbl(stat):
    return wisdom[stat]

# Charisma Table
max_hench       = (0,0,0,1,1,2,2,3,3,4,4,4,5,5,6,7,8,10,15,20,25,30,35,40,50,100)
lyl_base        = (0,0,0,-30,-25,-20,-15,-10,-5,0,0,0,0,5,10,15,20,30,40,50,60,70,80,90,100,150)
react_adj       = (0,0,0,-25,-20,-15,-10,-5,0,0,0,0,0,5,10,15,25,30,35,40,45,50,55,60,70,100)
charisma        = tuple(zip(max_hench,lyl_base,react_adj))
def cha_tbl(stat):
    return charisma[stat]