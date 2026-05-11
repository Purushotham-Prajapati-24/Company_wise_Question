import json
import os

def generate_json():
    problem_id = 849
    title = "Maximize Distance to Closest Person"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>849. Maximize Distance to Closest Person</h3>
<p>You are given an array representing a row of seats where <code>seats[i] = 1</code> represents a person sitting in the <code>i</code><sup>th</sup> seat, and <code>seats[i] = 0</code> represents that the <code>i</code><sup>th</sup> seat is empty (0-indexed).</p>

<p>There is at least one empty seat, and at least one person sitting.</p>

<p>Alex wants to sit in an empty seat such that the distance between him and the closest person to him is maximized. </p>

<p>Return <em>that maximum distance to the closest person</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> seats = [1,0,0,0,1,0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
If Alex sits in the second empty seat (i.e. seats[2]), the closest person is at distance 2.
If Alex sits in any other empty seat, the closest person is at distance 1.
Thus, the maximum distance to the closest person is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> seats = [1,0,0,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
If Alex sits in the last seat (i.e. seats[3]), the closest person is at distance 3.
This is the maximum distance possible, so the answer is 3.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> seats = [0,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= seats.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>seats[i]</code> is <code>0</code> or <code>1</code>.</li>
	<li>At least one seat is <b>empty</b>.</li>
	<li>At least one seat is <b>occupied</b>.</li>
</ul>"""

    input_format = "A single line containing space-separated integers (0 or 1)."
    output_format = "A single integer representing the maximum possible distance."
    
    constraints = [
        "2 <= n <= 20,000",
        "At least one empty and one occupied seat.",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To maximize the distance to the closest person:
1. **Three Scenario Analysis**:
   - There are three types of positions Alex can take:
     - **Before the first occupied seat**: The distance is simply the number of trailing zeros at the start.
     - **Between two occupied seats**: If there are `k` zeros between two people, the best Alex can do is sit in the middle, giving a distance of `(k + 1) // 2`.
     - **After the last occupied seat**: The distance is the number of trailing zeros at the end.
2. **Algorithm Steps**:
   - Traverse the array once, keeping track of the current number of consecutive zeros (`count`).
   - If we see a 1:
     - If this is the first 1 we've seen, update `max_dist` to `count` (left edge case).
     - Otherwise, update `max_dist` to `max(max_dist, (count + 1) // 2)` (middle case).
     - Reset `count` to 0.
   - After the loop, the final `count` represents the zeros after the last person. Update `max_dist` to `max(max_dist, count)` (right edge case).
3. **Complexity**:
   - Time Complexity: O(N) to traverse the seats once.
   - Space Complexity: O(1) extra space."""
    
    answer = """def maxDistToClosest(seats: list[int]) -> int:
    max_dist = 0
    last_person = -1
    n = len(seats)
    
    for i in range(n):
        if seats[i] == 1:
            if last_person == -1:
                max_dist = i
            else:
                max_dist = max(max_dist, (i - last_person) // 2)
            last_person = i
            
    # Check end of seats
    max_dist = max(max_dist, n - 1 - last_person)
    return max_dist"""

    boilerplate = {
        "python": "import sys\n\ndef maxDistToClosest(seats):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        seats = list(map(int, line.split()))\n        print(maxDistToClosest(seats))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint maxDistToClosest(vector<int>& seats) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int maxDistToClosest(int[] seats) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function maxDistToClosest(seats) {\n    // User logic\n}",
        "c": "int maxDistToClosest(int* seats, int seatsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 0 0 0 1 0 1", "expected_output": "2", "is_sample": True},
        {"input": "1 0 0 0", "expected_output": "3", "is_sample": True},
        {"input": "0 1", "expected_output": "1", "is_sample": True},
        {"input": "1 0 1", "expected_output": "1", "is_sample": False},
        {"input": "0 0 1 0 0", "expected_output": "2", "is_sample": False},
        {"input": "0 0 0 1", "expected_output": "3", "is_sample": False},
        {"input": "1 0 0 1 0 0 1", "expected_output": "1", "is_sample": False},
        {"input": "1 0 0 0 0 1", "expected_output": "2", "is_sample": False}, # (5-1) // 2 = 2
        # Stress cases
        {"input": "1 " + "0 " * 19998 + "1", "expected_output": "9999", "is_sample": False},
        {"input": "0 " * 19999 + "1", "expected_output": "19999", "is_sample": False}
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
        "topics": ["Array"],
        "companyIndex": 0
    }

    output_path = "801-1000/849_Maximize_Distance_to_Closest_Person.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
