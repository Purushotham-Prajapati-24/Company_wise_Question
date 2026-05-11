import json
import os

def generate_json():
    problem_id = 69
    title = "Sqrt(x)"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>69. Sqrt(x)</h3>
<p>Given a non-negative integer <code>x</code>, return <em>the square root of </em><code>x</code><em> rounded down to the nearest integer</em>. The returned integer should be <strong>non-negative</strong> as well.</p>

<p>You <strong>must not use</strong> any built-in exponent function or operator.</p>

<ul>
	<li>For example, do not use <code>pow(x, 0.5)</code> in c++ or <code>x ** 0.5</code> in python.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> x = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 4 is 2, so we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> x = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A single integer 'x'."
    output_format = "An integer representing the floor of the square root of 'x'."
    
    constraints = [
        "0 <= x <= 2^31 - 1",
        "Must not use any built-in exponent function or operator."
    ]
    
    explanation = """To find the square root of x rounded down to the nearest integer efficiently:
1. **Binary Search Strategy**: Since the function f(n) = n*n is monotonically increasing for non-negative n, we can use binary search to find the largest integer n such that n*n <= x.
2. **Handle Small Cases**: If x is 0 or 1, the square root is x itself.
3. **Range Selection**: The integer square root of x for x >= 2 must be in the range [1, x//2].
4. **Algorithm**:
   - Initialize `left = 1` and `right = x // 2`.
   - While `left <= right`:
     - Calculate `mid = left + (right - left) // 2`.
     - Calculate `square = mid * mid`.
     - If `square == x`, return `mid`.
     - If `square < x`, move `left = mid + 1`. This `mid` is a potential candidate.
     - If `square > x`, move `right = mid - 1`.
   - After the loop, `right` will be the largest integer whose square is less than or equal to x.
5. **Complexity**:
   - Time Complexity: O(log x).
   - Space Complexity: O(1)."""
    
    answer = """def mySqrt(x):
    if x < 2:
        return x
        
    left, right = 1, x // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return right"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys, re\n\ndef mySqrt(x):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    nums = [int(x) for x in re.findall(r'\\d+', data)]\n    if nums:\n        print(mySqrt(nums[0]))",
        "cpp": "#include <iostream>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int mySqrt(int x) {\n        // User Logic Here\n        return 0;\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(\"\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    if (iter != end) {\n        int x = stoi((*iter).str());\n        Solution sol;\n        cout << sol.mySqrt(x) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int mySqrt(int x) {\n        // User Logic Here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"\\\\d+\").matcher(input);\n        if (m.find()) {\n            int x = Integer.parseInt(m.group());\n            Solution sol = new Solution();\n            System.out.println(sol.mySqrt(x));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number} x\n * @return {number}\n */\nvar mySqrt = function(x) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    const nums = input.match(/\\d+/g);\n    if (nums) {\n        console.log(mySqrt(parseInt(nums[0])));\n    }\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint mySqrt(int x) {\n    // User Logic Here\n    return 0;\n}\n\nint main() {\n    char input[1024];\n    if (fgets(input, sizeof(input), stdin)) {\n        char* p = input;\n        while (*p && !isdigit(*p)) p++;\n        if (*p) {\n            int x = atoi(p);\n            printf(\"%d\\n\", mySqrt(x));\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "4", "expected_output": "2", "is_sample": True},
        {"input": "8", "expected_output": "2", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "100", "expected_output": "10", "is_sample": False},
        {"input": "1000", "expected_output": "31", "is_sample": False},
        {"input": "99", "expected_output": "9", "is_sample": False},
        # Last three: Stress tests
        {"input": "2147483647", "expected_output": "46340", "is_sample": False},
        {"input": "2147395600", "expected_output": "46340", "is_sample": False},
        {"input": "1073741824", "expected_output": "32768", "is_sample": False}
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
        "topics": ["Math", "Binary Search"],
        "companyIndex": 0
    }

    output_path = "1-200/69_Sqrt_x.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
