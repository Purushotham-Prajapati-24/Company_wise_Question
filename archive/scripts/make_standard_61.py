import json
import os

def generate_json():
    problem_id = 61
    title = "Rotate List"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>61. Rotate List</h3>
<p>Given the <code>head</code> of a linked list, rotate the list to the right by <code>k</code> places.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 450px; height: 191px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [4,5,1,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 305px; height: 350px;" />
<pre>
<strong>Input:</strong> head = [0,1,2], k = 4
<strong>Output:</strong> [2,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 500]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A list of integers representing the linked list followed by an integer k."
    output_format = "A list of integers representing the rotated linked list."
    
    constraints = [
        "The number of nodes in the list is in the range [0, 500].",
        "-100 <= Node.val <= 100",
        "0 <= k <= 2 * 10^9"
    ]
    
    explanation = """To rotate a linked list to the right by k places:
1. **Handle Edge Cases**: If the list is empty, has only one node, or `k = 0`, return the head as is.
2. **Find Length**: Traverse the list to find its length `n` and store a reference to the last node (tail).
3. **Normalize k**: Since rotating by `n` places results in the same list, we only need to rotate by `k % n` places. If `k % n == 0`, no rotation is needed.
4. **Transform into Circular List**: Connect the tail's next to the head, making the list circular.
5. **Find New Tail**: The new tail will be at position `n - (k % n) - 1` from the original head.
6. **Break the Circle**: Set the new head to `new_tail.next` and then set `new_tail.next = None`.
7. **Return**: The new head.

Complexity:
- Time Complexity: O(n), where n is the number of nodes (one pass to find length, another part of a pass to find the split point).
- Space Complexity: O(1)."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head
        
    # Find length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
        
    k = k % length
    if k == 0:
        return head
        
    # Connect tail to head to make it circular
    tail.next = head
    
    # Find new tail: (length - k - 1) nodes from head
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
        
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef rotateRight(head, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if not data:\n        print('[]')\n    else:\n        k = int(data[-1])\n        vals = list(map(int, data[:-1]))\n        head = None\n        for v in reversed(vals):\n            head = ListNode(v, head)\n        result = rotateRight(head, k)\n        out = []\n        while result:\n            out.append(str(result.val))\n            result = result.next\n        print('[' + ', '.join(out) + ']')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nstruct ListNode {int val; ListNode*next; ListNode(int x):val(x),next(NULL){};};\nListNode* rotateRight(ListNode* head, long long k) {\n    // User logic\n    return head;\n}\nint main() {\n    string line; if(!getline(cin,line)){cout<<\"[]\"<<endl;return 0;}\n    istringstream ss(line); vector<int> t; int x;\n    while(ss>>x) t.push_back(x);\n    if(t.empty()){cout<<\"[]\"<<endl;return 0;}\n    long long k=t.back(); t.pop_back();\n    ListNode* head=NULL;\n    for(int i=(int)t.size()-1;i>=0;i--){ListNode* n=new ListNode(t[i]);n->next=head;head=n;}\n    ListNode* res=rotateRight(head,k);\n    cout<<\"[\"; bool f=true;\n    while(res){if(!f)cout<<\", \";cout<<res->val;f=false;res=res->next;}\n    cout<<\"]\"<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    static class ListNode {int val; ListNode next; ListNode(int x){val=x;}}\n    public static ListNode rotateRight(ListNode head, int k) {\n        // User logic\n        return head;\n    }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in);\n        if(!sc.hasNextLine()){System.out.println(\"[]\");return;}\n        String[] parts=sc.nextLine().trim().split(\"\\\\s+\");\n        if(parts.length==0||parts[0].isEmpty()){System.out.println(\"[]\");return;}\n        long k=Long.parseLong(parts[parts.length-1]);\n        ListNode head=null;\n        for(int i=parts.length-2;i>=0;i--){ListNode n=new ListNode(Integer.parseInt(parts[i]));n.next=head;head=n;}\n        ListNode res=rotateRight(head,(int)(k%500+500)%500);\n        StringBuilder sb=new StringBuilder(\"[\"); boolean f=true;\n        while(res!=null){if(!f)sb.append(\", \");sb.append(res.val);f=false;res=res.next;}\n        sb.append(\"]\"); System.out.println(sb);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction ListNode(val,next){this.val=(val===undefined?0:val);this.next=(next===undefined?null:next);}\nfunction rotateRight(head,k){\n    // User logic\n    return head;\n}\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(tokens.length===0||tokens[0]===''){console.log('[]');}\nelse{\n  const k=parseInt(tokens[tokens.length-1]);\n  const vals=tokens.slice(0,-1).map(Number);\n  let head=null;\n  for(let i=vals.length-1;i>=0;i--){const n=new ListNode(vals[i]);n.next=head;head=n;}\n  let res=rotateRight(head,k);\n  const out=[];\n  while(res){out.push(res.val);res=res.next;}\n  console.log('['+out.join(', ')+']');\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct ListNode{int val;struct ListNode*next;};\nstruct ListNode* rotateRight(struct ListNode*head, int k){\n    // User logic\n    return head;\n}\nint main(){\n    char line[10000];\n    if(!fgets(line,sizeof(line),stdin)){printf(\"[]\\n\");return 0;}\n    int vals[501]; int cnt=0;\n    char*tok=strtok(line,\" \\t\\r\\n\");\n    while(tok&&cnt<501){vals[cnt++]=atoi(tok);tok=strtok(NULL,\" \\t\\r\\n\");}\n    if(cnt==0){printf(\"[]\\n\");return 0;}\n    int k=vals[cnt-1]; cnt--;\n    struct ListNode*nodes[501];\n    for(int i=0;i<cnt;i++){nodes[i]=(struct ListNode*)malloc(sizeof(struct ListNode));nodes[i]->val=vals[i];nodes[i]->next=NULL;}\n    for(int i=0;i<cnt-1;i++) nodes[i]->next=nodes[i+1];\n    struct ListNode*res=rotateRight(cnt>0?nodes[0]:NULL,k);\n    printf(\"[\"); int f=1;\n    while(res){if(!f)printf(\", \");printf(\"%d\",res->val);f=0;res=res->next;}\n    printf(\"]\\n\"); return 0;\n}"
    }

    def _rot(vals, k):
        if not vals: return []
        n = len(vals)
        k = k % n
        if k == 0: return vals
        return vals[n-k:] + vals[:n-k]

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 3 4 5 2", "expected_output": str(_rot([1,2,3,4,5], 2)), "is_sample": True},
        {"input": "0 1 2 4", "expected_output": str(_rot([0,1,2], 4)), "is_sample": True},
        # Middle five: Diverse cases
        {"input": "1 1", "expected_output": "[1]", "is_sample": False},
        {"input": "1 2 0", "expected_output": "[1, 2]", "is_sample": False},
        {"input": "1 2 2", "expected_output": "[1, 2]", "is_sample": False},
        {"input": "1 2 3 1", "expected_output": "[3, 1, 2]", "is_sample": False},
        {"input": "5 10 15 2", "expected_output": "[10, 15, 5]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(map(str, range(500))) + " 2000000000", "expected_output": str(_rot(list(range(500)), 2000000000)), "is_sample": False},
        {"input": "1 2000000000", "expected_output": "[1]", "is_sample": False},
        {"input": " ".join(map(str, range(10))) + " 5", "expected_output": str(_rot(list(range(10)), 5)), "is_sample": False}
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
        "topics": ["Linked List", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "1-200/61_Rotate_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
