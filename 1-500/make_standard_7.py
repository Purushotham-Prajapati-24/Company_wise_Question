import json
import os

def generate_json():
    problem_id = 7
    title = "Reverse Integer"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>7. Reverse Integer</h3>
<p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
"""

    input_format = "A single integer 'x'."
    output_format = "An integer representing reversed digits."
    
    constraints = [
        "-2^31 <= x <= 2^31 - 1"
    ]
    
    explanation = """To reverse an integer without 64-bit storage:
1. Extract the signs (positive or negative) and handle positive values for convenience.
2. Initialize 'rev' to 0.
3. Loop while 'x' is not zero:
   - Extract the last digit: pop = x % 10.
   - For 32-bit signed environments, check for overflow before performing 'rev = rev * 10 + pop'.
   - If rev > INT_MAX/10 or (rev == INT_MAX/10 and pop > 7), return 0. (Actually in Python we just check the final result against bounds).
4. For Python specifically: 
   - Python integers are arbitrary precision, so we reverse it and then check against the 32-bit signed bounds [-2^31, 2^31 - 1].
5. Multiply the reversed integer by its original sign and return the result if it's within bounds, otherwise return 0.

Time Complexity: O(log(X)) approximately O(10) for 32-bit integers.
Space Complexity: O(1)."""
    
    answer = """def reverse(x):
    limit = 2**31
    sign = 1 if x >= 0 else -1
    x = abs(x)
    res = 0
    while x:
        res = res * 10 + x % 10
        x //= 10
    if res > limit - 1 or res < -limit:
        return 0
    return res * sign"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef reverse(x: int) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().replace('[', '').replace(']', '').replace(',', ' ').split()\n    if data:\n        print(reverse(int(data[0])))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nint reverse(int x) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string s;\n    if (cin >> s) {\n        // Robustly parse the first integer from potential bracketed input\n        for(char &c : s) if(c == '[' || c == ']' || c == ',') c = ' ';\n        try {\n            size_t pos;\n            int x = stoi(s, &pos);\n            cout << reverse(x) << endl;\n        } catch (...) {\n            // Handle potential empty or invalid input\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int reverse(int x) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[\\\\[\\\\],]\", \"\");\n            if (!s.isEmpty()) {\n                try {\n                    int x = Integer.parseInt(s);\n                    System.out.println(reverse(x));\n                } catch (NumberFormatException e) {\n                    // Handle overflow or invalid input\n                }\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction reverse(x) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').replace(/[\\[\\],]/g, ' ').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    console.log(reverse(parseInt(input[0], 10)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint reverse(int x) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char s[100];\n    if (scanf(\"%99s\", s) == 1) {\n        // Robustly parse the integer\n        char cleaned[100];\n        int j = 0;\n        for (int i = 0; s[i]; i++) {\n            if (isdigit(s[i]) || s[i] == '-') {\n                cleaned[j++] = s[i];\n            }\n        }\n        cleaned[j] = '\\0';\n        if (j > 0) {\n            printf(\"%d\\n\", reverse(atoi(cleaned)));\n        }\n    }\n    return 0;\n}"
    }


    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "123", "expected_output": "321", "is_sample": True},
        {"input": "-123", "expected_output": "-321", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "120", "expected_output": "21", "is_sample": False},
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": "-1", "expected_output": "-1", "is_sample": False},
        {"input": "1534236469", "expected_output": "0", "is_sample": False},
        {"input": "-2147483648", "expected_output": "0", "is_sample": False},
        # Last three: Stress tests
        {"input": "2147483647", "expected_output": "0", "is_sample": False},
        {"input": "-2147447412", "expected_output": "-2147447412", "is_sample": False},
        {"input": "1463847412", "expected_output": "2147483641", "is_sample": False}
    ]
    # Check 1463847412 -> 2147483641. 2147483641 < 2147483647. Correct.

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
        "topics": ["Math"],
        "companyIndex": 0
    }

    output_path = "1-200/7_Reverse_Integer.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
