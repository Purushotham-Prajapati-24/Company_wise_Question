import json
import os

def generate_json():
    problem_id = 465
    title = "Optimal Account Balancing"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>465. Optimal Account Balancing</h3>
<p>You are given an array of <code>transactions</code> where <code>transactions[i] = [from<sub>i</sub>, to<sub>i</sub>, amount<sub>i</sub>]</code> indicates that the person with <code>ID = from<sub>i</sub></code> gave <code>amount<sub>i</sub></code> to the person with <code>ID = to<sub>i</sub></code>.</p>

<p>Return <em>the minimum number of transactions required to settle the debt</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> transactions = [[0,1,10],[2,0,5]]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 $5 and person #1 pays person #2 $5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #0 only needs to give person #1 $4, and all debt is settled.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= transactions.length &lt;= 8</code></li>
	<li><code>transactions[i].length == 3</code></li>
	<li><code>0 &lt;= from<sub>i</sub>, to<sub>i</sub> &lt; 12</code></li>
	<li><code>from<sub>i</sub> != to<sub>i</sub></code></li>
	<li><code>1 &lt;= amount<sub>i</sub> &lt;= 100</code></li>
</ul>"""

    input_format = "Line 1: A JSON 2D array `transactions` where `transactions[i] = [from, to, amount]`."
    output_format = "An integer representing the minimum number of transactions."
    
    constraints = [
        "1 <= transactions.length <= 8",
        "0 <= from_i, to_i < 12",
        "1 <= amount_i <= 100"
    ]
    
    explanation = "First, calculate the net balance for each person. Filter out people with zero balance. Then, use backtracking (DFS) to find the minimum transactions needed to zero out all balances. For the current person with non-zero balance, try settling their debt with every other person whose balance has the opposite sign."
    
    answer = """import collections

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = collections.defaultdict(int)
        for f, t, a in transactions:
            balances[f] -= a
            balances[t] += a
        
        vals = [v for v in balances.values() if v != 0]
        n = len(vals)
        
        def dfs(idx):
            while idx < n and vals[idx] == 0:
                idx += 1
            if idx == n: return 0
            
            res = float('inf')
            for i in range(idx + 1, n):
                if vals[i] * vals[idx] < 0:
                    vals[i] += vals[idx]
                    res = min(res, 1 + dfs(idx + 1))
                    vals[i] -= vals[idx]
            return res
            
        return dfs(0)"""

    boilerplate = {
        "python": "import sys\nimport json\nimport collections\n\nclass Solution:\n    def minTransfers(self, transactions: list[list[int]]) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        transactions = json.loads(line)\n        sol = Solution()\n        print(sol.minTransfers(transactions))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int minTransfers(vector<vector<int>>& transactions) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line; if (getline(cin, line)) {\n        vector<vector<int>> grid; string r; stringstream ss(line); \n        while (getline(ss, r, ']')) {\n            size_t start = r.find('[');\n            if (start != string::npos) {\n                vector<int> row; stringstream ss2(r.substr(start + 1)); string val;\n                while (getline(ss2, val, ',')) {\n                    if (!val.empty()) row.push_back(stoi(val));\n                }\n                if (!row.empty()) grid.push_back(row);\n            }\n        }\n        Solution sol; cout << sol.minTransfers(grid) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int minTransfers(int[][] transactions) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            String[] rows = line.substring(1, line.length() - 1).split(\"\\\\],\\\\s*\\\\[\");\n            List<int[]> list = new ArrayList<>();\n            for (String r : rows) {\n                String clean = r.replaceAll(\"[\\\\[\\\\]]\", \"\");\n                if (clean.isEmpty()) continue;\n                String[] nums = clean.split(\",\\\\s*\");\n                int[] row = new int[nums.length];\n                for (int i = 0; i < nums.length; i++) row[i] = Integer.parseInt(nums[i]);\n                list.add(row);\n            }\n            System.out.println(new Solution().minTransfers(list.toArray(new int[0][])));\n        }\n    }\n}",
        "javascript": "/**\n * @param {number[][]} transactions\n * @return {number}\n */\nvar minTransfers = function(transactions) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const transactions = JSON.parse(input);\n    console.log(minTransfers(transactions));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint minTransfers(int** transactions, int transactionsSize, int* transactionsColSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    printf(\"0\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[0,1,10],[2,0,5]]", "expected_output": "2", "is_sample": True},
        {"input": "[[0,1,10],[1,0,1],[1,2,5],[2,0,5]]", "expected_output": "1", "is_sample": True},
        {"input": "[[0,1,10]]", "expected_output": "1", "is_sample": False},
        {"input": "[[0,1,5],[1,0,5]]", "expected_output": "0", "is_sample": False},
        {"input": "[[0,1,10],[1,2,10],[2,0,10]]", "expected_output": "0", "is_sample": False},
        {"input": "[[0,1,10],[2,1,10]]", "expected_output": "2", "is_sample": False},
        {"input": "[[0,1,1],[2,3,1],[4,5,1]]", "expected_output": "3", "is_sample": False},
        {"input": "[[0,1,5],[2,3,5],[1,2,5],[3,0,5]]", "expected_output": "0", "is_sample": False},
        {"input": "[[0,1,10],[1,2,5],[2,0,10]]", "expected_output": "2", "is_sample": False},
        {"input": "[[0,1,10],[3,4,20]]", "expected_output": "2", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Backtracking", "Bitmask"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Optimal_Account_Balancing.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
