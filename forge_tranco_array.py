import os

# Define the absolute materialist path parameters
csv_filename = "tranco_K9YYW.csv"
output_filename = "target_domains_output.txt"

print("🪐 PSICO COMMUNICATIONS // TRANCO CSV REFINERY PIPELINE")
print("--------------------------------------------------------------------")

if not os.path.exists(csv_filename):
    print(f"❌ ERROR: Target database file not found at: {csv_filename}")
    print("   Ensure tranco_K9YYW.csv is resting in your current folder.")
else:
    try:
        # Read the raw lines from your Tranco database sector
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            lines = csv_file.readlines()

        print(f"📡 INGESTION SUCCESS: Loaded {len(lines):,} raw data rows.")
        
        # 🛠️ Define the chunk bounds (e.g., first 100 rows, or adjust as needed)
        # You can chop and change these index boundaries to extract any batch
        start_row = 600
        end_row = 700
        target_batch = lines[start_row:end_row]

        # Structure the clean array text container
        output_buffer = []
        output_buffer.append("    target_domains = [")

        for line in target_batch:
            clean_line = line.strip()
            if not clean_line:
                continue
            
            # Split line by the CSV comma marker (Index Number, Domain)
            parts = clean_line.split(",")
            if len(parts) >= 2:
                # Isolate the clean domain string token
                domain = parts[1].strip()
                output_buffer.append(f'        "{domain}",')

        output_buffer.append("    ]")

        # ⚡ Write the pristine, code-ready block directly out to a flat text file
        with open(output_filename, "w", encoding="utf-8") as out_file:
            out_file.write("\n".join(output_buffer) + "\n")

        print(f"🚀 REFINE SUCCESS: Burned batch [{start_row+1}-{end_row}] flat to disk!")
        print(f"   └── Output File node: {output_filename}")
        print("--------------------------------------------------------------------")
        print("Open the output .txt file, grab the array, and feed it straight to ico.py.")

    except Exception as e:
        print(f"❌ CRITICAL SUBSYSTEM FAILURE: {str(e)}")
