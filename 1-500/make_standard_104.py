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

def maxDepth(root):
    # Write your logic here
    return 0

if __name__ == "__main__":
    input_data = sys.stdin.read()
    if not input_data.strip():
        print(0)
        sys.exit(0)
    root = build_tree(input_data)
    result = maxDepth(root)
    print(result)
""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <regex>
#include <algorithm>

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

int maxDepth(TreeNode* root) {
    // Write your logic here
    return 0;
}

int main() {
    string line, input;
    while (getline(cin, line)) input += line + " ";
    TreeNode* root = buildTree(input);
    cout << maxDepth(root) << endl;
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

    public static int maxDepth(TreeNode root) {
        // Write your logic here
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(" ");
        TreeNode root = buildTree(sb.toString());
        System.out.println(maxDepth(root));
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

function maxDepth(root) {
    // Write your logic here
    return 0;
}

const input = fs.readFileSync(0, 'utf8');
const root = buildTree(input);
if (root || input.includes('null') || input.match(/-?\\d+/)) {
    console.log(maxDepth(root));
} else {
    console.log(0);
}
""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

int maxDepth(struct TreeNode* root) {
    // Write your logic here
    return 0;
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
        printf("0\\n");
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

    printf("%d\\n", maxDepth(root));
    return 0;
}
"""
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
