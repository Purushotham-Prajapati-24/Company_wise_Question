import json
import os

def generate_json():
    problem_id = 41
    title = "First Missing Positive"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>41. First Missing Positive</h3>
<p>Given an unsorted integer array <code>nums</code>. Return the <em>smallest positive integer</em> that is <strong>not present</strong> in <code>nums</code>.</p>

<p>You must implement an algorithm that runs in <code>O(n)</code> time and uses <code>O(1)</code> auxiliary space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The numbers in the range [1,2] are all in the array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,-1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 1 is in the array but 2 is missing.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,8,9,11,12]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest positive integer 1 is missing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers for the array 'nums'."
    output_format = "An integer representing the smallest missing positive integer."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "-2^31 <= nums[i] <= 2^31 - 1",
        "Smallest missing positive is in range [1, nums.length + 1]."
    ]
    
    explanation = """To find the smallest missing positive integer in O(n) time and O(1) space:
1. The smallest missing positive integer must fall within the range [1, n + 1], where n is the length of the array.
2. We can treat the array itself as a hash map where each index `i` should ideally store the value `i + 1`.
3. Use a 'Cyclic Sort' inspired approach:
   - Iterate through the array. For each element `nums[i]`, if it is in the range [1, n] and is not at its correct position (`nums[i] != nums[nums[i] - 1]`), swap it with the element at the index it belongs to (`nums[i] - 1`).
   - Repeat this swap at index `i` until `nums[i]` is either out of range, negative, or correctly placed.
4. After one pass, iterate through the array again. The first index `i` where `nums[i] != i + 1` gives the missing positive integer `i + 1`.
5. If all integers from 1 to `n` are present, then the smallest missing positive is `n + 1`."""
    
    answer = """def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        # Place nums[i] at its correct index (nums[i] - 1)
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            
    # Check for the first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef firstMissingPositive(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if input_data:\n        nums = [int(x) for x in input_data[0].strip().split()]\n        print(firstMissingPositive(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\n\nusing namespace std;\n\nint firstMissingPositive(vector<int>& nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line; getline(cin, line);\n    stringstream ss(line);\n    int num;\n    vector<int> nums;\n    while (ss >> num) nums.push_back(num);\n    cout << firstMissingPositive(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.stream.Collectors;\n\npublic class Main {\n    public static int firstMissingPositive(int[] nums) {\n        // User logic\n        return 0;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String[] tokens = sc.nextLine().trim().split(\"\\\\s+\");\n            if (tokens.length == 0 || tokens[0].isEmpty()) {\n                System.out.println(firstMissingPositive(new int[0]));\n            } else {\n                int[] nums = new int[tokens.length];\n                for (int i = 0; i < tokens.length; i++) nums[i] = Integer.parseInt(tokens[i]);\n                System.out.println(firstMissingPositive(nums));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction firstMissingPositive(nums) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split('\\n')[0];\nif (input) {\n    const nums = input.split(/\\s+/).map(Number);\n    console.log(firstMissingPositive(nums));\n} else {\n    console.log(firstMissingPositive([]));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint firstMissingPositive(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char line[2000000];\n    if (fgets(line, sizeof(line), stdin)) {\n        int capacity = 1000, size = 0;\n        int* nums = (int*)malloc(capacity * sizeof(int));\n        char* token = strtok(line, \" \\t\\r\\n\");\n        while (token) {\n            if (size == capacity) { capacity *= 2; nums = (int*)realloc(nums, capacity * sizeof(int)); }\n            nums[size++] = atoi(token);\n            token = strtok(NULL, \" \\t\\r\\n\");\n        }\n        printf(\"%d\\n\", firstMissingPositive(nums, size));\n        free(nums);\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 0", "expected_output": "3", "is_sample": True},
        {"input": "3 4 -1 1", "expected_output": "2", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "7 8 9 11 12", "expected_output": "1", "is_sample": False},
        {"input": "-5 -4 -3", "expected_output": "1", "is_sample": False},
        {"input": "0 0 0", "expected_output": "1", "is_sample": False},
        {"input": "1", "expected_output": "2", "is_sample": False},
        {"input": "2", "expected_output": "1", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(1, 100001)]), "expected_output": "100001", "is_sample": False},
        {"input": " ".join([str(i) for i in range(2, 100002)]), "expected_output": "1", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 100000)]) + " 100005", "expected_output": "100000", "is_sample": False}
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "1-200/41_First_Missing_Positive.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
