import json
import os

def generate_json():
    problem_id = 1
    title = "Two Sum"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1. Two Sum</h3>
<p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>"""

    input_format = "A single line containing space-separated integers for 'nums', followed by a second line containing the 'target' integer."
    output_format = "A list containing the two indices [i, j]."
    
    constraints = [
        "2 <= nums.length <= 10^4",
        "-10^9 <= nums[i] <= 10^9",
        "-10^9 <= target <= 10^9",
        "Exactly one solution exists."
    ]
    
    explanation = """To find the two numbers that add up to the target efficiently:
1. **Hash Map for Fast Lookup**: Use a hash map (or dictionary in Python) to store each number and its index as you iterate through the array.
2. **Complement Calculation**: For each element `nums[i]`, calculate its complement: `complement = target - nums[i]`.
3. **Check for Complement**: 
   - If the `complement` is already in the hash map, it means we've found the two numbers. The result is the index stored in the map and the current index `i`.
   - If not, add the current number and its index to the hash map and continue.
4. **Complexity**:
   - Time Complexity: O(n), as we traverse the list only once and each look-up in the hash map is O(1).
   - Space Complexity: O(n), to store the hash map with up to n elements."""
    
    answer = """def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i"""

    boilerplate = {
        "python": "import sys\n\ndef twoSum(nums, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        nums = [int(x) for x in input_data[0].strip().split()]\n        target = int(input_data[1].strip())\n        print(twoSum(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <sstream>\n\nusing namespace std;\n\nvector<int> twoSum(vector<int>& nums, int target) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int num;\n        vector<int> nums;\n        while (ss >> num) nums.push_back(num);\n        int target;\n        cin >> target;\n        vector<int> res = twoSum(nums, target);\n        cout << \"[\" << res[0] << \", \" << res[1] << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int[] twoSum(int[] nums, int target) {\n        // User logic\n        return new int[0];\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String[] parts = sc.nextLine().trim().split(\"\\\\s+\");\n            int[] nums = new int[parts.length];\n            for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);\n            int target = sc.nextInt();\n            int[] res = twoSum(nums, target);\n            System.out.println(Arrays.toString(res));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction twoSum(nums, target) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split('\\n');\nif (input.length >= 2) {\n    const nums = input[0].trim().split(/\\s+/).map(Number);\n    const target = parseInt(input[1].trim());\n    const res = twoSum(nums, target);\n    console.log(\"[\" + res.join(\", \") + \"]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint* twoSum(int* nums, int numsSize, int target, int* returnSize) {\n    // User logic\n    return NULL;\n}\n\nint main() {\n    char line[100000];\n    if (fgets(line, sizeof(line), stdin)) {\n        int cap = 100, count = 0;\n        int* nums = (int*)malloc(cap * sizeof(int));\n        char* pt = line;\n        while (*pt != '\\0') {\n            if (isdigit(*pt) || (*pt == '-' && isdigit(*(pt+1)))) {\n                if (count >= cap) {\n                    cap *= 2;\n                    nums = (int*)realloc(nums, cap * sizeof(int));\n                }\n                nums[count++] = atoi(pt);\n                while (*pt != '\\0' && (isdigit(*pt) || *pt == '-')) pt++;\n            } else { pt++; }\n        }\n        int target;\n        if (scanf(\"%d\", &target) == 1) {\n            int retSize = 0;\n            int* res = twoSum(nums, count, target, &retSize);\n            if (res && retSize == 2) { printf(\"[%d, %d]\\n\", res[0], res[1]); free(res); }\n            else { printf(\"[]\\n\"); }\n        }\n        free(nums);\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "2 7 11 15\\n9", "expected_output": "[0, 1]", "is_sample": True},
        {"input": "3 2 4\\n6", "expected_output": "[1, 2]", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "3 3\\n6", "expected_output": "[0, 1]", "is_sample": False},
        {"input": "1 5 8 2\\n10", "expected_output": "[2, 3]", "is_sample": False},
        {"input": "0 4 3 0\\n0", "expected_output": "[0, 3]", "is_sample": False},
        {"input": "-1 -2 -3 -4 -5\\n-8", "expected_output": "[2, 4]", "is_sample": False},
        {"input": "100 200 300\\n400", "expected_output": "[0, 2]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n19997", "expected_output": "[9998, 9999]", "is_sample": False},
        {"input": " ".join(["1"] * 9999 + ["2"]) + "\\n3", "expected_output": "[0, 9999]", "is_sample": False},
        {"input": " ".join([str(10**9 - i) for i in range(10000)]) + "\\n" + str(10**9 + 10**9 - 1), "expected_output": "[0, 1]", "is_sample": False}
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "1-200/1_Two_Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
