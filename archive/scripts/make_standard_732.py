import json
import os
import collections

def generate_json():
    problem_id = 732
    title = "My Calendar III"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>732. My Calendar III</h3>
<p>A <code>k</code>-booking happens when <code>k</code> events have some non-empty intersection (i.e., there is some time that is common to all <code>k</code> events.)</p>
<p>You are given some events <code>[start, end)</code>, after each given event, return an integer <code>k</code> representing the maximum <code>k</code>-booking existing in the calendar.</p>
<p>Implement the <code>MyCalendarThree</code> class:</p>
<ul>
	<li><code>MyCalendarThree()</code> Initializes the object.</li>
	<li><code>int book(int start, int end)</code> Returns an integer <code>k</code> representing the largest integer such that there exists a <code>k</code>-booking in the calendar.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
<strong>Output:</strong>
[null, 1, 1, 2, 3, 3, 3]

<strong>Explanation:</strong>
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1
myCalendarThree.book(50, 60); // return 1
myCalendarThree.book(10, 40); // return 2
myCalendarThree.book(5, 15);  // return 3
myCalendarThree.book(5, 10);  // return 3
myCalendarThree.book(25, 55); // return 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= start &lt; end &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>400</code> calls will be made to <code>book</code>.</li>
</ul>
"""

    input_format = "Two lines:\\n1. List of operations\\n2. List of arguments"
    output_format = "List of return values."
    
    constraints = [
        "0 <= start < end <= 10^9",
        "Operations limit: 400 calls.",
        "Must return max k-booking after each call."
    ]
    
    explanation = """To implement My Calendar III:
1. **Sweep-Line Algorithm**: Use a difference array (count of changes at specific time points).
2. **Data Structure**: Use a sorted map (e.g., `SortedDict` or `collections.defaultdict` + sorted keys) to store deltas:
   - `delta[start] += 1`
   - `delta[end] -= 1`
3. **Calculate Max K**:
   - To find the max k-booking, iterate through the sorted time points.
   - Maintain a `current` running sum of deltas.
   - The maximum value of `current` encountered during the sweep is the result.
4. **Complexity**:
   - N calls, each takes O(N log N) or O(N) depending on map implementation.
   - Total time: O(N^2). Since N=400, this is very efficient.

Complexity:
- Time: O(N^2) total for 400 bookings.
- Space: O(N) to store time points.
"""
    
    answer = """import collections
class MyCalendarThree:
    def __init__(self):
        self.delta = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1
        
        max_k = 0
        current_k = 0
        for time in sorted(self.delta.keys()):
            current_k += self.delta[time]
            if current_k > max_k:
                max_k = current_k
        return max_k"""

    boilerplate = {
        "python": "import sys\\nimport json\\nimport collections\\n\\nclass MyCalendarThree:\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    input_data = sys.stdin.read().splitlines()\\n    ops = json.loads(input_data[0])\\n    args = json.loads(input_data[1])\\n    # Orchestrator...\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <map>\\nusing namespace std;\\n\\nclass MyCalendarThree { public: int book(int start, int end) { return 0; } };",
        "java": "public class Main { public static void main(String[] args) { } }",
        "javascript": "const fs = require('fs');",
        "c": "typedef struct { } MyCalendarThree; MyCalendarThree* myCalendarThreeCreate() { }"
    }

    test_cases = [
        {"input": '["MyCalendarThree", "book", "book", "book", "book", "book", "book"]\\n[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]', "expected_output": "[null, 1, 1, 2, 3, 3, 3]", "is_sample": True},
        {"input": '["MyCalendarThree", "book", "book", "book"]\\n[[], [1, 10], [1, 10], [1, 10]]', "expected_output": "[null, 1, 2, 3]", "is_sample": False},
        {"input": '["MyCalendarThree", "book", "book", "book"]\\n[[], [1, 10], [5, 15], [10, 20]]', "expected_output": "[null, 1, 2, 2]", "is_sample": False},
        {"input": '["MyCalendarThree", "book", "book", "book"]\\n[[], [10, 20], [10, 20], [10, 20]]', "expected_output": "[null, 1, 2, 3]", "is_sample": False},
        {"input": '["MyCalendarThree", "book", "book", "book"]\\n[[], [10, 20], [0, 5], [30, 40]]', "expected_output": "[null, 1, 1, 1]", "is_sample": False},
        {"input": '["MyCalendarThree", "book", "book", "book", "book"]\\n[[], [5, 10], [10, 15], [15, 20], [20, 25]]', "expected_output": "[null, 1, 1, 1, 1]", "is_sample": False},
        {"input": '["MyCalendarThree", "book", "book", "book", "book"]\\n[[], [1, 100], [2, 100], [3, 100], [4, 100]]', "expected_output": "[null, 1, 2, 3, 4]", "is_sample": False},
        {"input": '["MyCalendarThree", "book", "book", "book"]\\n[[], [10, 20], [5, 25], [15, 21]]', "expected_output": "[null, 1, 2, 3]", "is_sample": False},
        # Stress cases
        {"input": '["MyCalendarThree"] + ["book"]*399\\n[...]', "expected_output": "[null] + [1]*399", "is_sample": False},
        {"input": '["MyCalendarThree"] + ["book"]*399\\n[... triple overlaps]', "expected_output": "[null] + [i+1 for i in range(399)]", "is_sample": False}
    ]
    
    # Specific stress inputs
    test_cases[8]["input"] = json.dumps(["MyCalendarThree"] + ["book"] * 399) + "\\n" + json.dumps([[]] + [[i*10, i*10+5] for i in range(399)])
    test_cases[9]["input"] = json.dumps(["MyCalendarThree"] + ["book"] * 399) + "\\n" + json.dumps([[]] + [[1, 1000]] * 399)

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
            "time_limit_ms": 3000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Design", "Segment Tree", "Ordered Set"],
        "companyIndex": 0
    }

    output_path = "601-800/732_My_Calendar_III.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
