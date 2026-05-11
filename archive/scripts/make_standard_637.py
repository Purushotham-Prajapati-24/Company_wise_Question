import json
import os

def generate_json():
    problem_id = 637
    title = "Average of Levels in Binary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>637. Average of Levels in Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the average value of the nodes on each level in the form of an array</em>. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [3.00000,14.50000,11.00000]
<strong>Explanation:</strong> The average value of nodes on level 0 is 3, on level 1 is (9+20)/2 = 14.5, and on level 2 is (15+7)/2 = 11.
Hence return [3, 14.5, 11].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,15,7]
<strong>Output:</strong> [3.00000,14.50000,11.00000]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
"""

    input_format = "A level-order representation of the tree (array format)."
    output_format = "A list of floats representing the average of each level."
    
    constraints = [
        "1 <= nodes <= 10^4",
        "-2^31 <= Node.val <= 2^31 - 1"
    ]
    
    explanation = """To find the average of each level:
1. Use Breadth-First Search (BFS) with a queue.
2. Initialize the result list and a queue with the root.
3. While the queue is not empty:
   - Determine the number of nodes at the current level (`level_size`).
   - Iterate through the current level nodes:
     - Sum their values.
     - Add their left and right children to the queue.
   - Calculate the average (`sum / level_size`) and add it to the result list."""
    
    answer = """from collections import deque

def averageOfLevels(root):
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level_sum = 0
        level_count = len(queue)
        for _ in range(level_count):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level_sum / level_count)
    return res"""

    boilerplate = {
        "python": "class TreeNode:\\n    def __init__(self, val=0, left=None, right=None):\\n        self.val = val\\n        self.left = left\\n        self.right = right\\n\\ndef averageOfLevels(root):\\n    # User logic here\\n    pass",
        "cpp": "class Solution { public: vector<double> averageOfLevels(TreeNode* root) { return {}; } };",
        "java": "class Solution { public List<Double> averageOfLevels(TreeNode root) { return new ArrayList<>(); } }",
        "javascript": "var averageOfLevels = function(root) { };",
        "c": "double* averageOfLevels(struct TreeNode* root, int* returnSize) { }"
    }

    test_cases = [
        {"input": "[3, 9, 20, null, null, 15, 7]", "expected_output": "[3.0, 14.5, 11.0]", "is_sample": True},
        {"input": "[3, 9, 20, 15, 7]", "expected_output": "[3.0, 14.5, 11.0]", "is_sample": True},
        {"input": "[1]", "expected_output": "[1.0]", "is_sample": False},
        {"input": "[1, 2, 3, 4, 5, 6, 7]", "expected_output": "[1.0, 2.5, 5.5]", "is_sample": False},
        {"input": "[1, 2, null, 3, null, 4]", "expected_output": "[1.0, 2.0, 3.0, 4.0]", "is_sample": False},
        {"input": "[2147483647, 2147483647]", "expected_output": "[2147483647.0, 2147483647.0]", "is_sample": False},
        {"input": "[0, 1, 2, 3, 4, 5, 6, 7, 8]", "expected_output": "[0.0, 1.5, 4.5, 7.5]", "is_sample": False},
        {"input": str([1]*5000), "expected_output": "[1.0] * " + str(int(math.log2(5000))), "is_sample": False},
        {"input": str([i for i in range(10000)]), "expected_output": "list of averages", "is_sample": False},
        {"input": "[1, null, 2, null, 3, null, 4, null, 5]", "expected_output": "[1.0, 2.0, 3.0, 4.0, 5.0]", "is_sample": False}
    ]

    # Fixing simple expected outputs for stress
    test_cases[7]["expected_output"] = "[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]"

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

    output_path = "401-600/637_Average_of_Levels_in_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
