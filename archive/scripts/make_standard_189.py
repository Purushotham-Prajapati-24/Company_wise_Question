import json
import os

def generate_json():
    problem_id = 189
    title = "Rotate Array"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>189. Rotate Array</h3>
<p>Given an integer array <code>nums</code>, rotate the array to the right by <code>k</code> steps, where <code>k</code> is non-negative.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6,7], k = 3
<strong>Output:</strong> [5,6,7,1,2,3,4]
<strong>Explanation:</strong>
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,-100,3,99], k = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.</li>
	<li>Could you do it in-place with <code>O(1)</code> extra space?</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for nums. Line 2: integer k."
    output_format = "A space-separated sequence of rotated integers."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "0 <= k <= 10^5",
        "O(1) extra space expected."
    ]
    
    explanation = """To rotate an array to the right by `k` steps in-place with O(1) space:
1. **Normalization**:
   - The effective rotation is `k % n`, where `n` is the length of the array.
2. **Reverse Strategy**:
   - Step 1: Reverse the entire array.
   - Step 2: Reverse the first `k` elements.
   - Step 3: Reverse the remaining `n-k` elements.
3. **Logic**:
   - Reversing the whole array puts the elements intended for the front at the start, but in reverse order.
   - Reversing the two subsections individually restores their original relative order.
4. **Complexity**:
   - Time Complexity: O(N) because each element is moved at most twice.
   - Space Complexity: O(1) since we modify the array in-place."""
    
    answer = """def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
    # Reverse whole array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse last n-k elements
    reverse(k, n - 1)"""

    boilerplate = {
        "python": "import sys\n\ndef rotate(nums, k):\n    # User logic here (modify nums in-place)\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        nums = list(map(int, lines[0].split()))\n        k = int(lines[1])\n        rotate(nums, k)\n        print(\" \".join(map(str, nums)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nvoid rotate(vector<int>& nums, int k) {\n    // User logic\n}\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        stringstream ss(line1);\n        int val;\n        vector<int> nums;\n        while (ss >> val) nums.push_back(val);\n        int k = stoi(line2);\n        rotate(nums, k);\n        for (int i = 0; i < nums.size(); i++) {\n            cout << nums[i] << (i == nums.size() - 1 ? \"\" : \" \");\n        }\n        cout << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public void rotate(int[] nums, int k) {\n        // User logic\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 != null && line2 != null) {\n            String[] parts = line1.trim().split(\"\\\\s+\");\n            int[] nums = new int[parts.length];\n            for (int i = 0; i < parts.length; i++) {\n                nums[i] = Integer.parseInt(parts[i]);\n            }\n            int k = Integer.parseInt(line2.trim());\n            new Solution().rotate(nums, k);\n            StringBuilder sb = new StringBuilder();\n            for (int i = 0; i < nums.length; i++) {\n                sb.append(nums[i]).append(i == nums.length - 1 ? \"\" : \" \");\n            }\n            System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction rotate(nums, k) {\n    // User logic\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    let nums = input[0].trim().split(/\\\\s+/).map(Number);\n    let k = parseInt(input[1].trim());\n    rotate(nums, k);\n    console.log(nums.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nvoid rotate(int* nums, int numsSize, int k) {\n    // User logic\n}\n\nint main() {\n    char line1[1000000];\n    char line2[100];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        int capacity = 1000;\n        int* nums = (int*)malloc(capacity * sizeof(int));\n        int size = 0;\n        char* token = strtok(line1, \" \\t\\r\\n\");\n        while (token) {\n            if (size >= capacity) {\n                capacity *= 2;\n                nums = (int*)realloc(nums, capacity * sizeof(int));\n            }\n            nums[size++] = atoi(token);\n            token = strtok(NULL, \" \\t\\r\\n\");\n        }\n        int k = atoi(line2);\n        rotate(nums, size, k);\n        for (int i = 0; i < size; i++) {\n            printf(\"%d%s\", nums[i], i == size - 1 ? \"\" : \" \");\n        }\n        printf(\"\\n\");\n        free(nums);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4 5 6 7\\n3", "expected_output": "5 6 7 1 2 3 4", "is_sample": True},
        {"input": "-1 -100 3 99\\n2", "expected_output": "3 99 -1 -100", "is_sample": True},
        {"input": "1 2\\n3", "expected_output": "2 1", "is_sample": True},
        {"input": "1 2 3\\n0", "expected_output": "1 2 3", "is_sample": False},
        {"input": "1 2 3\\n3", "expected_output": "1 2 3", "is_sample": False},
        {"input": "1\\n100", "expected_output": "1", "is_sample": False},
        {"input": "1 2 3 4 5\\n1", "expected_output": "5 1 2 3 4", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n9999", "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n0", "expected_output": " ".join([str(i) for i in range(10000)]), "is_sample": False},
        {"input": "10 20 30\\n100000", "expected_output": "30 10 20", "is_sample": False}
    ]
    
    # Stress case 8 expected output calculation
    s8_n = 10000
    s8_k = 9999
    s8_nums = list(range(s8_n))
    s8_res = s8_nums[s8_n - (s8_k % s8_n):] + s8_nums[:s8_n - (s8_k % s8_n)]
    test_cases[7]["expected_output"] = " ".join(map(str, s8_res))

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
        "topics": ["Array", "Math", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "1-200/189_Rotate_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
