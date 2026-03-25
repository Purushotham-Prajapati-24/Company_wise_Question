import json
import os

def generate_test_cases():
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    def build(ino, post):
        if not ino: return None
        root_val = post.pop()
        root = TreeNode(root_val)
        mid = ino.index(root_val)
        root.right = build(ino[mid+1:], post)
        root.left = build(ino[:mid], post)
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

    def get_inorder(node):
        if not node: return []
        return get_inorder(node.left) + [node.val] + get_inorder(node.right)
    
    def get_postorder(node):
        if not node: return []
        return get_postorder(node.left) + get_postorder(node.right) + [node.val]

    cases = [
        {"input": "[9,3,15,20,7]\\n[9,15,7,20,3]", "expected_output": "[3,9,20,null,null,15,7]", "is_sample": True},
        {"input": "[-1]\\n[-1]", "expected_output": "[-1]", "is_sample": True},
        {"input": "[]\\n[]", "expected_output": "[]", "is_sample": False},
        {"input": "[2,1]\\n[2,1]", "expected_output": "[1,2]", "is_sample": False},
        {"input": "[1,2,3]\\n[3,2,1]", "expected_output": "[1,null,2,null,3]", "is_sample": False},
    ]
    
    # Case 6: Right-skewed 300 nodes
    ino6 = list(range(1, 301))
    post6 = ino6[::-1]
    root6 = build(ino6, post6[:])
    cases.append({
        "input": json.dumps(ino6) + "\\n" + json.dumps(post6),
        "expected_output": json.dumps(get_level_order(root6)),
        "is_sample": False
    })

    # Case 7: Left-skewed 300 nodes
    ino7 = list(range(1, 301))[::-1]
    post7 = list(range(1, 301))
    root7 = build(ino7, post7[:])
    cases.append({
        "input": json.dumps(ino7) + "\\n" + json.dumps(post7),
        "expected_output": json.dumps(get_level_order(root7)),
        "is_sample": False
    })

    # Case 8: Balanced 1023 nodes
    def make_balanced(start, end):
        if start > end: return None
        mid = (start + end) // 2
        root = TreeNode(mid)
        root.left = make_balanced(start, mid-1)
        root.right = make_balanced(mid+1, end)
        return root
    
    root8 = make_balanced(1, 1023)
    ino8 = get_inorder(root8)
    post8 = get_postorder(root8)
    cases.append({
        "input": json.dumps(ino8) + "\\n" + json.dumps(post8),
        "expected_output": json.dumps(get_level_order(root8)),
        "is_sample": False
    })

    # Case 9: Random-ish 500 nodes
    root9 = make_balanced(5000, 5499)
    cases.append({
        "input": json.dumps(get_inorder(root9)) + "\\n" + json.dumps(get_postorder(root9)),
        "expected_output": json.dumps(get_level_order(root9)),
        "is_sample": False
    })
    
    # Case 10: 3000 nodes Balanced
    root10 = make_balanced(1, 3000)
    cases.append({
        "input": json.dumps(get_inorder(root10)) + "\\n" + json.dumps(get_postorder(root10)),
        "expected_output": json.dumps(get_level_order(root10)),
        "is_sample": False
    })
    
    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Twitter/106_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["difficulty"] = "MEDIUM"
    d["marks"] = 10
    d["input_format"] = "Inorder and Postorder arrays on separate lines."
    d["output_format"] = "Level-order traversal array of the constructed tree."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder: return None
        val = postorder.pop()
        root = TreeNode(val)
        idx = inorder.index(val)
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
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

def solve(inorder, postorder):
    if not inorder: return None
    pos = {v: i for i, v in enumerate(inorder)}
    def build(in_start, in_end, post_start, post_end):
        if in_start > in_end: return None
        root_val = postorder[post_end]
        root = TreeNode(root_val)
        mid = pos[root_val]
        left_size = mid - in_start
        root.left = build(in_start, mid-1, post_start, post_start + left_size - 1)
        root.right = build(mid+1, in_end, post_start + left_size, post_end - 1)
        return root
    return build(0, len(inorder)-1, 0, len(postorder)-1)

if __name__ == '__main__':
    lines = sys.stdin.read().strip().split('\\n')
    if len(lines) >= 2:
        ino = json.loads(lines[0])
        post = json.loads(lines[1])
        root = solve(ino, post)
        print(json.dumps(get_level_order(root)).replace("null", "null"))
    else:
        print("[]")"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 106 in Twitter")
