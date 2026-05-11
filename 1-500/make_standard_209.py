import json
import os

def generate_json():
    problem_id = 209
    title = "Minimum Size Subarray Sum"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>209. Minimum Size Subarray Sum</h3>
<p>Given an array of positive integers <code>nums</code> and a positive integer <code>target</code>, return the minimal length of a <strong>contiguous subarray</strong> <code>[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]</code> of which the sum is greater than or equal to <code>target</code>. If there is no such subarray, return <code>0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = 7, nums = [2,3,1,2,4,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The subarray [4,3] has the minimal length under the problem constraint.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = 4, nums = [1,4,4]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = 11, nums = [1,1,1,1,1,1,1,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution of which the time complexity is <code>O(n log n)</code>."""

    input_format = "Two lines. Line 1: target integer. Line 2: space-separated integers for nums."
    output_format = "An integer representing the minimal length, or 0 if no such subarray exists."
    
    constraints = [
        "1 <= target <= 10^9",
        "1 <= nums.length <= 10^5",
        "1 <= nums[i] <= 10^4",
        "O(N) time complexity expected."
    ]
    
    explanation = """To find the minimal length of a contiguous subarray with sum >= target:
1. **Sliding Window (Two Pointers)**:
   - Use two pointers, `left` and `right`, to define a window.
   - Maintain a `current_sum` of elements in the window.
2. **Logic**:
   - Iterate with `right` from 0 to `len(nums) - 1`.
   - Add `nums[right]` to `current_sum`.
   - While `current_sum >= target`:
     - Update the minimal length: `min_len = min(min_len, right - left + 1)`.
     - Shrink the window from the left: subtract `nums[left]` from `current_sum` and increment `left`.
3. **Complexity**:
   - Time Complexity: O(N) since each element is visited at most twice (one by `right`, one by `left`).
   - Space Complexity: O(1) as we only store a few variables."""
    
    answer = """def minSubArrayLen(target: int, nums: list[int]) -> int:
    min_len = float('inf')
    left = 0
    current_sum = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
            
    return 0 if min_len == float('inf') else min_len"""

    boilerplate = {
        "python": "import sys\n\ndef minSubArrayLen(target, nums):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        target = int(lines[0])\n        nums = [int(x) for x in lines[1].split()]\n        print(minSubArrayLen(target, nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nint minSubArrayLen(int target, vector<int>& nums) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int target;\n    if (cin >> target) {\n        string line;\n        getline(cin, line); // consume newline\n        if (getline(cin, line)) {\n            stringstream ss(line);\n            int val;\n            vector<int> nums;\n            while (ss >> val) nums.push_back(val);\n            cout << minSubArrayLen(target, nums) << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int minSubArrayLen(int target, int[] nums) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 != null && line2 != null) {\n            int target = Integer.parseInt(line1.trim());\n            String[] parts = line2.trim().split(\"\\\\s+\");\n            int[] nums = new int[parts.length];\n            for (int i = 0; i < parts.length; i++) {\n                nums[i] = Integer.parseInt(parts[i]);\n            }\n            System.out.println(new Solution().minSubArrayLen(target, nums));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction minSubArrayLen(target, nums) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    const target = parseInt(input[0].trim());\n    const nums = input[1].trim().split(/\\\\s+/).map(Number);\n    console.log(minSubArrayLen(target, nums));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint minSubArrayLen(int target, int* nums, int numsSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int target;\n    if (scanf(\"%d\", &target) == 1) {\n        int capacity = 1000;\n        int* nums = (int*)malloc(capacity * sizeof(int));\n        int size = 0;\n        int val;\n        while (scanf(\"%d\", &val) == 1) {\n            if (size >= capacity) {\n                capacity *= 2;\n                nums = (int*)realloc(nums, capacity * sizeof(int));\n            }\n            nums[size++] = val;\n        }\n        printf(\"%d\\n\", minSubArrayLen(target, nums, size));\n        free(nums);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "7\\n2 3 1 2 4 3", "expected_output": "2", "is_sample": True},
        {"input": "4\\n1 4 4", "expected_output": "1", "is_sample": True},
        {"input": "11\\n1 1 1 1 1 1 1 1", "expected_output": "0", "is_sample": True},
        {"input": "5\\n2 3", "expected_output": "2", "is_sample": False},
        {"input": "1\\n1", "expected_output": "1", "is_sample": False},
        {"input": "100\\n10 20 30 40 50", "expected_output": "3", "is_sample": False},
        {"input": "5\\n1 2 3 4 5", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": "1000000000\\n" + " ".join(["10000"]*100000), "expected_output": "100000", "is_sample": False},
        {"input": "1000000001\\n" + " ".join(["10000"]*100000), "expected_output": "0", "is_sample": False},
        {"input": "10\\n" + " ".join(["1"]*100000), "expected_output": "10", "is_sample": False}
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
        "topics": ["Array", "Binary Search", "Sliding Window", "Prefix Sum"],
        "companyIndex": 0
    }

    output_path = "1-200/209_Minimum_Size_Subarray_Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
