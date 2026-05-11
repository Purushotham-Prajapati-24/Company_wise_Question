import json
import os

def generate_json():
    problem_id = 630
    title = "Course Schedule III"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>630. Course Schedule III</h3>
<p>There are <code>n</code> different online courses numbered from 1 to <code>n</code>. You are given an array <code>courses</code> where <code>courses[i] = [duration<sub>i</sub>, lastDay<sub>i</sub>]</code> indicates that the <code>i<sup>th</sup></code> course should be taken continuously for <code>duration<sub>i</sub></code> days and must be finished before or on <code>lastDay<sub>i</sub></code>.</p>

<p>You will start on the 1<sup>st</sup> day and you cannot take two or more courses simultaneously.</p>

<p>Return <em>the maximum number of courses that you can take</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
There are totally 4 courses, but you can take 3 courses at most.
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> courses = [[1,2]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= courses.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= duration<sub>i</sub>, lastDay<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>
"""

    input_format = "A list of lists for 'courses', where each sublist is [duration, lastDay]."
    output_format = "A single integer representing the maximum number of courses."
    
    constraints = [
        "1 <= courses.length <= 10^4",
        "1 <= duration, lastDay <= 10^4"
    ]
    
    explanation = """To maximize courses using greedy + priority queue:
1. Sort all courses by their `lastDay`.
2. Keep track of the current total time consumed (`total_time`).
3. Maintain a max-heap of the durations of the courses taken so far.
4. For each course `(duration, lastDay)`:
   - Add `duration` to `total_time` and push `duration` to the heap.
   - If `total_time > lastDay`, remove the longest course from the heap (it's the bottleneck) and subtract its duration from `total_time`.
5. The number of elements in the heap is the maximum courses taken."""
    
    answer = """import heapq

def scheduleCourse(courses):
    courses.sort(key=lambda x: x[1])
    heap = []
    total_time = 0
    for d, last in courses:
        total_time += d
        heapq.heappush(heap, -d)
        if total_time > last:
            total_time += heapq.heappop(heap)
    return len(heap)"""

    boilerplate = {
        "python": "import sys\\nimport heapq\\n\\ndef scheduleCourse(courses):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    # Custom input handler\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <queue>\\n#include <algorithm>\\n\\nusing namespace std;\\n\\nclass Solution { public: int scheduleCourse(vector<vector<int>>& courses) { return 0; } };",
        "java": "class Solution { public int scheduleCourse(int[][] courses) { return 0; } }",
        "javascript": "const fs = require('fs');",
        "c": "int scheduleCourse(int** courses, int coursesSize, int* coursesColSize) { }"
    }

    test_cases = [
        {"input": "[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]", "expected_output": "3", "is_sample": True},
        {"input": "[[1, 2]]", "expected_output": "1", "is_sample": True},
        {"input": "[[3, 2], [4, 3]]", "expected_output": "0", "is_sample": False},
        {"input": "[[5, 5], [4, 6], [2, 6]]", "expected_output": "2", "is_sample": False},
        {"input": "[[2, 5], [2, 19], [1, 8], [1, 20]]", "expected_output": "4", "is_sample": False},
        {"input": "[[1, 1], [1, 1]]", "expected_output": "1", "is_sample": False},
        {"input": "[[10, 10], [10, 10]]", "expected_output": "1", "is_sample": False},
        {"input": str([[1, 1000]]*10000), "expected_output": "1000", "is_sample": False},
        {"input": str([[i+1, 10000] for i in range(10000)]), "expected_output": "140", "is_sample": False},
        {"input": str([[1, i+1] for i in range(10000)]), "expected_output": "10000", "is_sample": False}
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
        "topics": ["Array", "Greedy", "Heap (Priority Queue)", "Sorting"],
        "companyIndex": 0
    }

    output_path = "401-600/630_Course_Schedule_III.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
