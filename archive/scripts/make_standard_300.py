import json
import os
import bisect

def generate_json():
    problem_id = 300
    title = "Longest Increasing Subsequence"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>300. Longest Increasing Subsequence</h3>
<p>Given an integer array <code>nums</code>, return the length of the longest <strong>strictly increasing subsequence</strong>.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, <code>[3,6,2,7]</code> is a subsequence of the array <code>[0,3,1,6,2,2,7]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,9,2,5,3,7,101,18]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,0,3,2,3]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2500</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b>&nbsp;Can you come up with an algorithm that runs in&nbsp;<code>O(n log(n))</code> time complexity?</p>"""

    input_format = "A single line containing space-separated integers for the array nums."
    output_format = "An integer representing the length of the longest strictly increasing subsequence."
    
    constraints = [
        "1 <= nums.length <= 2500",
        "-10^4 <= nums[i] <= 10^4",
        "O(N log N) time complexity is preferred.",
        "O(N) space complexity."
    ]
    
    explanation = """To find the length of the longest strictly increasing subsequence (LIS):
1. **Dynamic Programming (O(N^2))**:
   - Let `dp[i]` be the length of the LIS ending at index `i`.
   - `dp[i] = 1 + max(dp[j])` for all `j < i` where `nums[j] < nums[i]`.
   - The result is `max(dp)`.
2. **Binary Search (O(N log N))**:
   - Maintain a list `tails` where `tails[i]` is the smallest tail of all increasing subsequences of length `i+1`.
   - For each `x` in `nums`:
     - If `x` is larger than all elements in `tails`, append it.
     - Otherwise, find the smallest element in `tails` that is greater than or equal to `x` using binary search (`bisect_left`) and replace it with `x`.
   - The length of the `tails` list is the length of the LIS.
3. **Complexity**:
   - Time Complexity: O(N log N).
   - Space Complexity: O(N)."""
    
    answer = """import bisect

def lengthOfLIS(nums: list[int]) -> int:
    if not nums:
        return 0
        
    tails = []
    for x in nums:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
            
    return len(tails)"""

    boilerplate = {
        "python": "import sys\nimport bisect\n\ndef lengthOfLIS(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        print(lengthOfLIS(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint lengthOfLIS(vector<int>& nums) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    vector<int> nums;\n    int x;\n    while (cin >> x) nums.push_back(x);\n    cout << lengthOfLIS(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int lengthOfLIS(int[] nums) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        System.out.println(new Solution().lengthOfLIS(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction lengthOfLIS(nums) {\n    // User logic here\n    return 0;\n}\n\nconst nums = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/).map(Number);\nconsole.log(lengthOfLIS(nums));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint lengthOfLIS(int* nums, int numsSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int nums[5000];\n    int size = 0;\n    while (scanf(\"%d\", &nums[size]) == 1) size++;\n    printf(\"%d\\n\", lengthOfLIS(nums, size));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "10 9 2 5 3 7 101 18", "expected_output": "4", "is_sample": True},
        {"input": "0 1 0 3 2 3", "expected_output": "4", "is_sample": True},
        {"input": "7 7 7 7 7 7 7", "expected_output": "1", "is_sample": True},
        {"input": "1 2 3 4 5", "expected_output": "5", "is_sample": False},
        {"input": "5 4 3 2 1", "expected_output": "1", "is_sample": False},
        {"input": "1 3 6 7 9 4 10 5 6", "expected_output": "6", "is_sample": False},
        {"input": "-1 -2 -3 0 1", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(2500)]), "expected_output": "2500", "is_sample": False},
        {"input": " ".join([str(2500-i) for i in range(2500)]), "expected_output": "1", "is_sample": False},
        {"input": " ".join([str(i%10) for i in range(2500)]), "expected_output": "10", "is_sample": False}
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
        "topics": ["Array", "Binary Search", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "201-400/300_Longest_Increasing_Subsequence.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
