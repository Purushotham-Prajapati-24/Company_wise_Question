import json
import os
import sys

# Increase the limit for integer to string conversion for large test cases
sys.set_int_max_str_digits(0)

def generate_json():
    problem_id = 238
    title = "Product of Array Except Self"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>238. Product of Array Except Self</h3>
<p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Can you solve the problem in <code>O(1)</code>&nbsp;extra&nbsp;space complexity? (The output array <strong>does not</strong> count as extra space for space complexity analysis.)</p>
"""

    input_format = "A stringified 1D array of integers."
    output_format = "A stringified 1D array of integers."
    
    constraints = [
        "2 <= nums.length <= 100,000",
        "-30 <= nums[i] <= 30",
        "No division allowed.",
        "O(n) time and O(1) space (excluding output)."
    ]
    
    explanation = """To solve this without division and in O(1) extra space:
1. **Prefix Products**: Initialize the result array `res`. Loop through `nums` and store the prefix product (product of all elements to the left) for each index in `res`.
   - `res[i] = res[i-1] * nums[i-1]`
2. **Suffix Products**: Maintain a variable `suffix_prod` (initially 1). Loop backwards through the array. Multiply the current `res[i]` by `suffix_prod` and then update `suffix_prod` by multiplying it with `nums[i]`.
3. **Logic**: At each index `i`, `res[i]` will eventually contain `(product of elements left of i) * (product of elements right of i)`.
4. **Complexity**:
   - Time: O(N) where N is the length of `nums`.
   - Space: O(1) extra space (ignoring the output array)."""
    
    answer = """class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Left products
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
            
        # Right products
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
            
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef productExceptSelf(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        match = re.search(r'\\[.*?\\]', input_data)\n        str_arr = match.group(0) if match else input_data\n        str_arr = str_arr.replace('[', '').replace(']', '').replace(',', ' ')\n        nums = [int(x) for x in str_arr.split()]\n        print(json.dumps(productExceptSelf(nums)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n#include <regex>\n\nusing namespace std;\n\nvector<int> productExceptSelf(vector<int>& nums) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        regex num_re(\"[-]?\\\\d+\");\n        vector<int> nums;\n        auto words_begin = sregex_iterator(line.begin(), line.end(), num_re);\n        auto words_end = sregex_iterator();\n        for (sregex_iterator i = words_begin; i != words_end; ++i) nums.push_back(stoi(i->str()));\n        \n        vector<int> res = productExceptSelf(nums);\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); i++) {\n            cout << res[i] << (i == res.size() - 1 ? \"\" : \", \");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int[] productExceptSelf(int[] nums) {\n        // User logic here\n        return new int[0];\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null) {\n            List<Integer> list = new ArrayList<>();\n            Matcher m = Pattern.compile(\"[-]?\\\\d+\").matcher(line);\n            while (m.find()) list.add(Integer.parseInt(m.group()));\n            \n            int[] nums = new int[list.size()];\n            for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n            \n            int[] res = new Solution().productExceptSelf(nums);\n            System.out.println(Arrays.toString(res));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction productExceptSelf(nums) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    const match = input.match(/\\[.*\\]/)?.[0] || input;\n    const nums = match.replace(/[\\[\\]]/g, '').split(',').map(s => parseInt(s.trim())).filter(n => !isNaN(n));\n    console.log(JSON.stringify(productExceptSelf(nums)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint* productExceptSelf(int* nums, int numsSize, int* returnSize) {\n    // User logic here\n    *returnSize = numsSize;\n    return NULL;\n}\n\nint main() {\n    static char line[1000000];\n    if (fgets(line, sizeof(line), stdin)) {\n        int* nums = (int*)malloc(100000 * sizeof(int));\n        int size = 0;\n        char* p = line;\n        while (*p) {\n            if (isdigit(*p) || *p == '-') {\n                nums[size++] = strtol(p, &p, 10);\n            } else p++;\n        }\n        \n        int returnSize = 0;\n        int* res = productExceptSelf(nums, size, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d%s\", res[i], i == returnSize - 1 ? \"\" : \", \");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,3,4]", "expected_output": "[24,12,8,6]", "is_sample": True},
        {"input": "[-1,1,0,-3,3]", "expected_output": "[0,0,9,0,0]", "is_sample": True},
        {"input": "[0,0]", "expected_output": "[0,0]", "is_sample": False},
        {"input": "[1,1]", "expected_output": "[1,1]", "is_sample": False},
        {"input": "[2,3,5]", "expected_output": "[15,10,6]", "is_sample": False},
        {"input": "[10,20]", "expected_output": "[20,10]", "is_sample": False},
        {"input": "[1,0,3,4]", "expected_output": "[0,12,0,0]", "is_sample": False},
        # Stress Tests (100,000 nodes)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_pes(nums):
        n = len(nums)
        res = [1] * n
        l = 1
        for i in range(n):
            res[i] = l
            l *= nums[i]
        r = 1
        for i in range(n-1, -1, -1):
            res[i] *= r
            r *= nums[i]
        return res

    # Stress 8: 100,000 ones
    n8 = [1] * 100000
    test_cases[7] = {"input": json.dumps(n8), "expected_output": json.dumps(_solve_pes(n8)), "is_sample": False}
    # Stress 9: 100,000 alternating 1, -1
    n9 = [1, -1] * 50000
    test_cases[8] = {"input": json.dumps(n9), "expected_output": json.dumps(_solve_pes(n9)), "is_sample": False}
    # Stress 10: 100,000 with one zero
    n10 = [2] * 50000 + [0] + [3] * 49999
    # expected too large for strings, output will be correct based on logic
    test_cases[9] = {"input": json.dumps(n10), "expected_output": json.dumps(_solve_pes(n10)), "is_sample": False}

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
        "topics": ["Array", "Prefix Sum"],
        "companyIndex": 0
    }

    output_path = "201-400/238_Product_of_Array_Except_Self.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
