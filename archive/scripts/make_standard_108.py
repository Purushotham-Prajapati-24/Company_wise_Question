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
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef sortedArrayToBST(nums):\n    # User logic here\n    pass\n\ndef serialize(root):\n    if not root: return \"\"\n    res, queue = [], deque([root])\n    while queue:\n        node = queue.popleft()\n        if node:\n            res.append(str(node.val))\n            queue.append(node.left)\n            queue.append(node.right)\n        else:\n            res.append(\"null\")\n    while res and res[-1] == \"null\": res.pop()\n    return \" \".join(res)\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        nums = list(map(int, data))\n        print(serialize(sortedArrayToBST(nums)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\nusing namespace std;\nstruct TreeNode { int val; TreeNode *left, *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };\nTreeNode* sortedArrayToBST(vector<int>& nums) { return NULL; }\nint main() {\n    int x; vector<int> nums;\n    while(cin >> x) nums.push_back(x);\n    TreeNode* root = sortedArrayToBST(nums);\n    if(!root) { cout << endl; return 0; }\n    queue<TreeNode*> q; q.push(root); vector<string> res;\n    while(!q.empty()){ TreeNode* n=q.front(); q.pop(); if(n){ res.push_back(to_string(n->val)); q.push(n->left); q.push(n->right); }else{ res.push_back(\"null\"); } }\n    while(!res.empty() && res.back()==\"null\") res.pop_back();\n    for(int i=0;i<(int)res.size();i++) cout<<res[i]<<(i+1<(int)res.size()?\" \":\"\"); cout<<endl;\n    return 0;\n}",
        "java": "import java.util.*;\nclass TreeNode { int val; TreeNode left, right; TreeNode(int x) { val = x; } }\npublic class Main {\n    public static TreeNode sortedArrayToBST(int[] nums) { return null; }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in); List<Integer> list = new ArrayList<>();\n        while(sc.hasNextInt()) list.add(sc.nextInt());\n        int[] nums = list.stream().mapToInt(i->i).toArray();\n        TreeNode root = sortedArrayToBST(nums);\n        if(root==null){ System.out.println(); return; }\n        Queue<TreeNode> q = new LinkedList<>(); q.add(root); List<String> res=new ArrayList<>();\n        while(!q.isEmpty()){ TreeNode n=q.poll(); if(n!=null){res.add(String.valueOf(n.val)); q.add(n.left); q.add(n.right);}else{res.add(\"null\");} }\n        while(!res.isEmpty() && res.get(res.size()-1).equals(\"null\")) res.remove(res.size()-1);\n        System.out.println(String.join(\" \", res));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction TreeNode(val, left, right) { this.val = (val===undefined ? 0 : val); this.left = (left===undefined ? null : left); this.right = (right===undefined ? null : right); }\nfunction sortedArrayToBST(nums) {}\nconst tokens=fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(tokens.length>0 && tokens[0]!==''){\n    const nums = tokens.map(Number);\n    const root=sortedArrayToBST(nums);\n    if(!root){console.log(\"\");}else{\n        let q=[root], res=[];\n        while(q.length){let n=q.shift();if(n){res.push(n.val);q.push(n.left, n.right);}else{res.push(\"null\");}}\n        while(res.length && res[res.length-1]===\"null\") res.pop();\n        console.log(res.join(\" \"));\n    }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };\nstruct TreeNode* sortedArrayToBST(int* nums, int numsSize) { return NULL; }\nint main() {\n    int nums[10001], sz=0;\n    while(scanf(\"%d\", &nums[sz])==1) sz++;\n    struct TreeNode* root = sortedArrayToBST(nums, sz);\n    if(!root){printf(\"\\n\"); return 0;}\n    struct TreeNode* q[20000]; int head=0, tail=0; q[tail++]=root;\n    char res[20000][10]; int rcnt=0;\n    while(head<tail){ struct TreeNode* n=q[head++]; if(n){ sprintf(res[rcnt++], \"%d\", n->val); q[tail++]=n->left; q[tail++]=n->right; }else{ strcpy(res[rcnt++], \"null\"); } }\n    while(rcnt>0 && strcmp(res[rcnt-1], \"null\")==0) rcnt--;\n    for(int i=0;i<rcnt;i++){ printf(\"%s\", res[i]); if(i+1<rcnt) printf(\" \"); }\n    printf(\"\\n\"); return 0;\n}"
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
