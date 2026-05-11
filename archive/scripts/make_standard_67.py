import json
import os

def generate_json():
    problem_id = 67
    title = "Add Binary"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>67. Add Binary</h3>
<p>Given two binary strings <code>a</code> and <code>b</code>, return <em>their sum as a binary string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = "11", b = "1"
<strong>Output:</strong> "100"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = "1010", b = "1011"
<strong>Output:</strong> "10101"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> and <code>b</code> consist&nbsp;only of <code>'0'</code> or <code>'1'</code> characters.</li>
	<li>Each string does not contain leading zeros except for the zero itself.</li>
</ul>"""

    input_format = "Two space-separated binary strings 'a' and 'b'."
    output_format = "A binary string representing the sum."
    
    constraints = [
        "1 <= a.length, b.length <= 10^4",
        "a and b consist only of '0' or '1' characters.",
        "No leading zeros except for the zero itself."
    ]
    
    explanation = """To add two binary strings:
1. **Initialize**: Use a pointer for each string (`i` for `a`, `j` for `b`) starting from the end, and a `carry` variable initialized to 0.
2. **Iteration**: Loop while `i >= 0`, `j >= 0`, or `carry > 0`:
   - Get the numeric value of the current binary digit if the pointer is within bounds; otherwise, use 0.
   - Calculate the sum of these values plus the `carry`.
   - The current bit in the total sum is `sum % 2`.
   - The new `carry` is `sum // 2`.
   - Append the current bit to a result list and move pointers to the left.
3. **Finish**: Reverse the result list and join its elements into a single string.
4. **Complexity**:
   - Time Complexity: O(max(N, M)), where N and M are the lengths of strings `a` and `b`.
   - Space Complexity: O(max(N, M)) to store the output string."""
    
    answer = """def addBinary(a, b):
    res = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        val_a = int(a[i]) if i >= 0 else 0
        val_b = int(b[j]) if j >= 0 else 0
        
        total = val_a + val_b + carry
        res.append(str(total % 2))
        carry = total // 2
        
        i -= 1
        j -= 1
        
    return "".join(res[::-1])"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef addBinary(a, b):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if len(data) >= 2:\n        print(addBinary(data[0], data[1]))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nstring addBinary(string a, string b) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    string a, b;\n    if (cin >> a >> b) {\n        cout << addBinary(a, b) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static String addBinary(String a, String b) {\n        // User logic\n        return \"\";\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String a = sc.next();\n            String b = sc.next();\n            System.out.println(addBinary(a, b));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction addBinary(a, b) {\n    // User logic\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nif (input.length >= 2) {\n    console.log(addBinary(input[0], input[1]));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nchar* addBinary(char* a, char* b) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    char a[10001], b[10001];\n    if (scanf(\"%s %s\", a, b) == 2) {\n        char* res = addBinary(a, b);\n        printf(\"%s\\n\", res);\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "11 1", "expected_output": "100", "is_sample": True},
        {"input": "1010 1011", "expected_output": "10101", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "0 0", "expected_output": "0", "is_sample": False},
        {"input": "1 1", "expected_output": "10", "is_sample": False},
        {"input": "111 111", "expected_output": "1110", "is_sample": False},
        {"input": "100 0", "expected_output": "100", "is_sample": False},
        {"input": "0 100", "expected_output": "100", "is_sample": False},
        # Last three: Stress tests
        {"input": "1"*10000 + " 1", "expected_output": "1" + "0"*10000, "is_sample": False},
        {"input": "1"*5000 + " " + "1"*5000, "expected_output": "1" + "1"*4999 + "0", "is_sample": False},
        {"input": "1"*10000 + " " + "0"*10000, "expected_output": "1"*10000, "is_sample": False}
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
        "topics": ["Math", "String", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "1-200/67_Add_Binary.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
