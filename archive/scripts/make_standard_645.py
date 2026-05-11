import json
import os

def generate_json():
    problem_id = 645
    title = "Set Mismatch"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>645. Set Mismatch</h3>
<p>You have a set of integers <code>s</code>, which originally contains all the numbers from <code>1</code> to <code>n</code>. Unfortunately, due to some error, one of the numbers in <code>s</code> got duplicated to another number in the set, which results in <b>repetition of one number and loss of another number</b>.</p>

<p>You are given an integer array <code>nums</code> representing the data status of this set after the error.</p>

<p>Find the number that occurs twice and the number that is missing and return them in the form of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,2,2,4]
<strong>Output:</strong> [2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the array nums."
    output_format = "Two space-separated integers: the duplicate number and the missing number."
    
    constraints = [
        "2 <= nums.length <= 10^4",
        "Unique duplicate and unique missing.",
        "O(N) time complexity.",
        "O(N) extra space or O(1) with modification."
    ]
    
    explanation = """To find the duplicate and missing numbers in a set of $[1, n]$:
1. **The Strategy (Frequency Array)**:
   - Create a frequency array (or hash map) of size $n+1$.
   - Iterate through `nums` and count occurrences.
   - The number with frequency 2 is the **duplicate**.
   - The number with frequency 0 (in the range $[1, n]$) is the **missing** one.
2. **Alternative (Math)**:
   - Sum of first $n$ numbers: $S_n = n(n+1)/2$.
   - Sum of squares: $Sq_n = n(n+1)(2n+1)/6$.
   - Let $d$ be duplicate and $m$ be missing.
   - $\sum nums = S_n + d - m$.
   - $\sum nums^2 = Sq_n + d^2 - m^2$.
   - Solve for $d$ and $m$.
3. **Complexity**:
   - Time Complexity: O(N) to traverse the array.
   - Space Complexity: O(N) for frequency tracking or O(1) if modifying input."""
    
    answer = """def findErrorNums(nums: list[int]) -> list[int]:
    n = len(nums)
    counts = [0] * (n + 1)
    for x in nums:
        counts[x] += 1
    
    dup = -1
    miss = -1
    for i in range(1, n + 1):
        if counts[i] == 2:
            dup = i
        elif counts[i] == 0:
            miss = i
    return [dup, miss]"""

    boilerplate = {
        "python": "import sys\n\ndef findErrorNums(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        res = findErrorNums(nums)\n        print(f\"{res[0]} {res[1]}\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <numeric>\n\nusing namespace std;\n\nvector<int> findErrorNums(vector<int>& nums) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[] findErrorNums(int[] nums) {\n        // User logic\n        return new int[2];\n    }\n}",
        "javascript": "function findErrorNums(nums) {\n    // User logic\n}",
        "c": "int* findErrorNums(int* nums, int numsSize, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 2 2 4", "expected_output": "2 3", "is_sample": True},
        {"input": "1 1", "expected_output": "1 2", "is_sample": True},
        {"input": "2 2", "expected_output": "2 1", "is_sample": False},
        {"input": "3 2 1 1", "expected_output": "1 4", "is_sample": False},
        {"input": "1 2 3 4 5 5", "expected_output": "5 6", "is_sample": False},
        {"input": "1 3 3 4", "expected_output": "3 2", "is_sample": False},
        {"input": "1 2 3 4 5 6 7 8 8 10", "expected_output": "8 9", "is_sample": False},
        {"input": "10 9 8 7 6 5 4 3 2 2", "expected_output": "2 1", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 10000)]) + " 1", "expected_output": "1 10000", "is_sample": False},
        {"input": " ".join([str(i) for i in range(2, 10001)]) + " 2", "expected_output": "2 1", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Math", "Sorting"],
        "companyIndex": 0
    }

    output_path = "601-800/645_Set_Mismatch.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
