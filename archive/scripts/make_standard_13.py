import json
import os

def generate_json():
    problem_id = 13
    title = "Roman to Integer"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>13. Roman to Integer</h3>
<p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<pre>
<strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code>2</code> is written as <code>II</code>&nbsp;in Roman numeral, just two ones added together. <code>12</code> is written as&nbsp;<code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given a roman numeral, convert it to an integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "III"
<strong>Output:</strong> 3
<strong>Explanation:</strong> III = 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "LVIII"
<strong>Output:</strong> 58
<strong>Explanation:</strong> L = 50, V = 5, III = 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "MCMXCIV"
<strong>Output:</strong> 1994
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 15</code></li>
	<li><code>s</code> contains only the characters (<code>'I'</code>, <code>'V'</code>, <code>'X'</code>, <code>'L'</code>, <code>'C'</code>, <code>'D'</code>, <code>'M'</code>).</li>
	<li>It is <strong>guaranteed</strong> that <code>s</code> is a valid roman numeral in the range <code>[1, 3999]</code>.</li>
</ul>
"""

    input_format = "A single line containing the Roman numeral string 's'."
    output_format = "An integer representing the Roman numeral."
    
    constraints = [
        "1 <= s.length <= 15",
        "s contains only characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')",
        "Guaranteed valid Roman numeral in range [1, 3999]."
    ]
    
    explanation = """To convert Roman numerals to an integer:
1. Use a hash map to store the values of Roman symbols (I: 1, V: 5, X: 10, ...).
2. Iterate through the string from left to right.
3. For each character:
   - If the current symbol's value is less than the next symbol's value:
     - Subtract current value from the total (since it acts as a prefix for subtraction, e.g., IV = -1 + 5).
   - Otherwise:
     - Add current value to the total.
4. Return the calculated total.

This approach ensures we correctly handle both simple addition and subtractive forms in O(N) time and O(1) space."""
    
    answer = """def romanToInt(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    return total"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef romanToInt(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        print(romanToInt(data))\n    else:\n        print(0)",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint romanToInt(string s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string s;\n    if (cin >> s) cout << romanToInt(s) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int romanToInt(String s) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            System.out.println(romanToInt(sc.next()));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction romanToInt(s) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    console.log(romanToInt(input));\n}",
        "c": "#include <stdio.h>\n\nint romanToInt(char* s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char s[25];\n    if (scanf(\"%24s\", s) == 1) {\n        printf(\"%d\\n\", romanToInt(s));\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "III", "expected_output": "3", "is_sample": True},
        {"input": "LVIII", "expected_output": "58", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "MCMXCIV", "expected_output": "1994", "is_sample": False},
        {"input": "I", "expected_output": "1", "is_sample": False},
        {"input": "IX", "expected_output": "9", "is_sample": False},
        {"input": "XL", "expected_output": "40", "is_sample": False},
        {"input": "DCXXI", "expected_output": "621", "is_sample": False},
        # Last three: Stress tests
        {"input": "MMMCMXCIX", "expected_output": "3999", "is_sample": False},
        {"input": "MMM", "expected_output": "3000", "is_sample": False},
        {"input": "CDXLIV", "expected_output": "444", "is_sample": False}
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

    output_path = "1-200/13_Roman_to_Integer.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
