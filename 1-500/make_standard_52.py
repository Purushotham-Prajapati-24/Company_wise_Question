import json
import os

def generate_json():
    problem_id = 52
    title = "N-Queens II"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>52. N-Queens II</h3>
<p>The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an <code>n x n</code> chessboard such that no two queens attack each other.</p>

<p>Given an integer <code>n</code>, return <em>the number of distinct solutions to the <strong>n-queens puzzle</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There exist two distinct solutions to the 4-queens puzzle as shown below.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
</ul>"""

    input_format = "An integer n representing the size of the board."
    output_format = "An integer representing the count of distinct solutions."
    
    constraints = [
        "1 <= n <= 9"
    ]
    
    explanation = """To find the number of distinct N-Queens solutions:
1. **Backtracking**:
   - Place queens row by row.
   - Maintain column and diagonal occupancy sets:
     - `cols`: `j` is occupied.
     - `pos_diag`: `i + j` is constant.
     - `neg_diag`: `i - j` is constant.
2. **Path Maintenance**:
   - When placing a queen at $(i, j)$, check if `j` in `cols`, `i+j` in `pos_diag`, or `i-j` in `neg_diag`.
   - Instead of building the board configurations, just increment a counter when a solution is reached ($i == n$).
3. **Complexity**:
   - **Time**: $O(N!)$ - many branches are pruned early.
   - **Space**: $O(N)$ to store the sets."""
    
    answer = """def totalNQueens(n):
    count = 0
    
    cols = set()
    pos_diag = set() # (r + c)
    neg_diag = set() # (r - c)
    
    def backtrack(r):
        nonlocal count
        if r == n:
            count += 1
            return
            
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
                
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            
            backtrack(r + 1)
            
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            
    backtrack(0)
    return count"""

    boilerplate = {
        "python": "import sys\n\ndef totalNQueens(n):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    import re\n    input_data = sys.stdin.read()\n    match = re.search(r'\\d+', input_data)\n    if match:\n        n = int(match.group())\n        print(totalNQueens(n))",
        "cpp": "#include <iostream>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int totalNQueens(int n) {\n        // User Logic Here\n        return 0;\n    }\n};\n\nint main() {\n    string input;\n    string line;\n    while (getline(cin, line)) input += line + \" \";\n    regex rgx(\"\\\\d+\");\n    smatch match;\n    int n = 0;\n    if (regex_search(input, match, rgx)) {\n        n = stoi(match.str());\n    }\n    Solution sol;\n    cout << sol.totalNQueens(n) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int totalNQueens(int n) {\n        // User Logic Here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"\\\\d+\").matcher(input);\n        int n = 0;\n        if (m.find()) n = Integer.parseInt(m.group());\n        Solution sol = new Solution();\n        System.out.println(sol.totalNQueens(n));\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number} n\n * @return {number}\n */\nvar totalNQueens = function(n) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const match = input.match(/\\d+/);\n    if (!match) return;\n    const n = parseInt(match[0]);\n    console.log(totalNQueens(n));\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint totalNQueens(int n){\n    // User Logic Here\n    return 0;\n}\n\nint main() {\n    char buffer[1024];\n    int n = 0;\n    if (fgets(buffer, sizeof(buffer), stdin)) {\n        char* p = buffer;\n        while (*p && !isdigit(*p)) p++;\n        if (*p) n = atoi(p);\n    }\n    printf(\"%d\\n\", totalNQueens(n));\n    return 0;\n}"
    }

    test_cases = [
        {"input": '{"n": 4}', "expected_output": "2", "is_sample": True},
        {"input": '{"n": 1}', "expected_output": "1", "is_sample": True},
        {"input": '{"n": 2}', "expected_output": "0", "is_sample": False},
        {"input": '{"n": 3}', "expected_output": "0", "is_sample": False},
        {"input": '{"n": 5}', "expected_output": "10", "is_sample": False},
        {"input": '{"n": 6}', "expected_output": "4", "is_sample": False},
        {"input": '{"n": 7}', "expected_output": "40", "is_sample": False},
        {"input": '{"n": 8}', "expected_output": "92", "is_sample": False},
        {"input": '{"n": 9}', "expected_output": "352", "is_sample": False},
        {"input": '{"n": 9}', "expected_output": "352", "is_sample": False}
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
        "topics": ["Array", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-100/52_N-Queens_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
