import json
import os

def generate_test_cases():
    def maxProfit(prices):
        if not prices: return 0
        buy1, buy2 = float('inf'), float('inf')
        sell1, sell2 = 0, 0
        for p in prices:
            buy1 = min(buy1, p)
            sell1 = max(sell1, p - buy1)
            buy2 = min(buy2, p - sell1)
            sell2 = max(sell2, p - buy2)
        return sell2

    cases = [
        {"input": "[3,3,5,0,0,3,1,4]", "expected_output": "6", "is_sample": True},
        {"input": "[1,2,3,4,5]", "expected_output": "4", "is_sample": True},
        {"input": "[7,6,4,3,1]", "expected_output": "0", "is_sample": True},
    ]

    # Case 8: 1000 nodes, oscillating
    prices8 = [1, 10] * 500
    cases.append({"input": json.dumps(prices8), "expected_output": str(maxProfit(prices8)), "is_sample": False})

    # Case 10: 100000 nodes (Peak Constraint)
    prices10 = list(range(1, 100001))
    cases.append({"input": json.dumps(prices10), "expected_output": str(maxProfit(prices10)), "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Atlasssian/123_Best_Time_to_Buy_and_Sell_Stock_III.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>123 Best Time to Buy and Sell Stock III</h3><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p><p>Find the maximum profit you can achieve. You may complete <strong>at most two transactions</strong>.</p><p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>"
    d["difficulty"] = "HARD"
    d["marks"] = 25
    d["input_format"] = "An integer array prices."
    d["output_format"] = "Integer representing max profit."
    
    d["metadata"] = {
        "time_limit_ms": 2000,
        "memory_limit_mb": 512,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        buy1, buy2 = float('inf'), float('inf')
        sell1, sell2 = 0, 0
        for p in prices:
            buy1 = min(buy1, p)
            sell1 = max(sell1, p - buy1)
            buy2 = min(buy2, p - sell1)
            sell2 = max(sell2, p - buy2)
        return sell2"""

    d["boilerplate"]["python"] = """import sys, json

def solve(prices):
    if not prices: return 0
    buy1, buy2 = float('inf'), float('inf')
    sell1, sell2 = 0, 0
    for p in prices:
        buy1 = min(buy1, p)
        sell1 = max(sell1, p - buy1)
        buy2 = min(buy2, p - sell1)
        sell2 = max(sell2, p - buy2)
    return sell2

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        try:
            prices = json.loads(line)
            print(solve(prices))
        except:
            print(0)
    else:
        print(0)"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 123 in Atlasssian")
