import json
import os

def generate_json():
    problem_id = 59
    title = "Spiral Matrix II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>59. Spiral Matrix II</h3>
<p>Given a positive integer <code>n</code>, generate an <code>n x n</code> <code>matrix</code> filled with elements from <code>1</code> to <code>n<sup>2</sup></code> in spiral order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [[1,2,3],[8,9,4],[7,6,5]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [[1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
</ul>"""

    input_format = "A single integer n representing the size of the matrix."
    output_format = "An n x n 2D array representing the spiral matrix."
    
    constraints = [
        "1 <= n <= 20"
    ]
    
    explanation = """To generate an n x n matrix in spiral order:
1. **Initialize Matrix**: Create an `n x n` 2D array filled with zeros.
2. **Initialize Boundaries**:
   - `top = 0`, `bottom = n - 1`
   - `left = 0`, `right = n - 1`
   - `curr_val = 1`
3. **Fill Matrix**: Iterate while `curr_val <= n * n`:
   - **Traverse Right**: Fill the `top` row from `left` to `right`. Increment `top`.
   - **Traverse Down**: Fill the `right` column from `top` to `bottom`. Decrement `right`.
   - **Traverse Left**: Fill the `bottom` row from `right` to `left`. Decrement `bottom`.
   - **Traverse Up**: Fill the `left` column from `bottom` to `top`. Increment `left`.
4. Return the generated matrix.

As the size `n` is small (up to 20), this simulation is very efficient.
Time Complexity: O(n^2), as we fill exactly n*n cells.
Space Complexity: O(1) (excluding the space for the result matrix)."""
    
    answer = """def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    rows, cols = n, n
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    
    num = 1
    while num <= n * n:
        # Move Right
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1
        
        # Move Down
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # Move Left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
            
        # Move Up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
    return matrix"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef generateMatrix(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        n = int(input_data)\n        print(generateMatrix(n))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<vector<int>> generateMatrix(int n) {\n    // User logic\n    return {};\n}\n\nint main() {\n    int n; cin >> n;\n    // logic to print result matrix\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int[][] generateMatrix(int n) {\n        // User logic\n        return new int[n][n];\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            int[][] res = generateMatrix(n);\n            System.out.println(Arrays.deepToString(res));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction generateMatrix(n) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    console.log(generateMatrix(parseInt(input)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint** generateMatrix(int n, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    return NULL;\n}\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
    }

    def _gen_matrix(n):
        res = [[0]*n for _ in range(n)]
        t, b, l, r, v = 0, n-1, 0, n-1, 1
        while v <= n*n:
            for j in range(l, r+1): res[t][j], v = v, v+1
            t += 1
            for i in range(t, b+1): res[i][r], v = v, v+1
            r -= 1
            if t <= b:
                for j in range(r, l-1, -1): res[b][j], v = v, v+1
                b -= 1
            if l <= r:
                for i in range(b, t-1, -1): res[i][l], v = v, v+1
                l += 1
        return res

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "3", "expected_output": str(_gen_matrix(3)), "is_sample": True},
        {"input": "1", "expected_output": str(_gen_matrix(1)), "is_sample": True},
        # Middle five: Diverse cases
        {"input": "2", "expected_output": str(_gen_matrix(2)), "is_sample": False},
        {"input": "4", "expected_output": str(_gen_matrix(4)), "is_sample": False},
        {"input": "5", "expected_output": str(_gen_matrix(5)), "is_sample": False},
        {"input": "6", "expected_output": str(_gen_matrix(6)), "is_sample": False},
        {"input": "10", "expected_output": str(_gen_matrix(10)), "is_sample": False},
        # Last three: Stress tests
        {"input": "15", "expected_output": str(_gen_matrix(15)), "is_sample": False},
        {"input": "20", "expected_output": str(_gen_matrix(20)), "is_sample": False},
        {"input": "2", "expected_output": str(_gen_matrix(2)), "is_sample": False}
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
        "topics": ["Array", "Matrix", "Simulation"],
        "companyIndex": 0
    }

    output_path = "1-200/59_Spiral_Matrix_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
