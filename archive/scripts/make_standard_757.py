import json
import os

def generate_json():
    problem_id = 757
    title = "Set Intersection Size At Least Two"
    difficulty = "Hard"
    marks = 30
    
    html_description = """<h3>757. Set Intersection Size At Least Two</h3>
<p>You are given a 2D integer array <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> represents all the integers from <code>start<sub>i</sub></code> to <code>end<sub>i</sub></code> inclusive.</p>

<p>A <strong>containing set</strong> is an array an integers <code>S</code> such that for every interval <code>intervals[i]</code>, the intersection of <code>S</code> and <code>intervals[i]</code> has a size of <strong>at least two</strong>.</p>

<p>Return <em>the minimum size of a containing set</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[1,4],[2,5],[3,5]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> S = [2,3,4] contains 2 integers from each interval.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[2,4],[4,5]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> S = [1,2,3,4,5] contains 2 integers from each interval.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 3000</code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>8</sup></code></li>
</ul>
"""

    input_format = "A 2D array of intervals."
    output_format = "An integer representing the minimum set size."
    
    constraints = [
        "1 <= intervals.length <= 3000",
        "intervals[i].length == 2",
        "0 <= start_i < end_i <= 10^8"
    ]
    
    explanation = """To find the minimum set size for intersection >= 2:
1. **The Greedy Strategy**:
   - Sort the intervals primarily by their `end` point (ascending).
   - If `end` points are equal, sort by `start` point (descending). This ensures that if two intervals end at the same place, we process the shorter one (more restrictive) first.
   
2. **Maintenance**:
   - Keep track of the two largest elements currently in our set `S`, say `p1` and `p2` where `p1 < p2`.
   - Iterate through the sorted intervals `[s, e]`:
     - **Case A**: If `s > p2`, both existing points are outside this interval. We must add TWO points. The best greedy choice is to add the latest points: `e-1` and `e`. Update `p1 = e-1, p2 = e`. Increment count by 2.
     - **Case B**: If `s > p1`, only `p2` is in the interval. We must add ONE more point. The best choice is `e`. Update `p1 = p2, p2 = e`. Increment count by 1.
     - **Case C**: If `s <= p1`, both `p1` and `p2` are already in the interval. Do nothing.

3. **Optimality**: 
   - By picking the largest possible values (end of the current interval), we maximize the chance of these points intersecting with future intervals.

Complexity:
- Time: O(N log N) for sorting, followed by O(N) traversal.
- Space: O(1) extra space beyond sorting storage."""
    
    answer = """def intersectionSizeTwo(intervals):
    # Sort by end ascending, then by start descending
    intervals.sort(key=lambda x: (x[1], -x[0]))
    
    res = 0
    p1, p2 = -1, -1 # Last and second last elements in set
    
    for s, e in intervals:
        if s > p2:
            # No intersection, add two points
            res += 2
            p1 = e - 1
            p2 = e
        elif s > p1:
            # One intersection point (p2), add one more
            res += 1
            p1 = p2
            p2 = e
            
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef intersectionSizeTwo(intervals):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    intervals = json.loads(sys.stdin.read())\n    print(intersectionSizeTwo(intervals))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint intersectionSizeTwo(vector<vector<int>>& intervals) {\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int intersectionSizeTwo(int[][] intervals) {\n        return 0;\n    }\n}",
        "javascript": "var intersectionSizeTwo = function(intervals) {\n    return 0;\n};",
        "c": "int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,3],[1,4],[2,5],[3,5]]", "expected_output": "3", "is_sample": True},
        {"input": "[[1,2],[2,3],[2,4],[4,5]]", "expected_output": "5", "is_sample": True},
        # Diverse cases
        {"input": "[[0,3],[0,4],[0,5]]", "expected_output": "2", "is_sample": False},
        {"input": "[[1,10],[2,10],[3,10]]", "expected_output": "2", "is_sample": False},
        {"input": "[[0,1],[1,2],[2,3]]", "expected_output": "4", "is_sample": False},
        {"input": "[[0,2],[1,3],[2,4]]", "expected_output": "4", "is_sample": False},
        {"input": "[[1,2],[3,4],[5,6]]", "expected_output": "6", "is_sample": False},
        # Stress cases
        {"input": "[[1,2]]", "expected_output": "2", "is_sample": False},
        {"input": json.dumps([[i, i+1] for i in range(3000)]), "expected_output": "3001", "is_sample": False},
        {"input": json.dumps([[0, 1000]] * 3000), "expected_output": "2", "is_sample": False}
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
        "topics": ["Array", "Greedy", "Sorting"],
        "companyIndex": 0
    }

    output_path = "601-800/757_Set_Intersection_Size_At_Least_Two.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
