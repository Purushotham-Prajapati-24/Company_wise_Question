import json
import os

def generate_json():
    problem_id = 55
    title = "Jump Game"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>55. Jump Game</h3>
<p>You are given an integer array <code>nums</code>. You are initially positioned at the array's <strong>first index</strong>, and each element in the array represents your maximum jump length at that position.</p>

<p>Return <code>true</code><em> if you can reach the last index, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "An array of non-negative integers nums."
    output_format = "Boolean true or false."
    
    constraints = [
        "1 <= nums.length <= 10^4",
        "0 <= nums[i] <= 10^5"
    ]
    
    explanation = """To determine if the last index is reachable:
1. **Greedy approach**: Maintain a variable `max_reachable` which stores the farthest index reachable from the current position.
2. **Iteration**: Loop through the array from `0` to `n-1`.
   - If current index `i > max_reachable`, it means index `i` is not reachable, so returning `false`.
   - Update `max_reachable = max(max_reachable, i + nums[i])`.
   - If `max_reachable >= n-1`, we have already reached the end, returning `true`.
3. **Complexity**:
   - **Time**: $O(N)$
   - **Space**: $O(1)$."""
    
    answer = """def canJump(nums):
    max_reachable = 0
    n = len(nums)
    for i in range(n):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])
        if max_reachable >= n - 1:
            return True
    return True"""

    boilerplate = {
        "python": "import sys\n\ndef canJump(nums):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    import re\n    input_data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'\\d+', input_data)]\n    print('true' if canJump(nums) else 'false')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    bool canJump(vector<int>& nums) {\n        // User Logic Here\n        return false;\n    }\n};\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    regex rgx(\"\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    vector<int> nums;\n    while (iter != end) {\n        nums.push_back(stoi(iter->str()));\n        iter++;\n    }\n    Solution sol;\n    cout << (sol.canJump(nums) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public boolean canJump(int[] nums) {\n        // User Logic Here\n        return false;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"\\\\d+\").matcher(input);\n        List<Integer> list = new ArrayList<>();\n        while (m.find()) list.add(Integer.parseInt(m.group()));\n        int[] nums = new int[list.size()];\n        for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n        Solution sol = new Solution();\n        System.out.println(sol.canJump(nums) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar canJump = function(nums) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const nums = (input.match(/\\d+/g) || []).map(Number);\n    console.log(canJump(nums) ? 'true' : 'false');\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <stdbool.h>\n\nbool canJump(int* nums, int numsSize) {\n    // User Logic Here\n    return false;\n}\n\nint main() {\n    int capacity = 10000, size = 0;\n    int* nums = malloc(capacity * sizeof(int));\n    int found = 0, c;\n    long long current = 0;\n    while ((c = getchar()) != EOF) {\n        if (isdigit(c)) {\n            if (!found) { found = 1; current = c - '0'; } else current = current * 10 + (c - '0');\n        } else {\n            if (found) {\n                if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); }\n                nums[size++] = (int)current; found = 0;\n            }\n        }\n    }\n    if (found) {\n        if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); }\n        nums[size++] = (int)current;\n    }\n    printf(\"%s\\n\", canJump(nums, size) ? \"true\" : \"false\");\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2 3 1 1 4", "expected_output": "true", "is_sample": True},
        {"input": "3 2 1 0 4", "expected_output": "false", "is_sample": True},
        {"input": "0", "expected_output": "true", "is_sample": False},
        {"input": "1 0", "expected_output": "true", "is_sample": False},
        {"input": "1 0 1 0", "expected_output": "false", "is_sample": False},
        {"input": "2 0 0", "expected_output": "true", "is_sample": False},
        {"input": "1 1 1", "expected_output": "true", "is_sample": False},
        {"input": "5 4 3 2 1 0 0", "expected_output": "false", "is_sample": False},
        {"input": "10 0 0 0", "expected_output": "true", "is_sample": False},
        {"input": " ".join(["1"] * 10), "expected_output": "true", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Greedy"],
        "companyIndex": 0
    }

    output_path = "1-200/55_Jump_Game.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
