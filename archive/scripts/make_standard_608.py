import json
import os

def generate_json():
    problem_id = 608
    title = "Tree Node"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>608. Tree Node</h3>
<p>Table: <code>Tree</code></p>
<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the id of a node and the id of its parent node.
</pre>

<p>Each node in the tree can be one of three types:</p>
<ul>
	<li><b>"Root"</b>: if the node is the root of the tree.</li>
	<li><b>"Leaf"</b>: if the node is a leaf node.</li>
	<li><b>"Inner"</b>: if the node is neither a root nor a leaf node.</li>
</ul>

<p>Write a solution to report the type of each node in the tree. Return the result table <b>ordered by id</b> in ascending order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0608.Tree%20Node/images/tree1.jpg" style="width: 100%; max-width: 304px;" />
<pre>
<strong>Input:</strong> 
1,null
2,1
3,1
4,2
5,2

<strong>Output:</strong> 
1 Root
2 Inner
3 Leaf
4 Leaf
5 Leaf

<strong>Explanation:</strong> 
Node 1 is the root node because its parent node is null and it has child nodes 2 and 3.
Node 2 is an inner node because it has parent node 1 and child nodes 4 and 5.
Nodes 3, 4, and 5 are leaf nodes because they have parent nodes and they do not have child nodes.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0608.Tree%20Node/images/tree1.jpg" style="width: 100%; max-width: 200px;" />
<pre>
<strong>Input:</strong> 
1,null

<strong>Output:</strong> 
1 Root

<strong>Explanation:</strong> 
If there is only one node on the tree, you only need to output its root type.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes is in the range <code>[1, 1000]</code>.</li>
</ul>"""

    input_format = "Each line contains a record: 'id,p_id'. Use 'null' for root's parent."
    output_format = "Each line contains 'id Type', sorted by id ascending."
    
    constraints = [
        "1 <= n_nodes <= 1000.",
        "Exactly one root.",
        "Types: Root, Inner, Leaf.",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To classify each node in a tree given child-parent pairs:
1. **The Strategy**:
   - A node is **Root** if its parent ID is `null`.
   - A node is **Inner** if it has a parent AND it is a parent to at least one other node.
   - A node is **Leaf** if it has a parent BUT it is not a parent to any other node.
2. **Implementation**:
   - Identify the set of all IDs that appear in the `p_id` column. These are "parents".
   - Iterate through each node `(id, p_id)`:
     - If `p_id` is `null`: Type is "Root".
     - Else if `id` is in the set of parents: Type is "Inner".
     - Else: Type is "Leaf".
3. **Sorting**:
   - Store results in a list and sort by `id` before outputting.
4. **Complexity**:
   - Time Complexity: O(N log N) due to sorting, or O(N) if we use an array/map for ID mapping.
   - Space Complexity: O(N) to store parentage and results."""
    
    answer = """def treeNode(tree: list[tuple]) -> list[tuple]:
    parents = set(node[1] for node in tree if node[1] is not None)
    all_parents = set(node[1] for node in tree if node[1] is not None)
    
    # Actually, the set of IDs that ARE parents of someone
    is_parent_of_someone = set(node[1] for node in tree if node[1] is not None)
    
    res = []
    for node_id, p_id in tree:
        if p_id is None:
            res.append((node_id, "Root"))
        elif node_id in is_parent_of_someone:
            res.append((node_id, "Inner"))
        else:
            res.append((node_id, "Leaf"))
            
    res.sort()
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef treeNode(tree):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    tree = []\n    for line in lines:\n        if not line: continue\n        parts = line.split(',')\n        node_id = int(parts[0])\n        p_id = int(parts[1]) if parts[1] != 'null' else None\n        tree.append((node_id, p_id))\n    res = treeNode(tree)\n    for nid, t in res:\n        print(f\"{nid} {t}\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_set>\n#include <algorithm>\n\nusing namespace std;\n\nint main() {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        // User logic\n    }\n}",
        "javascript": "function solve(tree) {\n    // User logic\n}",
        "c": "void solve() {\n    // User logic\n}"
    }

    test_cases = [
        {"input": "1,null\\n2,1\\n3,1\\n4,2\\n5,2", "expected_output": "1 Root\\n2 Inner\\n3 Leaf\\n4 Leaf\\n5 Leaf", "is_sample": True},
        {"input": "1,null", "expected_output": "1 Root", "is_sample": True},
        {"input": "1,null\\n2,1", "expected_output": "1 Root\\n2 Leaf", "is_sample": False},
        {"input": "1,null\\n2,1\\n3,2", "expected_output": "1 Root\\n2 Inner\\n3 Leaf", "is_sample": False},
        {"input": "10,null\\n5,10\\n15,10", "expected_output": "5 Leaf\\n10 Root\\n15 Leaf", "is_sample": False},
        {"input": "1,null\\n2,1\\n3,1\\n4,1", "expected_output": "1 Root\\n2 Leaf\\n3 Leaf\\n4 Leaf", "is_sample": False},
        {"input": "2,null\\n1,2", "expected_output": "1 Leaf\\n2 Root", "is_sample": False},
        # Stress cases
        {"input": "1,null\\n" + "\\n".join([f"{i},1" for i in range(2, 1001)]), "expected_output": "1 Root\\n" + "\\n".join([f"{i} Leaf" for i in range(2, 1001)]), "is_sample": False},
        {"input": "\\n".join([f"{i},{i-1}" for i in range(2, 1001)]) + "\\n1,null", "expected_output": "1 Root\\n" + "\\n".join([f"{i} Inner" for i in range(2, 1000)]) + "\\n1000 Leaf", "is_sample": False},
        {"input": "5,null\\n1,5\\n2,5\\n3,5\\n4,5", "expected_output": "1 Leaf\\n2 Leaf\\n3 Leaf\\n4 Leaf\\n5 Root", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Tree"],
        "companyIndex": 0
    }

    output_path = "601-800/608_Tree_Node.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
