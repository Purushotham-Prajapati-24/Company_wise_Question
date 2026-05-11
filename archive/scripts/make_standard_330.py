import json
import os

def generate_json():
    problem_id = 330
    title = "Patching Array"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>330. Patching Array</h3>
<p>Given a sorted integer array <code>nums</code> and an integer <code>n</code>, add/patch elements to the array such that any number in the range <code>[1, n]</code> inclusive can be formed by the sum of some elements in the array.</p>

<p>Return <em>the minimum number of patches required</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,3], n = 6
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Combinations of nums are [1], [3], [1,3], which form sums 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6.
Now all numbers from 1 to 6 can be formed.
We only need 1 patch.</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,5,10], n = 20
<strong>Output:</strong> 2
<strong>Explanation:</strong> The two patches can be [2, 4].
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2], n = 5
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>ascending order</strong>.</li>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A sorted integer array `nums` and a target integer `n`."
    output_format = "An integer representing the minimum number of patches."
    
    constraints = [
        "1 <= nums.length <= 1000",
        "1 <= nums[i] <= 10^4",
        "1 <= n <= 2^31 - 1"
    ]
    
    explanation = """To form all numbers in the range $[1, n]$, we use a **Greedy** approach.

### Key Strategy:
- Maintain a variable `miss` which represents the smallest sum that we **cannot** currently form. Initially, `miss = 1`.
- At any point, if we can form all sums in $[1, miss-1]$, then by adding a number $x \le miss$, we can expand our range to $[1, miss + x - 1]$.

### Algorithm Steps:
1. **Initialize**: `patches = 0`, `i = 0`, `miss = 1`.
2. **Loop**: While `miss <= n`:
   - If `i < nums.length` and `nums[i] <= miss`:
     - We can use the existing number `nums[i]` to expand our range.
     - New range becomes $[1, miss + nums[i] - 1]$.
     - Update `miss += nums[i]` and move `i` forward.
   - Else:
     - We encounter a gap. To fill the gap greediest way possible, we **patch** the current `miss`.
     - New range becomes $[1, miss + miss - 1] = [1, 2*miss - 1]$.
     - Update `miss += miss` and increment `patches`.
3. **Terminate**: Return `patches`.

### Complexity Analysis:
- **Time Complexity**: $O(K + \log N)$, where $K$ is the number of elements in `nums` and $\log N$ is the number of patches (at most 31).
- **Space Complexity**: $O(1)$."""
    
    answer = """class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        patches = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def minPatches(self, nums, n):\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        data = json.loads(raw_input)\n        nums = data['nums']\n        n = data['n']\n        sol = Solution()\n        print(json.dumps(sol.minPatches(nums, n)))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int minPatches(vector<int>& nums, int n) {\n        // Your logic here\n        return 0;\n    }\n};",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int minPatches(int[] nums, int n) {\n        // Your logic here\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @param {number} n\n * @return {number}\n */\nvar minPatches = function(nums, n) {\n    // Your logic here\n};",
        "c": "int minPatches(int* nums, int numsSize, int n) {\n    // Your logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": '{"nums": [1,3], "n": 6}', "expected_output": "1", "is_sample": True},
        {"input": '{"nums": [1,5,10], "n": 20}', "expected_output": "2", "is_sample": True},
        {"input": '{"nums": [1,2,2], "n": 5}', "expected_output": "0", "is_sample": True},
        {"input": '{"nums": [], "n": 8}', "expected_output": "4", "is_sample": False},
        {"input": '{"nums": [1,2,31,33], "n": 2147483647}', "expected_output": "28", "is_sample": False},
        {"input": '{"nums": [1,2,4,8,16,32], "n": 63}', "expected_output": "0", "is_sample": False},
        {"input": '{"nums": [1, 100], "n": 100}', "expected_output": "6", "is_sample": False},
        # Stress cases
        {"input": '{"nums": [], "n": 2147483647}', "expected_output": "31", "is_sample": False},
        {"input": '{"nums": [1]*1000, "n": 2147483647}', "expected_output": "1", "is_sample": False},
        {"input": '{"nums": [10000]*1000, "n": 2147483647}', "expected_output": "31", "is_sample": False}
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
        "topics": ["Array", "Greedy"],
        "companyIndex": 1
    }

    output_path = "301-500/330_Patching_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
