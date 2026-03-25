import json
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
        # Find next level start
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

specs = [
    {"arr": [1,2,3,4,5,None,7], "is_sample": True},
    {"arr": [], "is_sample": True},
    {"arr": [1], "is_sample": False},
    {"arr": [1,2,None,3,None,4,None,5], "is_sample": False},
    {"arr": [1,None,2,None,3,None,4,None,5], "is_sample": False},
    {"arr": [1,2,3,4,None,None,5], "is_sample": False},
    {"arr": [1,2,3,4,5,6,7], "is_sample": False},
    {"arr": [1,2,None,None,3,4], "is_sample": False},
    {"arr": list(range(1, 32)), "is_sample": False},
    {"arr": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "is_sample": False}
]

final_tcs = []
for spec in specs:
    arr = spec["arr"]
    root = build_tree(arr)
    root = connect(root)
    expected = get_level_order_with_next(root)
    
    in_str = json.dumps(arr).replace(" ", "")
    out_str = json.dumps(expected).replace("null", "null").replace(" ", "")
    
    final_tcs.append({
        "input": in_str,
        "expected_output": out_str,
        "is_sample": spec["is_sample"]
    })

file_path = 'd:/College Projects/MNC_based/companyWiseQuestions/Visa/117_Populating_Next_Right_Pointers_in_Each_Node_II.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data['test_cases'] = final_tcs

if "<h3>117 " in data['question_text']:
     data['question_text'] = data['question_text'].replace("<h3>117 ", "<h3>117. ")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Updated 117 in Visa")
