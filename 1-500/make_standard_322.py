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
        "python": "import sys\nimport json\nimport re\n\ndef coinChange(coins: list[int], amount: int) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    array_match = re.search(r'\\[[\\d\\s,.-]*\\]', raw_input)\n    if array_match:\n        coins = json.loads(array_match.group(0))\n        remaining = raw_input.replace(array_match.group(0), '')\n        amount_match = re.search(r'(?:amount\\s*=\\s*)?(\\d+)', remaining)\n        amount = int(amount_match.group(1)) if amount_match else 0\n    else:\n        nums = [int(x) for x in re.findall(r'-?\\d+', raw_input)]\n        if not nums: coins, amount = [], 0\n        else: coins, amount = nums[:-1], nums[-1]\n    print(coinChange(coins, amount))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nint coinChange(vector<int>& coins, int amount) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    regex re_arr(\"\\\\[[\\\\d\\\\s,.-]*\\\\]\");\n    smatch m;\n    vector<int> coins;\n    int amount = 0;\n    if (regex_search(input, m, re_arr)) {\n        string arr_str = m.str();\n        regex re_num(\"-?\\\\d+\");\n        auto it = sregex_iterator(arr_str.begin(), arr_str.end(), re_num);\n        for (; it != sregex_iterator(); ++it) coins.push_back(stoi(it->str()));\n        \n        string remaining = input.replace(input.find(arr_str), arr_str.length(), \" \");\n        if (regex_search(remaining, m, re_num)) amount = stoi(m.str());\n    } else {\n        regex re_num(\"-?\\\\d+\");\n        auto it = sregex_iterator(input.begin(), input.end(), re_num);\n        vector<int> nums;\n        for (; it != sregex_iterator(); ++it) nums.push_back(stoi(it->str()));\n        if (!nums.empty()) {\n            amount = nums.back(); nums.pop_back();\n            coins = nums;\n        }\n    }\n    cout << coinChange(coins, amount) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int coinChange(int[] coins, int amount) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while(sc.hasNext()) sb.append(sc.next()).append(\" \");\n        String input = sb.toString();\n        \n        Pattern pArr = Pattern.compile(\"\\\\[[\\\\d\\\\s,.-]*\\\\]\");\n        Matcher mArr = pArr.matcher(input);\n        int[] coins;\n        int amount = 0;\n        if (mArr.find()) {\n            String arrStr = mArr.group();\n            Matcher mNum = Pattern.compile(\"-?\\\\d+\").matcher(arrStr);\n            List<Integer> list = new ArrayList<>();\n            while(mNum.find()) list.add(Integer.parseInt(mNum.group()));\n            coins = list.stream().mapToInt(i->i).toArray();\n            \n            String remaining = input.replace(arrStr, \" \");\n            Matcher mAmt = Pattern.compile(\"\\\\d+\").matcher(remaining);\n            if (mAmt.find()) amount = Integer.parseInt(mAmt.group());\n        } else {\n            Matcher mNum = Pattern.compile(\"-?\\\\d+\").matcher(input);\n            List<Integer> list = new ArrayList<>();\n            while(mNum.find()) list.add(Integer.parseInt(mNum.group()));\n            if (list.isEmpty()) { coins = new int[0]; } else {\n                amount = list.remove(list.size()-1);\n                coins = list.stream().mapToInt(i->i).toArray();\n            }\n        }\n        System.out.println(new Solution().coinChange(coins, amount));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction coinChange(coins, amount) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst arrayMatch = input.match(/\\[[\\d\\s,.-]*\\]/);\nlet coins = [], amount = 0;\nif (arrayMatch) {\n    coins = JSON.parse(arrayMatch[0]);\n    const remaining = input.replace(arrayMatch[0], ' ');\n    const amountMatch = remaining.match(/\\d+/);\n    amount = amountMatch ? parseInt(amountMatch[0]) : 0;\n} else {\n    const nums = (input.match(/-?\\d+/g) || []).map(Number);\n    if (nums.length) {\n        amount = nums.pop();\n        coins = nums;\n    }\n}\nconsole.log(coinChange(coins, amount));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint coinChange(int* coins, int coinsSize, int amount) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) != 1) return 0;\n    int* coins = malloc(sizeof(int) * n);\n    for(int i=0; i<n; i++) scanf(\"%d\", &coins[i]);\n    int amount;\n    scanf(\"%d\", &amount);\n    printf(\"%d\\n\", coinChange(coins, n, amount));\n    return 0;\n}"
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
