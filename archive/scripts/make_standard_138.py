import json
import os

def generate_json():
    problem_id = 138
    title = "Copy List with Random Pointer"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>138. Copy List with Random Pointer</h3>
<p>A linked list of length <code>n</code> is given such that each node contains an additional random pointer, which could point to any node in the list, or <code>null</code>.</p>

<p>Construct a <strong>deep copy</strong> of the list. The deep copy should consist of exactly <code>n</code> <strong>brand new</strong> nodes, where each new node has its value set to the value of its corresponding original node. Both the <code>next</code> and <code>random</code> pointer of the new nodes should still point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. <strong>None of the pointers in the new list should point to nodes in the original list</strong>.</p>

<p>For example, if there are two nodes <code>X</code> and <code>Y</code> in the original list, where <code>X.random --&gt; Y</code>, then for the corresponding two nodes <code>x</code> and <code>y</code> in the copied list, <code>x.random --&gt; y</code>.</p>

<p>Return <em>the head of the copied linked list</em>.</p>

<p>The linked list is represented in the input/output as a list of <code>n</code> nodes. Each node is represented as a pair of <code>[val, random_index]</code> where:</p>

<ul>
	<li><code>val</code>: an integer representing <code>Node.val</code></li>
	<li><code>random_index</code>: the index of the node (range from <code>0</code> to <code>n-1</code>) that the <code>random</code> pointer points to, or <code>null</code> if it does not point to any node.</li>
</ul>

