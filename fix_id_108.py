import json
import os

def generate_test_cases():
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def sortedArrayToBST(nums):
        if not nums: return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBST(nums[:mid])
        root.right = sortedArrayToBST(nums[mid+1:])
        return root

    def get_level_order(root):
        if not root: return []
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)
        while res and res[-1] is None: res.pop()
        return res

    cases = [
        {"input": "[-10,-3,0,5,9]", "expected_output": "[0,-3,9,-10,null,5]", "is_sample": True},
        {"input": "[1,3]", "expected_output": "[3,1]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": False},
        {"input": "[1]", "expected_output": "[1]", "is_sample": False},
        {"input": "[-1,0,1]", "expected_output": "[0,-1,1]", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7]", "expected_output": "[4,2,6,1,3,5,7]", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7,8,9,10]", "expected_output": "[6,3,9,2,5,8,10,1,null,4,null,7]", "is_sample": False},
    ]

    # Case 8: 1000 nodes
    nums8 = list(range(1, 1001))
    root8 = sortedArrayToBST(nums8)
    cases.append({
        "input": json.dumps(nums8),
        "expected_output": json.dumps(get_level_order(root8)),
        "is_sample": False
    })

    # Case 9: 5000 nodes
    nums9 = list(range(-2500, 2500))
    root9 = sortedArrayToBST(nums9)
    cases.append({
        "input": json.dumps(nums9),
        "expected_output": json.dumps(get_level_order(root9)),
        "is_sample": False
    })

    # Case 10: 10000 nodes (Peak Constraint)
    nums10 = list(range(1, 10001))
    root10 = sortedArrayToBST(nums10)
    cases.append({
        "input": json.dumps(nums10),
        "expected_output": json.dumps(get_level_order(root10)),
        "is_sample": False
    })

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Airbnb/108_Convert_Sorted_Array_to_Binary_Search_Tree.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["difficulty"] = "EASY"
    d["marks"] = 5
    d["input_format"] = "A sorted integer array nums."
    d["output_format"] = "Level-order traversal array of the height-balanced BST."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root"""

    d["boilerplate"]["python"] = """import sys, json

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_level_order(root):
    if not root: return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None: res.pop()
    return res

def solve(nums):
    if not nums: return None
    def build(left, right):
        if left > right: return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root
    return build(0, len(nums) - 1)

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        nums = json.loads(line)
        root = solve(nums)
        print(json.dumps(get_level_order(root)).replace("null", "null"))
    else:
        print("[]")"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 108 in Airbnb")
