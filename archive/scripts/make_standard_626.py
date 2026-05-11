import json
import os

def generate_json():
    problem_id = 626
    title = "Exchange Seats"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>626. Exchange Seats</h3>
<p>Table: <code>Seat</code></p>
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a student.
The id sequence is a continuous incrementing sequence starting from 1.
</pre>

<p>Write a solution to swap the seat <code>id</code> of every two consecutive students. If the number of students is odd, the <code>id</code> of the last student is not swapped.</p>

<p>Return the result table ordered by <code>id</code> in <b>ascending order</b>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
1,Abbot
2,Doris
3,Emerson
4,Green
5,Jeames

<strong>Output:</strong> 
1 Doris
2 Abbot
3 Green
4 Emerson
5 Jeames

<strong>Explanation:</strong> 
Note that if the number of students is odd, there is no need to change the last one's seat.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of students is in the range <code>[1, 1000]</code>.</li>
</ul>"""

    input_format = "Each line contains a record: 'id,student'."
    output_format = "Each line contains 'id student' sorted by id."
    
    constraints = [
        "1 <= n_students <= 1000",
        "Swap consecutive students (1-2, 3-4, etc.)",
        "Last student in an odd list stays put.",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To exchange seats for consecutive students:
1. **The Logic**:
   - We are given a list of students with IDs $1, 2, 3, \dots, N$.
   - We need to swap the names of student 1 with student 2, student 3 with student 4, etc.
   - If $N$ is odd, the $N$-th student remains in their original seat.
2. **Implementation**:
   - Read all students into a list.
   - Iterate through the list with a step of 2 ($i = 0, 2, 4, \dots$).
   - If there is a next student ($i+1 < N$), swap `students[i]` and `students[i+1]`.
   - Output the modified list with incrementing IDs.
3. **Complexity**:
   - Time Complexity: O(N) to process the list once.
   - Space Complexity: O(N) to store the input students before swapping."""
    
    answer = """def exchangeSeats(seats: list[str]) -> list[str]:
    n = len(seats)
    for i in range(0, n - 1, 2):
        seats[i], seats[i+1] = seats[i+1], seats[i]
    return seats"""

    boilerplate = {
        "python": "import sys\n\ndef exchangeSeats(seats):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    students = []\n    for line in lines:\n        if not line: continue\n        parts = line.split(',')\n        students.append(parts[1])\n    res = exchangeSeats(students)\n    for i, s in enumerate(res, 1):\n        print(f\"{i} {s}\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        // User logic\n    }\n}",
        "javascript": "function solve(seats) {\n    // User logic\n}",
        "c": "void solve() {\n    // User logic\n}"
    }

    test_cases = [
        {"input": "1,Abbot\\n2,Doris\\n3,Emerson\\n4,Green\\n5,Jeames", "expected_output": "1 Doris\\n2 Abbot\\n3 Green\\n4 Emerson\\n5 Jeames", "is_sample": True},
        {"input": "1,A\\n2,B", "expected_output": "1 B\\n2 A", "is_sample": True},
        {"input": "1,Alone", "expected_output": "1 Alone", "is_sample": False},
        {"input": "1,A\\n2,B\\n3,C", "expected_output": "1 B\\n2 A\\n3 C", "is_sample": False},
        {"input": "1,A\\n2,B\\n3,C\\n4,D", "expected_output": "1 B\\n2 A\\n3 D\\n4 C", "is_sample": False},
        {"input": "1,First\\n2,Second\\n3,Third\\n4,Fourth\\n5,Fifth\\n6,Sixth", "expected_output": "1 Second\\n2 First\\n3 Fourth\\n4 Third\\n5 Sixth\\n6 Fifth", "is_sample": False},
        {"input": "1,X\\n2,Y\\n3,Z", "expected_output": "1 Y\\n2 X\\n3 Z", "is_sample": False},
        # Stress cases
        {"input": "\\n".join([f"{i},Stud{i}" for i in range(1, 1001)]), "expected_output": "\\n".join([f"{i} Stud{i+1}" if i%2!=0 else f"{i} Stud{i-1}" for i in range(1, 1001)]), "is_sample": False},
        {"input": "\\n".join([f"{i},Stud{i}" for i in range(1, 1000)]), "expected_output": "...", "is_sample": False},
        {"input": "1,Alpha\\n2,Beta", "expected_output": "1 Beta\\n2 Alpha", "is_sample": False}
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

    output_path = "601-800/626_Exchange_Seats.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
