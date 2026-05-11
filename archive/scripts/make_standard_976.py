import json
import os

def generate_json():
    problem_id = 976
    title = "Largest Perimeter Triangle"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>976. Largest Perimeter Triangle</h3>
<p>Given an integer array <code>nums</code>, return <em>the largest perimeter of a triangle with a non-zero area, formed from three of these lengths</em>. If it is impossible to form any triangle of a non-zero area, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [2,1,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can form a triangle with side lengths 1, 2, and 2, which has a perimeter of 1 + 2 + 2 = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,2,1,10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
You cannot use the side lengths 1, 1, and 2 to form a triangle because 1 + 1 is not greater than 2.
You cannot use the side lengths 1, 1, and 10 to form a triangle because 1 + 1 is not greater than 10.
You cannot use the side lengths 1, 2, and 10 to form a triangle because 1 + 2 is not greater than 10.
Since we cannot form any triangle from the side lengths, we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers."
    output_format = "An integer representing the largest possible perimeter, or 0 if no triangle can be formed."
    
    constraints = [
        "3 <= n <= 10,000",
        "1 <= nums[i] <= 1,000,000",
        "O(N log N) time complexity.",
        "O(1) extra space (excluding sorting space)."
    ]
    
    explanation = """To find the largest possible perimeter of a triangle from the given lengths:
1. **The Triangle Condition**:
   - For three lengths `a, b, c` (where `a <= b <= c`) to form a non-zero area triangle, they must satisfy `a + b > c`.
2. **Algorithm Strategy (Greedy)**:
   - Sort the array `nums` in descending order: `nums[0] >= nums[1] >= ... >= nums[n-1]`.
   - Iterate through the sorted array looking for the first triplet `(nums[i], nums[i+1], nums[i+2])` that satisfies the triangle condition.
   - Since `nums[i] >= nums[i+1] >= nums[i+2]`, we only need to check if `nums[i+1] + nums[i+2] > nums[i]`.
   - The first triplet that satisfies this condition will have the largest possible perimeter because we are checking the largest elements first.
3. **Complexity**:
   - Time Complexity: O(N log N) due to sorting. The linear scan takes O(N).
   - Space Complexity: O(1) or O(log N) depending on the sorting implementation."""
    
    answer = """def largestPerimeter(nums: list[int]) -> int:
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        if nums[i+1] + nums[i+2] > nums[i]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0"""

    boilerplate = {
        "python": "import sys\n\ndef largestPerimeter(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        print(largestPerimeter(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint largestPerimeter(vector<int>& nums) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int largestPerimeter(int[] nums) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function largestPerimeter(nums) {\n    // User logic\n}",
        "c": "int largestPerimeter(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2 1 2", "expected_output": "5", "is_sample": True},
        {"input": "1 2 1 10", "expected_output": "0", "is_sample": True},
        {"input": "3 2 3 4", "expected_output": "10", "is_sample": False},
        {"input": "3 6 2 3", "expected_output": "8", "is_sample": False},
        {"input": "1 1 1", "expected_output": "3", "is_sample": False},
        {"input": "100 1 1", "expected_output": "0", "is_sample": False},
        {"input": "10 5 4 3 2", "expected_output": "12", "is_sample": False},
        {"input": "1 2 3 4 5 6 7 8 9 10", "expected_output": "27", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 10001)]), "expected_output": "29997", "is_sample": False},
        {"input": " ".join([str(10**6) if i % 2 == 0 else "1" for i in range(10000)]), "expected_output": "0", "is_sample": False}
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
        "topics": ["Array", "Math", "Greedy", "Sorting"],
        "companyIndex": 0
    }

    output_path = "801-1000/976_Largest_Perimeter_Triangle.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
