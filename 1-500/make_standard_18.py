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
</ul>"""

    input_format = "Line 1: The 'nums' array (e.g., [1,0,-1,0,-2,2]).\nLine 2: The 'target' integer."
    output_format = "A list of unique quadruplets summing to the target."
    
    constraints = [
        "1 <= nums.length <= 200",
        "-10^9 <= nums[i] <= 10^9",
        "-10^9 <= target <= 10^9"
    ]
    
    explanation = """Sort the array first.
Use two nested loops to fix the first two numbers (i and j).
For each pair, use a two-pointer approach (left and right) to find the remaining two numbers.
Skip duplicate values for each pointer to ensure unique quadruplets."""
    
    answer = """def fourSum(nums, target):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j-1]: continue
            l, r = j + 1, n - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1
                elif s < target: l += 1
                else: r -= 1
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef fourSum(nums, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        nums = [int(x) for x in input_data[0].replace('[','').replace(']','').replace(',',' ').split()]\n        target = int(input_data[1].replace('[','').replace(']','').split('=')[-1].strip())\n        res = fourSum(nums, target)\n        print(json.dumps(res).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nvector<vector<int>> fourSum(vector<int>& nums, int target) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    vector<int> nums;\n    if (getline(cin, line)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        int val; while (ss >> val) nums.push_back(val);\n    }\n    int target = 0;\n    if (getline(cin, line)) {\n        string clean = \"\";\n        for(char c : line) if(isdigit(c) || c == '-') clean += c;\n        if(!clean.empty()) target = stoi(clean);\n    }\n    vector<vector<int>> res = fourSum(nums, target);\n    cout << \"[\";\n    for (int i = 0; i < res.size(); i++) {\n        cout << \"[\";\n        for (int j = 0; j < res[i].size(); j++) {\n            cout << res[i][j];\n            if (j < res[i].size() - 1) cout << \", \";\n        }\n        cout << \"]\";\n        if (i < res.size() - 1) cout << \", \";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<Integer>> fourSum(int[] nums, int target) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line1 = sc.nextLine();\n        String[] parts = line1.replaceAll(\"[\\\\\\\\[\\\\\\\\],]\", \" \").trim().split(\"\\\\\\\\s+\");\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);\n        if (!sc.hasNextLine()) return;\n        String line2 = sc.nextLine().replaceAll(\"[^0-9-]\", \"\");\n        int target = Integer.parseInt(line2);\n        List<List<Integer>> res = fourSum(nums, target);\n        System.out.println(res);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction fourSum(nums, target) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const nums = input[0].replace(/[\\\\[\\\\],]/g, ' ').trim().split(/\\\\s+/).map(Number);\n    const target = parseInt(input[1].replace(/[^0-9-]/g, ''), 10);\n    const res = fourSum(nums, target);\n    console.log(JSON.stringify(res).replace(/,/g, \", \"));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\nint** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int* nums = malloc(1000 * sizeof(int));\n    int size = 0;\n    char line[10000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                nums[size++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    int target = 0;\n    if (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while(*p && !isdigit(*p) && *p != '-') p++;\n        if(*p) target = atoi(p);\n    }\n    int returnSize;\n    int* returnColumnSizes;\n    int** res = fourSum(nums, size, target, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"[\");\n        for (int j = 0; j < returnColumnSizes[i]; j++) {\n            printf(\"%d\", res[i][j]);\n            if (j < returnColumnSizes[i] - 1) printf(\", \");\n        }\n        printf(\"]\");\n        if (i < returnSize - 1) printf(\", \");\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 0 -1 0 -2 2\n0", "expected_output": "[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]", "is_sample": True},
        {"input": "2 2 2 2 2\n8", "expected_output": "[[2, 2, 2, 2]]", "is_sample": True},
        {"input": "0 0 0 0\n0", "expected_output": "[[0, 0, 0, 0]]", "is_sample": False},
        {"input": "1 1 1 1\n4", "expected_output": "[[1, 1, 1, 1]]", "is_sample": False},
        {"input": "-3 -2 -1 0 1 2 3\n0", "expected_output": "[[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2]]", "is_sample": False},
        {"input": "100 200 300 400\n1000", "expected_output": "[[100, 200, 300, 400]]", "is_sample": False},
        {"input": "-1 0 1 2 -1 -4\n-1", "expected_output": "[[-4, 0, 1, 2], [-1, -1, 0, 1]]", "is_sample": False},
        {"input": "1 2 3 4 5\n100", "expected_output": "[]", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10)]) + "\n10", "expected_output": "[[0, 1, 2, 7], [0, 1, 3, 6], [0, 1, 4, 5], [0, 2, 3, 5], [1, 2, 3, 4]]", "is_sample": False},
        {"input": " ".join(["-1"]*10) + "\n-4", "expected_output": "[[-1, -1, -1, -1]]", "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
        "question_title": title,
        "difficulty": difficulty,
        "marks": marks,
        "question_text": html_description,
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
