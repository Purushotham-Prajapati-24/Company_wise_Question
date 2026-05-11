import json
import os

def generate_json():
    problem_id = 50
    title = "Pow(x, n)"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>50. Pow(x, n)</h3>
<p>Implement <a href="http://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(x, n)</a>, which calculates <code>x</code> raised to the power <code>n</code> (i.e., <code>x<sup>n</sup></code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = 10
<strong>Output:</strong> 1024.00000
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 2.10000, n = 3
<strong>Output:</strong> 9.26100
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = -2
<strong>Output:</strong> 0.25000
<strong>Explanation:</strong> 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-100.0 &lt; x &lt; 100.0</code></li>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>n</code> is an integer.</li>
	<li>Either <code>x</code> is not zero or <code>n &gt; 0</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= x<sup>n</sup> &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing a float 'x' and an integer 'n' separated by a space."
    output_format = "A float representing x raised to the power n, formatted to 5 decimal places."
    
    constraints = [
        "-100.0 < x < 100.0",
        "-2^31 <= n <= 2^31 - 1",
        "n is an integer.",
        "Either x is not zero or n > 0.",
        "-10^4 <= x^n <= 10^4",
        "Required time complexity: O(log n)."
    ]
    
    explanation = """To calculate x raised to the power n efficiently:
1. A naive multiplication approach would take O(n) time, which is too slow for n up to 2^31.
2. We use **Binary Exponentiation** (also known as Exponentiation by Squaring), which reduces the complexity to O(log n).
3. **Core Logic**:
   - If `n` is negative, we can compute `(1/x)^(-n)`. Note that for `-2^31`, we must be careful with integer overflow in some languages (though not Python).
   - Use an iterative approach:
     - Initialize `res = 1.0`.
     - While `n > 0`:
       - If `n` is odd (`n % 2 == 1`), multiply the result by the current `x`.
       - Square the current `x` (`x = x * x`).
       - Divide `n` by 2 (`n //= 2`).
4. This method works because every power `n` can be represented as a sum of powers of 2 (its binary representation). Square `x` at each bit position and multiply into the result whenever the corresponding bit in `n` is 1.

Time Complexity: O(log n).
Space Complexity: O(1)."""
    
    answer = """def myPow(x, n):
    if n == 0:
        return 1.0
    
    # Handle negative power
    if n < 0:
        x = 1 / x
        n = -n
        
    res = 1.0
    while n > 0:
        if n % 2 == 1:
            res *= x
        x *= x
        n //= 2
        
    return res"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\nimport re\n\ndef myPow(x, n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = re.findall(r'-?\\d+(?:\\.\\d+)?', data)\n    if len(nums) >= 2:\n        x = float(nums[0])\n        n = int(float(nums[1])) # Handle case where n might be written as float in input\n        print(\"{:.5f}\".format(myPow(x, n)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <iomanip>\n#include <algorithm>\n\nusing namespace std;\n\ndouble myPow(double x, int n) {\n    // User logic here\n    return 0.0;\n}\n\nint main() {\n    string line, data;\n    while (getline(cin, line)) data += line + \" \";\n    for (char &c : data) if (c == ',' || c == '[' || c == ']' || c == '=' || c == ':' || c == '\"' || c == '{' || c == '}') c = ' ';\n    stringstream ss(data);\n    string s1, s2;\n    if (ss >> s1 >> s2) {\n        double x = stod(s1);\n        int n = stoi(s2);\n        cout << fixed << setprecision(5) << myPow(x, n) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static double myPow(double x, int n) {\n        // User logic here\n        return 0.0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<String> allTokens = new ArrayList<>();\n        while (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[^0-9.-]\", \"\");\n            if (!s.isEmpty()) allTokens.add(s);\n        }\n        if (allTokens.size() >= 2) {\n            double x = Double.parseDouble(allTokens.get(0));\n            int n = (int) Double.parseDouble(allTokens.get(1));\n            System.out.printf(\"%.5f\\n\", myPow(x, n));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction myPow(x, n) {\n    // User logic here\n    return 0.0;\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst nums = (data.match(/-?\\d+(\\.\\d+)?/g) || []).map(Number);\nif (nums.length >= 2) {\n    console.log(myPow(nums[0], Math.floor(nums[1])).toFixed(5));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\ndouble myPow(double x, int n) {\n    // User logic here\n    return 0.0;\n}\n\nint main() {\n    char data[1000];\n    if (fgets(data, sizeof(data), stdin)) {\n        char* p = data;\n        double x = 0; int n = 0; int found = 0;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-' && *p != '.') p++;\n            if (*p) {\n                if (found == 0) x = atof(p);\n                else if (found == 1) n = atoi(p);\n                found++;\n                if (*p == '-' || *p == '.') p++;\n                while (*p && (isdigit(*p) || *p == '.')) p++;\n            }\n            if (found >= 2) break;\n        }\n        printf(\"%.5f\\n\", myPow(x, n));\n    }\n    return 0;\n}"
    }

    def _pow(x, n):
        return "{:.5f}".format(pow(x, n))

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "2.00000 10", "expected_output": "1024.00000", "is_sample": True},
        {"input": "2.10000 3", "expected_output": "9.26100", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "2.00000 -2", "expected_output": "0.25000", "is_sample": False},
        {"input": "1.00000 2147483647", "expected_output": "1.00000", "is_sample": False},
        {"input": "-1.00000 2147483647", "expected_output": "-1.00000", "is_sample": False},
        {"input": "-1.00000 2147483646", "expected_output": "1.00000", "is_sample": False},
        {"input": "0.00001 2", "expected_output": "0.00000", "is_sample": False},
        # Last three: Stress tests
        {"input": "1.00000 -2147483648", "expected_output": "1.00000", "is_sample": False},
        {"input": "2.00000 -2147483648", "expected_output": "0.00000", "is_sample": False},
        {"input": "0.00001 2147483647", "expected_output": "0.00000", "is_sample": False}
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
        "topics": ["Math", "Recursion"],
        "companyIndex": 0
    }

    output_path = "1-200/50_Pow_x_n.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
