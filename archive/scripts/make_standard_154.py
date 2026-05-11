import json
import os

def generate_json():
    problem_id = 154
    title = "Find Minimum in Rotated Sorted Array II"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>154. Find Minimum in Rotated Sorted Array II</h3>
<p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the array <code>nums = [0,1,2,4,4,4,5,6,7]</code> might become:</p>
<ul>
	<li><code>[4,5,6,7,0,1,2,4,4]</code> if it was rotated <code>4</code> times.</li>
	<li><code>[0,1,2,4,4,4,5,6,7]</code> if it was rotated <code>9</code> times.</li>
</ul>

<p>Notice that <strong>rotating</strong> an array <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 1 time results in the array <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>.</p>
<p>Given the sorted rotated array <code>nums</code> that may contain <strong>duplicates</strong>, return <em>the minimum element of this array</em>.</p>
<p>You must decrease the overall operation steps as much as possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,2,0,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li><code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> This problem is similar to&nbsp;<a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/" target="_blank">Find Minimum in Rotated Sorted Array</a>, but <code>nums</code> may contain <strong>duplicates</strong>. Would this affect the runtime complexity? How and why?</p>"""

    input_format = "A single line containing space-separated integers representing the rotated sorted array."
    output_format = "An integer representing the minimum element."
    
    constraints = [
        "1 <= nums.length <= 5000",
        "-5000 <= nums[i] <= 5000",
        "nums is sorted and rotated between 1 and n times.",
        "Must handle duplicates efficiently."
    ]
    
    explanation = """To find the minimum in a rotated sorted array with duplicates:
1. **Binary Search**: Use two pointers, `left` and `right`, initialized to the start and end of the array.
2. **Comparison**: Compare `nums[mid]` with `nums[right]`:
   - If `nums[mid] > nums[right]`: The minimum MUST be in the right half (excluding `mid`). So, `left = mid + 1`.
   - If `nums[mid] < nums[right]`: The minimum is in the left half (including `mid`) or at `mid`. So, `right = mid`.
   - If `nums[mid] == nums[right]`: We cannot determine which half contains the minimum because of duplicates (e.g., [3,3,1,3]). In this case, we safely decrement `right` by one (`right -= 1`) to reduce the search space while preserving the minimum.
3. **Complexity**:
   - Average Time Complexity: O(log n).
   - Worst Time Complexity: O(n) (when all elements are the same, e.g., [1,1,1,1]).
   - Space Complexity: O(1)."""
    
    answer = """class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                # Duplicates case: safely reduce search space
                right -= 1
                
        return nums[left]"""

    boilerplate = {
        "python": "import sys\n\ndef findMin(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if not line: sys.exit()\n    nums = [int(x) for x in line.replace('[','').replace(']','').replace(',',' ').split()]\n    print(findMin(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint findMin(vector<int>& nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    // Parsing logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int findMin(int[] nums) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar findMin = function(nums) {\n    // User logic\n};",
        "c": "#include <stdio.h>\n\nint findMin(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 3 5", "expected_output": "1", "is_sample": True},
        {"input": "2 2 2 0 1", "expected_output": "0", "is_sample": True},
        {"input": "3 3 1 3", "expected_output": "1", "is_sample": False},
        {"input": "1 1 1 1", "expected_output": "1", "is_sample": False},
        {"input": "10 1 10 10 10", "expected_output": "1", "is_sample": False},
        {"input": "1 1 2 0 0 1", "expected_output": "0", "is_sample": False},
        {"input": "3 1 3", "expected_output": "1", "is_sample": False},
        # Stress Tests
        {"input": " ".join(["2"]*2500 + ["1"] + ["2"]*2499), "expected_output": "1", "is_sample": False},
        {"input": " ".join(["1"]*5000), "expected_output": "1", "is_sample": False},
        {"input": " ".join([str(i) for i in range(5000)]), "expected_output": "0", "is_sample": False}
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
        "topics": ["Array", "Binary Search"],
        "companyIndex": 0
    }

    output_path = "1-200/154_Find_Minimum_in_Rotated_Sorted_Array_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
