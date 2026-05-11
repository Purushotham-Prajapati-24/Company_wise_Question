import json
import os

def generate_json():
    problem_id = 11
    title = "Container With Most Water"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>11. Container With Most Water</h3>
<p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Notice</strong> that you may not slant the container.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" />
<pre>
<strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>
"""

    input_format = "A single line containing the 'height' array (can be space-separated or in [1,2,3] format)."
    output_format = "An integer representing the maximum water container area."
    
    constraints = [
        "n == height.length",
        "2 <= n <= 10^5",
        "0 <= height[i] <= 10^4"
    ]
    
    explanation = """To find the maximum area, we use the Two-Pointer approach:
1. Initialize two pointers: `left` at the beginning (index 0) and `right` at the end (index n-1) of the array.
2. The area is defined by the shorter of the two lines and the distance between them: `area = min(height[left], height[right]) * (right - left)`.
3. In each step, calculate the current area and update the `max_area`.
4. To potentially find a larger area, we must move the pointer pointing to the shorter line inward.
5. Repeat until the pointers meet."""
    
    answer = """def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_area = max(max_area, h * w)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area"""

    boilerplate = {
        "python": "import sys\n\ndef maxArea(height):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) > 0:\n        line = input_data[0].strip()\n        height = [int(x) for x in line.replace('[','').replace(']','').replace(',',' ').split()]\n        print(maxArea(height))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nint maxArea(vector<int>& height) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        int val;\n        vector<int> height;\n        while (ss >> val) height.push_back(val);\n        cout << maxArea(height) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int maxArea(int[] height) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine();\n        String[] parts = line.replaceAll(\"[\\\\[\\\\],]\", \" \").trim().split(\"\\\\s+\");\n        if (parts.length == 0 || parts[0].isEmpty()) return;\n        int[] height = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) {\n            height[i] = Integer.parseInt(parts[i]);\n        }\n        System.out.println(maxArea(height));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction maxArea(height) {\n    // User logic\n    return 0;\n}\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    if (!input) return;\n    const height = input.replace(/[\\\\[\\\\],]/g, ' ').trim().split(/\\\\s+/).map(Number);\n    console.log(maxArea(height));\n}\n\nsolve();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint maxArea(int* height, int heightSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int* height = malloc(200000 * sizeof(int));\n    int size = 0;\n    char* line = malloc(1000000 * sizeof(char));\n    if (fgets(line, 1000000, stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                height[size++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    printf(\"%d\\n\", maxArea(height, size));\n    free(height);\n    free(line);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 8 6 2 5 4 8 3 7", "expected_output": "49", "is_sample": True},
        {"input": "1 1", "expected_output": "1", "is_sample": True},
        {"input": "2 2 2", "expected_output": "4", "is_sample": False},
        {"input": "1 2 4 3", "expected_output": "4", "is_sample": False},
        {"input": "10 9 8 7 6 5 4 3 2 1", "expected_output": "25", "is_sample": False},
        {"input": "8 8 1 1 1 1 8 8", "expected_output": "56", "is_sample": False},
        {"input": "0 2", "expected_output": "0", "is_sample": False},
        {"input": " ".join(["10000"] * 1000), "expected_output": "9990000", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 1001)]), "expected_output": "250000", "is_sample": False},
        {"input": " ".join([str(10000 - i) for i in range(1000)]), "expected_output": "8991999", "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
        "question_title": title,
        "difficulty": difficulty,
        "marks": marks,
        "question_text": html_description,
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
        "topics": ["Array", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "1-200/11_Container_With_Most_Water.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
