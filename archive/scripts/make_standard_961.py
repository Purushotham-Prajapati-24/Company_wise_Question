import json
import os

def generate_json():
    problem_id = 961
    title = "N-Repeated Element in Size 2N Array"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>961. N-Repeated Element in Size 2N Array</h3>
<p>You are given an integer array <code>nums</code> with the following properties:</p>

<ul>
	<li><code>nums.length == 2 * n</code>.</li>
	<li><code>nums</code> contains <code>n + 1</code> unique elements.</li>
	<li>Exactly one element of <code>nums</code> is repeated <code>n</code> times.</li>
</ul>

<p>Return <em>the element that is repeated </em><code>n</code><em> times</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,2,3,3]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [2,1,2,5,3,2]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> nums = [5,1,5,2,5,3,5,4]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5000</code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <code>n + 1</code> unique elements and one of them is repeated exactly <code>n</code> times.</li>
</ul>"""

    input_format = "A single line containing space-separated integers."
    output_format = "An integer representing the element that repeats n times."
    
    constraints = [
        "2 * n = array length",
        "2 <= n <= 5,000",
        "n + 1 unique elements.",
        "Exactly one element repeats n times.",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To find the element that repeats N times in an array of size 2N:
1. **The Core Insight**:
   - The array has 2N elements and N+1 unique elements.
   - N elements appear exactly once, and 1 element appears exactly N times.
   - This means as soon as we find *any* element that appears more than once, it must be the N-repeated element.
2. **Algorithm Strategy (Hash Set)**:
   - Use a hash set to track elements we have seen so far.
   - Iterate through the array.
   - If an element is already in the set, return it immediately.
3. **Optimized Constant Space Approach**:
   - In a 2N array where one element occurs N times, the repeated element must be close to another instance of itself.
   - Specifically, for N > 2, the repeated element will appear at least once in a window of size 3 (e.g., `nums[i] == nums[i+1]` or `nums[i] == nums[i+2]`).
   - For smaller N (N=2), you might need to check distance 3 (`nums[i] == nums[i+3]`).
4. **Complexity**:
   - Time Complexity: O(N) because we iterate through the array at most once.
   - Space Complexity: O(N) for the hash set, or O(1) for the window optimization."""
    
    answer = """def repeatedNTimes(nums: list[int]) -> int:
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
    return -1 # Should never happen"""

    boilerplate = {
        "python": "import sys\n\ndef repeatedNTimes(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        print(repeatedNTimes(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_set>\n\nusing namespace std;\n\nint repeatedNTimes(vector<int>& nums) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int repeatedNTimes(int[] nums) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function repeatedNTimes(nums) {\n    // User logic\n}",
        "c": "int repeatedNTimes(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 3", "expected_output": "3", "is_sample": True},
        {"input": "2 1 2 5 3 2", "expected_output": "2", "is_sample": True},
        {"input": "5 1 5 2 5 3 5 4", "expected_output": "5", "is_sample": True},
        {"input": "1 1 2 3", "expected_output": "1", "is_sample": False},
        {"input": "9 4 3 3", "expected_output": "3", "is_sample": False},
        {"input": "1 2 3 1", "expected_output": "1", "is_sample": False},
        {"input": "0 1 2 0", "expected_output": "0", "is_sample": False},
        {"input": "4 1 5 4", "expected_output": "4", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(5000)]) + " " + " ".join(["5000"] * 5000), "expected_output": "5000", "is_sample": False},
        {"input": " ".join(["7"] * 5000) + " " + " ".join([str(i) for i in range(5000)]), "expected_output": "7", "is_sample": False}
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "801-1000/961_N-Repeated_Element_in_Size_2N_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
