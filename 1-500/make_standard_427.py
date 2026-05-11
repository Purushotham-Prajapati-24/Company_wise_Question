import json
import os

def generate_json():
    problem_id = 427
    title = "Construct Quad Tree"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>427. Construct Quad Tree</h3>
<p>Given a <code>n * n</code> matrix <code>grid</code> of <code>0's</code> and <code>1's</code> only. We want to represent <code>grid</code> with a Quad Tree.</p>

<p>Return <em>the root of the Quad Tree representing </em><code>grid</code>.</p>

<p>A Quad Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:</p>
<ul>
	<li><code>val</code>: True if the node represents a grid of 1's or False if the node represents a grid of 0's.</li>
	<li><code>isLeaf</code>: True if the node is leaf node on the tree or False if the node has the four children.</li>
</ul>

<pre>
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
</pre>

<p>We can construct a Quad Tree from a two-dimensional area using the following steps:</p>

<ol>
	<li>If the current grid has the same value (i.e all <code>1's</code> or all <code>0's</code>) set <code>isLeaf</code> True and set <code>val</code> to the value of the grid and set the four children to Null and stop.</li>
	<li>If the current grid has different values, set <code>isLeaf</code> to False and set <code>val</code> to any value and divide the current grid into four sub-grids.</li>
	<li>Recurse for each of the four sub-grids with the appropriate area.</li>
</ol>

<p>The Quad Tree format is used to represent a binary tree. Each node is represented by a pair of <code>[isLeaf, val]</code> where <strong>val</strong> is <code>1</code> if <code>val</code> is True and <code>0</code> if <code>val</code> is False.</p>"""

    input_format = "A 2D matrix `grid` (JSON array of arrays)."
    output_format = "A list of Quad Tree nodes in level-order traversal format `[isLeaf, val]`."
    
    constraints = [
        "n == grid.length == grid[i].length",
        "n == 2^x where 0 <= x <= 6",
        "grid[i][j] is either 0 or 1."
    ]
    
    explanation = """Construct the Quad Tree recursively. For each grid segment, check if all elements are identical. If yes, return a leaf node. Otherwise, split the grid into four quadrants and recursively build the four children nodes."""
    
    answer = """class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r, c, size):
            if size == 1:
                return Node(grid[r][c] == 1, True)
            
            mid = size // 2
            tl = build(r, c, mid)
            tr = build(r, c + mid, mid)
            bl = build(r + mid, c, mid)
            br = build(r + mid, c + mid, mid)
            
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and \\
               tl.val == tr.val == bl.val == br.val:
                return Node(tl.val, True)
            
            return Node(True, False, tl, tr, bl, br)
            
        return build(0, 0, len(grid))"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Node:\n    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):\n        self.val = val\n        self.isLeaf = isLeaf\n        self.topLeft = topLeft\n        self.topRight = topRight\n        self.bottomLeft = bottomLeft\n        self.bottomRight = bottomRight\n\nclass Solution:\n    def construct(self, grid: list[list[int]]) -> 'Node':\n        # User logic here\n        pass\n\ndef serialize(root):\n    if not root: return []\n    res = []\n    queue = [root]\n    while queue:\n        node = queue.pop(0)\n        if node:\n            res.append([1 if node.isLeaf else 0, 1 if node.val else 0])\n            if not node.isLeaf:\n                queue.extend([node.topLeft, node.topRight, node.bottomLeft, node.bottomRight])\n        else:\n            res.append(None)\n    while res and res[-1] is None: res.pop()\n    return res\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        grid = json.loads(raw_input)\n        sol = Solution()\n        root = sol.construct(grid)\n        print(json.dumps(serialize(root)).replace(\" \", \"\"))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <algorithm>\n\nusing namespace std;\n\nclass Node {\npublic:\n    bool val;\n    bool isLeaf;\n    Node* topLeft;\n    Node* topRight;\n    Node* bottomLeft;\n    Node* bottomRight;\n    Node(bool _val, bool _isLeaf) : val(_val), isLeaf(_isLeaf), topLeft(NULL), topRight(NULL), bottomLeft(NULL), bottomRight(NULL) {}\n};\n\nclass Solution {\npublic:\n    Node* construct(vector<vector<int>>& grid) {\n        // User logic here\n        return NULL;\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<vector<int>> grid;\n        int i = 0;\n        while (i < line.length()) {\n            if (line[i] == '[') {\n                int j = i + 1;\n                while (j < line.length() && line[j] != '[') j++;\n                if (j < line.length()) {\n                    vector<int> row;\n                    int k = j + 1;\n                    while (k < line.length() && line[k] != ']') {\n                        if (isdigit(line[k])) row.push_back(line[k] - '0');\n                        k++;\n                    }\n                    grid.push_back(row);\n                    i = k;\n                } else break;\n            }\n            i++;\n        }\n        Solution sol;\n        Node* root = sol.construct(grid);\n        cout << \"[]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Node {\n    public boolean val;\n    public boolean isLeaf;\n    public Node topLeft, topRight, bottomLeft, bottomRight;\n    public Node(boolean _val, boolean _isLeaf) { val = _val; isLeaf = _isLeaf; }\n}\n\nclass Solution {\n    public Node construct(int[][] grid) {\n        // User logic here\n        return null;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        // I/O logic here\n    }\n}",
        "javascript": "function Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight) {\n    this.val = val;\n    this.isLeaf = isLeaf;\n    this.topLeft = topLeft;\n    this.topRight = topRight;\n    this.bottomLeft = bottomLeft;\n    this.bottomRight = bottomRight;\n}\n\nvar construct = function(grid) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const grid = JSON.parse(input);\n    const root = construct(grid);\n    console.log(\"[]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\nstruct Node {\n    bool val;\n    bool isLeaf;\n    struct Node* topLeft;\n    struct Node* topRight;\n    struct Node* bottomLeft;\n    struct Node* bottomRight;\n};\n\nstruct Node* construct(int** grid, int gridSize, int* gridColSize) {\n    // User logic here\n    return NULL;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[0,1],[1,0]]", "expected_output": "[[0,1],[1,0],[1,1],[1,1],[1,0]]", "is_sample": True},
        {"input": "[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]", "expected_output": "[[0,1],[1,1],[0,1],[1,1],[1,0],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[0,1],[1,1],[1,1],[1,1],[1,1],[1,0],[1,0],[1,0],[1,0],[1,1],[1,1],[1,1],[1,1]]", "is_sample": True},
        {"input": "[[1]]", "expected_output": "[[1,1]]", "is_sample": False},
        {"input": "[[0]]", "expected_output": "[[1,0]]", "is_sample": False},
        {"input": "[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]", "expected_output": "[[1,1]]", "is_sample": False},
        {"input": "[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]", "expected_output": "[[1,0]]", "is_sample": False},
        {"input": "[[1,0],[1,0]]", "expected_output": "[[0,1],[1,1],[1,0],[1,1],[1,0]]", "is_sample": False},
        {"input": "[[1,1],[0,0]]", "expected_output": "[[0,1],[1,1],[1,1],[1,0],[1,0]]", "is_sample": False},
        {"input": "[ [1, 1], [0, 0] ]", "expected_output": "[[0,1],[1,1],[1,1],[1,0],[1,0]]", "is_sample": False}, # Spaces
        {"input": "[[0,0,1,1],[0,0,1,1],[1,1,0,0],[1,1,0,0]]", "expected_output": "[[0,1],[1,0],[1,1],[1,1],[1,0]]", "is_sample": False}
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
        "topics": ["Matrix", "Divide and Conquer", "Tree"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
