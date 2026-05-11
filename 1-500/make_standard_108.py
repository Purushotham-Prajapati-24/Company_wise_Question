import json
import os
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_json():
    problem_id = 108
    title = "Convert Sorted Array to Binary Search Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>108. Convert Sorted Array to Binary Search Tree</h3>
<p>Given an integer array <code>nums</code> where the elements are sorted in <strong>ascending order</strong>, convert <em>it to a <strong>height-balanced</strong> binary search tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px;" />
<pre><strong>Input:</strong> nums = [-10,-3,0,5,9]
<strong>Output:</strong> [0,-3,9,-10,null,5]
<strong>Explanation:</strong> [0,-10,5,null,-3,null,9] is also accepted:
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px;" />
<pre><strong>Input:</strong> nums = [1,3]
<strong>Output:</strong> [3,1]
<strong>Explanation:</strong> [1,null,3] and [3,1] are both height-balanced BSTs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in a <strong>strictly increasing</strong> order.</li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the sorted array."
    output_format = "A single line containing space-separated values representing the level-order traversal of the height-balanced BST."
    
    constraints = [
        "1 <= nums.length <= 10^4",
        "-10^4 <= nums[i] <= 10^4",
        "nums is strictly increasing."
    ]
    
    explanation = """To convert a sorted array into a height-balanced BST:
1. **Divide and Conquer**:
   - The middle element of the sorted array should be the `root` of the balanced BST.
   - All elements to the left of the middle go into the left subtree.
   - All elements to the right of the middle go into the right subtree.
2. **Recursive Logic**:
   - `mid = (left + right) // 2`
   - `root = TreeNode(nums[mid])`
   - `root.left = sortedArrayToBST(nums, left, mid - 1)`
   - `root.right = sortedArrayToBST(nums, mid + 1, right)`
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of elements.
   - Space Complexity: O(log N) for the recursion stack (since it's height-balanced)."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def convert(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = convert(left, mid - 1)
        node.right = convert(mid + 1, right)
        return node
        
    return convert(0, len(nums) - 1)"""

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

def sortedArrayToBST(nums):
    # Write your logic here
    return None

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if input_data:
        nums = [int(x) for x in re.findall(r'-?\\d+', input_data)]
        root = sortedArrayToBST(nums)
        print(serialize(root))
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

TreeNode* sortedArrayToBST(vector<int>& nums) {
    // Write your logic here
    return NULL;
}

int main() {
    string line;
    if (!getline(cin, line)) return 0;
    regex re("-?\\\\d+");
    vector<int> nums;
    for (sregex_iterator it(line.begin(), line.end(), re), end; it != end; ++it) nums.push_back(stoi(it->str()));
    TreeNode* root = sortedArrayToBST(nums);
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

    public static TreeNode sortedArrayToBST(int[] nums) {
        // Write your logic here
        return null;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        String line = sc.nextLine();
        List<Integer> list = new ArrayList<>();
        Matcher m = Pattern.compile("-?\\\\d+").matcher(line);
        while (m.find()) list.add(Integer.parseInt(m.group()));
        int[] nums = list.stream().mapToInt(i -> i).toArray();
        TreeNode root = sortedArrayToBST(nums);
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

function sortedArrayToBST(nums) {
    // Write your logic here
    return null;
}

const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = (input.match(/-?\\d+/g) || []).map(Number);
    const root = sortedArrayToBST(nums);
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

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    // Write your logic here
    return NULL;
}

void serialize(struct TreeNode* root) {
    if (!root) return;
    struct TreeNode* q[20000];
    int head = 0, tail = 0;
    q[tail++] = root;
    char* res[20000];
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
    char line[100000];
    if (!fgets(line, sizeof(line), stdin)) return 0;
    int nums[10001], sz = 0;
    char* t = strtok(line, " ,[]\\n\\r");
    while (t) {
        nums[sz++] = atoi(t);
        t = strtok(NULL, " ,[]\\n\\r");
    }
    struct TreeNode* root = sortedArrayToBST(nums, sz);
    serialize(root);
    return 0;
}
"""
    }

    test_cases = [
        {"input": "-10 -3 0 5 9", "expected_output": "0 -10 5 null -3 null 9", "is_sample": True},
        {"input": "1 3", "expected_output": "3 1", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 2 3", "expected_output": "2 1 3", "is_sample": False},
        {"input": "1 2 3 4", "expected_output": "2 1 3 null null null 4", "is_sample": False},
        {"input": "-5 -4 -3 -2 -1", "expected_output": "-3 -5 -2 null -4 null -1", "is_sample": False},
        {"input": "0 1 2 3 4 5 6", "expected_output": "3 1 5 0 2 4 6", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 101)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(-500, 501, 10)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 1024)]), "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(nums):
        def conv(l, r):
            if l > r: return None
            m = (l+r)//2
            node = TreeNode(nums[m])
            node.left = conv(l, m-1); node.right = conv(m+1, r)
            return node
        root = conv(0, len(nums)-1)
        if not root: return ""
        from collections import deque
        res, q = [], deque([root])
        while q:
            n = q.popleft()
            if n: res.append(str(n.val)); q.append(n.left); q.append(n.right)
            else: res.append("null")
        while res and res[-1] == "null": res.pop()
        return " ".join(res)

    for i in range(7, 10):
        arr = list(map(int, test_cases[i]["input"].split()))
        test_cases[i]["expected_output"] = _solve(arr)

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
        "topics": ["Tree", "DFS", "Binary Search Tree", "Array"],
        "companyIndex": 0
    }

    output_path = "1-200/108_Convert_Sorted_Array_to_Binary_Search_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
