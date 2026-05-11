import json
import os
import bisect

def generate_json():
    problem_id = 729
    title = "My Calendar I"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>729. My Calendar I</h3>
<p>You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a <b>double booking</b>.</p>
<p>A <b>double booking</b> happens when two events have some non-empty intersection (i.e., some moment is common to both events.).</p>
<p>The event can be represented as a pair of integers <code>start</code> and <code>end</code> that represents a booking on the half-open interval <code>[start, end)</code>, the range of real numbers <code>x</code> such that <code>start &lt;= x &lt; end</code>.</p>
<p>Implement the <code>MyCalendar</code> class:</p>
<ul>
	<li><code>MyCalendar()</code> Initializes the calendar object.</li>
	<li><code>boolean book(int start, int end)</code> Returns <code>true</code> if the event can be added to the calendar successfully without causing a <b>double booking</b>. Otherwise, return <code>false</code> and do not add the event to the calendar.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
<strong>Output:</strong>
[null, true, false, true]

<strong>Explanation:</strong>
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event ends at 20, and does not include it.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= start &lt; end &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>1000</code> calls will be made to <code>book</code>.</li>
</ul>
"""

    input_format = "Two lines:\\n1. List of operations\\n2. List of arguments"
    output_format = "List of return values."
    
    constraints = [
        "0 <= start < end <= 10^9",
        "Operations limit: 1000 calls.",
        "No overlapping intervals allowed."
    ]
    
    explanation = """To implement My Calendar I:
1. **Sorted Structure**: Keep a list of intervals sorted by start time: `self.calendar = []`.
2. **Binary Search**: For a new request `[start, end)`:
   - Find the position `idx` where `start` would be inserted using `bisect_left`.
3. **Collision Detection**:
   - Check if the previous event `idx-1` overlaps: `calendar[idx-1][1] > start`.
   - Check if the next event `idx` overlaps: `calendar[idx][0] < end`.
4. **Insertion**: If no collision, insert `[start, end]` at `idx`.

Complexity:
- Time: O(N log N) total for N bookings (O(log N) search + O(N) array shifts in Python).
- Space: O(N) to store intervals.
"""
    
    answer = """import bisect
class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_left(self.calendar, (start, end))
        
        if idx > 0 and self.calendar[idx-1][1] > start:
            return False
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False
            
        self.calendar.insert(idx, (start, end))
        return True"""

    boilerplate = {
        "python": "import sys\\nimport json\\nimport bisect\\n\\nclass MyCalendar:\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    input_data = sys.stdin.read().splitlines()\\n    ops = json.loads(input_data[0])\\n    args = json.loads(input_data[1])\\n    # Orchestrator...\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <set>\\nusing namespace std;\\n\\nclass MyCalendar { public: bool book(int start, int end) { return false; } };",
        "java": "public class Main { public static void main(String[] args) { } }",
        "javascript": "const fs = require('fs');",
        "c": "typedef struct { } MyCalendar; MyCalendar* myCalendarCreate() { }"
    }

    test_cases = [
        {"input": '["MyCalendar", "book", "book", "book"]\\n[[], [10, 20], [15, 25], [20, 30]]', "expected_output": "[null, true, false, true]", "is_sample": True},
        {"input": '["MyCalendar", "book", "book"]\\n[[], [1, 5], [5, 10]]', "expected_output": "[null, true, true]", "is_sample": False},
        {"input": '["MyCalendar", "book", "book"]\\n[[], [1, 10], [2, 3]]', "expected_output": "[null, true, false]", "is_sample": False},
        {"input": '["MyCalendar", "book", "book"]\\n[[], [5, 10], [1, 6]]', "expected_output": "[null, true, false]", "is_sample": False},
        {"input": '["MyCalendar", "book", "book"]\\n[[], [10, 20], [0, 5]]', "expected_output": "[null, true, true]", "is_sample": False},
        {"input": '["MyCalendar", "book", "book", "book"]\\n[[], [10, 20], [0, 10], [20, 30]]', "expected_output": "[null, true, true, true]", "is_sample": False},
        {"input": '["MyCalendar", "book", "book"]\\n[[], [10, 20], [10, 20]]', "expected_output": "[null, true, false]", "is_sample": False},
        {"input": '["MyCalendar", "book", "book", "book"]\\n[[], [47, 50], [33, 41], [39, 45]]', "expected_output": "[null, true, true, false]", "is_sample": False},
        # Stress cases
        {"input": '["MyCalendar"] + ["book"]*500\\n[...]', "expected_output": "[null] + [true]*500", "is_sample": False},
        {"input": '["MyCalendar"] + ["book"]*500\\n[... overlapping]', "expected_output": "[null, true] + [false]*499", "is_sample": False}
    ]
    
    # Specific stress inputs
    test_cases[8]["input"] = json.dumps(["MyCalendar"] + ["book"] * 499) + "\\n" + json.dumps([[]] + [[i*10, i*10+5] for i in range(499)])
    test_cases[9]["input"] = json.dumps(["MyCalendar"] + ["book"] * 499) + "\\n" + json.dumps([[]] + [[10, 20]] * 499)

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
        "topics": ["Design", "Segment Tree", "Ordered Set"],
        "companyIndex": 0
    }

    output_path = "601-800/729_My_Calendar_I.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
