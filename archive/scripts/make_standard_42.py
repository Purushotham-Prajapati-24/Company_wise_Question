import json
import os

def generate_json():
    problem_id = 42
    title = "Trapping Rain Water"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>42. Trapping Rain Water</h3>
<p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;" />
<pre>
<strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>0 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the elevation map heights."
    output_format = "An integer representing the total amount of trapped water."
    
    constraints = [
        "n == height.length",
        "0 <= n <= 2 * 10^4",
        "0 <= height[i] <= 10^5"
    ]
    
    explanation = """To compute the total amount of trapped rainwater efficiently:
1. The capacity of a bar to trap water is determined by the maximum height to its left and the maximum height to its right. Specifically, `water[i] = max(0, min(left_max[i], right_max[i]) - height[i])`.
2. We can use a Two-Pointer approach to solve this in O(n) time and O(1) auxiliary space:
   - Initialize `left = 0`, `right = n - 1`, `left_max = 0`, and `right_max = 0`.
   - While `left < right`:
     - If `height[left] < height[right]`:
       - This implies that `right_max` is guaranteed to be greater than or equal to `height[left]`. Thus, the water trapped at index `left` depends only on `left_max`.
       - If `height[left] >= left_max`, update `left_max = height[left]`.
       - Otherwise, add `left_max - height[left]` to the total result.
       - Increment `left`.
     - Else (`height[left] >= height[right]`):
       - Similar logic applies: the water trapped at `right` depends only on `right_max`.
       - If `height[right] >= right_max`, update `right_max = height[right]`.
       - Otherwise, add `right_max - height[right]` to the total results.
       - Decrement `right`.
3. This single-pass approach ensures we visit each element exactly once with no extra space needed for auxiliary arrays."""
    
    answer = """def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    res = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                res += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
            right -= 1
            
    return res"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef trap(height):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if input_data:\n        height = [int(x) for x in input_data[0].strip().split()]\n        print(trap(height))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nint trap(vector<int>& height) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line; getline(cin, line);\n    stringstream ss(line);\n    int num;\n    vector<int> height;\n    while (ss >> num) height.push_back(num);\n    cout << trap(height) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int trap(int[] height) {\n        // User logic\n        return 0;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String[] tokens = sc.nextLine().trim().split(\"\\\\s+\");\n            if (tokens.length == 0 || tokens[0].isEmpty()) {\n                System.out.println(trap(new int[0]));\n            } else {\n                int[] height = new int[tokens.length];\n                for (int i = 0; i < tokens.length; i++) height[i] = Integer.parseInt(tokens[i]);\n                System.out.println(trap(height));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction trap(height) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split('\\n')[0];\nif (input) {\n    const height = input.split(/\\s+/).map(Number);\n    console.log(trap(height));\n} else {\n    console.log(trap([]));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint trap(int* height, int heightSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char line[200000];\n    if (fgets(line, sizeof(line), stdin)) {\n        int capacity = 1000, size = 0;\n        int* height = (int*)malloc(capacity * sizeof(int));\n        char* token = strtok(line, \" \\t\\r\\n\");\n        while (token) {\n            if (size == capacity) { capacity *= 2; height = (int*)realloc(height, capacity * sizeof(int)); }\n            height[size++] = atoi(token);\n            token = strtok(NULL, \" \\t\\r\\n\");\n        }\n        printf(\"%d\\n\", trap(height, size));\n        free(height);\n    }\n    return 0;\n}"
    }

    def _trap(h):
        if not h: return 0
        l, r = 0, len(h) - 1
        lm, rm = 0, 0
        ans = 0
        while l < r:
            if h[l] < h[r]:
                if h[l] >= lm: lm = h[l]
                else: ans += lm - h[l]
                l += 1
            else:
                if h[r] >= rm: rm = h[r]
                else: ans += rm - h[r]
                r -= 1
        return ans

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "0 1 0 2 1 0 1 3 2 1 2 1", "expected_output": "6", "is_sample": True},
        {"input": "4 2 0 3 2 5", "expected_output": "9", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "5 4 3 2 1", "expected_output": "0", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "0", "is_sample": False},
        {"input": "5 1 5", "expected_output": "4", "is_sample": False},
        {"input": "3 0 0 2 0 4", "expected_output": "10", "is_sample": False},
        {"input": "1 1 1 1 1", "expected_output": "0", "is_sample": False},
        # Last three: Stress tests
        {"input": ("10 0 " * 5000).strip(), "expected_output": str(_trap([10, 0] * 5000)), "is_sample": False},
        {"input": "100000 0 100000", "expected_output": "100000", "is_sample": False},
        {"input": " ".join(["0"] * 20000), "expected_output": "0", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Dynamic Programming", "Stack", "Monotonic Stack"],
        "companyIndex": 0
    }

    output_path = "1-200/42_Trapping_Rain_Water.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
