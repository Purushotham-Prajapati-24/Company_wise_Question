import json
import os

def generate_json():
    problem_id = 117
    title = "Populating Next Right Pointers in Each Node II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>117. Populating Next Right Pointers in Each Node II</h3>
<p>Given a binary tree</p>

<pre>
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
</pre>

<p>Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to <code>NULL</code>.</p>
<p>Initially, all next pointers are set to <code>NULL</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/15/117_sample.png" style="width: 500px; height: 171px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,null,7]
<strong>Output:</strong> [1,#,2,3,#,4,5,7,#]
<strong>Explanation: </strong>Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 6000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong>
<ul>
	<li>You may only use constant extra space.</li>
	<li>The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.</li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree (integers or 'null')."
    output_format = "A single line containing space-separated values representing the level-order traversal with '#' at the end of each level."
    
    constraints = [
        "0 <= number of nodes <= 6000",
        "-100 <= Node.val <= 100.",
        "The tree can be any binary tree (not necessarily perfect)."
    ]
    
    explanation = """To populate the `next` pointers in any binary tree using O(1) extra space:
1. **Level-by-Level Iteration with Dummy Node**:
   - For each level, we use a `dummy` node to act as a placeholder for the head of the next level.
   - We maintain a `prev` pointer initialized to `dummy` to connect nodes in the next level as we find them.
2. **Logic**:
   - Traverse the current level using the existing `next` pointers.
   - For each node `curr` in the current level:
     - If `curr.left` exists, link `prev.next = curr.left` and move `prev`.
     - If `curr.right` exists, link `prev.next = curr.right` and move `prev`.
   - After finishing the current level, move to the head of the next level: `curr = dummy.next`.
3. **Complexity**:
   - Time Complexity: O(N) because each node is visited once.
   - Space Complexity: O(1) as we reuse pointers and only use a few temporary variables."""
    
    answer = """class Node:
    def __init__(self, val: int = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return root
    
    curr = root
    while curr:
        dummy = Node(0)
        prev = dummy
        while curr:
            if curr.left:
                prev.next = curr.left
                prev = prev.next
            if curr.right:
                prev.next = curr.right
                prev = prev.next
            curr = curr.next
        # Move to the first node of the next level
        curr = dummy.next
        
    return root"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass Node:\n    def __init__(self, val: int = 0, left=None, right=None, next=None):\n        self.val = val\n        self.left = left\n        self.right = right\n        self.next = next\n\ndef connect(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = Node(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = Node(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = Node(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef serialize(root):\n    if not root: return \"\"\n    res = []\n    leftmost = root\n    while leftmost:\n        curr = leftmost\n        next_level_head = None\n        while curr:\n            res.append(str(curr.val))\n            if not next_level_head:\n                if curr.left: next_level_head = curr.left\n                elif curr.right: next_level_head = curr.right\n            curr = curr.next\n        res.append(\"#\")\n        # Finding the leftmost node of the next level is tricky if current leftmost has no children\n        # The dummy approach in the logic is better. Let's use it here too.\n        temp_dummy = Node(0)\n        temp_p = temp_dummy\n        curr = leftmost\n        while curr:\n            if curr.left: temp_p.next = curr.left; break\n            if curr.right: temp_p.next = curr.right; break\n            curr = curr.next\n        leftmost = temp_dummy.next\n    return \" \".join(res)\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        root = build_tree(data)\n        connect(root)\n        print(serialize(root))\n    else:\n        print(\"\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\nusing namespace std;\nstruct Node {int val; Node *left, *right, *next; Node(int x) : val(x), left(NULL), right(NULL), next(NULL) {}};\nNode* connect(Node* root) { return root; }\nvoid serialize(Node* root) {\n    if(!root){ cout << endl; return; }\n    vector<string> res; Node* leftmost = root;\n    while(leftmost) { Node* c = leftmost; while(c) { res.push_back(to_string(c->val)); c = c->next; } res.push_back(\"#\");\n    Node* dummy = new Node(0); Node* temp = leftmost; while(temp){if(temp->left){dummy->next=temp->left;break;}if(temp->right){dummy->next=temp->right;break;}temp=temp->next;}\n    leftmost=dummy->next; delete dummy; }\n    for(int i=0;i<(int)res.size();i++) cout<<res[i]<<(i+1<(int)res.size()?\" \":\"\"); cout<<endl;\n}\nint main() {\n    string tok; queue<Node*> q; Node* root=NULL; bool first=true;\n    while(cin>>tok){ Node* n=(tok==\"null\")?NULL:new Node(stoi(tok));\n    if(first){root=n;first=false;if(root)q.push(root);}\n    else if(!q.empty()){Node* p=q.front();if(!p->left){p->left=n;if(n)q.push(n);}else{p->right=n;if(n)q.push(n);q.pop();}} }\n    connect(root); serialize(root); return 0;\n}",
        "java": "import java.util.*;\nclass Node {int val; Node left, right, next; Node(int x){val=x;}}\npublic class Main {\n    public static Node connect(Node root) { return root; }\n    public static void serialize(Node root) {\n        if(root==null) {System.out.println(); return;}\n        List<String> res=new ArrayList<>(); Node leftmost=root;\n        while(leftmost!=null){ Node c=leftmost; while(c!=null){res.add(String.valueOf(c.val));c=c.next;} res.add(\"#\"); Node dummy=new Node(0); Node temp=leftmost; while(temp!=null){if(temp.left!=null){dummy.next=temp.left;break;}if(temp.right!=null){dummy.next=temp.right;break;}temp=temp.next;} leftmost=dummy.next; }\n        System.out.println(String.join(\" \", res));\n    }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in); Queue<Node> q=new LinkedList<>(); Node root=null; boolean first=true;\n        while(sc.hasNext()){ String tok=sc.next(); Node n=tok.equals(\"null\")?null:new Node(Integer.parseInt(tok));\n        if(first){root=n;first=false;if(root!=null)q.add(root);}\n        else if(!q.isEmpty()){Node p=q.peek();if(p.left==null){p.left=n;if(n!=null)q.add(n);}else{p.right=n;if(n!=null)q.add(n);q.poll();}} }\n        connect(root); serialize(root);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction Node(v,l,r,n){this.val=v===undefined?0:v;this.left=l===undefined?null:l;this.right=r===undefined?null:r;this.next=n===undefined?null:n;}\nfunction connect(root){ return root; }\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(tokens.length>0&&tokens[0]!==''){\n  let root=null,q=[],i=0;const mk=t=>t==='null'?null:new Node(parseInt(t));\n  root=mk(tokens[i++]);if(root)q.push(root);\n  while(q.length&&i<tokens.length){let p=q[0];p.left=mk(tokens[i++]);if(p.left)q.push(p.left);if(i<tokens.length){p.right=mk(tokens[i++]);if(p.right)q.push(p.right);}q.shift();}\n  connect(root); let res=[]; let leftmost=root;\n  while(leftmost){ let c=leftmost; while(c){res.push(c.val);c=c.next;} res.push(\"#\"); let dummy=new Node(0); let temp=leftmost; while(temp){if(temp.left){dummy.next=temp.left;break;}if(temp.right){dummy.next=temp.right;break;}temp=temp.next;} leftmost=dummy.next; }\n  console.log(res.join(\" \"));\n}else{console.log(\"\");}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct Node{int val;struct Node*left,*right,*next;};\nstruct Node* connect(struct Node* root) { return root; }\nvoid serialize(struct Node* root) {\n    if(!root){printf(\"\\n\"); return;}\n    struct Node* leftmost=root; int first=1;\n    while(leftmost){ struct Node* c=leftmost; while(c){ if(!first)printf(\" \"); printf(\"%d\", c->val); first=0; c=c->next; } printf(\" #\"); struct Node* dummy = (struct Node*)malloc(sizeof(struct Node)); dummy->next=NULL; struct Node* temp=leftmost; while(temp){if(temp->left){dummy->next=temp->left;break;}if(temp->right){dummy->next=temp->right;break;}temp=temp->next;} leftmost=dummy->next; free(dummy); }\n    printf(\"\\n\");\n}\nint main(){\n  struct Node*nodes[10001];int cnt=0;char tok[20];\n  while(cnt<10001&&scanf(\"%s\",tok)==1){if(strcmp(tok,\"null\")==0)nodes[cnt++]=NULL;else{nodes[cnt]=(struct Node*)malloc(sizeof(struct Node));nodes[cnt]->val=atoi(tok);nodes[cnt]->left=nodes[cnt]->right=nodes[cnt]->next=NULL;cnt++;}}\n  if(cnt==0){printf(\"\\n\");return 0;}\n  int qi=0,ni=1;while(ni<cnt){if(nodes[qi]){nodes[qi]->left=(ni<cnt?nodes[ni++]:NULL);nodes[qi]->right=(ni<cnt?nodes[ni++]:NULL);}qi++;}\n  connect(nodes[0]); serialize(nodes[0]); return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4 5 null 7", "expected_output": "1 # 2 3 # 4 5 7 #", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "1", "expected_output": "1 #", "is_sample": False},
        {"input": "1 2 null 3", "expected_output": "1 # 2 # 3 #", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "1 # 2 # 3 #", "is_sample": False},
        {"input": "1 2 3 null 4 null 5", "expected_output": "1 # 2 3 # 4 5 #", "is_sample": False},
        {"input": "1 2 2 null 3 null 3", "expected_output": "1 # 2 2 # 3 3 #", "is_sample": False},
        # Stress cases
        {"input": "1 " + "2 null "*50, "expected_output": "1 # " + " ".join(["2"]*51 + ["#"]*51).replace("  ", " ").strip(), "is_sample": False}, # Actually not that simple serialization. I'll use a helper for stress.
        {"input": " ".join(["1"]*15), "expected_output": "1 # 1 1 # 1 1 1 1 # 1 1 1 1 1 1 1 1 #", "is_sample": False},
        {"input": "1 2 3 4 null 5 6 null null null null 7", "expected_output": "1 # 2 3 # 4 5 6 # 7 #", "is_sample": False}
    ]
    
    # Fix stress case 8
    test_cases[7] = {"input": "1 " + "2 null "*10, "expected_output": "1 # 2 # 2 # 2 # 2 # 2 # 2 # 2 # 2 # 2 # 2 #", "is_sample": False}

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
        "topics": ["Tree", "DFS", "Linked List", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/117_Populating_Next_Right_Pointers_in_Each_Node_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
