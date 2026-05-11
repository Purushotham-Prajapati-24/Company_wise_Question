import json

def get_gap_list():
    with open('d:/College Projects/MNC_based/pending_audit.json', 'r') as f:
        data = json.load(f)
        pending = data['pending']
    
    with open('d:/College Projects/MNC_based/archive/scripts/existing_scripts.txt', 'r', encoding='utf-16') as f:
        existing = set()
        for line in f:
            line = line.strip()
            if line:
                try:
                    existing.add(int(line))
                except ValueError:
                    pass
    
    gap_list = [pid for pid in pending if pid >= 500 and pid not in existing]
    gap_list.sort()
    
    print(f"Total pending >= 500: {len([pid for pid in pending if pid >= 500])}")
    print(f"Total existing >= 500: {len([pid for pid in existing if pid >= 500])}")
    print(f"Gap List size: {len(gap_list)}")
    print(f"Gap List (first 50): {gap_list[:50]}")
    
    with open('d:/College Projects/MNC_based/gap_list.json', 'w') as f:
        json.dump(gap_list, f, indent=2)

if __name__ == "__main__":
    get_gap_list()
