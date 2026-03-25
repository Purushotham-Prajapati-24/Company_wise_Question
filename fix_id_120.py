import json
import os

def generate_test_cases():
    def minimumTotal(triangle):
        if not triangle: return 0
        dp = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col+1])
        return dp[0]

    cases = [
        {"input": "[[2],[3,4],[6,5,7],[4,1,8,3]]", "expected_output": "11", "is_sample": True},
        {"input": "[[-10]]", "expected_output": "-10", "is_sample": True},
    ]

    # Case 8: 10 rows
    tri8 = [[i for i in range(r+1)] for r in range(10)]
    cases.append({"input": json.dumps(tri8), "expected_output": str(minimumTotal(tri8)), "is_sample": False})

    # Case 10: 200 rows (Peak Constraint)
    tri10 = [[1 for _ in range(r+1)] for r in range(200)]
    cases.append({"input": json.dumps(tri10), "expected_output": "200", "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Goldman Sachs/120_Triangle.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>120 Triangle</h3><p>Given a <code>triangle</code> array, return <em>the minimum path sum from top to bottom</em>.</p><p>For each step, you may move to an adjacent number of the row below. More formally, if you are on index <code>i</code> on the current row, you may move to either index <code>i</code> or index <code>i + 1</code> on the next row.</p>"
    d["difficulty"] = "MEDIUM"
    d["marks"] = 15
    d["input_format"] = "A 2D integer array triangle representation."
    d["output_format"] = "Integer representing the minimum path sum."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]"""

    d["boilerplate"]["python"] = """import sys, json

def solve(triangle):
    if not triangle: return 0
    dp = triangle[-1][:]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    return dp[0]

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        try:
            triangle = json.loads(line)
            print(solve(triangle))
        except:
            print(0)
    else:
        print(0)"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 120 in Goldman Sachs")
