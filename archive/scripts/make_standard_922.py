import json
import os

def generate_json():
    problem_id = 922
    title = "Sort Array By Parity II"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>922. Sort Array By Parity II</h3>
<p>Given an array of integers <code>nums</code>, half of the integers in <code>nums</code> are <b>odd</b>, and half of the integers are <b>even</b>.</p>

<p>Sort the array so that whenever <code>nums[i]</code> is odd, <code>i</code> is odd, and whenever <code>nums[i]</code> is even, <code>i</code> is even.</p>

<p>Return <em>any answer array that satisfies this condition</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [4,2,5,7]
<strong>Output:</strong> [4,5,2,7]
<strong>Explanation:</strong> [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [2,3]
<strong>Output:</strong> [2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>nums.length</code> is even.</li>
	<li>Half of the integers in <code>nums</code> are even.</li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow Up:</strong> Could you solve it in-place?</p>"""

    input_format = "A single line containing space-separated integers."
    output_format = "A single line containing space-separated integers (any valid permutation)."
    
    constraints = [
        "2 <= n <= 20,000",
        "n is even.",
        "Exactly n/2 odd and n/2 even integers.",
        "O(N) time complexity.",
        "O(1) extra space (in-place)."
    ]
    
    explanation = """To sort the array such that evens are at even indices and odds are at odd indices:
1. **The In-Place Strategy (Two-Pointer)**:
   - Use two pointers: `even` starting at 0 and `odd` starting at 1.
   - Increment `even` by 2 as long as `nums[even]` is correctly an even number.
   - Increment `odd` by 2 as long as `nums[odd]` is correctly an odd number.
   - If `nums[even]` is odd and `nums[odd]` is even, swap them. This fixes both at once.
   - Continue until one of the pointers goes out of bounds.
2. **Alternative Strategy (Extra Array)**:
   - Initialize an empty array `res` of length N.
   - Put even numbers at `0, 2, 4...` and odd numbers at `1, 3, 5...`.
3. **Complexity**:
   - Time Complexity: O(N) because each element is visited at most once.
   - Space Complexity: O(1) if swapped in-place, or O(N) if using a result array."""
    
    answer = """def sortArrayByParityII(nums: list[int]) -> list[int]:
    n = len(nums)
    j = 1 # odd pointer
    for i in range(0, n, 2): # even indices
        if nums[i] % 2 != 0: # found odd at even index
            while nums[j] % 2 != 0: # find first even at odd index
                j += 2
            nums[i], nums[j] = nums[j], nums[i]
    return nums"""

    boilerplate = {
        "python": "import sys\n\ndef sortArrayByParityII(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        ans = sortArrayByParityII(nums)\n        print(\" \".join(map(str, ans)))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<int> sortArrayByParityII(vector<int>& nums) {\n    // User logic\n    return nums;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[] sortArrayByParityII(int[] nums) {\n        // User logic\n        return nums;\n    }\n}",
        "javascript": "function sortArrayByParityII(nums) {\n    // User logic\n}",
        "c": "int* sortArrayByParityII(int* nums, int numsSize, int* returnSize) {\n    // User logic\n    return nums;\n}"
    }

    test_cases = [
        {"input": "4 2 5 7", "expected_output": "4 5 2 7", "is_sample": True},
        {"input": "2 3", "expected_output": "2 3", "is_sample": True},
        {"input": "1 2", "expected_output": "2 1", "is_sample": False},
        {"input": "4 1 2 3", "expected_output": "4 1 2 3", "is_sample": False},
        {"input": "0 1 0 1", "expected_output": "0 1 0 1", "is_sample": False},
        {"input": "1 0 1 0", "expected_output": "0 1 0 1", "is_sample": False},
        {"input": "8 2 6 4 1 3 5 7", "expected_output": "8 1 6 3 4 5 2 7", "is_sample": False},
        {"input": "1 3 5 7 2 4 6 8", "expected_output": "2 1 4 3 6 5 8 7", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i%2) for i in range(20000)]), "expected_output": "CUSTOM_VALIDATION", "is_sample": False},
        {"input": " ".join(["0", "1"] * 10000), "expected_output": "0 1 " * 10000, "is_sample": False}
    ]
    # Note: For expected_output in 9, I will use a simple valid case to avoid complex validation strings
    test_cases[8]["expected_output"] = " ".join(["0" if i % 2 == 0 else "1" for i in range(20000)])

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
        "topics": ["Array", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "801-1000/922_Sort_Array_By_Parity_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
