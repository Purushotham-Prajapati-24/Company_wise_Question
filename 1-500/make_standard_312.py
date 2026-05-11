import json
import os

def generate_json():
    problem_id = 312
    title = "Burst Balloons"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>312. Burst Balloons</h3>
<p>You are given <code>n</code> balloons, indexed from <code>0</code> to <code>n - 1</code>. Each balloon is painted with a number on it represented by an array <code>nums</code>. You are asked to burst all the balloons.</p>

<p>If you burst the <code>i</code><sup>th</sup> balloon, you will get <code>nums[i - 1] * nums[i] * nums[i + 1]</code> coins. After the burst, the <code>i - 1</code><sup>th</sup> and <code>i + 1</code><sup>th</sup> balloons become adjacent.</p>

<p>Find the maximum coins you can collect by bursting the balloons wisely.</p>

<p><strong>Note:</strong></p>
<ul>
	<li>You may imagine <code>nums[-1] = nums[n] = 1</code>. They are not real therefore you can not burst them.</li>
	<li><code>0 &lt;= n &lt;= 300</code>, <code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,1,5,8]
<strong>Output:</strong> 167
<strong>Explanation:</strong>
nums = [3,1,5,8] --&gt; [3,5,8] --&gt; [3,8] --&gt; [8] --&gt; []
coins =  3*1*5    +  3*5*8    +  1*3*8    +  1*8*1   = 167</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,5]
<strong>Output:</strong> 10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>"""

    input_format = "An array of integers `nums`."
    output_format = "An integer representing the maximum coins."
    
    constraints = [
        "1 <= n <= 300",
        "0 <= nums[i] <= 100"
    ]
    
    explanation = """To solve the Burst Balloons problem efficiently:
1. **Dynamic Programming (Range DP)**:
   - Let `dp[i][j]` be the maximum coins you can collect by bursting all balloons between index `i` and `j` (exclusive).
2. **Preprocessing**:
   - Add virtual balloons `1` at the start and end of `nums`. Now the range is from `0` to `n+1`.
3. **Transition**:
   - For a range `(i, j)`, consider the LAST balloon to be burst in this range. Let this balloon be at position `k` (`i < k < j`).
   - The total coins will be: `dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]`.
   - `dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])` for all `i < k < j`.
4. **Order of Solving**:
   - Iterate by the length of the interval (from 2 up to n+1).
5. **Complexity Analysis**:
   - Time: O(N^3) due to triple-nested loops (interval length, left index, split point).
   - Space: O(N^2) for the DP table."""
    
    answer = """class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add boundary balloons
        val = [1] + nums + [1]
        n = len(val)
        dp = [[0] * n for _ in range(n)]
        
        # l is the length of the range
        for length in range(2, n):
            # i is the start of the range
            for i in range(n - length):
                j = i + length
                # k is the last balloon to burst in range (i, j)
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], \
                                  dp[i][k] + dp[k][j] + val[i] * val[k] * val[j])
                                  
        return dp[0][n-1]"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef maxCoins(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    # Lethal extraction: find the first bracketed array\n    # e.g. nums = [3,1,5,8]\n    match = re.search(r'\\[[\\d\\s,.-]*\\]', raw_input)\n    if match:\n        nums = json.loads(match.group(0))\n        print(maxCoins(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nint maxCoins(vector<int>& nums) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    \n    regex re(\"-?\\\\d+\");\n    auto begin = sregex_iterator(input.begin(), input.end(), re);\n    auto end = sregex_iterator();\n    \n    vector<int> nums;\n    for (sregex_iterator i = begin; i != end; ++i) {\n        nums.push_back(stoi((*i).str()));\n    }\n    \n    cout << maxCoins(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int maxCoins(int[] nums) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while(sc.hasNextLine()) sb.append(sc.nextLine());\n        String input = sb.toString();\n\n        List<Integer> list = new ArrayList<>();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        while(m.find()) {\n            list.add(Integer.parseInt(m.group()));\n        }\n        \n        int[] nums = new int[list.size()];\n        for(int i=0; i<list.size(); i++) nums[i] = list.get(i);\n        \n        System.out.println(new Solution().maxCoins(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction maxCoins(nums) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconst match = input.match(/\\[[\\d\\s,.-]*\\]/);\nif (match) {\n    const nums = JSON.parse(match[0]);\n    console.log(maxCoins(nums));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint maxCoins(int* nums, int numsSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char buf[10000];\n    int len = 0, ch;\n    while((ch = getchar()) != EOF) buf[len++] = ch;\n    buf[len] = '\\0';\n\n    int nums[500], sz = 0;\n    char* p = buf;\n    while(*p) {\n        if(isdigit(*p) || *p == '-') {\n            nums[sz++] = strtol(p, &p, 10);\n        } else p++;\n    }\n    printf(\"%d\\n\", maxCoins(nums, sz));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[3,1,5,8]", "expected_output": "167", "is_sample": True},
        {"input": "[1,5]", "expected_output": "10", "is_sample": True},
        {"input": "[5]", "expected_output": "5", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "12", "is_sample": False},
        {"input": "[1,1,1]", "expected_output": "3", "is_sample": False},
        {"input": "[0,0,0]", "expected_output": "0", "is_sample": False},
        {"input": "[8,2,6,8]", "expected_output": "288", "is_sample": False},
        {"input": "[9,8,7,6,5,4,3,2,1]", "expected_output": "2700", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7,8,9,10]", "expected_output": "27420", "is_sample": False},
        {"input": "[1]*10".replace("[1]*10", "[1,1,1,1,1,1,1,1,1,1]"), "expected_output": "10", "is_sample": False}
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
        "companyIndex": 0
    }

    output_path = "201-400/312_Burst_Balloons.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
