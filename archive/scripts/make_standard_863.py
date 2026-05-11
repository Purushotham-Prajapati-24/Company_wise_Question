import json
import os

def generate_json():
    problem_id = 863
    title = "All Nodes Distance K in Binary Tree"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>863. All Nodes Distance K in Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, the value of a target node <code>target</code>, and an integer <code>k</code>, return <em>an array of the values of all nodes that have a distance </em><code>k</code><em> from the target node</em>.</p>

<p>You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" style="width: 500px; height: 429px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
<strong>Output:</strong> [7,4,1]
<strong>Explanation:</strong> The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> root = [1], target = 1, k = 3
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 500]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 500</code></li>
	<li>All the values <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>target</code> is the value of one of the nodes in the tree.</li>
	<li><code>0 &lt;= k &lt;= 1000</code></li>
</ul>
"""

    input_format = "A root binary tree JSON, target node value, and integer k."
    output_format = "An array of node values."
    
    constraints = [
        "1 <= Number of nodes <= 500",
        "Unique node values between 0 and 500.",
        "Target is guaranteed to exist."
    ]
    
    explanation = """To find all nodes at distance K from a given target node in a binary tree:
1. **The Graph Perspective**:
   - A tree is an undirected connected graph without cycles. Distance in a tree can be calculated using graph algorithms once we have pointers from children to parents.
2. **Strategy**:
   - **Step 1: Graph Representation**: Traverse the tree (DFS or BFS) to build an adjacency list (undirected graph) or a mapping of parent pointers for each node.
   - **Step 2: Distance Search**:
     - Start from the `target` node.
     - Use **Breadth-First Search (BFS)** to explore neighbors layer by layer. Neighbors of node `p` are `p.left`, `p.right`, and `p.parent`.
     - After `K` layers, the nodes in the current layer are exactly at distance `K`.
     - Maintain a `visited` set to avoid back-tracking.

Complexity:
- Time: O(N) to build the parent map and O(N) for BFS.
- Space: O(N) to store the parent map and queue."""
    
    answer = """import collections

def distanceK(root: 'TreeNode', target: 'TreeNode', k: int) -> list[int]:
    # Use BFS/DFS to store parents
    adj = collections.defaultdict(list)
    def build_graph(node, parent):
        if not node: return
        if parent:
            adj[node.val].append(parent.val)
            adj[parent.val].append(node.val)
        build_graph(node.left, node)
        build_graph(node.right, node)
        
    build_graph(root, None)
    
    # BFS starting from target
    queue = collections.deque([(target.val, 0)])
    visited = {target.val}
    res = []
    
    while queue:
        val, dist = queue.popleft()
        if dist == k:
            res.append(val)
        elif dist < k:
            for neighbor in adj[val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
                    
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef distanceK(root, target, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Tree deserialization code goes here\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <unordered_set>\n#include <queue>\n\nusing namespace std;\ntypedef struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n} TreeNode;",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {\n        return new ArrayList<>();\n    }\n}",
        "javascript": "var distanceK = function(root, target, k) {\n    return [];\n};",
        "c": "int* distanceK(struct TreeNode* root, struct TreeNode* target, int k, int* returnSize){\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "[3,5,1,6,2,0,8,null,null,7,4]\\n5\\n2", "expected_output": "[7,4,1]", "is_sample": True},
        {"input": "[1]\\n1\\n3", "expected_output": "[]", "is_sample": True},
        # Diverse cases
        {"input": "[1,2,3,4,5]\\n2\\n1", "expected_output": "[1,4,5]", "is_sample": False},
        {"input": "[1,2,3,4,5]\\n1\\n0", "expected_output": "[1]", "is_sample": False},
        {"input": "[1,2,3]\\n3\\n2", "expected_output": "[2]", "is_sample": False},
        {"input": "[0,1,null,null,2,null,3,null,4]\\n3\\n2", "expected_output": "[1,4]", "is_sample": False},
        {"input": "[1,2,3]\\n1\\n10", "expected_output": "[]", "is_sample": False},
        {"input": "[1,2,3]\\n2\\n10", "expected_output": "[]", "is_sample": False},
        # Stress cases
        {"input": "[0 to 499 linear tree]", "expected_output": "check logic", "is_sample": False},
        {"input": "[0 to 499 balanced tree]", "expected_output": "check logic", "is_sample": False}
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

    output_path = "801-1000/863_All_Nodes_Distance_K_in_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
