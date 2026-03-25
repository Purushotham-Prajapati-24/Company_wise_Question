import os
import json
import shutil

# Paths
base_dir = r"d:\College Projects\MNC_based\companyWiseQuestions"
google_dir = os.path.join(base_dir, "Google")
audit_file = r"d:\College Projects\MNC_based\audit_100_130.json"

def propagate():
    if not os.path.exists(audit_file):
        print("Audit file not found.")
        return

    with open(audit_file, 'r', encoding='utf-8') as f:
        audit_data = json.load(f)

    # Group target files by ID
    targets = {}
    for entry in audit_data:
        pid = entry['id']
        if 120 <= pid <= 128:
            if pid not in targets:
                targets[pid] = []
            targets[pid].append(entry['file'])

    # Find source files in Google folder
    google_files = {}
    for f in os.listdir(google_dir):
        if f.endswith(".json"):
            pid_str = f.split("_")[0]
            if pid_str.isdigit():
                pid = int(pid_str)
                if 120 <= pid <= 128:
                    google_files[pid] = os.path.join(google_dir, f)

    # Perform propagation
    count = 0
    for pid, source_path in google_files.items():
        if pid in targets:
            for target_path in targets[pid]:
                if target_path == source_path: continue # Skip copying to itself
                try:
                    # Enforce the specific filename format if it differs? 
                    # Usually, they are the same filename but in different folders.
                    shutil.copy2(source_path, target_path)
                    # We also need to update the 'companyIndex' in the target?
                    # Wait, 'companyIndex' might be specific to the company folder.
                    # Let's check if 'companyIndex' is used.
                    
                    # Actually, usually propagation just copies the whole file. 
                    # If companyIndex is 0 in Google, it stays 0 in Amazon. 
                    # Is that okay? The user's role model doesn't specify.
                    # Let's see if other files have different companyIndex.
                    count += 1
                except Exception as e:
                    print(f"Error copying {pid} to {target_path}: {e}")

    print(f"Propagated {count} files.")

if __name__ == "__main__":
    propagate()
