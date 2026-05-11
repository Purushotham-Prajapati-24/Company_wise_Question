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
        "python": "import sys\nimport re\n\ndef trap(height):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    height = [int(x) for x in re.findall(r'-?\\d+', data)]\n    print(trap(height))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nint trap(vector<int>& height) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line;\n    vector<int> all_nums;\n    while (getline(cin, line)) {\n        for (char &c : line) if (c == ',' || c == '[' || c == ']' || c == '=' || c == ':' || c == '\"' || c == '{' || c == '}') c = ' ';\n        stringstream ss(line);\n        string part;\n        while (ss >> part) {\n            try { all_nums.push_back(stoi(part)); } catch(...) {}\n        }\n    }\n    cout << trap(all_nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int trap(int[] height) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> allNums = new ArrayList<>();\n        while (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[^0-9-]\", \"\");\n            if (!s.isEmpty()) try { allNums.add(Integer.parseInt(s)); } catch(Exception e) {}\n        }\n        int[] height = new int[allNums.size()];\n        for (int i = 0; i < allNums.size(); i++) height[i] = allNums.get(i);\n        System.out.println(trap(height));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction trap(height) {\n    // User logic here\n    return 0;\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst allNums = (data.match(/-?\\d+/g) || []).map(Number);\nconsole.log(trap(allNums));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint trap(int* height, int heightSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int* all_nums = malloc(100000 * sizeof(int));\n    int count = 0;\n    char line[1000];\n    while (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                all_nums[count++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    printf(\"%d\\n\", trap(all_nums, count));\n    free(all_nums);\n    return 0;\n}"
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
