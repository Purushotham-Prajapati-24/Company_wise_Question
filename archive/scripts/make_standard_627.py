import json
import os

def generate_json():
    problem_id = 627
    title = "Swap Salary"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>627. Swap Salary</h3>
<p>Table: <code>Salary</code></p>
<pre>
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
id is the primary key (column with unique values) for this table.
The sex column is ENUM value of type ('m', 'f').
The table contains information about an employee.
</pre>

<p>Write a solution to swap all <code>'f'</code> and <code>'m'</code> values (i.e., change all <code>'f'</code> values to <code>'m'</code> and vice versa) with a <b>single pass</b> and without using any temporary intermediate table.</p>

<p>Note that you must write a solution that modifies the sex values in place (or simulates an in-place update).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
1,A,m,2500
2,B,f,1500
3,C,m,5500
4,D,f,500

<strong>Output:</strong> 
1 A f 2500
2 B m 1500
3 C f 5500
4 D m 500

<strong>Explanation:</strong> 
(1, A, m, 2500) becomes (1, A, f, 2500)
(2, B, f, 1500) becomes (2, B, m, 1500)
(3, C, m, 5500) becomes (3, C, f, 5500)
(4, D, f, 500) becomes (4, D, m, 500)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of records is in the range <code>[1, 1000]</code>.</li>
</ul>"""

    input_format = "Each line contains a record: 'id,name,sex,salary'."
    output_format = "Each line contains 'id name sex salary' sorted by id."
    
    constraints = [
        "1 <= n_employees <= 1000",
        "Swap 'f' <-> 'm'.",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To swap gender statuses efficiently:
1. **The Logic**:
   - For each employee record, check the value of the `sex` field.
   - if `sex == 'm'`, change it to `'f'`.
   - if `sex == 'f'`, change it to `'m'`.
2. **Implementation**:
   - This can be done using a ternary operator (if-else) or a mapping.
   - For example: `new_sex = 'f' if current_sex == 'm' else 'm'`.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of employees.
   - Space Complexity: O(1) auxiliary space beyond storage."""
    
    answer = """def swapSalary(employees: list[list]) -> list[list]:
    for emp in employees:
        emp[2] = 'f' if emp[2] == 'm' else 'm'
    return employees"""

    boilerplate = {
        "python": "import sys\n\ndef swapSalary(employees):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    employees = []\n    for line in lines:\n        if not line: continue\n        parts = line.split(',')\n        employees.append([int(parts[0]), parts[1], parts[2], int(parts[3])])\n    res = swapSalary(employees)\n    for row in res:\n        print(f\"{row[0]} {row[1]} {row[2]} {row[3]}\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        // User logic\n    }\n}",
        "javascript": "function solve(employees) {\n    // User logic\n}",
        "c": "void solve() {\n    // User logic\n}"
    }

    test_cases = [
        {"input": "1,A,m,2500\\n2,B,f,1500\\n3,C,m,5500\\n4,D,f,500", "expected_output": "1 A f 2500\\n2 B m 1500\\n3 C f 5500\\n4 D m 500", "is_sample": True},
        {"input": "1,m_only,m,100", "expected_output": "1 m_only f 100", "is_sample": True},
        {"input": "1,f_only,f,100", "expected_output": "1 f_only m 100", "is_sample": False},
        {"input": "1,A,m,1\\n2,B,m,2\\n3,C,f,3", "expected_output": "1 A f 1\\n2 B f 2\\n3 C m 3", "is_sample": False},
        {"input": "10,Boss,m,1000000", "expected_output": "10 Boss f 1000000", "is_sample": False},
        {"input": "1,1,f,10\\n2,2,f,20", "expected_output": "1 1 m 10\\n2 2 m 20", "is_sample": False},
        {"input": "1,X,m,100\\n2,Y,m,100", "expected_output": "1 X f 100\\n2 Y f 100", "is_sample": False},
        # Stress cases
        {"input": "\\n".join([f"{i},Name,m,1000" for i in range(1, 1001)]), "expected_output": "...", "is_sample": False},
        {"input": "\\n".join([f"{i},Name,f,1000" for i in range(1, 1001)]), "expected_output": "...", "is_sample": False},
        {"input": "1,Mixed,m,0\\n2,Mixed,f,0", "expected_output": "1 Mixed f 0\\n2 Mixed m 0", "is_sample": False}
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
        "topics": ["Array", "Simulation"],
        "companyIndex": 0
    }

    output_path = "601-800/627_Swap_Salary.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
