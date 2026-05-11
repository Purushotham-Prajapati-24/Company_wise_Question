import json
import os

def generate_json():
    problem_id = 704
    title = "Binary Search"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>704. Binary Search</h3>
<p>Given an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in nums and its index is 4
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in nums so return -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt; Gnums[i], target &lt; 10<sup>4</sup></code></li>
	<li>All the integers in <code>nums</code> are <b>unique</b>.</li>
	<li><code>nums</code> is sorted in ascending order.</li>
</ul>"""

    input_format = "Two lines: 1) Space-separated sorted integers 2) the target integer."
    output_format = "A single integer representing the zero-indexed position or -1."
    
    constraints = [
        "1 <= nums.length <= 10^4",
        "Unique elements, sorted ascending.",
        "O(log N) time complexity required.",
        "O(1) extra space."
    ]
    
    explanation = """To search for a target in a sorted array with logarithmic time complexity:
1. **The Principle (Binary Search)**:
   - Maintain a search range defined by `left = 0` and `right = len(nums) - 1`.
   - While `left <= right`:
     - Calculate the midpoint `mid = left + (right - left) // 2`.
     - If `nums[mid] == target`, return `mid`.
     - If `nums[mid] < target`, the target must be in the right half, so set `left = mid + 1`.
     - Otherwise, move to the left half with `right = mid - 1`.
2. **Result**: If the loop finishes without finding the target, return -1.
3. **Complexity**:
   - Time Complexity: O(log N) because the search space is halved at each step.
   - Space Complexity: O(1)."""
    
    answer = """def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1"""

    boilerplate = {
        "python": "import sys\n\ndef search(nums, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        nums = list(map(int, lines[0].split()))\n        target = int(lines[1])\n        print(search(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint search(vector<int>& nums, int target) {\n    // User logic\n    return -1;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int search(int[] nums, int target) {\n        // User logic\n        return -1;\n    }\n}",
        "javascript": "function search(nums, target) {\n    // User logic\n}",
        "c": "int search(int* nums, int numsSize, int target) {\n    // User logic\n    return -1;\n}"
    }

    test_cases = [
        {"input": "-1 0 3 5 9 12\\n9", "expected_output": "4", "is_sample": True},
        {"input": "-1 0 3 5 9 12\\n2", "expected_output": "-1", "is_sample": True},
        {"input": "5\\n5", "expected_output": "0", "is_sample": False},
        {"input": "5\\n2", "expected_output": "-1", "is_sample": False},
        {"input": "1 3 5 7 9\\n3", "expected_output": "1", "is_sample": False},
        {"input": "1 3 5 7 9\\n9", "expected_output": "4", "is_sample": False},
        {"input": "1 3 5 7 9\\n1", "expected_output": "0", "is_sample": False},
        {"input": "2 5\\n0", "expected_output": "-1", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n9999", "expected_output": "9999", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n-1", "expected_output": "-1", "is_sample": False}
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

    output_path = "601-800/704_Binary_Search.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
