import json
import os

def generate_test_cases():
    def maxProfit(prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

    cases = [
        {"input": "[7,1,5,3,6,4]", "expected_output": "5", "is_sample": True},
        {"input": "[7,6,4,3,1]", "expected_output": "0", "is_sample": True},
        {"input": "[]", "expected_output": "0", "is_sample": False},
        {"input": "[1]", "expected_output": "0", "is_sample": False},
        {"input": "[1,2]", "expected_output": "1", "is_sample": False},
        {"input": "[2,1]", "expected_output": "0", "is_sample": False},
        {"input": "[1,2,3,4,5]", "expected_output": "4", "is_sample": False},
    ]

    # Case 8: 1000 nodes, increasing
    cases.append({"input": json.dumps(list(range(1, 1001))), "expected_output": str(maxProfit(list(range(1, 1001)))), "is_sample": False})

    # Case 9: 10000 nodes, random-ish
    import random
    random.seed(42)
    prices9 = [random.randint(0, 10**4) for _ in range(10000)]
    cases.append({"input": json.dumps(prices9), "expected_output": str(maxProfit(prices9)), "is_sample": False})

    # Case 10: 100000 nodes (Peak Constraint)
    prices10 = list(range(100000, 0, -1)) # Decreasing, profit 0
    cases.append({"input": json.dumps(prices10), "expected_output": "0", "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Adobe/121_Best_Time_to_Buy_and_Sell_Stock.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>121 Best Time to Buy and Sell Stock</h3><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p><p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p><p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>"
    d["difficulty"] = "EASY"
    d["marks"] = 5
    d["input_format"] = "An integer array prices."
    d["output_format"] = "An integer representing the maximum profit."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit"""

    d["boilerplate"]["python"] = """import sys, json

def solve(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

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
    print("Standardized ID 121 in Adobe")
