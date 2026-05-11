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
        "python": "import sys\n\ndef missingNumber(nums: list[int]) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    if not input_data: sys.exit()\n    nums = list(map(int, input_data))\n    print(missingNumber(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint missingNumber(vector<int>& nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    vector<int> nums;\n    int val;\n    while (cin >> val) {\n        nums.push_back(val);\n    }\n    cout << missingNumber(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int missingNumber(int[] nums) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] nums = new int[list.size()];\n        for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n        System.out.println(new Solution().missingNumber(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction missingNumber(nums) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    let nums = input.map(Number);\n    console.log(missingNumber(nums));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint missingNumber(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int* nums = malloc(100005 * sizeof(int));\n    int size = 0;\n    int val;\n    while (scanf(\"%d\", &val) == 1) {\n        nums[size++] = val;\n    }\n    printf(\"%d\\n\", missingNumber(nums, size));\n    free(nums);\n    return 0;\n}"
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
