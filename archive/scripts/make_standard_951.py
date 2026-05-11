import json
import os

def generate_json():
    problem_id = 951
    title = "Flip Equivalent Binary Trees"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>951. Flip Equivalent Binary Trees</h3>
<p>For a binary tree <strong>T</strong>, we can define a <strong>flip operation</strong> as follows: choose any node, and swap the left and right child subtrees.</p>

<p>A binary tree <strong>X</strong>&nbsp;is <strong>flip equivalent</strong> to a binary tree <strong>Y</strong> if and only if <strong>X</strong> can be transformed into <strong>Y</strong> by some number of flip operations.</p>

<p>Given the roots of two binary trees <code>root1</code> and <code>root2</code>, return <code>true</code> if the trees are flip equivalent or <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="Flipped Binary Tree" src="https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png" style="width: 500px; height: 220px;" />
<pre>
<strong>Input:</strong> root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
<strong>Output:</strong> true
<strong>Explanation: </strong>We flipped at nodes with values 1, 3, and 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root1 = [], root2 = []
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root1 = [], root2 = [1]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each tree is in the range <code>[0, 100]</code>.</li>
	<li>Each tree will have <strong>unique</strong> node values in the range <code>[0, 99]</code>.</li>
</ul>"""

    input_format = "Two level-order traversals of binary trees root1 and root2. Each preceded by its length."
    output_format = "A boolean (true/false)."
    
    constraints = ["Nodes: 0 to 100.", "Unique values: 0 to 99."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def flipEquiv(root1, root2):
    if root1 is root2: return True
    if not root1 or not root2 or root1.val != root2.val: return False
    
    return (flipEquiv(root1.left, root2.left) and flipEquiv(root1.right, root2.right)) or \\
           (flipEquiv(root1.left, root2.right) and flipEquiv(root1.right, root2.left))"""

    boilerplate = {
        "python": "import sys\n\ndef flipEquiv(root1, root2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    root1 = input_data[0] if len(input_data) > 0 else \"\"\n    root2 = input_data[1] if len(input_data) > 1 else \"\"\n    print(flipEquiv(root1, root2))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint flipEquiv(string root1, string root2) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string root1; cin >> root1;\n    string root2; cin >> root2;\n    cout << flipEquiv(root1, root2) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
