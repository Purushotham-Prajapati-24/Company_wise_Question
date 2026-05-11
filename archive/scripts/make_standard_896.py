import json
import os

def generate_json():
    problem_id = 896
    title = "Monotonic Array"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>896. Monotonic Array</h3>
<p>An array is <b>monotonic</b> if it is either monotone increasing or monotone decreasing.</p>

<p>An array <code>nums</code> is monotone increasing if for all <code>i &lt;= j</code>, <code>nums[i] &lt;= nums[j]</code>. An array <code>nums</code> is monotone decreasing if for all <code>i &lt;= j</code>, <code>nums[i] &gt;= nums[j]</code>.</p>

<p>Given an integer array <code>nums</code>, return <code>true</code> <em>if the given array is monotonic, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,2,2,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [6,5,4,4]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,3,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "1 <= n <= 100,000",
        "-100,000 <= val <= 100,000",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To check if an array is monotonic in O(N) time:
1. **The Core Approach (Flags)**:
   - An array is monotonic if it doesn't have *both* increasing and decreasing steps.
   - Use two boolean flags: `increasing = True` and `decreasing = True`.
2. **Algorithm Steps**:
   - Iterate through the array from the second element to the last.
   - For each pair `(nums[i-1], nums[i])`:
     - If `nums[i-1] < nums[i]`: This step is increasing. Set `decreasing = False`.
     - If `nums[i-1] > nums[i]`: This step is decreasing. Set `increasing = False`.
   - After the loop, the array is monotonic if either `increasing` OR `decreasing` is still `True`.
3. **Complexity**:
   - Time Complexity: O(N) since we perform a single pass over the array.
   - Space Complexity: O(1) as we only use two boolean variables."""
    
    answer = """def isMonotonic(nums: list[int]) -> bool:
    inc = dec = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            inc = False
        if nums[i] < nums[i+1]:
            dec = False
    return inc or dec"""

    boilerplate = {
        "python": "import sys\n\ndef isMonotonic(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        print('true' if isMonotonic(nums) else 'false')",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nbool isMonotonic(vector<int>& nums) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean isMonotonic(int[] nums) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function isMonotonic(nums) {\n    // User logic\n}",
        "c": "bool isMonotonic(int* nums, int numsSize) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "1 2 2 3", "expected_output": "true", "is_sample": True},
        {"input": "6 5 4 4", "expected_output": "true", "is_sample": True},
        {"input": "1 3 2", "expected_output": "false", "is_sample": True},
        {"input": "1 1 1", "expected_output": "true", "is_sample": False},
        {"input": "1 2 3 2 1", "expected_output": "false", "is_sample": False},
        {"input": "5 4 3 2 1", "expected_output": "true", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "true", "is_sample": False},
        {"input": "1 2 1 2", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(100000)]), "expected_output": "true", "is_sample": False},
        {"input": " ".join([str(100000 - i) for i in range(100000)]), "expected_output": "true", "is_sample": False}
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

    output_path = "801-1000/896_Monotonic_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
