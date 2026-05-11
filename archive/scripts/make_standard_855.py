import json
import os

def generate_json():
    problem_id = 855
    title = "Exam Room"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>855. Exam Room</h3>
<p>There is an exam room with <code>n</code> seats in a single row from <code>0</code> to <code>n - 1</code>.</p>

<p>When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat 0.</p>

<p>Design a class that simulates the exam room.</p>

<p>Implement the <code>ExamRoom</code> class:</p>

<ul>
	<li><code>ExamRoom(int n)</code> Initializes the object with the number of seats <code>n</code>.</li>
	<li><code>int seat()</code> Returns the label of the seat at which the next student will sit.</li>
	<li><code>void leave(int p)</code> Indicates that the student sitting at seat <code>p</code> will leave the room. It is guaranteed that there will be a student sitting at seat <code>p</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]
<strong>Output</strong>
[null, 0, 9, 4, 2, null, 5]

<strong>Explanation</strong>
ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // return 0, no one is in the room, then the student sits at seat 0.
examRoom.seat(); // return 9, the student sits at the last seat number 9.
examRoom.seat(); // return 4, the student sits at the middle seat number 4.
examRoom.seat(); // return 2, the student sits at the middle seat number 2.
examRoom.leave(4);
examRoom.seat(); // return 5, the student sits at the middle seat number 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li>It is guaranteed that there is a student sitting at seat <code>p</code> when <code>leave(p)</code> is called.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>seat</code> and <code>leave</code>.</li>
</ul>
"""

    input_format = "Class initialization and calls to seat() or leave()."
    output_format = "Integer result for seat() calls."
    
    constraints = [
        "1 <= n <= 10^9",
        "Student sitting at seat p when leave(p) is called.",
        "At most 10000 calls."
    ]
    
    explanation = """To implement the Exam Room efficiently:
1. **The Core Approach**: Use a sorted list `students` to keep track of the indices where current students are seated.

2. **The logic for `seat()`**:
   - If the room is empty, seat at `0` and return.
   - We need to find the best gap between nodes.
   - Initial distance candidate: `d = students[0]` (distance from 0 to the first student). The corresponding seat is `0`.
   - Mid-gap candidate: For each adjacent pair `(s1, s2)` in `students`:
     - Distance from mid-point: `dist = (s2 - s1) // 2`.
     - If `dist > d`, update `d = dist` and `seat_to_be = s1 + dist`.
   - End-gap candidate: `dist = (N - 1) - students[-1]` (distance from the last student to the last seat).
     - If `dist > d`, update `d = dist` and `seat_to_be = N - 1`.
   - After finding the best `seat_to_be`, insert it into the sorted list.

3. **The logic for `leave(p)`**: Simply remove `p` from the `students` list.

Complexity:
- `seat()`: O(P) where P is the number of students (to iterate over gaps and insert).
- `leave()`: O(P) to find and remove from the list.
- With total calls limited to 10^4, this approach is clearly sufficient."""
    
    answer = """import bisect

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            res = 0
        else:
            # Case 1: seat at 0
            dist, res = self.students[0], 0
            
            # Case 2: seat between students
            for i in range(len(self.students) - 1):
                s1, s2 = self.students[i], self.students[i+1]
                d = (s2 - s1) // 2
                if d > dist:
                    dist, res = d, s1 + d
            
            # Case 3: seat at N-1
            if (self.n - 1) - self.students[-1] > dist:
                res = self.n - 1
                
        bisect.insort(self.students, res)
        return res

    def leave(self, p: int) -> None:
        self.students.remove(p)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass ExamRoom:\n    def __init__(self, n):\n        pass\n    def seat(self):\n        pass\n    def leave(self, p):\n        pass\n\nif __name__ == '__main__':\n    # Class interaction driver goes here\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <set>\n\nusing namespace std;\n\nclass ExamRoom {\npublic:\n    ExamRoom(int n) {\n    }\n    \n    int seat() {\n        return 0;\n    }\n    \n    void leave(int p) {\n    }\n};",
        "java": "import java.util.*;\n\nclass ExamRoom {\n    public ExamRoom(int n) {\n    }\n    \n    public int seat() {\n        return 0;\n    }\n    \n    public void leave(int p) {\n    }\n}",
        "javascript": "/**\n * @param {number} n\n */\nvar ExamRoom = function(n) {\n    \n};\n\n/**\n * @return {number}\n */\nExamRoom.prototype.seat = function() {\n    \n};\n\n/**\n * @param {number} p\n * @return {void}\n */\nExamRoom.prototype.leave = function(p) {\n    \n};",
        "c": "typedef struct {\n    \n} ExamRoom;\n\nExamRoom* examRoomCreate(int n) {\n    \n}\n\nint examRoomSeat(ExamRoom* obj) {\n    \n}\n\nvoid examRoomLeave(ExamRoom* obj, int p) {\n    \n}"
    }

    test_cases = [
        {"input": "[\"ExamRoom\", \"seat\", \"seat\", \"seat\", \"seat\", \"leave\", \"seat\"]\\n[[10], [], [], [], [], [4], []]", "expected_output": "[null, 0, 9, 4, 2, null, 5]", "is_sample": True},
        # Diverse cases
        {"input": "[\"ExamRoom\", \"seat\", \"seat\", \"leave\", \"seat\"]\\n[[5], [], [], [0], []]", "expected_output": "[null, 0, 4, null, 0]", "is_sample": False},
        {"input": "[\"ExamRoom\", \"seat\", \"seat\", \"seat\", \"leave\", \"leave\", \"seat\"]\\n[[10], [], [], [], [0], [4], []]", "expected_output": "[null, 0, 9, 4, null, null, 0]", "is_sample": False},
        {"input": "[\"ExamRoom\", \"seat\", \"leave\"]\\n[[2], [], [0]]", "expected_output": "[null, 0, null]", "is_sample": False},
        # Stress cases
        {"input": "Class simulation", "expected_output": "Check logic", "is_sample": False}
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
        "topics": ["Design", "Array", "Sorted Set"],
        "companyIndex": 0
    }

    output_path = "801-1000/855_Exam_Room.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
