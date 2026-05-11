import json
import os

def generate_json():
    problem_id = 351
    title = "Android Unlock Patterns"
    difficulty = "Medium"
    marks = 10

    html_description = """<h3>351. Android Unlock Patterns</h3>
<p>Android devices have a special lock screen with a <code>3 x 3</code> grid of dots. Users can set an unlock pattern by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoint is the next dot. A sequence of <code>k</code> dots that are all distinct and not all the same is called a valid unlock pattern of length <code>k</code>.</p>
<p>Rules for valid patterns:</p>
<ul>
\t<li>All dots in the pattern must be distinct.</li>
\t<li>If a line segment connecting two consecutive dots in the pattern passes through any other dot, that dot must have previously been included in the pattern.</li>
</ul>
<p>Given two integers <code>m</code> and <code>n</code>, return <em>the number of unique and valid unlock patterns of length at least </em><code>m</code><em> and at most </em><code>n</code>.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> m = 1, n = 1
<strong>Output:</strong> 9
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> m = 1, n = 2
<strong>Output:</strong> 65
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>1 &lt;= m, n &lt;= 9</code></li>
</ul>"""

    input_format = "Two integers `m` and `n` on a single line, space-separated."
    output_format = "A single integer: number of valid unlock patterns of length `m` to `n`."

    constraints = ["1 <= m <= n <= 9"]

    explanation = """Use **backtracking** with a precomputed `skip` table.

### Precomputing Skip:
- `skip[i][j]` = the dot that must be visited before going from `i` to `j` (or 0 if no skip required).
- Examples: `skip[1][3] = 2`, `skip[1][7] = 4`, `skip[1][9] = 5`.

### Backtracking:
- From each starting dot, try all unvisited next dots.
- A move to `next` is valid only if `skip[curr][next] == 0` or `skip[curr][next]` was already visited.
- Count all valid sequences of length `m` to `n`.

### Complexity: O(n! · 9) — bounded by at most 9! sequences."""

    answer = """def numberOfPatterns(m: int, n: int) -> int:
    skip = [[0]*10 for _ in range(10)]
    skip[1][3] = skip[3][1] = 2
    skip[1][7] = skip[7][1] = 4
    skip[3][9] = skip[9][3] = 6
    skip[7][9] = skip[9][7] = 8
    skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5

    def dfs(curr, remaining, visited):
        if remaining == 0:
            return 1
        count = 0
        for nxt in range(1, 10):
            if not visited[nxt] and (skip[curr][nxt] == 0 or visited[skip[curr][nxt]]):
                visited[nxt] = True
                count += dfs(nxt, remaining - 1, visited)
                visited[nxt] = False
        return count

    total = 0
    visited = [False] * 10
    for length in range(m, n + 1):
        # 1,3,7,9 symmetric; 2,4,6,8 symmetric; 5 unique
        visited[1] = True
        total += dfs(1, length - 1, visited) * 4
        visited[1] = False
        visited[2] = True
        total += dfs(2, length - 1, visited) * 4
        visited[2] = False
        visited[5] = True
        total += dfs(5, length - 1, visited)
        visited[5] = False
    return total"""

    boilerplate = {
        "python": "import sys\nimport re\n\nclass Solution:\n    def numberOfPatterns(self, m: int, n: int) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', input_data)]\n    if len(nums) >= 2:\n        sol = Solution()\n        print(sol.numberOfPatterns(nums[0], nums[1]))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\nusing namespace std;\n\nclass Solution {\npublic:\n    int numberOfPatterns(int m, int n) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string input; char ch;\n    while (cin.get(ch)) input += ch;\n    regex re(\"-?\\\\d+\");\n    auto b = sregex_iterator(input.begin(), input.end(), re);\n    auto e = sregex_iterator();\n    vector<int> nums;\n    for (auto i = b; i != e; ++i) nums.push_back(stoi(i->str()));\n    if (nums.size() >= 2) {\n        Solution sol;\n        cout << sol.numberOfPatterns(nums[0], nums[1]) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int numberOfPatterns(int m, int n) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        List<Integer> nums = new ArrayList<>();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        while (m.find()) nums.add(Integer.parseInt(m.group()));\n        if (nums.size() >= 2) {\n            System.out.println(new Solution().numberOfPatterns(nums.get(0), nums.get(1)));\n        }\n    }\n}",
        "javascript": "\"use strict\";\nconst fs = require('fs');\n\nvar numberOfPatterns = function(m, n) {\n    // User logic here\n    return 0;\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const nums = input.match(/-?\\d+/g)?.map(Number) || [];\n    if (nums.length >= 2) {\n        console.log(numberOfPatterns(nums[0], nums[1]));\n    }\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\nint numberOfPatterns(int m, int n) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char *input = malloc(1000000);\n    int len = 0, c;\n    while ((c = getchar()) != EOF) input[len++] = c;\n    input[len] = '\\0';\n    int nums[2], count = 0;\n    char *p = input;\n    while (*p && count < 2) {\n        if (isdigit(*p) || (*p == '-' && isdigit(*(p+1)))) {\n            nums[count++] = strtol(p, &p, 10);\n        } else p++;\n    }\n    if (count >= 2) printf(\"%d\\n\", numberOfPatterns(nums[0], nums[1]));\n    return 0;\n}"
    }


    # Known answers (precomputed)
    known = {
        (1, 1): 9, (1, 2): 65, (1, 9): 389112,
        (2, 2): 56, (3, 3): 320, (4, 4): 1624,
        (5, 5): 7152, (6, 6): 26016, (7, 7): 72912,
        (8, 8): 140704, (9, 9): 140704,
        (1, 3): 385, (2, 9): 389103, (3, 9): 389047
    }

    test_cases = [
        # 2 sample cases
        {"input": "1 1", "expected_output": "9", "is_sample": True},
        {"input": "1 2", "expected_output": "65", "is_sample": True},
        # 5 diverse cases
        {"input": "1 9", "expected_output": "389112", "is_sample": False},
        {"input": "2 2", "expected_output": "56", "is_sample": False},
        {"input": "3 3", "expected_output": "320", "is_sample": False},
        {"input": "4 4", "expected_output": "1624", "is_sample": False},
        {"input": "5 5", "expected_output": "7152", "is_sample": False},
        # 3 stress cases (maximum n values)
        {"input": "6 6", "expected_output": "26016", "is_sample": False},
        {"input": "9 9", "expected_output": "140704", "is_sample": False},
        {"input": "2 9", "expected_output": "389103", "is_sample": False},
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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Dynamic Programming", "Backtracking"],
        "companyIndex": 1
    }

    output_path = "301-500/351_Android_Unlock_Patterns.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
