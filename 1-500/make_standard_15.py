import json
import os

def generate_json():
    problem_id = 15
    title = "3Sum"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>15. 3Sum</h3>
<p>Given an integer array <code>nums</code>, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>
<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>3 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
"""

    input_format = "A single line containing the 'nums' array (e.g., [-1,0,1,2,-1,-4] or -1 0 1 2 -1 -4)."
    output_format = "A list of unique triplets that sum to zero."
    
    constraints = [
        "3 <= nums.length <= 3000",
        "-10^5 <= nums[i] <= 10^5"
    ]
    
    explanation = """To find unique triplets that sum to zero:
1. Sort the array.
2. Iterate with a fixed pointer `i`.
3. Use two pointers `left` and `right` to find pairs that sum to `-nums[i]`.
4. Skip duplicate elements for all three pointers to avoid duplicate triplets."""
    
    answer = """def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0: l += 1
            elif s > 0: r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1; r -= 1
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef threeSum(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = [int(x) for x in line.replace('[','').replace(']','').replace(',',' ').split()]\n        res = threeSum(nums)\n        print(json.dumps(res))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nvector<vector<int>> threeSum(vector<int>& nums) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        int val;\n        vector<int> nums;\n        while (ss >> val) nums.push_back(val);\n        vector<vector<int>> res = threeSum(nums);\n        cout << \"[\";\n        for (int i = 0; i < res.size(); i++) {\n            cout << \"[\" << res[i][0] << \",\" << res[i][1] << \",\" << res[i][2] << \"]\";\n            if (i < res.size() - 1) cout << \",\";\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<Integer>> threeSum(int[] nums) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine();\n        String[] parts = line.replaceAll(\"[\\\\\\\\[\\\\\\\\],]\", \" \").trim().split(\"\\\\\\\\s+\");\n        if (parts.length == 0 || parts[0].isEmpty()) { System.out.println(\"[]\"); return; }\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);\n        List<List<Integer>> res = threeSum(nums);\n        System.out.println(res);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction threeSum(nums) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    const nums = input.replace(/[\\\\[\\\\],]/g, ' ').trim().split(/\\\\s+/).map(Number);\n    console.log(JSON.stringify(threeSum(nums)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int* nums = malloc(10000 * sizeof(int));\n    int size = 0;\n    char* line = malloc(1000000);\n    if (fgets(line, 1000000, stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                nums[size++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    int returnSize;\n    int* returnColumnSizes;\n    int** res = threeSum(nums, size, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"[%d,%d,%d]\", res[i][0], res[i][1], res[i][2]);\n        if (i < returnSize - 1) printf(\",\");\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "-1 0 1 2 -1 -4", "expected_output": "[[-1, -1, 2], [-1, 0, 1]]", "is_sample": True},
        {"input": "0 1 1", "expected_output": "[]", "is_sample": True},
        {"input": "0 0 0", "expected_output": "[[0, 0, 0]]", "is_sample": False},
        {"input": "-2 0 1 1 2", "expected_output": "[[-2, 0, 2], [-2, 1, 1]]", "is_sample": False},
        {"input": "-5 1 1 2 3 4", "expected_output": "[[-5, 1, 4], [-5, 2, 3]]", "is_sample": False},
        {"input": "10 -10 0", "expected_output": "[[-10, 0, 10]]", "is_sample": False},
        {"input": "-1 -1 -1 2 2", "expected_output": "[[-1, -1, 2]]", "is_sample": False},
        {"input": " ".join(["0"] * 30), "expected_output": "[[0, 0, 0]]", "is_sample": False},
        {"input": " ".join([str(i) for i in range(-5, 6)]), "expected_output": "[[-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]", "is_sample": False},
        {"input": "-1 1 0 -1 1 0", "expected_output": "[[-1, 0, 1]]", "is_sample": False}
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

    output_path = "1-200/15_3Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
