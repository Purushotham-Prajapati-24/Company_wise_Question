import json
import os

def generate_json():
    problem_id = 442
    difficulty = "MEDIUM"
    marks = 10
    title = "Find All Duplicates in an Array"
    
    html_description = """<h3>442. Find All Duplicates in an Array</h3>
<p>Given an integer array <code>nums</code> of length <code>n</code> where all the integers of <code>nums</code> are in the range <code>[1, n]</code> and each integer appears <strong>once</strong> or <strong>twice</strong>, return <em>an array of all the integers that appears <strong>twice</strong></em>.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and uses only <strong>constant</strong> extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,3,2,7,8,2,3,1]
<strong>Output:</strong> [2,3]
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> [1]
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li>Each element in <code>nums</code> appears <strong>once</strong> or <strong>twice</strong>.</li>
</ul>"""

    input_format = "An integer array `nums`."
    output_format = "A list of integers."
    
    constraints = [
        "1 <= n <= 100,000",
        "Must be O(N) time.",
        "Must be O(1) constant extra space."
    ]
    
    explanation = """To find duplicates in $O(N)$ time and $O(1)$ space, we use the input array itself as a frequency map.

### Key Observation:
- Each value in `nums` is in the range `[1, n]`.
- We can map each value to an index in the range `[0, n-1]`.
- We can **mark** that a number has been seen by negating the value at its corresponding index.

### Algorithm Steps:
1. Initialize an empty results list `res`.
2. Iterate through `nums`:
   - For each element $x$:
     - Find the index it maps to: `idx = abs(x) - 1`.
     - Check the value at `nums[idx]`.
     - If `nums[idx]` is **negative**, it means we have visited this index before. So `abs(x)` is a duplicate. Add it to `res`.
     - If `nums[idx]` is **positive**, negate it: `nums[idx] = -nums[idx]`.
3. Return `res`.

### Complexity Analysis:
- **Time Complexity**: $O(N)$, where $N$ is the number of elements. We iterate through the array once.
- **Space Complexity**: $O(1)$ extra space (excluding the result list)."""
    
    answer = """class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] < 0:
                res.append(abs(x))
            else:
                nums[idx] *= -1
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def findDuplicates(self, nums: list[int]) -> list[int]:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        nums = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.findDuplicates(nums)))",
        "cpp": "class Solution {\npublic:\n    vector<int> findDuplicates(vector<int>& nums) {\n        // Your logic here\n        return {};\n    }\n};",
        "java": "public class Solution {\n    public List<Integer> findDuplicates(int[] nums) {\n        // Your logic here\n        return new ArrayList<>();\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar findDuplicates = function(nums) {\n    // Your logic here\n};",
        "c": "/**\n * Note: The returned array must be malloced.\n */\nint* findDuplicates(int* nums, int numsSize, int* returnSize) {\n    // Your logic here\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "[4,3,2,7,8,2,3,1]", "expected_output": "[2,3]", "is_sample": True},
        {"input": "[1,1,2]", "expected_output": "[1]", "is_sample": True},
        {"input": "[1]", "expected_output": "[]", "is_sample": True},
        {"input": "[1,2,3,4,5]", "expected_output": "[]", "is_sample": False},
        {"input": "[5,4,3,2,1]", "expected_output": "[]", "is_sample": False},
        {"input": "[2,2,2,2,2]", "expected_output": "[2,2]", "is_sample": False}, # Note: Problem says 1 or 2 times, but stress testing
        {"input": "[1,1,2,2]", "expected_output": "[1,2]", "is_sample": False},
        # Stress cases
        {"input": "[i for i in range(1, 100001)]", "expected_output": "[]", "is_sample": False},
        {"input": "[i for i in range(1, 50001)] * 2", "expected_output": "[i for i in range(1, 50001)]", "is_sample": False},
        {"input": "[1, 1] + [i for i in range(3, 100001)]", "expected_output": "[1]", "is_sample": False}
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
        "companyIndex": 1
    }

    output_path = "301-500/442_Find_All_Duplicates_in_an_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
