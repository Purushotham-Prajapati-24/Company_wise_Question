import json
import os

def generate_json():
    problem_id = 18
    title = "4Sum"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>18. 4Sum</h3>
<p>Given an array <code>nums</code> of <code>n</code> integers, return an array of all the <strong>unique</strong> quadruplets <code>[nums[a], nums[b], nums[c], nums[d]]</code> such that:</p>

<ul>
	<li><code>0 &lt;= a, b, c, d &lt; n</code></li>
	<li><code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code> are <strong>distinct</strong>.</li>
	<li><code>nums[a] + nums[b] + nums[c] + nums[d] == target</code></li>
</ul>

<p>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,-1,0,-2,2], target = 0
<strong>Output:</strong> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2], target = 8
<strong>Output:</strong> [[2,2,2,2]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>
"""

    input_format = "Line 1: Space-separated integers for 'nums'.\nLine 2: An integer 'target'."
    output_format = "A string representing a list of unique quadruplets."
    
    constraints = [
        "1 <= nums.length <= 200",
        "-10^9 <= nums[i] <= 10^9",
        "-10^9 <= target <= 10^9"
    ]
    
    explanation = """To find all unique quadruplets summing to a target in O(N^3) time:
1. Sort the input array `nums`.
2. Use four pointers or nested loops:
   - Fixed pointer `i`: iterates from 0 to `len(nums) - 4`. Skip duplicates (`nums[i] == nums[i-1]`).
   - Fixed pointer `j`: iterates from `i + 1` to `len(nums) - 3`. Skip duplicates (`nums[j] == nums[j-1]`).
3. Inside the `j` loop, use two pointers `left = j + 1` and `right = len(nums) - 1`.
4. While `left < right`:
   - Calculate `sum = nums[i] + nums[j] + nums[left] + nums[right]`.
   - If `sum == target`:
     - Add `[nums[i], nums[j], nums[left], nums[right]]` to the result.
     - Move `left` while skipping duplicates and `right` while skipping duplicates.
     - Move both pointers inwards.
   - Else if `sum < target`, increment `left`.
   - Else `sum > target`, decrement `right`.
5. Return the list of unique quadruplets.

This approach generalizes the 3Sum technique by using another outer loop."""
    
    answer = """def fourSum(nums, target):
    nums.sort()
    res = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j-1]: continue
            l, r = j + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
    return res"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport json\n\ndef fourSum(nums, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    nums_str = input_data[0].strip() if len(input_data) > 0 else \"\"\n    target_str = input_data[1].strip() if len(input_data) > 1 else \"\"\n    nums = [int(x.strip('[],')) for x in nums_str.split() if x.strip('[],')]\n    target = int(target_str) if target_str else 0\n    res = fourSum(nums, target)\n    print(json.dumps(res).replace(',', ', '))\n",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nvector<vector<int>> fourSum(vector<int>& nums, int target) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    vector<int> nums;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int val;\n        while (ss >> val) nums.push_back(val);\n    }\n    int target = 0;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        ss >> target;\n    }\n    vector<vector<int>> res = fourSum(nums, target);\n    cout << \"[\";\n    for (size_t i = 0; i < res.size(); i++) {\n        cout << \"[\";\n        for (size_t j = 0; j < res[i].size(); j++) {\n            cout << res[i][j];\n            if (j < res[i].size() - 1) cout << \", \";\n        }\n        cout << \"]\";\n        if (i < res.size() - 1) cout << \", \";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<Integer>> fourSum(int[] nums, int target) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String line1 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        String line2 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        \n        String[] parts = line1.isEmpty() ? new String[0] : line1.split(\"\\\\s+\");\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) {\n            nums[i] = Integer.parseInt(parts[i]);\n        }\n        int target = line2.isEmpty() ? 0 : Integer.parseInt(line2);\n        List<List<Integer>> res = fourSum(nums, target);\n        System.out.println(res);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction fourSum(nums, target) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const nums = input[0].trim().split(/\\s+/).map(Number);\n    const target = parseInt(input[1].trim(), 10);\n    const res = fourSum(nums, target);\n    console.log(JSON.stringify(res).replace(/,/g, \", \"));\n} else {\n    console.log(\"[]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char line1[20000];\n    char line2[100];\n    if (fgets(line1, sizeof(line1), stdin)) {\n        int capacity = 1005;\n        int* nums = (int*)malloc(capacity * sizeof(int));\n        int size = 0;\n        char* token = strtok(line1, \" \\r\\n\");\n        while (token != NULL) {\n            nums[size++] = atoi(token);\n            token = strtok(NULL, \" \\r\\n\");\n        }\n        int target = 0;\n        if (fgets(line2, sizeof(line2), stdin)) {\n            target = atoi(line2);\n        }\n        \n        int returnSize;\n        int* returnColumnSizes;\n        int** res = fourSum(nums, size, target, &returnSize, &returnColumnSizes);\n        \n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"[\");\n            for (int j = 0; j < returnColumnSizes[i]; j++) {\n                printf(\"%d\", res[i][j]);\n                if (j < returnColumnSizes[i] - 1) printf(\", \");\n            }\n            printf(\"]\");\n            if (i < returnSize - 1) printf(\", \");\n        }\n        printf(\"]\\n\");\n        free(nums);\n    }\n    return 0;\n}"
    }

    def _4sum_ref(nums, target):
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                l, r = j+1, len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l-1]: l += 1 # wait this logic is wrong if l was just incremented, actually the usual way is while l < r and nums[l] == nums[l+1]: l+=1. But for expected output generation, I'll just use a set tuple to be safe and simple.
                    
                    if s < target: l += 1
                    else: r -= 1
        return res
        
    def get_4sum(nums, target):
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1, n-2):
                l, r = j+1, n-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif s < target: l += 1
                    else: r -= 1
        return [list(x) for x in sorted(res)]

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 0 -1 0 -2 2\n0", "expected_output": "[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]", "is_sample": True},
        {"input": "2 2 2 2 2\n8", "expected_output": "[[2, 2, 2, 2]]", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "0 0 0 0\n0", "expected_output": "[[0, 0, 0, 0]]", "is_sample": False},
        {"input": "1 2 3 4\n10", "expected_output": "[[1, 2, 3, 4]]", "is_sample": False},
        {"input": "1 2 3 4\n11", "expected_output": "[]", "is_sample": False},
        {"input": "-5 -4 -3 -2 -1 0 1 2 3 4 5\n0", "expected_output": str(get_4sum([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 0)), "is_sample": False},
        {"input": "-1 -2 -3 -4 -5\n-10", "expected_output": "[[-4, -3, -2, -1]]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(["0"] * 200) + "\n0", "expected_output": "[[0, 0, 0, 0]]", "is_sample": False},
        {"input": " ".join([str(i) for i in range(-100, 100)]) + "\n0", "expected_output": str(get_4sum([i for i in range(-100, 100)], 0)), "is_sample": False},
        {"input": " ".join(["1000", "-1000"] * 100) + "\n0", "expected_output": "[[-1000, -1000, 1000, 1000]]", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/18_4Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
