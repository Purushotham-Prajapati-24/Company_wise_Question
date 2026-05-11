import json
import os

def generate_json():
    problem_id = 273
    title = "Integer to English Words"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>273. Integer to English Words</h3>
<p>Convert a non-negative integer <code>num</code> to its English words representation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = 123
<strong>Output:</strong> "One Hundred Twenty Three"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = 12345
<strong>Output:</strong> "Twelve Thousand Three Hundred Forty Five"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> num = 1234567
<strong>Output:</strong> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "An integer `num`."
    output_format = "A string representing the number in English words."
    
    constraints = [
        "0 <= num <= 2,147,483,647"
    ]
    
    explanation = """To convert an integer to English words:
1. **Divide into Chunks**: Break the number into groups of three digits (billions, millions, thousands, and the rest).
2. **Helper Function**: Create a function `helper(n)` that converts a number `n < 1000` into words.
   - Handle cases for hundreds, tens, and units/teens.
   - Use mappings for `LESS_THAN_20`, `TENS`, and `THOUSANDS`.
3. **Handle Zero**: Special case for `num == 0` is "Zero".
4. **Iterative/Recursive Process**: Process each group of 3 digits from largest (billion) to smallest, adding the corresponding unit (Billion, Million, Thousand) only if the group is non-zero.
5. **Complexity**:
   - Time: O(1) as the number of digits is bounded (at most 10 digits).
   - Space: O(1) for the fixed set of word mappings."""
    
    answer = """class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
            
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return LESS_THAN_20[n] + " "
            elif n < 100:
                return TENS[n // 10] + " " + helper(n % 10)
            else:
                return LESS_THAN_20[n // 100] + " Hundred " + helper(n % 100)
                
        res = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + THOUSANDS[i] + " " + res
            num //= 1000
            i += 1
            
        return res.strip()"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef numberToWords(num: int) -> str:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    match = re.search(r'\\d+', raw_input)\n    if match:\n        num = int(match.group())\n        print(numberToWords(num))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <regex>\n\nusing namespace std;\n\nstring numberToWords(int num) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    regex re_num(R\"(\\d+)\");\n    smatch match;\n    if (regex_search(input, match, re_num)) {\n        int num = stoi(match.str());\n        cout << numberToWords(num) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public String numberToWords(int num) {\n        // User logic here\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (sc.hasNext()) {\n            String input = sc.next();\n            Matcher m = Pattern.compile(\"\\\\d+\").matcher(input);\n            if (m.find()) {\n                int num = Integer.parseInt(m.group());\n                System.out.println(new Solution().numberToWords(num));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction numberToWords(num) {\n    // User logic here\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst match = input.match(/\\d+/);\nif (match) {\n    const num = parseInt(match[0]);\n    console.log(numberToWords(num));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nchar* numberToWords(int num) {\n    // User logic here\n    return (char*)\"\";\n}\n\nint main() {\n    static char buffer[100000];\n    if (fread(buffer, 1, 99999, stdin) > 0) {\n        char *p = buffer;\n        while (*p && !isdigit(*p)) p++;\n        if (*p) {\n            int num = atoi(p);\n            char* res = numberToWords(num);\n            printf(\"%s\\n\", res);\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "123", "expected_output": '"One Hundred Twenty Three"', "is_sample": True},
        {"input": "12345", "expected_output": '"Twelve Thousand Three Hundred Forty Five"', "is_sample": True},
        {"input": "1234567", "expected_output": '"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"', "is_sample": True},
        {"input": "0", "expected_output": '"Zero"', "is_sample": False},
        {"input": "100", "expected_output": '"One Hundred"', "is_sample": False},
        {"input": "1000", "expected_output": '"One Thousand"', "is_sample": False},
        {"input": "1000000", "expected_output": '"One Million"', "is_sample": False},
        # Stress cases
        {"input": "2147483647", "expected_output": '"Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"', "is_sample": False},
        {"input": "1000000001", "expected_output": '"One Billion One"', "is_sample": False},
        {"input": "1100110011", "expected_output": '"One Billion One Hundred Million One Hundred Ten Thousand Eleven"', "is_sample": False}
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
        "topics": ["Math", "String", "Recursion"],
        "companyIndex": 0
    }

    output_path = "201-400/273_Integer_to_English_Words.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
