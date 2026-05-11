import json
import os

def generate_json():
    problem_id = 123
    title = "Best Time to Buy and Sell Stock III"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>123. Best Time to Buy and Sell Stock III</h3>
<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>Find the maximum profit you can achieve. You may complete <strong>at most two transactions</strong>.</p>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> prices = [3,3,5,0,0,3,1,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Total profit is 3 + 3 = 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you must sell before you buy again.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing stock prices over time."
    output_format = "An integer representing the maximum achievable profit with at most two transactions."
    
    constraints = [
        "1 <= prices.length <= 10^5",
        "0 <= prices[i] <= 10^5."
    ]
    
    explanation = """To solve the at-most-two-transactions problem efficiently:
1. **Dynamic Programming with 4 states**:
   - Maintain four variables representing the current "max profit" after each event:
     - `first_buy`: Profit after the first buy (negative if we spend money).
     - `first_sell`: Total profit after the first sell.
     - `second_buy`: Total profit after the second buy (incorporates profit from first sell).
     - `second_sell`: Total profit after the second sell.
2. **Logic**:
   - For each `price` in `prices`:
     - `first_buy = max(first_buy, -price)`
     - `first_sell = max(first_sell, first_buy + price)`
     - `second_buy = max(second_buy, first_sell - price)`
     - `second_sell = max(second_sell, second_buy + price)`
3. **Complexity**:
   - Time Complexity: O(N) as we traverse the array once.
   - Space Complexity: O(1) as we only use 4 variables."""
    
    answer = """def maxProfit(prices):
    if not prices:
        return 0
        
    # Variables representing max profit after each step
    first_buy = second_buy = -float('inf')
    first_sell = second_sell = 0
    
    for price in prices:
        first_buy = max(first_buy, -price)
        first_sell = max(first_sell, first_buy + price)
        second_buy = max(second_buy, first_sell - price)
        second_sell = max(second_sell, second_buy + price)
        
    return second_sell"""

    boilerplate = {
        "python": "import sys\n\ndef maxProfit(prices):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        prices = list(map(int, line.split()))\n        print(maxProfit(prices))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <climits>\n#include <sstream>\nusing namespace std;\nint maxProfit(vector<int>& prices) {\n    // User logic\n    return 0;\n}\nint main() {\n    string line; if(!getline(cin,line)) return 0;\n    istringstream ss(line); vector<int> p; int x;\n    while(ss>>x) p.push_back(x);\n    cout << maxProfit(p) << endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int maxProfit(int[] prices) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if(!sc.hasNextLine()) return;\n        String[] parts = sc.nextLine().trim().split(\"\\\\s+\");\n        int[] p = new int[parts.length];\n        for(int i=0;i<parts.length;i++) p[i]=Integer.parseInt(parts[i]);\n        System.out.println(maxProfit(p));\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction maxProfit(prices) {\n    // User logic\n    return 0;\n}\nconst line = fs.readFileSync(0,'utf8').trim();\nif(line) console.log(maxProfit(line.split(/\\s+/).map(Number)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint maxProfit(int* prices, int pricesSize) {\n    // User logic\n    return 0;\n}\nint main() {\n    char buf[2000000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int arr[100001],cnt=0; char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&cnt<100001){arr[cnt++]=atoi(tok);tok=strtok(NULL,\" \\t\\r\\n\");}\n    printf(\"%d\\n\",maxProfit(arr,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "3 3 5 0 0 3 1 4", "expected_output": "6", "is_sample": True},
        {"input": "1 2 3 4 5", "expected_output": "4", "is_sample": True},
        {"input": "7 6 4 3 1", "expected_output": "0", "is_sample": True},
        {"input": "1 2 1 2 1 2", "expected_output": "2", "is_sample": False},
        {"input": "1 10 1 10", "expected_output": "18", "is_sample": False},
        {"input": "2 1 4 5 2 9 7", "expected_output": "11", "is_sample": False},
        {"input": "1 2 4 2 5 7 2 4 9 0", "expected_output": "13", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(1, 100001))), "expected_output": "99999", "is_sample": False},
        {"input": " ".join(map(str, range(100000, 0, -1))), "expected_output": "0", "is_sample": False},
        {"input": " ".join(["1", "100000"] * 50000), "expected_output": "199998", "is_sample": False}
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

    output_path = "1-200/123_Best_Time_to_Buy_and_Sell_Stock_III.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
