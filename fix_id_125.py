import json
import os

def generate_test_cases():
    def isPalindrome(s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]

    cases = [
        {"input": '"A man, a plan, a canal: Panama"', "expected_output": "true", "is_sample": True},
        {"input": '"race a car"', "expected_output": "false", "is_sample": True},
        {"input": '" "', "expected_output": "true", "is_sample": True},
        {"input": '""', "expected_output": "true", "is_sample": False},
        {"input": '"a"', "expected_output": "true", "is_sample": False},
        {"input": '"ab"', "expected_output": "false", "is_sample": False},
        {"input": '".,"', "expected_output": "true", "is_sample": False},
    ]

    # Case 8: 1000 chars, palindrome
    s8 = "a" * 1000
    cases.append({"input": json.dumps(s8), "expected_output": "true", "is_sample": False})

    # Case 9: 10000 chars, non-palindrome
    s9 = "a" * 5000 + "b" + "a" * 4999
    cases.append({"input": json.dumps(s9), "expected_output": "false", "is_sample": False})

    # Case 10: 200000 chars (Peak Constraint)
    s10 = "a" * 200000
    cases.append({"input": json.dumps(s10), "expected_output": "true", "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Meta/125_Valid_Palindrome.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>125 Valid Palindrome</h3><p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p><p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>"
    d["difficulty"] = "EASY"
    d["marks"] = 5
    d["input_format"] = "A string s."
    d["output_format"] = "boolean"
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]"""

    d["boilerplate"]["python"] = """import sys, json

def solve(s):
    res = []
    for char in s:
        if char.isalnum():
            res.append(char.lower())
    filtered = "".join(res)
    return filtered == filtered[::-1]

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        try:
            # Handle potential surrounding quotes from JSON input
            s = json.loads(line)
            print("true" if solve(s) else "false")
        except:
            print("true")
    else:
        print("true")"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 125 in Meta")
