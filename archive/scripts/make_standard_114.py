import json
import os

def generate_json():
    problem_id = 114
    title = "Flatten Binary Tree to Linked List"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>114. Flatten Binary Tree to Linked List</h3>
<p>Given the <code>root</code> of a binary tree, flatten the tree into a "linked list":</p>

<ul>
	<li>The "linked list" should use the same <code>TreeNode</code> class where the <code>right</code> child pointer points to the next node in the list and the <code>left</code> child pointer is always <code>null</code>.</li>
	<li>The "linked list" should be in the same order as a <a href="http://en.wikipedia.org/wiki/Tree_traversal#Pre-order" target="_blank"><strong>pre-order</strong><strong> traversal</strong></a> of the binary tree.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" style="width: 500px; height: 226px;" />
<pre>
<strong>Input:</strong> root = [1,2,5,3,4,null,6]
<strong>Output:</strong> [1,null,2,null,3,null,4,null,5,null,6]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Can you flatten the tree in-place (with <code>O(1)</code> extra space)? """

    input_format = "A single line containing space-separated values representing the level-order traversal of the tree (integers or 'null')."
    output_format = "A single line containing space-separated values representing the level-order traversal of the flattened tree (linked list structure)."
    
    constraints = [
        "0 <= number of nodes <= 2000",
        "-100 <= Node.val <= 100."
    ]
    
    explanation = """To flatten a binary tree into a linked list in-place:
1. **Iterative In-place Approach (O(1) space)**:
   - For each node `curr` starting from the root:
     - If `curr.left` exists:
       - Find the **rightmost** node in the left subtree. This node is the inorder predecessor of `curr.right` in a preorder traversal.
       - Connect the rightmost node's `right` pointer to `curr.right`.
       - Move the entire left subtree to the right: `curr.right = curr.left`.
       - Set `curr.left = null`.
     - Move to the next node on the right: `curr = curr.right`.
2. **Why this works**:
   - In a preorder traversal (Root -> Left -> Right), the entire left subtree comes before the right subtree.
   - By attaching the right subtree to the end of the left subtree, we maintain the correct preorder sequence while linearizing the tree.
