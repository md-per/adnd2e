import random as rand
import pandas as pd
from .roll_stats import mthd_npc
from .roll_vitals import get_vitals
from data.races import RACES
from data.campaign.tally_npc import export_npc_pop

def create_pop(count, gen_name):
    print(f"Generating {count} NPCs for '{gen_name}'...")
    headers = ['Race', 'Sex', 'Age', 'Weight', 'Height', 'Alignment', 'Stats', 'Power', 'Death']
    
#################################################################
# START OF FIX: CLEAN GENERATION (NO LIVE TALLYING)
#################################################################
    lists = {gen_name: []}

    for _ in range(count):
        raw_stats = mthd_npc()
        pwr = sum(raw_stats)

        # Race selection based on stats
        val_races = [r for r in RACES if all(s <= high for s, (_, high) in zip(raw_stats, r.limits))]
        race = rand.choice(val_races) if val_races else RACES[0]
        r_name = "Half-Elf" if race.name.lower() == "half-elf" else race.name
        
        # Apply racial adjustments
        r_stats = [s + a for s, a in zip(raw_stats, race.adjust)]
        gender, age, height, weight, align, death = get_vitals(race)
        
        stats_str = f"[ {', '.join(str(s).zfill(2) for s in r_stats)} ]"        
        
        # Store as clean row; the Printer will handle the rest
        row = [f"{r_name}: ", gender, age, weight, height, align, stats_str, f"{pwr} pts.", death]
        lists[gen_name].append(row)

    # Trigger the Printer/Auditor
    export_npc_pop(lists, gen_name, matrix={})
#################################################################
# END OF FIX
#################################################################

    return pd.DataFrame(lists[gen_name], columns=headers)

