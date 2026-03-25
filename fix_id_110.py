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

    def isBalanced(root):
        def check(node):
            if not node: return 0
            left = check(node.left)
            if left == -1: return -1
            right = check(node.right)
            if right == -1: return -1
            if abs(left - right) > 1: return -1
            return 1 + max(left, right)
        return check(root) != -1

    cases = [
        {"input": "[3,9,20,null,null,15,7]", "expected_output": "true", "is_sample": True},
        {"input": "[1,2,2,3,3,null,null,4,4]", "expected_output": "false", "is_sample": True},
        {"input": "[]", "expected_output": "true", "is_sample": True},
        {"input": "[1]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,null,3]", "expected_output": "false", "is_sample": False},
        {"input": "[1,2,2,3,null,null,3,4,null,null,4]", "expected_output": "false", "is_sample": False},
        {"input": "[1,null,2,null,3]", "expected_output": "false", "is_sample": False},
    ]

    # Case 8: Balanced 1023 nodes (Perfect binary tree)
    nodes8 = [1] * 1023
    cases.append({"input": json.dumps(nodes8), "expected_output": "true", "is_sample": False})

    # Case 9: Extreme left-skewed 100 nodes (Serialized carefully)
    # 1 -> 2 -> 3 -> 4 ... 16 nodes to make it deep enough
    # [1, 2, null, 3, null, null, null, 4, ...]
    nodes9 = [1, 2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5]
    cases.append({"input": json.dumps(nodes9).replace("None", "null"), "expected_output": "false", "is_sample": False})

    # Case 10: 5000 nodes (Peak Constraint) Balanced
    nodes10 = [1] * 5000
    cases.append({"input": json.dumps(nodes10), "expected_output": "true", "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Cisco/110_Balanced_Binary_Tree.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>110 Balanced Binary Tree</h3><p>Given a binary tree, determine if it is height-balanced (depth of two subtrees of every node never differs by more than 1).</p>"
    d["difficulty"] = "EASY"
    d["marks"] = 10
    d["input_format"] = "A serialized level-order traversal array of a binary tree."
    d["output_format"] = "boolean"
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node: return 0
            left = check(node.left)
            if left == -1: return -1
            right = check(node.right)
            if right == -1: return -1
            if abs(left - right) > 1: return -1
            return 1 + max(left, right)
        return check(root) != -1"""

    d["boilerplate"]["python"] = """import sys, json

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
    def check(node):
        if not node: return 0
        l = check(node.left)
        if l == -1: return -1
        r = check(node.right)
        if r == -1: return -1
        if abs(l - r) > 1: return -1
        return 1 + max(l, r)
    return check(root) != -1

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        arr = json.loads(line)
        root = build_tree(arr)
        print("true" if solve(root) else "false")
    else:
        print("true")"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 110 in Cisco")
