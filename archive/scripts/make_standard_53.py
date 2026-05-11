import json
import os

def generate_json():
    problem_id = 53
    title = "Maximum Subarray"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>53. Maximum Subarray</h3>
<p>Given an integer array <code>nums</code>, find the subarray with the largest sum, and return <em>its sum</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [1] has the largest sum 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>"""

    input_format = "A single line containing space-separated integers for the array 'nums'."
    output_format = "An integer representing the maximum possible sum of a contiguous subarray."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "-10^4 <= nums[i] <= 10^4"
    ]
    
    explanation = """To find the contiguous subarray with the maximum sum efficiently:
1. ** Kadane's Algorithm** is the most optimal approach, running in O(n) time with O(1) space.
2. **Concept**: At each position `i` in the array, the maximum subarray sum ending at `i` is either the element `nums[i]` itself or the sum of `nums[i]` and the maximum subarray ending at `i-1`.
3. **Algorithm**:
   - Initialize two variables: `current_max` and `global_max` with the first element of the array.
   - Iterate through the array starting from the second element:
     - Update `current_max = max(nums[i], current_max + nums[i])`. This step decides whether to "restart" the subarray at the current element or include it in the existing subarray.
     - Update `global_max = max(global_max, current_max)`.
4. Return `global_max` after the loop.

This algorithm works because `global_max` keeps track of the overall maximum sum encountered so far, while `current_max` tracks the local maximum at every position."""
    
    answer = """def maxSubArray(nums):
    if not nums:
        return 0
        
    current_max = global_max = nums[0]
    
    for i in range(1, len(nums)):
        # Deciding whether to extend the previous subarray or start a new one
        current_max = max(nums[i], current_max + nums[i])
        # Update the overall maximum found so far
        global_max = max(global_max, current_max)
        
    return global_max"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef maxSubArray(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip().split()\n    if input_data:\n        nums = [int(x) for x in input_data]\n        print(maxSubArray(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint maxSubArray(vector<int>& nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int val;\n    vector<int> nums;\n    while (cin >> val) nums.push_back(val);\n    cout << maxSubArray(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int maxSubArray(int[] nums) {\n        // User logic\n        return 0;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        System.out.println(maxSubArray(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction maxSubArray(nums) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/).map(Number);\nconsole.log(maxSubArray(input));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <limits.h>\n\nint maxSubArray(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char line[2000000];\n    if (fgets(line, sizeof(line), stdin)) {\n        int capacity = 1000, size = 0;\n        int* nums = (int*)malloc(capacity * sizeof(int));\n        char* token = strtok(line, \" \\t\\r\\n\");\n        while (token) {\n            if (size == capacity) { capacity *= 2; nums = (int*)realloc(nums, capacity * sizeof(int)); }\n            nums[size++] = atoi(token);\n            token = strtok(NULL, \" \\t\\r\\n\");\n        }\n        printf(\"%d\\n\", maxSubArray(nums, size));\n        free(nums);\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "-2 1 -3 4 -1 2 1 -5 4", "expected_output": "6", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "5 4 -1 7 8", "expected_output": "23", "is_sample": False},
        {"input": "-5 -4 -3 -2 -1", "expected_output": "-1", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "15", "is_sample": False},
        {"input": "10 -5 10 -5 10", "expected_output": "20", "is_sample": False},
        {"input": "0 0 0 0", "expected_output": "0", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(["-10000"] * 100000), "expected_output": "-10000", "is_sample": False},
        {"input": " ".join(["10000"] * 100000), "expected_output": "1000000000", "is_sample": False},
        {"input": " ".join([str(i % 2 * 10 - 5) for i in range(100000)]), "expected_output": "5", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Divide and Conquer"],
        "companyIndex": 0
    }

    output_path = "1-200/53_Maximum_Subarray.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
