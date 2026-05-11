import json
import os

def generate_json():
    problem_id = 198
    title = "House Robber"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>198. House Robber</h3>
<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <b>without alerting the police</b></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 400</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the array nums."
    output_format = "An integer representing the maximum amount that can be robbed."
    
    constraints = [
        "1 <= nums.length <= 100",
        "0 <= nums[i] <= 400",
        "Linear time complexity expected."
    ]
    
    explanation = """To solve the House Robber problem using Dynamic Programming:
1. **Define Subproblems**:
   - `dp[i]` represents the maximum money that can be robbed up to house `i`.
2. **State Transition**:
   - At each house `i`, you have two choices:
     - **Option 1**: Rob house `i`. In this case, you cannot rob house `i-1`. Total = `nums[i] + dp[i-2]`.
     - **Option 2**: Do not rob house `i`. Total = `dp[i-1]`.
   - Therefore, `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.
3. **Optimizing Space**:
   - Observe that we only ever need the results of the previous two subproblems (`dp[i-1]` and `dp[i-2]`).
   - We can use two variables `prev1` and `prev2` to track these, reducing space complexity to O(1).
4. **Complexity**:
   - Time Complexity: O(N) where N is the number of houses.
   - Space Complexity: O(1)."""
    
    answer = """def rob(nums: list[int]) -> int:
    prev2, prev1 = 0, 0
    for num in nums:
        # dp[i] = max(dp[i-1], num + dp[i-2])
        current = max(prev1, num + prev2)
        prev2 = prev1
        prev1 = current
    return prev1"""

    boilerplate = {
        "python": "import sys\n\ndef rob(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if not data:\n        sys.exit(0)\n    nums = [int(x) for x in data]\n    print(rob(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint rob(vector<int>& nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int val;\n    vector<int> nums;\n    while (cin >> val) {\n        nums.push_back(val);\n    }\n    if (nums.empty()) return 0;\n    cout << rob(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int rob(int[] nums) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line == null || line.trim().isEmpty()) return;\n        String[] parts = line.trim().split(\"\\\\s+\");\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) {\n            nums[i] = Integer.parseInt(parts[i]);\n        }\n        System.out.println(new Solution().rob(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction rob(nums) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    const nums = input.map(Number);\n    console.log(rob(nums));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint rob(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int capacity = 1000;\n    int* nums = (int*)malloc(capacity * sizeof(int));\n    int size = 0;\n    int val;\n    while (scanf(\"%d\", &val) == 1) {\n        if (size >= capacity) {\n            capacity *= 2;\n            nums = (int*)realloc(nums, capacity * sizeof(int));\n        }\n        nums[size++] = val;\n    }\n    if (size == 0) {\n        free(nums);\n        return 0;\n    }\n    printf(\"%d\\n\", rob(nums, size));\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 1", "expected_output": "4", "is_sample": True},
        {"input": "2 7 9 3 1", "expected_output": "12", "is_sample": True},
        {"input": "10", "expected_output": "10", "is_sample": False},
        {"input": "1 5", "expected_output": "5", "is_sample": False},
        {"input": "5 1", "expected_output": "5", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "9", "is_sample": False},
        {"input": "4 1 2 7 5 3 1", "expected_output": "14", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i%400) for i in range(100)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join(["400"]*100), "expected_output": str(400*50), "is_sample": False},
        {"input": " ".join(["0"]*100), "expected_output": "0", "is_sample": False}
    ]
    
    # Simple fix for stress case 8
    def _solve(nums):
        p2, p1 = 0, 0
        for n in nums:
            p2, p1 = p1, max(p1, n + p2)
        return p1
    test_cases[7]["expected_output"] = str(_solve([i%400 for i in range(100)]))

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
        "topics": ["Array", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1-200/198_House_Robber.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
