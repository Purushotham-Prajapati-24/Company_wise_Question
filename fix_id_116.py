import json
import os

def generate_test_cases():
    class TreeNode:
        def __init__(self, val=0, left=None, right=None, next=None):
            self.val = val
            self.left = left
            self.right = right
            self.next = next

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

    def get_level_order_with_next(root):
        if not root: return []
        res = []
        curr = root
        while curr:
            temp = curr
            while temp:
                res.append(temp.val)
                temp = temp.next
            res.append(None)
            curr = curr.left
        return res

    def connect(root):
        if not root: return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

    cases = [
        {"input": "[1,2,3,4,5,6,7]", "expected_output": "[1,null,2,3,null,4,5,6,7,null]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": True},
        {"input": "[1]", "expected_output": "[1,null]", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "[1,null,2,3,null]", "is_sample": False},
    ]

    # Case 8: 15 nodes (Perfect)
    vals8 = list(range(1, 16))
    root8 = connect(build_tree(vals8))
    cases.append({"input": json.dumps(vals8), "expected_output": json.dumps(get_level_order_with_next(root8)).replace("None", "null"), "is_sample": False})

    # Case 10: 4095 nodes (Peak Constraint 2^12 - 1)
    vals10 = [1] * 4095
    root10 = connect(build_tree(vals10))
    cases.append({"input": json.dumps(vals10), "expected_output": json.dumps(get_level_order_with_next(root10)).replace("None", "null"), "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Microsoft/116_Populating_Next_Right_Pointers_in_Each_Node.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>116 Populating Next Right Pointers in Each Node</h3><p>You are given a <strong>perfect binary tree</strong> where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:</p><pre>struct Node {\\n  int val;\\n  Node *left;\\n  Node *right;\\n  Node *next;\\n}</pre><p>Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to <code>NULL</code>.</p><p>Initially, all next pointers are set to <code>NULL</code>.</p>"
    d["difficulty"] = "MEDIUM"
    d["marks"] = 15
    d["input_format"] = "A serialized level-order traversal array of a perfect binary tree."
    d["output_format"] = "A serialized level-order traversal array where each level ends with a null."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root"""

    d["boilerplate"]["python"] = """import sys, json

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def build_tree(arr):
    if not arr: return None
    nodes = [Node(v) if v is not None else None for v in arr]
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

def get_level_order_with_next(root):
    if not root: return []
    res = []
    curr = root
    while curr:
        temp = curr
        while temp:
            res.append(temp.val)
            temp = temp.next
        res.append(None)
        curr = curr.left
    return res

def solve(root):
    if not root: return root
    leftmost = root
    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    return root

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        try:
            arr = json.loads(line)
            root = build_tree(arr)
            root = solve(root)
            print(json.dumps(get_level_order_with_next(root)).replace("None", "null"))
        except:
            print("[]")
    else:
        print("[]")"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 116 in Microsoft")
