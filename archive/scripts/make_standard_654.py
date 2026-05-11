import json
import os

def generate_json():
    problem_id = 654
    title = "Maximum Binary Tree"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>654. Maximum Binary Tree</h3>
<p>You are given an integer array <code>nums</code> with no duplicates. A <b>maximum binary tree</b> can be built recursively from <code>nums</code> using the following algorithm:</p>

<ol>
	<li>Create a root node whose value is the maximum value in <code>nums</code>.</li>
	<li>Recursively build the left subtree on the <b>subarray prefix</b> to the left of the maximum value.</li>
	<li>Recursively build the right subtree on the <b>subarray suffix</b> to the right of the maximum value.</li>
</ol>

<p>Return <em>the maximum binary tree built from </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg" style="width: 302px; height: 422px;" />
<pre>
<strong>Input:</strong> nums = [3,2,1,6,0,5]
<strong>Output:</strong> [6,3,5,null,2,0,null,null,1]
<strong>Explanation:</strong> The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - The largest value in [1] is 1. Left prefix is [] and right suffix is [].
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - The largest value in [0] is 0. Left prefix is [] and right suffix is [].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg" style="width: 182px; height: 301px;" />
<pre>
<strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> [3,null,2,null,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li>All integers in <code>nums</code> are <b>unique</b>.</li>
</ul>"""

    input_format = "A single line containing space-separated unique integers."
    output_format = "Space-separated Level-Order Traversal of the built tree (use 'null' for missing)."
    
    constraints = [
        "1 <= N <= 1000",
        "All integers are unique.",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To build a Maximum Binary Tree efficiently:
1. **The Recursive Approach (Simple)**:
   - Find the maximum element index $idx$.
   - Root is $nums[idx]$.
   - $root.left = build(nums[0 \dots idx-1])$.
   - $root.right = build(nums[idx+1 \dots N-1])$.
   - This takes $O(N^2)$ in the worst case (already sorted array).
2. **The Optimal Approach (Monotonic Stack)**:
   - Use a stack to maintain a decreasing sequence of nodes.
   - For each value `x` in `nums`:
     - Create a new `TreeNode(x)`.
     - While stack is not empty and `stack[-1].val < x`:
       - The last element on the stack becomes the left child of `x`.
       - Pop the stack.
     - If stack is not empty:
       - `x` becomes the right child of `stack[-1]`.
     - Push `x` onto the stack.
   - The first element in the stack is the root.
3. **Complexity**:
   - Time Complexity: O(N) as each element is pushed and popped once.
   - Space Complexity: O(N) for nodes and the stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums: list[int]):
    stack = []
    for x in nums:
        node = TreeNode(x)
        while stack and stack[-1].val < x:
            node.left = stack.pop()
        if stack:
            stack[-1].right = node
        stack.append(node)
    return stack[0]"""

    boilerplate = {
        "python": "import sys\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef constructMaximumBinaryTree(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        # Parser logic here\n        pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <stack>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n};",
        "java": "public class Solution {\n    public TreeNode constructMaximumBinaryTree(int[] nums) {\n        // User logic\n        return null;\n    }\n}",
        "javascript": "function constructMaximumBinaryTree(nums) {\n    // User logic\n}",
        "c": "struct TreeNode* constructMaximumBinaryTree(int* nums, int numsSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "3 2 1 6 0 5", "expected_output": "6 3 5 null 2 0 null null 1", "is_sample": True},
        {"input": "3 2 1", "expected_output": "3 null 2 null 1", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 2", "expected_output": "2 1", "is_sample": False},
        {"input": "2 1", "expected_output": "2 null 1", "is_sample": False},
        {"input": "7 5 3 4 8 2", "expected_output": "8 7 2 null 5 null null 3 4", "is_sample": False},
        {"input": "1 3 2", "expected_output": "3 1 2", "is_sample": False},
        {"input": "100 50 75", "expected_output": "100 null 75 50", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 1001)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1000, 0, -1)]), "expected_output": "...", "is_sample": False}
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
        "topics": ["Array", "Tree", "Stack", "Monotonic Stack", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "601-800/654_Maximum_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
