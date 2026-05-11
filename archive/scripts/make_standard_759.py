import json
import os

def generate_json():
    problem_id = 759
    title = "Employee Free Time"
    difficulty = "Hard"
    marks = 30
    
    html_description = """<h3>759. Employee Free Time</h3>
<p>We are given a list <code>schedule</code> of employees, which represents the working time for each employee.</p>

<p>Each employee has a list of non-overlapping <code>Intervals</code>, and these intervals are in sorted order.</p>

<p>Return <em>the list of finite intervals representing <strong>common, positive-length free time</strong> for all employees, also in sorted order</em>.</p>

<p>(Even though we are representing <code>Intervals</code> in the form <code>[x, y]</code>, the objects inside are <code>Intervals</code>, not lists or arrays. For example, <code>schedule[0][0].start = 1, schedule[0][0].end = 2</code>, and <code>schedule[0][0][0]</code> is not defined). Also, we wouldn't include intervals like <code>[5, 5]</code> in our answer, as they have zero length.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
<strong>Output:</strong> [[3,4]]
<strong>Explanation:</strong> There are a total of three employees, and their schedule of working hours are:
[[1,2], [5,6]], [[1,3]], [[4,10]].
The common free time is [3,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
<strong>Output:</strong> [[5,6],[7,9]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= schedule.length &lt;= 50</code></li>
	<li><code>0 &lt;= schedule[i].length &lt;= 50</code></li>
	<li><code>0 &lt;= schedule[i][j].start &lt; schedule[i][j].end &lt;= 10<sup>8</sup></code></li>
</ul>
"""

    input_format = "A nested JSON array for the schedule."
    output_format = "A 2D JSON array of common free intervals."
    
    constraints = [
        "1 <= schedule.length <= 50",
        "0 <= schedule[i].length <= 50",
        "0 <= start < end <= 10^8"
    ]
    
    explanation = """To find the common free time for all employees:
1. **The Core Objective**: Identify time intervals that are NOT covered by any employee's work schedule.
2. **The Algorithm (Sort then Merge)**:
   - Collect every work interval `[start, end]` from ALL employees into a single list.
   - Sort these intervals by `start` time.
   - Iterate through the sorted intervals and maintain a `merged_end` representing the point up to which all time is covered.
   - For a current interval `[s, e]`:
     - If `s > merged_end`, it means there is a gap between `merged_end` and `s`. This gap `[merged_end, s]` is common free time for everyone.
     - Update `merged_end = max(merged_end, e)`.
3. **Optimized Approach (Heap)**:
   - Since each individual schedule is already sorted, we can use a Min-Heap to perform a k-way merge of the schedules. This reduces memory pressure as we don't store one massive list upfront.
   
Complexity:
- Time: O(N log N) where N is the total number of intervals (sorting all) or O(N log K) with a heap of size K (number of employees).
- Space: O(N) to store common free intervals."""
    
    answer = """def employeeFreeTime(schedule):
    # flatten and sort
    intervals = []
    for emp in schedule:
        for interval in emp:
            intervals.append(interval)
            
    intervals.sort(key=lambda x: x[0])
    
    res = []
    temp_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start > temp_end:
            res.append([temp_end, start])
        
        if end > temp_end:
            temp_end = end
            
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef employeeFreeTime(schedule):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    schedule = json.loads(sys.stdin.read())\n    print(json.dumps(employeeFreeTime(schedule)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nvector<vector<int>> employeeFreeTime(vector<vector<vector<int>>>& schedule) {\n    return {};\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    class Interval { public int start; public int end; }\n    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {\n        return new ArrayList<>();\n    }\n}",
        "javascript": "var employeeFreeTime = function(schedule) {\n    return [];\n};",
        "c": "typedef struct Interval { int start; int end; } Interval;\nInterval** employeeFreeTime(Interval*** schedule, int scheduleSize, int* employeeSizes, int* returnSize) {\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "[[[1,2],[5,6]],[[1,3]],[[4,10]]]", "expected_output": "[[3,4]]", "is_sample": True},
        {"input": "[[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]", "expected_output": "[[5,6],[7,9]]", "is_sample": True},
        # Diverse cases
        {"input": "[[[1,2]],[[2,3]],[[3,4]]]", "expected_output": "[]", "is_sample": False},
        {"input": "[[[1,10]],[[1,10]]]", "expected_output": "[]", "is_sample": False},
        {"input": "[[[1,2]],[[5,6]]]", "expected_output": "[[2,5]]", "is_sample": False},
        {"input": "[[[1,2]],[[100,200]]]", "expected_output": "[[2,100]]", "is_sample": False},
        {"input": "[[[1,5]],[[2,6]],[[3,7]]]", "expected_output": "[]", "is_sample": False},
        # Stress cases
        {"input": json.dumps([[[i*2, i*2+1]] for i in range(50)]), "expected_output": json.dumps([[1+2*i, 2+2*i] for i in range(49)]), "is_sample": False},
        {"input": json.dumps([[[0, 100000000]] for _ in range(50)]), "expected_output": "[]", "is_sample": False},
        {"input": json.dumps([[[1,2]], [[2,3]]] * 25), "expected_output": "[]", "is_sample": False}
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
        "topics": ["Array", "Sorting", "Heap (Priority Queue)"],
        "companyIndex": 0
    }

    output_path = "601-800/759_Employee_Free_Time.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
