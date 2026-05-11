import json
import os

def generate_json():
    problem_id = 573
    title = "Squirrel Simulation"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>573. Squirrel Simulation</h3>
<p>There is a squirrel and a tree in a 2D grid. The squirrel must collect all nuts and bring them to the tree one by one. The squirrel can only carry one nut at a time.</p>

<p>The distance is the Manhattan distance: <code>|r1 - r2| + |c1 - c2|</code>.</p>

<p>You are given <code>height</code> and <code>width</code> representing the grid's size, the positions of the <code>tree</code>, the <code>squirrel</code>, and multiple <code>nuts</code>.</p>

<p>Return <em>the minimum total distance for the squirrel to collect all the nuts and put them into the tree one by one</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/squirrel1-grid.jpg" style="width: 493px; height: 577px;" />
<pre>
<strong>Input:</strong> height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [2,5]]
<strong>Output:</strong> 12
<strong>Explanation:</strong> 
- Nut 1: squirrel to [3,0] (distance 5), then [3,0] to [2,2] (distance 3). Total: 8.
- Nut 2: [2,2] to [2,5] (distance 3), then [2,5] to [2,2] (distance 3). Total: 6.
- Grand total: 8 + 6 = 14. 
OR
- Nut 2: squirrel to [2,5] (distance 3), then [2,5] to [2,2] (distance 3). Total: 6.
- Nut 1: [2,2] to [3,0] (distance 3), then [3,0] to [2,2] (distance 3). Total: 6.
- Grand total: 6 + 6 = 12.
The minimum total distance is 12.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= height, width &lt;= 100</code></li>
	<li><code>tree.length == 2</code></li>
	<li><code>squirrel.length == 2</code></li>
	<li><code>1 &lt;= nuts.length &lt;= 5000</code></li>
	<li><code>nuts[i].length == 2</code></li>
</ul>
"""

    input_format = "Multiple lines: height, width, tree, squirrel, and nuts (each as space/comma separated)."
    output_format = "A single integer representing the minimum distance."
    
    constraints = [
        "1 <= height, width <= 100",
        "1 <= nuts.length <= 5000"
    ]
    
    explanation = """To find the minimum distance:
1. For every nut except the first one visited, the squirrel must travel from the tree to the nut and back to the tree (Manhattan distance * 2).
2. For the first nut visited, the squirrel travels from its starting position to the nut, then back to the tree.
3. The total distance is `sum(2 * distance(nut, tree))` for all nuts, minus the maximum "saving" we get by choosing the best first nut.
4. Saving for a nut = `distance(nut, tree) - distance(nut, squirrel)`."""
    
    answer = """def minDistance(height, width, tree, squirrel, nuts):
    def dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    total_dist = 0
    max_saving = -float('inf')
    
    for nut in nuts:
        d_nut_tree = dist(nut, tree)
        total_dist += 2 * d_nut_tree
        max_saving = max(max_saving, d_nut_tree - dist(nut, squirrel))
    
    return total_dist - max_saving"""

    boilerplate = {
        "python": "import sys\\n\\ndef minDistance(height, width, tree, squirrel, nuts):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    # Custom input handler\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <cmath>\\n#include <algorithm>\\n\\nusing namespace std;\\n\\nclass Solution { public: int minDistance(int height, int width, vector<int>& tree, vector<int>& squirrel, vector<vector<int>>& nuts) { return 0; } };",
        "java": "class Solution { public int minDistance(int height, int width, int[] tree, int[] squirrel, int[][] nuts) { return 0; } }",
        "javascript": "const fs = require('fs');",
        "c": "int minDistance(int height, int width, int* tree, int treeSize, int* squirrel, int squirrelSize, int** nuts, int nutsSize, int* nutsColSize) { }"
    }

    test_cases = [
        {"input": "5 7 2,2 4,4 3,0 2,5", "expected_output": "12", "is_sample": True},
        {"input": "1 1 0,0 0,0 0,0", "expected_output": "0", "is_sample": False},
        {"input": "10 10 0,0 1,1 2,2", "expected_output": "8", "is_sample": False},
        {"input": "100 100 0,0 50,50 1,1 2,2 3,3", "expected_output": "12", "is_sample": False},
        {"input": "10 10 5,5 0,0 1,1 0,0", "expected_output": "22", "is_sample": False},
        {"input": "10 10 5,5 0,0 1,1 1,1", "expected_output": "24", "is_sample": False},
        {"input": "2 2 0,0 1,1 0,1 1,0 1,1", "expected_output": "6", "is_sample": False},
        {"input": "5 5 0,0 4,4 0,1 1,0", "expected_output": "8", "is_sample": False},
        {"input": "10 10 0,0 9,9 0,1 0,2 0,3", "expected_output": "12", "is_sample": False},
        {"input": "5 5 2,2 2,2 0,0 4,4", "expected_output": "16", "is_sample": False}
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
        "topics": ["Array", "Math"],
        "companyIndex": 0
    }

    output_path = "401-600/573_Squirrel_Simulation.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
