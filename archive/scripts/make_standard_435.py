import json
import os

def generate_json():
    problem_id = 435
    title = "Non-overlapping Intervals"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>435. Non-overlapping Intervals</h3>
<p>Given an array of intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[1,2],[2,3],[3,4],[1,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> [1,3] can be removed and the rest of the intervals are non-overlapping.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[1,2],[1,2],[1,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need to remove two [1,2] to make the rest of the intervals non-overlapping.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> intervals = [[1,2],[2,3]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You don't need to remove any of the intervals since they're already non-overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>-5 * 10<sup>4</sup> &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 5 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An array of `[start, end]` intervals."
    output_format = "An integer (minimum removals)."
    
    constraints = [
        "1 <= number of intervals <= 100,000",
        "Intervals that touch at a point are NOT overlapping.",
        "Must be O(N log N) complexity."
    ]
    
    explanation = """To minimize the number of removals, we want to maximize the number of non-overlapping intervals we keep. This is a classic **Interval Scheduling** problem.

### Key Observation:
- We should always pick the interval that **ends first**.
- By picking the one that finishes earliest, we leave as much room as possible for subsequent intervals.

### Algorithm Steps:
1. **Sort**: Sort all intervals by their **end time**.
2. **Greedy Selection**:
   - Initialize `count = 0` (removals) and `prev_end = -infinity`.
   - Iterate through the sorted intervals:
     - If the `current_start` >= `prev_end`:
       - No overlap! Update `prev_end = current_end`.
     - Else (the current interval starts before the last one ended):
       - Overlap detected! We must remove this interval to keep the one that ends earlier.
       - Increment `count`.
3. **Return**: The total `count`.

### Complexity Analysis:
- **Time Complexity**: $O(N \log N)$ due to sorting. The linear scan takes $O(N)$.
- **Space Complexity**: $O(1)$ extra space if sorting in-place, or $O(N)$ depending on the sort implementation."""
    
    answer = """class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
            
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        prev_end = float('-inf')
        
        for start, end in intervals:
            if start >= prev_end:
                # No overlap
                prev_end = end
            else:
                # Overlap, remove the one that ends later (which we've already done by sorting)
                removals += 1
                
        return removals"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        intervals = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.eraseOverlapIntervals(intervals)))",
        "cpp": "class Solution {\npublic:\n    int eraseOverlapIntervals(vector<vector<int>>& intervals) {\n        // Your logic here\n        return 0;\n    }\n};",
        "java": "public class Solution {\n    public int eraseOverlapIntervals(int[][] intervals) {\n        // Your logic here\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {number[][]} intervals\n * @return {number}\n */\nvar eraseOverlapIntervals = function(intervals) {\n    // Your logic here\n};",
        "c": "int eraseOverlapIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {\n    // Your logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,2],[2,3],[3,4],[1,3]]", "expected_output": "1", "is_sample": True},
        {"input": "[[1,2],[1,2],[1,2]]", "expected_output": "2", "is_sample": True},
        {"input": "[[1,2],[2,3]]", "expected_output": "0", "is_sample": True},
        {"input": "[[1,10],[2,3],[3,4],[5,6]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,2],[2,3],[3,4],[1,3],[2,4]]", "expected_output": "2", "is_sample": False},
        {"input": "[[1,5],[2,3],[3,4]]", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": "[[i, i+1] for i in range(100000)]", "expected_output": "0", "is_sample": False},
        {"input": "[[0, 100000]] + [[i, i+1] for i in range(100000)]", "expected_output": "1", "is_sample": False},
        {"input": "[[i, i+100] for i in range(100000)]", "expected_output": "99901", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Greedy", "Sorting"],
        "companyIndex": 1
    }

    output_path = "301-500/435_Non-overlapping_Intervals.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
