import json
import os

def generate_json():
    problem_id = 570
    title = "Managers with at Least 5 Direct Reports"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>570. Managers with at Least 5 Direct Reports</h3>
<p>Table: <code>Employee</code></p>
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themselves.
</pre>

<p>Write a solution to find the names of the managers who have at least **five** direct reports.</p>
<p>Return the result table in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | None      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
<strong>Output:</strong> 
+------+
| name |
+------+
| John |
+------+
</pre>
"""

    input_format = "A list of employee records (e.g., [[101, 'John', 'A', None], ...])."
    output_format = "A list of names of managers."
    
    constraints = [
        "The number of rows is in the range [1, 500].",
        "No employee is their own manager.",
        "managerId may be null."
    ]
    
    explanation = """To find managers with at least 5 reports:
1. Count direct reports for each `managerId` in the `Employee` table.
2. Filter those `managerId`s that have a count of 5 or more.
3. Join the filtered IDs back to the `Employee` table (on `id`) to get the managers' names."""
    
    answer = """def findManagers(employees):
    # employees is list of [id, name, department, managerId]
    report_counts = {}
    for _, _, _, managerId in employees:
        if managerId is not None:
            report_counts[managerId] = report_counts.get(managerId, 0) + 1
            
    # Filter managers with count >= 5
    manager_ids = {m_id for m_id, count in report_counts.items() if count >= 5}
    
    # Get names
    res = []
    for emp_id, name, _, _ in employees:
        if emp_id in manager_ids:
            res.append(name)
    return res"""

    boilerplate = {
        "python": "import sys\\n\\ndef findManagers(employees):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    # Custom input handler\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <string>\\n#include <unordered_map>\\n\\nusing namespace std;\\n\\nclass Solution { public: vector<string> findManagers(vector<vector<string>>& employee) { return {}; } };",
        "java": "class Solution { public List<String> findManagers(List<List<String>> employee) { return new ArrayList<>(); } }",
        "javascript": "const fs = require('fs');",
        "c": "char** findManagers(char*** employee, int employeeSize, int* employeeColSize, int* returnSize){ }"
    }

    test_cases = [
        {"input": "101,John,A,None\\n102,Dan,A,101\\n103,James,A,101\\n104,Amy,A,101\\n105,Anne,A,101\\n106,Ron,B,101", "expected_output": "['John']", "is_sample": True},
        {"input": "1,Alice,D,None\\n2,Bob,D,1\\n3,Charlie,D,1\\n4,David,D,1\\n5,Eve,D,1\\n6,Frank,D,1", "expected_output": "['Alice']", "is_sample": False},
        {"input": "1,A,D,None\\n2,B,D,1\\n3,C,D,1", "expected_output": "[]", "is_sample": False},
        {"input": "101,John,A,None", "expected_output": "[]", "is_sample": False},
        {"input": "1,M1,D,None\\n2,M2,D,None\\n3,E1,D,1\\n4,E2,D,1\\n5,E3,D,1\\n6,E4,D,1\\n7,E5,D,1\\n8,E6,D,2\\n9,E7,D,2\\n10,E8,D,2\\n11,E9,D,2\\n12,E10,D,2", "expected_output": "['M1', 'M2']", "is_sample": False},
        {"input": "1,A,D,None\\n2,B,D,None\\n3,C,D,None\\n4,D,D,None\\n5,E,D,None\\n6,F,D,1\\n7,G,D,1\\n8,H,D,1\\n9,I,D,1\\n10,J,D,1", "expected_output": "['A']", "is_sample": False},
        {"input": "1,A,D,None\\n2,B,D,1\\n3,C,D,1\\n4,D,D,1\\n5,E,D,1\\n6,F,D,1\\n7,G,D,2\\n8,H,D,2\\n9,I,D,2\\n10,J,D,2\\n11,K,D,2", "expected_output": "['A', 'B']", "is_sample": False},
        {"input": "1,A,D,None\\n2,B,D,1\\n3,C,D,1\\n4,D,D,1\\n5,E,D,1\\n6,F,A,1", "expected_output": "['A']", "is_sample": False},
        {"input": "1,A,D,None\\n2,B,D,10\\n3,C,D,10", "expected_output": "[]", "is_sample": False},
        {"input": "10,Boss,X,None\\n1,A,D,10\\n2,B,D,10\\n3,C,D,10\\n4,D,D,10\\n5,E,D,10", "expected_output": "['Boss']", "is_sample": False}
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
        "topics": ["Database", "SQL"],
        "companyIndex": 0
    }

    output_path = "401-600/570_Managers_with_at_Least_5_Direct_Reports.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
