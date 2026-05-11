import json
import os

def generate_json():
    problem_id = 171
    title = "Excel Sheet Column Number"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>171. Excel Sheet Column Number</h3>
<p>Given a string <code>columnTitle</code> that represents the column title as it appears in an Excel sheet, return <em>its corresponding column number</em>.</p>

<p>For example:</p>
<pre>
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> columnTitle = "A"
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> columnTitle = "AB"
<strong>Output:</strong> 28
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> columnTitle = "ZY"
<strong>Output:</strong> 701
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= columnTitle.length &lt;= 7</code></li>
	<li><code>columnTitle</code> consists only of uppercase English letters.</li>
	<li><code>columnTitle</code> is in the range <code>["A", "FXSHRXW"]</code>.</li>
</ul>"""

    input_format = "A single string columnTitle."
    output_format = "An integer representing the column number."
    
    constraints = [
        "1 <= columnTitle.length <= 7",
        "Uppercase English letters only.",
        "Range: ['A', 'FXSHRXW']"
    ]
    
    explanation = """To convert an Excel column title to its number:
1. **Base-26 Conversion**:
   - This is essentially converting a base-26 number (where A=1, B=2, ..., Z=26) to base-10.
2. **Logic**:
   - Initialize `result = 0`.
   - Iterate through the string from left to right:
     - Multiply the current `result` by 26.
     - Add the value of the current character (`ord(char) - ord('A') + 1`).
3. **Complexity**:
   - Time Complexity: O(N) where N is the length of `columnTitle`.
   - Space Complexity: O(1)."""
    
    answer = """def titleToNumber(columnTitle: str) -> int:
    res = 0
    for char in columnTitle:
        res = res * 26 + (ord(char) - ord('A') + 1)
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef titleToNumber(columnTitle):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if not data:\n        sys.exit(0)\n    print(titleToNumber(data[0]))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint titleToNumber(string columnTitle) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string s;\n    if (cin >> s) {\n        cout << titleToNumber(s) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int titleToNumber(String columnTitle) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line == null || line.trim().isEmpty()) return;\n        Solution sol = new Solution();\n        System.out.println(sol.titleToNumber(line.trim()));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction titleToNumber(columnTitle) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    console.log(titleToNumber(input[0]));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint titleToNumber(char* columnTitle) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char s[1024];\n    if (scanf(\"%1023s\", s) == 1) {\n        printf(\"%d\\n\", titleToNumber(s));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "A", "expected_output": "1", "is_sample": True},
        {"input": "AB", "expected_output": "28", "is_sample": True},
        {"input": "ZY", "expected_output": "701", "is_sample": True},
        {"input": "Z", "expected_output": "26", "is_sample": False},
        {"input": "AA", "expected_output": "27", "is_sample": False},
        {"input": "AAA", "expected_output": "703", "is_sample": False},
        {"input": "ZZ", "expected_output": "702", "is_sample": False},
        # Stress cases
        {"input": "FXSHRXW", "expected_output": "2147483647", "is_sample": False},
        {"input": "ALL", "expected_output": "1000", "is_sample": False},
        {"input": "ZZZ", "expected_output": "18278", "is_sample": False}
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
        "topics": ["Math", "String"],
        "companyIndex": 0
    }

    output_path = "1-200/171_Excel_Sheet_Column_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
