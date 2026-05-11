import json
# The script writes relative to its CWD (archive/scripts), so JSON goes here:
path = r'd:\College Projects\MNC_based\archive\scripts\301-500\380_Insert_Delete_GetRandom_O(1).json'
with open(path) as f:
    d = json.load(f)
tc = d['test_cases']
result = f'Total test cases: {len(tc)}\n'
for i, t in enumerate(tc):
    result += f"  [{i+1}] is_sample={t['is_sample']}\n"
print(result)
