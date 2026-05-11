import json
import collections
import os

def generate_json():
    problem_id = 987
    title = "Vertical Order Traversal of a Binary Tree"
    difficulty = "Hard"
    marks = 30
    
    html_description = """<h3>987. Vertical Order Traversal of a Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, calculate the <strong>vertical order traversal</strong> of the binary tree.</p>

<p>For each node at position <code>(row, col)</code>, its left child will be at position <code>(row + 1, col - 1)</code> and its right child will be at position <code>(row + 1, col + 1)</code>. The root of the tree is at <code>(0, 0)</code>.</p>

<p>The <strong>vertical order traversal</strong> of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.</p>

<p>Return <em>the <strong>vertical order traversal</strong> of the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/29/vtree1.jpg" style="width: 431px; height: 304px;" />
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[9],[3,15],[20],[7]]
<strong>Explanation:</strong>
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column at positions (0,0) and (2,0).
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/29/vtree2.jpg" style="width: 512px; height: 304px;" />
<pre><strong>Input:</strong> root = [1,2,3,4,5,6,7]
<strong>Output:</strong> [[4],[2],[1,5,6],[3],[7]]
<strong>Explanation:</strong>
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at (0,0), 5 is at (2,0), and 6 is at (2,0).
          Since 5 and 6 are at the same position (2,0), sort them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>
"""

    input_format = "Level-order representation of a binary tree."
    output_format = "List of lists containing vertical traversal values."
    
    constraints = [
        "1 <= Number of nodes <= 1000",
        "0 <= Node.val <= 1000",
        "Sort by column, then row, then value for same (row, col)"
    ]
    
    explanation = """To perform a vertical order traversal:
1. **The Coordinate System**:
   - Assign coordinates to each node. Let root be `(0, 0)`.
   - For a node at `(r, c)`:
     - Left child is at `(r + 1, c - 1)`.
     - Right child is at `(r + 1, c + 1)`.
2. **Collection Strategy (BFS/DFS)**:
   - Traverse the tree and store each node's location and value: `(col, row, value)`.
3. **The Sorting Rule**:
   - Sort the collected node data. The primary sort key is `col` (left to right). 
   - The secondary key is `row` (top to bottom).
   - If multiple nodes have the same `(row, col)`, the tertiary key is the `value` (increasing order).
4. **The Result Construction**:
   - Iterate through the sorted data and group values by `col`.

Complexity:
- Time: O(N log N) because we might visit all N nodes and sort them.
- Space: O(N) to store the coordinates and values."""
    
    answer = """import collections

def verticalTraversal(root) -> list[list[int]]:
    # List to store (col, row, value)
    nodes = []
    
    # Simple BFS to assign coordinates
    queue = collections.deque([(root, 0, 0)]) # (node, row, col)
    while queue:
        node, r, c = queue.popleft()
        if node:
            nodes.append((c, r, node.val))
            queue.append((node.left, r + 1, c - 1))
            queue.append((node.right, r + 1, c + 1))
            
    # Sort: col (asc), row (asc), value (asc)
    nodes.sort()
    
    res = collections.defaultdict(list)
    for c, r, v in nodes:
        res[c].append(v)
        
    return [res[c] for c in sorted(res.keys())]"""

    boilerplate = {
        "python": "import sys\nimport collections\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef verticalTraversal(root):\n    # User logic here\n    pass",
        "cpp": "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n};",
        "java": "public class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n}",
        "javascript": "function TreeNode(val, left, right) {\n    this.val = val;\n    this.left = left;\n    this.right = right;\n}",
        "c": "struct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};"
    }

    test_cases = [
        {"input": "[3,9,20,null,null,15,7]", "expected_output": "[[9],[3,15],[20],[7]]", "is_sample": True},
        {"input": "[1,2,3,4,5,6,7]", "expected_output": "[[4],[2],[1,5,6],[3],[7]]", "is_sample": True},
        # Diverse cases
        {"input": "[1]", "expected_output": "[[1]]", "is_sample": False},
        {"input": "[1,2,3,4,6,5,7]", "expected_output": "[[4],[2],[1,5,6],[3],[7]]", "is_sample": False},
        {"input": "[3,1,4,0,2,2]", "expected_output": "[[0],[1],[3,2,2],[4]]", "is_sample": False},
        {"input": "[0,8,1,null,null,3,2,null,4,5,null,null,7,6]", "expected_output": "[[8],[0,3,4,7],[1,5,6],[2]]", "is_sample": False},
        {"input": "[1,2,3,null,null,4,5,null,null,null,null]", "expected_output": "[[2],[1,4],[3],[5]]", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]", "expected_output": "[[8],[4],[2,9,10],[1,5,6,11,12],[3,13,14],[7],[15]]", "is_sample": False},
        {"input": "[1,2,3,4,5,null,null,null,null,null,null]", "expected_output": "[[4],[2],[1],[5],[3]]", "is_sample": False},
        {"input": "[1,2,4,3,null,null,5,null,null,null,null]", "expected_output": "[[3],[2,1],[4,5]]", "is_sample": False}
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
        "topics": ["Hash Table", "Tree", "Depth-First Search", "Breadth-First Search", "Sorting", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "standardized_json/801-1000/987_Vertical_Order_Traversal_of_a_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
