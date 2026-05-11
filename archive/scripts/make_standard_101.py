import json
import os

def generate_json():
    problem_id = 101
    title = "Symmetric Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>101. Symmetric Tree</h3>
<p>Given the <code>root</code> of a binary tree, <em>check whether it is a mirror of itself</em> (i.e., symmetric around its center).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg" style="width: 354px; height: 291px;" />
<pre><strong>Input:</strong> root = [1,2,2,3,4,4,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg" style="width: 308px; height: 258px;" />
<pre><strong>Input:</strong> root = [1,2,2,null,3,null,3]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it both recursively and iteratively?"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree (integers or 'null')."
    output_format = "true if the tree is symmetric, false otherwise."
    
    constraints = [
        "1 <= number of nodes <= 1000",
        "-100 <= Node.val <= 100."
    ]
    
    explanation = """To check if a binary tree is symmetric:
1. **Mirror Property**: A tree is symmetric if and only if its left subtree and right subtree are mirrors of each other.
2. **Recursive Comparison**:
   - Compare two nodes `L` and `R`.
   - Both must be null OR both must be non-null with equal values.
   - If they match, recursively check:
     - `L.left` with `R.right` (outer children).
     - `L.right` with `R.left` (inner children).
3. **Complexity**:
   - Time Complexity: O(N) as we visit every node once.
   - Space Complexity: O(H) where H is the height of the tree, due to the recursion stack."""
    
    answer = """def isSymmetric(root):
    if not root:
        return True
        
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
            
        return (t1.val == t2.val and 
                isMirror(t1.left, t2.right) and 
                isMirror(t1.right, t2.left))
                
    return isMirror(root.left, root.right)"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef isSymmetric(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(str(isSymmetric(build_tree(data))).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <queue>\nusing namespace std;\nstruct TreeNode { int val; TreeNode *left, *right; TreeNode(int x):val(x),left(NULL),right(NULL){} };\nbool isSymmetric(TreeNode* root) { return true; }\nint main() {\n    string tok; queue<TreeNode*> q; TreeNode* root=NULL; bool first=true;\n    while(cin>>tok){ TreeNode* n=(tok==\"null\")?NULL:new TreeNode(stoi(tok));\n    if(first){root=n;first=false;if(root)q.push(root);}\n    else if(!q.empty()){TreeNode* p=q.front();if(!p->left){p->left=n;if(n)q.push(n);}else{p->right=n;if(n)q.push(n);q.pop();}} }\n    cout<<(isSymmetric(root)?\"true\":\"false\")<<endl; return 0;\n}",
        "java": "import java.util.*;\nclass TreeNode { int val; TreeNode left,right; TreeNode(int x){val=x;} }\npublic class Main {\n    public static boolean isSymmetric(TreeNode root) { return true; }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in); Queue<TreeNode> q=new LinkedList<>(); TreeNode root=null; boolean first=true;\n        while(sc.hasNext()){ String tok=sc.next(); TreeNode n=tok.equals(\"null\")?null:new TreeNode(Integer.parseInt(tok));\n        if(first){root=n;first=false;if(root!=null)q.add(root);}\n        else if(!q.isEmpty()){TreeNode p=q.peek();if(p.left==null){p.left=n;if(n!=null)q.add(n);}else{p.right=n;if(n!=null)q.add(n);q.poll();}} }\n        System.out.println(isSymmetric(root)?\"true\":\"false\");\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(v,l,r){this.val=v===undefined?0:v;this.left=l===undefined?null:l;this.right=r===undefined?null:r;}\nfunction isSymmetric(root){}\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(tokens.length>0&&tokens[0]!==''){\n  let root=null,q=[],i=0;const mk=t=>t==='null'?null:new TreeNode(parseInt(t));\n  root=mk(tokens[i++]);if(root)q.push(root);\n  while(q.length&&i<tokens.length){let p=q[0];p.left=mk(tokens[i++]);if(p.left)q.push(p.left);if(i<tokens.length){p.right=mk(tokens[i++]);if(p.right)q.push(p.right);}q.shift();}\n  console.log(String(isSymmetric(root)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\nstruct TreeNode{int val;struct TreeNode*left,*right;};\nbool isSymmetric(struct TreeNode*root){return true;}\nint main(){\n  struct TreeNode*nodes[1001];int cnt=0;char tok[20];\n  while(cnt<1001&&scanf(\"%s\",tok)==1){if(strcmp(tok,\"null\")==0)nodes[cnt++]=NULL;else{nodes[cnt]=(struct TreeNode*)malloc(sizeof(struct TreeNode));nodes[cnt]->val=atoi(tok);nodes[cnt]->left=nodes[cnt]->right=NULL;cnt++;}}\n  if(cnt==0){printf(\"true\\n\");return 0;}\n  int qi=0,ni=1;while(ni<cnt){if(nodes[qi]){nodes[qi]->left=(ni<cnt?nodes[ni++]:NULL);nodes[qi]->right=(ni<cnt?nodes[ni++]:NULL);}qi++;}\n  printf(\"%s\\n\",isSymmetric(nodes[0])?\"true\":\"false\");return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 2 3 4 4 3", "expected_output": "true", "is_sample": True},
        {"input": "1 2 2 null 3 null 3", "expected_output": "false", "is_sample": True},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "1 2 2 2 null null 2", "expected_output": "true", "is_sample": False},
        {"input": "1 2 2 null 3 3", "expected_output": "true", "is_sample": False},
        {"input": "1 2 3", "expected_output": "false", "is_sample": False},
        {"input": "1 2 2 2 null 2 null", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": "1 " + "2 2 "*50, "expected_output": "true", "is_sample": False},
        {"input": " ".join(["1"]*1023), "expected_output": "true", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100)]), "expected_output": "false", "is_sample": False}
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
        "topics": ["Tree", "DFS", "BFS", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/101_Symmetric_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
