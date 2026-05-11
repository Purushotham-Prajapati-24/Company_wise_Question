import json
import os

def generate_json():
    problem_id = 113
    title = "Path Sum II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>113. Path Sum II</h3>
<p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <em>all <strong>root-to-leaf</strong> paths where the sum of the node values in the path equals </em><code>targetSum</code><em>. Each path should be returned as a list of the node values, not node references</em>.</p>
<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg" style="width: 500px; height: 356px;" />
<pre>
<strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>Output:</strong> [[5,4,11,2],[5,8,4,5]]
<strong>Explanation:</strong> There are two paths whose sum equals targetSum:
5 -&gt; 4 -&gt; 11 -&gt; 2 = 22
5 -&gt; 8 -&gt; 4 -&gt; 5 = 22
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" style="width: 212px; height: 181px;" />
<pre>
<strong>Input:</strong> root = [1,2,3], targetSum = 5
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> root = [1,2], targetSum = 0
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
</ul>"""

    input_format = "Line 1: space-separated level-order traversal of the tree (integers or 'null'). Line 2: An integer representing targetSum."
    output_format = "A JSON formatted list of all root-to-leaf paths that sum to targetSum."
    
    constraints = [
        "0 <= number of nodes <= 5000",
        "-1000 <= Node.val <= 1000",
        "-1000 <= targetSum <= 1000."
    ]
    
    explanation = """To find all root-to-leaf paths with a specific sum:
1. **DFS with Backtracking**:
   - Traverse the tree from root to leaf using Depth-First Search.
   - Maintain a `current_path` list to store values of nodes visited during the current recursion.
   - At each node:
     - Add the node's value to `current_path`.
     - **Base Case**: If the node is a **leaf** and `node.val` equals the remaining `targetSum`, add a copy of `current_path` to the final `results` list.
     - **Recursive Step**: Recursively call DFS on left and right children with updated `targetSum - node.val`.
     - **Backtrack**: After exploring both children, remove the current node's value from `current_path` to restore the state for the parent.
2. **Efficiency**:
   - This approach visits each node once (O(N)).
   - Backtracking ensures we don't create unnecessary copies of the path except when a valid path is found.
