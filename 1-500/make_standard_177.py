import json
import os

def generate_json():
    problem_id = 177
    title = "Nth Highest Salary"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>177. Nth Highest Salary</h3>
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

<p>Write a solution to find the <code>n<sup>th</sup></code> highest salary from the <code>Employee</code> table. If there is no <code>n<sup>th</sup></code> highest salary, return <code>null</code>.</p>

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
n = 2
<strong>Output:</strong> 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
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
n = 2
<strong>Output:</strong> 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
</pre>"""

    input_format = "JSON containing 'Employee' table and an integer 'n'."
    output_format = "A single record with the field 'getNthHighestSalary(n)'."
    
    constraints = [
        "id is the primary key.",
        "Must handle duplicates (find nth highest DISTINCT salary).",
        "Must return null if nth highest salary doesn't exist.",
        "n is a positive integer."
    ]
    
    explanation = """To find the nth highest distinct salary:
1. **Sorted Distinct Values**: Filter unique salaries and sort them in descending order.
2. **Limit and Offset**: Use `LIMIT 1 OFFSET n-1` to skip the top `n-1` salaries and pick the `n`th one.
3. **Variable Offset**: In SQL, the `OFFSET` parameter must be a non-negative integer. Since we receive `n`, we calculate `m = n - 1` and use it.
4. **Function Definition**: This logic is typically wrapped in a SQL function.
5. **Alternative Approach**: Using `DENSE_RANK()` window function.
   ```sql
   CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
   BEGIN
     SET N = N - 1;
     RETURN (
         SELECT DISTINCT salary
         FROM Employee
         ORDER BY salary DESC
         LIMIT 1 OFFSET N
     );
   END
   ```"""
    
    answer = """CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
  );
END"""

    boilerplate = {
        "python": "# SQL Function Problem: Use the query provided.\nimport pandas as pd\n\ndef nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:\n    unique_salaries = employee['salary'].unique()\n    if len(unique_salaries) < n or n < 1:\n        return pd.DataFrame({f'getNthHighestSalary({n})': [None]})\n    unique_salaries.sort()\n    return pd.DataFrame({f'getNthHighestSalary({n})': [unique_salaries[-n]]})"
    }

    test_cases = [
        {"input": '{"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}], "n": 2}', "expected_output": '{"getNthHighestSalary(2)": 200}', "is_sample": True},
        {"input": '{"Employee": [{"id": 1, "salary": 100}], "n": 2}', "expected_output": '{"getNthHighestSalary(2)": null}', "is_sample": True},
        {"input": '{"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 100}], "n": 1}', "expected_output": '{"getNthHighestSalary(1)": 100}', "is_sample": False},
        {"input": '{"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 100}], "n": 2}', "expected_output": '{"getNthHighestSalary(2)": null}', "is_sample": False},
        {"input": '{"Employee": [{"id": 1, "salary": 500}, {"id": 2, "salary": 400}, {"id": 3, "salary": 600}], "n": 3}', "expected_output": '{"getNthHighestSalary(3)": 400}', "is_sample": False},
        {"input": '{"Employee": [{"id": i, "salary": i*10} for i in range(1, 11)], "n": 10}', "expected_output": '{"getNthHighestSalary(10)": 10}', "is_sample": False},
        {"input": '{"Employee": [], "n": 1}', "expected_output": '{"getNthHighestSalary(1)": null}', "is_sample": False},
        # Stress Tests
        {"input": '{"Employee": [{"id": i, "salary": i} for i in range(1000)], "n": 500}', "expected_output": '{"getNthHighestSalary(500)": 500}', "is_sample": False},
        {"input": '{"Employee": [{"id": i, "salary": 1000} for i in range(1000)], "n": 2}', "expected_output": '{"getNthHighestSalary(2)": null}', "is_sample": False},
        {"input": '{"Employee": [{"id": i, "salary": i if i!=999 else 0} for i in range(1000)], "n": 1000}', "expected_output": '{"getNthHighestSalary(1000)": 0}', "is_sample": False}
    ]

    for i in [5, 7, 8, 9]:
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

    output_path = "1-200/177_Nth_Highest_Salary.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
