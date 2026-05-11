import json
import os

def generate_json():
    problem_id = 918
    title = "Maximum Sum Circular Subarray"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>918. Maximum Sum Circular Subarray</h3>
<p>Given a <strong>circular integer array</strong> <code>nums</code> of length <code>n</code>, return <em>the maximum possible sum of a non-empty <strong>subarray</strong> of </em><code>nums</code>.</p>

<p>A <strong>circular array</strong> means the end of the array connects to the beginning of the array. Formally, the next element of <code>nums[i]</code> is <code>nums[(i + 1) % n]</code> and the previous element of <code>nums[i]</code> is <code>nums[(i - 1 + n) % n]</code>.</p>

<p>A <strong>subarray</strong> may only include each element of the fixed buffer <code>nums</code> at most once. Formally, for a subarray <code>nums[i], nums[i+1], ..., nums[j]</code>, there does not exist <code>i &lt;= k1, k2 &lt;= j</code> with <code>k1 % n == k2 % n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,-2,3,-2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Subarray [3] has maximum sum 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,-3,5]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Subarray [5,5] has maximum sum 5 + 5 = 10.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [-3,-2,-3]
<strong>Output:</strong> -2
<strong>Explanation:</strong> Subarray [-2] has maximum sum -2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An integer n, followed by n space-separated integers."
    output_format = "An integer representing the maximum circular subarray sum."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def maxSubarraySumCircular(nums):
    total_sum = 0
    max_sum = nums[0]
    curr_max = 0
    min_sum = nums[0]
    curr_min = 0
    
    for x in nums:
        curr_max = max(x, curr_max + x)
        max_sum = max(max_sum, curr_max)
        curr_min = min(x, curr_min + x)
        min_sum = min(min_sum, curr_min)
        total_sum += x
        
    return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum"""

    boilerplate = {
        "python": "import sys\n\ndef maxSubarraySumCircular(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    nums = input_data[0] if len(input_data) > 0 else \"\"\n    print(maxSubarraySumCircular(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint maxSubarraySumCircular(string nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string nums; cin >> nums;\n    cout << maxSubarraySumCircular(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
