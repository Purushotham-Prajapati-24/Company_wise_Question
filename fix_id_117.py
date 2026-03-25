import json
import os
from collections import deque

def generate_test_cases():
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
            # Find next level leftmost
            head = curr
            curr = None
            while head:
                if head.left:
                    curr = head.left
                    break
                if head.right:
                    curr = head.right
                    break
                head = head.next
        return res

    def connect(root):
        if not root: return root
        queue = deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i < n - 1:
                    node.next = queue[0]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return root

    cases = [
        {"input": "[1,2,3,4,5,null,7]", "expected_output": "[1,null,2,3,null,4,5,7,null]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": True},
    ]

    # Case 10: 6000 nodes (Peak Constraint)
    vals10 = [1] * 6000
    root10 = connect(build_tree(vals10))
    cases.append({"input": json.dumps(vals10), "expected_output": json.dumps(get_level_order_with_next(root10)).replace("None", "null"), "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Bloomberg/117_Populating_Next_Right_Pointers_in_Each_Node_II.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>117 Populating Next Right Pointers in Each Node II</h3><p>Given a binary tree</p><pre>struct Node {\\n  int val;\\n  Node *left;\\n  Node *right;\\n  Node *next;\\n}</pre><p>Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to <code>NULL</code>.</p><p>Initially, all next pointers are set to <code>NULL</code>.</p>"
    d["difficulty"] = "MEDIUM"
    d["marks"] = 15
    d["input_format"] = "A serialized level-order traversal array of a binary tree."
    d["output_format"] = "A serialized level-order traversal array where each level ends with a null."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = collections.deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i < n - 1:
                    node.next = queue[0]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return root"""

    d["boilerplate"]["python"] = """import sys, json
from collections import deque

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
        head = curr
        curr = None
        while head:
            if head.left:
                curr = head.left
                break
            if head.right:
                curr = head.right
                break
            head = head.next
    return res

def solve(root):
    if not root: return root
    queue = deque([root])
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            if i < n - 1:
                node.next = queue[0]
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
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
    print("Standardized ID 117 in Bloomberg")
