import json
import os

def generate_json():
    problem_id = 148
    title = "Sort List"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>148. Sort List</h3>
<p>Given the <code>head</code> of a linked list, return <em>the list after sorting it in <strong>ascending order</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg" style="width: 422px; height: 302px;" />
<pre><strong>Input:</strong> head = [4,2,1,3]
<strong>Output:</strong> [1,2,3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg" style="width: 542px; height: 302px;" />
<pre><strong>Input:</strong> head = [-1,5,3,4,0]
<strong>Output:</strong> [-1,0,3,4,5]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you sort the linked list in <code>O(n log n)</code> time and <code>O(1)</code> memory (i.e., constant space)?</p>"""

    input_format = "A single line containing space-separated integers representing the linked-list."
    output_format = "A single line containing space-separated integers representing the sorted list."
    
    constraints = [
        "0 <= number of nodes <= 5 * 10^4",
        "-10^5 <= Node.val <= 10^5."
    ]
    
    explanation = """To sort a linked list in O(N log N) time:
1. **Merge Sort (Recursive Divide and Conquer)**:
   - **Divide**: Find the middle of the linked list using the slow/fast pointer technique. Split the list into two halves.
   - **Conquer**: Recursively sort each half.
   - **Merge**: Merge the two sorted halves into a single sorted list.
2. **Logic**:
   - Base case: If the list is empty or has only one node, it is already sorted.
   - Keep splitting until single-node lists are reached, then merge them upwards.
3. **Complexity**:
   - Time Complexity: O(N log N) because we split the list log N times and merge N elements at each level.
   - Space Complexity: O(log N) due to the recursion stack (can be O(1) using iterative bottom-up merge sort)."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head
        
    # Split the list into two halves
    mid = getMid(head)
    left = head
    right = mid.next
    mid.next = None
    
    # Recursively sort
    left = sortList(left)
    right = sortList(right)
    
    # Merge
    return merge(left, right)

def getMid(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef sortList(head):\n    # User logic here\n    pass\n\ndef build_list(vals):\n    if not vals: return None\n    dummy = ListNode(0)\n    curr = dummy\n    for v in vals:\n        curr.next = ListNode(int(v))\n        curr = curr.next\n    return dummy.next\n\ndef print_list(head):\n    res = []\n    while head:\n        res.append(str(head.val))\n        head = head.next\n    print(\" \".join(res))\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        head = build_list(data)\n        sorted_head = sortList(head)\n        print_list(sorted_head)\n    else:\n        print(\"\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nstruct ListNode{int val;ListNode*next;ListNode():val(0),next(nullptr){}ListNode(int x):val(x),next(nullptr){}};\nListNode* sortList(ListNode* head){\n    // User logic here\n    return nullptr;\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    istringstream ss(line); vector<int> vals; int x;\n    while(ss>>x) vals.push_back(x);\n    if(vals.empty()){return 0;}\n    vector<ListNode*> nodes;\n    for(int v:vals) nodes.push_back(new ListNode(v));\n    for(int i=0;i<(int)nodes.size()-1;i++) nodes[i]->next=nodes[i+1];\n    ListNode* head=sortList(nodes[0]);\n    bool first=true;\n    while(head){if(!first)cout<<\" \";cout<<head->val;first=false;head=head->next;}\n    cout<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    static class ListNode{int val;ListNode next;ListNode(){}ListNode(int v){val=v;}}\n    public static ListNode sortList(ListNode head){\n        // User logic here\n        return null;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine();\n        if(line==null||line.trim().isEmpty()) return;\n        String[] parts=line.trim().split(\"\\\\s+\");\n        ListNode dummy=new ListNode(), cur=dummy;\n        for(String p:parts) if(!p.isEmpty()){cur.next=new ListNode(Integer.parseInt(p));cur=cur.next;}\n        ListNode head=sortList(dummy.next);\n        StringBuilder sb=new StringBuilder();\n        while(head!=null){if(sb.length()>0)sb.append(\" \");sb.append(head.val);head=head.next;}\n        System.out.println(sb);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction ListNode(val,next){this.val=(val===undefined?0:val);this.next=(next===undefined?null:next);}\nfunction sortList(head){\n    // User logic here\n    return null;\n}\nconst data=fs.readFileSync(0,'utf8').trim().split(/\\s+/).filter(Boolean);\nif(data.length){\n  const nodes=data.map(v=>new ListNode(parseInt(v)));\n  for(let i=0;i<nodes.length-1;i++) nodes[i].next=nodes[i+1];\n  let head=sortList(nodes[0]);\n  const res=[]; while(head){res.push(head.val);head=head.next;}\n  console.log(res.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct ListNode{int val;struct ListNode*next;};\nstruct ListNode* sortList(struct ListNode* head){\n    // User logic here\n    return NULL;\n}\nint main(){\n    char buf[2000000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    struct ListNode*nodes[50001]; int cnt=0;\n    char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&cnt<50001){nodes[cnt]=(struct ListNode*)malloc(sizeof(struct ListNode));nodes[cnt]->val=atoi(tok);nodes[cnt]->next=NULL;cnt++;tok=strtok(NULL,\" \\t\\r\\n\");}\n    if(cnt==0) return 0;\n    for(int i=0;i<cnt-1;i++) nodes[i]->next=nodes[i+1];\n    struct ListNode*head=sortList(nodes[0]); int first=1;\n    while(head){if(!first)printf(\" \");printf(\"%d\",head->val);first=0;head=head->next;}\n    printf(\"\\n\"); return 0;\n}"
    }

    test_cases = [
        {"input": "4 2 1 3", "expected_output": "1 2 3 4", "is_sample": True},
        {"input": "-1 5 3 4 0", "expected_output": "-1 0 3 4 5", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "2 1", "expected_output": "1 2", "is_sample": False},
        {"input": "5 4 3 2 1", "expected_output": "1 2 3 4 5", "is_sample": False},
        {"input": "1 3 2 4 5 7 6", "expected_output": "1 2 3 4 5 6 7", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1000, 0, -1)]), "expected_output": " ".join([str(i) for i in range(1, 1001)]), "is_sample": False},
        {"input": " ".join([str(i) for i in range(5000, 0, -1)]), "expected_output": " ".join([str(i) for i in range(1, 5001)]), "is_sample": False},
        {"input": " ".join([str(i%100) for i in range(5000)]), "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(vals):
        if not vals: return ""
        ints = sorted([int(v) for v in vals])
        return " ".join(map(str, ints))

    test_cases[-1]["expected_output"] = _solve(test_cases[-1]["input"].split())

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
        "topics": ["Linked List", "Two Pointers", "Divide and Conquer", "Sorting", "Merge Sort"],
        "companyIndex": 0
    }

    output_path = "1-200/148_Sort_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
