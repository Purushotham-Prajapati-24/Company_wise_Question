import json
import os

def generate_json():
    problem_id = 985
    title = "Sum of Even Numbers After Queries"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>985. Sum of Even Numbers After Queries</h3>
<p>You are given an integer array <code>nums</code> and an array <code>queries</code> where <code>queries[i] = [val<sub>i</sub>, index<sub>i</sub>]</code>.</p>

<p>For each query <code>i</code>, first, apply <code>nums[index<sub>i</sub>] = nums[index<sub>i</sub>] + val<sub>i</sub></code>, then print the sum of the even values of <code>nums</code>.</p>

<p>Return <em>an integer array </em><code>answer</code><em> where </em><code>answer[i]</code><em> is the answer to the </em><code>i<sup>th</sup></code><em> query</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
<strong>Output:</strong> [8,6,2,4]
<strong>Explanation:</strong> At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [1], queries = [[4,0]]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= val<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= index<sub>i</sub> &lt; nums.length</code></li>
</ul>"""

    input_format = "Two parts. Line 1: space-separated integers for nums. Subsequent lines: space-separated pairs [val, index] for each query."
    output_format = "A single line containing space-separated integers representing the answer to each query."
    
    constraints = [
        "1 <= n <= 10,000",
        "1 <= q <= 10,000",
        "-10,000 <= nums[i], val_i <= 10,000",
        "O(N + Q) time complexity.",
        "O(Q) space for result."
    ]
    
    explanation = """To efficiently calculate the sum of even numbers after each query:
1. **Initial Summation**:
   - First, calculate the sum of all even numbers in the initial `nums` array. Let this be `total_even_sum`.
2. **Incremental Updates**:
   - For each query `[val, index]`:
     - **Step A**: Check if the current value at `nums[index]` is even. If so, subtract it from `total_even_sum` because we are about to modify it.
     - **Step B**: Update the value: `nums[index] += val`.
     - **Step C**: Check if the *new* value at `nums[index]` is even. If so, add it to `total_even_sum`.
     - **Step D**: Store the updated `total_even_sum` as the result for this query.
3. **Complexity**:
   - Time Complexity: O(N + Q) where N is the size of `nums` (for initial sum) and Q is the number of queries (for incremental updates).
   - Space Complexity: O(Q) to store the result array."""
    
    answer = """def sumEvenAfterQueries(nums: list[int], queries: list[list[int]]) -> list[int]:
    total_even_sum = sum(x for x in nums if x % 2 == 0)
    ans = []
    for val, idx in queries:
        if nums[idx] % 2 == 0:
            total_even_sum -= nums[idx]
        nums[idx] += val
        if nums[idx] % 2 == 0:
            total_even_sum += nums[idx]
        ans.append(total_even_sum)
    return ans"""

    boilerplate = {
        "python": "import sys\n\ndef sumEvenAfterQueries(nums, queries):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if lines:\n        nums = list(map(int, lines[0].strip().split()))\n        queries = []\n        for i in range(1, len(lines)):\n            if lines[i].strip():\n                queries.append(list(map(int, lines[i].strip().split())))\n        ans = sumEvenAfterQueries(nums, queries)\n        print(\" \".join(map(str, ans)))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {\n        // User logic\n        return new int[0];\n    }\n}",
        "javascript": "function sumEvenAfterQueries(nums, queries) {\n    // User logic\n}",
        "c": "int* sumEvenAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4\\n1 0\\n-3 1\\n-4 0\\n2 3", "expected_output": "8 6 2 4", "is_sample": True},
        {"input": "1\\n4 0", "expected_output": "0", "is_sample": True},
        {"input": "2 4 6\\n1 0\\n1 1\\n1 2", "expected_output": "10 6 0", "is_sample": False},
        {"input": "2 2 2\\n0 0\\n0 1\\n0 2", "expected_output": "6 6 6", "is_sample": False},
        {"input": "1 3 5\\n1 0\\n1 1\\n1 2", "expected_output": "2 6 12", "is_sample": False},
        {"input": "-2 2\\n1 0\\n1 0\\n-10 1", "expected_output": "2 0 -10", "is_sample": False},
        {"input": "0 0\\n5 0\\n-5 0", "expected_output": "0 0", "is_sample": False},
        {"input": "10 -10 20\\n-5 0\\n-5 1\\n10 2", "expected_output": "10 5 -5", "is_sample": False},
        # Stress cases
        {"input": " ".join(["0"] * 10000) + "\\n" + "\\n".join(["2 0"] * 10000), "expected_output": " ".join([str(2*(i+1)) for i in range(10000)]), "is_sample": False},
        {"input": " ".join(["1"] * 10000) + "\\n" + "\\n".join(["1 0"] * 10000), "expected_output": " ".join(["2" if i % 2 == 0 else "0" for i in range(10000)]), "is_sample": False}
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
        "topics": ["Array", "Simulation", "Running Sum"],
        "companyIndex": 0
    }

    output_path = "801-1000/985_Sum_of_Even_Numbers_After_Queries.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
