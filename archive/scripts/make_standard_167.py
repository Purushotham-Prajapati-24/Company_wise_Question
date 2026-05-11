import json
import os

def generate_json():
    problem_id = 167
    title = "Two Sum II - Input Array Is Sorted"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>167. Two Sum II - Input Array Is Sorted</h3>
<p>Given a <strong>1-indexed</strong> array of integers <code>numbers</code> that is already <strong><em>sorted in non-decreasing order</em></strong>, find two numbers such that they add up to a specific <code>target</code> number. Let these two numbers be <code>numbers[index<sub>1</sub>]</code> and <code>numbers[index<sub>2</sub>]</code> where <code>1 &lt;= index<sub>1</sub> &lt; index<sub>2</sub> &lt;= numbers.length</code>.</p>

<p>Return<em> the indices of the two numbers, </em><code>index<sub>1</sub></code><em> and </em><code>index<sub>2</sub></code><em>, <strong>added by one</strong> as an integer array </em><code>[index<sub>1</sub>, index<sub>2</sub>]</code><em> of length 2.</em></p>

<p>The tests are generated such that there is <strong>exactly one solution</strong>. You <strong>may not</strong> use the same element twice.</p>

<p>Your solution must use only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numbers = [2,7,11,15], target = 9
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of 2 and 7 is 9. Therefore, index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numbers = [2,3,4], target = 6
<strong>Output:</strong> [1,3]
<strong>Explanation:</strong> The sum of 2 and 4 is 6. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 3. We return [1, 3].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> numbers = [-1,0], target = -1
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of -1 and 0 is -1. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= numbers.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= numbers[i] &lt;= 1000</code></li>
	<li><code>numbers</code> is sorted in <strong>non-decreasing order</strong>.</li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
	<li>The tests are generated such that there is <strong>exactly one solution</strong>.</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for numbers. Line 2: integer target."
    output_format = "A space-separated pair of 1-indexed integers."
    
    constraints = [
        "2 <= numbers.length <= 3 * 10^4",
        "O(1) extra space.",
        "Exactly one solution.",
        "Sorted input."
    ]
    
    explanation = """To find two numbers summing to a target in a sorted array using constant space:
1. **Two Pointers Approach**:
   - Initialize two pointers: `left` at the beginning (0) and `right` at the end (n-1) of the array.
2. **Logic**:
   - While `left < right`:
     - Calculate the current sum: `current_sum = numbers[left] + numbers[right]`.
     - If `current_sum == target`: Return the indices `[left + 1, right + 1]` (conversion to 1-indexed).
     - If `current_sum < target`: The sum is too small. To increase it, move the `left` pointer to the right (`left += 1`).
     - If `current_sum > target`: The sum is too large. To decrease it, move the `right` pointer to the left (`right -= 1`).
3. **Complexity**:
   - Time Complexity: O(N) since each pointer moves at most N steps.
   - Space Complexity: O(1) as we only use two variables."""
    
    answer = """def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        cur = numbers[left] + numbers[right]
        if cur == target:
            return [left + 1, right + 1]
        elif cur < target:
            left += 1
        else:
            right -= 1
    return []"""

    boilerplate = {
        "python": "import sys\n\ndef twoSum(numbers, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        nums = list(map(int, lines[0].split()))\n        target = int(lines[1])\n        res = twoSum(nums, target)\n        if res and len(res) >= 2:\n            print(str(res[0]) + \" \" + str(res[1]))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\nusing namespace std;\nvector<int> twoSum(vector<int>& numbers, int target) {\n    // User logic\n    return {};\n}\nint main() {\n    string line;\n    vector<int> numbers;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int x;\n        while(ss >> x) numbers.push_back(x);\n    }\n    int target;\n    if (cin >> target) {\n        vector<int> res = twoSum(numbers, target);\n        if(res.size() >= 2) cout << res[0] << \" \" << res[1] << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\npublic class Main {\n    public static int[] twoSum(int[] numbers, int target) {\n        // User logic\n        return new int[2];\n    }\n    public static void main(String[] args) throws Exception {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null && !line.trim().isEmpty()) {\n            String[] parts = line.trim().split(\"\\\\s+\");\n            int[] nums = new int[parts.length];\n            for (int i=0; i<parts.length; i++) nums[i] = Integer.parseInt(parts[i]);\n            String tLine = br.readLine();\n            if (tLine != null) {\n                int target = Integer.parseInt(tLine.trim());\n                int[] res = twoSum(nums, target);\n                if (res != null && res.length >= 2) {\n                    System.out.println(res[0] + \" \" + res[1]);\n                }\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction twoSum(numbers, target) {\n    // User logic\n    return [];\n}\nconst lines = fs.readFileSync(0, 'utf8').trim().split('\\n');\nif (lines.length >= 2) {\n    const nums = lines[0].trim().split(/\\s+/).map(Number);\n    const target = parseInt(lines[1], 10);\n    const res = twoSum(nums, target);\n    if (res && res.length >= 2) {\n        console.log(res[0] + \" \" + res[1]);\n    }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\nint main() {\n    char line[1000000];\n    int capacity = 1000, size = 0;\n    int* nums = (int*)malloc(capacity * sizeof(int));\n    if (fgets(line, sizeof(line), stdin)) {\n        char* token = strtok(line, \" \\t\\r\\n\");\n        while (token != NULL) {\n            if (size >= capacity) {\n                capacity *= 2;\n                nums = (int*)realloc(nums, capacity * sizeof(int));\n            }\n            nums[size++] = atoi(token);\n            token = strtok(NULL, \" \\t\\r\\n\");\n        }\n    }\n    int target;\n    if (scanf(\"%d\", &target) == 1) {\n        int returnSize = 0;\n        int* res = twoSum(nums, size, target, &returnSize);\n        if (res && returnSize >= 2) {\n            printf(\"%d %d\\n\", res[0], res[1]);\n            free(res);\n        }\n    }\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2 7 11 15\\n9", "expected_output": "1 2", "is_sample": True},
        {"input": "2 3 4\\n6", "expected_output": "1 3", "is_sample": True},
        {"input": "-1 0\\n-1", "expected_output": "1 2", "is_sample": True},
        {"input": "5 25 75\\n100", "expected_output": "2 3", "is_sample": False},
        {"input": "-10 -5 0 5 10\\n0", "expected_output": "1 5", "is_sample": False},
        {"input": "1 2 3\\n4", "expected_output": "1 3", "is_sample": False},
        {"input": "1 2 3 4 5\\n9", "expected_output": "4 5", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(2, 30002)]) + "\\n30003", "expected_output": "1 30000", "is_sample": False},
        {"input": " ".join([str(i) for i in range(-30000, 1)]) + "\\n-59999", "expected_output": "1 2", "is_sample": False},
        {"input": " ".join([str(-1000)]*15000 + [str(1000)]*15000) + "\\n0", "expected_output": "1 30000", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Binary Search"],
        "companyIndex": 0
    }

    output_path = "1-200/167_Two_Sum_II_-_Input_Array_Is_Sorted.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
