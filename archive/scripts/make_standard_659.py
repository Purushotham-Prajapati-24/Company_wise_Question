import json
import collections
import os

def generate_json():
    problem_id = 659
    title = "Split Array into Consecutive Subsequences"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>659. Split Array into Consecutive Subsequences</h3>
<p>You are given an integer array <code>nums</code> that is <strong>sorted in non-decreasing order</strong>.</p>

<p>Determine if it is possible to split <code>nums</code> into <strong>one or more subsequences</strong> such that <strong>each subsequence</strong> is a <strong>consecutive increasing sequence</strong> (i.e. <code>x, x + 1, x + 2, ..., x + n</code>) and has a length of <strong>at least 3</strong>.</p>

<p>Return <code>true</code><em> if such a split is possible, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,3,4,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> nums can be split into the following subsequences:
[1,2,3,4,5], [3] - Invalid (length 1)
[1,2,3], [3,4,5] - Valid (both length 3)
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,3,4,4,5,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> nums can be split into the following subsequences:
[1,2,3,4,5], [3,4,5] - Valid (both length 3)
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4,4,5]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to split nums into consecutive increasing subsequences of length at least 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing order</strong>.</li>
</ul>"""

    input_format = "A sorted array of integers `nums`."
    output_format = "A boolean: true or false."
    
    constraints = [
        "1 <= nums.length <= 10,000",
        "nums is sorted in non-decreasing order."
    ]
    
    explanation = """To determine if the array can be split into consecutive subsequences of length >= 3:
1. **Greedy Strategy**:
   - Use two hash maps (dictionaries):
     - `counts`: To track the frequency of each number in `nums`.
     - `ends`: To track the number of subsequences ending at a particular value.
2. **Algorithm**:
   - Iterate through each number `x` in `nums`:
     - If `counts[x] == 0`, continue (it's already been used in another subsequence).
     - Otherwise, decrement `counts[x]`.
     - **Option 1 (Append)**: If there's a subsequence ending at `x-1`, append `x` to it.
       - If `ends[x-1] > 0`: Decrement `ends[x-1]` and increment `ends[x]`.
     - **Option 2 (Create New)**: If we can't append, try creating a new subsequence of length 3 starting with `x` (using `x, x+1, x+2`).
       - If `counts[x+1] > 0` and `counts[x+2] > 0`:
         - Decrement `counts[x+1]` and `counts[x+2]`.
         - Increment `ends[x+2]`.
     - **Otherwise**: Return `False`.
3. **Complexity Analysis**:
   - Time: O(N) where N is the length of `nums`.
   - Space: O(N) to store frequencies in the hash maps."""
    
    answer = """class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = collections.Counter(nums)
        # ends[i] is the number of valid subsequences ending at index i
        ends = collections.defaultdict(int)
        
        for x in nums:
            if counts[x] == 0:
                continue
            
            counts[x] -= 1
            
            # 1. Try to append to an existing subsequence
            if ends[x - 1] > 0:
                ends[x - 1] -= 1
                ends[x] += 1
            # 2. Try to create a new subsequence of length 3
            elif counts[x + 1] > 0 and counts[x + 2] > 0:
                counts[x + 1] -= 1
                counts[x + 2] -= 1
                ends[x + 2] += 1
            else:
                return False
                
        return True"""

    boilerplate = {
        "python": "import sys\nimport json\nimport collections\n\ndef isPossible(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        nums = json.loads(input_data)\n        print(json.dumps(isPossible(nums)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nbool isPossible(vector<int>& nums) {\n    // User logic here\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean isPossible(int[] nums) {\n        // User logic\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar isPossible = function(nums) {\n    // User logic here\n};",
        "c": "bool isPossible(int* nums, int numsSize) {\n    // User logic here\n}"
    }

    test_cases = [
        {"input": "[1,2,3,3,4,5]", "expected_output": "true", "is_sample": True},
        {"input": "[1,2,3,3,4,4,5,5]", "expected_output": "true", "is_sample": True},
        {"input": "[1,2,3,4,4,5]", "expected_output": "false", "is_sample": True},
        {"input": "[1,2,3]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,4]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,4,5,6]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,4,5,7,8,9]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,3,4,4,5,5,6,6]", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "[i for i in range(10000)]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3]*3333", "expected_output": "true", "is_sample": False},
        {"input": "[1]*10000", "expected_output": "false", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Greedy"],
        "companyIndex": 0
    }

    output_path = "601-800/659_Split_Array_into_Consecutive_Subsequences.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
