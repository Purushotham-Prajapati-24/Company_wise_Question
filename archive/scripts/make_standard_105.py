import json
import os
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_json():
    problem_id = 105
    title = "Construct Binary Tree from Preorder and Inorder Traversal"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>105. Construct Binary Tree from Preorder and Inorder Traversal</h3>
<p>Given two integer arrays <code>preorder</code> and <code>inorder</code> where <code>preorder</code> is the preorder traversal of a binary tree and <code>inorder</code> is the inorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" />
<pre><strong>Input:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> preorder = [-1], inorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= preorder.length &lt;= 3000</code></li>
	<li><code>inorder.length == preorder.length</code></li>
	<li><code>-3000 &lt;= preorder[i], inorder[i] &lt;= 3000</code></li>
	<li><code>preorder</code> and <code>inorder</code> consist of <strong>unique</strong> values.</li>
	<li>Each value of <code>inorder</code> also appears in <code>preorder</code>.</li>
	<li><code>preorder</code> is <strong>guaranteed</strong> to be the preorder traversal of the tree.</li>
	<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for preorder. Line 2: space-separated integers for inorder."
    output_format = "A single line containing space-separated values representing the level-order traversal of the constructed tree."
    
    constraints = [
        "1 <= preorder.length <= 3000",
        "inorder.length == preorder.length",
        "Values are unique and in range [-3000, 3000]."
    ]
    
    explanation = """To construct a binary tree from preorder and inorder traversals:
1. **Understand Properties**:
   - The first element in `preorder` is always the `root`.
   - In `inorder`, elements to the left of the `root` value belong to the left subtree, and elements to the right belong to the right subtree.
2. **Recursive Construction**:
   - Find the index of the root in `inorder`. Let this be `idx`.
   - The left subtree has `idx` nodes.
   - Recurse for the left subtree using appropriate slices of `preorder` and `inorder`.
   - Recurse for the right subtree using the remaining slices.
3. **Optimized Search**:
   - Use a hash map to store `inorder` values and their indices for O(1) lookups.
4. **Complexity**:
   - Time Complexity: O(N) because we build each node exactly once.
   - Space Complexity: O(N) to store the hash map and recursion stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    inorder_map = {val: i for i, val in enumerate(inorder)}
    pre_iter = iter(preorder)
    
    def build(in_start, in_end):
        if in_start > in_end:
            return None
        
        val = next(pre_iter)
        root = TreeNode(val)
        idx = inorder_map[val]
        
        root.left = build(in_start, idx - 1)
        root.right = build(idx + 1, in_end)
        return root
        
    return build(0, len(inorder) - 1)"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef buildTree(preorder, inorder):\n    # User logic here\n    pass\n\ndef serialize(root):\n    if not root: return \"\"\n    res, queue = [], deque([root])\n    while queue:\n        node = queue.popleft()\n        if node:\n            res.append(str(node.val))\n            queue.append(node.left)\n            queue.append(node.right)\n        else:\n            res.append(\"null\")\n    while res and res[-1] == \"null\": res.pop()\n    return \" \".join(res)\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        preorder = list(map(int, lines[0].split()))\n        inorder = list(map(int, lines[1].split()))\n        print(serialize(buildTree(preorder, inorder)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <queue>\n#include <unordered_map>\nusing namespace std;\nstruct TreeNode {int val; TreeNode *left, *right; TreeNode(int x):val(x),left(NULL),right(NULL){}};\nTreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) { return NULL; }\nint main() {\n    string line; vector<int> pre, in;\n    if(getline(cin, line)) { stringstream ss(line); int x; while(ss>>x) pre.push_back(x); }\n    if(getline(cin, line)) { stringstream ss(line); int x; while(ss>>x) in.push_back(x); }\n    TreeNode* root = buildTree(pre, in);\n    if(!root) { cout << endl; return 0; }\n    queue<TreeNode*> q; q.push(root); vector<string> res;\n    while(!q.empty()){ TreeNode* n=q.front(); q.pop(); if(n){ res.push_back(to_string(n->val)); q.push(n->left); q.push(n->right); }else{ res.push_back(\"null\"); } }\n    while(!res.empty() && res.back()==\"null\") res.pop_back();\n    for(int i=0;i<(int)res.size();i++) cout<<res[i]<<(i+1<(int)res.size()?\" \":\"\"); cout<<endl;\n    return 0;\n}",
        "java": "import java.util.*;\nclass TreeNode {int val; TreeNode left, right; TreeNode(int x){val=x;}}\npublic class Main {\n    public static TreeNode buildTree(int[] preorder, int[] inorder) { return null; }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in);\n        if(!sc.hasNextLine()) return;\n        String[] preStr = sc.nextLine().trim().split(\"\\\\s+\");\n        if(!sc.hasNextLine()) return;\n        String[] inStr = sc.nextLine().trim().split(\"\\\\s+\");\n        if (preStr[0].isEmpty()) return;\n        int[] pre=new int[preStr.length], in=new int[inStr.length];\n        for(int i=0;i<preStr.length;i++) pre[i]=Integer.parseInt(preStr[i]);\n        for(int i=0;i<inStr.length;i++) in[i]=Integer.parseInt(inStr[i]);\n        TreeNode root = buildTree(pre, in);\n        if(root==null){ System.out.println(); return; }\n        Queue<TreeNode> q = new LinkedList<>(); q.add(root); List<String> res=new ArrayList<>();\n        while(!q.isEmpty()){ TreeNode n=q.poll(); if(n!=null){res.add(String.valueOf(n.val)); q.add(n.left); q.add(n.right);}else{res.add(\"null\");} }\n        while(!res.isEmpty() && res.get(res.size()-1).equals(\"null\")) res.remove(res.size()-1);\n        System.out.println(String.join(\" \", res));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(v,l,r){this.val=v===undefined?0:v;this.left=l===undefined?null:l;this.right=r===undefined?null:r;}\nfunction buildTree(preorder, inorder) {}\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=2){\n  const pre=lines[0].trim().split(/\\s+/).filter(x=>x).map(Number);\n  const inn=lines[1].trim().split(/\\s+/).filter(x=>x).map(Number);\n  const root=buildTree(pre, inn);\n  if(!root){console.log(\"\");}else{\n    let q=[root], res=[];\n    while(q.length){let n=q.shift();if(n){res.push(n.val);q.push(n.left, n.right);}else{res.push(\"null\");}}\n    while(res.length && res[res.length-1]===\"null\") res.pop();\n    console.log(res.join(\" \"));\n  }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct TreeNode{int val;struct TreeNode*left,*right;};\nstruct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) { return NULL; }\nint main() {\n  char line1[20000], line2[20000];\n  if(!fgets(line1, sizeof(line1), stdin)) return 0;\n  if(!fgets(line2, sizeof(line2), stdin)) return 0;\n  int pre[3000], in[3000], psz=0, isz=0;\n  char* t = strtok(line1, \" \\n\"); while(t){pre[psz++]=atoi(t); t=strtok(NULL, \" \\n\");}\n  t = strtok(line2, \" \\n\"); while(t){in[isz++]=atoi(t); t=strtok(NULL, \" \\n\");}\n  struct TreeNode* root = buildTree(pre, psz, in, isz);\n  if(!root){printf(\"\\n\"); return 0;}\n  struct TreeNode* q[10000]; int head=0, tail=0; q[tail++]=root;\n  char res[10000][10]; int rcnt=0;\n  while(head<tail){ struct TreeNode* n=q[head++]; if(n){ sprintf(res[rcnt++], \"%d\", n->val); q[tail++]=n->left; q[tail++]=n->right; }else{ strcpy(res[rcnt++], \"null\"); } }\n  while(rcnt>0 && strcmp(res[rcnt-1], \"null\")==0) rcnt--;\n  for(int i=0;i<rcnt;i++){ printf(\"%s\", res[i]); if(i+1<rcnt) printf(\" \"); }\n  printf(\"\\n\"); return 0;\n}"
    }

    test_cases = [
        {"input": "3 9 20 15 7\\n9 3 15 20 7", "expected_output": "3 9 20 null null 15 7", "is_sample": True},
        {"input": "-1\\n-1", "expected_output": "-1", "is_sample": True},
        {"input": "1 2 3\\n1 2 3", "expected_output": "1 null 2 null 3", "is_sample": False},
        {"input": "1 2 3\\n3 2 1", "expected_output": "1 2 null 3", "is_sample": False},
        {"input": "1 2 3 4\\n1 2 3 4", "expected_output": "1 null 2 null 3 null 4", "is_sample": False},
        {"input": "2 1 3\\n1 2 3", "expected_output": "2 1 3", "is_sample": False},
        {"input": "1 2 4 5 3 6 7\\n4 2 5 1 6 3 7", "expected_output": "1 2 3 4 5 6 7", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n" + " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n" + " ".join([str(i) for i in range(100, 0, -1)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100, 0, -1)]) + "\\n" + " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(preorder, inorder):
        in_map = {v: i for i, v in enumerate(inorder)}
        pi = 0
        def b(l, r):
            nonlocal pi
            if l > r: return None
            v = preorder[pi]; pi += 1
            root = TreeNode(v); idx = in_map[v]
            root.left = b(l, idx-1); root.right = b(idx+1, r)
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
        pre = list(map(int, test_cases[i]["input"].split("\\n")[0].split()))
        ino = list(map(int, test_cases[i]["input"].split("\\n")[1].split()))
        test_cases[i]["expected_output"] = _solve(pre, ino)

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

    output_path = "1-200/105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
