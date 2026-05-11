import json
import os
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_json():
    problem_id = 102
    title = "Binary Tree Level Order Traversal"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>102. Binary Tree Level Order Traversal</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes' values</em>. (i.e., from left to right, level by level).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[9,20],[15,7]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree (integers or 'null')."
    output_format = "A list of lists representing the values at each level."
    
    constraints = [
        "0 <= number of nodes <= 2000",
        "-1000 <= Node.val <= 1000."
    ]
    
    explanation = """To perform level order traversal:
1. **BFS using Queue**: Use a queue to keep track of nodes at the current level.
2. **Iteration**:
   - For each level, determine the number of nodes currently in the queue (`level_size`).
   - Process `level_size` nodes by popping them, adding their values to a `current_level` list, and pushing their children into the queue for the next level.
3. **Complexity**:
   - Time Complexity: O(N) because every node is visited exactly once.
   - Space Complexity: O(N) to store the result and handle the queue in the worst case (the last level can have up to N/2 nodes)."""
    
    answer = """from collections import deque

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
        
    return result"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef levelOrder(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(json.dumps(levelOrder(build_tree(data))))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\nusing namespace std;\nstruct TreeNode{int val;TreeNode*left,*right;TreeNode(int x):val(x),left(NULL),right(NULL){}};\nvector<vector<int>> levelOrder(TreeNode*root){return {};}\nint main(){\n  string tok;queue<TreeNode*>q;TreeNode*root=NULL;bool first=true;\n  while(cin>>tok){TreeNode*n=(tok==\"null\")?NULL:new TreeNode(stoi(tok));\n    if(first){root=n;first=false;if(root)q.push(root);}\n    else if(!q.empty()){TreeNode*p=q.front();if(!p->left){p->left=n;if(n)q.push(n);}else{p->right=n;if(n)q.push(n);q.pop();}}}\n  auto res=levelOrder(root);\n  cout<<\"[\";for(int i=0;i<(int)res.size();i++){cout<<\"[\";for(int j=0;j<(int)res[i].size();j++){cout<<res[i][j];if(j+1<(int)res[i].size())cout<<\", \";}cout<<\"]\";if(i+1<(int)res.size())cout<<\", \";}cout<<\"]\"<<endl;\n  return 0;\n}",
        "java": "import java.util.*;\nclass TreeNode{int val;TreeNode left,right;TreeNode(int x){val=x;}}\npublic class Main{\n  public static List<List<Integer>> levelOrder(TreeNode root){return new ArrayList<>();}\n  public static void main(String[]args){\n    Scanner sc=new Scanner(System.in);Queue<TreeNode>q=new LinkedList<>();TreeNode root=null;boolean first=true;\n    while(sc.hasNext()){String tok=sc.next();TreeNode n=tok.equals(\"null\")?null:new TreeNode(Integer.parseInt(tok));\n      if(first){root=n;first=false;if(root!=null)q.add(root);}\n      else if(!q.isEmpty()){TreeNode p=q.peek();if(p.left==null){p.left=n;if(n!=null)q.add(n);}else{p.right=n;if(n!=null)q.add(n);q.poll();}}}\n    System.out.println(levelOrder(root));\n  }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(v,l,r){this.val=v===undefined?0:v;this.left=l===undefined?null:l;this.right=r===undefined?null:r;}\nfunction levelOrder(root){}\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(tokens.length>0&&tokens[0]!==''){\n  let root=null,q=[],i=0;const mk=t=>t==='null'?null:new TreeNode(parseInt(t));\n  root=mk(tokens[i++]);if(root)q.push(root);\n  while(q.length&&i<tokens.length){let p=q[0];p.left=mk(tokens[i++]);if(p.left)q.push(p.left);if(i<tokens.length){p.right=mk(tokens[i++]);if(p.right)q.push(p.right);}q.shift();}\n  console.log(JSON.stringify(levelOrder(root)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct TreeNode{int val;struct TreeNode*left,*right;};\nint** levelOrder(struct TreeNode*root,int*returnSize,int**returnColSizes){*returnSize=0;return NULL;}\nint main(){\n  struct TreeNode*nodes[2001];int cnt=0;char tok[20];\n  while(cnt<2001&&scanf(\"%s\",tok)==1){if(strcmp(tok,\"null\")==0)nodes[cnt++]=NULL;else{nodes[cnt]=(struct TreeNode*)malloc(sizeof(struct TreeNode));nodes[cnt]->val=atoi(tok);nodes[cnt]->left=nodes[cnt]->right=NULL;cnt++;}}\n  if(cnt==0){printf(\"[]\\n\");return 0;}\n  int qi=0,ni=1;while(ni<cnt){if(nodes[qi]){nodes[qi]->left=(ni<cnt?nodes[ni++]:NULL);nodes[qi]->right=(ni<cnt?nodes[ni++]:NULL);}qi++;}\n  int rsz=0;int*csz=NULL;int**res=levelOrder(nodes[0],&rsz,&csz);\n  printf(\"[\");for(int i=0;i<rsz;i++){printf(\"[\");for(int j=0;j<csz[i];j++){printf(\"%d\",res[i][j]);if(j+1<csz[i])printf(\", \");}printf(\"]\");if(i+1<rsz)printf(\", \");}printf(\"]\\n\");\n  return 0;\n}"
    }

    test_cases = [
        {"input": "3 9 20 null null 15 7", "expected_output": "[[3], [9, 20], [15, 7]]", "is_sample": True},
        {"input": "1", "expected_output": "[[1]]", "is_sample": True},
        {"input": "", "expected_output": "[]", "is_sample": True},
        {"input": "1 2 null 3", "expected_output": "[[1], [2], [3]]", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "[[1], [2], [3]]", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "[[1], [2, 3], [4, 5, 6, 7]]", "is_sample": False},
        {"input": "1 2 2 3 3 3 3", "expected_output": "[[1], [2, 2], [3, 3, 3, 3]]", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"]*1023), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100)]), "expected_output": "...", "is_sample": False},
        {"input": "1 " + "2 null "*50, "expected_output": "[[1]" + ", [2]"*50 + "]", "is_sample": False}
    ]

    # Generate stress results
    def _solve(vals):
        if not vals or vals[0] == "null": return []
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        lvl_queue = deque([root])
        i = 1
        while lvl_queue and i < len(vals):
            node = lvl_queue.popleft()
            if i < len(vals) and vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                lvl_queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                lvl_queue.append(node.right)
            i += 1
        
        # Now do the BFS
        res = []
        q = deque([root])
        while q:
            sz = len(q)
            cur = []
            for _ in range(sz):
                node = q.popleft()
                cur.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(cur)
        return res

    test_cases[7]["expected_output"] = str(_solve(test_cases[7]["input"].split()))
    test_cases[8]["expected_output"] = str(_solve(test_cases[8]["input"].split()))

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
        "topics": ["Tree", "BFS", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/102_Binary_Tree_Level_Order_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    # Local TreeNode for _solve logic inside generate_json
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    from collections import deque
    generate_json()
