import json
import os

def generate_json():
    problem_id = 169
    title = "Majority Element"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>169. Majority Element</h3>
<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?"""

    input_format = "A single line containing space-separated integers representing the array nums."
    output_format = "An integer representing the majority element."
    
    constraints = [
        "n == nums.length",
        "1 <= n <= 5 * 10^4",
        "-10^9 <= nums[i] <= 10^9",
        "Linear time and constant space expected."
    ]
    
    explanation = """To find the majority element in O(N) time and O(1) space:
1. **Boyer-Moore Voting Algorithm**:
   - Maintain a `candidate` and a `count`.
   - Iterate through the array:
     - If `count == 0`, set the current element as the `candidate`.
     - If the current element equals `candidate`, increment `count`.
     - Otherwise, decrement `count`.
2. **Logic**:
   - Since the majority element appears more than `n/2` times, it will eventually "win" the voting process and remain as the candidate at the end of the traversal.
3. **Complexity**:
   - Time Complexity: O(N) because we iterate through the array once.
   - Space Complexity: O(1) as we only use two variables."""
    
    answer = """def majorityElement(nums: list[int]) -> int:
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
        
    return candidate"""

    boilerplate = {
        "python": "import sys\n\ndef majorityElement(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if not data:\n        sys.exit(0)\n    nums = [int(x) for x in data]\n    print(majorityElement(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint majorityElement(vector<int>& nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    vector<int> nums;\n    int val;\n    while (cin >> val) {\n        nums.push_back(val);\n    }\n    if (nums.empty()) return 0;\n    cout << majorityElement(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int majorityElement(int[] nums) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line == null || line.trim().isEmpty()) return;\n        String[] parts = line.trim().split(\"\\\\s+\");\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) {\n            nums[i] = Integer.parseInt(parts[i]);\n        }\n        Solution sol = new Solution();\n        System.out.println(sol.majorityElement(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction majorityElement(nums) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    const nums = input.map(Number);\n    console.log(majorityElement(nums));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint majorityElement(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int capacity = 1000;\n    int* nums = (int*)malloc(capacity * sizeof(int));\n    int size = 0;\n    int val;\n    while (scanf(\"%d\", &val) == 1) {\n        if (size >= capacity) {\n            capacity *= 2;\n            nums = (int*)realloc(nums, capacity * sizeof(int));\n        }\n        nums[size++] = val;\n    }\n    if (size == 0) {\n        free(nums);\n        return 0;\n    }\n    printf(\"%d\\n\", majorityElement(nums, size));\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3 2 3", "expected_output": "3", "is_sample": True},
        {"input": "2 2 1 1 1 2 2", "expected_output": "2", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 1 2", "expected_output": "1", "is_sample": False},
        {"input": "5 5 5 2 2", "expected_output": "5", "is_sample": False},
        {"input": "100 100 1 100 2", "expected_output": "100", "is_sample": False},
        {"input": "1 1 1 1 2 2 2", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": " ".join(["7"]*25001 + ["1"]*25000), "expected_output": "7", "is_sample": False},
        {"input": " ".join(["-1000000000"]*1000 + ["123"]*999), "expected_output": "-1000000000", "is_sample": False},
        {"input": " ".join(["0"]*10000), "expected_output": "0", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Divide and Conquer", "Sorting", "Counting"],
        "companyIndex": 0
    }

    output_path = "1-200/169_Majority_Element.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
