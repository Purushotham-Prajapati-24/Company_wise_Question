import json
import os

def generate_json():
    problem_id = 1120
    title = "Maximum Average Subtree"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1120. Maximum Average Subtree</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the maximum average value of a subtree of that tree</em>. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p>A subtree of a tree is any node of that tree plus all its descendants.</p>

<p>The average value of a tree is the sum of its values, divided by the number of nodes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/09/1308_example_1.png" style="width: 132px; height: 123px;" />
<pre>
<strong>Input:</strong> root = [5,6,1]
<strong>Output:</strong> 6.00000
<strong>Explanation:</strong> 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
The maximum average is 6 which is the average of the subtree rooted at 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [0,null,1]
<strong>Output:</strong> 1.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>
"""

    input_format = "A binary tree `root` provided as `[root]` in JSON (level-order)."
    output_format = "A float representing the maximum average."

    constraints = [
        "1 <= Number of nodes <= 10^4",
        "0 <= Node.val <= 10^5"
    ]

    explanation = """To find the maximum average subtree:
1. Use a post-order traversal (DFS) to process each node.
2. For each node, return two values: the total sum of the subtree and the count of nodes in the subtree.
3. The average of the current subtree is `total_sum / count`.
4. Keep track of the maximum average seen so far across all nodes.
5. Return the maximum average."""

    answer = """# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = 0.0
        
        def dfs(node):
            if not node:
                return 0, 0 # sum, count
            
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            
            curr_sum = ls + rs + node.val
            curr_count = lc + rc + 1
            self.max_avg = max(self.max_avg, curr_sum / curr_count)
            return curr_sum, curr_count
        
        dfs(root)
        return self.max_avg"""

    boilerplate = {
        "python": """import sys
import json

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        # User logic here
        return 0.0

def build_tree(lst):
    if not lst or lst[0] is None: return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        data = json.loads(raw)
        if isinstance(data[0], list): data = data[0]
        root = build_tree(data)
        sol = Solution()
        print(f"{sol.maximumAverageSubtree(root):.5f}")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    double maximumAverageSubtree(TreeNode* root) {
        // User logic here
        return 0.0;
    }
};

TreeNode* buildTree(json j) {
    if (j.empty() || j[0].is_null()) return NULL;
    TreeNode* root = new TreeNode(j[0].get<int>());
    vector<TreeNode*> q;
    q.push_back(root);
    int head = 0, i = 1;
    while (head < q.size() && i < j.size()) {
        TreeNode* curr = q[head++];
        if (!j[i].is_null()) {
            curr->left = new TreeNode(j[i].get<int>());
            q.push_back(curr->left);
        }
        i++;
        if (i < j.size() && !j[i].is_null()) {
            curr->right = new TreeNode(j[i].get<int>());
            q.push_back(curr->right);
        }
        i++;
    }
    return root;
}

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        if (j.is_array() && j.size() > 0 && j[0].is_array()) j = j[0];
        TreeNode* root = buildTree(j);
        Solution sol;
        cout << fixed << setprecision(5) << sol.maximumAverageSubtree(root) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public double maximumAverageSubtree(TreeNode root) {
        // User logic here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object raw = mapper.readValue(sc.nextLine(), Object.class);
            List<Integer> list;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)raw).get(0) instanceof List) {
                list = (List<Integer>)((List)raw).get(0);
            } else {
                list = (List<Integer>)raw;
            }
            TreeNode root = buildTree(list);
            System.out.printf("%.5f\\n", new Solution().maximumAverageSubtree(root));
        }
    }
    private static TreeNode buildTree(List<Integer> list) {
        if (list.isEmpty() || list.get(0) == null) return null;
        TreeNode root = new TreeNode(list.get(0));
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int i = 1;
        while (!q.isEmpty() && i < list.size()) {
            TreeNode curr = q.poll();
            if (i < list.size() && list.get(i) != null) {
                curr.left = new TreeNode(list.get(i));
                q.offer(curr.left);
            }
            i++;
            if (i < list.size() && list.get(i) != null) {
                curr.right = new TreeNode(list.get(i));
                q.offer(curr.right);
            }
            i++;
        }
        return root;
    }
}""",
        "javascript": """function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var maximumAverageSubtree = function(root) {
    // User logic here
    return 0.0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let list = JSON.parse(input);
    if (Array.isArray(list[0])) list = list[0];
    const root = buildTree(list);
    console.log(maximumAverageSubtree(root).toFixed(5));
}

