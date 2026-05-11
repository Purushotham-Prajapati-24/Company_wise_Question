import json
import os

def generate_json():
    problem_id = 43
    title = "Multiply Strings"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>43. Multiply Strings</h3>
<p>Given two non-negative integers <code>num1</code> and <code>num2</code> represented as strings, return the product of <code>num1</code> and <code>num2</code>, also represented as a string.</p>

<p><strong>Note:</strong>&nbsp;You must not use any built-in BigInteger library or convert the inputs to integer directly.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num1 = "2", num2 = "3"
<strong>Output:</strong> "6"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num1 = "123", num2 = "456"
<strong>Output:</strong> "56088"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1.length, num2.length &lt;= 200</code></li>
	<li><code>num1</code> and <code>num2</code> consist of digits only.</li>
	<li>Both <code>num1</code> and <code>num2</code>&nbsp;do not contain any leading zero, except the number <code>0</code> itself.</li>
</ul>"""

    input_format = "A single line containing two space-separated digit strings 'num1' and 'num2'."
    output_format = "A string representing the product of the two input integers."
    
    constraints = [
        "1 <= num1.length, num2.length <= 200",
        "Inputs consist of digits only.",
        "No leading zeros except for '0' itself.",
        "Must not use built-in BigInteger libraries or direct string-to-int conversion of the whole number."
    ]
    
    explanation = """To multiply two large numbers represented as strings without using built-in high-precision libraries:
1. We simulate the elementary school long multiplication process.
2. If either number is "0", the result is "0".
3. Initialize a result array `res` of size `len(num1) + len(num2)` with zeros. The maximum possible length of the product is the sum of the lengths of the multipliers.
4. Iterate through `num1` from right to left using index `i` (from `len(num1)-1` to `0`).
5. For each digit in `num1`, iterate through `num2` from right to left using index `j`.
6. Multiply the digits `int(num1[i])` and `int(num2[j])`.
7. Add the product to the current value at `res[i + j + 1]`.
8. Handle the carry:
   - Add the carry (`res[i + j + 1] // 10`) to the next position `res[i + j]`.
   - Update `res[i + j + 1]` to its remainder modulo 10 (`res[i + j + 1] % 10`).
9. After completing the nested loops, convert the `res` array to a string. Skip any leading zeros at the beginning of the result.
10. Return the final string.

Time Complexity: O(N * M) where N and M are the lengths of num1 and num2.
Space Complexity: O(N + M) for the result array."""
    
    answer = """def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    
    res = [0] * (len(num1) + len(num2))
    
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            p1, p2 = i + j, i + j + 1
            total = mul + res[p2]
            
            res[p2] = total % 10
            res[p1] += total // 10
            
    # Skipping leading zeros
    start = 0
    while start < len(res) and res[start] == 0:
        start += 1
        
    return "".join(map(str, res[start:]))"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\nimport re\n\ndef multiply(num1, num2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    parts = re.findall(r'\\d+', data)\n    if len(parts) >= 2:\n        print(multiply(parts[0], parts[1]))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nstring multiply(string num1, string num2) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    string data;\n    string line;\n    while (getline(cin, line)) data += line + \" \";\n    string n1 = \"\", n2 = \"\";\n    string current = \"\";\n    vector<string> parts;\n    for (char c : data) {\n        if (isdigit(c)) current += c;\n        else if (!current.empty()) {\n            parts.push_back(current);\n            current = \"\";\n        }\n    }\n    if (!current.empty()) parts.push_back(current);\n    if (parts.size() >= 2) {\n        cout << multiply(parts[0], parts[1]) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static String multiply(String num1, String num2) {\n        // User logic here\n        return \"0\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String data = sb.toString();\n        List<String> parts = new ArrayList<>();\n        String[] tokens = data.split(\"[^0-9]\");\n        for (String t : tokens) {\n            if (!t.isEmpty()) parts.add(t);\n        }\n        if (parts.size() >= 2) {\n            System.out.println(multiply(parts.get(0), parts.get(1)));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction multiply(num1, num2) {\n    // User logic here\n    return \"0\";\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst parts = data.match(/\\d+/g);\nif (parts && parts.length >= 2) {\n    console.log(multiply(parts[0], parts[1]));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nchar* multiply(char* num1, char* num2) {\n    // User logic here\n    return \"0\";\n}\n\nint main() {\n    char* n1 = malloc(1000);\n    char* n2 = malloc(1000);\n    int count = 0;\n    char line[2000];\n    while (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p)) p++;\n            if (*p) {\n                char temp[1000];\n                int idx = 0;\n                while (*p && isdigit(*p)) temp[idx++] = *p++;\n                temp[idx] = '\\0';\n                if (count == 0) strcpy(n1, temp);\n                else if (count == 1) strcpy(n2, temp);\n                count++;\n            }\n        }\n    }\n    if (count >= 2) {\n        printf(\"%s\\n\", multiply(n1, n2));\n    }\n    free(n1); free(n2);\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "2 3", "expected_output": "6", "is_sample": True},
        {"input": "123 456", "expected_output": "56088", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "0 123", "expected_output": "0", "is_sample": False},
        {"input": "1 1", "expected_output": "1", "is_sample": False},
        {"input": "99 99", "expected_output": "9801", "is_sample": False},
        {"input": "100 10", "expected_output": "1000", "is_sample": False},
        {"input": "498828660196 840477629533", "expected_output": "419254329861794116453468", "is_sample": False},
        # Last three: Stress tests
        {"input": "9" * 200 + " 9" * 200, "expected_output": str(int("9" * 200) * int("9" * 200)), "is_sample": False},
        {"input": "1" + "0" * 199 + " 2" + "0" * 199, "expected_output": "2" + "0" * 398, "is_sample": False},
        {"input": "1" * 200 + " 1" * 200, "expected_output": str(int("1" * 200) * int("1" * 200)), "is_sample": False}
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
        "topics": ["Math", "String", "Simulation"],
        "companyIndex": 0
    }

    output_path = "1-200/43_Multiply_Strings.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
