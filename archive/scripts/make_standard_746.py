import json
import os

def generate_json():
    problem_id = 746
    title = "Min Cost Climbing Stairs"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>746. Min Cost Climbing Stairs</h3>
<p>You are given an integer array <code>cost</code> where <code>cost[i]</code> is the cost of <code>i<sup>th</sup></code> step on a staircase. Once you pay the cost, you can either climb one or two steps.</p>

<p>You can either start from the step with index <code>0</code>, or the step with index <code>1</code>.</p>

<p>Return <em>the minimum cost to reach the top of the floor.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> cost = [10,15,20]
<strong>Output:</strong> 15
<strong>Explanation:</strong> You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> cost = [1,100,1,1,1,100,1,1,100,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= cost.length &lt;= 1000</code></li>
	<li><code>0 &lt;= cost[i] &lt;= 999</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers cost."
    output_format = "A single integer representing the minimum cost to reach the top."
    
    constraints = [
        "2 <= cost.length <= 1000",
        "0 <= cost[i] <= 999",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To find the minimum cost to reach the top of the stairs:
1. **The Core Dynamic Programming Idea**:
   - Let `min_cost[i]` be the minimum cost to climb to step `i`.
   - To reach step `i`, you must have come from either step `i-1` or step `i-2`.
2. **Transition**:
   - `min_cost[i] = cost[i] + min(min_cost[i-1], min_cost[i-2])`.
   - The "top" is at index `n` (beyond the last step). To reach index `n`, we can step from `n-1` or `n-2`.
   - So the final answer is `min(min_cost[n-1], min_cost[n-2])`.
3. **Space Optimization**:
   - We only need the costs for the two preceding steps.
   - We can use two variables `down_one` and `down_two` to store these.
4. **Complexity**:
   - Time Complexity: O(N) to iterate through the array once.
   - Space Complexity: O(1) if we use variables instead of an array."""
    
    answer = """def minCostClimbingStairs(cost: list[int]) -> int:
    down_one = down_two = 0
    for i in range(2, len(cost) + 1):
        temp = down_one
        down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
        down_two = temp
    return down_one"""

    boilerplate = {
        "python": "import sys\n\ndef minCostClimbingStairs(cost):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        cost = list(map(int, line.split()))\n        print(minCostClimbingStairs(cost))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint minCostClimbingStairs(vector<int>& cost) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int minCostClimbingStairs(int[] cost) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function minCostClimbingStairs(cost) {\n    // User logic\n}",
        "c": "int minCostClimbingStairs(int* cost, int costSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "10 15 20", "expected_output": "15", "is_sample": True},
        {"input": "1 100 1 1 1 100 1 1 100 1", "expected_output": "6", "is_sample": True},
        {"input": "0 0", "expected_output": "0", "is_sample": False},
        {"input": "1 0", "expected_output": "0", "is_sample": False},
        {"input": "0 1", "expected_output": "0", "is_sample": False},
        {"input": "10 10 10 10", "expected_output": "20", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "6", "is_sample": False},
        {"input": "100 1 1 100", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"] * 1000), "expected_output": "500", "is_sample": False},
        {"input": " ".join(["999"] * 1000), "expected_output": "499500", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "601-800/746_Min_Cost_Climbing_Stairs.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
