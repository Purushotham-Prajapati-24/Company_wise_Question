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

<p>Given a roman numeral, convert it to an integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "III"
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "LVIII"
<strong>Output:</strong> 58
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "MCMXCIV"
<strong>Output:</strong> 1994
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
2. Iterate through the string.
3. If a symbol's value is less than the next one, subtract it; otherwise, add it."""
    
    answer = """def romanToInt(s):
    m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
    return ans"""

    boilerplate = {
        "python": "import sys\n\ndef romanToInt(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        # Lethal parsing: strip quotes, brackets, and prefix like 's = '\n        s = line.replace('[','').replace(']','').replace('\"','').replace(\"'\",\"\").split('=')[-1].strip()\n        print(romanToInt(s))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nint romanToInt(string s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string s;\n    if (cin >> s) {\n        // Lethal parsing: remove quotes and brackets\n        string clean = \"\";\n        for(char c : s) if(c != '[' && c != ']' && c != '\"' && c != '\\'') clean += c;\n        // If input was 's=III', split by '='\n        size_t pos = clean.find('=');\n        if(pos != string::npos) clean = clean.substr(pos+1);\n        cout << romanToInt(clean) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int romanToInt(String s) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[\\\\[\\\\]\\\"']\", \"\");\n            if(s.contains(\"=\")) s = s.substring(s.indexOf(\"=\") + 1);\n            System.out.println(romanToInt(s));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction romanToInt(s) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    let s = input.replace(/[\\\\[\\\\]\\\"']/g, '');\n    if(s.includes('=')) s = s.split('=')[1].trim();\n    console.log(romanToInt(s));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n\nint romanToInt(char* s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char buf[100];\n    if (scanf(\"%s\", buf) == 1) {\n        char* p = buf;\n        if(strchr(p, '=')) p = strchr(p, '=') + 1;\n        // Simple check to skip leading quote if any\n        if(*p == '\"' || *p == '\\'') p++;\n        // Remove trailing quote if any\n        int len = strlen(p);\n        if(len > 0 && (p[len-1] == '\"' || p[len-1] == '\\'')) p[len-1] = '\\0';\n        printf(\"%d\\n\", romanToInt(p));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "III", "expected_output": "3", "is_sample": True},
        {"input": "LVIII", "expected_output": "58", "is_sample": True},
        {"input": "MCMXCIV", "expected_output": "1994", "is_sample": False},
        {"input": "I", "expected_output": "1", "is_sample": False},
        {"input": "IX", "expected_output": "9", "is_sample": False},
        {"input": "XL", "expected_output": "40", "is_sample": False},
        {"input": "DCXXI", "expected_output": "621", "is_sample": False},
        {"input": "MMMCMXCIX", "expected_output": "3999", "is_sample": False},
        {"input": "MMM", "expected_output": "3000", "is_sample": False},
        {"input": "CDXLIV", "expected_output": "444", "is_sample": False}
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

    output_path = "1-200/13_Roman_to_Integer.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
