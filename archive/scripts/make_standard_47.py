import json
import os

def generate_json():
    problem_id = 47
    title = "Permutations II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>47. Permutations II</h3>
<p>Given a collection of numbers, <code>nums</code>, that might contain duplicates, return <em>all possible unique permutations <strong>in any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>"""

    input_format = "An array of integers nums."
    output_format = "A list of unique permutations."
    
    constraints = [
        "1 <= nums.length <= 8",
        "-10 <= nums[i] <= 10"
    ]
    
    explanation = """To find all unique permutations of an array with duplicates:
1. **Sort the input**: Sorting helps in identifying and skipping duplicate elements at the same recursion level.
2. **Backtracking**:
   - Use a `visited` array to keep track of indices used in the current permutation path.
   - For the current position, iterate through all elements.
   - **Skip condition**: Skip an element if:
     - It is already visited.
     - It is the same as the previous element AND the previous element was not visited (meaning we already processed a branch starting with this value at this level).
3. **Complexity**:
   - **Time**: $O(N \cdot N!)$ in the worst case (all elements unique), but reduced significantly by duplicates.
   - **Space**: $O(N)$ for the recursion stack and $O(N)$ for the visited array."""
    
    answer = """def permuteUnique(nums):
    res = []
    nums.sort()
    visited = [False] * len(nums)
    
    def backtrack(path):
        if len(path) == len(nums):
            res.append(list(path))
            return
            
        for i in range(len(nums)):
            if visited[i]:
                continue
            # Skip duplicates at the same level
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
                
            visited[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            visited[i] = False
            
    backtrack([])
    return res"""

    boilerplate = {
        "python": "import sys, json\n\ndef permuteUnique(nums):\n    # implementation\n    pass\n\nif __name__ == '__main__':\n    data = json.loads(sys.stdin.read())\n    print(permuteUnique(data['nums']))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<vector<int>> permuteUnique(vector<int>& nums) {\n        // implementation\n        return {};\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<List<Integer>> permuteUnique(int[] nums) {\n        // implementation\n        return new ArrayList<>();\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number[][]}\n */\nvar permuteUnique = function(nums) {\n    \n};",
        "c": "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the arrays are returned as *returnColumnSizes array.\n * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().\n */\nint** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){\n    \n}"
    }

    test_cases = [
        {"input": '{"nums": [1,1,2]}', "expected_output": "[[1,1,2],[1,2,1],[2,1,1]]", "is_sample": True},
        {"input": '{"nums": [1,2,3]}', "expected_output": "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]", "is_sample": True},
        {"input": '{"nums": [1]}', "expected_output": "[[1]]", "is_sample": False},
        {"input": '{"nums": [1,1]}', "expected_output": "[[1,1]]", "is_sample": False},
        {"input": '{"nums": [2,2,1,1]}', "expected_output": "[[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]", "is_sample": False},
        {"input": '{"nums": [3,3,0,3]}', "expected_output": "[[0,3,3,3],[3,0,3,3],[3,3,0,3],[3,3,3,0]]", "is_sample": False},
        {"input": '{"nums": [1,2]}', "expected_output": "[[1,2],[2,1]]", "is_sample": False},
        {"input": '{"nums": [-1,0,1]}', "expected_output": "[[-1,0,1],[-1,1,0],[0,-1,1],[0,1,-1],[1,-1,0],[1,0,-1]]", "is_sample": False},
        {"input": '{"nums": [0,0,0]}', "expected_output": "[[0,0,0]]", "is_sample": False},
        {"input": '{"nums": [1,2,2,2]}', "expected_output": "[[1,2,2,2],[2,1,2,2],[2,2,1,2],[2,2,2,1]]", "is_sample": False}
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
        "topics": ["Array", "Backtracking", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-100/47_Permutations_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
