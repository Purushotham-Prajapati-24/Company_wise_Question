import json
import os

def generate_json():
    problem_id = 124
    title = "Binary Tree Maximum Path Sum"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>124. Binary Tree Maximum Path Sum</h3>
<p>A <strong>path</strong> in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at <strong>most once</strong>. Note that the path does not need to pass through the root.</p>

<p>The <strong>path sum</strong> of a path is the sum of the node's values in the path.</p>

<p>Given the <code>root</code> of a binary tree, return <em>the maximum <strong>path sum</strong> of any <strong>non-empty</strong> path</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 322px; height: 182px;" />
<pre><strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg" style="width: 432px; height: 341px;" />
<pre><strong>Input:</strong> root = [-10,9,20,null,null,15,7]
<strong>Output:</strong> 42
<strong>Explanation:</strong> The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 3 * 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree (integers or 'null')."
    output_format = "An integer representing the maximum path sum."
    
    constraints = [
        "1 <= number of nodes <= 3 * 10^4",
        "-1000 <= Node.val <= 1000."
    ]
    
    explanation = """To find the maximum path sum in a binary tree:
1. **Recursive DFS**:
   - For every node, we want to calculate the maximum "contribution" it can provide to its parent.
   - A node's contribution is its own value plus the maximum contribution from either its left child or its right child (if that contribution is positive).
   - `max_gain = node.val + max(0, left_gain, right_gain)`
2. **Global Maximum Update**:
   - At each node, we also consider the path that *turns* at this node (includes the node and both its left and right positive contributions).
   - `current_path_sum = node.val + max(0, left_gain) + max(0, right_gain)`
   - We maintain a global `max_sum` variable and update it with `current_path_sum`.
3. **Complexity**:
   - Time Complexity: O(N) because each node is visited once.
   - Space Complexity: O(H) where H is the height of the tree, due to recursion stack."""
    
    answer = """def maxPathSum(root):
    max_sum = -float('inf')
    
    def gain(node):
        nonlocal max_sum
        if not node:
            return 0
            
        # Max gain from left and right subtrees
        left_gain = max(gain(node.left), 0)
        right_gain = max(gain(node.right), 0)
        
        # Path sum if this node is the highest point (peak)
        current_peak_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_peak_sum)
        
        # Max gain this node can offer to its parent
        return node.val + max(left_gain, right_gain)
        
    gain(root)
    return max_sum"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef maxPathSum(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        root = build_tree(data)\n        print(maxPathSum(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <climits>\n#include <queue>\nusing namespace std;\nstruct TreeNode {int val;TreeNode*left,*right;TreeNode(int x):val(x),left(NULL),right(NULL){}};\nint maxPathSum(TreeNode* root) {\n    // User logic here\n    return 0;\n}\nint main() {\n    vector<string> vals; string t;\n    while(cin>>t) vals.push_back(t);\n    if(vals.empty()||vals[0]==\"null\"){cout<<0<<endl;return 0;}\n    vector<TreeNode*> nodes; nodes.push_back(new TreeNode(stoi(vals[0])));\n    queue<TreeNode*> q; q.push(nodes[0]); int i=1;\n    while(!q.empty()&&i<(int)vals.size()){\n        TreeNode*n=q.front();q.pop();\n        if(i<(int)vals.size()&&vals[i]!=\"null\"){n->left=new TreeNode(stoi(vals[i]));q.push(n->left);}i++;\n        if(i<(int)vals.size()&&vals[i]!=\"null\"){n->right=new TreeNode(stoi(vals[i]));q.push(n->right);}i++;\n    }\n    cout<<maxPathSum(nodes[0])<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    static class TreeNode{int val;TreeNode left,right;TreeNode(int x){val=x;}}\n    public static int maxPathSum(TreeNode root) {\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in);\n        List<String> vals=new ArrayList<>();\n        while(sc.hasNext()) vals.add(sc.next());\n        if(vals.isEmpty()||vals.get(0).equals(\"null\")){System.out.println(0);return;}\n        TreeNode root=new TreeNode(Integer.parseInt(vals.get(0)));\n        Queue<TreeNode> q=new LinkedList<>(); q.add(root); int i=1;\n        while(!q.isEmpty()&&i<vals.size()){\n            TreeNode n=q.poll();\n            if(i<vals.size()&&!vals.get(i).equals(\"null\")){n.left=new TreeNode(Integer.parseInt(vals.get(i)));q.add(n.left);}i++;\n            if(i<vals.size()&&!vals.get(i).equals(\"null\")){n.right=new TreeNode(Integer.parseInt(vals.get(i)));q.add(n.right);}i++;\n        }\n        System.out.println(maxPathSum(root));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(val){this.val=val;this.left=null;this.right=null;}\nfunction maxPathSum(root) {\n    // User logic here\n    return 0;\n}\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(!tokens.length||tokens[0]==='null'){console.log(0);}\nelse{\n  const root=new TreeNode(parseInt(tokens[0]));\n  const q=[root]; let i=1;\n  while(q.length&&i<tokens.length){\n    const n=q.shift();\n    if(i<tokens.length&&tokens[i]!=='null'){n.left=new TreeNode(parseInt(tokens[i]));q.push(n.left);}i++;\n    if(i<tokens.length&&tokens[i]!=='null'){n.right=new TreeNode(parseInt(tokens[i]));q.push(n.right);}i++;\n  }\n  console.log(maxPathSum(root));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <limits.h>\nstruct TreeNode{int val;struct TreeNode*left,*right;};\nstruct TreeNode* newNode(int v){struct TreeNode*n=(struct TreeNode*)malloc(sizeof(struct TreeNode));n->val=v;n->left=n->right=NULL;return n;}\nint maxPathSum(struct TreeNode* root) {\n    // User logic here\n    return 0;\n}\nint main(){\n    char tok[30]; char buf[4000][20]; int cnt=0;\n    while(scanf(\"%s\",tok)==1) {strncpy(buf[cnt++],tok,19); if(cnt>=4000)break;}\n    if(cnt==0||strcmp(buf[0],\"null\")==0){printf(\"0\\n\");return 0;}\n    struct TreeNode** nodes=(struct TreeNode**)malloc(cnt*sizeof(struct TreeNode*));\n    nodes[0]=newNode(atoi(buf[0]));\n    int qi=0,ni=1;\n    struct TreeNode* q[4000]; int qhead=0,qtail=0; q[qtail++]=nodes[0];\n    while(qhead<qtail&&ni<cnt){\n        struct TreeNode*n=q[qhead++];\n        if(ni<cnt&&strcmp(buf[ni],\"null\")!=0){n->left=newNode(atoi(buf[ni]));q[qtail++]=n->left;}ni++;\n        if(ni<cnt&&strcmp(buf[ni],\"null\")!=0){n->right=newNode(atoi(buf[ni]));q[qtail++]=n->right;}ni++;\n    }\n    printf(\"%d\\n\",maxPathSum(nodes[0]));\n    free(nodes); return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3", "expected_output": "6", "is_sample": True},
        {"input": "-10 9 20 null null 15 7", "expected_output": "42", "is_sample": True},
        {"input": "-3", "expected_output": "-3", "is_sample": False},
        {"input": "2 -1", "expected_output": "2", "is_sample": False},
        {"input": "-1 -2 -3", "expected_output": "-1", "is_sample": False},
        {"input": "1 -2 -3 1 3 -2", "expected_output": "3", "is_sample": False},
        {"input": "5 4 8 11 null 13 4 7 2 null null null 1", "expected_output": "48", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"]*1023), "expected_output": "19", "is_sample": False}, # Full tree height 10. Path root to leaf*2 = 10+9=19
        {"input": " ".join(["-1"]*1023), "expected_output": "-1", "is_sample": False},
        {"input": " ".join([str(i%100) for i in range(1000)]), "expected_output": "970", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Dynamic Programming", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/124_Binary_Tree_Maximum_Path_Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