function buildTree(list) {
    if (!list.length || list[0] === null) return null;
    let root = new TreeNode(list[0]);
    let q = [root];
    let i = 1;
    while (q.length && i < list.length) {
        let curr = q.shift();
        if (i < list.length && list[i] !== null) {
            curr.left = new TreeNode(list[i]);
            q.push(curr.left);
        }
        i++;
        if (i < list.length && list[i] !== null) {
            curr.right = new TreeNode(list[i]);
            q.push(curr.right);
        }
        i++;
    }
    return root;
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

double maximumAverageSubtree(struct TreeNode* root) {
    // User logic here
    return 0.0;
}

struct TreeNode* buildTree(char** nodes, int size) {
    if (size == 0 || strcmp(nodes[0], "null") == 0) return NULL;
    struct TreeNode** queue = malloc(size * sizeof(struct TreeNode*));
    struct TreeNode* root = malloc(sizeof(struct TreeNode));
    root->val = atoi(nodes[0]);
    root->left = root->right = NULL;
    queue[0] = root;
    int head = 0, tail = 1, i = 1;
    while (i < size) {
        struct TreeNode* curr = queue[head++];
        if (i < size && strcmp(nodes[i], "null") != 0) {
            curr->left = malloc(sizeof(struct TreeNode));
            curr->left->val = atoi(nodes[i]);
            curr->left->left = curr->left->right = NULL;
            queue[tail++] = curr->left;
        }
        i++;
        if (i < size && strcmp(nodes[i], "null") != 0) {
            curr->right = malloc(sizeof(struct TreeNode));
            curr->right->val = atoi(nodes[i]);
            curr->right->left = curr->right->right = NULL;
            queue[tail++] = curr->right;
        }
        i++;
    }
    free(queue);
    return root;
}

int main() {
    char line[10000];
    if (fgets(line, sizeof(line), stdin)) {
        char* p = strchr(line, '[');
        if (!p) return 0;
        p++;
        char* end = strrchr(p, ']');
        if (end) *end = '\\0';
        char* nodes[10000];
        int size = 0;
        char* token = strtok(p, ",");
        while (token) {
            while (*token == ' ') token++;
            nodes[size++] = token;
            token = strtok(NULL, ",");
        }
        struct TreeNode* root = buildTree(nodes, size);
        printf("%.5f\\n", maximumAverageSubtree(root));
    }
    return 0;
}"""
    }

    def solve(lst):
        if not lst or lst[0] is None: return 0.0
        class Node:
            def __init__(self, val):
                self.val = val
                self.left = self.right = None
        def build(lst):
            root = Node(lst[0])
            q = [root]
            i = 1
            while q and i < len(lst):
                curr = q.pop(0)
                if i < len(lst) and lst[i] is not None:
                    curr.left = Node(lst[i])
                    q.append(curr.left)
                i += 1
                if i < len(lst) and lst[i] is not None:
                    curr.right = Node(lst[i])
                    q.append(curr.right)
                i += 1
            return root
        
        mx = [0.0]
        def dfs(node):
            if not node: return 0, 0
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            s = ls + rs + node.val
            c = lc + rc + 1
            mx[0] = max(mx[0], s / c)
            return s, c
        dfs(build(lst))
        return mx[0]

    test_cases_data = [
        [[5,6,1]],        # Sample 1
        [[0,None,1]],     # Sample 2
        [[10,2,3,4,5,1,1]],
        [[100]],
        [[1,2,3,4,5,100]],
        [[0,0,0,0,0]],
        [[None]],
        # Stress tests
        [[i for i in range(1000)]],
        [[100000]*1000],
        [[0]*1000]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = f"{solve(t[0]):.5f}"
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Tree", "Depth-First Search", "Binary Tree"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