<p>Your code will <strong>only</strong> be given the <code>head</code> of the original linked list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e1.png" style="width: 700px; height: 142px;" />
<pre><strong>Input:</strong> head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
<strong>Output:</strong> [[7,null],[13,0],[11,4],[10,2],[1,0]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e2.png" style="width: 358px; height: 103px;" />
<pre><strong>Input:</strong> head = [[1,1],[2,1]]
<strong>Output:</strong> [[1,1],[2,1]]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e3.png" style="width: 367px; height: 103px;" />
<pre><strong>Input:</strong> head = [[3,null],[3,0],[3,null]]
<strong>Output:</strong> [[3,null],[3,0],[3,null]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><code>Node.random</code> is <code>null</code> or is pointing to some node in the linked list.</li>
</ul>"""

    input_format = "A JSON array of [val, random_index] pairs representing the linked list."
    output_format = "A JSON array of [val, random_index] pairs representing the deep-copied list."
    
    constraints = [
        "0 <= n <= 1000",
        "-10^4 <= Node.val <= 10^4",
        "Deep copy must not reference original nodes.",
        "random can be null or any node in the list."
    ]
    
    explanation = """To deep copy a linked list with random pointers:
1. **Hash Map Approach**:
   - Use a dictionary to map each original node to its brand new clone: `mapping = {orig_node: Node(orig_node.val)}`.
   - Iterate through the original list once to create all the clones.
   - Iterate a second time to link the clones' `next` and `random` pointers based on the mapping: `mapping[orig_node].next = mapping[orig_node.next]`.
2. **Interweaving Approach (Space Efficient)**:
   - Create copy nodes and insert them between original nodes: `A -> A' -> B -> B'`.
   - Assign `random` pointers: `A'.random = A.random.next` (since `A.random.next` is the clone of `A.random`).
   - Separate the original and copied lists.
3. **Complexity**:
   - Time Complexity: O(N) as it requires a few passes.
   - Space Complexity: O(N) for the hash map, or O(1) for the interweaving approach."""
    
    answer = """class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Use a map to link original nodes to their copies
        mapping = {None: None}
        
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        while curr:
            mapping[curr].next = mapping[curr.next]
            mapping[curr].random = mapping[curr.random]
            curr = curr.next
            
        return mapping[head]"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Node:\n    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):\n        self.val = int(x)\n        self.next = next\n        self.random = random\n\ndef build_list(arr):\n    if not arr: return None\n    nodes = [Node(x[0]) for x in arr]\n    for i, node in enumerate(nodes):\n        if i < len(nodes) - 1: node.next = nodes[i+1]\n        if arr[i][1] is not None: node.random = nodes[arr[i][1]]\n    return nodes[0]\n\ndef list_to_arr(head):\n    if not head: return []\n    res = []\n    node_to_idx = {}\n    curr = head\n    idx = 0\n    while curr:\n        node_to_idx[curr] = idx\n        curr = curr.next\n        idx += 1\n    curr = head\n    while curr:\n        ridx = node_to_idx.get(curr.random, None)\n        res.append([curr.val, ridx])\n        curr = curr.next\n    return res\n\ndef copyRandomList(head):\n    # User logic\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if not line: print([]); sys.exit()\n    arr = json.loads(line)\n    print(json.dumps(list_to_arr(copyRandomList(build_list(arr)))))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <sstream>\nusing namespace std;\nclass Node{public:int val;Node*next,*random;Node(int v):val(v),next(NULL),random(NULL){}};\nNode* copyRandomList(Node* head){\n    // User logic\n    return nullptr;\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    // input: [[v,r],...] where r is index or null\n    if(line==\"[]\"){cout<<\"[]\"<<endl;return 0;}\n    // parse\n    vector<int> vals; vector<int> rands;\n    // manually parse JSON\n    int i=1,n=line.size();\n    while(i<n){\n        if(line[i]=='['){\n            i++;\n            // read val\n            int neg=1; if(line[i]=='-'){neg=-1;i++;}\n            int v=0; while(i<n&&isdigit(line[i])) v=v*10+(line[i++]-'0'); v*=neg;\n            vals.push_back(v);\n            i++; // comma\n            // read rand (might be null)\n            if(i<n&&line[i]=='n'){rands.push_back(-1);while(i<n&&line[i]!=']')i++;}\n            else{int neg2=1;if(line[i]=='-'){neg2=-1;i++;}int r=0;while(i<n&&isdigit(line[i]))r=r*10+(line[i++]-'0');r*=neg2;rands.push_back(r);}\n            while(i<n&&line[i]!=']') i++; i++; // skip ]\n        } else i++;\n    }\n    if(vals.empty()){cout<<\"[]\"<<endl;return 0;}\n    int sz=vals.size();\n    vector<Node*> nodes(sz);\n    for(int k=0;k<sz;k++) nodes[k]=new Node(vals[k]);\n    for(int k=0;k<sz-1;k++) nodes[k]->next=nodes[k+1];\n    for(int k=0;k<sz;k++) if(rands[k]!=-1) nodes[k]->random=nodes[rands[k]];\n    Node* cloned=copyRandomList(nodes[0]);\n    // serialize\n    vector<Node*> clist; Node*cur=cloned;\n    while(cur){clist.push_back(cur);cur=cur->next;}\n    unordered_map<Node*,int> idx;\n    for(int k=0;k<(int)clist.size();k++) idx[clist[k]]=k;\n    cout<<\"[\";\n    for(int k=0;k<(int)clist.size();k++){\n        int ri=clist[k]->random?idx[clist[k]->random]:-1;\n        cout<<\"[\"<<clist[k]->val<<\", \";\n        if(ri==-1) cout<<\"null\"; else cout<<ri;\n        cout<<\"]\";if(k+1<(int)clist.size())cout<<\", \";\n    }\n    cout<<\"]\"<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    static class Node{int val;Node next,random;Node(int v){val=v;}}\n    public static Node copyRandomList(Node head){\n        // User logic\n        return null;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine().trim();\n        if(line==null||line.equals(\"[]\")){ System.out.println(\"[]\"); return;}\n        List<int[]> pairs=new ArrayList<>();\n        int i=1,n=line.length();\n        while(i<n){\n            if(line.charAt(i)=='['){\n                i++;\n                int neg=1; if(line.charAt(i)=='-'){neg=-1;i++;}\n                int v=0; while(i<n&&Character.isDigit(line.charAt(i)))v=v*10+(line.charAt(i++)-'0'); v*=neg;\n                i++; // comma+space\n                if(i<n&&line.charAt(i)==' ')i++;\n                int r;\n                if(i<n&&line.charAt(i)=='n'){r=-1;while(i<n&&line.charAt(i)!=']')i++;}\n                else{int neg2=1;if(line.charAt(i)=='-'){neg2=-1;i++;}r=0;while(i<n&&Character.isDigit(line.charAt(i)))r=r*10+(line.charAt(i++)-'0');r*=neg2;}\n                pairs.add(new int[]{v,r});\n                while(i<n&&line.charAt(i)!=']')i++; i++;\n            } else i++;\n        }\n        if(pairs.isEmpty()){System.out.println(\"[]\");return;}\n        int sz=pairs.size();\n        Node[] nodes=new Node[sz];\n        for(int k=0;k<sz;k++) nodes[k]=new Node(pairs.get(k)[0]);\n        for(int k=0;k<sz-1;k++) nodes[k].next=nodes[k+1];\n        for(int k=0;k<sz;k++) if(pairs.get(k)[1]!=-1) nodes[k].random=nodes[pairs.get(k)[1]];\n        Node cloned=copyRandomList(nodes[0]);\n        List<Node> clist=new ArrayList<>(); Node cur=cloned;\n        while(cur!=null){clist.add(cur);cur=cur.next;}\n        Map<Node,Integer> idx=new IdentityHashMap<>();\n        for(int k=0;k<clist.size();k++) idx.put(clist.get(k),k);\n        StringBuilder sb=new StringBuilder(\"[\");\n        for(int k=0;k<clist.size();k++){\n            Node nd=clist.get(k);\n            int ri=nd.random!=null?idx.getOrDefault(nd.random,-1):-1;\n            sb.append(\"[\").append(nd.val).append(\", \");\n            if(ri==-1)sb.append(\"null\");else sb.append(ri);\n            sb.append(\"]\"); if(k+1<clist.size())sb.append(\", \");\n        }\n        sb.append(\"]\"); System.out.println(sb);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction Node(val){this.val=val;this.next=null;this.random=null;}\nfunction copyRandomList(head){\n    // User logic\n    return null;\n}\nconst line=fs.readFileSync(0,'utf8').trim();\nif(!line||line==='[]'){console.log('[]');}\nelse{\n  const arr=JSON.parse(line);\n  const nodes=arr.map(([v])=>new Node(v));\n  for(let i=0;i<nodes.length-1;i++) nodes[i].next=nodes[i+1];\n  for(let i=0;i<arr.length;i++) if(arr[i][1]!==null) nodes[i].random=nodes[arr[i][1]];\n  const cloned=copyRandomList(nodes[0]);\n  const clist=[]; let cur=cloned; while(cur){clist.push(cur);cur=cur.next;}\n  const idx=new Map(); clist.forEach((n,i)=>idx.set(n,i));\n  const res=clist.map(n=>[n.val,n.random!=null?(idx.get(n.random)??null):null]);\n  console.log('['+res.map(([v,r])=>'['+v+', '+(r===null?'null':r)+']').join(', ')+']');\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct Node{int val;struct Node*next,*random;};\nstruct Node* copyRandomList(struct Node* head){\n    // User logic\n    return NULL;\n}\nint main(){\n    printf(\"[]\\n\"); return 0;\n}"
    }

    test_cases = [
        {"input": "[[7,null],[13,0],[11,4],[10,2],[1,0]]", "expected_output": "[[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]", "is_sample": True},
        {"input": "[[1,1],[2,1]]", "expected_output": "[[1, 1], [2, 1]]", "is_sample": True},
        {"input": "[[3,null],[3,0],[3,null]]", "expected_output": "[[3, null], [3, 0], [3, null]]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": False},
        {"input": "[[1,null]]", "expected_output": "[[1, null]]", "is_sample": False},
        {"input": "[[1,0]]", "expected_output": "[[1, 0]]", "is_sample": False},
        {"input": "[[1,2],[2,null],[3,1]]", "expected_output": "[[1, 2], [2, null], [3, 1]]", "is_sample": False},
        # Stress Tests (N=1000)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    # Stress 8: Circular last to first
    arr8 = [[i, (i + 1) % 1000] for i in range(1000)]
    test_cases[7] = {"input": json.dumps(arr8), "expected_output": json.dumps(arr8), "is_sample": False}
    # Stress 9: All random to first
    arr9 = [[i, 0] for i in range(1000)]
    test_cases[8] = {"input": json.dumps(arr9), "expected_output": json.dumps(arr9), "is_sample": False}
    # Stress 10: Random null
    arr10 = [[i, None] for i in range(1000)]
    test_cases[9] = {"input": json.dumps(arr10), "expected_output": json.dumps(arr10), "is_sample": False}

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
        "topics": ["Linked List", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "1-200/138_Copy_List_with_Random_Pointer.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
