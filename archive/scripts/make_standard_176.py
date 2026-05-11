import json
import os

def generate_json():
    problem_id = 176
    title = "Second Highest Salary"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>176. Second Highest Salary</h3>
<p>Table: <code>Employee</code></p>
<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
</pre>

<p>Write a solution to find the second highest salary from the <code>Employee</code> table. If there is no second highest salary, return <code>null</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
<strong>Output:</strong> 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
<strong>Output:</strong> 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
</pre>"""

    input_format = "JSON containing 'Employee' table as a list of records."
    output_format = "A single record with the field 'SecondHighestSalary'."
    
    constraints = [
        "id is the primary key.",
        "Must handle cases with fewer than 2 distinct salaries by returning null.",
        "Must handle duplicates (find second highest DISTINCT salary)."
    ]
    
    explanation = """To find the second highest distinct salary:
1. **Distinct Salaries**: We need to unique values since multiple employees might have the same highest salary.
2. **Sorting**: Sort the distinct salaries in descending order.
3. **Offset**: Use `LIMIT 1 OFFSET 1` to skip the highest and take the second highest.
4. **Null Handling**: Wrapping the query in a subquery or using `IFNULL` ensures that if no second salary exists (e.g., table has 1 row), the result is `null`.
5. **Alternative Approach**: 
   ```sql
   SELECT MAX(salary) AS SecondHighestSalary
   FROM Employee
   WHERE salary < (SELECT MAX(salary) FROM Employee);
   ```"""
    
    answer = """SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);"""

    boilerplate = {
        "python": "# SQL Problem: Use the query provided.\nimport pandas as pd\n\ndef second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:\n    unique_salaries = employee['salary'].unique()\n    if len(unique_salaries) < 2:\n        return pd.DataFrame({'SecondHighestSalary': [None]})\n    unique_salaries.sort()\n    return pd.DataFrame({'SecondHighestSalary': [unique_salaries[-2]]})"
    }

    test_cases = [
        {"input": '{"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}]}', "expected_output": '{"SecondHighestSalary": 200}', "is_sample": True},
        {"input": '{"Employee": [{"id": 1, "salary": 100}]}', "expected_output": '{"SecondHighestSalary": null}', "is_sample": True},
        {"input": '{"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 100}]}', "expected_output": '{"SecondHighestSalary": null}', "is_sample": False},
        {"input": '{"Employee": [{"id": 1, "salary": 500}, {"id": 2, "salary": 400}, {"id": 3, "salary": 500}]}', "expected_output": '{"SecondHighestSalary": 400}', "is_sample": False},
        {"input": '{"Employee": [{"id": 1, "salary": 10}, {"id": 2, "salary": 20}, {"id": 3, "salary": 30}, {"id": 4, "salary": 40}]}', "expected_output": '{"SecondHighestSalary": 30}', "is_sample": False},
        {"input": '{"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 100}, {"id": 3, "salary": 100}]}', "expected_output": '{"SecondHighestSalary": null}', "is_sample": False},
        {"input": '{"Employee": []}', "expected_output": '{"SecondHighestSalary": null}', "is_sample": False},
        # Stress Tests
        {"input": '{"Employee": [{"id": i, "salary": i} for i in range(1000)]}', "expected_output": '{"SecondHighestSalary": 998}', "is_sample": False},
        {"input": '{"Employee": [{"id": i, "salary": 1000} for i in range(1000)]}', "expected_output": '{"SecondHighestSalary": null}', "is_sample": False},
        {"input": '{"Employee": [{"id": i, "salary": 5000 if i%2==0 else 4000} for i in range(1000)]}', "expected_output": '{"SecondHighestSalary": 4000}', "is_sample": False}
    ]

    for i in [7, 8, 9]:
        test_cases[i]["input"] = json.dumps(eval(test_cases[i]["input"]))

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
            "allowed_languages": ["sql"]
        },
        "topics": ["Database"],
        "companyIndex": 0
    }

    output_path = "1-200/176_Second_Highest_Salary.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
