import json
import os

def generate_json():
    problem_id = 731
    title = "My Calendar II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>731. My Calendar II</h3>
<p>You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a <b>triple booking</b>.</p>
<p>A <b>triple booking</b> happens when <b>three</b> events have some non-empty intersection (i.e., some moment is common to all three events.).</p>
<p>The event can be represented as a pair of integers <code>start</code> and <code>end</code> that represents a booking on the half-open interval <code>[start, end)</code>, the range of real numbers <code>x</code> such that <code>start &lt;= x &lt; end</code>.</p>
<p>Implement the <code>MyCalendarTwo</code> class:</p>
<ul>
	<li><code>MyCalendarTwo()</code> Initializes the calendar object.</li>
	<li><code>boolean book(int start, int end)</code> Returns <code>true</code> if the event can be added to the calendar successfully without causing a <b>triple booking</b>. Otherwise, return <code>false</code> and do not add the event to the calendar.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
<strong>Output:</strong>
[null, true, true, true, false, true, true]

<strong>Explanation:</strong>
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True
myCalendarTwo.book(50, 60); // return True
myCalendarTwo.book(10, 40); // return True, The event can be double booked.
myCalendarTwo.book(5, 15);  // return False, It can not be booked because it would result in a triple booking.
myCalendarTwo.book(5, 10);  // return True, It can be booked, as it doesn't double book with [10, 20] or [10, 40].
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
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
        "No triple booking allowed."
    ]
    
    explanation = """To implement My Calendar II:
1. **Maintain Two Lists**:
   - `self.calendar`: Stores all accepted single events.
   - `self.overlaps`: Stores all intersections between existing single events (double bookings).
2. **Handle Booking** `[s, e)`:
   - Check if `[s, e)` overlaps with any interval in `self.overlaps`. If it does, return `False` (would cause a triple booking).
   - If no triple booking:
     - For every event `[cs, ce)` in `self.calendar`, find the intersection: `start = max(s, cs)`, `end = min(e, ce)`.
     - If `start < end`, add `[start, end]` to `self.overlaps`.
     - Add `[s, e]` to `self.calendar`.
3. **Complexity**:
   - N calls, each checking existing N events.
   - Total time: O(N^2). Since N=1000, N^2 = 1M, which is efficient enough.

Complexity:
- Time: O(N^2) total for N bookings.
- Space: O(N) to store intervals.
"""
    
    answer = """class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))
        
        self.calendar.append((start, end))
        return True"""

    boilerplate = {
        "python": "import sys\\nimport json\\n\\nclass MyCalendarTwo:\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    input_data = sys.stdin.read().splitlines()\\n    ops = json.loads(input_data[0])\\n    args = json.loads(input_data[1])\\n    # Orchestrator...\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\nusing namespace std;\\n\\nclass MyCalendarTwo { public: bool book(int start, int end) { return false; } };",
        "java": "public class Main { public static void main(String[] args) { } }",
        "javascript": "const fs = require('fs');",
        "c": "typedef struct { } MyCalendarTwo; MyCalendarTwo* myCalendarTwoCreate() { }"
    }

    test_cases = [
        {"input": '["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]\\n[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]', "expected_output": "[null, true, true, true, false, true, true]", "is_sample": True},
        {"input": '["MyCalendarTwo", "book", "book", "book"]\\n[[], [1, 10], [1, 10], [1, 10]]', "expected_output": "[null, true, true, false]", "is_sample": False},
        {"input": '["MyCalendarTwo", "book", "book", "book"]\\n[[], [1, 10], [5, 15], [6, 7]]', "expected_output": "[null, true, true, false]", "is_sample": False},
        {"input": '["MyCalendarTwo", "book", "book", "book"]\\n[[], [1, 10], [5, 15], [10, 20]]', "expected_output": "[null, true, true, true]", "is_sample": False},
        {"input": '["MyCalendarTwo", "book", "book", "book"]\\n[[], [10, 20], [50, 60], [10, 60]]', "expected_output": "[null, true, true, true]", "is_sample": False},
        {"input": '["MyCalendarTwo", "book", "book", "book", "book"]\\n[[], [10, 20], [10, 20], [15, 25], [15, 25]]', "expected_output": "[null, true, true, false, false]", "is_sample": False},
        {"input": '["MyCalendarTwo", "book", "book"]\\n[[], [0, 1000000000], [0, 1000000000]]', "expected_output": "[null, true, true]", "is_sample": False},
        {"input": '["MyCalendarTwo", "book", "book", "book"]\\n[[], [10, 20], [20, 30], [30, 40]]', "expected_output": "[null, true, true, true]", "is_sample": False},
        # Stress cases
        {"input": '["MyCalendarTwo"] + ["book"]*500\\n[...]', "expected_output": "[null] + [true]*500", "is_sample": False},
        {"input": '["MyCalendarTwo"] + ["book"]*500\\n[... triple overlaps]', "expected_output": "[null, true, true] + [false]*498", "is_sample": False}
    ]
    
    # Specific stress inputs
    test_cases[8]["input"] = json.dumps(["MyCalendarTwo"] + ["book"] * 499) + "\\n" + json.dumps([[]] + [[i*10, i*10+5] for i in range(499)])
    test_cases[9]["input"] = json.dumps(["MyCalendarTwo"] + ["book"] * 499) + "\\n" + json.dumps([[]] + [[10, 20]] * 499)

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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Design", "Segment Tree", "Ordered Set"],
        "companyIndex": 0
    }

    output_path = "601-800/731_My_Calendar_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
