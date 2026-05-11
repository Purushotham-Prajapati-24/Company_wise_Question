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

<p>Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:</p>

<ul>
	<li>If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.</li>
	<li>If the value starts with 4 or 9, use the <strong>subtractive form</strong>, which involves subtracting one symbol from the next symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).</li>
	<li>Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the <strong>subtractive form</strong>.</li>
</ul>

<p>Given an integer, convert it to a Roman numeral.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 3749</span></p>

<p><strong>Output:</strong> <span class="example-io">"MMMDCCXLIX"</span></p>

<p><strong>Explanation:</strong></p>

<pre>
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal place values
</pre>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 58</span></p>

<p><strong>Output:</strong> <span class="example-io">"LVIII"</span></p>

<p><strong>Explanation:</strong></p>

<pre>
50 = L
 8 = VIII
</pre>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 1994</span></p>

<p><strong>Output:</strong> <span class="example-io">"MCMXCIV"</span></p>

<p><strong>Explanation:</strong></p>

<pre>
1000 = M
 900 = CM
  90 = XC
   4 = IV
</pre>
</div>

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
    
    explanation = """To convert an integer to dynamic Roman numerals:
1. Define a list of tuples containing Roman symbols and their corresponding values in descending order.
2. Include both standard symbols (M: 1000, D: 500, etc.) and subtractive cases (CM: 900, CD: 400, XC: 90, XL: 40, IX: 9, IV: 4).
3. Initialize an empty resulting string.
4. Iterate through the mapping:
   - While the current value can be subtracted from 'num':
     - Append the symbol to the result.
     - Subtract the value from 'num'.
5. Return the resulting string.

Time Complexity: O(1) as the number of Roman numerals is finite (max num is 3999).
Space Complexity: O(1)."""
    
    answer = """def intToRoman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef intToRoman(num):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        print(intToRoman(int(data)))\n    else:\n        print(\"\")",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nstring intToRoman(int num) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    int num;\n    if (cin >> num) cout << intToRoman(num) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static String intToRoman(int num) {\n        // User logic\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            System.out.println(intToRoman(sc.nextInt()));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction intToRoman(num) {\n    // User logic\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    console.log(intToRoman(parseInt(input, 10)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nchar* intToRoman(int num) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    int num;\n    if (scanf(\"%d\", &num) == 1) {\n        char *res = intToRoman(num);\n        printf(\"%s\\n\", res ? res : \"\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "3749", "expected_output": "MMMDCCXLIX", "is_sample": True},
        {"input": "58", "expected_output": "LVIII", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1994", "expected_output": "MCMXCIV", "is_sample": False},
        {"input": "1", "expected_output": "I", "is_sample": False},
        {"input": "4", "expected_output": "IV", "is_sample": False},
        {"input": "9", "expected_output": "IX", "is_sample": False},
        {"input": "40", "expected_output": "XL", "is_sample": False},
        # Last three: Stress tests
        {"input": "3999", "expected_output": "MMMCMXCIX", "is_sample": False},
        {"input": "900", "expected_output": "CM", "is_sample": False},
        {"input": "444", "expected_output": "CDXLIV", "is_sample": False}
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
