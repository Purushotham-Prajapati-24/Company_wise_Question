import json
import os

def generate_json():
    problem_id = 1145
    title = "Binary Tree Coloring Game"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1145. Binary Tree Coloring Game</h3>
<p>Two players play a turn-based game on a binary tree. We are given the <code>root</code> of this binary tree, and the number of nodes <code>n</code> in the tree. <code>n</code> is odd, and each node has a distinct value from <code>1</code> to <code>n</code>.</p>

<p>Initially, the first player named 'First' chooses a node with value <code>x</code>, and colors it red. Then, the second player named 'Second' chooses a node with value <code>y</code> (where <code>y != x</code>) and colors it blue. After that, the players take turns until they cannot make any more moves. In each turn, a player chooses a node of their color (red if First, blue if Second) and colors an <strong>uncolored</strong> neighbor of that node (either the left child, right child, or parent), or colors it Blue if Second.</p>

<p>A player's goal is to color more nodes than the opponent. Return <code>true</code> if and only if the second player can win the game.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/08/01/1480-binary-tree-coloring-game.png" style="width: 300px; height: 186px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> The second player can choose the node with value 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2,3], n = 3, x = 1
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>root</code> is a binary tree with <code>n</code> nodes and distinct node values from <code>1</code> to <code>n</code>.</li>
	<li><code>n</code> is odd.</li>
	<li><code>1 &lt;= x &lt;= n &lt;= 100</code></li>
</ul>
"""

    input_format = "An integer `n`, an integer `x`, and a binary tree `root` provided as `[n, x, root]` in JSON."
    output_format = "A boolean representing if the second player can win."

    constraints = [
        "1 <= n <= 100",
        "n is odd",
        "1 <= x <= n"
    ]

    explanation = """To determine if player 2 can win:
1. Player 1 picks node `x`. This splits the tree into three potentially disjoint components relative to `x`:
   - Left subtree of `x`.
   - Right subtree of `x`.
   - The rest of the tree (parent side).
2. Player 2 wins if they can choose a neighbor of `x` such that the size of that neighbor's component is more than half of the total nodes `n`.
3. Let `lc` be the count of nodes in the left subtree of `x` and `rc` be the count in the right subtree of `x`.
4. Then the count of nodes in the parent side is `n - (lc + rc + 1)`.
5. Player 2 wins if `max(lc, rc, n - lc - rc - 1) > n / 2`."""

    answer = """# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.lc, self.rc = 0, 0
        
        def count(node):
            if not node:
                return 0
            l = count(node.left)
            r = count(node.right)
            if node.val == x:
                self.lc = l
                self.rc = r
            return l + r + 1
        
        count(root)
        parent_part = n - (self.lc + self.rc + 1)
        return max(self.lc, self.rc, parent_part) > n // 2"""

    boilerplate = {
        "python": """import sys
import json

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # User logic here
        return False

def build_tree(lst):
    if not lst or lst[0] is None: return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if i < len(lst) and lst[i] is not None:
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
        n, x, tree_data = data
        root = build_tree(tree_data)
        sol = Solution()
        print("true" if sol.btreeGameWinningMove(root, n, x) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
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
    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        // User logic here
        return false;
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
        int n = j[0].get<int>();
        int x = j[1].get<int>();
        TreeNode* root = buildTree(j[2]);
        Solution sol;
        cout << (sol.btreeGameWinningMove(root, n, x) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int n = (int)data[0];
            int x = (int)data[1];
            List<Integer> list = (List<Integer>)data[2];
            TreeNode root = buildTree(list);
            System.out.println(new Solution().btreeGameWinningMove(root, n, x));
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

var btreeGameWinningMove = function(root, n, x) {
    // User logic here
    return false;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [n, x, list] = JSON.parse(input);
    const root = buildTree(list);
    console.log(btreeGameWinningMove(root, n, x));
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
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool btreeGameWinningMove(struct TreeNode* root, int n, int x) {
    // User logic here
    return false;
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
    int n, x;
    if (scanf("%d %d", &n, &x) != 2) return 0;
    while (getchar() != '[');
    char line[10000];
    if (fgets(line, sizeof(line), stdin)) {
        char* end = strrchr(line, ']');
        if (end) *end = '\\0';
        char* nodes[1000];
        int size = 0;
        char* token = strtok(line, ",");
        while (token) {
            while (*token == ' ') token++;
            nodes[size++] = token;
            token = strtok(NULL, ",");
        }
        struct TreeNode* root = buildTree(nodes, size);
        printf("%s\\n", btreeGameWinningMove(root, n, x) ? "true" : "false");
    }
    return 0;
}"""
    }

    def solve(n, x, lst):
        class Node:
            def __init__(self, val):
                self.val = val
                self.left = self.right = None
        def build(lst):
            if not lst or lst[0] is None: return None
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
        
        info = {'lc': 0, 'rc': 0}
        def count(node):
            if not node: return 0
            l = count(node.left)
            r = count(node.right)
            if node.val == x:
                info['lc'] = l
                info['rc'] = r
            return l + r + 1
        
        root = build(lst)
        count(root)
        p = n - info['lc'] - info['rc'] - 1
        return max(info['lc'], info['rc'], p) > n // 2

    test_cases_data = [
        [11, 3, [1,2,3,4,5,6,7,8,9,10,11]], # Sample 1
        [3, 1, [1,2,3]],                   # Sample 2
        [7, 2, [1,2,3,4,5,6,7]],
        [7, 1, [1,2,3,4,5,6,7]],
        [5, 1, [1,2,3,4,5]],
        [9, 1, [1,2,3,4,5,6,7,None,None,8,9]],
        [3, 2, [1,2,3]],
        # Stress tests
        [99, 1, [i for i in range(1, 100)]],
        [99, 50, [i for i in range(1, 100)]],
        [99, 99, [i for i in range(1, 100)]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = "true" if solve(t[0], t[1], t[2]) else "false"
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
