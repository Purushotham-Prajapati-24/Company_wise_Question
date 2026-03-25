import os
import json

base_path = r"d:\College Projects\MNC_based\companyWiseQuestions\Google"

def update_json(problem_id, filename, new_test_cases):
    full_path = os.path.join(base_path, filename)
    if not os.path.exists(full_path):
        print(f"File {filename} not found.")
        return
    
    with open(full_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Keep existing test cases and append/replace to make it exactly 10
    existing = data.get('test_cases', [])
    
    # Stratified cases for 120
    if problem_id == 120:
        # We need to reach 10. Existing has 4.
        # Cases already there:
        # 1. Sample 1
        # 2. Sample 2
        # 3. 0 to 9 triangle (0)
        # 4. 1s triangle (67 rows)
        
        # New cases:
        additions = [
            {"input": "[[5]]", "expected_output": "5", "is_sample": False},
            {"input": "[[1],[2,3]]", "expected_output": "3", "is_sample": False},
            {"input": "[[-1],[-2,-3],[-4,-5,-6]]", "expected_output": "-10", "is_sample": False},
            {"input": "[[10000],[10000,10000]]", "expected_output": "20000", "is_sample": False},
            {"input": "[[1],[-2,-3],[4,-5,6],[-7,8,-9,10]]", "expected_output": "-9", "is_sample": False},
            {"input": "[[8],[2,3],[4,5,1]]", "expected_output": "12", "is_sample": False}
        ]

        data['test_cases'] = existing + additions
    
    if problem_id == 123:
        # Existing has 5.
        # 1. [3,3,5,0,0,3,1,4] -> 6
        # 2. [1,2,3,4,5] -> 4
        # 3. [7,6,4,3,1] -> 0
        # 4. [1] -> 0
        # 5. [1,2] -> 1
        additions = [
            {"input": "[3,2,6,5,0,3]", "expected_output": "7", "is_sample": False}, # (6-2) + (3-0) = 4 + 3 = 7
            {"input": "[1,4,2,7]", "expected_output": "8", "is_sample": False}, # (4-1) + (7-2) = 3 + 5 = 8
            {"input": "[1,2,3,4,5,6,7,8,9,10]", "expected_output": "9", "is_sample": False},
            {"input": "[10,9,8,7,6,5,4,3,2,1]", "expected_output": "0", "is_sample": False},
            {"input": "[2,1,2,1,2,1,2]", "expected_output": "2", "is_sample": False}
        ]

        data['test_cases'] = existing + additions

    if problem_id == 126:
        # Existing has 6.
        # "hit", "cog", ["hot","dot","dog","lot","log","cog"] -> [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
        # ...
        additions = [
            {"input": '["a", "c", ["a", "b", "c"]]', "expected_output": '[["a","c"]]', "is_sample": False},
            {"input": '["hot", "dog", ["hot", "dog"]]', "expected_output": "[]", "is_sample": False},
            {"input": '["cat", "fin", ["cat", "can", "fan", "fin"]]', "expected_output": '[["cat","can","fan","fin"]]', "is_sample": False},
            {"input": '["red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]]', "expected_output": '[["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]', "is_sample": False}
        ]

        data['test_cases'] = existing + additions

    if problem_id == 127:
        # Existing has 7.
        additions = [
            {"input": '["hit", "cog", ["hot","dot","dog","lot","log"]]', "expected_output": "0", "is_sample": False},
            {"input": '["a", "b", ["a", "b", "c"]]', "expected_output": "2", "is_sample": False},
            {"input": '["a", "c", ["a", "b"]]', "expected_output": "0", "is_sample": False}
        ]

        data['test_cases'] = existing + additions

    # Final check: Must be exactly 10
    if len(data['test_cases']) != 10:
        print(f"Warning: Problem {problem_id} still has {len(data['test_cases'])} cases.")
    
    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Updated {filename}")

# IDs that need fixing
fix_map = {
    120: "120_Triangle.json",
    123: "123_Best_Time_to_Buy_and_Sell_Stock_III.json",
    126: "126_Word_Ladder_II.json",
    127: "127_Word_Ladder.json"
}

for pid, fname in fix_map.items():
    update_json(pid, fname, [])
