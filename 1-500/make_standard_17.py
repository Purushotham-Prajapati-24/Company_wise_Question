import json
import os

def generate_json():
    problem_id = 17
    title = "Letter Combinations of a Phone Number"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>17. Letter Combinations of a Phone Number</h3>
<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent. Return the answer in <strong>any order</strong>.</p>
<p>A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png" style="width: 300px; height: 243px;" />

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> digits = "23"
<strong>Output:</strong> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> digits = ""
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> digits = "2"
<strong>Output:</strong> ["a","b","c"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> is a digit in the range <code>['2', '9']</code>.</li>
</ul>"""

    input_format = "A single string 'digits' representing phone numbers."
    output_format = "A list of strings representing all possible letter combinations."
    
    constraints = [
        "0 <= digits.length <= 4",
        "digits[i] is a digit in the range ['2', '9']"
    ]
    
    explanation = """Use a hash map to store the mapping of digits to letters.
Use backtracking or BFS to generate all combinations.
Iteratively, for each digit, multiply the current combinations with the letters of the current digit."""
    
    answer = """def letterCombinations(digits):
    if not digits: return []
    m = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    res = [""]
    for d in digits:
        res = [p + s for p in res for s in m[d]]
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef letterCombinations(digits):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    digits = data.replace('[','').replace(']','').replace('\"','').replace(\"'\",\"\").split('=')[-1].strip()\n    res = letterCombinations(digits)\n    print(json.dumps(res).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nvector<string> letterCombinations(string digits) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        string digits = \"\";\n        bool start = false;\n        for(char c : line) {\n            if (isdigit(c)) digits += c;\n            else if (c == '\"' || c == '\\'') continue;\n        }\n        // More robust extraction: find first digit-only segment after '=' if exists\n        size_t eq = line.find('=');\n        if (eq != string::npos) {\n            digits = \"\";\n            for(size_t i = eq + 1; i < line.length(); i++) {\n                if(isdigit(line[i])) digits += line[i];\n            }\n        } else {\n            digits = \"\";\n            for(char c : line) if(isdigit(c)) digits += c;\n        }\n        vector<string> res = letterCombinations(digits);\n        cout << \"[\";\n        for (int i = 0; i < res.size(); i++) {\n            cout << \"\\\"\" << res[i] << \"\\\"\";\n            if (i < res.size() - 1) cout << \", \";\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<String> letterCombinations(String digits) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine();\n        String digits = \"\";\n        if (line.contains(\"=\")) line = line.substring(line.indexOf('=') + 1);\n        for (char c : line.toCharArray()) if (Character.isDigit(c)) digits += c;\n        List<String> res = letterCombinations(digits);\n        System.out.print(\"[\");\n        for (int i = 0; i < res.size(); i++) {\n            System.out.print(\"\\\"\" + res.get(i) + \"\\\"\");\n            if (i < res.size() - 1) System.out.print(\", \");\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction letterCombinations(digits) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nlet digits = input;\nif (digits.includes('=')) digits = digits.split('=')[1];\ndigits = digits.replace(/[^0-9]/g, '');\nconst res = letterCombinations(digits);\nprocess.stdout.write(JSON.stringify(res).split(',').join(', ') + '\\n');",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nchar** letterCombinations(char* digits, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char line[1000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char digits[100];\n        int dIdx = 0;\n        char* p = line;\n        if (strchr(line, '=')) p = strchr(line, '=') + 1;\n        while (*p) {\n            if (isdigit(*p)) digits[dIdx++] = *p;\n            p++;\n        }\n        digits[dIdx] = '\\0';\n        int returnSize = 0;\n        char** res = letterCombinations(digits, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"\\\"%s\\\"\", res[i]);\n            if (i < returnSize - 1) printf(\", \");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "\"23\"", "expected_output": "[\"ad\", \"ae\", \"af\", \"bd\", \"be\", \"bf\", \"cd\", \"ce\", \"cf\"]", "is_sample": True},
        {"input": "\"\"", "expected_output": "[]", "is_sample": True},
        {"input": "\"2\"", "expected_output": "[\"a\", \"b\", \"c\"]", "is_sample": True},
        {"input": "234", "expected_output": json.dumps(["adj","adk","adl","aej","aek","ael","afj","afk","afl","bdj","bdk","bdl","bej","bek","bel","bfj","bfk","bfl","cdj","cdk","cdl","cej","cek","cel","cfj","cfk","cfl"]).replace(',', ', '), "is_sample": False},
        {"input": "7", "expected_output": "[\"p\", \"q\", \"r\", \"s\"]", "is_sample": False},
        {"input": "9", "expected_output": "[\"w\", \"x\", \"y\", \"z\"]", "is_sample": False},
        {"input": "22", "expected_output": "[\"aa\", \"ab\", \"ac\", \"ba\", \"bb\", \"bc\", \"ca\", \"cb\", \"cc\"]", "is_sample": False},
        {"input": "78", "expected_output": "[\"pt\", \"pu\", \"pv\", \"qt\", \"qu\", \"qv\", \"rt\", \"ru\", \"rv\", \"st\", \"su\", \"sv\"]", "is_sample": False},
        {"input": "33", "expected_output": "[\"dd\", \"de\", \"df\", \"ed\", \"ee\", \"ef\", \"fd\", \"fe\", \"ff\"]", "is_sample": False},
        {"input": "45", "expected_output": "[\"gj\", \"gk\", \"gl\", \"hj\", \"hk\", \"hl\", \"ij\", \"ik\", \"il\"]", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-200/17_Letter_Combinations_of_a_Phone_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
