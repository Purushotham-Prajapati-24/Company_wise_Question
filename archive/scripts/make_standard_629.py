import json
import os

def generate_json():
    problem_id = 629
    title = "K Inverse Pairs Array"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>629. K Inverse Pairs Array</h3>
<p>For an integer array <code>nums</code>, an <b>inverse pair</b> is a pair of integers <code>[i, j]</code> such that <code>0 &lt;= i &lt; j &lt; nums.length</code> and <code>nums[i] &gt; nums[j]</code>.</p>

<p>Given two integers <code>n</code> and <code>k</code>, return the number of different arrays consist of numbers from <code>1</code> to <code>n</code> such that there are exactly <code>k</code> <b>inverse pairs</b>. Since the answer can be huge, return it <b>modulo</b> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3, k = 0
<strong>Output:</strong> 1
<strong>Explanation:</strong> Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= k &lt;= 1000</code></li>
</ul>
"""

    input_format = "A single line containing space-separated integers for n, k."
    output_format = "A single integer modulo 10^9 + 7."
    
    constraints = [
        "1 <= n <= 1000",
        "0 <= k <= 1000"
    ]
    
    explanation = """To solve for the number of arrays with k inverse pairs:
1. Let `dp[i][j]` be the number of permutations of length `i` with `j` inverse pairs.
2. When adding element `i` into a permutation of length `i-1`:
   - If placed at the end, 0 additional pairs.
   - If placed in the middle, `j-m` pairs where `m` is the number of elements after it.
   - Max additional pairs is `i-1`.
3. So, `dp[i][j] = sum(dp[i-1][j-m])` for `m` from 0 to `min(j, i-1)`.
4. This can be optimized using prefix sums:
   `dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + ... + dp[i-1][j-i+1]`
   `dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i]`
5. Time Complexity: O(n * k). Space complexity can be optimized to O(k)."""
    
    answer = """def kInversePairs(n, k):
    mod = 10**9 + 7
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        new_dp = [0] * (k + 1)
        curr_sum = 0
        for j in range(k + 1):
            curr_sum += dp[j]
            if j >= i:
                curr_sum -= dp[j - i]
            new_dp[j] = curr_sum % mod
        dp = new_dp
        
    return dp[k]"""

    boilerplate = {
        "python": "import sys\\n\\ndef kInversePairs(n, k):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    # Custom input handler\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n\\nusing namespace std;\\n\\nclass Solution { public: int kInversePairs(int n, int k) { return 0; } };",
        "java": "class Solution { public int kInversePairs(int n, int k) { return 0; } }",
        "javascript": "const fs = require('fs');",
        "c": "int kInversePairs(int n, int k) { }"
    }

    test_cases = [
        {"input": "3 0", "expected_output": "1", "is_sample": True},
        {"input": "3 1", "expected_output": "2", "is_sample": True},
        {"input": "1 0", "expected_output": "1", "is_sample": False},
        {"input": "2 1", "expected_output": "1", "is_sample": False},
        {"input": "3 2", "expected_output": "2", "is_sample": False},
        {"input": "3 3", "expected_output": "1", "is_sample": False},
        {"input": "10 5", "expected_output": "391", "is_sample": False},
        {"input": "1000 0", "expected_output": "1", "is_sample": False},
        {"input": "1000 1000", "expected_output": "663677020", "is_sample": False},
        {"input": "500 450", "expected_output": "358971488", "is_sample": False}
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
        "topics": ["Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "401-600/629_K_Inverse_Pairs_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
