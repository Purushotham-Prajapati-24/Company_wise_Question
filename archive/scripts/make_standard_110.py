import json
import os

def generate_json():
    problem_id = 110
    title = "Balanced Binary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>110. Balanced Binary Tree</h3>
<p>Given a binary tree, determine if it is <strong>height-balanced</strong>.</p>

<p>A <strong>height-balanced</strong> binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;" />
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;" />
<pre><strong>Input:</strong> root = [1,2,2,3,3,null,null,4,4]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree (integers or 'null')."
    output_format = "true if the tree is height-balanced, false otherwise."
    
    constraints = [
        "0 <= number of nodes <= 5000",
        "-10^4 <= Node.val <= 10^4."
    ]
    
    explanation = """To determine if a binary tree is height-balanced:
1. **Definition**: For every node, the difference in height between its left and right subtrees `abs(height(left) - height(right))` must be `<= 1`.
2. **Optimized Bottom-Up DFS**:
   - Instead of checking the height of subtrees repeatedly (which would be O(N^2)), we can return the height from a helper function.
   - If a subtree is unbalanced, the helper returns `-1`.
   - If both subtrees are balanced and their height difference is `<= 1`, return the calculated height: `1 + max(left_height, right_height)`.
   - Otherwise, return `-1`.
3. **Complexity**:
   - Time Complexity: O(N) because each node is visited once.
   - Space Complexity: O(H) where H is the height of the tree, for the recursion stack."""
    
    answer = """def isBalanced(root):
    def checkHeight(node):
        if not node:
            return 0
        
        left_h = checkHeight(node.left)
        if left_h == -1: return -1
        
        right_h = checkHeight(node.right)
        if right_h == -1: return -1
        
        if abs(left_h - right_h) > 1:
            return -1
            
        return 1 + max(left_h, right_h)
        
    return checkHeight(root) != -1"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef isBalanced(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(str(isBalanced(build_tree(data))).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <queue>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nbool isBalanced(TreeNode* root) {\n    // User logic\n    return true;\n}\n\nint main() {\n    string tok; queue<TreeNode*> q; TreeNode* root=NULL; bool first=true;\n    while(cin>>tok){ TreeNode* n=(tok==\"null\")?NULL:new TreeNode(stoi(tok));\n    if(first){root=n;first=false;if(root)q.push(root);}\n    else if(!q.empty()){TreeNode* p=q.front();if(!p->left){p->left=n;if(n)q.push(n);}else{p->right=n;if(n)q.push(n);q.pop();}} }\n    cout<<(isBalanced(root)?\"true\":\"false\")<<endl; return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static boolean isBalanced(TreeNode root) {\n        // User logic\n        return true;\n    }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in); Queue<TreeNode> q=new LinkedList<>(); TreeNode root=null; boolean first=true;\n        while(sc.hasNext()){ String tok=sc.next(); TreeNode n=tok.equals(\"null\")?null:new TreeNode(Integer.parseInt(tok));\n        if(first){root=n;first=false;if(root!=null)q.add(root);}\n        else if(!q.isEmpty()){TreeNode p=q.peek();if(p.left==null){p.left=n;if(n!=null)q.add(n);}else{p.right=n;if(n!=null)q.add(n);q.poll();}} }\n        System.out.println(isBalanced(root)?\"true\":\"false\");\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(v,l,r){this.val=v===undefined?0:v;this.left=l===undefined?null:l;this.right=r===undefined?null:r;}\nfunction isBalanced(root) { return true; }\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(tokens.length>0&&tokens[0]!==''){\n  let root=null,q=[],i=0;const mk=t=>t==='null'?null:new TreeNode(parseInt(t));\n  root=mk(tokens[i++]);if(root)q.push(root);\n  while(q.length&&i<tokens.length){let p=q[0];p.left=mk(tokens[i++]);if(p.left)q.push(p.left);if(i<tokens.length){p.right=mk(tokens[i++]);if(p.right)q.push(p.right);}q.shift();}\n  console.log(isBalanced(root)?\"true\":\"false\");\n}",
        "c": "#include <stdbool.h>\n#include <stdlib.h>\n#include <stdio.h>\n#include <string.h>\nstruct TreeNode{int val;struct TreeNode*left,*right;};\nbool isBalanced(struct TreeNode*root){return true;}\nint main(){\n  struct TreeNode*nodes[10001];int cnt=0;char tok[20];\n  while(cnt<10001&&scanf(\"%s\",tok)==1){if(strcmp(tok,\"null\")==0)nodes[cnt++]=NULL;else{nodes[cnt]=(struct TreeNode*)malloc(sizeof(struct TreeNode));nodes[cnt]->val=atoi(tok);nodes[cnt]->left=nodes[cnt]->right=NULL;cnt++;}}\n  if(cnt==0){printf(\"true\\n\");return 0;}\n  int qi=0,ni=1;while(ni<cnt){if(nodes[qi]){nodes[qi]->left=(ni<cnt?nodes[ni++]:NULL);nodes[qi]->right=(ni<cnt?nodes[ni++]:NULL);}qi++;}\n  printf(\"%s\\n\",isBalanced(nodes[0])?\"true\":\"false\");return 0;\n}"
    }

    test_cases = [
        {"input": "3 9 20 null null 15 7", "expected_output": "true", "is_sample": True},
        {"input": "1 2 2 3 3 null null 4 4", "expected_output": "false", "is_sample": True},
        {"input": "", "expected_output": "true", "is_sample": False},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "1 2 null 3", "expected_output": "false", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "false", "is_sample": False},
        {"input": "1 2 2 3 null null 3 4 null null 4", "expected_output": "false", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 1025)]), "expected_output": "true", "is_sample": False},
        {"input": "1 " + "2 null "*50, "expected_output": "false", "is_sample": False},
        {"input": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", "expected_output": "true", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/110_Balanced_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
