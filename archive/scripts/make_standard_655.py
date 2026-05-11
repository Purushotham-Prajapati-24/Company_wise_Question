import json
import os

def generate_json():
    problem_id = 655
    title = "Print Binary Tree"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>655. Print Binary Tree</h3>
<p>Print a binary tree in an <code>m x n</code> 2D string array <code>res</code> following these rules:</p>

<ol>
	<li>The <strong>height</strong> of the tree is <code>height</code>, and the number of rows <code>m</code> should be <code>height + 1</code>.</li>
	<li>The number of columns <code>n</code> should be <code>2<sup>height + 1</sup> - 1</code>.</li>
	<li>Place the <strong>root node</strong> in the <strong>middle</strong> of the <strong>top row</strong> (at <code>res[0][(n-1)/2]</code>).</li>
	<li>For a node located at <code>res[r][c]</code>:
	<ul>
		<li>The <strong>left child</strong> should be placed at <code>res[r+1][c - 2<sup>height-r-1</sup>]</code>.</li>
		<li>The <strong>right child</strong> should be placed at <code>res[r+1][c + 2<sup>height-r-1</sup>]</code>.</li>
	</ul>
	</li>
	<li>Continue this process until all the nodes in the tree have been placed.</li>
	<li>Cells without a node should contain the empty string <code>""</code>.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/print1-tree.jpg" style="width: 132px; height: 101px;" />
<pre><strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 
[["","1",""],
 ["2","",""]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/print2-tree.jpg" style="width: 382px; height: 222px;" />
<pre><strong>Input:</strong> root = [1,2,3,null,4]
<strong>Output:</strong> 
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 2<sup>10</sup>]</code>.</li>
	<li><code>-99 &lt;= Node.val &lt;= 99</code></li>
	<li>The depth of the tree is in the range <code>[1, 10]</code>.</li>
</ul>"""

    input_format = "A root of a binary tree represented as an array."
    output_format = "An m x n array of strings representing the grid layout."
    
    constraints = [
        "1 <= nodes <= 1024",
        "1 <= depth <= 10",
        "m = height + 1, n = 2^(height+1) - 1."
    ]
    
    explanation = """To print a binary tree in a grid format defined by LeetCode rules:
1. **Find Tree Height**:
   - Perform a simple DFS or recursion to find the maximum depth of the tree (`height`).
2. **Setup grid**:
   - Create a 2D string array with row count `m = height + 1` and column count `n = 2^(height+1) - 1`.
   - Initialize all cells to an empty string `""`.
3. **Recursive DFS Placement**:
   - Start with the root at `r = 0, c = (n - 1) // 2`.
   - For a node at `(r, c)` with value `v`:
     - Assign `res[r][c] = str(v)`.
     - Calculate the offset for its children: `offset = 2^(height - r - 1)`.
     - Recursively call for `node.left` at `(r + 1, c - offset)`.
     - Recursively call for `node.right` at `(r + 1, c + offset)`.
4. **Complexity Analysis**:
   - Time: O(M * N) which is O(2^(height)) cells to populate.
   - Space: O(M * N) to store the result grid."""
    
    answer = """class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            if not node: return -1
            return 1 + max(get_height(node.left), get_height(node.right))
            
        height = get_height(root)
        rows = height + 1
        cols = 2**(height + 1) - 1
        res = [[""] * cols for _ in range(rows)]
        
        def fill(node, r, c):
            if not node: return
            res[r][c] = str(node.val)
            offset = 2**(height - r - 1)
            if node.left:
                fill(node.left, r+1, c - offset)
            if node.right:
                fill(node.right, r+1, c + offset)
                
        fill(root, 0, (cols - 1) // 2)
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef printTree(root):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Tree conversion logic\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <cmath>\nusing namespace std;\n\ncvstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nvector<vector<string>> printTree(TreeNode* root) {\n    // User logic here\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<List<String>> printTree(TreeNode root) {\n        // User logic\n    }\n}",
        "javascript": "/**\n * @param {TreeNode} root\n * @return {string[][]}\n */\nvar printTree = function(root) {\n    // User logic here\n};",
        "c": "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the arrays are returned as *returnColumnSizes array.\n */\nchar *** printTree(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {\n    // User logic here\n}"
    }

    test_cases = [
        {"input": "[1,2]", "expected_output": '[["","1",""],["2","",""]]', "is_sample": True},
        {"input": "[1,2,3,null,4]", "expected_output": '[["","","","1","","",""],["","2","","","","3",""],["","","4","","","",""]]', "is_sample": True},
        {"input": "[1]", "expected_output": '[["1"]]', "is_sample": False},
        {"input": "[1,2,3]", "expected_output": '[["","1",""],["2","","3"]]', "is_sample": False},
        {"input": "[1,null,2,null,3]", "expected_output": '[["","","","1","","",""],["","","","","","2",""],["","","","","","","3"]]', "is_sample": False},
        # Stress cases
        {"input": "[i for i in range(1, 16)]", "expected_output": "...", "is_sample": False},
        {"input": "[1,2,2,3,3,3,3,4,4,4,4,4,4,4,4]", "expected_output": "...", "is_sample": False},
        {"input": "[1]*1024", "expected_output": "...", "is_sample": False}
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
        "topics": ["Tree", "Depth-First Search", "Breadth-First Search", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "601-800/655_Print_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
