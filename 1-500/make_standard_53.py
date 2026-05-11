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

    boilerplate = {
        "python": "import sys\n\ndef maxSubArray(nums):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    import re\n    input_data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', input_data)]\n    print(maxSubArray(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int maxSubArray(vector<int>& nums) {\n        // User Logic Here\n        return 0;\n    }\n};\n\nint main() {\n    string input;\n    string line;\n    while (getline(cin, line)) input += line + \" \";\n    regex rgx(\"-?\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx);\n    sregex_iterator end;\n    vector<int> nums;\n    while (iter != end) {\n        nums.push_back(stoi(iter->str()));\n        iter++;\n    }\n    Solution sol;\n    cout << sol.maxSubArray(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int maxSubArray(int[] nums) {\n        // User Logic Here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        List<Integer> list = new ArrayList<>();\n        while (m.find()) list.add(Integer.parseInt(m.group()));\n        int[] nums = new int[list.size()];\n        for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n        Solution sol = new Solution();\n        System.out.println(sol.maxSubArray(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maxSubArray = function(nums) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const nums = (input.match(/-?\\d+/g) || []).map(Number);\n    console.log(maxSubArray(nums));\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint maxSubArray(int* nums, int numsSize) {\n    // User Logic Here\n    return 0;\n}\n\nint main() {\n    int capacity = 10000;\n    int size = 0;\n    int* nums = malloc(capacity * sizeof(int));\n    int found = 0;\n    long long current = 0;\n    int sign = 1;\n    int c;\n    while ((c = getchar()) != EOF) {\n        if (isdigit(c)) {\n            if (!found) {\n                found = 1;\n                current = c - '0';\n            } else {\n                current = current * 10 + (c - '0');\n            }\n        } else if (c == '-') {\n            if (found) {\n                if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); }\n                nums[size++] = (int)(current * sign);\n                found = 0;\n                sign = 1;\n            }\n            int next = getchar();\n            if (isdigit(next)) {\n                sign = -1;\n                current = next - '0';\n                found = 1;\n            } else {\n                ungetc(next, stdin);\n            }\n        } else {\n            if (found) {\n                if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); }\n                nums[size++] = (int)(current * sign);\n                found = 0;\n                sign = 1;\n            }\n        }\n    }\n    if (found) {\n        if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); }\n        nums[size++] = (int)(current * sign);\n    }\n    printf(\"%d\\n\", maxSubArray(nums, size));\n    free(nums);\n    return 0;\n}"
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
