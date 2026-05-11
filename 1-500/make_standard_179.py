import json
import os

def generate_json():
    problem_id = 179
    title = "Largest Number"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>179. Largest Number</h3>
<p>Given a list of non-negative integers <code>nums</code>, arrange them such that they form the largest number and return it.</p>

<p>Since the result may be very large, you need to return a string instead of an integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,2]
<strong>Output:</strong> "210"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,30,34,5,9]
<strong>Output:</strong> "9534330"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated non-negative integers representing the array nums."
    output_format = "A string representing the largest number formed."
    
    constraints = [
        "1 <= nums.length <= 100",
        "0 <= nums[i] <= 10^9."
    ]
    
    explanation = """To form the largest number from a list of integers:
1. **Custom Sorting Comparator**:
   - Simply sorting the integers in descending order (e.g., 9 > 5) is not enough. For example, [3, 30] should be "330", not "303".
   - Convert integers to strings.
   - For any two strings `a` and `b`, compare the concatenated results `a + b` and `b + a`. 
   - If `a + b > b + a`, then `a` should come before `b`.
2. **Implementation**:
   - In Python, we can use `functools.cmp_to_key` to convert this comparison logic into a sorting key.
   - In other languages (C++, Java), use custom comparators in the sort function.
3. **Edge Case**:
   - If the largest number is "0" (e.g., [0, 0]), return "0" instead of "00".
4. **Complexity**:
   - Time Complexity: O(N log N) for sorting, plus concatenation costs O(N * L) where L is the max length of a number.
   - Space Complexity: O(N * L) to store the strings."""
    
    answer = """import functools

def largestNumber(nums: list[int]) -> str:
    # Convert numbers to strings
    nums_str = [str(n) for n in nums]
    
    # Custom comparison logic
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0
        
    # Sort with custom key
    nums_str.sort(key=functools.cmp_to_key(compare))
    
    # Handle the case where the largest number is 0
    if nums_str[0] == "0":
        return "0"
        
    return "".join(nums_str)"""

    boilerplate = {
        "python": "import sys\nimport functools\n\ndef largestNumber(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if not data:\n        sys.exit(0)\n    nums = [int(x) for x in data]\n    print(largestNumber(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nstring largestNumber(vector<int>& nums) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    vector<int> nums;\n    int val;\n    while (cin >> val) {\n        nums.push_back(val);\n    }\n    if (nums.empty()) return 0;\n    cout << largestNumber(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public String largestNumber(int[] nums) {\n        // User logic here\n        return \"\";\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line == null || line.trim().isEmpty()) return;\n        String[] parts = line.trim().split(\"\\\\s+\");\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) {\n            nums[i] = Integer.parseInt(parts[i]);\n        }\n        Solution sol = new Solution();\n        System.out.println(sol.largestNumber(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction largestNumber(nums) {\n    // User logic here\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    const nums = input.map(Number);\n    console.log(largestNumber(nums));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* largestNumber(int* nums, int numsSize) {\n    // User logic here\n    char* res = (char*)malloc(2);\n    res[0] = '0'; res[1] = '\\0';\n    return res;\n}\n\nint main() {\n    int capacity = 1000;\n    int* nums = (int*)malloc(capacity * sizeof(int));\n    int size = 0;\n    int val;\n    while (scanf(\"%d\", &val) == 1) {\n        if (size >= capacity) {\n            capacity *= 2;\n            nums = (int*)realloc(nums, capacity * sizeof(int));\n        }\n        nums[size++] = val;\n    }\n    if (size == 0) {\n        free(nums);\n        return 0;\n    }\n    char* result = largestNumber(nums, size);\n    printf(\"%s\\n\", result);\n    free(result);\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "10 2", "expected_output": "210", "is_sample": True},
        {"input": "3 30 34 5 9", "expected_output": "9534330", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "0 0", "expected_output": "0", "is_sample": False},
        {"input": "12 121", "expected_output": "12121", "is_sample": False},
        {"input": "128 12", "expected_output": "12812", "is_sample": False},
        {"input": "9 99 999", "expected_output": "999999", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(100)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join(["1000000000"]*100), "expected_output": "1000000000"*100, "is_sample": False},
        {"input": " ".join(["0"]*100), "expected_output": "0", "is_sample": False}
    ]

    # Stress case 8 expected output calculation
    s8_nums = [str(i) for i in range(100)]
    s8_nums.sort(key=functools.cmp_to_key(lambda a, b: -1 if a+b > b+a else (1 if b+a > a+b else 0)))
    test_cases[7]["expected_output"] = "".join(s8_nums)

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
        "topics": ["Array", "String", "Greedy", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/179_Largest_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    import functools
    generate_json()
