import json
import os

def generate_test_cases():
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def build_tree(arr):
        if not arr: return None
        nodes = [TreeNode(v) if v is not None else None for v in arr]
        it = iter(nodes)
        try:
            root = next(it)
        except StopIteration:
            return None
        queue = [root]
        for node in queue:
            if node:
                try:
                    node.left = next(it)
                    queue.append(node.left)
                    node.right = next(it)
                    queue.append(node.right)
                except StopIteration:
                    break
        return root

    def maxPathSum(root):
        max_s = [float('-inf')]
        def gain(node):
            if not node: return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            max_s[0] = max(max_s[0], node.val + left + right)
            return node.val + max(left, right)
        gain(root)
        return max_s[0]

    cases = [
        {"input": "[1,2,3]", "expected_output": "6", "is_sample": True},
        {"input": "[-10,9,20,null,null,15,7]", "expected_output": "42", "is_sample": True},
        {"input": "[1]", "expected_output": "1", "is_sample": False},
        {"input": "[-3]", "expected_output": "-3", "is_sample": False},
        {"input": "[2,-1]", "expected_output": "2", "is_sample": False},
        {"input": "[1,-2,3]", "expected_output": "4", "is_sample": False},
        {"input": "[1,-2,-3,1,3,-2,null,-1]", "expected_output": "3", "is_sample": False},
    ]

    # Case 8: Balanced 1023 nodes, all 1s
    vals8 = [1] * 1023
    cases.append({"input": json.dumps(vals8), "expected_output": "511", "is_sample": False}) # Balanced tree sum is 2^k - 1? No, path sum is different.
    # Actually let's just use the function.
    cases[-1]["expected_output"] = str(maxPathSum(build_tree(vals8)))

    # Case 9: 5000 nodes, all 1s
    vals9 = [1] * 5000
    cases.append({"input": json.dumps(vals9), "expected_output": str(maxPathSum(build_tree(vals9))), "is_sample": False})

    # Case 10: 30000 nodes (Peak Constraint)
    vals10 = [1] * 30000
    cases.append({"input": json.dumps(vals10), "expected_output": str(maxPathSum(build_tree(vals10))), "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Meta/124_Binary_Tree_Maximum_Path_Sum.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>124 Binary Tree Maximum Path Sum</h3><p>A <strong>path</strong> in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence <strong>at most once</strong>. Note that the path does not need to pass through the root.</p><p>The <strong>path sum</strong> of a path is the sum of the node's values in the path.</p><p>Given the <code>root</code> of a binary tree, return <em>the maximum <strong>path sum</strong> of any <strong>non-empty</strong> path</em>.</p>"
    d["difficulty"] = "HARD"
    d["marks"] = 20
    d["input_format"] = "A serialized level-order traversal array of a binary tree."
    d["output_format"] = "Integer representing max path sum."
    
    d["metadata"] = {
        "time_limit_ms": 2000,
        "memory_limit_mb": 512,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def gain(node):
            if not node: return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)
        gain(root)
        return self.max_sum"""

    d["boilerplate"]["python"] = """import sys, json

# Increase recursion depth for deep trees
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr: return None
    nodes = [TreeNode(v) if v is not None else None for v in arr]
    it = iter(nodes)
    try:
        root = next(it)
    except StopIteration:
        return None
    queue = [root]
    for node in queue:
        if node:
            try:
                node.left = next(it)
                queue.append(node.left)
                node.right = next(it)
                queue.append(node.right)
            except StopIteration:
                break
    return root

def solve(root):
    max_s = [float('-inf')]
    def gain(node):
        if not node: return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        max_s[0] = max(max_s[0], node.val + left + right)
        return node.val + max(left, right)
    gain(root)
    return max_s[0]

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        arr = json.loads(line)
        root = build_tree(arr)
        print(solve(root))
    else:
        print(0)"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 124 in Meta")
