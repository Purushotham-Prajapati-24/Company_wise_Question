path = r'd:\College Projects\MNC_based\archive\scripts\make_standard_381.py'

with open(path, encoding='utf-8') as f:
    content = f.read()

new_tc = '''    test_cases = [
        # Sample cases (2)
        {"input": '["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]\\n[[], [1], [1], [2], [], [1], []]', "expected_output": "[null,true,false,true,1,true,1]", "is_sample": True},
        {"input": '["RandomizedCollection", "insert", "insert", "remove", "getRandom"]\\n[[], [1], [1], [1], []]', "expected_output": "[null,true,false,true,1]", "is_sample": True},
        # Diverse cases (5)
        {"input": '["RandomizedCollection", "insert", "remove", "insert"]\\n[[], [1], [1], [1]]', "expected_output": "[null,true,true,true]", "is_sample": False},
        {"input": '["RandomizedCollection", "insert", "insert", "remove", "remove"]\\n[[], [1], [2], [1], [2]]', "expected_output": "[null,true,true,true,true]", "is_sample": False},
        {"input": '["RandomizedCollection", "remove", "insert"]\\n[[], [0], [0]]', "expected_output": "[null,false,true]", "is_sample": False},
        {"input": '["RandomizedCollection", "insert", "getRandom"]\\n[[], [5], []]', "expected_output": "[null,true,5]", "is_sample": False},
        {"input": '["RandomizedCollection", "insert", "insert", "insert", "remove", "getRandom"]\\n[[], [3], [3], [3], [3], []]', "expected_output": "[null,true,false,false,true,3]", "is_sample": False},
        # Stress cases (3)
        {"input": '["RandomizedCollection"]' + ',"insert"'*5 + ',"getRandom"]\\n[[]' + ',[10]'*5 + ',[]]', "expected_output": "[null,true,false,false,false,false,10]", "is_sample": False},
        {"input": '["RandomizedCollection","insert","remove","insert","remove","insert","remove","insert","remove","insert","remove","insert","getRandom"]\\n[[],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2],[]]', "expected_output": "[null,true,true,true,true,true,true,true,true,true,true,true,2]", "is_sample": False},
        {"input": '["RandomizedCollection","insert","insert","insert","insert","insert","getRandom"]\\n[[],[1],[2],[3],[1],[2],[]]', "expected_output": "[null,true,true,true,false,false,1]", "is_sample": False},
    ]'''

idx = content.find('    test_cases = [')
end_idx = content.find('\n    data = {', idx)

if idx == -1 or end_idx == -1:
    print("ERROR: markers not found")
else:
    new_content = content[:idx] + new_tc + '\n' + content[end_idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Done. Test cases block updated. Total lines: {new_content.count(chr(10))}")
