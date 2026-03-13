import os
import pandas as pd
from data.campaign.tally_npc import apply_npc_styling

def relocate_notables(df, prime_file_path, randos_path, count=10):
    """
    Identifies valid NPCs, exports them to text, 
    blanks them in the source, and saves the update.
    """
    # 1. Filter: Identify non-blank rows
    valid_df = df.dropna(how='all')
    
    if valid_df.empty:
        print("No valid NPCs left to pick!")
        return df

    # 2. Select Sample
    print(f"Selecting {count} randos for text export...")
    sample_npcs = valid_df.sample(n=min(count, len(valid_df)))

    # 3. Export to Text
    for index, row in sample_npcs.iterrows():
        txt_filename = os.path.join(randos_path, f"character_row_{index + 1}.txt")
        with open(txt_filename, "w") as f:
            f.write(f"--- CHARACTER RECORD: ROW {index + 1} ---\n")
            for header, value in zip(df.columns, row):
                if pd.notna(value) and str(value).strip() != "":
                    f.write(f"{header}: {value}\n")
            f.write("--- END OF RECORD ---")

    # 4. Surgical Blanking
    print("Blanking exported rows and re-applying formatting...")
    df.loc[sample_npcs.index, :] = None 

    # 5. Save updated Prime (with blank holes)
    with pd.ExcelWriter(prime_file_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Population', index=False)
        apply_npc_styling(writer, 'Population', df)

    return df