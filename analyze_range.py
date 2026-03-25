import json
import os
import re

def main():
    try:
        with open('question_id_map.json', 'r', encoding='utf-8') as f:
            id_map = json.load(f)
    except FileNotFoundError:
        print("Error: question_id_map.json not found.")
        return

    target_ids = [str(i) for i in range(500, 1001)]
    found_ids = {}

    for tid in target_ids:
        if tid in id_map:
            found_ids[tid] = id_map[tid]

    print(f"Total IDs found in map: {len(found_ids)}")

    # Check for existing files in companyWiseQuestions
    base_dir = 'companyWiseQuestions'
    existing_files = []
    if os.path.exists(base_dir):
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                match = re.match(r'^(\d+)_', file)
                if match:
                    qid = match.group(1)
                    if 500 <= int(qid) <= 1000:
                        existing_files.append(os.path.join(root, file))
    else:
        print(f"Error: {base_dir} directory not found.")

    print(f"Total existing files in range 500-1000: {len(existing_files)}")
    
    with open('analysis_results.json', 'w', encoding='utf-8') as f:
        json.dump({
            "found_ids": found_ids,
            "existing_files": existing_files
        }, f, indent=4)
    print("Results saved to analysis_results.json")

if __name__ == '__main__':
    main()
