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

    def pathSum(root, targetSum):
        res = []
        def dfs(node, curr_sum, path):
            if not node: return
            curr_sum += node.val
            new_path = path + [node.val]
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    res.append(new_path)
                return
            dfs(node.left, curr_sum, new_path)
            dfs(node.right, curr_sum, new_path)
        dfs(root, 0, [])
        return res

    cases = [
        {"input": "[5,4,8,11,null,13,4,7,2,null,null,5,1]\\n22", "expected_output": json.dumps([[5,4,11,2],[5,8,4,5]]), "is_sample": True},
        {"input": "[1,2,3]\\n5", "expected_output": "[]", "is_sample": True},
        {"input": "[1,2]\\n0", "expected_output": "[]", "is_sample": True},
    ]

    # Case 8: Single node
    cases.append({"input": "[1]\\n1", "expected_output": "[[1]]", "is_sample": False})

    # Case 9: Line tree
    vals9 = [1, 2, None, 3, None, None, None, 4]
    cases.append({"input": json.dumps(vals9) + "\\n10", "expected_output": json.dumps(pathSum(build_tree(vals9), 10)), "is_sample": False})

    # Case 10: Balanced 5000 nodes (Peak Constraint)
    vals10 = [1] * 5000
    root10 = build_tree(vals10)
    # The sum will be log2(5000) depth... approx 12.
    cases.append({"input": json.dumps(vals10) + "\\n12", "expected_output": json.dumps(pathSum(root10, 12)), "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Quora/113_Path_Sum_II.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>113 Path Sum II</h3><p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <em>all <strong>root-to-leaf</strong> paths where the sum of the node values in the path equals </em><code>targetSum</code><em>. Each path should be returned as a list of the node <strong>values</strong>, not node references</em>.</p><p>A <strong>root-to-leaf</strong> path is a path starting from the root and ending at any leaf node.</p>"
    d["difficulty"] = "MEDIUM"
    d["marks"] = 15
    d["input_format"] = "Two lines: 1. Serialized level-order traversal array of a binary tree. 2. targetSum (integer)."
    d["output_format"] = "A list of lists of integers representing paths."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, curr_sum, path):
            if not node: return
            curr_sum += node.val
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    res.append(path + [node.val])
                return
            dfs(node.left, curr_sum, path + [node.val])
            dfs(node.right, curr_sum, path + [node.val])
        dfs(root, 0, [])
        return res"""

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

def solve(root, targetSum):
    res = []
    def dfs(node, curr_sum, path):
        if not node: return
        curr_sum += node.val
        if not node.left and not node.right:
            if curr_sum == targetSum:
                res.append(path + [node.val])
            return
        dfs(node.left, curr_sum, path + [node.val])
        dfs(node.right, curr_sum, path + [node.val])
    dfs(root, 0, [])
    return res

if __name__ == '__main__':
    lines = sys.stdin.read().strip().split('\\n')
    if len(lines) >= 2:
        try:
            arr = json.loads(lines[0])
            targetSum = int(lines[1])
            root = build_tree(arr)
            print(json.dumps(solve(root, targetSum)))
        except:
            print("[]")
    else:
        print("[]")"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 113 in Quora")
