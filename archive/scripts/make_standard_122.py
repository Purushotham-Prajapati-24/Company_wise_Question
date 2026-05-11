import json
import os

def generate_json():
    problem_id = 122
    title = "Best Time to Buy and Sell Stock II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>122. Best Time to Buy and Sell Stock II</h3>
<p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>On each day, you may decide to buy and/or sell the stock. You can only hold <strong>at most one</strong> share of the stock at any time. However, you can buy it then immediately sell it on the <strong>same day</strong>.</p>

<p>Find and return <em>the <strong>maximum</strong> profit you can achieve</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= prices.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing stock prices over time."
    output_format = "An integer representing the maximum achievable profit."
    
    constraints = [
        "1 <= prices.length <= 3 * 10^4",
        "0 <= prices[i] <= 10^4."
    ]
    
    explanation = """To maximize profit with multiple transactions:
1. **Greedy Approach**:
   - Since we can buy and sell on the same day or consecutive days, our total maximum profit is the sum of all positive daily price increments.
   - For every day `i`, if `prices[i]` is greater than `prices[i-1]`, we add the difference `prices[i] - prices[i-1]` to our total profit.
   - This effectively captures every upward price movement, which combined results in the maximum possible profit over any number of transactions.
2. **Complexity**:
   - Time Complexity: O(N) as we traverse the price array once.
   - Space Complexity: O(1) as we only use a single variable to accumulate the profit."""
    
    answer = """def maxProfit(prices):
    if not prices:
        return 0
        
    total_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            total_profit += prices[i] - prices[i-1]
            
    return total_profit"""

    boilerplate = {
        "python": "import sys\n\ndef maxProfit(prices):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        prices = list(map(int, line.split()))\n        print(maxProfit(prices))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nint maxProfit(vector<int>& prices) {\n    // User logic\n    return 0;\n}\nint main() {\n    string line; if(!getline(cin,line)) return 0;\n    istringstream ss(line); vector<int> p; int x;\n    while(ss>>x) p.push_back(x);\n    cout << maxProfit(p) << endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int maxProfit(int[] prices) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if(!sc.hasNextLine()) return;\n        String[] parts = sc.nextLine().trim().split(\"\\\\s+\");\n        int[] p = new int[parts.length];\n        for(int i=0;i<parts.length;i++) p[i]=Integer.parseInt(parts[i]);\n        System.out.println(maxProfit(p));\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction maxProfit(prices) {\n    // User logic\n    return 0;\n}\nconst line = fs.readFileSync(0,'utf8').trim();\nif(line) console.log(maxProfit(line.split(/\\s+/).map(Number)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint maxProfit(int* prices, int pricesSize) {\n    // User logic\n    return 0;\n}\nint main() {\n    char buf[1000000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int arr[30001],cnt=0; char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&cnt<30001){arr[cnt++]=atoi(tok);tok=strtok(NULL,\" \\t\\r\\n\");}\n    printf(\"%d\\n\",maxProfit(arr,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "7 1 5 3 6 4", "expected_output": "7", "is_sample": True},
        {"input": "1 2 3 4 5", "expected_output": "4", "is_sample": True},
        {"input": "7 6 4 3 1", "expected_output": "0", "is_sample": True},
        {"input": "1 2 1 2 1 2", "expected_output": "3", "is_sample": False},
        {"input": "1 10 1 10", "expected_output": "18", "is_sample": False},
        {"input": "1 2 4 8 16", "expected_output": "15", "is_sample": False},
        {"input": "100 0 100 0", "expected_output": "100", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(30000))), "expected_output": "29999", "is_sample": False},
        {"input": " ".join(map(str, range(30000, 0, -1))), "expected_output": "0", "is_sample": False},
        {"input": " ".join(["1", "10000"] * 15000), "expected_output": str(9999 * 15000), "is_sample": False}
    ]

    data = {
        "question_text": html_description,
        "difficulty": difficulty,
        "marks": marks,
        "input_format": input_format,
        "output_format": output_format,
        "constraints": constraints,
        "explanation": explanation,
        "answer": answer,
        "boilerplate": boilerplate,
        "test_cases": test_cases,
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Dynamic Programming", "Greedy"],
        "companyIndex": 0
    }

    output_path = "1-200/122_Best_Time_to_Buy_and_Sell_Stock_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
