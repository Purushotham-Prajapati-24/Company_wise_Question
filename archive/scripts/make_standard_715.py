import json
import os
import bisect

def generate_json():
    problem_id = 715
    title = "Range Module"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>715. Range Module</h3>
<p>A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.</p>

<ul>
	<li><code>addRange(int left, int right)</code> Adds the half-open interval <code>[left, right)</code>, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval <code>[left, right)</code> that are not already tracked.</li>
	<li><code>queryRange(int left, int right)</code> Returns <code>true</code> if and only if every real number in the interval <code>[left, right)</code> is currently being tracked.</li>
	<li><code>removeRange(int left, int right)</code> Stops tracking every real number currently being tracked in the half-open interval <code>[left, right)</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 20]]
<strong>Output:</strong>
[null, null, null, true, false, true]

<strong>Explanation:</strong>
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False, (numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 20); // return True, (every number in [16, 20) is being tracked)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= left &lt; right &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>addRange</code>, <code>queryRange</code>, and <code>removeRange</code>.</li>
</ul>
"""

    input_format = "Two lines:\\n1. List of operations\\n2. List of arguments"
    output_format = "List of return values."
    
    constraints = [
        "1 <= left < right <= 10^9",
        "Operations limit: 10,000 calls.",
        "Efficient merging and querying of non-overlapping intervals."
    ]
    
    explanation = """To implement the Range Module effectively:
1. **Representing Ranges**: Store ranges as non-overlapping sorted intervals. A flat list `self.ranges = [start1, end1, start2, end2, ...]` is memory-efficient and easy to maintain with binary search.
2. **Operations**:
   - `addRange(L, R)`: Use `bisect_left` and `bisect_right` to find the range of elements that are affected by `[L, R)`. Merge them by replacing the affected indices with `L` and `R` if necessary.
   - `queryRange(L, R)`: Use binary search to find where `L` and `R` would fit. If `L` and `R` both land inside the same "tracked" interval (even indices are starts, odd are ends), return `True`.
   - `removeRange(L, R)`: Similar to `addRange`, find affected indices and replace them with `L` and `R` ensuring they become a "gap".
3. **Execution**: Python's `bisect` and slice assignment `X[i:j] = [v1, v2]` make this very concise.

Complexity:
- Time: O(N) worst case for adding/removing (due to array shifts), but O(log N) for querying.
- Space: O(N) to store intervals.
"""
    
    answer = """import bisect
class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        i, j = bisect.bisect_left(self.ranges, left), bisect.bisect_right(self.ranges, right)
        merged = []
        if i % 2 == 0: merged.append(left)
        if j % 2 == 0: merged.append(right)
        self.ranges[i:j] = merged

    def queryRange(self, left: int, right: int) -> bool:
        i, j = bisect.bisect_right(self.ranges, left), bisect.bisect_left(self.ranges, right)
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        i, j = bisect.bisect_left(self.ranges, left), bisect.bisect_right(self.ranges, right)
        merged = []
        if i % 2 == 1: merged.append(left)
        if j % 2 == 1: merged.append(right)
        self.ranges[i:j] = merged"""

    boilerplate = {
        "python": "import sys\\nimport json\\nimport bisect\\n\\nclass RangeModule:\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    input_data = sys.stdin.read().splitlines()\\n    ops = json.loads(input_data[0])\\n    args = json.loads(input_data[1])\\n    # Orchestrator logic...\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <map>\\nusing namespace std;\\n\\nclass RangeModule { public: void addRange(int left, int right) {} bool queryRange(int left, int right) { return false; } void removeRange(int left, int right) {} };",
        "java": "public class Main { public static void main(String[] args) { } }",
        "javascript": "const fs = require('fs');",
        "c": "typedef struct { } RangeModule; RangeModule* rangeModuleCreate() { }"
    }

    test_cases = [
        {"input": '["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]\\n[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 20]]', "expected_output": "[null, null, null, true, false, true]", "is_sample": True},
        {"input": '["RangeModule", "addRange", "queryRange"]\\n[[], [1, 5], [1, 5]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["RangeModule", "addRange", "queryRange"]\\n[[], [1, 5], [1, 6]]', "expected_output": "[null, null, false]", "is_sample": False},
        {"input": '["RangeModule", "addRange", "addRange", "queryRange"]\\n[[], [1, 3], [3, 5], [1, 5]]', "expected_output": "[null, null, null, true]", "is_sample": False},
        {"input": '["RangeModule", "addRange", "removeRange", "queryRange"]\\n[[], [1, 10], [2, 9], [1, 10]]', "expected_output": "[null, null, null, false]", "is_sample": False},
        {"input": '["RangeModule", "addRange", "removeRange", "queryRange"]\\n[[], [1, 10], [1, 10], [1, 10]]', "expected_output": "[null, null, null, false]", "is_sample": False},
        {"input": '["RangeModule", "addRange", "queryRange"]\\n[[], [100, 200], [150, 151]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["RangeModule", "addRange", "removeRange", "queryRange"]\\n[[], [10, 20], [10, 20], [10, 20]]', "expected_output": "[null, null, null, false]", "is_sample": False},
        # Stress cases
        {"input": '["RangeModule"] + ["addRange"]*5000 + ["queryRange"]*5000\\n[...]', "expected_output": "[null]*5001 + [true]*5000", "is_sample": False},
        {"input": '["RangeModule", "addRange", "removeRange"] * 3333\\n[...]', "expected_output": "[null]*10000", "is_sample": False}
    ]

    # Fixing large input mocks
    test_cases[8]["input"] = json.dumps(["RangeModule"] + ["addRange"]*499 + ["queryRange"]*500) + "\\n" + json.dumps([[]] + [[i*10, i*10+5] for i in range(499)] + [[i*10, i*10+5] for i in range(500)])
    test_cases[9]["input"] = json.dumps(["RangeModule"] + ["addRange", "removeRange"]*499) + "\\n" + json.dumps([[]] + [[1, 10], [1, 10]]*499)

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
        "topics": ["Design", "Segment Tree", "Ordered Set", "Array"],
        "companyIndex": 0
    }

    output_path = "601-800/715_Range_Module.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
