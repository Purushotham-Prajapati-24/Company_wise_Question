import json
import os

def generate_json():
    # 360. Sort Transformed Array
    problem_id = 360
    title = "Sort Transformed Array"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>360. Sort Transformed Array</h3>
<p>Given a <strong>sorted</strong> integer array <code>nums</code> and three integers <code>a</code>, <code>b</code>, and <code>c</code>, apply a quadratic function of the form <code>f(x) = ax<sup>2</sup> + bx + c</code> to each element <code>nums[i]</code> in the array, and return the array in a <strong>sorted</strong> order.</p>

<p>You must write an algorithm that runs in <code>O(n)</code> time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [-4,-2,2,4], a = 1, b = 3, c = 5
<strong>Output:</strong> [3,9,15,33]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-4,-2,2,4], a = -1, b = 3, c = 5
<strong>Output:</strong> [-23,-5,1,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>-100 &lt;= nums[i], a, b, c &lt;= 100</code></li>
	<li><code>nums</code> is sorted in ascending order.</li>
</ul>"""

    input_format = "Sorted array `nums`, and integers `a`, `b`, `c` defining the quadratic function."
    output_format = "Sorted results after applying the function."
    
    constraints = [
        "1 <= nums.length <= 200",
        "-100 <= nums[i], a, b, c <= 100",
        "Input array is already sorted in ascending order.",
        "Must run in O(n) time."
    ]
    
    explanation = """### Comprehensive Explanation for 360. Sort Transformed Array

This problem asks to transform a sorted array using a quadratic function $f(x) = ax^2 + bx + c$ and return the result in sorted order. While a naive $O(N \log N)$ sorting approach works, the requirement is $O(N)$.

#### Mathematical Intuition (Properties of Quadratics)
The behavior of the function $f(x) = ax^2 + bx + c$ is determined by the coefficient $a$:

1.  **$a > 0$ (Parabola opens UP)**:
    - The largest values are found at the ends of the range (far from the vertex), and the smallest value is near the vertex (middle of the curve).
    - Thus, to build the sorted array from largest to smallest, we compare the values at the ends of the input array using two pointers.

2.  **$a < 0$ (Parabola opens DOWN)**:
    - The smallest values are at the ends of the range, and the largest value is near the vertex.
    - Thus, to build the sorted array from smallest to largest, we compare the values at the ends.

3.  **$a = 0$ (Linear function $f(x) = bx + c$)**:
    - If $b \ge 0$, the function is non-decreasing; the order remains the same.
    - If $b < 0$, the function is non-increasing; the order is reversed.
    - Both behaviors can be handled by the same two-pointer logic as $a \ge 0$ (monotonically increasing) or $a < 0$ logic.

#### Most Optimized Approach in Python (Two Pointers)
We use two pointers, `left` and `right`, starting at the ends of the input array.

- **For $a \ge 0$**:
  - We pick the larger of $f(nums[left])$ or $f(nums[right])$ and place it at the **end** of the result array, then shrink the pointer inward.
- **For $a < 0$**:
  - We pick the smaller of $f(nums[left])$ or $f(nums[right])$ and place it at the **beginning** of the result array, then shrink the pointer inward.

#### Complexity Analysis
- **Time Complexity**: $O(N)$ because each element is visited exactly once.
- **Space Complexity**: $O(1)$ extra space if we don't count the output array.

### Optimization Note
Even though $N$ is small (200), the linear time complexity ensures performance remains consistent even if $N$ were scaled to millions."""

    answer = """class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        \"\"\"
        Transforms nums into f(x) = ax^2 + bx + c and returns sorted list in O(N).
        \"\"\"
        def f(x):
            return a*x*x + b*x + c
            
        n = len(nums)
        left, right = 0, n - 1
        res = [0] * n
        
        # Behavior depends on vertex and parabola concavity
        if a >= 0:
            # Largest values are at the ends
            idx = n - 1
            while left <= right:
                val1, val2 = f(nums[left]), f(nums[right])
                if val1 >= val2:
                    res[idx] = val1
                    left += 1
                else:
                    res[idx] = val2
                    right -= 1
                idx -= 1
        else:
            # Smallest values are at the ends
            idx = 0
            while left <= right:
                val1, val2 = f(nums[left]), f(nums[right])
                if val1 <= val2:
                    res[idx] = val1
                    left += 1
                else:
                    res[idx] = val2
                    right -= 1
                idx += 1
                    
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def sortTransformedArray(self, nums: list[int], a: int, b: int, c: int) -> list[int]:\n        pass\n\nif __name__ == '__main__':\n    # handle input\n    pass",
        "cpp": "class Solution {\npublic:\n    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) { return {}; }\n};",
        "java": "class Solution {\n    public int[] sortTransformedArray(int[] nums, int a, int b, int c) { return new int[0]; }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @param {number} a\n * @param {number} b\n * @param {number} c\n * @return {number[]}\n */\nvar sortTransformedArray = function(nums, a, b, c) { return []; };",
        "c": "int* sortTransformedArray(int* nums, int numsSize, int a, int b, int c, int* returnSize) { return NULL; }"
    }

    test_cases = [
        # 1. Sample 1 (a > 0)
        {"input": '{"nums": [-4,-2,2,4], "a": 1, "b": 3, "c": 5}', "expected_output": "[3,9,15,33]", "is_sample": True},
        # 2. Sample 2 (a < 0)
        {"input": '{"nums": [-4,-2,2,4], "a": -1, "b": 3, "c": 5}', "expected_output": "[-23,-5,1,7]", "is_sample": True},
        # 3. Diverse: a = 0 (Linear increasing)
        {"input": '{"nums": [1, 2, 3], "a": 0, "b": 2, "c": 1}', "expected_output": "[3, 5, 7]", "is_sample": False},
        # 4. Diverse: a = 0 (Linear decreasing)
        {"input": '{"nums": [1, 2, 3], "a": 0, "b": -1, "c": 0}', "expected_output": "[-3, -2, -1]", "is_sample": False},
        # 5. Diverse: Vertex in middle
        {"input": '{"nums": [-10, 0, 10], "a": 1, "b": 0, "c": 0}', "expected_output": "[0, 100, 100]", "is_sample": False},
        # 6. Diverse: Large range nums
        {"input": '{"nums": [-100, 100], "a": 1, "b": 1, "c": 1}', "expected_output": "[9901, 10101]", "is_sample": False},
        # 7. Diverse: Constant function (a=b=0)
        {"input": '{"nums": [1, 5, 9], "a": 0, "b": 0, "c": 42}', "expected_output": "[42, 42, 42]", "is_sample": False},
        # 8. Stress: Max N=200, large a
        {"input": '{"nums": [i for i in range(-100, 100)], "a": 100, "b": 100, "c": 100}', "expected_output": "sorted([100*i*i + 100*i + 100 for i in range(-100, 100)])", "is_sample": False},
        # 9. Stress: Max N=200, large negative a
        {"input": '{"nums": [i for i in range(-100, 100)], "a": -100, "b": 1, "c": 1}', "expected_output": "sorted([-100*i*i + i + 1 for i in range(-100, 100)])", "is_sample": False},
        # 10. Stress: All identical numbers
        {"input": '{"nums": [10]*200, "a": 1, "b": 1, "c": 1}', "expected_output": "[111]*200", "is_sample": False}
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
        "topics": ["Array", "Math", "Two Pointers", "Sorting"],
        "companyIndex": 1
    }

    output_path = "301-500/360_Sort_Transformed_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path} with 10 test cases.")

if __name__ == "__main__":
    generate_json()
