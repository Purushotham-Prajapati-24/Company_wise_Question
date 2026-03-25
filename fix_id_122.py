import json
import os

def generate_test_cases():
    def maxProfit(prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    cases = [
        {"input": "[7,1,5,3,6,4]", "expected_output": "7", "is_sample": True},
        {"input": "[1,2,3,4,5]", "expected_output": "4", "is_sample": True},
        {"input": "[7,6,4,3,1]", "expected_output": "0", "is_sample": True},
        {"input": "[]", "expected_output": "0", "is_sample": False},
        {"input": "[1]", "expected_output": "0", "is_sample": False},
        {"input": "[1,2]", "expected_output": "1", "is_sample": False},
        {"input": "[2,1]", "expected_output": "0", "is_sample": False},
    ]

    # Case 8: 1000 nodes, zigzag
    prices8 = [100, 200, 100, 200] * 250
    cases.append({"input": json.dumps(prices8), "expected_output": str(maxProfit(prices8)), "is_sample": False})

    # Case 9: 10000 nodes, increasing
    prices9 = list(range(1, 10001))
    cases.append({"input": json.dumps(prices9), "expected_output": str(maxProfit(prices9)), "is_sample": False})

    # Case 10: 30000 nodes (Peak Constraint) random-ish
    import random
    random.seed(42)
    prices10 = [random.randint(0, 10**4) for _ in range(30000)]
    cases.append({"input": json.dumps(prices10), "expected_output": str(maxProfit(prices10)), "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Goldman Sachs/122_Best_Time_to_Buy_and_Sell_Stock_II.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>122 Best Time to Buy and Sell Stock II</h3><p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p><p>On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.</p><p>Find and return the maximum profit you can achieve.</p>"
    d["difficulty"] = "MEDIUM"
    d["marks"] = 10
    d["input_format"] = "An integer array prices."
    d["output_format"] = "Integer representing max profit."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit"""

    d["boilerplate"]["python"] = """import sys, json

def solve(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

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
    print("Standardized ID 122 in Goldman Sachs")
