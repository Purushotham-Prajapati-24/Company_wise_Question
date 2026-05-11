import json
import os

def generate_json():
    problem_id = 322
    title = "Coin Change"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>322. Coin Change</h3>
<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return <em>the fewest number of coins that you need to make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= coins.length &lt;= 12</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= amount &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two lines. Line 1: an array of integers representing `coins`. Line 2: an integer representing `amount`."
    output_format = "An integer representing the minimum number of coins."
    
    constraints = [
        "1 <= coins.length <= 12",
        "0 <= amount <= 10^4",
        "O(amount * coins.length) time complexity.",
        "O(amount) space complexity."
    ]
    
    explanation = """To find the minimum number of coins needed for a target amount (unbounded knapsack problem):
1. **Dynamic Programming**:
   - Let `dp[i]` be the minimum number of coins required to make the amount `i`.
   - Initialize `dp[0] = 0` and all other `dp[i]` to `infinity`.
2. **Transition**:
   - For each coin in `coins`:
     - For `i` from `coin` to `amount`:
       - `dp[i] = min(dp[i], dp[i - coin] + 1)`
3. **Complexity**:
   - Time Complexity: O(amount * N) where N is the number of coin types.
   - Space Complexity: O(amount) to store the DP table."""
    
    answer = """def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def coinChange(self, coins: list[int], amount: int) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        lines = raw_input.split('\\n')\n        if len(lines) >= 2:\n            coins = json.loads(lines[0])\n            amount = json.loads(lines[1])\n            sol = Solution()\n            print(json.dumps(sol.coinChange(coins, amount)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\nusing namespace std;\n\nclass Solution {\npublic:\n    int coinChange(vector<int>& coins, int amount) {\n        // Your logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        vector<int> coins;\n        if (line1.length() >= 2) {\n            line1 = line1.substr(1, line1.length() - 2);\n            if (!line1.empty()) {\n                stringstream ss(line1);\n                string item;\n                while (getline(ss, item, ',')) {\n                    coins.push_back(stoi(item));\n                }\n            }\n        }\n        int amount = stoi(line2);\n        Solution sol;\n        cout << sol.coinChange(coins, amount) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int coinChange(int[] coins, int amount) {\n        // Your logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        if (scanner.hasNextLine()) {\n            String line1 = scanner.nextLine().trim();\n            String line2 = scanner.nextLine().trim();\n            if (line1.length() >= 2) {\n                line1 = line1.substring(1, line1.length() - 1);\n            }\n            int[] coins;\n            if (line1.isEmpty()) {\n                coins = new int[0];\n            } else {\n                String[] parts = line1.split(\",\");\n                coins = new int[parts.length];\n                for (int i = 0; i < parts.length; i++) {\n                    coins[i] = Integer.parseInt(parts[i].trim());\n                }\n            }\n            int amount = Integer.parseInt(line2);\n            Solution sol = new Solution();\n            System.out.println(sol.coinChange(coins, amount));\n        }\n    }\n}",
        "javascript": "/**\n * @param {number[]} coins\n * @param {number} amount\n * @return {number}\n */\nvar coinChange = function(coins, amount) {\n    // Your logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync('/dev/stdin', 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const coins = JSON.parse(input[0]);\n    const amount = JSON.parse(input[1]);\n    console.log(JSON.stringify(coinChange(coins, amount)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint coinChange(int* coins, int coinsSize, int amount) {\n    // Your logic here\n    return 0;\n}\n\nint main() {\n    char line1[100000];\n    char line2[1000];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        line1[strcspn(line1, \"\\r\\n\")] = 0;\n        line2[strcspn(line2, \"\\r\\n\")] = 0;\n        int capacity = 100;\n        int* coins = malloc(capacity * sizeof(int));\n        int size = 0;\n        char* ptr = line1;\n        while (*ptr && *ptr != '[') ptr++;\n        if (*ptr == '[') ptr++;\n        while (*ptr && *ptr != ']') {\n            int val;\n            int charsRead;\n            if (sscanf(ptr, \"%d%n\", &val, &charsRead) == 1) {\n                if (size >= capacity) {\n                    capacity *= 2;\n                    coins = realloc(coins, capacity * sizeof(int));\n                }\n                coins[size++] = val;\n                ptr += charsRead;\n            } else {\n                ptr++;\n            }\n        }\n        int amount = atoi(line2);\n        printf(\"%d\\n\", coinChange(coins, size, amount));\n        free(coins);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,5]\\n11", "expected_output": "3", "is_sample": True},
        {"input": "[2]\\n3", "expected_output": "-1", "is_sample": True},
        {"input": "[1]\\n0", "expected_output": "0", "is_sample": True},
        {"input": "[2,4]\\n7", "expected_output": "-1", "is_sample": False},
        {"input": "[10]\\n10", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,5,10,20,50]\\n100", "expected_output": "2", "is_sample": False},
        {"input": "[186,419,83,408]\\n6249", "expected_output": "20", "is_sample": False},
        # Stress cases
        {"input": "[1,2,5]\\n10000", "expected_output": "2000", "is_sample": False},
        {"input": "[10,20,50]\\n9999", "expected_output": "-1", "is_sample": False},
        {"input": "[100,200,500]\\n10000", "expected_output": "20", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Breadth-First Search"],
        "companyIndex": 0
    }

    output_path = "201-400/322_Coin_Change.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
