path = r'd:\College Projects\MNC_based\archive\scripts\make_standard_383.py'

with open(path, encoding='utf-8') as f:
    content = f.read()

# Find and replace the test_cases block
old_start = '    test_cases = [{"input": \'\"a\"\\\\n\"b\"'
new_block = '''    test_cases = [
        # Sample cases (2)
        {"input": '"a"\\n"b"', "expected_output": "false", "is_sample": True},
        {"input": '"aa"\\n"aab"', "expected_output": "true", "is_sample": True},
        # Diverse cases (5)
        {"input": '"aa"\\n"ab"', "expected_output": "false", "is_sample": False},
        {"input": '""\\n"abc"', "expected_output": "true", "is_sample": False},
        {"input": '"abc"\\n""', "expected_output": "false", "is_sample": False},
        {"input": '"fffbfg"\\n"effjfggeffjgfejjfge"', "expected_output": "true", "is_sample": False},
        {"input": '"bg"\\n"efjbdfbdgfjhgalig"', "expected_output": "true", "is_sample": False},
        # Stress cases (3)
        {"input": '"' + "a"*100000 + '"\\n"' + "a"*100000 + '"', "expected_output": "true", "is_sample": False},
        {"input": '"' + "a"*100000 + '"\\n"' + "b"*100000 + '"', "expected_output": "false", "is_sample": False},
        {"input": '"' + "abcdefghijklmnopqrstuvwxyz"*3846 + '"\\n"' + "abcdefghijklmnopqrstuvwxyz"*3847 + '"', "expected_output": "true", "is_sample": False},
    ]'''

# Find the start index of test_cases
idx = content.find('    test_cases = [')
end_marker = '    data = {'
end_idx = content.find(end_marker, idx)

if idx == -1 or end_idx == -1:
    print("ERROR: Could not find markers")
else:
    new_content = content[:idx] + new_block + '\n\n' + content[end_idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done. Lines:", new_content.count('\n'))
    # Verify
    lines = new_content.splitlines()
    tc_start = next(i for i, l in enumerate(lines) if '    test_cases = [' in l)
    tc_end = next(i for i, l in enumerate(lines) if '    data = {' in l)
    print("Test cases block lines:", tc_start+1, "to", tc_end)
