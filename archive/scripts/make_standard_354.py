import json
import os

def generate_json():
    problem_id = 354
    title = "Russian Doll Envelopes"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>354. Russian Doll Envelopes</h3>
<p>You are given a 2D array of integers <code>envelopes</code> where <code>envelopes[i] = [w<sub>i</sub>, h<sub>i</sub>]</code> represents the width and the height of an envelope.</p>

<p>One envelope can fit into another if and only if both the width and height of one envelope are strictly greater than the other envelope's width and height.</p>

<p>Return <em>the maximum number of envelopes you can Russian doll (i.e., put one inside the other)</em>.</p>

<p><strong>Note:</strong> You cannot rotate an envelope.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> envelopes = [[5,4],[6,4],[6,7],[2,3]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The maximum number of envelopes you can Russian doll is <code>3</code> ([2,3] => [5,4] => [6,7]).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> envelopes = [[1,1],[1,1],[1,1]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= envelopes.length &lt;= 10<sup>5</sup></code></li>
	<li><code>envelopes[i].length == 2</code></li>
	<li><code>1 &lt;= w<sub>i</sub>, h<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A 2D integer array `envelopes`."
    output_format = "An integer representing the maximum nested envelopes."
    
    constraints = [
        "1 <= envelopes.length <= 100,000",
        "1 <= width, height <= 100,000"
    ]
    
    explanation = """To solve this problem in $O(N \log N)$ time, we transform the 2D problem into a 1D **Longest Increasing Subsequence (LIS)** problem.

### Key Insight:
- If we sort the envelopes by **width** in ascending order, we only need to worry about the **heights**.
- If multiple envelopes have the same width, we sort them by **height in descending order**.
  - **Why?** Since we need strictly nesting (width1 < width2 and height1 < height2), if widths are equal, we cannot nest any of them. By sorting heights descending, we ensure that for a fixed width, the LIS algorithm only picks at most one height.

### Algorithm Steps:
1. **Sort**: Sort `envelopes` by width ascending, then by height descending.
2. **LIS on Heights**: Extract the heights and find the LIS using the binary search method (`bisect_left`).
   - Maintain a list `tails` where `tails[i]` is the smallest tail of all increasing subsequences of length `i+1`.
   - For each height `h`:
     - Find the leftmost position `idx` in `tails` such that `tails[idx] >= h`.
     - If `idx` is equal to the length of `tails`, append `h`.
     - Otherwise, replace `tails[idx]` with `h`.
3. **Result**: The length of the `tails` list is the result.

### Complexity Analysis:
- **Time Complexity**: $O(N \log N)$ for sorting and $O(N \log N)$ for the LIS (each of the $N$ elements takes $\log N$ binary search).
- **Space Complexity**: $O(N)$ to store the heights or the `tails` array."""
    
    answer = """import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width ascending, then by height descending
        # Descending height ensures that for same width, we don't pick more than one
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Now find LIS on heights
        tails = []
        for _, h in envelopes:
            idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
                
        return len(tails)"""

    boilerplate = {
        "python": "import sys\nimport json\nimport bisect\n\nclass Solution:\n    def maxEnvelopes(self, envelopes):\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        envelopes = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.maxEnvelopes(envelopes)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int maxEnvelopes(vector<vector<int>>& envelopes) {\n        // Your logic here\n        return 0;\n    }\n};",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int maxEnvelopes(int[][] envelopes) {\n        // Your logic here\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {number[][]} envelopes\n * @return {number}\n */\nvar maxEnvelopes = function(envelopes) {\n    // Your logic here\n};",
        "c": "int maxEnvelopes(int** envelopes, int envelopesSize, int* envelopesColSize) {\n    // Your logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[5,4],[6,4],[6,7],[2,3]]", "expected_output": "3", "is_sample": True},
        {"input": "[[1,1],[1,1],[1,1]]", "expected_output": "1", "is_sample": True},
        {"input": "[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]", "expected_output": "5", "is_sample": False},
        {"input": "[[1,1]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,2],[2,3],[3,4]]", "expected_output": "3", "is_sample": False},
        {"input": "[[1,3],[1,4],[1,5]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,5],[2,5],[3,5]]", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": "[[i, i] for i in range(100000)]", "expected_output": "100000", "is_sample": False},
        {"input": "[[1, i] for i in range(100000)]", "expected_output": "1", "is_sample": False},
        {"input": "[[i, 1] for i in range(100000)]", "expected_output": "1", "is_sample": False}
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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Binary Search", "Dynamic Programming", "Sorting"],
        "companyIndex": 1
    }

    output_path = "301-500/354_Russian_Doll_Envelopes.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
