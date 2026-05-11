import json
import os

def generate_json():
    problem_id = 164
    title = "Maximum Gap"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>164. Maximum Gap</h3>
<p>Given an integer array <code>nums</code>, return <em>the maximum difference between two successive elements in its sorted form</em>. If the array contains less than two elements, return <code>0</code>.</p>

<p>You must write an algorithm that runs in <strong>linear time</strong> and uses <strong>linear extra space</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,6,9,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The array contains less than 2 elements, therefore return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the array nums."
    output_format = "An integer representing the maximum gap."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "0 <= nums[i] <= 10^9",
        "Time Complexity: O(n)",
        "Space Complexity: O(n)"
    ]
    
    explanation = """To find the maximum gap in O(n) time and space, we use the **Bucket Sort** principle (based on the Pigeonhole Principle):
1. **Range and Bucket Size**:
   - Find the minimum (`min_val`) and maximum (`max_val`) in the array.
   - If `n < 2` or `min_val == max_val`, the gap is 0.
   - The minimum possible "maximum gap" is `ceil((max_val - min_val) / (n - 1))`. Let this be `gap_size`.
2. **Bucket Distribution**:
   - Create `n-1` buckets. Each bucket will store the `min` and `max` values of the elements falling into its range.
   - The range for bucket `i` is `[min_val + i * gap_size, min_val + (i + 1) * gap_size)`.
3. **Pigeonhole Principle**:
   - Since we have `n` elements and `n-1` gaps between them in sorted order, the maximum gap MUST be at least `gap_size`.
   - Therefore, the maximum gap cannot occur within a single bucket (as the range of a bucket is `gap_size`). It must occur between the `max` of one non-empty bucket and the `min` of the next non-empty bucket.
4. **Final Step**:
   - Iterate through the buckets, tracking the `prev_max`. For each non-empty bucket, calculate `curr_min - prev_max` and update the `max_gap`.
5. **Complexity**:
   - Time Complexity: O(n) for finding min/max and filling buckets.
   - Space Complexity: O(n) for the buckets."""
    
    answer = """class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
            
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
            
        n = len(nums)
        # Min gap size based on Pigeonhole Principle
        gap_size = max(1, (max_val - min_val) // (n - 1))
        # Number of buckets needed
        bucket_count = (max_val - min_val) // gap_size + 1
        
        buckets_min = [float('inf')] * bucket_count
        buckets_max = [float('-inf')] * bucket_count
        
        # Fill buckets
        for x in nums:
            idx = (x - min_val) // gap_size
            buckets_min[idx] = min(buckets_min[idx], x)
            buckets_max[idx] = max(buckets_max[idx], x)
            
        max_gap = 0
        prev_max = min_val
        
        # Calculate gap between buckets
        for i in range(bucket_count):
            if buckets_min[i] == float('inf'):
                continue
            max_gap = max(max_gap, buckets_min[i] - prev_max)
            prev_max = buckets_max[i]
            
        return max_gap"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef maximumGap(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    if not input_data: sys.exit()\n    nums = [int(x) for x in input_data]\n    print(maximumGap(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <cmath>\nusing namespace std;\n\nint maximumGap(vector<int>& nums) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int maximumGap(int[] nums) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maximumGap = function(nums) {\n    // User logic\n};",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <limits.h>\n\nint maximumGap(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3 6 9 1", "expected_output": "3", "is_sample": True},
        {"input": "10", "expected_output": "0", "is_sample": True},
        {"input": "1 100", "expected_output": "99", "is_sample": False},
        {"input": "1 1 1 1", "expected_output": "0", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "1", "is_sample": False},
        {"input": "1 10 20 30 40", "expected_output": "10", "is_sample": False},
        {"input": "10 5 100 2 80", "expected_output": "75", "is_sample": False},
        # Stress Tests
        {"input": " ".join(map(str, range(0, 100001, 10))), "expected_output": "10", "is_sample": False},
        {"input": "0 1000000000", "expected_output": "1000000000", "is_sample": False},
        {"input": "1 3 5 7 9 11 13 1000000000", "expected_output": "999999987", "is_sample": False}
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
        "topics": ["Array", "Sorting", "Bucket Sort", "Radix Sort"],
        "companyIndex": 0
    }

    output_path = "1-200/164_Maximum_Gap.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
