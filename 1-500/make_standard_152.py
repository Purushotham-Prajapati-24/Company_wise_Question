import json
import os

def generate_json():
    problem_id = 152
    title = "Maximum Product Subarray"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>152. Maximum Product Subarray</h3>
<p>Given an integer array <code>nums</code>, find a <span data-keyword="contiguous-subarray">contiguous</span> non-empty subarray within the array that has the largest product, and return <em>the product</em>.</p>

<p>The test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,-2,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [2,3] has the largest product 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,0,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The result cannot be 2, because [-2,-1] is not a subarray.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>The product of any subarray of <code>nums</code> is guaranteed to fit in a <strong>32-bit</strong> integer.</li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the array nums."
    output_format = "An integer representing the maximum product of a contiguous subarray."
    
    constraints = [
        "1 <= nums.length <= 2 * 10^4",
        "-10 <= nums[i] <= 10.",
        "Answer fits in 32-bit integer."
    ]
    
    explanation = """To find the maximum product subarray:
1. **Dynamic Programming (Tracking Min and Max)**:
   - When we encounter a negative number, a very small (negative) product can become a very large (positive) product when multiplied.
   - Therefore, at each step `i`, we maintain both the `current_max` product and the `current_min` product ending at index `i`.
2. **Logic**:
   - For each number `n` in `nums`:
     - If `n` is negative, swap `current_max` and `current_min`.
     - Update `current_max = max(n, current_max * n)`.
     - Update `current_min = min(n, current_min * n)`.
     - Update the overall `result = max(result, current_max)`.
3. **Complexity**:
   - Time Complexity: O(N) because we iterate through the array once.
   - Space Complexity: O(1) as we only use a few variables for tracking."""
    
    answer = """def maxProduct(nums):
    if not nums:
        return 0
        
    res = nums[0]
    cur_min, cur_max = 1, 1
    
    for n in nums:
        if n < 0:
            cur_min, cur_max = cur_max, cur_min
            
        cur_max = max(n, cur_max * n)
        cur_min = min(n, cur_min * n)
        
        res = max(res, cur_max)
        
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef maxProduct(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(maxProduct(list(map(int, data))))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <sstream>\nusing namespace std;\nint maxProduct(vector<int>& nums){\n    // User logic here\n    return 0;\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    istringstream ss(line); vector<int> nums; int x;\n    while(ss>>x) nums.push_back(x);\n    cout<<maxProduct(nums)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int maxProduct(int[] nums){\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine();\n        if(line==null||line.trim().isEmpty()) return;\n        String[] parts=line.trim().split(\"\\\\s+\");\n        int[] nums=new int[parts.length];\n        for(int i=0;i<parts.length;i++) nums[i]=Integer.parseInt(parts[i]);\n        System.out.println(maxProduct(nums));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction maxProduct(nums){\n    // User logic here\n    return 0;\n}\nconst nums=fs.readFileSync(0,'utf8').trim().split(/\\s+/).map(Number);\nif(nums.length) console.log(maxProduct(nums));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint maxProduct(int* nums, int numsSize){\n    // User logic here\n    return 0;\n}\nint main(){\n    char buf[200000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int nums[20001]; int cnt=0;\n    char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&cnt<20001){nums[cnt++]=atoi(tok);tok=strtok(NULL,\" \\t\\r\\n\");}\n    printf(\"%d\\n\",maxProduct(nums,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "2 3 -2 4", "expected_output": "6", "is_sample": True},
        {"input": "-2 0 -1", "expected_output": "0", "is_sample": True},
        {"input": "-2", "expected_output": "-2", "is_sample": False},
        {"input": "0 2", "expected_output": "2", "is_sample": False},
        {"input": "-2 3 -4", "expected_output": "24", "is_sample": False},
        {"input": "1 -2 3 -4 5 -6", "expected_output": "720", "is_sample": False},
        {"input": "0 -1 0 -2", "expected_output": "0", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"]*20000), "expected_output": "1", "is_sample": False},
        {"input": " ".join(["-1"]*20000), "expected_output": "1", "is_sample": False},
        {"input": " ".join([str(i % 10 - 5) for i in range(20000)]), "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(nums):
        if not nums: return "0"
        res = nums[0]
        cur_mi, cur_ma = 1, 1
        for n in nums:
            if n < 0: cur_mi, cur_ma = cur_ma, cur_mi
            cur_ma = max(n, cur_ma * n)
            cur_mi = min(n, cur_mi * n)
            res = max(res, cur_ma)
        return str(res)

    test_cases[9]["expected_output"] = _solve([i % 10 - 5 for i in range(20000)])

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

    output_path = "1-200/152_Maximum_Product_Subarray.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
