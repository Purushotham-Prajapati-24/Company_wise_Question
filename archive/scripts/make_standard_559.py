import json
import os

def generate_json():
    problem_id = 559
    title = "Maximum Depth of N-ary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>559. Maximum Depth of N-ary Tree</h3>
<p>Given a n-ary tree, find its maximum depth.</p>

<p>The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.</p>

<p><em>Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" />
<pre>
<strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 100%; max-width: 296px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3,4,5,null,None,6,7,null,8,null,9,10,null,None,11,null,12,null,13,null,None,14]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The total number of nodes is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li>The depth of the n-ary tree is less than or equal to <code>1000</code>.</li>
</ul>
"""

    input_format = "A serialized N-ary tree level-order representation (e.g., [1,null,3,2,4,null,5,6])."
    output_format = "A single integer representing the maximum depth."
    
    constraints = [
        "Nodes range: [0, 10^4].",
        "Max depth: 1000."
    ]
    
    explanation = """To find the maximum depth of an N-ary tree:
1. Use recursion (DFS).
2. Base Case: If the root is None, the depth is 0.
3. Recursive step:
   - For a node, the depth is 1 + the maximum depth of all its children.
   - If a node has no children (leaf), its depth is 1.
4. Calculate maximum child depth and return `1 + max_child_depth`."""
    
    answer = """class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        
        max_child_depth = 0
        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child))
            
        return 1 + max_child_depth"""

    boilerplate = {
        "python": "import sys\\nclass Node:\\n    def __init__(self, val=None, children=None):\\n        self.val = val; self.children = children if children is not None else []\\n\\nclass Solution:\\n    def maxDepth(self, root):\\n        return 0",
        "cpp": "class Node { public: int val; vector<Node*> children; };\\nclass Solution { public: int maxDepth(Node* root) { return 0; } };",
        "java": "class Solution { public int maxDepth(Node root) { return 0; } }",
        "javascript": "const fs = require('fs');",
        "c": "int maxDepth(struct Node* root) { }"
    }

    test_cases = [
        {"input": "1 null 3 2 4 null 5 6", "expected_output": "3", "is_sample": True},
        {"input": "1 null 2 3 4 5 null null 6 7 null 8 null 9 10 null null 11 null 12 null 13 null null 14", "expected_output": "5", "is_sample": True},
        {"input": "", "expected_output": "0", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 null 2", "expected_output": "2", "is_sample": False},
        {"input": "1 null 2 3", "expected_output": "2", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "3", "is_sample": False},
        {"input": "1 null 2 null 3 null 4", "expected_output": "4", "is_sample": False},
        {"input": "1 null 2 3 null 4 5 null 6 7", "expected_output": "4", "is_sample": False},
        {"input": "1 null 2 3 4 5 6", "expected_output": "2", "is_sample": False}
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
        "topics": ["Tree", "N-ary Tree", "Depth-First Search", "Breadth-First Search"],
        "companyIndex": 0
    }

    output_path = "401-600/559_Maximum_Depth_of_N-ary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
