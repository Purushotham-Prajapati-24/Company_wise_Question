import json
import os

def generate_json():
    problem_id = 84
    title = "Largest Rectangle in Histogram"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>84. Largest Rectangle in Histogram</h3>
<p>Given an array of integers <code>heights</code> representing the histogram's bar height where the width of each bar is <code>1</code>, return <em>the area of the largest rectangle in the histogram</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" style="width: 522px; height: 242px;" />
<pre>
<strong>Input:</strong> heights = [2,1,5,6,2,3]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" style="width: 202px; height: 142px;" />
<pre>
<strong>Input:</strong> heights = [2,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= heights[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the heights of the histogram bars."
    output_format = "An integer representing the maximum area of a rectangle that can be formed."
    
    constraints = [
        "1 <= heights.length <= 10^5",
        "0 <= heights[i] <= 10^4"
    ]
    
    explanation = """To find the largest rectangle in a histogram:
1. **Monotonic Stack Approach**:
   - Maintain a stack that stores indices of bars in increasing order of heights.
   - For each bar `i` from 0 to N (including a dummy bar of height 0 at the end):
     - While the current bar's height is less than the height of the bar at the top of the stack:
       - Pop the top index `j` from the stack. This bar's height `h = heights[j]` is a candidate height for the rectangle.
       - The width of the rectangle with height `h` is determined by the distance between the current index `i` and the index now at the top of the stack.
       - Specifically, `width = i - stack[-1] - 1`. If the stack is empty, `width = i`.
       - Update `max_area = max(max_area, h * width)`.
     - Push the current index `i` onto the stack.
2. **Complexity**:
   - Time Complexity: O(N) because each index is pushed and popped from the stack exactly once.
   - Space Complexity: O(N) for the stack."""
    
    answer = """def largestRectangleArea(heights):
    stack = []
    max_area = 0
    # Add a dummy height 0 at the end to flush out the stack
    heights.append(0)
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)
        
    heights.pop() # Restore original array
    return max_area"""

    boilerplate = {
        "python": "import sys\n\ndef largestRectangleArea(heights):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        heights = [int(x) for x in data]\n        print(largestRectangleArea(heights))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <stack>\n#include <algorithm>\n\nusing namespace std;\n\nint largestRectangleArea(vector<int>& heights) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int h;\n    vector<int> heights;\n    while (cin >> h) heights.push_back(h);\n    cout << largestRectangleArea(heights) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int largestRectangleArea(int[] heights) {\n        // User logic\n        return 0;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] heights = list.stream().mapToInt(i -> i).toArray();\n        System.out.println(largestRectangleArea(heights));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction largestRectangleArea(heights) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const heights = input.split(/\\s+/).map(Number);\n    console.log(largestRectangleArea(heights));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint largestRectangleArea(int* heights, int heightsSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int buff[100001], size = 0;\n    while (size < 100001 && scanf(\"%d\", &buff[size]) == 1) size++;\n    printf(\"%d\\n\", largestRectangleArea(buff, size));\n    return 0;\n}"
    }

    def _solve(heights):
        stack = []
        max_area = 0
        h_copy = list(heights) + [0]
        for i in range(len(h_copy)):
            while stack and h_copy[i] < h_copy[stack[-1]]:
                h = h_copy[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area

    test_cases = [
        {"input": "2 1 5 6 2 3", "expected_output": str(_solve([2,1,5,6,2,3])), "is_sample": True},
        {"input": "2 4", "expected_output": str(_solve([2,4])), "is_sample": True},
        {"input": "1 3 7", "expected_output": "7", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 1 1 1", "expected_output": "4", "is_sample": False},
        {"input": "5 4 3 2 1", "expected_output": str(_solve([5,4,3,2,1])), "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": str(_solve([1,2,3,4,5])), "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(1, 1001))), "expected_output": str(_solve(list(range(1, 1001)))), "is_sample": False},
        {"input": " ".join(map(str, range(1000, 0, -1))), "expected_output": str(_solve(list(range(1000, 0, -1)))), "is_sample": False},
        {"input": " ".join(["500"] * 1000), "expected_output": "500000", "is_sample": False}
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
        "topics": ["Array", "Stack", "Monotonic Stack"],
        "companyIndex": 0
    }

    output_path = "1-200/84_Largest_Rectangle_in_Histogram.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
