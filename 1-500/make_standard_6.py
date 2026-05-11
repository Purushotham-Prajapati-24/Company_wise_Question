import json
import os

def generate_json():
    problem_id = 6
    title = "ZigZag Conversion"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>6. ZigZag Conversion</h3>
<p>The string <code>"PAYPALISHIRING"</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>And then read line by line: <code>"PAHNAPLSIIGYIR"</code></p>

<p>Write the code that will take a string and make this conversion given a number of rows:</p>

<pre>
string convert(string s, int numRows);
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "PAYPALISHIRING", numRows = 3
<strong>Output:</strong> "PAHNAPLSIIGYIR"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "PAYPALISHIRING", numRows = 4
<strong>Output:</strong> "PINALSIGYAHRPI"
<strong>Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "A", numRows = 1
<strong>Output:</strong> "A"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), <code>','</code> and <code>'.'</code>.</li>
	<li><code>1 &lt;= numRows &lt;= 1000</code></li>
</ul>
"""

    input_format = "Line 1: The input string 's'.\nLine 2: The number of rows 'numRows'."
    output_format = "A string representing the ZigZag converted result."
    
    constraints = [
        "1 <= s.length <= 1000",
        "s consists of English letters, ',', and '.'",
        "1 <= numRows <= 1000"
    ]
    
    explanation = """To perform a ZigZag conversion:
1. If numRows is 1 or greater than the string length, the zigzag pattern is equivalent to the original string. Return it.
2. Create 'numRows' strings (or lists) to store characters for each row.
3. Traverse the string while maintaining:
   - 'curr_row': The index of the row to append the current character.
   - 'down': A boolean indicating the direction of movement (downward or upward diagonal).
4. For each character:
   - Append it to row 'curr_row'.
   - If we reach the first or last row, toggle the 'down' flag.
   - Increment or decrement 'curr_row' based on the 'down' flag.
5. Combine all row strings together to get the final converted output.

This approach ensures each character is visited once, achieving O(N) time and O(N) space complexity."""
    
    answer = """def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = ["" for _ in range(numRows)]
    curr_row = 0
    down = False
    
    for char in s:
        rows[curr_row] += char
        if curr_row == 0 or curr_row == numRows - 1:
            down = not down
        curr_row += 1 if down else -1
        
    return "".join(rows)"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef convert(s, numRows):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().splitlines()\n    if len(data) >= 2:\n        s = data[0].strip().strip('\"')\n        numRows = int(data[1].strip())\n        print(convert(s, numRows))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nstring convert(string s, int numRows) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    string s;\n    int numRows;\n    if (getline(cin, s)) {\n        if (!s.empty() && s.back() == '\\r') s.pop_back();\n        size_t first = s.find_first_not_of(\" \\t\\n\\r\\\"\");\n        if (string::npos != first) {\n            size_t last = s.find_last_not_of(\" \\t\\n\\r\\\"\");\n            s = s.substr(first, (last - first + 1));\n        } else {\n            s = \"\";\n        }\n        if (cin >> numRows) {\n            cout << convert(s, numRows) << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static String convert(String s, int numRows) {\n        // User logic here\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine().trim();\n            if (s.startsWith(\"\\\"\") && s.endsWith(\"\\\"\")) {\n                s = s.substring(1, s.length() - 1);\n            }\n            if (sc.hasNextInt()) {\n                int numRows = sc.nextInt();\n                System.out.println(convert(s, numRows));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction convert(s, numRows) {\n    // User logic here\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    let s = input[0].trim();\n    if (s.startsWith('\"') && s.endsWith('\"')) s = s.slice(1, -1);\n    const numRows = parseInt(input[1].trim());\n    console.log(convert(s, numRows));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nchar* convert(char* s, int numRows) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    char s[100005];\n    if (fgets(s, sizeof(s), stdin)) {\n        s[strcspn(s, \"\\r\\n\")] = 0;\n        char *start = s;\n        while(*start == ' ' || *start == '\"') start++;\n        char *end = s + strlen(s) - 1;\n        while(end > start && (*end == ' ' || *end == '\"')) {\n            *end = '\\0';\n            end--;\n        }\n        int numRows;\n        if (scanf(\"%d\", &numRows) == 1) {\n            printf(\"%s\\n\", convert(start, numRows));\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "PAYPALISHIRING\n3", "expected_output": "PAHNAPLSIIGYIR", "is_sample": True},
        {"input": "PAYPALISHIRING\n4", "expected_output": "PINALSIGYAHRPI", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "A\n1", "expected_output": "A", "is_sample": False},
        {"input": "ABCDE\n2", "expected_output": "ACEBD", "is_sample": False},
        {"input": "ABCDE\n5", "expected_output": "ABCDE", "is_sample": False},
        {"input": "PAYPALISHIRING\n2", "expected_output": "PYAIHRNAPLSIIG", "is_sample": False},
        {"input": "PAYPALISHIRING\n20", "expected_output": "PAYPALISHIRING", "is_sample": False},
        # Last three: Stress tests
        {"input": "A" * 1000 + "\n3", "expected_output": "A" * 1000, "is_sample": False},
        {"input": "PAYPALISHIRING" * 50 + "\n5", "expected_output": convert("PAYPALISHIRING" * 50, 5) if 'convert' in locals() else "", "is_sample": False}, # I'll compute manually or use dummy
        {"input": "ABC" * 333 + "A\n1000", "expected_output": "ABC" * 333 + "A", "is_sample": False}
    ]
    # Correcting dynamic expected output
    def _convert_ref(s, numRows):
        if numRows == 1 or numRows >= len(s): return s
        rows = ["" for _ in range(numRows)]; r, d = 0, False
        for c in s:
            rows[r] += c
            if r == 0 or r == numRows-1: d = not d
            r += 1 if d else -1
        return "".join(rows)

    test_cases[8]["expected_output"] = _convert_ref("PAYPALISHIRING" * 50, 5)

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
        "topics": ["String"],
        "companyIndex": 0
    }

    output_path = "1-200/6_ZigZag_Conversion.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
