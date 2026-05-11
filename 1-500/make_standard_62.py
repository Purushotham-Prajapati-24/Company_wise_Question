import json
import os
import math

def generate_json():
    problem_id = 62
    title = "Unique Paths"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>62. Unique Paths</h3>
<p>There is a robot on an <code>m x n</code> grid. The robot is initially located at the <strong>top-left corner</strong> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>

<p>Given the two integers <code>m</code> and <code>n</code>, return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<p>The test cases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;" />
<pre>
<strong>Input:</strong> m = 3, n = 7
<strong>Output:</strong> 28
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> m = 3, n = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> From the top-left corner, there are a total of 3 paths to reach the bottom-right corner:
1. Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right
3. Down -&gt; Right -&gt; Down
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>"""

    input_format = "Two space-separated integers 'm' and 'n'."
    output_format = "An integer representing the number of unique paths."
    
    constraints = [
        "1 <= m, n <= 100",
        "The robot can only move either down or right.",
        "The answer will be less than or equal to 2 * 10^9."
    ]
    
    explanation = """To find the number of unique paths from the top-left to the bottom-right corner of an m x n grid:
1. **Observation**: To reach the destination `(m-1, n-1)` from `(0, 0)`, the robot MUST take exactly `m-1` vertical moves (Down) and `n-1` horizontal moves (Right), totaling `(m-1) + (n-1) = m + n - 2` moves.
2. **Combinatorial Solution**:
   - The problem is equivalent to choosing `m-1` positions for "Down" moves out of the `m+n-2` total moves.
   - This can be calculated using the binomial coefficient formula: `C(N, k) = N! / (k! * (N-k)!)`, where `N = m + n - 2` and `k = m - 1`.
   - Alternatively, we can use `k = n - 1` since `C(N, k) = C(N, N-k)`.
3. **Dynamic Programming Solution**:
   - Let `dp[i][j]` be the number of unique paths to reach cell `(i, j)`.
   - The robot can reach `(i, j)` either from `(i-1, j)` (move Down) or from `(i, j-1)` (move Right).
   - Thus, the recurrence relation is: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.
   - Base Cases: `dp[0][j] = 1` and `dp[i][0] = 1` for all `i, j`.
4. **Complexity**:
   - Combinatorial approach: Time O(min(m, n)), Space O(1).
   - DP approach: Time O(m*n), Space O(m*n) or O(min(m, n)) with optimization."""
    
    answer = """import math

def uniquePaths(m, n):
    # Combinatorial solution using binomial coefficient formula
    # Total moves = (m-1) + (n-1)
    # Number of ways = Combination(Total moves, m-1)
    return math.comb(m + n - 2, m - 1)"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys, re\n\ndef uniquePaths(m, n):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'\\d+', data)]\n    if len(nums) >= 2:\n        print(uniquePaths(nums[0], nums[1]))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int uniquePaths(int m, int n) {\n        // User Logic Here\n        return 0;\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(\"\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    vector<int> nums;\n    while (iter != end) { nums.push_back(stoi(iter->str())); iter++; }\n    if (nums.size() >= 2) {\n        Solution sol;\n        cout << sol.uniquePaths(nums[0], nums[1]) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int uniquePaths(int m, int n) {\n        // User Logic Here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"\\\\d+\").matcher(input);\n        List<Integer> list = new ArrayList<>();\n        while (m.find()) list.add(Integer.parseInt(m.group()));\n        if (list.size() >= 2) {\n            Solution sol = new Solution();\n            System.out.println(sol.uniquePaths(list.get(0), list.get(1)));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number} m\n * @param {number} n\n * @return {number}\n */\nvar uniquePaths = function(m, n) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const nums = (input.match(/\\d+/g) || []).map(Number);\n    if (nums.length >= 2) {\n        console.log(uniquePaths(nums[0], nums[1]));\n    }\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint uniquePaths(int m, int n) {\n    // User Logic Here\n    return 0;\n}\n\nint main() {\n    int nums[2], count = 0, found = 0, c;\n    long long current = 0;\n    while ((c = getchar()) != EOF && count < 2) {\n        if (isdigit(c)) {\n            if (!found) { found = 1; current = c - '0'; } else current = current * 10 + (c - '0');\n        } else {\n            if (found) { nums[count++] = (int)current; found = 0; }\n        }\n    }\n    if (found && count < 2) nums[count++] = (int)current;\n    if (count >= 2) {\n        printf(\"%d\\n\", uniquePaths(nums[0], nums[1]));\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "3 7", "expected_output": "28", "is_sample": True},
        {"input": "3 2", "expected_output": "3", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "1 1", "expected_output": "1", "is_sample": False},
        {"input": "1 100", "expected_output": "1", "is_sample": False},
        {"input": "100 1", "expected_output": "1", "is_sample": False},
        {"input": "2 2", "expected_output": "2", "is_sample": False},
        {"input": "10 10", "expected_output": "48620", "is_sample": False},
        # Last three: Stress tests
        {"input": "100 2", "expected_output": "100", "is_sample": False},
        {"input": "23 12", "expected_output": "193536720", "is_sample": False},
        {"input": "51 9", "expected_output": "1916797311", "is_sample": False}
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
        "topics": ["Math", "Dynamic Programming", "Combinatorics"],
        "companyIndex": 0
    }

    output_path = "1-200/62_Unique_Paths.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
