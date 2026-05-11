import json
import os

def generate_json():
    problem_id = 580
    title = "Count Student Number in Departments"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>580. Count Student Number in Departments</h3>
<p>A university uses two tables, <code>department</code> and <code>student</code>, to store data about its students and the departments associated with each major.</p>

<p>Write a solution to report the department name and the number of students majoring in each department.</p>

<p>Include <b>all</b> departments listed in the <code>department</code> table, even those with no students.</p>

<p>Return the result table ordered by the number of students in <b>descending order</b>. In case of a tie, order them by department name <b>alphabetically</b>.</p>

<p>&nbsp;</p>
<p><strong>Table schemas:</strong></p>
<pre>
<b>Department Table:</b>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| dept_id     | int     |
| dept_name   | varchar |
+-------------+---------+

<b>Student Table:</b>
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| student_name | varchar |
| gender       | varchar |
| dept_id      | int     |
+--------------+---------+
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
Department Table:
1,Engineering
2,Science
3,Law
---
Student Table:
1,Jack,M,1
2,Jane,F,1
3,Mark,M,2

<strong>Output:</strong> 
Engineering 2
Science 1
Law 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of departments is in the range <code>[1, 1000]</code>.</li>
	<li>The number of students is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li>Department IDs and Student IDs are unique within their tables.</li>
</ul>"""

    input_format = "Lines for the Department table (dept_id,dept_name), a '---' separator, and lines for the Student table (student_id,student_name,gender,dept_id)."
    output_format = "Each line contains 'dept_name student_count', sorted by count DESC then name ASC."
    
    constraints = [
        "1 <= departments <= 1000",
        "0 <= students <= 10^4",
        "Include all departments (even with 0 students).",
        "O(S + D log D) time complexity.",
        "O(S + D) extra space."
    ]
    
    explanation = """To count students per department and sort the results:
1. **Hash Map for Counting**:
   - Iterate through the `student` table.
   - For each student, increment the count for their `dept_id` in a frequency map (dictionary). 
2. **Left Join with Departments**:
   - Iterate through the `department` table.
   - For each department, look up its student count from the frequency map. If the ID is not found, the count is 0.
3. **Sorting**:
   - Store the results as pairs of `(dept_name, student_count)`.
   - Sort these pairs primarily by `student_count` in descending order.
   - Use `dept_name` as the secondary key in ascending order for ties.
4. **Complexity**:
   - Time Complexity: O(S + D log D), where S is the number of students and D is the number of departments (sorting dominates D).
   - Space Complexity: O(S + D) to store input data and counts."""
    
    answer = """from collections import Counter
def countStudents(departments: list[tuple], students: list[tuple]) -> list[tuple]:
    # students: [(id, name, gender, dept_id), ...]
    # departments: [(dept_id, name), ...]
    counts = Counter(s[3] for s in students)
    
    res = []
    for d_id, d_name in departments:
        res.append((d_name, counts[d_id]))
        
    res.sort(key=lambda x: (-x[1], x[0]))
    return res"""

    boilerplate = {
        "python": "import sys\nfrom collections import Counter\n\ndef countStudents(departments, students):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip().split('\\n---\\n')\n    if len(input_data) == 2:\n        dept_lines = input_data[0].splitlines()\n        stud_lines = input_data[1].splitlines()\n        depts = [tuple(line.split(',')) for line in dept_lines if line]\n        # Map dept_id to int\n        depts = [(int(d[0]), d[1]) for d in depts]\n        studs = [tuple(line.split(',')) for line in stud_lines if line]\n        studs = [(int(s[0]), s[1], s[2], int(s[3])) for s in studs]\n        \n        res = countStudents(depts, studs)\n        for name, count in res:\n            print(f\"{name} {count}\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n#include <algorithm>\n\nusing namespace std;\n\nstruct Dept { int id; string name; };\nstruct Stud { int id; string name; string gender; int dept_id; };\n\nvoid solve() {\n    // User logic\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        // User logic\n    }\n}",
        "javascript": "function solve(departments, students) {\n    // User logic\n}",
        "c": "void solve() {\n    // User logic\n}"
    }

    test_cases = [
        {"input": "1,Engineering\\n2,Science\\n3,Law\\n---\\n1,Jack,M,1\\n2,Jane,F,1\\n3,Mark,M,2", "expected_output": "Engineering 2\\nScience 1\\nLaw 0", "is_sample": True},
        {"input": "10,Arts\\n---\\n", "expected_output": "Arts 0", "is_sample": True},
        {"input": "1,D1\\n2,D2\\n---\\n1,S1,M,1\\n2,S2,M,2", "expected_output": "D1 1\\nD2 1", "is_sample": False},
        {"input": "1,A1\\n2,A2\\n---\\n1,S1,M,2", "expected_output": "A2 1\\nA1 0", "is_sample": False},
        {"input": "1,Z_Dept\\n2,A_Dept\\n---\\n1,S1,M,1\\n2,S2,M,2", "expected_output": "A_Dept 1\\nZ_Dept 1", "is_sample": False},
        {"input": "1,D1\\n2,D2\\n3,D3\\n---\\n1,S1,M,1\\n2,S2,M,1\\n3,S3,M,1", "expected_output": "D1 3\\nD2 0\\nD3 0", "is_sample": False},
        {"input": "1,D1\\n2,D2\\n3,D3\\n---\\n1,S1,M,2\\n2,S2,M,2\\n3,S3,M,3", "expected_output": "D2 2\\nD3 1\\nD1 0", "is_sample": False},
        # Stress cases
        {"input": "\\n".join([f"{i},Dept{i}" for i in range(1, 1001)]) + "\\n---\\n", "expected_output": "\\n".join([f"Dept{i} 0" for i in range(1, 1001)]), "is_sample": False},
        {"input": "1,D1\\n---\\n" + "\\n".join([f"{i},S{i},M,1" for i in range(1, 10001)]), "expected_output": "D1 10000", "is_sample": False},
        {"input": "1,X1\\n2,X2\\n---\\n1,S1,M,1\\n2,S2,M,2\\n3,S3,M,1", "expected_output": "X1 2\\nX2 1", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Sorting"],
        "companyIndex": 0
    }

    output_path = "401-600/580_Count_Student_Number_in_Departments.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
