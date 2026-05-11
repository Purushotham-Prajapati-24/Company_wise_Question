import json
import os

def generate_json():
    problem_id = 137
    title = "Single Number II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>137. Single Number II</h3>
<p>Given an integer array <code>nums</code> where every element appears <strong>three times</strong> except for one, which appears <strong>exactly once</strong>. <em>Find the single element and return it</em>.</p>

<p>You must implement a solution with a linear runtime complexity and use only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,3,2]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,1,0,1,99]
<strong>Output:</strong> 99
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Each element in <code>nums</code> appears exactly <strong>three times</strong> except for one element which appears <strong>once</strong>.</li>
</ul>"""

    input_format = "A single line containing an array of integers 'nums'."
    output_format = "An integer representing the element that appears exactly once."
    
    constraints = [
        "1 <= nums.length <= 3 * 10^4",
        "-2^31 <= nums[i] <= 2^31 - 1",
        "Linear O(n) runtime complexity.",
        "Constant O(1) extra space."
    ]
    
    explanation = """To find the single element in an array where all other elements appear three times using O(1) space:
1. **Finite State Machine**: We track the count of bits modulo 3.
2. **State Logic**:
   - Use two variables, `ones` and `twos`. 
   - `ones` stores bits that have appeared 1 time (mod 3).
   - `twos` stores bits that have appeared 2 times (mod 3).
   - When a bit appears a third time, both `ones` and `twos` are cleared for that bit.
3. **Transition**:
   - `ones = (ones ^ num) & ~twos`: Add `num` bits to `ones` only if they aren't already in `twos`.
   - `twos = (twos ^ num) & ~ones`: Add `num` bits to `twos` only if they aren't already in `ones` (after `ones` update).
4. **Complexity**:
   - Time Complexity: O(n)
   - Space Complexity: O(1)"""
    
    answer = """class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # bits that appear once
            ones = (ones ^ num) & ~twos
            # bits that appear twice
            twos = (twos ^ num) & ~ones
            
        return ones"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef singleNumber(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if not line: sys.exit()\n    nums = json.loads(line)\n    print(singleNumber(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nint singleNumber(vector<int>& nums){\n    // User logic\n    return 0;\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    line=line.substr(1,line.size()-2);\n    stringstream ss(line); string t; vector<int> n;\n    while(getline(ss,t,',')) if(!t.empty()) n.push_back(stoi(t));\n    cout<<singleNumber(n)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int singleNumber(int[] nums) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine().trim();\n        line=line.substring(1,line.length()-1);\n        String[] parts=line.split(\",\");\n        int[] n=new int[parts.length];\n        for(int i=0;i<parts.length;i++) n[i]=Integer.parseInt(parts[i].trim());\n        System.out.println(singleNumber(n));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction singleNumber(nums){\n    // User logic\n    return 0;\n}\nconsole.log(singleNumber(JSON.parse(fs.readFileSync(0,'utf8').trim())));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint singleNumber(int* nums, int numsSize){\n    // User logic\n    return 0;\n}\nint main(){\n    char buf[1000000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int arr[30001],cnt=0; char*tok=strtok(buf,\"[],\\n\\r \");\n    while(tok&&cnt<30001){arr[cnt++]=atoi(tok);tok=strtok(NULL,\"[],\\n\\r \");}\n    printf(\"%d\\n\",singleNumber(arr,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "[2,2,3,2]", "expected_output": "3", "is_sample": True},
        {"input": "[0,1,0,1,0,1,99]", "expected_output": "99", "is_sample": True},
        {"input": "[1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,1,1,2,2,2,3]", "expected_output": "3", "is_sample": False},
        {"input": "[-2,-2,1,1,-3,1,-2]", "expected_output": "-3", "is_sample": False},
        {"input": "[2147483647, 2147483647, 2147483647, 10]", "expected_output": "10", "is_sample": False},
        {"input": "[-2147483648, -2147483648, -2147483648, -500]", "expected_output": "-500", "is_sample": False},
        # Stress Tests (N=3*10^4)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    # Stress 8: Large array single at start
    nums8 = [12345] + [100]*3 + [i for i in range(9000) for _ in range(3)]
    test_cases[7] = {"input": json.dumps(nums8), "expected_output": "12345", "is_sample": False}
    # Stress 9: Large array single at end
    nums9 = [i for i in range(9999) for _ in range(3)] + [6789]
    test_cases[8] = {"input": json.dumps(nums9), "expected_output": "6789", "is_sample": False}
    # Stress 10: All large negative
    nums10 = [-10**9] * 3 + [-2 * 10**9] * 3 + [-1]
    test_cases[9] = {"input": json.dumps(nums10), "expected_output": "-1", "is_sample": False}

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

    output_path = "1-200/137_Single_Number_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
