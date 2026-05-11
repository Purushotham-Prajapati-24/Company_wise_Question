import json
import os

def generate_json():
    problem_id = 1035
    title = "Uncrossed Lines"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>1035. Uncrossed Lines</h3>
<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>. We write the integers of <code>nums1</code> and <code>nums2</code> (in the order they are given) on two separate horizontal lines.</p>

<p>We may draw connecting lines: a straight line connecting two numbers <code>nums1[i]</code> and <code>nums2[j]</code> such that:</p>
<ul>
	<li><code>nums1[i] == nums2[j]</code>, and</li>
    <li>the line we draw does not intersect any other connecting (non-horizontal) line.</li>
</ul>

<p>Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only be part of one connection).</p>

<p>Return <em>the maximum number of connecting lines we can draw in this way</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/26/142.png" style="width: 400px; height: 286px;" />
<pre>
<strong>Input:</strong> nums1 = [1,4,2], nums2 = [1,2,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2] = 2 to nums2[1] = 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums1.length, nums2.length &le; 500</code></li>
	<li><code>1 &lt;= nums1[i], nums2[j] &le; 2000</code></li>
</ul>
"""

    input_format = "Two integer arrays nums1 and nums2."
    output_format = "An integer maximum lines."
    
    constraints = [
        "1 <= nums1.length, nums2.length <= 500",
        "1 <= nums1[i], nums2[j] <= 2000",
        "Goal: Max connections without intersection."
    ]
    
    explanation = """To find the maximum number of uncrossed lines:
1. **The Core Insight (Longest Common Subsequence)**:
   - The "uncrossed" requirement means that if we connect `nums1[i]` to `nums2[j]`, any future connection `nums1[i']` to `nums2[j']` must satisfy `i' > i` AND `j' > j`.
   - This is exactly the definition of the Longest Common Subsequence (LCS) problem. We are searching for the length of the longest subsequence that is common to both `nums1` and `nums2`.

2. **The Dynamic Programming Algorithm**:
   - Define `dp[i][j]` as the maximum lines we can draw using `nums1[0...i-1]` and `nums2[0...j-1]`.
   - Transition:
     - If `nums1[i-1] == nums2[j-1]`:
       - `dp[i][j] = dp[i-1][j-1] + 1` (Take this connection).
     - Otherwise:
       - `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (Skip one of the current numbers).

Complexity:
- Time: O(M * N) where M and N are lengths of the two arrays.
- Space: O(M * N) for the DP table (can be optimized to O(min(M, N)) using only two rows)."""
    
    answer = """def maxUncrossedLines(nums1: list[int], nums2: list[int]) -> int:
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef maxUncrossedLines(nums1, nums2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    nums1 = json.loads(lines[0])\n    nums2 = json.loads(lines[1])\n    print(maxUncrossedLines(nums1, nums2))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {\n        return 0;\n    }\n};",
        "java": "class Solution {\n    public int maxUncrossedLines(int[] nums1, int[] nums2) {\n        return 0;\n    }\n}",
        "javascript": "var maxUncrossedLines = function(nums1, nums2) {\n    return 0;\n};",
        "c": "int maxUncrossedLines(int* nums1, int nums1Size, int* nums2, int nums2Size){\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,4,2]\\n[1,2,4]", "expected_output": "2", "is_sample": True},
        {"input": "[2,5,1,2,5]\\n[10,5,2,1,5,2]", "expected_output": "3", "is_sample": True},
        {"input": "[1,3,7,1,7,5]\\n[1,9,2,5,1]", "expected_output": "2", "is_sample": True},
        # Diverse cases
        {"input": "[1]\\n[2]", "expected_output": "0", "is_sample": False},
        {"input": "[1,2,3]\\n[1,2,3]", "expected_output": "3", "is_sample": False},
        {"input": "[1,2,3]\\n[3,2,1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,1,2]\\n[2,1,2,1]", "expected_output": "3", "is_sample": False},
        {"input": "[10, 10, 10]\\n[10, 10]", "expected_output": "2", "is_sample": False},
        {"input": "[1,3,2,4,8]\\n[1,5,6,4,2]", "expected_output": "2", "is_sample": False},
        {"input": "list(range(500))\\nlist(range(499, -1, -1))", "expected_output": "1", "is_sample": False},
        # Stress cases (500x500)
        {"input": "[1]*500\\n[1]*500", "expected_output": "500", "is_sample": False},
        {"input": "random 500x500", "expected_output": "various", "is_sample": False}
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

    output_path = "1001-1100/1035_Uncrossed_Lines.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
