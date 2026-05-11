import json
import os

def generate_json():
    problem_id = 143
    title = "Reorder List"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>143. Reorder List</h3>
<p>You are given the head of a singly linked-list. The list can be represented as:</p>

<p style="margin-left: 20px;">L<sub>0</sub> &rarr; L<sub>1</sub> &rarr; &hellip; &rarr; L<sub>n - 1</sub> &rarr; L<sub>n</sub></p>

<p><em>Reorder the list to be on the following form:</em></p>

<p style="margin-left: 20px;">L<sub>0</sub> &rarr; L<sub>n</sub> &rarr; L<sub>1</sub> &rarr; L<sub>n - 1</sub> &rarr; L<sub>2</sub> &rarr; L<sub>n - 2</sub> &rarr; &hellip;</p>

<p>You may not modify the values in the list's nodes. Only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg" style="width: 422px; height: 222px;" />
<pre><strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [1,4,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg" style="width: 542px; height: 222px;" />
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,5,2,4,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the linked-list."
    output_format = "A single line containing space-separated integers representing the reordered list."
    
    constraints = [
        "1 <= number of nodes <= 5 * 10^4",
        "1 <= Node.val <= 1000."
    ]
    
    explanation = """To reorder a linked list in-place using O(1) space:
1. **Find the Middle**:
   - Use two pointers, `slow` and `fast`. When `fast` reaches the end, `slow` will be at the middle.
2. **Reverse the Second Half**:
   - Reverse the linked list starting from the node after `slow`.
   - Disconnect the first half from the second half (`slow.next = None`).
3. **Merge Two Halves**:
   - Interleave nodes from the first half and the reversed second half.
4. **Complexity**:
   - Time Complexity: O(N) because we traverse the list a constant number of times.
   - Space Complexity: O(1) as we modify the pointers in-place."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return
        
    # 1. Find the mid
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # 2. Reverse the second half
    prev, curr = None, slow.next
    slow.next = None # Split
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    # 3. Merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef reorderList(head):\n    # User logic here\n    pass\n\ndef build_list(vals):\n    if not vals: return None\n    dummy = ListNode(0)\n    curr = dummy\n    for v in vals:\n        curr.next = ListNode(int(v))\n        curr = curr.next\n    return dummy.next\n\ndef print_list(head):\n    res = []\n    while head:\n        res.append(str(head.val))\n        head = head.next\n    print(\" \".join(res))\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        head = build_list(data)\n        reorderList(head)\n        print_list(head)",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nstruct ListNode{int val;ListNode*next;ListNode():val(0),next(nullptr){}ListNode(int x):val(x),next(nullptr){}};\nvoid reorderList(ListNode* head){\n    // User logic here\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    istringstream ss(line); vector<int> vals; int x;\n    while(ss>>x) vals.push_back(x);\n    if(vals.empty()) return 0;\n    vector<ListNode*> nodes;\n    for(int v:vals) nodes.push_back(new ListNode(v));\n    for(int i=0;i<(int)nodes.size()-1;i++) nodes[i]->next=nodes[i+1];\n    reorderList(nodes[0]);\n    ListNode*cur=nodes[0]; bool first=true;\n    while(cur){if(!first)cout<<\" \";cout<<cur->val;first=false;cur=cur->next;}\n    cout<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    static class ListNode{int val;ListNode next;ListNode(){}ListNode(int v){val=v;}}\n    public static void reorderList(ListNode head){\n        // User logic here\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine();\n        if(line==null||line.trim().isEmpty()) return;\n        String[] parts=line.trim().split(\"\\\\s+\");\n        ListNode dummy=new ListNode(), cur=dummy;\n        for(String p:parts){cur.next=new ListNode(Integer.parseInt(p));cur=cur.next;}\n        reorderList(dummy.next);\n        cur=dummy.next; StringBuilder sb=new StringBuilder();\n        while(cur!=null){if(sb.length()>0)sb.append(\" \");sb.append(cur.val);cur=cur.next;}\n        System.out.println(sb);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction ListNode(val,next){this.val=(val===undefined?0:val);this.next=(next===undefined?null:next);}\nfunction reorderList(head){\n    // User logic here\n}\nconst data=fs.readFileSync(0,'utf8').trim().split(/\\s+/).filter(Boolean);\nif(data.length){\n  const nodes=data.map(v=>new ListNode(parseInt(v)));\n  for(let i=0;i<nodes.length-1;i++) nodes[i].next=nodes[i+1];\n  reorderList(nodes[0]);\n  const res=[]; let cur=nodes[0]; while(cur){res.push(cur.val);cur=cur.next;}\n  console.log(res.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct ListNode{int val;struct ListNode*next;};\nvoid reorderList(struct ListNode* head){\n    // User logic here\n}\nint main(){\n    char buf[2000000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    struct ListNode*nodes[50001]; int cnt=0;\n    char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&cnt<50001){nodes[cnt]=(struct ListNode*)malloc(sizeof(struct ListNode));nodes[cnt]->val=atoi(tok);nodes[cnt]->next=NULL;cnt++;tok=strtok(NULL,\" \\t\\r\\n\");}\n    if(cnt==0) return 0;\n    for(int i=0;i<cnt-1;i++) nodes[i]->next=nodes[i+1];\n    reorderList(nodes[0]);\n    struct ListNode*cur=nodes[0]; int first=1;\n    while(cur){if(!first)printf(\" \");printf(\"%d\",cur->val);first=0;cur=cur->next;}\n    printf(\"\\n\"); return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4", "expected_output": "1 4 2 3", "is_sample": True},
        {"input": "1 2 3 4 5", "expected_output": "1 5 2 4 3", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 2", "expected_output": "1 2", "is_sample": False},
        {"input": "1 2 3", "expected_output": "1 3 2", "is_sample": False},
        {"input": "10 20 30 40 50 60", "expected_output": "10 60 20 50 30 40", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "1 7 2 6 3 5 4", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 1001)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1000, 0, -1)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 10001)]), "expected_output": "...", "is_sample": False}
    ]

    def _solve(vals):
        n = len(vals)
        if n <= 2: return " ".join(vals)
        from collections import deque
        q = deque(vals)
        res = []
        while q:
            res.append(q.popleft())
            if q:
                res.append(q.pop())
        return " ".join(res)

    for i in range(7, 10):
        test_cases[i]["expected_output"] = _solve(test_cases[i]["input"].split())

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
        "topics": ["Linked List", "Two Pointers", "Stack", "Recursion"],
        "companyIndex": 0
    }

    output_path = "1-200/143_Reorder_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