3. **Complexity**:
   - Time Complexity: O(N^2) in the worst case (a full tree where every path is a match, requiring O(N) to copy each O(log N) path). More typically O(N).
   - Space Complexity: O(H) where H is the height of the tree for recursion and path storage."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    res = []
    
    def dfs(node, currentSum, path):
        if not node:
            return
            
        path.append(node.val)
        
        # Check if it's a leaf
        if not node.left and not node.right:
            if node.val == currentSum:
                res.append(list(path))
        else:
            dfs(node.left, currentSum - node.val, path)
            dfs(node.right, currentSum - node.val, path)
            
        # Backtrack
        path.pop()
        
    dfs(root, targetSum, [])
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef pathSum(root, targetSum):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        tree_data = lines[0].split()\n        target = int(lines[1].strip())\n        print(json.dumps(pathSum(build_tree(tree_data), target)))\n    else:\n        print(\"[]\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <sstream>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nvector<vector<int>> pathSum(TreeNode* root, int targetSum) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line; if(!getline(cin, line)) return 0;\n    string tok; stringstream ss(line); queue<TreeNode*> q; TreeNode* root=NULL; bool first=true;\n    while(ss>>tok){ TreeNode* n=(tok==\"null\")?NULL:new TreeNode(stoi(tok));\n    if(first){root=n;first=false;if(root)q.push(root);}\n    else if(!q.empty()){TreeNode* p=q.front();if(!p->left){p->left=n;if(n)q.push(n);}else{p->right=n;if(n)q.push(n);q.pop();}} }\n    int targetSum; if(!(cin >> targetSum)) targetSum=0;\n    vector<vector<int>> res = pathSum(root, targetSum);\n    cout << \"[\";\n    for(int i=0;i<(int)res.size();i++){\n        cout << \"[\";\n        for(int j=0;j<(int)res[i].size();j++) cout << res[i][j] << (j+1<(int)res[i].size()?\", \":\"\");\n        cout << \"]\" << (i+1<(int)res.size()?\", \":\"\");\n    }\n    cout << \"]\\n\"; return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static List<List<Integer>> pathSum(TreeNode root, int targetSum) {\n        // User logic\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in);\n        if(!sc.hasNextLine()) return;\n        String[] toks = sc.nextLine().trim().split(\"\\\\s+\");\n        if(!sc.hasNextLine()) return;\n        int targetSum = Integer.parseInt(sc.nextLine().trim());\n        Queue<TreeNode> q=new LinkedList<>(); TreeNode root=null; boolean first=true;\n        if(toks.length>0 && !toks[0].isEmpty()) {\n            for(String tok : toks) {\n                TreeNode n=tok.equals(\"null\")?null:new TreeNode(Integer.parseInt(tok));\n                if(first){root=n;first=false;if(root!=null)q.add(root);}\n                else if(!q.isEmpty()){TreeNode p=q.peek();if(p.left==null){p.left=n;if(n!=null)q.add(n);}else{p.right=n;if(n!=null)q.add(n);q.poll();}}\n            }\n        }\n        List<List<Integer>> res = pathSum(root, targetSum);\n        StringBuilder sb=new StringBuilder(\"[\");\n        for(int i=0;i<res.size();i++){\n            sb.append(\"[\");\n            for(int j=0;j<res.get(i).size();j++) sb.append(res.get(i).get(j)).append(j+1<res.get(i).size() ? \", \" : \"\");\n            sb.append(\"]\").append(i+1<res.size() ? \", \" : \"\");\n        }\n        sb.append(\"]\"); System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\nfunction pathSum(root, targetSum) {\n    // User logic\n}\n\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=2){\n  const tokens=lines[0].trim().split(/\\s+/);\n  const targetSum = parseInt(lines[1].trim());\n  let root=null,q=[],i=0;const mk=t=>t==='null'?null:new TreeNode(parseInt(t));\n  if(tokens.length>0 && tokens[0]!==''){\n    root=mk(tokens[i++]);if(root)q.push(root);\n    while(q.length&&i<tokens.length){let p=q[0];p.left=mk(tokens[i++]);if(p.left)q.push(p.left);if(i<tokens.length){p.right=mk(tokens[i++]);if(p.right)q.push(p.right);}q.shift();}\n  }\n  console.log(JSON.stringify(pathSum(root, targetSum) || []).replace(/,/g, \", \"));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\n/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the arrays are returned as *returnColumnSizes array.\n * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().\n */\nint** pathSum(struct TreeNode* root, int targetSum, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n  char line1[20000], line2[200];\n  if(!fgets(line1, sizeof(line1), stdin)) return 0;\n  if(!fgets(line2, sizeof(line2), stdin)) return 0;\n  struct TreeNode*nodes[10001];int cnt=0;char* tok=strtok(line1, \" \\n\");\n  while(tok){if(strcmp(tok,\"null\")==0)nodes[cnt++]=NULL;else{nodes[cnt]=(struct TreeNode*)malloc(sizeof(struct TreeNode));nodes[cnt]->val=atoi(tok);nodes[cnt]->left=nodes[cnt]->right=NULL;cnt++;}tok=strtok(NULL, \" \\n\");}\n  int qi=0,ni=1;while(ni<cnt){if(nodes[qi]){nodes[qi]->left=(ni<cnt?nodes[ni++]:NULL);nodes[qi]->right=(ni<cnt?nodes[ni++]:NULL);}qi++;}\n  int targetSum = atoi(line2);\n  int returnSize = 0;\n  int* returnColumnSizes = NULL;\n  struct TreeNode* root = cnt>0?nodes[0]:NULL;\n  int** res = pathSum(root, targetSum, &returnSize, &returnColumnSizes);\n  printf(\"[\");\n  for(int i=0;i<returnSize;i++){\n    printf(\"[\");\n    for(int j=0;j<returnColumnSizes[i];j++) printf(\"%d%s\", res[i][j], j+1<returnColumnSizes[i]?\", \":\"\");\n    printf(\"]%s\", i+1<returnSize?\", \":\"\");\n    free(res[i]);\n  }\n  printf(\"]\\n\");\n  if(res) free(res);\n  if(returnColumnSizes) free(returnColumnSizes);\n  return 0;\n}"
    }

    def _solve(vals, target):
        if not vals or vals[0] == "null": return []
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
            
        res = []
        def dfs(n, s, p):
            if not n: return
            p.append(n.val)
            if not n.left and not n.right:
                if n.val == s: res.append(list(p))
            else:
                dfs(n.left, s - n.val, p)
                dfs(n.right, s - n.val, p)
            p.pop()
        dfs(root, target, [])
        return res

    test_cases = [
        {"input": "5 4 8 11 null 13 4 7 2 null null 5 1\n22", "expected_output": "[[5, 4, 11, 2], [5, 8, 4, 5]]", "is_sample": True},
        {"input": "1 2 3\n5", "expected_output": "[]", "is_sample": True},
        {"input": "1 2\n1", "expected_output": "[]", "is_sample": False},
        {"input": "1 2\n3", "expected_output": "[[1, 2]]", "is_sample": False},
        {"input": "1 2 2\n3", "expected_output": "[[1, 2], [1, 2]]", "is_sample": False},
        {"input": "1\n1", "expected_output": "[[1]]", "is_sample": False},
        {"input": "1 2 3\n4", "expected_output": "[[1, 3]]", "is_sample": False},
        # Stress cases
        {"input": " ".join(["0"]*15) + "\n0", "expected_output": str(_solve(["0"]*15, 0)), "is_sample": False},
        {"input": " ".join(["1"]*50) + "\n100", "expected_output": "[]", "is_sample": False},
        {"input": "1 " + "null 1 "*50 + "\n51", "expected_output": "[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Binary Tree", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-200/113_Path_Sum_II.json"
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
