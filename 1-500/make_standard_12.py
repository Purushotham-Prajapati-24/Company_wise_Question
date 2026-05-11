import json
import os

def generate_json():
    problem_id = 12
    title = "Integer to Roman"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>12. Integer to Roman</h3>
<p>Seven different symbols represent Roman numerals:</p>

<table class="table" style="width: 200px;">
	<thead>
		<tr>
			<th>Symbol</th>
			<th>Value</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>I</td>
			<td>1</td>
		</tr>
		<tr>
			<td>V</td>
			<td>5</td>
		</tr>
		<tr>
			<td>X</td>
			<td>10</td>
		</tr>
		<tr>
			<td>L</td>
			<td>50</td>
		</tr>
		<tr>
			<td>C</td>
			<td>100</td>
		</tr>
		<tr>
			<td>D</td>
			<td>500</td>
		</tr>
		<tr>
			<td>M</td>
			<td>1000</td>
		</tr>
	</tbody>
</table>

<p>Given an integer, convert it to a Roman numeral.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> num = 3749
<strong>Output:</strong> "MMMDCCXLIX"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> num = 58
<strong>Output:</strong> "LVIII"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> num = 1994
<strong>Output:</strong> "MCMXCIV"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= num &lt;= 3999</code></li>
</ul>
"""

    input_format = "A single integer 'num'."
    output_format = "A string representing the Roman numeral."
    
    constraints = [
        "1 <= num <= 3999"
    ]
    
    explanation = """To convert an integer to Roman numerals:
1. Define a list of tuples containing Roman symbols and their corresponding values in descending order.
2. Include both standard symbols (M: 1000, D: 500, etc.) and subtractive cases (CM: 900, CD: 400, XC: 90, XL: 40, IX: 9, IV: 4).
3. Iterate through the mapping and append symbols while subtracting values."""
    
    answer = """def intToRoman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    for i in range(len(val)):
        while num >= val[i]:
            res += syb[i]
            num -= val[i]
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef intToRoman(num):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        num = int(line.replace('[','').replace(']','').split('=')[-1].strip())\n        print(intToRoman(num))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nstring intToRoman(int num) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    string s;\n    if (cin >> s) {\n        // Strip non-digits\n        string clean = \"\";\n        for(char c : s) if(isdigit(c)) clean += c;\n        if(!clean.empty()) cout << intToRoman(stoi(clean)) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static String intToRoman(int num) {\n        // User logic\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[^0-9]\", \"\");\n            if(!s.isEmpty()) System.out.println(intToRoman(Integer.parseInt(s)));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction intToRoman(num) {\n    // User logic\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    const clean = input.replace(/[^0-9]/g, '');\n    if(clean) console.log(intToRoman(parseInt(clean, 10)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nchar* intToRoman(int num) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    char buf[100];\n    if (scanf(\"%s\", buf) == 1) {\n        char* p = buf;\n        while(*p && !isdigit(*p)) p++;\n        if(*p) printf(\"%s\\n\", intToRoman(atoi(p)));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3749", "expected_output": "MMMDCCXLIX", "is_sample": True},
        {"input": "58", "expected_output": "LVIII", "is_sample": True},
        {"input": "1994", "expected_output": "MCMXCIV", "is_sample": False},
        {"input": "1", "expected_output": "I", "is_sample": False},
        {"input": "4", "expected_output": "IV", "is_sample": False},
        {"input": "9", "expected_output": "IX", "is_sample": False},
        {"input": "40", "expected_output": "XL", "is_sample": False},
        {"input": "3999", "expected_output": "MMMCMXCIX", "is_sample": False},
        {"input": "900", "expected_output": "CM", "is_sample": False},
        {"input": "444", "expected_output": "CDXLIV", "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
        "question_title": title,
        "difficulty": difficulty,
        "marks": marks,
        "question_text": html_description,
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
        "topics": ["Hash Table", "Math", "String"],
        "companyIndex": 0
    }

    output_path = "1-200/12_Integer_to_Roman.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
