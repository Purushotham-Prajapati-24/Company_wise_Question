import json
import os

def generate_json():
    problem_id = 256
    title = "Paint House"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>256. Paint House</h3>
<p>There is a row of <code>n</code> houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.</p>

<p>The cost of painting each house with a certain color is represented by an <code>n x 3</code> cost matrix <code>costs</code>.</p>

<ul>
	<li>For example, <code>costs[0][0]</code> is the cost of painting house 0 with the color red; <code>costs[1][2]</code> is the cost of painting house 1 with color green, and so on.</li>
</ul>

<p>Return <em>the minimum cost to paint all houses</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> costs = [[17,2,17],[16,16,5],[14,3,19]]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Paint house 0 into blue, house 1 into green, house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> costs = [[7,6,2]]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>costs.length == n</code></li>
	<li><code>costs[i].length == 3</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= costs[i][j] &lt;= 20</code></li>
</ul>"""

    input_format = "First line: Number of houses N. Next N lines: 3 space-separated integers representing the costs for red, blue, and green respectively."
    output_format = "An integer representing the minimum cost."
    
    constraints = [
        "1 <= n <= 100",
        "3 colors exactly.",
        "Adjacent houses must have different colors."
    ]
    
    explanation = """To minimize the painting cost:
1. **Dynamic Programming**: Let `dp[i][c]` be the minimum cost to paint house `i` with color `c`.
2. **Transition**:
   - `dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])`
   - `dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])`
   - `dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])`
3. **Space Optimization**: Since we only need the costs of house `i-1`, we can use three variables instead of an entire `dp` table.
4. **Complexity**:
   - Time: O(N) where N is the number of houses.
   - Space: O(1)."""
    
    answer = """class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        r, b, g = costs[0]
        
        for i in range(1, len(costs)):
            curr_r = costs[i][0] + min(b, g)
            curr_b = costs[i][1] + min(r, g)
            curr_g = costs[i][2] + min(r, b)
            r, b, g = curr_r, curr_b, curr_g
            
        return min(r, b, g)"""

    boilerplate = {
        "python": "import sys\n\ndef minCost(costs: list[list[int]]) -> int:\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().split()\n    if not lines: sys.exit()\n    n = int(lines[0])\n    costs = []\n    idx = 1\n    for _ in range(n):\n        costs.append([int(lines[idx]), int(lines[idx+1]), int(lines[idx+2])])\n        idx += 3\n    print(minCost(costs))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint minCost(vector<vector<int>>& costs) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (cin >> n) {\n        vector<vector<int>> costs(n, vector<int>(3));\n        for (int i = 0; i < n; i++) {\n            cin >> costs[i][0] >> costs[i][1] >> costs[i][2];\n        }\n        cout << minCost(costs) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int minCost(int[][] costs) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            int[][] costs = new int[n][3];\n            for (int i = 0; i < n; i++) {\n                costs[i][0] = sc.nextInt();\n                costs[i][1] = sc.nextInt();\n                costs[i][2] = sc.nextInt();\n            }\n            System.out.println(new Solution().minCost(costs));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction minCost(costs) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    let n = parseInt(input[0]);\n    let costs = [];\n    let idx = 1;\n    for (let i = 0; i < n; i++) {\n        costs.push([parseInt(input[idx++]), parseInt(input[idx++]), parseInt(input[idx++])]);\n    }\n    console.log(minCost(costs));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint minCost(int** costs, int costsSize, int* costsColSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        int** costs = (int**)malloc(n * sizeof(int*));\n        int* cols = (int*)malloc(n * sizeof(int));\n        for (int i = 0; i < n; i++) {\n            costs[i] = (int*)malloc(3 * sizeof(int));\n            scanf(\"%d %d %d\", &costs[i][0], &costs[i][1], &costs[i][2]);\n            cols[i] = 3;\n        }\n        printf(\"%d\\n\", minCost(costs, n, cols));\n        \n        for (int i = 0; i < n; i++) free(costs[i]);\n        free(costs);\n        free(cols);\n    }\n    return 0;\n}"
    }

    def create_tc(costs):
        res = [str(len(costs))]
        for cost in costs:
            res.append(f"{cost[0]} {cost[1]} {cost[2]}")
        return "\\n".join(res)

    test_cases = [
        {"input": create_tc([[17,2,17],[16,16,5],[14,3,19]]), "expected_output": "10", "is_sample": True},
        {"input": create_tc([[7,6,2]]), "expected_output": "2", "is_sample": True},
        {"input": create_tc([[1,1,1],[1,1,1]]), "expected_output": "2", "is_sample": False},
        {"input": create_tc([[1,2,3],[4,5,6],[7,8,9]]), "expected_output": "13", "is_sample": False},
        {"input": create_tc([[20,20,20],[1,1,1]]), "expected_output": "21", "is_sample": False},
        {"input": create_tc([[10,10,10],[1,10,10],[10,1,10]]), "expected_output": "12", "is_sample": False},
        {"input": create_tc([[5,5,5],[5,5,5],[5,5,5]]), "expected_output": "15", "is_sample": False},
    ]
    
    def _solve_paint(costs):
        if not costs: return 0
        r, b, g = costs[0]
        for i in range(1, len(costs)):
            nr = costs[i][0] + min(b, g)
            nb = costs[i][1] + min(r, g)
            ng = costs[i][2] + min(r, b)
            r, b, g = nr, nb, ng
        return min(r, b, g)

    # Stress 8: 100 identical rows
    c8 = [[10, 10, 10]] * 100
    test_cases.append({"input": create_tc(c8), "expected_output": str(_solve_paint(c8)), "is_sample": False})
    # Stress 9: Max cost vs Min cost
    c9 = [[20, 1, 20]] * 100
    test_cases.append({"input": create_tc(c9), "expected_output": str(_solve_paint(c9)), "is_sample": False})
    # Stress 10: Mixed pattern
    c10 = [[i%20 + 1, (i+5)%20 + 1, (i+10)%20 + 1] for i in range(100)]
    test_cases.append({"input": create_tc(c10), "expected_output": str(_solve_paint(c10)), "is_sample": False})

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
        "topics": ["Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "201-400/256_Paint_House.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
