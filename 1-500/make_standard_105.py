import json
import os
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_json():
    problem_id = 105
    title = "Construct Binary Tree from Preorder and Inorder Traversal"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>105. Construct Binary Tree from Preorder and Inorder Traversal</h3>
<p>Given two integer arrays <code>preorder</code> and <code>inorder</code> where <code>preorder</code> is the preorder traversal of a binary tree and <code>inorder</code> is the inorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" />
<pre><strong>Input:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> preorder = [-1], inorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= preorder.length &lt;= 3000</code></li>
	<li><code>inorder.length == preorder.length</code></li>
	<li><code>-3000 &lt;= preorder[i], inorder[i] &lt;= 3000</code></li>
	<li><code>preorder</code> and <code>inorder</code> consist of <strong>unique</strong> values.</li>
	<li>Each value of <code>inorder</code> also appears in <code>preorder</code>.</li>
	<li><code>preorder</code> is <strong>guaranteed</strong> to be the preorder traversal of the tree.</li>
	<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for preorder. Line 2: space-separated integers for inorder."
    output_format = "A single line containing space-separated values representing the level-order traversal of the constructed tree."
    
    constraints = [
        "1 <= preorder.length <= 3000",
        "inorder.length == preorder.length",
        "Values are unique and in range [-3000, 3000]."
    ]
    
    explanation = """To construct a binary tree from preorder and inorder traversals:
1. **Understand Properties**:
   - The first element in `preorder` is always the `root`.
   - In `inorder`, elements to the left of the `root` value belong to the left subtree, and elements to the right belong to the right subtree.
2. **Recursive Construction**:
   - Find the index of the root in `inorder`. Let this be `idx`.
   - The left subtree has `idx` nodes.
   - Recurse for the left subtree using appropriate slices of `preorder` and `inorder`.
   - Recurse for the right subtree using the remaining slices.
3. **Optimized Search**:
   - Use a hash map to store `inorder` values and their indices for O(1) lookups.
4. **Complexity**:
   - Time Complexity: O(N) because we build each node exactly once.
   - Space Complexity: O(N) to store the hash map and recursion stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    inorder_map = {val: i for i, val in enumerate(inorder)}
    pre_iter = iter(preorder)
    
    def build(in_start, in_end):
        if in_start > in_end:
            return None
        
        val = next(pre_iter)
        root = TreeNode(val)
        idx = inorder_map[val]
        
        root.left = build(in_start, idx - 1)
        root.right = build(idx + 1, in_end)
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

def buildTree(preorder, inorder):
    # Write your logic here
    return None

if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split('\\n')
    if len(input_data) >= 2:
        preorder = [int(x) for x in re.findall(r'-?\\d+', input_data[0])]
        inorder = [int(x) for x in re.findall(r'-?\\d+', input_data[1])]
        root = buildTree(preorder, inorder)
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

TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    // Write your logic here
    return NULL;
}

int main() {
    string line1, line2;
    if (!getline(cin, line1) || !getline(cin, line2)) return 0;
    regex re("-?\\\\d+");
    vector<int> pre, in;
    for (sregex_iterator it(line1.begin(), line1.end(), re), end; it != end; ++it) pre.push_back(stoi(it->str()));
    for (sregex_iterator it(line2.begin(), line2.end(), re), end; it != end; ++it) in.push_back(stoi(it->str()));
    TreeNode* root = buildTree(pre, in);
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

    public static TreeNode buildTree(int[] preorder, int[] inorder) {
        // Write your logic here
        return null;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        String line1 = sc.nextLine();
        if (!sc.hasNextLine()) return;
        String line2 = sc.nextLine();
        
        List<Integer> preList = new ArrayList<>();
        Matcher m1 = Pattern.compile("-?\\\\d+").matcher(line1);
        while (m1.find()) preList.add(Integer.parseInt(m1.group()));
        
        List<Integer> inList = new ArrayList<>();
        Matcher m2 = Pattern.compile("-?\\\\d+").matcher(line2);
        while (m2.find()) inList.add(Integer.parseInt(m2.group()));
        
        int[] pre = preList.stream().mapToInt(i -> i).toArray();
        int[] in = inList.stream().mapToInt(i -> i).toArray();
        
        TreeNode root = buildTree(pre, in);
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

function buildTree(preorder, inorder) {
    // Write your logic here
    return null;
}

const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const pre = (input[0].match(/-?\\d+/g) || []).map(Number);
    const ino = (input[1].match(/-?\\d+/g) || []).map(Number);
    const root = buildTree(pre, ino);
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

struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
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
    int pre[3000], in[3000], psz = 0, isz = 0;
    char* t1 = strtok(line1, " ,[]\\n\\r");
    while (t1) { pre[psz++] = atoi(t1); t1 = strtok(NULL, " ,[]\\n\\r"); }
    char* t2 = strtok(line2, " ,[]\\n\\r");
    while (t2) { in[isz++] = atoi(t2); t2 = strtok(NULL, " ,[]\\n\\r"); }
    struct TreeNode* root = buildTree(pre, psz, in, isz);
    serialize(root);
    return 0;
}
"""
    }

    test_cases = [
        {"input": "3 9 20 15 7\\n9 3 15 20 7", "expected_output": "3 9 20 null null 15 7", "is_sample": True},
        {"input": "-1\\n-1", "expected_output": "-1", "is_sample": True},
        {"input": "1 2 3\\n1 2 3", "expected_output": "1 null 2 null 3", "is_sample": False},
        {"input": "1 2 3\\n3 2 1", "expected_output": "1 2 null 3", "is_sample": False},
        {"input": "1 2 3 4\\n1 2 3 4", "expected_output": "1 null 2 null 3 null 4", "is_sample": False},
        {"input": "2 1 3\\n1 2 3", "expected_output": "2 1 3", "is_sample": False},
        {"input": "1 2 4 5 3 6 7\\n4 2 5 1 6 3 7", "expected_output": "1 2 3 4 5 6 7", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n" + " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n" + " ".join([str(i) for i in range(100, 0, -1)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100, 0, -1)]) + "\\n" + " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(preorder, inorder):
        in_map = {v: i for i, v in enumerate(inorder)}
        pi = 0
        def b(l, r):
            nonlocal pi
            if l > r: return None
            v = preorder[pi]; pi += 1
            root = TreeNode(v); idx = in_map[v]
            root.left = b(l, idx-1); root.right = b(idx+1, r)
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
        pre = list(map(int, test_cases[i]["input"].split("\\n")[0].split()))
        ino = list(map(int, test_cases[i]["input"].split("\\n")[1].split()))
        test_cases[i]["expected_output"] = _solve(pre, ino)

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

    output_path = "1-200/105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
