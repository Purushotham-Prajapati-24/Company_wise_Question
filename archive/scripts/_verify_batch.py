import json, os

files = [
    (r'd:\College Projects\MNC_based\archive\scripts\301-500\381_Insert_Delete_GetRandom_O(1)_Duplicates_allowed.json', '381'),
    (r'd:\College Projects\MNC_based\archive\scripts\301-500\383_Ransom_Note.json', '383'),
    (r'd:\College Projects\MNC_based\archive\scripts\301-500\384_Shuffle_an_Array.json', '384'),
]

all_ok = True
for path, pid in files:
    name = os.path.basename(path)
    with open(path) as f:
        d = json.load(f)
    tc = d['test_cases']
    samples = sum(1 for t in tc if t['is_sample'])
    non_s = len(tc) - samples
    status = "OK" if len(tc) == 10 and samples == 2 else "FAIL"
    if status != "OK":
        all_ok = False
    print(f"[{status}] ID {pid}: total={len(tc)}, samples={samples}, non_samples={non_s}")

print()
print("All compliant:", all_ok)
