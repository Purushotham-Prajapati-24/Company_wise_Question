import json
import os

def generate_json():
    problem_id = 1018
    title = "Binary Prefix Divisible By 5"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1018. Binary Prefix Divisible By 5</h3>
<p>You are given a binary array <code>nums</code> (<strong>0-indexed</strong>).</p>

<p>We define <code>x<sub>i</sub></code> as the number whose binary representation is the subarray <code>nums[0..i]</code> (from most-significant-bit to least-significant-bit).</p>

<ul>
	<li>For example, if <code>nums = [1,0,1]</code>, then <code>x<sub>0</sub> = 1</code>, <code>x<sub>1</sub> = 2</code>, and <code>x<sub>2</sub> = 5</code>.</li>
</ul>

<p>Return <em>an array of booleans </em><code>answer</code><em> where </em><code>answer[i]</code><em> is </em><code>true</code><em> if </em><code>x<sub>i</sub></code><em> is divisible by </em><code>5</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> [true,false,false]
<strong>Explanation:</strong> The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> [false,false,false]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>"""

    input_format = "A single line containing space-separated integers (0 or 1)."
    output_format = "A single line containing space-separated 'true' or 'false'."
    
    constraints = [
        "1 <= nums.length <= 100,000",
        "Binary digits only.",
        "O(N) time complexity.",
        "O(1) extra space (excluding result array)."
    ]
    
    explanation = """To determine divisibility of binary prefixes by 5:
1. **The Challenge (Large Numbers)**:
   - Binary numbers with up to 10^5 bits can be astronomically large. We cannot compute their decimal values directly as it would cause overflow.
2. **The Insight (Modular Arithmetic)**:
   - We only care if `x_i % 5 == 0`.
   - Property: `(A * 2 + B) % 5 == ((A % 5) * 2 + B) % 5`.
   - This means we only need to keep track of the current number's remainder when divided by 5.
3. **Algorithm Strategy**:
   - Initialize `current_remainder = 0`.
   - Iterate through the array `nums`:
     - Update `current_remainder = (current_remainder * 2 + num) % 5`.
     - Record `true` if `current_remainder == 0`, else `false`.
4. **Complexity**:
   - Time Complexity: O(N) as we process each element once.
   - Space Complexity: O(1) extra space (besides storing the boolean result)."""
    
    answer = """def prefixesDivBy5(nums: list[int]) -> list[bool]:
    res = []
    curr = 0
    for num in nums:
        curr = (curr * 2 + num) % 5
        res.append(curr == 0)
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef prefixesDivBy5(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        ans = prefixesDivBy5(nums)\n        print(\" \".join(['true' if x else 'false' for x in ans]))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nvector<bool> prefixesDivBy5(vector<int>& nums) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<Boolean> prefixesDivBy5(int[] nums) {\n        // User logic\n        return new ArrayList<>();\n    }\n}",
        "javascript": "function prefixesDivBy5(nums) {\n    // User logic\n}",
        "c": "bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "0 1 1", "expected_output": "true false false", "is_sample": True},
        {"input": "1 1 1", "expected_output": "false false false", "is_sample": True},
        {"input": "1 0 1", "expected_output": "false false true", "is_sample": False},
        {"input": "1 1 0 0 1 1", "expected_output": "false false false false false false", "is_sample": False},
        {"input": "0 0 0", "expected_output": "true true true", "is_sample": False},
        {"input": "1 1 0 0", "expected_output": "false false false false", "is_sample": False},
        {"input": "0 1 0 1 1", "expected_output": "true false false false false", "is_sample": False},
        {"input": "1 0 1 0", "expected_output": "false false true true", "is_sample": False},
        # Stress cases
        {"input": " ".join(["0"] * 10000), "expected_output": " ".join(["true"] * 10000), "is_sample": False},
        {"input": " ".join(["1"] * 100) + " " + " ".join(["0"] * 100), "expected_output": "false " * 199 + "false", "is_sample": False}
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
        "topics": ["Array", "Math"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1018_Binary_Prefix_Divisible_By_5.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
