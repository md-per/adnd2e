import os
import random
import pandas as pd
from data.campaign.tally_npc import export_npc_pop

def create_settlement(df, campaign_name, settlement_name, low, high, kingdom_prime_path):
    """Plucks NPCs, triggers Tally, then performs a precision pass and blanking for Special Characters."""
    # Determine size and drop empty rows
    pop_size = random.randint(low, high)
    valid_df = df.dropna(how='all')
    
    if len(valid_df) < pop_size:
        pop_size = len(valid_df)

    # Sample without replacement
    settlement_df = valid_df.sample(n=pop_size)
    settlement_folder = os.path.join("data/campaign", campaign_name, settlement_name)
    os.makedirs(settlement_folder, exist_ok=True)

    # Plugin Call: Build the settlement summary first
    export_npc_pop(
        lists={settlement_name: settlement_df.values.tolist()},
        gen_name=settlement_name, 
        matrix={}, 
        folder_path=settlement_folder
    )

    #######################################################################
    # POST-TALLY PRECISION PASS & BLANKING
    # Reads the final Prime file, generates sheets, then surgically blanks them
    #######################################################################
    prime_file = os.path.join(settlement_folder, f"{settlement_name}_Prime.xlsx")
    
    if os.path.exists(prime_file):
        # Load the newly created Excel file
        final_df = pd.read_excel(prime_file, sheet_name="Prime")
        indices_to_blank = []
        
        for idx, row in final_df.iterrows():
            try:
                # Standardized extraction from Column H (Power)
                pwr_val = int(str(row.iloc[7]).split()[0])
            except (ValueError, IndexError):
                pwr_val = 0

            if pwr_val >= 78:
                tier = "Gods" if pwr_val >= 92 else "Heroes"
                tier_folder = os.path.join(settlement_folder, tier)
                os.makedirs(tier_folder, exist_ok=True)
                
                # Naming Convention: {race}_{Settlement Name}_{Row}_{power}.txt
                clean_race = str(row.iloc[0]).strip().rstrip(':')
                # idx + 2: idx is 0-based; Excel is 1-based + 1 for header row
                row_num = idx + 2 
                filename = f"{clean_race}_{settlement_name}_{pwr_val}_Row-{row_num}.txt"
                sheet_path = os.path.join(tier_folder, filename)
                
                with open(sheet_path, "w") as f:
                    f.write(f"--- {tier.upper()} CHARACTER SHEET ---\n\n")
                    for col_name, value in row.items():
                        f.write(f"{col_name}: {value}\n")
                
                # Mark this index for blanking from the Excel file
                indices_to_blank.append(idx)
        
        # Surgical Blanking from the Settlement Prime File
        if indices_to_blank:
            final_df.loc[indices_to_blank, :] = None
            with pd.ExcelWriter(prime_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                final_df.to_excel(writer, sheet_name="Prime", index=False)
    #######################################################################

    print(f"Relocating {pop_size} NPCs to {settlement_name}...")
    # Surgical blanking in the main kingdom pool
    # df.loc[settlement_df.index, :] = None !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    df.loc[settlement_df.index, :] = None 
    return df