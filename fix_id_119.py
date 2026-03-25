import json
import os

def generate_test_cases():
    def getRow(rowIndex):
        row = [1]
        for i in range(rowIndex):
            row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
        return row

    cases = [
        {"input": "3", "expected_output": "[1,3,3,1]", "is_sample": True},
        {"input": "0", "expected_output": "[1]", "is_sample": True},
        {"input": "1", "expected_output": "[1,1]", "is_sample": True},
    ]

    # Case 8: rowIndex = 10
    cases.append({"input": "10", "expected_output": json.dumps(getRow(10)), "is_sample": False})

    # Case 9: rowIndex = 20
    cases.append({"input": "20", "expected_output": json.dumps(getRow(20)), "is_sample": False})

    # Case 10: rowIndex = 33 (Peak Constraint)
    cases.append({"input": "33", "expected_output": json.dumps(getRow(33)), "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Goldman Sachs/119_Pascal_s_Triangle_II.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>119 Pascal's Triangle II</h3><p>Given an integer <code>rowIndex</code>, return the <code>rowIndex<sup>th</sup></code> (<strong>0-indexed</strong>) row of the <strong>Pascal's triangle</strong>.</p><p>In <strong>Pascal's triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>"
    d["difficulty"] = "EASY"
    d["marks"] = 5
    d["input_format"] = "An integer rowIndex."
    d["output_format"] = "A list of integers representing the rowIndex-th row."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row"""

    d["boilerplate"]["python"] = """import sys, json

def solve(rowIndex):
    row = [1] * (rowIndex + 1)
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j - 1]
    return row

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        try:
            rowIndex = int(line)
            print(json.dumps(solve(rowIndex)))
        except:
            print("[1]")
    else:
        print("[1]")"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 119 in Goldman Sachs")
