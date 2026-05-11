import json
import os

def generate_json():
    problem_id = 891
    title = "Sum of Subsequence Widths"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>891. Sum of Subsequence Widths</h3>
<p>The <strong>width</strong> of a subsequence is the difference between the maximum and minimum elements in it.</p>

<p>Given an integer array <code>nums</code>, return <em>the sum of the <strong>widths</strong> of all its non-empty <strong>subsequences</strong></em>. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, <code>[3,6,2,7]</code> is a subsequence of <code>[0,3,1,6,2,2,7]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,3]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An integer n, followed by n space-separated integers."
    output_format = "An integer representing the sum of widths modulo 10^9 + 7."
    
    constraints = []
    
    explanation = """HARD problem on ."""
    
    answer = """def sumSubseqWidths(nums):
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)
    res = 0
    pow2 = [1] * n
    for i in range(1, n):
        pow2[i] = (pow2[i-1] * 2) % MOD
        
    for i in range(n):
        res = (res + nums[i] * (pow2[i] - pow2[n-1-i])) % MOD
    return res % MOD"""

    boilerplate = {
        "python": "import sys\n\ndef sumSubseqWidths(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    nums = input_data[0] if len(input_data) > 0 else \"\"\n    print(sumSubseqWidths(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint sumSubseqWidths(string nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string nums; cin >> nums;\n    cout << sumSubseqWidths(nums) << endl;\n    return 0;\n}",
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
