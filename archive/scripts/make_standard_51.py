import json
import os

def generate_json():
    problem_id = 51
    title = "N-Queens"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>51. N-Queens</h3>
<p>The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an <code>n x n</code> chessboard such that no two queens attack each other.</p>

<p>Given an integer <code>n</code>, return <em>all distinct solutions to the <strong>n-queens puzzle</strong></em>. You may return the answer in <strong>any order</strong>.</p>

<p>Each solution contains a distinct board configuration of the n-queens' placement, where <code>'Q'</code> and <code>'.'</code> both indicate a queen and an empty space, respectively.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
<strong>Explanation:</strong> There exist two distinct solutions to the 4-queens puzzle as shown above.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [["Q"]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
</ul>"""

    input_format = "An integer n representing the size of the board."
    output_format = "A list of distinct board configurations (2D list of strings)."
    
    constraints = [
        "1 <= n <= 9"
    ]
    
    explanation = """To find all N-Queens solutions:
1. **Backtracking**:
   - Place queens row by row from 0 to $n-1$.
   - Maintain column and diagonal occupancy sets:
     - `cols`: `j` is occupied.
     - `pos_diag`: `i + j` is constant.
     - `neg_diag`: `i - j` is constant.
2. **Path Maintenance**:
   - When placing a queen at $(i, j)$, check if `j` in `cols`, `i+j` in `pos_diag`, or `i-j` in `neg_diag`.
   - If acceptable, mark as occupied and move to row $i+1$.
   - Record the column index `j` for row `i`.
3. **Board Conversion**:
   - For each valid complete assignment of columns, construct the board string representations.
4. **Complexity**:
   - **Time**: $O(N!)$ - many branches are pruned early.
   - **Space**: $O(N^2)$ to store the solutions."""
    
    answer = """def solveNQueens(n):
    res = []
    board = [["."] * n for _ in range(n)]
    
    cols = set()
    pos_diag = set() # (r + c)
    neg_diag = set() # (r - c)
    
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
            
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
                
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"
            
            backtrack(r + 1)
            
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."
            
    backtrack(0)
    return res"""

    boilerplate = {
        "python": "import sys, json\n\ndef solveNQueens(n):\n    # implementation\n    pass\n\nif __name__ == '__main__':\n    data = json.loads(sys.stdin.read())\n    print(solveNQueens(data['n']))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<vector<string>> solveNQueens(int n) {\n        // implementation\n        return {};\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<List<String>> solveNQueens(int n) {\n        // implementation\n        return new ArrayList<>();\n    }\n}",
        "javascript": "/**\n * @param {number} n\n * @return {string[][]}\n */\nvar solveNQueens = function(n) {\n    \n};",
        "c": "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the arrays are returned as *returnColumnSizes array.\n * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().\n */\nchar*** solveNQueens(int n, int* returnSize, int** returnColumnSizes){\n    \n}"
    }

    def solveNQueens(n):
        res = []
        board = [["."] * n for _ in range(n)]
        
        cols = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
                
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                    
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return res

    test_cases = [
        {"input": '{"n": 4}', "expected_output": json.dumps(solveNQueens(4)).replace(' ', ''), "is_sample": True},
        {"input": '{"n": 1}', "expected_output": json.dumps(solveNQueens(1)).replace(' ', ''), "is_sample": True},
        {"input": '{"n": 2}', "expected_output": json.dumps(solveNQueens(2)).replace(' ', ''), "is_sample": False},
        {"input": '{"n": 3}', "expected_output": json.dumps(solveNQueens(3)).replace(' ', ''), "is_sample": False},
        {"input": '{"n": 5}', "expected_output": json.dumps(solveNQueens(5)).replace(' ', ''), "is_sample": False},
        {"input": '{"n": 6}', "expected_output": json.dumps(solveNQueens(6)).replace(' ', ''), "is_sample": False},
        {"input": '{"n": 7}', "expected_output": json.dumps(solveNQueens(7)).replace(' ', ''), "is_sample": False},
        # Stress cases
        {"input": '{"n": 8}', "expected_output": json.dumps(solveNQueens(8)).replace(' ', ''), "is_sample": False},
        {"input": '{"n": 9}', "expected_output": json.dumps(solveNQueens(9)).replace(' ', ''), "is_sample": False},
        {"input": '{"n": 9}', "expected_output": json.dumps(solveNQueens(9)).replace(' ', ''), "is_sample": False}
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

    output_path = "1-100/51_N-Queens.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
