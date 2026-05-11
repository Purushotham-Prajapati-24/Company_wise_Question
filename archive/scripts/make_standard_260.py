import json
import os

def generate_json():
    problem_id = 260
    title = "Single Number III"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>260. Single Number III</h3>
<p>Given an integer array <code>nums</code>, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in <strong>any order</strong>.</p>

<p>You must write an algorithm that runs in linear runtime complexity and uses&nbsp;only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,1,3,2,5]
<strong>Output:</strong> [3,5]
<strong>Explanation: </strong> [5, 3] is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,0]
<strong>Output:</strong> [-1,0]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>2 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Each integer in <code>nums</code> will appear twice, only two integers will appear once.</li>
</ul>"""

    input_format = "A stringified array of integers `nums`."
    output_format = "A stringified array containing the two unique integers."
    
    constraints = [
        "2 <= nums.length <= 30,000",
        "-2^31 <= nums[i] <= 2^31 - 1",
        "Exactly two elements appear once, all others twice."
    ]
    
    explanation = """To find the two unique numbers in linear time and constant space:
1. **XOR All Numbers**: XORing all numbers results in `x_or_sum = a ^ b`, where `a` and `b` are the two unique numbers.
2. **Find a Differentiating Bit**: Since `a != b`, there must be at least one bit that is different between them. We can find the lowest set bit in `x_or_sum` using `diff = x_or_sum & -x_or_sum`.
3. **Partition and XOR**: Iterate through the numbers again. If a number has the `diff` bit set, XOR it into `group1`; otherwise, XOR it into `group2`. This effectively separates `a` and `b` into different groups while all other pairs cancel each other out within their respective groups.
4. **Complexity**:
   - Time: O(N) because we iterate through the array twice.
   - Space: O(1) for storing the XOR sums."""
    
    answer = """class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: Get XOR sum of the two unique numbers
        x_or_sum = 0
        for n in nums:
            x_or_sum ^= n
            
        # Step 2: Get a bit that is different between the two numbers
        # (Lowest set bit)
        diff = x_or_sum & -x_or_sum
        
        # Step 3: Partition the numbers into two groups and find unique in each
        res = [0, 0]
        for n in nums:
            if n & diff:
                res[0] ^= n
            else:
                res[1] ^= n
                
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef singleNumber(nums):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        try:\n            arr = json.loads(line)\n        except:\n            arr = [int(x) for x in line.replace('[', '').replace(']', '').replace(',', ' ').split()]\n        res = singleNumber(arr)\n        res.sort()\n        print(json.dumps(res))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nvector<int> singleNumber(vector<int>& nums) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        int val;\n        vector<int> nums;\n        while (ss >> val) nums.push_back(val);\n        vector<int> res = singleNumber(nums);\n        sort(res.begin(), res.end());\n        cout << \"[\" << res[0] << \", \" << res[1] << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int[] singleNumber(int[] nums) {\n        // User logic\n        return new int[0];\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null) {\n            line = line.replace(\"[\", \"\").replace(\"]\", \"\").replace(\",\", \" \");\n            String[] parts = line.trim().split(\"\\\\s+\");\n            int[] nums = new int[parts.length];\n            for (int i = 0; i < parts.length; i++) {\n                if (!parts[i].isEmpty()) nums[i] = Integer.parseInt(parts[i]);\n            }\n            int[] res = new Solution().singleNumber(nums);\n            Arrays.sort(res);\n            System.out.println(Arrays.toString(res).replaceAll(\"\\\\s+\", \"\"));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction singleNumber(nums) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    let arr = JSON.parse(input);\n    let res = singleNumber(arr);\n    res.sort((a, b) => a - b);\n    console.log(JSON.stringify(res));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint compare(const void* a, const void* b) {\n    return (*(int*)a - *(int*)b);\n}\n\nint* singleNumber(int* nums, int numsSize, int* returnSize) {\n    // User logic\n    *returnSize = 2;\n    int* res = (int*)malloc(2 * sizeof(int));\n    return res;\n}\n\nint main() {\n    char line[1000000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* token = strtok(line, \"[], \");\n        int* nums = (int*)malloc(100000 * sizeof(int));\n        int size = 0;\n        while (token) {\n            nums[size++] = atoi(token);\n            token = strtok(NULL, \"[], \");\n        }\n        int returnSize = 0;\n        int* res = singleNumber(nums, size, &returnSize);\n        qsort(res, returnSize, sizeof(int), compare);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d%s\", res[i], i == returnSize - 1 ? \"\" : \",\");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,1,3,2,5]", "expected_output": "[3,5]", "is_sample": True},
        {"input": "[-1,0]", "expected_output": "[-1,0]", "is_sample": True},
        {"input": "[0,1]", "expected_output": "[0,1]", "is_sample": True},
        {"input": "[2,4,6,8,10,2,4,6,3,8]", "expected_output": "[10,3]", "is_sample": False},
        {"input": "[11,11,22,22,33,44]", "expected_output": "[33,44]", "is_sample": False},
        {"input": "[1,1,2,2,3,4,5,5,6,6]", "expected_output": "[3,4]", "is_sample": False},
        {"input": "[-2147483648,2147483647,-2147483648,0]", "expected_output": "[2147483647,0]", "is_sample": False},
        # Stress cases
        {"input": "[" + ",".join([str(i) for i in range(14999)] + [str(i) for i in range(14999)] + ["100000", "200000"]) + "]", "expected_output": "[100000,200000]", "is_sample": False},
        {"input": "[" + ",".join(["10"]*15000 + ["20"]*14998 + ["30", "40"]) + "]", "expected_output": "[30,40]", "is_sample": False},
        {"input": "[" + ",".join([str(i) for i in range(30000)]) + "]", "expected_output": "...", "is_sample": False} # This case isn't possible by constraints (every other must be twice)
    ]
    # Correcting the 10th test case logic to match constraints
    test_cases[9] = {"input": "[" + ",".join([str(i) for i in range(14999)] + [str(i) for i in range(14999)] + ["300000", "400000"]) + "]", "expected_output": "[300000,400000]", "is_sample": False}

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

    output_path = "201-400/260_Single_Number_III.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
