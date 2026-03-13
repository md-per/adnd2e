import os
import pandas as pd
import random as rand
#######################################################################
import multiprocessing
#######################################################################
from rng import roll_npc, roll_settlement

def main():
    """High-Level Campaign Controller."""
    base_path = "data/campaign"
    os.makedirs(base_path, exist_ok=True)
    
    # Scan for folders
    existing = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f)) and not f.startswith('__')]
    
    print("\n--- CAMPAIGN SELECTION ---")
    print(" 0. [CREATE NEW]")
    for i, folder in enumerate(existing, 1):
        print(f" {i}. {folder}")
    
    choice = input("\nSelect: ").strip()
    gen_name = input("Enter name: ").strip() if choice == "0" else existing[int(choice)-1]

    path = os.path.join(base_path, gen_name, "npc_population", f"{gen_name}_Prime.xlsx")

    # Load or Generate
    #######################################################################
    # df = pd.read_excel(path) if os.path.exists(path) else roll_npc.create_pop(5000, gen_name) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if os.path.exists(path):
        df = pd.read_excel(path)
    else:
        pop_size = rand.randint(5000, 1048575)
        print(f"Generating new kingdom with population: {pop_size}...")
        df = roll_npc.create_pop(pop_size, gen_name)
    #######################################################################

    type_map = {"A":"Thorp", "B":"Hamlet", "C":"Village", "D":"Small Town", "E":"Large Town", "F":"Small City", "G":"Large City", "H":"Metropolis"}

    #######################################################################
    # MULTI-CORE PRE-PLANNING
    #######################################################################
    tasks = []
    temp_df = df.copy()

    while True:
        valid_df = temp_df.dropna(how='all')
        pop_left = len(valid_df)
        if pop_left == 0: break

        # Calculate Settlement Type
        full_ranges = {"A":(1,100), "B":(80,400), "C":(400,1000), "D":(900,2000), "E":(2000,5000), "F":(5001,12000), "G":(12001,25000), "H":(25001,pop_left)}
        available = [k for k, v in full_ranges.items() if pop_left >= v[0]]
        picked = rand.choice(available)
        
        low, high = full_ranges[picked]
        
        # Determine unique slice for this core
        pop_size = rand.randint(low, high)
        if len(valid_df) < pop_size: pop_size = len(valid_df)
        
        set_chunk = valid_df.sample(n=pop_size)
        temp_df.loc[set_chunk.index, :] = None # Pluck in main thread memory
        
        set_num = len(tasks) + 1
        name = f"Set.{set_num}-{type_map[picked]}"
        
        # Package for pool: (DF_Slice, Campaign, Set_Name, Low, High, Master_Path)
        tasks.append((set_chunk, gen_name, name, low, high, path))

    # EXECUTION: Processing all precision passes simultaneously
    print(f"Processing {len(tasks)} settlements across {multiprocessing.cpu_count()} cores...")
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(roll_settlement.settlement_worker, tasks)
        
    # Final save of the Prime database (now containing all blanked holes)
    temp_df.to_excel(path, index=False)
    #######################################################################

if __name__ == "__main__":
    main()