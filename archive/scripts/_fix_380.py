path = r'd:\College Projects\MNC_based\archive\scripts\make_standard_380.py'

with open(path, encoding='utf-8') as f:
    lines = f.readlines()

# Line 481 is index 480
bad_line = lines[480]
print("BEFORE:", repr(bad_line[:80]))

good_line = '        {"input": \'["RandomizedSet","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","getRandom"]\\n[[],[10],[20],[30],[40],[50],[60],[70],[80],[90],[100],[]]\', "expected_output": "[null,true,true,true,true,true,true,true,true,true,true,10]", "is_sample": False},\n'
lines[480] = good_line
print("AFTER:", repr(good_line[:80]))

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done. Total lines:", len(lines))
