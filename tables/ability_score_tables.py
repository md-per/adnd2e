# Strength Table
hitprob = [-5,-3,-3,-2,-1]+[0]*5+[1]*3+[2]*3+[3]*3+[4,4,5,6,7]
dmgadjust = [-4,-2,-1,-1]+[0]*5+[1,1,2,3,3]+list(range(4,13))+[14]
wghtallow = [1,1,5,10,20,35,40,45,55,70,85,110,135,160,185,235,335,485,535,635,785,935,1235,1535]
maxpress = [3,5,10,25,55,90,115,140,170,195,220,255,280,305,330,380,480,640,700,810,970,1130,1440,1750]
opendrs = [1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,[15,3],[16,6],[16,8],[17,10],[17,12],[18,14],[18,16],[19,17],[19,18]]
bndbarlftgate = [0]*5+[1,2,4]+list(range(7,14,3))+[16]+list(range(20,41,5))+list(range(50,91,10))+[95,99]
strength = [hitprob,dmgadjust,wghtallow,maxpress,opendrs,bndbarlftgate]
def str_tbl(stat):
    mod = 0
    tbl = []
    if isinstance(stat, int):
        pos = stat-1
        if stat >= 4 and stat <= 18:
            pos = 3
            if stat > 5 and stat < 16:
                mod = list(range(4,16))
                mod = (mod.index(stat))//2
            elif 16 <= stat and stat <= 18:
                pos = 9
                if stat > 16:
                    mod = [16,17,18]
                    mod = (mod.index(stat))
            elif stat >= 19:
                pos = 17
                if stat > 19:
                    mod = list(range(19,26))
                    mod = (mod.index(stat))
    else:
        pos = 12
        mod = 0
        ex_str = stat[1]
        if ex_str > 50 and ex_str < 100:
            bottom = [51,76,91,100]
            x = 0
            while ex_str in range(bottom[x],ex_str+1):
                mod += 1
                x += 1
        else:
            pos = 16
    pos += mod
    for i in strength:
        line = i[pos]
        tbl += [line]
    return tbl

# Dexteritiy Table
react = [-6]+list(range(-4,0))+[0]*6+[1,2,2,3,3,4,4,4,5,5]
missile = react
defence = [5]+list(reversed(range(1,6)))+[0]*4+[-1,-2,-3]+[-4]*3+[-5]*3+[-6,-6]
dexterity = [react, missile, defence]
def dex_tbl(stat):
    pos = stat-1
    tbl = []
    if stat > 6 and stat <= 14:
        pos = 6
    elif stat > 14:
        pos = stat-5
    for i in dexterity:
        line = i[pos]
        tbl += [line]
    return tbl

# Constitution Table
hp_adj = [-3,-2,-2]+[-1]*3+[0]*8+[1]+[2]*9
# For Warrior Classes
# if 'Class' == 'Warrior':
    # hp_adj = hp_adj[16:]
    # hp_adj += [3,4,5,5]+[6]*3+[7,7]
sys_shock = list(range(25,86,5))+[0.88,0.90,0.95,0.97]+[0.99]*7+[1]
res_survive = list(range(3,91,5))+list(range(92,99,2))+[1]*8
psn_save = [-2,-1]+[0]*16+[1,1,2,2,3,3,4]
regen = [0]*19+list(range(6,0,-1))
constitution = [hp_adj,sys_shock,res_survive,psn_save,regen]
def con_tbl(stat):
    pos = stat-1
    tbl = []
    for i in constitution:
        line = i[pos]
        tbl += [line]
    return tbl