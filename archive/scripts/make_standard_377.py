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
        "python": (
            "import sys\n"
            "import json\n\n"
            "def combinationSum4(nums, target):\n"
            "    # User logic here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    lines = sys.stdin.read().strip().splitlines()\n"
            "    if len(lines) >= 2:\n"
            "        nums = json.loads(lines[0])\n"
            "        target = json.loads(lines[1])\n"
            "        print(combinationSum4(nums, target))\n"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <string>\n"
            "using namespace std;\n\n"
            "int combinationSum4(vector<int>& nums, int target) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "}\n\n"
            "int main() {\n"
            "    string line;\n"
            "    if (getline(cin, line)) {\n"
            "        vector<int> nums;\n"
            "        int i = 0, n = line.length();\n"
            "        while (i < n) {\n"
            "            if (line[i] == '-' || (line[i] >= '0' && line[i] <= '9')) {\n"
            "                int v = 0, sign = 1;\n"
            "                if (line[i] == '-') { sign = -1; i++; }\n"
            "                while (i < n && line[i] >= '0' && line[i] <= '9') {\n"
            "                    v = v * 10 + (line[i] - '0'); i++;\n"
            "                }\n"
            "                nums.push_back(v * sign);\n"
            "            } else { i++; }\n"
            "        }\n"
            "        if (getline(cin, line)) {\n"
            "            int target = 0, sign = 1, j = 0;\n"
            "            while (j < line.length() && (line[j] < '0' || line[j] > '9') && line[j] != '-') j++;\n"
            "            if (j < line.length() && line[j] == '-') { sign = -1; j++; }\n"
            "            while (j < line.length() && line[j] >= '0' && line[j] <= '9') {\n"
            "                target = target * 10 + (line[j] - '0'); j++;\n"
            "            }\n"
            "            target *= sign;\n"
            "            cout << combinationSum4(nums, target) << endl;\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        ),
        "java": (
            "import java.util.*;\n\n"
            "public class Main {\n"
            "    public static int combinationSum4(int[] nums, int target) {\n"
            "        // User logic here\n"
            "        return 0;\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextLine()) {\n"
            "            String line = sc.nextLine().trim();\n"
            "            line = line.substring(1, line.length() - 1);\n"
            "            String[] parts = line.split(\",\");\n"
            "            List<Integer> list = new ArrayList<>();\n"
            "            for (String p : parts) {\n"
            "                p = p.trim();\n"
            "                if (!p.isEmpty()) list.add(Integer.parseInt(p));\n"
            "            }\n"
            "            int[] nums = list.stream().mapToInt(i -> i).toArray();\n"
            "            if (sc.hasNextLine()) {\n"
            "                int target = Integer.parseInt(sc.nextLine().trim());\n"
            "                System.out.println(combinationSum4(nums, target));\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "var combinationSum4 = function(nums, target) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "};\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').trim().split('\\n');\n"
            "    if (input.length >= 2) {\n"
            "        const nums = JSON.parse(input[0].trim());\n"
            "        const target = JSON.parse(input[1].trim());\n"
            "        console.log(combinationSum4(nums, target));\n"
            "    }\n"
            "}\n"
            "main();\n"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n\n"
            "int combinationSum4(int* nums, int numsSize, int target) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "}\n\n"
            "int main() {\n"
            "    char buf[10000];\n"
            "    if (fgets(buf, sizeof(buf), stdin)) {\n"
            "        int nums[500];\n"
            "        int numsSize = 0, i = 0;\n"
            "        while (buf[i]) {\n"
            "            if (buf[i] == '-' || (buf[i] >= '0' && buf[i] <= '9')) {\n"
            "                int v = 0, sign = 1;\n"
            "                if (buf[i] == '-') { sign = -1; i++; }\n"
            "                while (buf[i] >= '0' && buf[i] <= '9') {\n"
            "                    v = v * 10 + (buf[i] - '0'); i++;\n"
            "                }\n"
            "                nums[numsSize++] = v * sign;\n"
            "            } else { i++; }\n"
            "        }\n"
            "        if (fgets(buf, sizeof(buf), stdin)) {\n"
            "            int target = atoi(buf);\n"
            "            printf(\"%d\\n\", combinationSum4(nums, numsSize, target));\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        )
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
