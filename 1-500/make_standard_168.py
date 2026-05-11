import json
import os

def generate_json():
    problem_id = 168
    title = "Excel Sheet Column Title"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>168. Excel Sheet Column Title</h3>
<p>Given an integer <code>columnNumber</code>, return <em>its corresponding column title as it appears in an Excel sheet</em>.</p>

<p>For example:</p>
<pre>
A -&gt; 1
B -&gt; 2
C -&gt; 3
...
Z -&gt; 26
AA -&gt; 27
AB -&gt; 28 
...
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> columnNumber = 1
<strong>Output:</strong> "A"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> columnNumber = 28
<strong>Output:</strong> "AB"
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> columnNumber = 701
<strong>Output:</strong> "ZY"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= columnNumber &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A single integer columnNumber."
    output_format = "A string representing the Excel column title."
    
    constraints = [
        "1 <= columnNumber <= 2^31 - 1"
    ]
    
    explanation = """To convert an integer to an Excel column title:
1. **Bijective Base-26 Conversion**:
   - This problem is similar to converting a number to base-26, but since it's 1-indexed (A=1, ..., Z=26), we need to adjust the number at each step.
2. **Logic**:
   - While `columnNumber > 0`:
     - Subtract 1 from `columnNumber` to turn it into a 0-indexed system (0=A, ..., 25=Z).
     - Calculate the remainder when divided by 26: `rem = columnNumber % 26`.
     - Convert the remainder to a character: `chr(ord('A') + rem)`.
     - Update `columnNumber` by dividing it by 26: `columnNumber //= 26`.
   - Reverse the collected characters to get the final title.
3. **Complexity**:
   - Time Complexity: O(log26 N) where N is the columnNumber.
   - Space Complexity: O(1) beyond the output string."""
    
    answer = """def convertToTitle(columnNumber: int) -> str:
    res = []
    while columnNumber > 0:
        columnNumber -= 1
        res.append(chr(ord('A') + (columnNumber % 26)))
        columnNumber //= 26
    return "".join(res[::-1])"""

    boilerplate = {
        "python": "import sys\n\ndef convertToTitle(columnNumber):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        print(convertToTitle(int(data)))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\nusing namespace std;\nstring convertToTitle(int columnNumber) {\n    // User logic here\n    return \"\";\n}\nint main() {\n    int columnNumber;\n    if (cin >> columnNumber) {\n        cout << convertToTitle(columnNumber) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static String convertToTitle(int columnNumber) {\n        // User logic here\n        return \"\";\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            System.out.println(convertToTitle(sc.nextInt()));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction convertToTitle(columnNumber) {\n    // User logic here\n    return \"\";\n}\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    console.log(convertToTitle(parseInt(input, 10)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\nchar* convertToTitle(int columnNumber) {\n    // User logic here\n    return NULL;\n}\nint main() {\n    int columnNumber;\n    if (scanf(\"%d\", &columnNumber) == 1) {\n        char* res = convertToTitle(columnNumber);\n        if (res) {\n            printf(\"%s\\n\", res);\n            free(res);\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1", "expected_output": "A", "is_sample": True},
        {"input": "28", "expected_output": "AB", "is_sample": True},
        {"input": "701", "expected_output": "ZY", "is_sample": True},
        {"input": "26", "expected_output": "Z", "is_sample": False},
        {"input": "702", "expected_output": "ZZ", "is_sample": False},
        {"input": "52", "expected_output": "AZ", "is_sample": False},
        {"input": "676", "expected_output": "YZ", "is_sample": False},
        # Stress cases
        {"input": "2147483647", "expected_output": "FXSHRXW", "is_sample": False},
        {"input": "1000", "expected_output": "ALL", "is_sample": False},
        {"input": "18278", "expected_output": "ZZZ", "is_sample": False}
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

    output_path = "1-200/168_Excel_Sheet_Column_Title.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
