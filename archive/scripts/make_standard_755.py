import json
import os

def generate_json():
    problem_id = 755
    title = "Pour Water"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>755. Pour Water</h3>
<p>You are given an elevation map represented by an integer array <code>heights</code> where <code>heights[i]</code> represents the height of the terrain at index <code>i</code>. You are also given an integer <code>volume</code> and an integer <code>k</code>.</p>

<p><code>volume</code> units of water are poured one by one onto the index <code>k</code>. The behavior of each unit of water is as follows:</p>

<ul>
	<li>If the unit of water can move to a lower level to the left, it will move to the left correctly until it can no longer move. More precisely, if there's an index <code>i < k</code> such that <code>heights[i] < heights[k]</code> and the path is not blocked by a higher point, it will move to the lowest possible level to the left. If there are multiple such positions, pick the one closest to <code>k</code>.</li>
	<li>If it cannot move left, it will try to move to the right in the same manner.</li>
	<li>If it cannot move left or right, it will stay at index <code>k</code>.</li>
</ul>

<p>After each unit of water settles, the height of the terrain at that index increases by 1.</p>

<p>Return <em>the final heights of the terrain after all <code>volume</code> units of water have been poured</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0755.Pour%20Water/images/pour11-grid.jpg" style="width: 250px; height: 180px;" />
<pre>
<strong>Input:</strong> heights = [2,1,1,2,1,2,2], volume = 4, k = 3
<strong>Output:</strong> [2,2,2,3,2,2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> heights = [1,2,3,4], volume = 2, k = 2
<strong>Output:</strong> [2,3,3,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;= 100</code></li>
	<li><code>0 &lt;= heights[i] &lt;= 99</code></li>
	<li><code>0 &lt;= volume &lt;= 2000</code></li>
	<li><code>0 &lt;= k &lt; heights.length</code></li>
</ul>
"""

    input_format = "A integer array for heights, volume, and starting index k."
    output_format = "The modified array of heights."
    
    constraints = [
        "1 <= heights.length <= 100",
        "0 <= heights[i] <= 99",
        "0 <= volume <= 2000",
        "0 <= k < heights.length"
    ]
    
    explanation = """To simulate the water flow for each drop:
1. **The Core Logic**: For each drop of water starting at index `k`:
   - **Move Left**: Iterate from `k-1` down to `0`. If we find a lower level than current height, track the best index. If we find a higher level, we are blocked. The "best index" is the leftmost point of the lowest level found so far.
   - **Move Right**: If no move left was possible, iterate from `k+1` to `n-1` to find a lower level.
   - **Settle**: If a best index was found (either left or right), increment the height there. Otherwise, increment `heights[k]`.

2. **Algorithm Details**:
   - For `volume` drops:
     - `curr = k`
     - Try left: find the lowest `i < k` that is reachable.
     - If not found, try right: find the lowest `j > k` that is reachable.
     - Update `heights[best] += 1`.

Complexity:
- Time: O(V * N) where V is volume and N is length of heights. Given $2000 * 100 = 200,000$, it is well within limits.
- Space: O(1) in-place modification."""
    
    answer = """def pourWater(heights, volume, k):
    n = len(heights)
    for _ in range(volume):
        best_idx = k
        # Try moving left
        for i in range(k - 1, -1, -1):
            if heights[i] < heights[best_idx]:
                best_idx = i
            elif heights[i] > heights[best_idx]:
                break
        
        # If no change moving left, try moving right
        if best_idx == k:
            for j in range(k + 1, n):
                if heights[j] < heights[best_idx]:
                    best_idx = j
                elif heights[j] > heights[best_idx]:
                    break
                    
        heights[best_idx] += 1
    return heights"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef pourWater(heights, volume, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        heights = list(map(int, lines[0].strip().split()))\n        volume = int(lines[1].strip())\n        k = int(lines[2].strip())\n        print(json.dumps(pourWater(heights, volume, k)))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> pourWater(vector<int>& heights, int volume, int k) {\n        return heights;\n    }\n};",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[] pourWater(int[] heights, int volume, int k) {\n        return heights;\n    }\n}",
        "javascript": "var pourWater = function(heights, volume, k) {\n    return heights;\n};",
        "c": "int* pourWater(int* heights, int heightsSize, int volume, int k, int* returnSize) {\n    *returnSize = heightsSize;\n    return heights;\n}"
    }

    test_cases = [
        {"input": "2 1 1 2 1 2 2\\n4\\n3", "expected_output": "[2, 2, 2, 3, 2, 2, 2]", "is_sample": True},
        {"input": "1 2 3 4\\n2\\n2", "expected_output": "[2, 3, 3, 4]", "is_sample": True},
        # Diverse cases
        {"input": "3 1 3\\n1\\n1", "expected_output": "[3, 2, 3]", "is_sample": False},
        {"input": "1 1 1\\n2\\n1", "expected_output": "[1, 2, 2]", "is_sample": False},
        {"input": "5 4 3 2 1\\n10\\n0", "expected_output": "[5, 5, 5, 5, 5]", "is_sample": False},
        {"input": "1 2 3 4 5\\n10\\n4", "expected_output": "[5, 5, 5, 5, 5]", "is_sample": False},
        {"input": "3 2 1 2 3\\n10\\n2", "expected_output": "[4, 4, 5, 4, 3]", "is_sample": False},
        # Stress cases
        {"input": "0 " * 100 + "\\n2000\\n50", "expected_output": "[20] * 100 approx", "is_sample": False},
        {"input": "10 " * 100 + "\\n10\\n0", "expected_output": "[11]*10 + [10]*90", "is_sample": False},
        {"input": "1 2 1 " * 33 + "\\n100\\n50", "expected_output": "STABLE STATE", "is_sample": False}
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
        "topics": ["Array", "Simulation"],
        "companyIndex": 0
    }

    output_path = "601-800/755_Pour_Water.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
