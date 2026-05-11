import json
import os

def generate_json():
    problem_id = 104
    title = "Maximum Depth of Binary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>104. Maximum Depth of Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, return <em>its maximum depth</em>.</p>

<p>A binary tree's <strong>maximum depth</strong>&nbsp;is the number of nodes along the longest path from the root node down to the farthest leaf node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg" style="width: 400px; height: 277px;" />
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [1,null,2]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree (integers or 'null')."
    output_format = "An integer representing the maximum depth of the tree."
    
    constraints = [
        "0 <= number of nodes <= 10^4",
        "-100 <= Node.val <= 100."
    ]
    
    explanation = """To find the maximum depth of a binary tree:
1. **Recursive DFS**:
   - If the node is `None`, its depth is `0`.
   - Otherwise, the depth of the tree at this node is `1 + max(depth(left_child), depth(right_child))`.
2. **Iterative BFS (Alternative)**:
   - Use a level-order traversal and count the number of levels.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes, as we visit each node once.
   - Space Complexity: O(H) where H is the height of the tree, for the recursion stack."""
    
    answer = """def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef maxDepth(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(maxDepth(build_tree(data)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <queue>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nint maxDepth(TreeNode* root) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string tok; queue<TreeNode*> q; TreeNode* root=NULL; bool first=true;\n    while(cin>>tok){ TreeNode* n=(tok==\"null\")?NULL:new TreeNode(stoi(tok));\n    if(first){root=n;first=false;if(root)q.push(root);}\n    else if(!q.empty()){TreeNode* p=q.front();if(!p->left){p->left=n;if(n)q.push(n);}else{p->right=n;if(n)q.push(n);q.pop();}} }\n    cout<<maxDepth(root)<<endl; return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static int maxDepth(TreeNode root) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in); Queue<TreeNode> q=new LinkedList<>(); TreeNode root=null; boolean first=true;\n        while(sc.hasNext()){ String tok=sc.next(); TreeNode n=tok.equals(\"null\")?null:new TreeNode(Integer.parseInt(tok));\n        if(first){root=n;first=false;if(root!=null)q.add(root);}\n        else if(!q.isEmpty()){TreeNode p=q.peek();if(p.left==null){p.left=n;if(n!=null)q.add(n);}else{p.right=n;if(n!=null)q.add(n);q.poll();}} }\n        System.out.println(maxDepth(root));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(v,l,r){this.val=v===undefined?0:v;this.left=l===undefined?null:l;this.right=r===undefined?null:r;}\nfunction maxDepth(root){ return 0; }\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(tokens.length>0&&tokens[0]!==''){\n  let root=null,q=[],i=0;const mk=t=>t==='null'?null:new TreeNode(parseInt(t));\n  root=mk(tokens[i++]);if(root)q.push(root);\n  while(q.length&&i<tokens.length){let p=q[0];p.left=mk(tokens[i++]);if(p.left)q.push(p.left);if(i<tokens.length){p.right=mk(tokens[i++]);if(p.right)q.push(p.right);}q.shift();}\n  console.log(maxDepth(root));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct TreeNode{int val;struct TreeNode*left,*right;};\nint maxDepth(struct TreeNode*root){return 0;}\nint main(){\n  struct TreeNode*nodes[10001];int cnt=0;char tok[20];\n  while(cnt<10001&&scanf(\"%s\",tok)==1){if(strcmp(tok,\"null\")==0)nodes[cnt++]=NULL;else{nodes[cnt]=(struct TreeNode*)malloc(sizeof(struct TreeNode));nodes[cnt]->val=atoi(tok);nodes[cnt]->left=nodes[cnt]->right=NULL;cnt++;}}\n  if(cnt==0){printf(\"0\\n\");return 0;}\n  int qi=0,ni=1;while(ni<cnt){if(nodes[qi]){nodes[qi]->left=(ni<cnt?nodes[ni++]:NULL);nodes[qi]->right=(ni<cnt?nodes[ni++]:NULL);}qi++;}\n  printf(\"%d\\n\",maxDepth(nodes[0]));return 0;\n}"
    }

    test_cases = [
        {"input": "3 9 20 null null 15 7", "expected_output": "3", "is_sample": True},
        {"input": "1 null 2", "expected_output": "2", "is_sample": True},
        {"input": "", "expected_output": "0", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "3", "is_sample": False},
        {"input": "1 null 2 null 3 null 4", "expected_output": "4", "is_sample": False},
        {"input": "1 2 null 3 null 4", "expected_output": "4", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 1025)]), "expected_output": "10", "is_sample": False},
        {"input": " ".join(["1"] + ["null", "2"]*1000), "expected_output": "1001", "is_sample": False},
        {"input": " ".join(["1"] + ["2", "null"]*1000), "expected_output": "1001", "is_sample": False}
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

    output_path = "1-200/104_Maximum_Depth_of_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
