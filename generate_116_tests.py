import json

def get_perfect_tree(depth, val=1):
    n = (2 ** depth) - 1
    return [val] * n

def get_expected_output(arr):
    if not arr: return []
    res = []
    n = len(arr)
    # Binary tree level order
    level = 0
    start = 0
    while start < n:
        num_nodes_in_level = 2 ** level
        end = start + num_nodes_in_level
        res.extend(arr[start:end])
        res.append(None)
        start = end
        level += 1
    return res

test_depths = [3, 0, 1, 2, 4, 3, 5, 2, 6, 7] # Mix of depths
final_tcs = []

# Manual override for some to match samples or variety
specs = [
    {"arr": [1,2,3,4,5,6,7], "is_sample": True},
    {"arr": [], "is_sample": True},
    {"arr": [1], "is_sample": False},
    {"arr": [1,2,3], "is_sample": False},
    {"arr": list(range(1, 16)), "is_sample": False},
    {"arr": [1]*31, "is_sample": False},
    {"arr": [5]*7, "is_sample": False},
    {"arr": list(range(1, 64)), "is_sample": False},
    {"arr": [0]*127, "is_sample": False},
    {"arr": [1]*511, "is_sample": False} # d=9
]

for spec in specs:
    arr = spec["arr"]
    expected = get_expected_output(arr)
    
    in_str = json.dumps(arr).replace(" ", "")
    out_str = json.dumps(expected).replace("null", "null").replace(" ", "")
    
    final_tcs.append({
        "input": in_str,
        "expected_output": out_str,
        "is_sample": spec["is_sample"]
    })

file_path = 'd:/College Projects/MNC_based/companyWiseQuestions/Visa/116_Populating_Next_Right_Pointers_in_Each_Node.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data['test_cases'] = final_tcs

# Update formatting of h3 tag if needed (though it seems ok)
if "<h3>116 " in data['question_text']:
     data['question_text'] = data['question_text'].replace("<h3>116 ", "<h3>116. ")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Updated 116 in Visa")
