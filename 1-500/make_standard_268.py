import json
import os

def generate_json():
    problem_id = 268
    title = "Missing Number"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>268. Missing Number</h3>
<p>Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return <em>the only number in the range that is missing from the array.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,6,4,2,3,5,7,0,1]
<strong>Output:</strong> 8
<strong>Explanation:</strong> n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n</code></li>
	<li>All the numbers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you implement a solution using only <code>O(1)</code> extra space complexity and <code>O(n)</code> runtime complexity?</p>"""

    input_format = "A single line containing space-separated integers representing the array nums."
    output_format = "An integer representing the missing number."
    
    constraints = [
        "n == nums.length",
        "1 <= n <= 10^4",
        "0 <= nums[i] <= n",
        "Unique elements in nums.",
        "O(N) time complexity.",
        "O(1) extra space complexity."
    ]
    
    explanation = """To find the missing number in the range [0, n] efficiently:
1. **Sum Formula (Guaranteed Result)**:
   - The sum of all integers from 0 to `n` is given by the formula: `S = n * (n + 1) // 2`.
   - Calculate the actual sum of elements in the given array `nums`.
   - The missing number is `S - actual_sum`.
2. **XOR Approach (Alternative)**:
   - XOR all numbers from 0 to `n`.
   - XOR the result with every element in the array `nums`.
   - The remaining value is the missing number (since `x ^ x = 0`).
3. **Complexity**:
   - Time Complexity: O(N) to sum the elements.
   - Space Complexity: O(1) to store the sum variables."""
    
    answer = """def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef missingNumber(nums: list[int]) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Lethal parsing: extract all numbers from inside brackets if they exist\n    bracket_match = re.search(r'\\[(.*?)\\]', raw_input)\n    if bracket_match:\n        nums = [int(x) for x in re.findall(r'-?\\d+', bracket_match.group(1))]\n    else:\n        nums = [int(x) for x in re.findall(r'-?\\d+', raw_input)]\n    \n    if nums or '0' in raw_input or '[]' in raw_input:\n        print(missingNumber(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nint missingNumber(vector<int>& nums) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    vector<int> nums;\n    regex re_num(R\"(-?\\d+)\");\n    auto start = input.find('[');\n    auto end = input.find(']', start);\n    \n    string target = (start != string::npos && end != string::npos) ? input.substr(start, end - start) : input;\n    \n    for (sregex_iterator i = sregex_iterator(target.begin(), target.end(), re_num), end_iter; i != end_iter; ++i) {\n        nums.push_back(stoi(i->str()));\n    }\n    \n    cout << missingNumber(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int missingNumber(int[] nums) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (sc.hasNext()) {\n            String input = sc.next();\n            List<Integer> list = new ArrayList<>();\n            Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n            while (m.find()) {\n                list.add(Integer.parseInt(m.group()));\n            }\n            int[] nums = new int[list.size()];\n            for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n            System.out.println(new Solution().missingNumber(nums));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction missingNumber(nums) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst numsMatch = input.match(/\\[(.*?)\\]/) || [null, input];\nconst nums = (numsMatch[1] || numsMatch[0]).match(/-?\\d+/g)?.map(Number) || [];\n\nconsole.log(missingNumber(nums));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint missingNumber(int* nums, int numsSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    static char buffer[1000000];\n    int* nums = malloc(100005 * sizeof(int));\n    int size = 0;\n    \n    if (fread(buffer, 1, 999999, stdin) > 0) {\n        char *p = buffer;\n        while (*p) {\n            if (isdigit(*p) || (*p == '-' && isdigit(*(p+1)))) {\n                nums[size++] = strtol(p, &p, 10);\n            } else {\n                p++;\n            }\n        }\n    }\n    \n    printf(\"%d\\n\", missingNumber(nums, size));\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3 0 1", "expected_output": "2", "is_sample": True},
        {"input": "0 1", "expected_output": "2", "is_sample": True},
        {"input": "9 6 4 2 3 5 7 0 1", "expected_output": "8", "is_sample": True},
        {"input": "0", "expected_output": "1", "is_sample": False},
        {"input": "1", "expected_output": "0", "is_sample": False},
        {"input": "1 2", "expected_output": "0", "is_sample": False},
        {"input": "0 2", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 10001)]), "expected_output": "0", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]), "expected_output": "10000", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10001) if i != 5000]), "expected_output": "5000", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Math", "Binary Search", "Bit Manipulation", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/268_Missing_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
