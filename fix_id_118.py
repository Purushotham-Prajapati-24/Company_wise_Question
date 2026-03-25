import json
import os

def generate_test_cases():
    def generate(numRows):
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res

    cases = [
        {"input": "5", "expected_output": json.dumps([[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]), "is_sample": True},
        {"input": "1", "expected_output": json.dumps([[1]]), "is_sample": True},
        {"input": "2", "expected_output": json.dumps([[1],[1,1]]), "is_sample": False},
        {"input": "3", "expected_output": json.dumps([[1],[1,1],[1,2,1]]), "is_sample": False},
        {"input": "4", "expected_output": json.dumps([[1],[1,1],[1,2,1],[1,3,3,1]]), "is_sample": False},
        {"input": "6", "expected_output": json.dumps(generate(6)), "is_sample": False},
        {"input": "10", "expected_output": json.dumps(generate(10)), "is_sample": False},
    ]

    # Case 8: 15 rows
    cases.append({"input": "15", "expected_output": json.dumps(generate(15)), "is_sample": False})

    # Case 9: 25 rows
    cases.append({"input": "25", "expected_output": json.dumps(generate(25)), "is_sample": False})

    # Case 10: 30 rows (Peak Constraint)
    cases.append({"input": "30", "expected_output": json.dumps(generate(30)), "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Goldman Sachs/118_Pascal_s_Triangle.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>118 Pascal's Triangle</h3><p>Given an integer <code>numRows</code>, return the first <code>numRows</code> of <strong>Pascal's triangle</strong>.</p><p>In <strong>Pascal's triangle</strong>, each number is the sum of the two numbers directly above it.</p>"
    d["difficulty"] = "EASY"
    d["marks"] = 5
    d["input_format"] = "An integer numRows."
    d["output_format"] = "A list of lists of integers representing Pascal's triangle."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res"""

    d["boilerplate"]["python"] = """import sys, json

def solve(numRows):
    res = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = res[i-1][j-1] + res[i-1][j]
        res.append(row)
    return res

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        try:
            numRows = int(line)
            print(json.dumps(solve(numRows)))
        except:
            print("[]")
    else:
        print("[]")"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 118 in Goldman Sachs")
