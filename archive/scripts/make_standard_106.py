import json
import os
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_json():
    problem_id = 106
    title = "Construct Binary Tree from Inorder and Postorder Traversal"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>106. Construct Binary Tree from Inorder and Postorder Traversal</h3>
<p>Given two integer arrays <code>inorder</code> and <code>postorder</code> where <code>inorder</code> is the inorder traversal of a binary tree and <code>postorder</code> is the postorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" />
<pre><strong>Input:</strong> inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> inorder = [-1], postorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= inorder.length &lt;= 3000</code></li>
	<li><code>postorder.length == inorder.length</code></li>
	<li><code>-3000 &lt;= inorder[i], postorder[i] &lt;= 3000</code></li>
	<li><code>inorder</code> and <code>postorder</code> consist of <strong>unique</strong> values.</li>
	<li>Each value of <code>postorder</code> also appears in <code>inorder</code>.</li>
	<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
	<li><code>postorder</code> is <strong>guaranteed</strong> to be the postorder traversal of the tree.</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for inorder. Line 2: space-separated integers for postorder."
    output_format = "A single line containing space-separated values representing the level-order traversal of the constructed tree."
    
    constraints = [
        "1 <= inorder.length <= 3000",
        "postorder.length == inorder.length",
        "Values are unique and in range [-3000, 3000]."
    ]
    
    explanation = """To construct a binary tree from inorder and postorder traversals:
1. **Understand Properties**:
   - The *last* element in `postorder` is always the `root`.
   - In `inorder`, elements to the left of the `root` value belong to the left subtree, and elements to the right belong to the right subtree.
2. **Recursive Construction**:
   - Start from the end of `postorder`.
   - Find the index of the current root in `inorder`.
   - Build the **right** subtree first (because postorder follows Left-Right-Root, so reverse iteration visits Root-Right-Left).
   - Then build the left subtree.
3. **Optimized Search**:
   - Use a hash map to store `inorder` values and their indices for O(1) lookups.
4. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(N) to store the hash map and recursion stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    inorder_map = {val: i for i, val in enumerate(inorder)}
    post_idx = len(postorder) - 1
    
    def build(in_start, in_end):
        nonlocal post_idx
        if in_start > in_end:
            return None
        
        val = postorder[post_idx]
        post_idx -= 1
        root = TreeNode(val)
        idx = inorder_map[val]
        
        # Build RIGHT subtree first because we are traversing postorder backwards
        root.right = build(idx + 1, in_end)
        root.left = build(in_start, idx - 1)
        return root
        
    return build(0, len(inorder) - 1)"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef buildTree(inorder, postorder):\n    # User logic here\n    pass\n\ndef serialize(root):\n    if not root: return \"\"\n    res, queue = [], deque([root])\n    while queue:\n        node = queue.popleft()\n        if node:\n            res.append(str(node.val))\n            queue.append(node.left)\n            queue.append(node.right)\n        else:\n            res.append(\"null\")\n    while res and res[-1] == \"null\": res.pop()\n    return \" \".join(res)\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        inorder = list(map(int, lines[0].split()))\n        postorder = list(map(int, lines[1].split()))\n        print(serialize(buildTree(inorder, postorder)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <queue>\n#include <unordered_map>\nusing namespace std;\nstruct TreeNode {int val; TreeNode *left, *right; TreeNode(int x):val(x),left(NULL),right(NULL){}};\nTreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) { return NULL; }\nint main() {\n    string line; vector<int> in, post;\n    if(getline(cin, line)) { stringstream ss(line); int x; while(ss>>x) in.push_back(x); }\n    if(getline(cin, line)) { stringstream ss(line); int x; while(ss>>x) post.push_back(x); }\n    TreeNode* root = buildTree(in, post);\n    if(!root) { cout << endl; return 0; }\n    queue<TreeNode*> q; q.push(root); vector<string> res;\n    while(!q.empty()){ TreeNode* n=q.front(); q.pop(); if(n){ res.push_back(to_string(n->val)); q.push(n->left); q.push(n->right); }else{ res.push_back(\"null\"); } }\n    while(!res.empty() && res.back()==\"null\") res.pop_back();\n    for(int i=0;i<(int)res.size();i++) cout<<res[i]<<(i+1<(int)res.size()?\" \":\"\"); cout<<endl;\n    return 0;\n}",
        "java": "import java.util.*;\nclass TreeNode {int val; TreeNode left, right; TreeNode(int x){val=x;}}\npublic class Main {\n    public static TreeNode buildTree(int[] inorder, int[] postorder) { return null; }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in);\n        if(!sc.hasNextLine()) return;\n        String[] inStr = sc.nextLine().trim().split(\"\\\\s+\");\n        if(!sc.hasNextLine()) return;\n        String[] postStr = sc.nextLine().trim().split(\"\\\\s+\");\n        if (inStr[0].isEmpty()) return;\n        int[] in=new int[inStr.length], post=new int[postStr.length];\n        for(int i=0;i<inStr.length;i++) in[i]=Integer.parseInt(inStr[i]);\n        for(int i=0;i<postStr.length;i++) post[i]=Integer.parseInt(postStr[i]);\n        TreeNode root = buildTree(in, post);\n        if(root==null){ System.out.println(); return; }\n        Queue<TreeNode> q = new LinkedList<>(); q.add(root); List<String> res=new ArrayList<>();\n        while(!q.isEmpty()){ TreeNode n=q.poll(); if(n!=null){res.add(String.valueOf(n.val)); q.add(n.left); q.add(n.right);}else{res.add(\"null\");} }\n        while(!res.isEmpty() && res.get(res.size()-1).equals(\"null\")) res.remove(res.size()-1);\n        System.out.println(String.join(\" \", res));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(v,l,r){this.val=v===undefined?0:v;this.left=l===undefined?null:l;this.right=r===undefined?null:r;}\nfunction buildTree(inorder, postorder) {}\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=2){\n  const inn=lines[0].trim().split(/\\s+/).filter(x=>x).map(Number);\n  const pos=lines[1].trim().split(/\\s+/).filter(x=>x).map(Number);\n  const root=buildTree(inn, pos);\n  if(!root){console.log(\"\");}else{\n    let q=[root], res=[];\n    while(q.length){let n=q.shift();if(n){res.push(n.val);q.push(n.left, n.right);}else{res.push(\"null\");}}\n    while(res.length && res[res.length-1]===\"null\") res.pop();\n    console.log(res.join(\" \"));\n  }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct TreeNode{int val;struct TreeNode*left,*right;};\nstruct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) { return NULL; }\nint main() {\n  char line1[20000], line2[20000];\n  if(!fgets(line1, sizeof(line1), stdin)) return 0;\n  if(!fgets(line2, sizeof(line2), stdin)) return 0;\n  int in[3000], post[3000], isz=0, psz=0;\n  char* t = strtok(line1, \" \\n\"); while(t){in[isz++]=atoi(t); t=strtok(NULL, \" \\n\");}\n  t = strtok(line2, \" \\n\"); while(t){post[psz++]=atoi(t); t=strtok(NULL, \" \\n\");}\n  struct TreeNode* root = buildTree(in, isz, post, psz);\n  if(!root){printf(\"\\n\"); return 0;}\n  struct TreeNode* q[10000]; int head=0, tail=0; q[tail++]=root;\n  char res[10000][10]; int rcnt=0;\n  while(head<tail){ struct TreeNode* n=q[head++]; if(n){ sprintf(res[rcnt++], \"%d\", n->val); q[tail++]=n->left; q[tail++]=n->right; }else{ strcpy(res[rcnt++], \"null\"); } }\n  while(rcnt>0 && strcmp(res[rcnt-1], \"null\")==0) rcnt--;\n  for(int i=0;i<rcnt;i++){ printf(\"%s\", res[i]); if(i+1<rcnt) printf(\" \"); }\n  printf(\"\\n\"); return 0;\n}"
    }

    test_cases = [
        {"input": "9 3 15 20 7\\n9 15 7 20 3", "expected_output": "3 9 20 null null 15 7", "is_sample": True},
        {"input": "-1\\n-1", "expected_output": "-1", "is_sample": True},
        {"input": "1 2 3\\n3 2 1", "expected_output": "1 null 2 null 3", "is_sample": False},
        {"input": "3 2 1\\n3 2 1", "expected_output": "1 2 null 3", "is_sample": False},
        {"input": "1 2 3 4\\n4 3 2 1", "expected_output": "1 null 2 null 3 null 4", "is_sample": False},
        {"input": "1 2 3\\n1 3 2", "expected_output": "2 1 3", "is_sample": False},
        {"input": "4 2 5 1 6 3 7\\n4 5 2 6 7 3 1", "expected_output": "1 2 3 4 5 6 7", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n" + " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n" + " ".join([str(i) for i in range(100, 0, -1)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100, 0, -1)]) + "\\n" + " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False}
    ]

    def _solve(inorder, postorder):
        in_map = {v: i for i, v in enumerate(inorder)}
        pi = len(postorder)-1
        from collections import deque
        def b(l, r):
            nonlocal pi
            if l > r: return None
            v = postorder[pi]; pi -= 1
            root = TreeNode(v); idx = in_map[v]
            root.right = b(idx+1, r); root.left = b(l, idx-1)
            return root
        root = b(0, len(inorder)-1)
        if not root: return ""
        res, q = [], deque([root])
        while q:
            n = q.popleft()
            if n: res.append(str(n.val)); q.append(n.left); q.append(n.right)
            else: res.append("null")
        while res and res[-1] == "null": res.pop()
        return " ".join(res)

    for i in range(7, 10):
        ino = list(map(int, test_cases[i]["input"].split("\\n")[0].split()))
        post = list(map(int, test_cases[i]["input"].split("\\n")[1].split()))
        test_cases[i]["expected_output"] = _solve(ino, post)

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
        "topics": ["Tree", "DFS", "Array", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/106_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
