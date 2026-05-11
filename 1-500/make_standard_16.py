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
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>3 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Line 1: The 'nums' array (e.g., [-1,2,1,-4]).\nLine 2: The 'target' integer."
    output_format = "An integer representing the sum closest to the target."
    
    constraints = [
        "3 <= nums.length <= 1000",
        "-1000 <= nums[i] <= 1000",
        "-10^4 <= target <= 10^4"
    ]
    
    explanation = """To find the triplet sum closest to a target:
1. Sort the array.
2. Iterate with a fixed pointer `i`.
3. Use two pointers `left` and `right`.
4. Update the `closest_sum` if the current sum is nearer to the target."""
    
    answer = """def threeSumClosest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == target: return s
            if abs(s - target) < abs(res - target):
                res = s
            if s < target: l += 1
            else: r -= 1
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef threeSumClosest(nums, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        nums = [int(x) for x in input_data[0].replace('[','').replace(']','').replace(',',' ').split()]\n        target = int(input_data[1].replace('[','').replace(']','').split('=')[-1].strip())\n        print(threeSumClosest(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nint threeSumClosest(vector<int>& nums, int target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line;\n    vector<int> nums;\n    if (getline(cin, line)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        int val; while (ss >> val) nums.push_back(val);\n    }\n    int target = 0;\n    if (getline(cin, line)) {\n        string clean = \"\";\n        for(char c : line) if(isdigit(c) || c == '-') clean += c;\n        if(!clean.empty()) target = stoi(clean);\n    }\n    cout << threeSumClosest(nums, target) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int threeSumClosest(int[] nums, int target) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line1 = sc.nextLine();\n        String[] parts = line1.replaceAll(\"[\\\\\\\\[\\\\\\\\],]\", \" \").trim().split(\"\\\\\\\\s+\");\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);\n        if (!sc.hasNextLine()) return;\n        String line2 = sc.nextLine().replaceAll(\"[^0-9-]\", \"\");\n        int target = Integer.parseInt(line2);\n        System.out.println(threeSumClosest(nums, target));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction threeSumClosest(nums, target) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const nums = input[0].replace(/[\\\\[\\\\],]/g, ' ').trim().split(/\\\\s+/).map(Number);\n    const target = parseInt(input[1].replace(/[^0-9-]/g, ''), 10);\n    console.log(threeSumClosest(nums, target));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\nint threeSumClosest(int* nums, int numsSize, int target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int* nums = malloc(10000 * sizeof(int));\n    int size = 0;\n    char line[1000000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                nums[size++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    int target = 0;\n    if (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while(*p && !isdigit(*p) && *p != '-') p++;\n        if(*p) target = atoi(p);\n    }\n    printf(\"%d\\n\", threeSumClosest(nums, size, target));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "-1 2 1 -4\n1", "expected_output": "2", "is_sample": True},
        {"input": "0 0 0\n1", "expected_output": "0", "is_sample": True},
        {"input": "1 1 1 0\n-100", "expected_output": "2", "is_sample": False},
        {"input": "1 1 1 1\n0", "expected_output": "3", "is_sample": False},
        {"input": "-100 -98 -2 -1\n-101", "expected_output": "-200", "is_sample": False},
        {"input": "1 2 4 8 16 32\n10", "expected_output": "11", "is_sample": False},
        {"input": "1 2 4 8 16 32\n20", "expected_output": "21", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100)]) + "\n10000", "expected_output": "294", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100)]) + "\n-10000", "expected_output": "3", "is_sample": False},
        {"input": " ".join(["1000"]*10) + "\n3000", "expected_output": "3000", "is_sample": False}
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
