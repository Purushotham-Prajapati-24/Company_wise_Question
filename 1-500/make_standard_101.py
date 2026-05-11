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
        "python": """import sys
import re
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(data):
    vals = re.findall(r'null|-?\\d+', data)
    if not vals or vals[0] == 'null':
        return None
    root = TreeNode(int(vals[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] != 'null':
            node.left = TreeNode(int(vals[i]))
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] != 'null':
            node.right = TreeNode(int(vals[i]))
            queue.append(node.right)
        i += 1
    return root

def isSymmetric(root):
    # Write your logic here
    return True

if __name__ == "__main__":
    input_data = sys.stdin.read()
    if not input_data.strip():
        sys.exit(0)
    root = build_tree(input_data)
    result = isSymmetric(root)
    print(str(result).lower())
""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <regex>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* buildTree(string data) {
    regex re("null|-?\\\\d+");
    sregex_iterator it(data.begin(), data.end(), re), end;
    vector<string> vals;
    while (it != end) {
        vals.push_back(it->str());
        it++;
    }
    if (vals.empty() || vals[0] == "null") return NULL;
    TreeNode* root = new TreeNode(stoi(vals[0]));
    queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < vals.size()) {
        TreeNode* curr = q.front();
        q.pop();
        if (i < vals.size() && vals[i] != "null") {
            curr->left = new TreeNode(stoi(vals[i]));
            q.push(curr->left);
        }
        i++;
        if (i < vals.size() && vals[i] != "null") {
            curr->right = new TreeNode(stoi(vals[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

bool isSymmetric(TreeNode* root) {
    // Write your logic here
    return true;
}

int main() {
    string line, input;
    while (getline(cin, line)) input += line + " ";
    TreeNode* root = buildTree(input);
    cout << (isSymmetric(root) ? "true" : "false") << endl;
    return 0;
}
""",
        "java": """import java.util.*;
import java.util.regex.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Main {
    public static TreeNode buildTree(String data) {
        List<String> vals = new ArrayList<>();
        Matcher m = Pattern.compile("null|-?\\\\d+").matcher(data);
        while (m.find()) vals.add(m.group());
        if (vals.isEmpty() || vals.get(0).equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(vals.get(0)));
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.size()) {
            TreeNode curr = q.poll();
            if (i < vals.size() && !vals.get(i).equals("null")) {
                curr.left = new TreeNode(Integer.parseInt(vals.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < vals.size() && !vals.get(i).equals("null")) {
                curr.right = new TreeNode(Integer.parseInt(vals.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    public static boolean isSymmetric(TreeNode root) {
        // Write your logic here
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(" ");
        TreeNode root = buildTree(sb.toString());
        System.out.println(isSymmetric(root) ? "true" : "false");
    }
}
""",
        "javascript": """const fs = require('fs');

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function buildTree(data) {
    const vals = data.match(/null|-?\\d+/g);
    if (!vals || vals[0] === 'null') return null;
    const root = new TreeNode(parseInt(vals[0]));
    const queue = [root];
    let i = 1;
    while (queue.length > 0 && i < vals.length) {
        const node = queue.shift();
        if (i < vals.length && vals[i] !== 'null') {
            node.left = new TreeNode(parseInt(vals[i]));
            queue.push(node.left);
        }
        i++;
        if (i < vals.length && vals[i] !== 'null') {
            node.right = new TreeNode(parseInt(vals[i]));
            queue.push(node.right);
        }
        i++;
    }
    return root;
}

function isSymmetric(root) {
    // Write your logic here
    return true;
}

const input = fs.readFileSync(0, 'utf8');
const root = buildTree(input);
if (root || input.includes('null') || input.match(/-?\\d+/)) {
    console.log(isSymmetric(root).toString());
}
""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* newNode(int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}

bool isSymmetric(struct TreeNode* root) {
    // Write your logic here
    return true;
}

int main() {
    char data[20000];
    int bytes = fread(data, 1, sizeof(data) - 1, stdin);
    data[bytes] = '\\0';
    
    char* vals[2000];
    int count = 0;
    char* token = strtok(data, " ,[]\\n\\r\\t");
    while (token != NULL) {
        vals[count++] = token;
        token = strtok(NULL, " ,[]\\n\\r\\t");
    }

    if (count == 0 || strcmp(vals[0], "null") == 0) {
        printf("%s\\n", isSymmetric(NULL) ? "true" : "false");
        return 0;
    }

    struct TreeNode* root = newNode(atoi(vals[0]));
    struct TreeNode* queue[2000];
    int head = 0, tail = 0;
    queue[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        struct TreeNode* node = queue[head++];
        if (i < count && strcmp(vals[i], "null") != 0) {
            node->left = newNode(atoi(vals[i]));
            queue[tail++] = node->left;
        }
        i++;
        if (i < count && strcmp(vals[i], "null") != 0) {
            node->right = newNode(atoi(vals[i]));
            queue[tail++] = node->right;
        }
        i++;
    }

    printf("%s\\n", isSymmetric(root) ? "true" : "false");
    return 0;
}
"""
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
