import json
import os

def generate_json():
    problem_id = 934
    title = "Shortest Bridge"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>934. Shortest Bridge</h3>
<p>You are given an <code>n x n</code> binary matrix <code>grid</code> where <code>1</code> represents land and <code>0</code> represents water.</p>

<p>An <strong>island</strong> is a 4-directionally connected group of <code>1</code>'s not connected to any other <code>1</code>'s. There are <strong>exactly two islands</strong> in <code>grid</code>.</p>

<p>You may change <code>0</code>'s to <code>1</code>'s to connect the two islands to form <strong>one island</strong>.</p>

<p>Return <em>the smallest number of <code>0</code>'s you must flip to connect the two islands</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,1],[1,0]]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,1,0],[0,0,0],[0,0,1]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li>There are exactly two islands in <code>grid</code>.</li>
</ul>"""

    input_format = "An integer n for grid size, followed by n x n space-separated integers."
    output_format = "An integer representing the minimum flips."
    
    constraints = ["2 <= n <= 100", "Exactly two islands.", "Smallest flips to connect."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """from collections import deque

def shortestBridge(grid):
    n = len(grid)
    first_island = []
    found = False
    for r in range(n):
        if found: break
        for c in range(n):
            if grid[r][c] == 1:
                # DFS to find first island
                q = deque([(r, c)])
                grid[r][c] = 2
                while q:
                    curr_r, curr_c = q.popleft()
                    first_island.append((curr_r, curr_c))
                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                found = True
                break
    
    # BFS from first island
    q = deque(first_island)
    dist = 0
    while q:
        for _ in range(len(q)):
            curr_r, curr_c = q.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 1:
                        return dist
                    elif grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        dist += 1
    return dist"""

    boilerplate = {
        "python": "import sys\n\ndef shortestBridge(grid):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    grid = input_data[0] if len(input_data) > 0 else \"\"\n    print(shortestBridge(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint shortestBridge(string grid) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string grid; cin >> grid;\n    cout << shortestBridge(grid) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
