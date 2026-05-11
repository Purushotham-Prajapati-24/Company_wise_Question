import json
import os

def generate_json():
    problem_id = 136
    title = "Single Number"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>136. Single Number</h3>
<p>Given a <strong>non-empty</strong>&nbsp;array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,1,2,1,2]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
	<li>Each element in the array appears twice except for one element which appears only once.</li>
</ul>"""

    input_format = "A single line containing an array of integers 'nums'."
    output_format = "An integer representing the element that appears exactly once."
    
    constraints = [
        "1 <= nums.length <= 3 * 10^4",
        "-3 * 10^4 <= nums[i] <= 3 * 10^4",
        "Linear O(n) runtime complexity.",
        "Constant O(1) extra space."
    ]
    
    explanation = """To find the single element in an array where all other elements appear twice, we leverage the properties of the bitwise XOR operator:
1. **Properties of XOR**:
   - `x ^ x = 0`: Any number XORed with itself results in 0.
   - `x ^ 0 = x`: Any number XORed with 0 remains unchanged.
   - XOR is commutative and associative.
2. **Algorithm**:
   - Initialize a variable `res = 0`.
   - Iterate through every element in the array and XOR it with `res`.
   - The elements that appear twice will cancel each other out (reach 0), and only the element appearing once will remain in `res`.
3. **Complexity**:
   - Time Complexity: O(n) as we traverse the array once.
   - Space Complexity: O(1) as we only use one integer variable."""
    
    answer = """class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef singleNumber(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if not line: sys.exit()\n    nums = json.loads(line)\n    print(singleNumber(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nint singleNumber(vector<int>& nums){\n    // User logic\n    return 0;\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    line=line.substr(1,line.size()-2);\n    stringstream ss(line); string t; vector<int> n;\n    while(getline(ss,t,',')) if(!t.empty()) n.push_back(stoi(t));\n    cout<<singleNumber(n)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int singleNumber(int[] nums) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine().trim();\n        line=line.substring(1,line.length()-1);\n        String[] parts=line.split(\",\");\n        int[] n=new int[parts.length];\n        for(int i=0;i<parts.length;i++) n[i]=Integer.parseInt(parts[i].trim());\n        System.out.println(singleNumber(n));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction singleNumber(nums){\n    // User logic\n    return 0;\n}\nconsole.log(singleNumber(JSON.parse(fs.readFileSync(0,'utf8').trim())));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint singleNumber(int* nums, int numsSize){\n    // User logic\n    return 0;\n}\nint main(){\n    char buf[1000000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int arr[30001],cnt=0; char*tok=strtok(buf,\"[],\\n\\r \");\n    while(tok&&cnt<30001){arr[cnt++]=atoi(tok);tok=strtok(NULL,\"[],\\n\\r \");}\n    printf(\"%d\\n\",singleNumber(arr,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "[2,2,1]", "expected_output": "1", "is_sample": True},
        {"input": "[4,1,2,1,2]", "expected_output": "4", "is_sample": True},
        {"input": "[1]", "expected_output": "1", "is_sample": False},
        {"input": "[7,11,7]", "expected_output": "11", "is_sample": False},
        {"input": "[0,1,0]", "expected_output": "1", "is_sample": False},
        {"input": "[-1,-1,-2]", "expected_output": "-2", "is_sample": False},
        {"input": "[30000, 100, 30000]", "expected_output": "100", "is_sample": False},
        # Stress Tests (N=3*10^4)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    # Stress 8: Large array with single at start
    nums8 = [99] + [i for i in range(14999) for _ in range(2)]
    test_cases[7] = {"input": json.dumps(nums8), "expected_output": "99", "is_sample": False}
    # Stress 9: Large array with single at end
    nums9 = [i for i in range(14999) for _ in range(2)] + [88]
    test_cases[8] = {"input": json.dumps(nums9), "expected_output": "88", "is_sample": False}
    # Stress 10: All large numbers
    nums10 = [30000] * 2 + [29999] * 2 + [12345] + [1] * 2
    test_cases[9] = {"input": json.dumps(nums10), "expected_output": "12345", "is_sample": False}

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
        "topics": ["Array", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "1-200/136_Single_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
