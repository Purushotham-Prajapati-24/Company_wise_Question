import json
import os

def generate_json():
    problem_id = 726
    title = "Number of Atoms"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>726. Number of Atoms</h3>
<p>Given a string <code>formula</code> representing a chemical formula, return the count of each atom.</p>
<p>The atomic element always starts with an uppercase character, followed by zero or more lowercase letters.</p>
<p>One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.</p>
<ul>
	<li>For example, <code>"H2O"</code> and <code>"H2O2"</code> are possible, but <code>"H1O2"</code> is impossible.</li>
</ul>
<p>Two formulas concatenated together is also a formula.</p>
<ul>
	<li>For example, <code>"H2O2He3Mg4"</code> is also a formula.</li>
</ul>
<p>A formula placed in parentheses, and a count (optionally added) after it, is also a formula.</p>
<ul>
	<li>For example, <code>"(H2O2)"</code> and <code>"(H2O2)3"</code> are formulas.</li>
</ul>
<p>Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is greater than 1), followed by the second name (in sorted order), followed by its count (if that count is greater than 1), and so on.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> formula = "H2O"
<strong>Output:</strong> "H2O"
<strong>Explanation:</strong> The count of elements are {'H': 2, 'O': 1}.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> formula = "Mg(OH)2"
<strong>Output:</strong> "H2MgO2"
<strong>Explanation:</strong> The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> formula = "K4(ON(SO3)2)2"
<strong>Output:</strong> "K4N2O14S4"
<strong>Explanation:</strong> The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 <= formula.length <= 1000</code></li>
	<li><code>formula</code> consists of English letters, digits, <code>'('</code>, and <code>')'</code>.</li>
	<li><code>formula</code> is always valid.</li>
</ul>"""

    input_format = "A string representing the chemical formula."
    output_format = "A string representing the atom counts in sorted order."
    
    constraints = ["1 <= formula.length <= 1000", "Valid chemical formula notation"]
    
    explanation = """HARD problem on ."""
    
    answer = """import collections
def countOfAtoms(formula):
    stack = [collections.Counter()]
    i, n = 0, len(formula)
    while i < n:
        if formula[i] == '(':
            stack.append(collections.Counter())
            i += 1
        elif formula[i] == ')':
            top = stack.pop()
            i += 1
            i_start = i
            while i < n and formula[i].isdigit(): i += 1
            multiplier = int(formula[i_start:i] or 1)
            for atom, count in top.items():
                stack[-1][atom] += count * multiplier
        else:
            i_start = i
            i += 1
            while i < n and formula[i].islower(): i += 1
            atom = formula[i_start:i]
            i_start = i
            while i < n and formula[i].isdigit(): i += 1
            count = int(formula[i_start:i] or 1)
            stack[-1][atom] += count
            
    res = stack[0]
    items = sorted(res.items())
    return "".join(atom + (str(count) if count > 1 else "") for atom, count in items)"""

    boilerplate = {
        "python": "import sys\n\ndef countOfAtoms(formula):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    formula = input_data[0].strip() if len(input_data) > 0 else \"\"\n    print(countOfAtoms(formula))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint countOfAtoms(string formula) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string formula; cin >> formula;\n    cout << countOfAtoms(formula) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "H2O", "expected_output": "H2O", "is_sample": True},
        {"input": "Mg(OH)2", "expected_output": "H2MgO2", "is_sample": True},
        {"input": "K4(ON(SO3)2)2", "expected_output": "K4N2O14S4", "is_sample": True},
        {"input": "H", "expected_output": "H", "is_sample": False},
        {"input": "NaCl", "expected_output": "ClNa", "is_sample": False},
        {"input": "(H2O)2", "expected_output": "H4O2", "is_sample": False},
        {"input": "((H)2)3", "expected_output": "H6", "is_sample": False},
        {"input": "Be32", "expected_output": "Be32", "is_sample": False},
        {"input": "Au", "expected_output": "Au", "is_sample": False},
        {"input": "C6H12O6", "expected_output": "C6H12O6", "is_sample": False}]

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

    output_path = "1-1000/726_Number_of_Atoms.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
