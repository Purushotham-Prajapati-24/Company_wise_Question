import json
import os
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_json():
    problem_id = 106
    title = "Construct Binary Tree from Inorder and Postorder Traversal"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>106. Construct Binary Tree from Inorder and Postorder Traversal</h3>
<p>Given two integer arrays <code>inorder</code> and <code>postorder</code> where <code>inorder</code> is the inorder traversal of a binary tree and <code>postorder</code> is the postorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" />
<pre><strong>Input:</strong> inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> inorder = [-1], postorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= inorder.length &lt;= 3000</code></li>
	<li><code>postorder.length == inorder.length</code></li>
	<li><code>-3000 &lt;= inorder[i], postorder[i] &lt;= 3000</code></li>
	<li><code>inorder</code> and <code>postorder</code> consist of <strong>unique</strong> values.</li>
	<li>Each value of <code>postorder</code> also appears in <code>inorder</code>.</li>
	<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
	<li><code>postorder</code> is <strong>guaranteed</strong> to be the postorder traversal of the tree.</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for inorder. Line 2: space-separated integers for postorder."
    output_format = "A single line containing space-separated values representing the level-order traversal of the constructed tree."
    
    constraints = [
        "1 <= inorder.length <= 3000",
        "postorder.length == inorder.length",
        "Values are unique and in range [-3000, 3000]."
    ]
    
    explanation = """To construct a binary tree from inorder and postorder traversals:
1. **Understand Properties**:
   - The *last* element in `postorder` is always the `root`.
   - In `inorder`, elements to the left of the `root` value belong to the left subtree, and elements to the right belong to the right subtree.
2. **Recursive Construction**:
   - Start from the end of `postorder`.
   - Find the index of the current root in `inorder`.
   - Build the **right** subtree first (because postorder follows Left-Right-Root, so reverse iteration visits Root-Right-Left).
   - Then build the left subtree.
3. **Optimized Search**:
   - Use a hash map to store `inorder` values and their indices for O(1) lookups.
4. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(N) to store the hash map and recursion stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    inorder_map = {val: i for i, val in enumerate(inorder)}
    post_idx = len(postorder) - 1
    
    def build(in_start, in_end):
        nonlocal post_idx
        if in_start > in_end:
            return None
        
        val = postorder[post_idx]
        post_idx -= 1
        root = TreeNode(val)
        idx = inorder_map[val]
        
        # Build RIGHT subtree first because we are traversing postorder backwards
        root.right = build(idx + 1, in_end)
        root.left = build(in_start, idx - 1)
        return root
        
    return build(0, len(inorder) - 1)"""

    boilerplate = {
        "python": """import sys
import re
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root: return ""
    res, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append("null")
    while res and res[-1] == "null": res.pop()
    return " ".join(res)

def buildTree(inorder, postorder):
    # Write your logic here
    return None

if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split('\\n')
    if len(input_data) >= 2:
        inorder = [int(x) for x in re.findall(r'-?\\d+', input_data[0])]
        postorder = [int(x) for x in re.findall(r'-?\\d+', input_data[1])]
        root = buildTree(inorder, postorder)
        print(serialize(root))
""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <regex>
#include <unordered_map>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void serialize(TreeNode* root) {
    if (!root) return;
    vector<string> res;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();
        if (node) {
            res.push_back(to_string(node->val));
            q.push(node->left);
            q.push(node->right);
        } else {
            res.push_back("null");
        }
    }
    while (!res.empty() && res.back() == "null") res.pop_back();
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << (i == res.size() - 1 ? "" : " ");
    }
    cout << endl;
}

TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
    // Write your logic here
    return NULL;
}

int main() {
    string line1, line2;
    if (!getline(cin, line1) || !getline(cin, line2)) return 0;
    regex re("-?\\\\d+");
    vector<int> in, post;
    for (sregex_iterator it(line1.begin(), line1.end(), re), end; it != end; ++it) in.push_back(stoi(it->str()));
    for (sregex_iterator it(line2.begin(), line2.end(), re), end; it != end; ++it) post.push_back(stoi(it->str()));
    TreeNode* root = buildTree(in, post);
    serialize(root);
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
    public static void serialize(TreeNode root) {
        if (root == null) return;
        List<String> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            if (node != null) {
                res.add(String.valueOf(node.val));
                q.add(node.left);
                q.add(node.right);
            } else {
                res.add("null");
            }
        }
        while (!res.isEmpty() && res.get(res.size() - 1).equals("null")) res.remove(res.size() - 1);
        for (int i = 0; i < res.size(); i++) {
            System.out.print(res.get(i) + (i == res.size() - 1 ? "" : " "));
        }
        System.out.println();
    }

    public static TreeNode buildTree(int[] inorder, int[] postorder) {
        // Write your logic here
        return null;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        String line1 = sc.nextLine();
        if (!sc.hasNextLine()) return;
        String line2 = sc.nextLine();
        
        List<Integer> inList = new ArrayList<>();
        Matcher m1 = Pattern.compile("-?\\\\d+").matcher(line1);
        while (m1.find()) inList.add(Integer.parseInt(m1.group()));
        
        List<Integer> postList = new ArrayList<>();
        Matcher m2 = Pattern.compile("-?\\\\d+").matcher(line2);
        while (m2.find()) postList.add(Integer.parseInt(m2.group()));
        
        int[] in = inList.stream().mapToInt(i -> i).toArray();
        int[] post = postList.stream().mapToInt(i -> i).toArray();
        
        TreeNode root = buildTree(in, post);
        serialize(root);
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

function serialize(root) {
    if (!root) return "";
    let res = [], q = [root];
    while (q.length) {
        let node = q.shift();
        if (node) {
            res.push(node.val.toString());
            q.push(node.left);
            q.push(node.right);
        } else {
            res.push("null");
        }
    }
    while (res.length && res[res.length - 1] === "null") res.pop();
    return res.join(" ");
}

function buildTree(inorder, postorder) {
    // Write your logic here
    return null;
}

const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const ino = (input[0].match(/-?\\d+/g) || []).map(Number);
    const pos = (input[1].match(/-?\\d+/g) || []).map(Number);
    const root = buildTree(ino, pos);
    console.log(serialize(root));
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

struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    // Write your logic here
    return NULL;
}

void serialize(struct TreeNode* root) {
    if (!root) return;
    struct TreeNode* q[10000];
    int head = 0, tail = 0;
    q[tail++] = root;
    char* res[10000];
    int rcnt = 0;
    while (head < tail) {
        struct TreeNode* node = q[head++];
        if (node) {
            res[rcnt] = (char*)malloc(10);
            sprintf(res[rcnt++], "%d", node->val);
            q[tail++] = node->left;
            q[tail++] = node->right;
        } else {
            res[rcnt++] = "null";
        }
    }
    while (rcnt > 0 && strcmp(res[rcnt - 1], "null") == 0) rcnt--;
    for (int i = 0; i < rcnt; i++) {
        printf("%s%s", res[i], (i == rcnt - 1 ? "" : " "));
    }
    printf("\\n");
}

int main() {
    char line1[20000], line2[20000];
    if (!fgets(line1, sizeof(line1), stdin) || !fgets(line2, sizeof(line2), stdin)) return 0;
    int in[3000], post[3000], isz = 0, psz = 0;
    char* t1 = strtok(line1, " ,[]\\n\\r");
    while (t1) { in[isz++] = atoi(t1); t1 = strtok(NULL, " ,[]\\n\\r"); }
    char* t2 = strtok(line2, " ,[]\\n\\r");
    while (t2) { post[psz++] = atoi(t2); t2 = strtok(NULL, " ,[]\\n\\r"); }
    struct TreeNode* root = buildTree(in, isz, post, psz);
    serialize(root);
    return 0;
}
"""
    }

    test_cases = [
        {"input": "9 3 15 20 7\\n9 15 7 20 3", "expected_output": "3 9 20 null null 15 7", "is_sample": True},
        {"input": "-1\\n-1", "expected_output": "-1", "is_sample": True},
        {"input": "1 2 3\\n3 2 1", "expected_output": "1 null 2 null 3", "is_sample": False},
        {"input": "3 2 1\\n3 2 1", "expected_output": "1 2 null 3", "is_sample": False},
        {"input": "1 2 3 4\\n4 3 2 1", "expected_output": "1 null 2 null 3 null 4", "is_sample": False},
        {"input": "1 2 3\\n1 3 2", "expected_output": "2 1 3", "is_sample": False},
        {"input": "4 2 5 1 6 3 7\\n4 5 2 6 7 3 1", "expected_output": "1 2 3 4 5 6 7", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n" + " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n" + " ".join([str(i) for i in range(100, 0, -1)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100, 0, -1)]) + "\\n" + " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False}
    ]

    def _solve(inorder, postorder):
        in_map = {v: i for i, v in enumerate(inorder)}
        pi = len(postorder)-1
        from collections import deque
        def b(l, r):
            nonlocal pi
            if l > r: return None
            v = postorder[pi]; pi -= 1
            root = TreeNode(v); idx = in_map[v]
            root.right = b(idx+1, r); root.left = b(l, idx-1)
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
        ino = list(map(int, test_cases[i]["input"].split("\\n")[0].split()))
        post = list(map(int, test_cases[i]["input"].split("\\n")[1].split()))
        test_cases[i]["expected_output"] = _solve(ino, post)

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

    output_path = "1-200/106_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
