import json
import os

def generate_json():
    problem_id = 377
    title = "Combination Sum IV"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>377. Combination Sum IV</h3>
<p>Given an array of <strong>distinct</strong> integers <code>nums</code> and a target integer <code>target</code>, return <em>the number of possible combinations that add up to</em> <code>target</code>.</p>

<p>The test cases are generated so that the answer can fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3], target = 4
<strong>Output:</strong> 7
<strong>Explanation:</strong>
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [9], target = 3
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li>All the elements of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?</p>"""

    input_format = "An array of distinct integers `nums` and a target integer `target`."
    output_format = "An integer representing the number of combinations."
    
    constraints = [
        "1 <= nums.length <= 200",
        "1 <= target <= 1000"
    ]
    
    explanation = """To find the number of possible combinations where the order of elements matters, we use **Dynamic Programming (Bottom-Up)**.

### Key Observation:
- This is a variation of the "Change Making" or "Knapsack" problem, but because order matters, it is more like counting paths in a DAG.
- Let `dp[i]` be the number of ways to reach target `i`.
- To reach `target`, we can pick any number `num` from `nums` if `num <= i`, and then we find the number of ways to reach `i - num`.
- Therefore, the recurrence is: `dp[i] = sum(dp[i - num] for num in nums if i - num >= 0)`.

### Algorithm Steps:
1. **Initialize DP**: `dp = [0] * (target + 1)`.
2. **Base Case**: `dp[0] = 1` (one way to reach 0: by picking nothing).
3. **Loop**:
   - For `i` from 1 to `target`:
     - For `num` in `nums`:
       - If `i >= num`:
         - `dp[i] += dp[i - num]`.
4. **Result**: Return `dp[target]`.

### Complexity Analysis:
- **Time Complexity**: $O(T \cdot N)$, where $T$ is the target and $N$ is the number of integers.
- **Space Complexity**: $O(T)$ for the DP array."""
    
    answer = """def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]"""

    boilerplate = {
        "python": "import sys\nimport re\ndef combinationSum4(nums, target):\n    # User logic here\n    pass\nif __name__ == '__main__':\n    input_data = sys.stdin.read()\n    all_nums = list(map(int, re.findall(r'-?\\d+', input_data)))\n    if all_nums:\n        target = all_nums[-1]\n        nums = all_nums[:-1]\n        print(combinationSum4(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\nusing namespace std;\nint combinationSum4(vector<int>& nums, int target) {\n    // User logic here\n    return 0;\n}\nint main() {\n    string input((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());\n    regex re(\"-?\\\\d+\");\n    sregex_iterator it(input.begin(), input.end(), re), end;\n    vector<int> all_nums;\n    while (it != end) all_nums.push_back(stoi(it->str()), ++it);\n    if (!all_nums.empty()) {\n        int target = all_nums.back();\n        all_nums.pop_back();\n        cout << combinationSum4(all_nums, target) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\npublic class Main {\n    public static int combinationSum4(int[] nums, int target) {\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        List<Integer> allNums = new ArrayList<>();\n        while (m.find()) allNums.add(Integer.parseInt(m.group()));\n        if (!allNums.isEmpty()) {\n            int target = allNums.get(allNums.size() - 1);\n            int[] nums = new int[allNums.size() - 1];\n            for (int i = 0; i < nums.length; i++) nums[i] = allNums.get(i);\n            System.out.println(combinationSum4(nums, target));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nconst combinationSum4 = (nums, target) => {\n    // User logic here\n    return 0;\n};\nconst input = fs.readFileSync(0, 'utf8');\nconst allNums = (input.match(/-?\\d+/g) || []).map(Number);\nif (allNums.length > 0) {\n    const target = allNums.pop();\n    console.log(combinationSum4(allNums, target));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\nint combinationSum4(int* nums, int numsSize, int target) {\n    // User logic here\n    return 0;\n}\nint main() {\n    char *buf = malloc(1000000);\n    int n = fread(buf, 1, 1000000, stdin);\n    buf[n] = '\\0';\n    int *all_nums = malloc(100000 * sizeof(int)), count = 0;\n    char *p = buf;\n    while (*p) {\n        if (isdigit(*p) || (*p == '-' && isdigit(*(p+1)))) {\n            all_nums[count++] = strtol(p, &p, 10);\n        } else p++;\n    }\n    if (count > 0) {\n        int target = all_nums[count-1];\n        printf(\"%d\\n\", combinationSum4(all_nums, count-1, target));\n    }\n    return 0;\n}"
    }


    test_cases = [
        {"input": "[1, 2, 3]\\n4", "expected_output": "7", "is_sample": True},
        {"input": "[9]\\n3", "expected_output": "0", "is_sample": True},
        {"input": "[1, 2]\\n3", "expected_output": "3", "is_sample": False},
        {"input": "[1, 2, 3]\\n0", "expected_output": "1", "is_sample": False},
        {"input": "[1]\\n10", "expected_output": "1", "is_sample": False},
        {"input": "[2, 4, 6]\\n10", "expected_output": "15", "is_sample": False},
        {"input": "[3, 4, 5, 6, 7]\\n10", "expected_output": "14", "is_sample": False},
        {"input": "[1]\\n1000", "expected_output": "1", "is_sample": False},
        {"input": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\\n20", "expected_output": "524288", "is_sample": False},
        {"input": "[1, 2]\\n10", "expected_output": "89", "is_sample": False},
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
        "topics": ["Array", "Dynamic Programming"],
        "companyIndex": 1
    }

    output_path = "301-500/377_Combination_Sum_IV.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