3. **Complexity**:
   - Time Complexity: O(N) because each node is visited at most twice.
   - Space Complexity: O(1) as we reuse existing pointers and don't use a recursion stack or extra data structures."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    curr = root
    while curr:
        if curr.left:
            # Find the rightmost node in the left subtree
            predecessor = curr.left
            while predecessor.right:
                predecessor = predecessor.right
            
            # Connect the original right subtree to the predecessor
            predecessor.right = curr.right
            
            # Move left subtree to the right
            curr.right = curr.left
            curr.left = None
            
        # Move to the next node
        curr = curr.right"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef flatten(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef level_order(root):\n    if not root: return \"\"\n    res = []\n    queue = deque([root])\n    while queue:\n        node = queue.popleft()\n        if node:\n            res.append(str(node.val))\n            queue.append(node.left)\n            queue.append(node.right)\n        else:\n            res.append(\"null\")\n    while res and res[-1] == \"null\": res.pop()\n    return \" \".join(res)\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        root = build_tree(data)\n        flatten(root)\n        print(level_order(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <sstream>\nusing namespace std;\nstruct TreeNode {int val; TreeNode *left, *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {}};\nvoid flatten(TreeNode* root) { /* User logic */ }\nvoid serialize(TreeNode* root) {\n    if(!root) return;\n    queue<TreeNode*> q; q.push(root); vector<string> res;\n    while(!q.empty()){ TreeNode* n=q.front(); q.pop(); if(n){ res.push_back(to_string(n->val)); q.push(n->left); q.push(n->right); }else{ res.push_back(\"null\"); } }\n    while(!res.empty() && res.back()==\"null\") res.pop_back();\n    for(int i=0;i<(int)res.size();i++) cout<<res[i]<<(i+1<(int)res.size()?\" \":\"\"); cout<<endl;\n}\nint main() {\n    string tok; queue<TreeNode*> q; TreeNode* root=NULL; bool first=true;\n    while(cin>>tok){ TreeNode* n=(tok==\"null\")?NULL:new TreeNode(stoi(tok));\n    if(first){root=n;first=false;if(root)q.push(root);}\n    else if(!q.empty()){TreeNode* p=q.front();if(!p->left){p->left=n;if(n)q.push(n);}else{p->right=n;if(n)q.push(n);q.pop();}} }\n    flatten(root); serialize(root); return 0;\n}",
        "java": "import java.util.*;\nclass TreeNode {int val; TreeNode left, right; TreeNode(int x){val=x;}}\npublic class Main {\n    public static void flatten(TreeNode root) { /* User logic */ }\n    public static void serialize(TreeNode root) {\n        if(root==null) {System.out.println(); return;}\n        Queue<TreeNode> q = new LinkedList<>(); q.add(root); List<String> res=new ArrayList<>();\n        while(!q.isEmpty()){ TreeNode n=q.poll(); if(n!=null){res.add(String.valueOf(n.val)); q.add(n.left); q.add(n.right);}else{res.add(\"null\");} }\n        while(!res.isEmpty() && res.get(res.size()-1).equals(\"null\")) res.remove(res.size()-1);\n        System.out.println(String.join(\" \", res));\n    }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in); Queue<TreeNode> q=new LinkedList<>(); TreeNode root=null; boolean first=true;\n        while(sc.hasNext()){ String tok=sc.next(); TreeNode n=tok.equals(\"null\")?null:new TreeNode(Integer.parseInt(tok));\n        if(first){root=n;first=false;if(root!=null)q.add(root);}\n        else if(!q.isEmpty()){TreeNode p=q.peek();if(p.left==null){p.left=n;if(n!=null)q.add(n);}else{p.right=n;if(n!=null)q.add(n);q.poll();}} }\n        flatten(root); serialize(root);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(v,l,r){this.val=v===undefined?0:v;this.left=l===undefined?null:l;this.right=r===undefined?null:r;}\nfunction flatten(root){}\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(tokens.length>0&&tokens[0]!==''){\n  let root=null,q=[],i=0;const mk=t=>t==='null'?null:new TreeNode(parseInt(t));\n  root=mk(tokens[i++]);if(root)q.push(root);\n  while(q.length&&i<tokens.length){let p=q[0];p.left=mk(tokens[i++]);if(p.left)q.push(p.left);if(i<tokens.length){p.right=mk(tokens[i++]);if(p.right)q.push(p.right);}q.shift();}\n  flatten(root);\n  q=[root]; let res=[];\n  while(q.length){let n=q.shift();if(n){res.push(n.val);q.push(n.left, n.right);}else{res.push(\"null\");}}\n  while(res.length && res[res.length-1]===\"null\") res.pop();\n  console.log(res.join(\" \"));\n}else{console.log(\"\");}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct TreeNode{int val;struct TreeNode*left,*right;};\nvoid flatten(struct TreeNode* root) { }\nvoid serialize(struct TreeNode* root) {\n    if(!root){printf(\"\\n\"); return;}\n    struct TreeNode* q[10000]; int head=0, tail=0; q[tail++]=root;\n    char res[10000][10]; int rcnt=0;\n    while(head<tail){ struct TreeNode* n=q[head++]; if(n){ sprintf(res[rcnt++], \"%d\", n->val); q[tail++]=n->left; q[tail++]=n->right; }else{ strcpy(res[rcnt++], \"null\"); } }\n    while(rcnt>0 && strcmp(res[rcnt-1], \"null\")==0) rcnt--;\n    for(int i=0;i<rcnt;i++){ printf(\"%s\", res[i]); if(i+1<rcnt) printf(\" \"); }\n    printf(\"\\n\");\n}\nint main(){\n  struct TreeNode*nodes[10001];int cnt=0;char tok[20];\n  while(cnt<10001&&scanf(\"%s\",tok)==1){if(strcmp(tok,\"null\")==0)nodes[cnt++]=NULL;else{nodes[cnt]=(struct TreeNode*)malloc(sizeof(struct TreeNode));nodes[cnt]->val=atoi(tok);nodes[cnt]->left=nodes[cnt]->right=NULL;cnt++;}}\n  if(cnt==0){printf(\"\\n\");return 0;}\n  int qi=0,ni=1;while(ni<cnt){if(nodes[qi]){nodes[qi]->left=(ni<cnt?nodes[ni++]:NULL);nodes[qi]->right=(ni<cnt?nodes[ni++]:NULL);}qi++;}\n  flatten(nodes[0]); serialize(nodes[0]); return 0;\n}"
    }

    def _solve(vals):
        if not vals or vals[0] == "null": return ""
        from collections import deque
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(vals):
            node = queue.popleft()
            if i < len(vals) and vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
            
        curr = root
        while curr:
            if curr.left:
                p = curr.left
                while p.right: p = p.right
                p.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
            
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        while res and res[-1] == "null": res.pop()
        return " ".join(res)

    test_cases = [
        {"input": "1 2 5 3 4 null 6", "expected_output": "1 null 2 null 3 null 4 null 5 null 6", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "0", "expected_output": "0", "is_sample": True},
        {"input": "1 2", "expected_output": "1 null 2", "is_sample": False},
        {"input": "1 null 2", "expected_output": "1 null 2", "is_sample": False},
        {"input": "1 2 3", "expected_output": "1 null 2 null 3", "is_sample": False},
        {"input": "1 2 2", "expected_output": "1 null 2 null 2", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(1, 11))), "expected_output": _solve(list(map(str, range(1, 11)))), "is_sample": False},
        {"input": "1 " + "2 null "*50, "expected_output": _solve(["1"] + ["2", "null"]*50), "is_sample": False},
        {"input": "1 " + "null 2 "*50, "expected_output": _solve(["1"] + ["null", "2"]*50), "is_sample": False}
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
        "topics": ["Tree", "DFS", "Linked List", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/114_Flatten_Binary_Tree_to_Linked_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

# Local TreeNode for script logic
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    generate_json()
