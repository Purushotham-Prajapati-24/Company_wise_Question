import json
import os

def generate_json():
    problem_id = 121
    title = "Best Time to Buy and Sell Stock"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>121. Best Time to Buy and Sell Stock</h3>
<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing stock prices over time."
    output_format = "An integer representing the maximum profit."
    
    constraints = [
        "1 <= prices.length <= 10^5",
        "0 <= prices[i] <= 10^4."
    ]
    
    explanation = """To find the maximum profit from a single transaction:
1. **One-Pass Approach**:
   - Maintain a variable `min_price` to track the lowest price seen so far (initialized to infinity).
   - Maintain a variable `max_profit` to track the maximum difference found (initialized to 0).
   - Iterate through the `prices` array:
     - Update `min_price` if the current price is lower than the current `min_price`.
     - Otherwise, calculate the profit if the stock was sold today (`current_price - min_price`). If this profit is greater than `max_profit`, update `max_profit`.
2. **Complexity**:
   - Time Complexity: O(N) as we traverse the array once.
   - Space Complexity: O(1) as we only use a few constant variables."""
    
    answer = """def maxProfit(prices):
    if not prices:
        return 0
        
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit"""

    boilerplate = {
        "python": "import sys\n\ndef maxProfit(prices):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        prices = list(map(int, line.split()))\n        print(maxProfit(prices))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nint maxProfit(vector<int>& prices) {\n    // User logic\n    return 0;\n}\nint main() {\n    string line; if(!getline(cin,line)) return 0;\n    istringstream ss(line); vector<int> p; int x;\n    while(ss>>x) p.push_back(x);\n    cout << maxProfit(p) << endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int maxProfit(int[] prices) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if(!sc.hasNextLine()) return;\n        String[] parts = sc.nextLine().trim().split(\"\\\\s+\");\n        int[] p = new int[parts.length];\n        for(int i=0;i<parts.length;i++) p[i]=Integer.parseInt(parts[i]);\n        System.out.println(maxProfit(p));\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction maxProfit(prices) {\n    // User logic\n    return 0;\n}\nconst line = fs.readFileSync(0,'utf8').trim();\nif(line) console.log(maxProfit(line.split(/\\s+/).map(Number)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint maxProfit(int* prices, int pricesSize) {\n    // User logic\n    return 0;\n}\nint main() {\n    char buf[2000000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int arr[100001],cnt=0; char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&cnt<100001){arr[cnt++]=atoi(tok);tok=strtok(NULL,\" \\t\\r\\n\");}\n    printf(\"%d\\n\",maxProfit(arr,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "7 1 5 3 6 4", "expected_output": "5", "is_sample": True},
        {"input": "7 6 4 3 1", "expected_output": "0", "is_sample": True},
        {"input": "1 2", "expected_output": "1", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "4", "is_sample": False},
        {"input": "5 4 3 2 1", "expected_output": "0", "is_sample": False},
        {"input": "3 3 3 3", "expected_output": "0", "is_sample": False},
        {"input": "2 4 1", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(100000, 0, -1))), "expected_output": "0", "is_sample": False},
        {"input": " ".join(map(str, range(1, 100001))), "expected_output": "99999", "is_sample": False},
        {"input": " ".join(["0", "10000"] * 50000), "expected_output": "10000", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1-200/121_Best_Time_to_Buy_and_Sell_Stock.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
