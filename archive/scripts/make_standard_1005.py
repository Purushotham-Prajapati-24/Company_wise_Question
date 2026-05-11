import json
import os

def generate_json():
    problem_id = 1005
    title = "Maximize Sum Of Array After K Negations"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1005. Maximize Sum Of Array After K Negations</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, modify the array in the following way:</p>

<ul>
	<li>choose an index <code>i</code> and replace <code>nums[i]</code> with <code>-nums[i]</code>.</li>
</ul>

<p>You should apply this process exactly <code>k</code> times. You may choose the same index <code>i</code> multiple times.</p>

<p>Return <em>the largest possible sum of the array after modifying it in this way</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [4,2,3], k = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> Choose index 1 and nums becomes [4,-2,3]. The sum is 4 + -2 + 3 = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [3,-1,0,2], k = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> Choose index 1, nums becomes [3,1,0,2]. Then choose index 1 AGAIN, nums becomes [3,-1,0,2]. Finally, choose index 1 for the third time, nums becomes [3,1,0,2]. The sum is 3 + 1 + 0 + 2 = 6.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> nums = [2,-3,-1,5,-4], k = 2
<strong>Output:</strong> 13
<strong>Explanation:</strong> Choose indices 1 and 4, nums becomes [2,3,-1,5,4]. The sum is 2 + 3 + -1 + 5 + 4 = 13.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two lines. Line 1: integer k. Line 2: space-separated integers for nums."
    output_format = "An integer representing the maximum possible sum."
    
    constraints = [
        "1 <= n <= 10,000",
        "-100 <= nums[i] <= 100",
        "1 <= k <= 10,000",
        "O(N log N) time complexity.",
        "O(1) extra space (excluding sorting space)."
    ]
    
    explanation = """To maximize the sum of an array after K negations:
1. **The Greedy Principle**:
   - Negating a negative number increases the total sum.
   - We should prioritize negating the most negative numbers.
2. **Algorithm Strategy**:
   - Sort the array `nums` in increasing order.
   - Iterate through the sorted array. If we encounter a negative number and `k > 0`:
     - Negate it (`nums[i] = -nums[i]`).
     - Decrement `k`.
   - After processing negative numbers, if `k` is still greater than 0:
     - If `k % 2 == 1`, we must negate an element exactly one more time (since negating twice cancels out).
     - To minimize the loss, we should negate the smallest absolute element currently in the array.
     - Sort again or just find the minimum element in the current array and negate it.
3. **Complexity**:
   - Time Complexity: O(N log N) due to sorting.
   - Space Complexity: O(1) as we modify the array in-place."""
    
    answer = """def largestSumAfterKNegations(nums: list[int], k: int) -> int:
    nums.sort()
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
        elif nums[i] >= 0:
            break
            
    # If k is still odd, negate the smallest value in the modified array
    if k % 2 == 1:
        nums.sort()
        nums[0] = -nums[0]
        
    return sum(nums)"""

    boilerplate = {
        "python": "import sys\n\ndef largestSumAfterKNegations(nums, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        k = int(lines[0].strip())\n        nums = list(map(int, lines[1].strip().split()))\n        print(largestSumAfterKNegations(nums, k))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <numeric>\n\nusing namespace std;\n\nint largestSumAfterKNegations(vector<int>& nums, int k) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int largestSumAfterKNegations(int[] nums, int k) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function largestSumAfterKNegations(nums, k) {\n    // User logic\n}",
        "c": "int largestSumAfterKNegations(int* nums, int numsSize, int k) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1\\n4 2 3", "expected_output": "5", "is_sample": True},
        {"input": "3\\n3 -1 0 2", "expected_output": "6", "is_sample": True},
        {"input": "2\\n2 -3 -1 5 -4", "expected_output": "13", "is_sample": True},
        {"input": "10\\n1 1 1", "expected_output": "3", "is_sample": False},
        {"input": "1\\n-8 3 -5 -3 -5 -2", "expected_output": "13", "is_sample": False},
        {"input": "5\\n-2 5 -3 4 -1 1 0", "expected_output": "16", "is_sample": False},
        {"input": "1\\n0 0 0", "expected_output": "0", "is_sample": False},
        {"input": "1\\n-1 -1 -1", "expected_output": "-1", "is_sample": False},
        # Stress cases
        {"input": "10000\\n" + " ".join(["-100"] * 10000), "expected_output": "1000000", "is_sample": False},
        {"input": "1\\n" + " ".join([str(i) for i in range(-5000, 5000)]), "expected_output": str(sum(i for i in range(-5000, 5000)) + 10000), "is_sample": False}
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
        "topics": ["Array", "Greedy", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1005_Maximize_Sum_Of_Array_After_K_Negations.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
