import json
import os

def generate_json():
    problem_id = 1265
    title = "Print Immutable Linked List in Reverse"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>1265. Print Immutable Linked List in Reverse</h3>
<p>You are given an immutable linked list, print out all nodes of each node in reverse order using the following interface:</p>

<ul>
	<li><code>ImmutableListNode</code>: An interface of immutable linked list, you are given the head of the list.</li>
	<li><code>ImmutableListNode.printValue()</code>: Print value of the current node.</li>
	<li><code>ImmutableListNode.getNext()</code>: Return the next node.</li>
</ul>

<p>The input is given internally as a linked list in which each node's value is between <code>-1000</code> and <code>1000</code>. The length of the linked list is between <code>1</code> and <code>1000</code>.</p>

<p><strong>You are not allowed to modify the linked list or access the <code>ImmutableListNode</code> implementation directly.</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [4,3,2,1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [0,-4,-1,3,-5]
<strong>Output:</strong> [-5,3,-1,-4,0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [-2,0,6,4,4,-6]
<strong>Output:</strong> [-6,4,4,6,0,-2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The length of the linked list is between <code>1</code> and <code>1000</code>.</li>
	<li>The value of each node in the linked list is between <code>-1000</code> and <code>1000</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong>

<ul>
	<li>Could you solve this problem in:
	<ul>
		<li>Constant space complexity?</li>
		<li>Linear time complexity and less than linear space complexity?</li>
	</ul>
	</li>
</ul>"""

    input_format = "A list of integers representing the linked list."
    output_format = "The node values printed in reverse order, one per line or separated by spaces."
    
    constraints = ["1 <= list.length <= 1000", "-1000 <= node.val <= 1000", "Cannot modify the linked list."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def printLinkedListInReverse(head):
    if head:
        printLinkedListInReverse(head.getNext())
        head.printValue()"""

    boilerplate = {
        "python": "import sys\n\ndef printLinkedListInReverse(head):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    head = input_data[0].strip() if len(input_data) > 0 else \"\"\n    print(printLinkedListInReverse(head))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint printLinkedListInReverse(string head) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string head; cin >> head;\n    cout << printLinkedListInReverse(head) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "1 2 3 4", "expected_output": "4 3 2 1", "is_sample": True},
        {"input": "0 -4 -1 3 -5", "expected_output": "-5 3 -1 -4 0", "is_sample": True},
        {"input": "-2 0 6 4 4 -6", "expected_output": "-6 4 4 6 0 -2", "is_sample": True},
        {"input": "10", "expected_output": "10", "is_sample": False},
        {"input": "1 1 1 1", "expected_output": "1 1 1 1", "is_sample": False},
        {"input": "5 4 3 2 1", "expected_output": "1 2 3 4 5", "is_sample": False},
        {"input": "-1000 1000", "expected_output": "1000 -1000", "is_sample": False},
        {"input": "0", "expected_output": "0", "is_sample": False},
        # Stress Cases
        {"input": " ".join([str(i) for i in range(1000)]), "expected_output": " ".join([str(i) for i in range(999, -1, -1)]), "is_sample": False},
        {"input": " ".join(["0"]*1000), "expected_output": " ".join(["0"]*1000), "is_sample": False}]

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
