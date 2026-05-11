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
        "python": "import sys, json\n\ndef totalNQueens(n):\n    # implementation\n    pass\n\nif __name__ == '__main__':\n    data = json.loads(sys.stdin.read())\n    print(totalNQueens(data['n']))",
        "cpp": "#include <iostream>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int totalNQueens(int n) {\n        // implementation\n        return 0;\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public int totalNQueens(int n) {\n        // implementation\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {number} n\n * @return {number}\n */\nvar totalNQueens = function(n) {\n    \n};",
        "c": "int totalNQueens(int n){\n    \n}"
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
