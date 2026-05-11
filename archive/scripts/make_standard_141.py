import json
import os

def generate_json():
    problem_id = 141
    title = "Linked List Cycle"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>141. Linked List Cycle</h3>
<p>Given <code>head</code>, the head of a linked list, determine if the linked list has a cycle in it.</p>

<p>There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the&nbsp;<code>next</code>&nbsp;pointer. Internally, <code>pos</code>&nbsp;is used to denote the index of the node that&nbsp;tail's&nbsp;<code>next</code>&nbsp;pointer is connected to.&nbsp;<strong>Note that&nbsp;<code>pos</code>&nbsp;is not passed as a parameter</strong>.</p>

<p>Return&nbsp;<code>true</code><em> if there is a cycle in the linked list</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="width: 300px; height: 97px; margin-top: 8px; margin-bottom: 8px;" />
<pre><strong>Input:</strong> head = [3,2,0,-4], pos = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="width: 141px; height: 74px;" />
<pre><strong>Input:</strong> head = [1,2], pos = 0
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a cycle in the linked list, where the tail connects to the 0th node.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="width: 45px; height: 45px;" />
<pre><strong>Input:</strong> head = [1], pos = -1
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no cycle in the linked list.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>pos</code> is <code>-1</code> or a <strong>valid index</strong> in the linked-list.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you solve it using <code>O(1)</code> (i.e., constant) memory?</p>"""

    input_format = "Two lines. Line 1: space-separated integers for node values. Line 2: pos (-1 for no cycle, else index of node connected by tail)."
    output_format = "true if there is a cycle, false otherwise."
    
    constraints = [
        "0 <= number of nodes <= 10^4",
        "-10^5 <= Node.val <= 10^5",
        "pos is -1 or a valid index."
    ]
    
    explanation = """To determine if a linked list has a cycle using O(1) space:
1. **Floyd's Cycle-Finding Algorithm (Tortoise and Hare)**:
   - Use two pointers, `slow` and `fast`.
   - Initialize both to the `head` of the list.
   - Move `slow` by one step and `fast` by two steps in each iteration.
2. **Logic**:
   - If there is no cycle, `fast` (or `fast.next`) will eventually reach `None`.
   - If there is a cycle, the `fast` pointer will eventually "lap" the `slow` pointer, and they will meet at the same node.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(1) as only two pointers are used."""
    
    answer = """class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
            
    return False"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, x):\n        self.val = x\n        self.next = None\n\ndef hasCycle(head):\n    # User logic here\n    pass\n\ndef build_list(vals, pos):\n    if not vals: return None\n    nodes = [ListNode(int(v)) for v in vals]\n    for i in range(len(nodes) - 1):\n        nodes[i].next = nodes[i+1]\n    if pos != -1:\n        nodes[-1].next = nodes[pos]\n    return nodes[0]\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        vals = lines[0].split()\n        pos = int(lines[1].strip())\n        print(str(hasCycle(build_list(vals, pos))).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nstruct ListNode{int val;ListNode*next;ListNode(int x):val(x),next(NULL){}};\nbool hasCycle(ListNode* head){\n    // User logic\n    return false;\n}\nint main(){\n    string vline,pline;\n    if(!getline(cin,vline)||!getline(cin,pline)) return 0;\n    istringstream ss(vline); vector<int> vals; int x;\n    while(ss>>x) vals.push_back(x);\n    int pos=stoi(pline);\n    if(vals.empty()){cout<<\"false\"<<endl;return 0;}\n    vector<ListNode*> nodes;\n    for(int v:vals) nodes.push_back(new ListNode(v));\n    for(int i=0;i<(int)nodes.size()-1;i++) nodes[i]->next=nodes[i+1];\n    if(pos!=-1) nodes.back()->next=nodes[pos];\n    cout<<(hasCycle(nodes[0])?\"true\":\"false\")<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    static class ListNode{int val;ListNode next;ListNode(int x){val=x;}}\n    public static boolean hasCycle(ListNode head){\n        // User logic\n        return false;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String vline=br.readLine(), pline=br.readLine();\n        if(vline==null||pline==null){System.out.println(\"false\");return;}\n        String[] parts=vline.trim().split(\"\\\\s+\");\n        int pos=Integer.parseInt(pline.trim());\n        if(parts[0].isEmpty()){System.out.println(\"false\");return;}\n        List<ListNode> nodes=new ArrayList<>();\n        for(String p:parts) if(!p.isEmpty()) nodes.add(new ListNode(Integer.parseInt(p)));\n        for(int i=0;i<nodes.size()-1;i++) nodes.get(i).next=nodes.get(i+1);\n        if(pos!=-1&&pos<nodes.size()) nodes.get(nodes.size()-1).next=nodes.get(pos);\n        System.out.println(hasCycle(nodes.get(0))?\"true\":\"false\");\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction ListNode(val){this.val=val;this.next=null;}\nfunction hasCycle(head){\n    // User logic\n    return false;\n}\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=2){\n  const vals=lines[0].trim().split(/\\s+/).filter(Boolean);\n  const pos=parseInt(lines[1].trim());\n  if(!vals.length){console.log('false');}\n  else{\n    const nodes=vals.map(v=>new ListNode(parseInt(v)));\n    for(let i=0;i<nodes.length-1;i++) nodes[i].next=nodes[i+1];\n    if(pos!==-1) nodes[nodes.length-1].next=nodes[pos];\n    console.log(hasCycle(nodes[0])?'true':'false');\n  }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\nstruct ListNode{int val;struct ListNode*next;};\nbool hasCycle(struct ListNode* head){\n    // User logic\n    return false;\n}\nint main(){\n    char vline[200000],pline[20];\n    if(!fgets(vline,sizeof(vline),stdin)||!fgets(pline,sizeof(pline),stdin)){printf(\"false\\n\");return 0;}\n    int pos=atoi(pline);\n    struct ListNode*nodes[10001]; int cnt=0;\n    char*tok=strtok(vline,\" \\t\\r\\n\");\n    while(tok&&cnt<10001){nodes[cnt]=(struct ListNode*)malloc(sizeof(struct ListNode));nodes[cnt]->val=atoi(tok);nodes[cnt]->next=NULL;cnt++;tok=strtok(NULL,\" \\t\\r\\n\");}\n    if(cnt==0){printf(\"false\\n\");return 0;}\n    for(int i=0;i<cnt-1;i++) nodes[i]->next=nodes[i+1];\n    if(pos!=-1&&pos<cnt) nodes[cnt-1]->next=nodes[pos];\n    printf(\"%s\\n\",hasCycle(nodes[0])?\"true\":\"false\"); return 0;\n}"
    }

    test_cases = [
        {"input": "3 2 0 -4\\n1", "expected_output": "true", "is_sample": True},
        {"input": "1 2\\n0", "expected_output": "true", "is_sample": True},
        {"input": "1\\n-1", "expected_output": "false", "is_sample": True},
        {"input": "\\n-1", "expected_output": "false", "is_sample": False},
        {"input": "1 2 3 4 5\\n-1", "expected_output": "false", "is_sample": False},
        {"input": "1 2 3 4 5\\n2", "expected_output": "true", "is_sample": False},
        {"input": "1 2 3 4 5\\n4", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n-1", "expected_output": "false", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n0", "expected_output": "true", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n9999", "expected_output": "true", "is_sample": False}
    ]

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
        "topics": ["Linked List", "Two Pointers", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "1-200/141_Linked_List_Cycle.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
