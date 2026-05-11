import json
import os

def generate_json():
    problem_id = 144
    title = "Binary Tree Preorder Traversal"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>144. Binary Tree Preorder Traversal</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the preorder traversal of its nodes' values</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png" style="width: 200px; height: 200px;" />
<pre><strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [1,2,3,4,5,null,8,null,null,6,7,9]
<strong>Output:</strong> [1,2,4,5,6,7,3,8,9]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 4:</strong></p>
<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree."
    output_format = "A single line containing space-separated integers representing the preorder traversal."
    
    constraints = [
        "0 <= number of nodes <= 100",
        "-100 <= Node.val <= 100."
    ]
    
    explanation = """To perform preorder traversal (Root -> Left -> Right):
1. **Iterative Approach (Stack)**:
   - Use a stack to store nodes yet to be visited.
   - Initialize the stack with the `root`.
   - While the stack is not empty:
     - Pop a node and add its value to the result.
     - Push the **right** child to the stack (if it exists).
     - Push the **left** child to the stack (if it exists).
   - We push the right child first so that the left child is popped and processed first (LIFO property).
2. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(H) where H is the height of the tree (for the stack)."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if not root:
        return []
        
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right then left (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return result"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef preorderTraversal(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        res = preorderTraversal(build_tree(data))\n        print(\" \".join(map(str, res)))\n    else:\n        print(\"\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <stack>\n#include <queue>\n#include <string>\n#include <sstream>\nusing namespace std;\nstruct TreeNode{int val;TreeNode*left,*right;TreeNode(int x):val(x),left(NULL),right(NULL){}};\nvector<int> preorderTraversal(TreeNode* root){\n    // User logic here\n    return {};\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    istringstream ss(line); vector<string> tokens; string t;\n    while(ss>>t) tokens.push_back(t);\n    if(tokens.empty()){return 0;}\n    // BFS build\n    TreeNode* root=new TreeNode(stoi(tokens[0]));\n    queue<TreeNode*> q; q.push(root); int i=1;\n    while(!q.empty()&&i<(int)tokens.size()){\n        TreeNode*nd=q.front();q.pop();\n        if(i<(int)tokens.size()&&tokens[i]!=\"null\"){nd->left=new TreeNode(stoi(tokens[i]));q.push(nd->left);}i++;\n        if(i<(int)tokens.size()&&tokens[i]!=\"null\"){nd->right=new TreeNode(stoi(tokens[i]));q.push(nd->right);}i++;\n    }\n    vector<int> res=preorderTraversal(root);\n    for(int k=0;k<(int)res.size();k++){if(k)cout<<\" \";cout<<res[k];}\n    cout<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    static class TreeNode{int val;TreeNode left,right;TreeNode(int x){val=x;}}\n    public static List<Integer> preorderTraversal(TreeNode root){\n        // User logic here\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine();\n        if(line==null||line.trim().isEmpty()) return;\n        String[] tokens=line.trim().split(\"\\\\s+\");\n        TreeNode root=new TreeNode(Integer.parseInt(tokens[0]));\n        Queue<TreeNode> q=new LinkedList<>(); q.add(root); int i=1;\n        while(!q.isEmpty()&&i<tokens.length){\n            TreeNode nd=q.poll();\n            if(i<tokens.length&&!tokens[i].equals(\"null\")){nd.left=new TreeNode(Integer.parseInt(tokens[i]));q.add(nd.left);}i++;\n            if(i<tokens.length&&!tokens[i].equals(\"null\")){nd.right=new TreeNode(Integer.parseInt(tokens[i]));q.add(nd.right);}i++;\n        }\n        List<Integer> res=preorderTraversal(root);\n        StringBuilder sb=new StringBuilder();\n        for(int k=0;k<res.size();k++){if(k>0)sb.append(\" \");sb.append(res.get(k));}\n        System.out.println(sb);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(val,left,right){this.val=(val===undefined?0:val);this.left=(left===undefined?null:left);this.right=(right===undefined?null:right);}\nfunction preorderTraversal(root){\n    // User logic here\n    return [];\n}\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/).filter(Boolean);\nif(tokens.length){\n  const root=new TreeNode(parseInt(tokens[0])); const q=[root]; let i=1;\n  while(q.length&&i<tokens.length){const nd=q.shift();if(i<tokens.length&&tokens[i]!=='null'){nd.left=new TreeNode(parseInt(tokens[i]));q.push(nd.left);}i++;if(i<tokens.length&&tokens[i]!=='null'){nd.right=new TreeNode(parseInt(tokens[i]));q.push(nd.right);}i++;}\n  console.log(preorderTraversal(root).join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct TreeNode{int val;struct TreeNode*left,*right;};\nstruct TreeNode* newNode(int v){struct TreeNode*n=(struct TreeNode*)malloc(sizeof(struct TreeNode));n->val=v;n->left=n->right=NULL;return n;}\nint* preorderTraversal(struct TreeNode* root, int* returnSize){\n    // User logic here\n    *returnSize=0; return NULL;\n}\nint main(){\n    char buf[10000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    char*tokens[105]; int tcnt=0;\n    char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&tcnt<105){tokens[tcnt++]=tok;tok=strtok(NULL,\" \\t\\r\\n\");}\n    if(tcnt==0) return 0;\n    struct TreeNode*nodearr[105]={0}; int ncnt=0;\n    struct TreeNode*q[105]; int qh=0,qt=0;\n    nodearr[ncnt]=newNode(atoi(tokens[ncnt])); ncnt++;\n    q[qt++]=nodearr[0]; int i=1;\n    while(qh<qt&&i<tcnt){\n        struct TreeNode*nd=q[qh++];\n        if(i<tcnt&&strcmp(tokens[i],\"null\")!=0){nd->left=newNode(atoi(tokens[i]));q[qt++]=nd->left;}i++;\n        if(i<tcnt&&strcmp(tokens[i],\"null\")!=0){nd->right=newNode(atoi(tokens[i]));q[qt++]=nd->right;}i++;\n    }\n    int rsz=0; int*res=preorderTraversal(nodearr[0],&rsz);\n    for(int k=0;k<rsz;k++){if(k)printf(\" \");printf(\"%d\",res[k]);}\n    printf(\"\\n\"); return 0;\n}"
    }

    test_cases = [
        {"input": "1 null 2 3", "expected_output": "1 2 3", "is_sample": True},
        {"input": "1 2 3 4 5 null 8 null null 6 7 9", "expected_output": "1 2 4 5 6 7 3 8 9", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 2", "expected_output": "1 2", "is_sample": False},
        {"input": "1 null 2", "expected_output": "1 2", "is_sample": False},
        {"input": "1 2 3", "expected_output": "1 2 3", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False},
        {"input": "1 " + "2 null "*50, "expected_output": "...", "is_sample": False},
        {"input": "1 " + "null 2 "*50, "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(vals):
        from collections import deque
        if not vals: return ""
        class TN:
            def __init__(self, v): self.v = v; self.l = self.r = None
        def bt(vs):
            if not vs: return None
            r = TN(vs[0]); q = deque([r]); i = 1
            while q and i < len(vs):
                n = q.popleft()
                if i < len(vs) and vs[i] != "null": n.l = TN(vs[i]); q.append(n.l)
                i += 1
                if i < len(vs) and vs[i] != "null": n.r = TN(vs[i]); q.append(n.r)
                i += 1
            return r
        root = bt(vals)
        res = []
        def d(n):
            if not n: return
            res.append(n.v); d(n.l); d(n.r)
        d(root)
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
        "topics": ["Stack", "Tree", "DFS", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/144_Binary_Tree_Preorder_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
