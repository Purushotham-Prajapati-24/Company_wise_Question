import json
import os

def generate_json():
    problem_id = 1261
    title = "Find Elements in a Contaminated Binary Tree"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>1261. Find Elements in a Contaminated Binary Tree</h3>
<p>Given a binary tree with the following rules:</p>

<ol>
	<li><code>root.val == 0</code></li>
	<li>If <code>treeNode.val == x</code> and <code>treeNode.left != null</code>, then <code>treeNode.left.val == 2 * x + 1</code></li>
	<li>If <code>treeNode.val == x</code> and <code>treeNode.right != null</code>, then <code>treeNode.right.val == 2 * x + 2</code></li>
</ol>

<p>Now the binary tree is contaminated, which means all <code>treeNode.val</code> have been changed to <code>-1</code>.</p>

<p>Implement the <code>FindElements</code> class:</p>

<ul>
	<li><code>FindElements(TreeNode* root)</code> Initializes the object with a contaminated binary tree and recovers it.</li>
	<li><code>bool find(int target)</code> Returns <code>true</code> if the <code>target</code> value exists in the recovered binary tree.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4-1.jpg" style="width: 322px; height: 191px;" />
<pre>
<strong>Input</strong>
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
<strong>Output</strong>
[null,false,true]
<strong>Explanation</strong>
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True </pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4.jpg" style="width: 486px; height: 175px;" />
<pre>
<strong>Input</strong>
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
<strong>Output</strong>
[null,true,true,false]
<strong>Explanation</strong>
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/07/untitled-diagram-4-1-1.jpg" style="width: 500px; height: 260px;" />
<pre>
<strong>Input</strong>
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
<strong>Output</strong>
[null,true,false,false,true]
<strong>Explanation</strong>
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>TreeNode.val == -1</code></li>
	<li>The height of the binary tree is less than or equal to <code>20</code></li>
	<li>The total number of nodes is between <code>[1, 10<sup>4</sup>]</code></li>
	<li>The total number of calls to <code>find()</code> is between <code>[1, 10<sup>4</sup>]</code></li>
	<li><code>0 &lt;= target &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "A serialized level-order traversal of the contaminated tree (using"
    output_format = "For each find operation,"
    
    constraints = ["Tree height <= 20", "Total nodes <= 10", "000", "Total find() calls <= 10", "000", "0 <= target <= 10^6"]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """class FindElements:
    def __init__(self, root):
        self.seen = set()
        self.dfs(root, 0)

    def dfs(self, node, val):
        if not node:
            return
        self.seen.add(val)
        self.dfs(node.left, 2 * val + 1)
        self.dfs(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.seen"""

    boilerplate = {
        "python": "import sys\n\ndef dfs(node, val):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    node = input_data[0].strip() if len(input_data) > 0 else \"\"\n    val = input_data[1].strip() if len(input_data) > 1 else \"\"\n    print(dfs(node, val))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint dfs(string node, string val) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string node; cin >> node;\n    string val; cin >> val;\n    cout << dfs(node, val) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "3 -1 null -1 2 1 2", "expected_output": "false true", "is_sample": True},
        {"input": "5 -1 -1 -1 -1 -1 3 1 3 5", "expected_output": "true true false", "is_sample": True},
        {"input": "6 -1 null -1 -1 null -1 4 2 3 4 5", "expected_output": "true false false true", "is_sample": True},
        {"input": "1 -1 1 0", "expected_output": "true", "is_sample": False},
        {"input": "7 -1 -1 -1 -1 -1 -1 -1 7 0 1 2 3 4 5 6", "expected_output": "true true true true true true true", "is_sample": False},
        {"input": "3 -1 -1 null 1 2", "expected_output": "false", "is_sample": False},
        {"input": "1 -1 2 100 0", "expected_output": "false true", "is_sample": False},
        # Stress Cases
        {"input": "1000 " + " ".join(["-1"]*1000) + " 1 999", "expected_output": "true", "is_sample": False},
        {"input": "1000 " + " ".join(["-1"]*1000) + " 1 1001", "expected_output": "false", "is_sample": False},]

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
