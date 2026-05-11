import json
import os

def generate_json():
    problem_id = 643
    title = "Maximum Average Subarray I"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>643. Maximum Average Subarray I</h3>
<p>You are given an integer array <code>nums</code> consisting of <code>n</code> elements, and an integer <code>k</code>.</p>

<p>Find a contiguous subarray whose <b>length is equal to</b> <code>k</code> that has the maximum average value and return this value. Any answer with a calculation error less than <code>10<sup>-5</sup></code> will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,12,-5,-6,50,3], k = 4
<strong>Output:</strong> 12.75000
<strong>Explanation:</strong> Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [5], k = 1
<strong>Output:</strong> 5.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two lines: 1) space-separated integers for nums 2) single integer k."
    output_format = "A single floating point number representing the maximum average value."
    
    constraints = [
        "1 <= k <= n <= 10^5",
        "O(N) time complexity.",
        "O(1) extra space.",
        "Precision within 10^-5 required."
    ]
    
    explanation = """To find the maximum average subarray of length $k$:
1. **The Insight**:
   - Maximizing the average is equivalent to maximizing the **sum**, because $Avg = Sum / k$ and $k$ is constant.
2. **Implementation (Sliding Window)**:
   - Initial Sum: Calculate the sum of the first $k$ elements ($nums[0 \dots k-1]$).
   - Slid: Traverse from $i = k$ to $n-1$:
     - Add `nums[i]` to `curr_sum`.
     - Subtract `nums[i-k]` from `curr_sum`.
     - Update `max_sum` if `curr_sum > max_sum`.
3. **Return**:
   - Return `max_sum / k`.
4. **Complexity**:
   - Time Complexity: O(N) as we traverse the array once.
   - Space Complexity: O(1)."""
    
    answer = """def findMaxAverage(nums: list[int], k: int) -> float:
    # Initial window sum
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i-k]
        if curr_sum > max_sum:
            max_sum = curr_sum
            
    return max_sum / k"""

    boilerplate = {
        "python": "import sys\n\ndef findMaxAverage(nums, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        nums = list(map(int, lines[0].strip().split()))\n        k = int(lines[1].strip())\n        print(f\"{findMaxAverage(nums, k):.5f}\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <numeric>\n#include <iomanip>\n\nusing namespace std;\n\ndouble findMaxAverage(vector<int>& nums, int k) {\n    // User logic\n    return 0.0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public double findMaxAverage(int[] nums, int k) {\n        // User logic\n        return 0.0;\n    }\n}",
        "javascript": "function findMaxAverage(nums, k) {\n    // User logic\n}",
        "c": "double findMaxAverage(int* nums, int numsSize, int k) {\n    // User logic\n    return 0.0;\n}"
    }

    test_cases = [
        {"input": "1 12 -5 -6 50 3\\n4", "expected_output": "12.75000", "is_sample": True},
        {"input": "5\\n1", "expected_output": "5.00000", "is_sample": True},
        {"input": "1 2 3 4 5\\n2", "expected_output": "4.50000", "is_sample": False},
        {"input": "0 1 1 3 3\\n4", "expected_output": "2.00000", "is_sample": False},
        {"input": " -1\\n1", "expected_output": "-1.00000", "is_sample": False},
        {"input": "1 2 3\\n3", "expected_output": "2.00000", "is_sample": False},
        {"input": "-1 -2 -3 -4 -5\\n3", "expected_output": "-2.00000", "is_sample": False},
        {"input": "100 0 100 0\\n2", "expected_output": "50.00000", "is_sample": False},
        # Stress cases
        {"input": " ".join(["10000"] * 100000) + "\\n1", "expected_output": "10000.00000", "is_sample": False},
        {"input": " ".join([str(i%100) for i in range(100000)]) + "\\n10000", "expected_output": "49.50000", "is_sample": False}
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
        "topics": ["Array", "Sliding Window"],
        "companyIndex": 0
    }

    output_path = "601-800/643_Maximum_Average_Subarray_I.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
