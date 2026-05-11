import json
import os

def generate_json():
    problem_id = 16
    title = "3Sum Closest"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>16. 3Sum Closest</h3>
<p>Given an integer array <code>nums</code> of length <code>n</code> and an integer <code>target</code>, find three integers in <code>nums</code> such that the sum is closest to <code>target</code>.</p>

<p>Return <em>the sum of the three integers</em>.</p>

<p>You may assume that each input would have exactly one solution.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,2,1,-4], target = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0], target = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Line 1: Space-separated integers for 'nums'.\nLine 2: An integer 'target'."
    output_format = "An integer representing the sum of three integers closest to target."
    
    constraints = [
        "3 <= nums.length <= 1000",
        "-1000 <= nums[i] <= 1000",
        "-10^4 <= target <= 10^4"
    ]
    
    explanation = """To find the triplet sum closest to a target in O(N^2) time:
1. Sort the array `nums` to enable the two-pointer technique.
2. Initialize `closest_sum` with the sum of the first three elements.
3. Iterate through `nums` with a fixed pointer `i` up to `len(nums) - 2`.
4. For each `i`, use two pointers `left = i + 1` and `right = len(nums) - 1`.
5. While `left < right`:
   - Calculate the current sum `s = nums[i] + nums[left] + nums[right]`.
   - If `s` is equal to the target, return `s` immediately (it's the closest possible).
   - If the difference `abs(s - target)` is smaller than `abs(closest_sum - target)`, update `closest_sum`.
   - If `s < target`, increment `left` to increase the sum.
   - Else if `s > target`, decrement `right` to decrease the sum.
6. Return `closest_sum`.

Wait, the logic is consistent with 3Sum but focuses on proximity rather than equality to zero."""
    
    answer = """def threeSumClosest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == target:
                return s
            if abs(s - target) < abs(res - target):
                res = s
            if s < target:
                l += 1
            else:
                r -= 1
    return res"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef threeSumClosest(nums, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    nums_str = input_data[0].strip() if len(input_data) > 0 else \"\"\n    target_str = input_data[1].strip() if len(input_data) > 1 else \"\"\n    nums = [int(x.strip('[],')) for x in nums_str.split() if x.strip('[],')]\n    target = int(target_str) if target_str else 0\n    print(threeSumClosest(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nint threeSumClosest(vector<int>& nums, int target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line;\n    vector<int> nums;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int val;\n        while (ss >> val) nums.push_back(val);\n    }\n    int target = 0;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        ss >> target;\n    }\n    cout << threeSumClosest(nums, target) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int threeSumClosest(int[] nums, int target) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String line1 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        String line2 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        \n        String[] parts = line1.isEmpty() ? new String[0] : line1.split(\"\\\\s+\");\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) {\n            nums[i] = Integer.parseInt(parts[i]);\n        }\n        int target = line2.isEmpty() ? 0 : Integer.parseInt(line2);\n        System.out.println(threeSumClosest(nums, target));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction threeSumClosest(nums, target) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const nums = input[0].trim().split(/\\s+/).map(Number);\n    const target = parseInt(input[1].trim(), 10);\n    console.log(threeSumClosest(nums, target));\n} else {\n    console.log(0);\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint threeSumClosest(int* nums, int numsSize, int target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char line1[20000];\n    char line2[100];\n    if (fgets(line1, sizeof(line1), stdin)) {\n        int capacity = 1005;\n        int* nums = (int*)malloc(capacity * sizeof(int));\n        int size = 0;\n        char* token = strtok(line1, \" \\r\\n\");\n        while (token != NULL) {\n            nums[size++] = atoi(token);\n            token = strtok(NULL, \" \\r\\n\");\n        }\n        int target = 0;\n        if (fgets(line2, sizeof(line2), stdin)) {\n            target = atoi(line2);\n        }\n        printf(\"%d\\n\", threeSumClosest(nums, size, target));\n        free(nums);\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "-1 2 1 -4\n1", "expected_output": "2", "is_sample": True},
        {"input": "0 0 0\n1", "expected_output": "0", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1 1 1 0\n-100", "expected_output": "2", "is_sample": False},
        {"input": "1 1 1 1\n0", "expected_output": "3", "is_sample": False},
        {"input": "-100 -98 -2 -1\n-101", "expected_output": "-200", "is_sample": False},
        {"input": "1 2 4 8 16 32\n10", "expected_output": "11", "is_sample": False},
        {"input": "1 2 4 8 16 32\n20", "expected_output": "21", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(1000)]) + "\n10000", "expected_output": "2991", "is_sample": False}, # sum of 997, 998, 999
        {"input": " ".join([str(i) for i in range(1000)]) + "\n-10000", "expected_output": "3", "is_sample": False}, # sum of 0, 1, 2
        {"input": " ".join(["1000"]*1000) + "\n3000", "expected_output": "3000", "is_sample": False}
    ]
    # Recalculating stress 1: sum of top 3 is 997+998+999 = 2994. Wait, 1000 items (0..999).
    # Correct: 997+998+999 = 2994. My previous was 2994 in the file but I wrote 2991 in thought.
    test_cases[7]["expected_output"] = "2994"

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
        "topics": ["Array", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "1-200/16_3Sum_Closest.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
