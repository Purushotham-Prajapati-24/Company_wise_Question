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
</ul>
"""

    input_format = "A single string containing digits 'digits'."
    output_format = "A string representing a list of all possible letter combinations."
    
    constraints = [
        "0 <= digits.length <= 4",
        "digits[i] is in the range ['2', '9']"
    ]
    
    explanation = """To find all letter combinations of a phone number:
1. Define a mapping (hash map) from each digit '2'-'9' to its corresponding letters.
2. If the input `digits` is empty, return an empty list.
3. Use a recursive backtracking approach or a simple iterative loop (using a queue or list comprehension) to build combinations.
4. For each digit in `digits`:
   - Take the current set of combinations and append each letter from the current digit to every combination in the set.
5. Return the final list of combinations.

Time Complexity: O(4^N * N), where N is the length of digits and 4 is the maximum number of letters per digit.
Space Complexity: O(4^N) for the resulting combinations."""
    
    answer = """def letterCombinations(digits):
    if not digits:
        return []
    phone = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    res = [""]
    for d in digits:
        temp = []
        for combination in res:
            for letter in phone[d]:
                temp.append(combination + letter)
        res = temp
    return res"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport json\n\ndef letterCombinations(digits):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    res = letterCombinations(data)\n    print(json.dumps(res).replace(',', ', '))\n",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nvector<string> letterCombinations(string digits) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string digits;\n    if (cin >> digits) {\n        vector<string> res = letterCombinations(digits);\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); i++) {\n            cout << \"\\\"\" << res[i] << \"\\\"\";\n            if (i < res.size() - 1) cout << \", \";\n        }\n        cout << \"]\" << endl;\n    } else {\n        cout << \"[]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<String> letterCombinations(String digits) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            List<String> res = letterCombinations(sc.next());\n            System.out.print(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                System.out.print(\"\\\"\" + res.get(i) + \"\\\"\");\n                if (i < res.size() - 1) System.out.print(\", \");\n            }\n            System.out.println(\"]\");\n        } else {\n            System.out.println(\"[]\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction letterCombinations(digits) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    const res = letterCombinations(input);\n    console.log(JSON.stringify(res).replace(/,/g, \", \"));\n} else {\n    console.log(\"[]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar** letterCombinations(char* digits, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char digits[25];\n    if (scanf(\"%24s\", digits) == 1) {\n        int returnSize;\n        char** res = letterCombinations(digits, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"\\\"%s\\\"\", res[i]);\n            if (i < returnSize - 1) printf(\", \");\n        }\n        printf(\"]\\n\");\n    } else {\n        printf(\"[]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "23", "expected_output": "[\"ad\", \"ae\", \"af\", \"bd\", \"be\", \"bf\", \"cd\", \"ce\", \"cf\"]", "is_sample": True},
        {"input": "", "expected_output": "[]", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "2", "expected_output": "[\"a\", \"b\", \"c\"]", "is_sample": False},
        {"input": "7", "expected_output": "[\"p\", \"q\", \"r\", \"s\"]", "is_sample": False},
        {"input": "22", "expected_output": "[\"aa\", \"ab\", \"ac\", \"ba\", \"bb\", \"bc\", \"ca\", \"cb\", \"cc\"]", "is_sample": False},
        {"input": "99", "expected_output": "[\"ww\", \"wx\", \"wy\", \"wz\", \"xw\", \"xx\", \"xy\", \"xz\", \"yw\", \"yx\", \"yy\", \"yz\", \"zw\", \"zx\", \"zy\", \"zz\"]", "is_sample": False},
        {"input": "1", "expected_output": "[]", "is_sample": False}, # Note constraint says 2-9 but let's be safe
        # Last three: Stress tests
        {"input": "2345", "expected_output": str(letterCombinations("2345") if 'letterCombinations' in locals() else ""), "is_sample": False},
        {"input": "789", "expected_output": str(letterCombinations("789") if 'letterCombinations' in locals() else ""), "is_sample": False},
        {"input": "9999", "expected_output": str(letterCombinations("9999") if 'letterCombinations' in locals() else ""), "is_sample": False}
    ]
    # Update stress outputs
    def _lc_ref(digits):
        if not digits: return []
        phone = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = [""]
        for d in digits:
            if d not in phone: return []
            res = [c + l for c in res for l in phone[d]]
        return res

    test_cases[7]["expected_output"] = json.dumps(_lc_ref("2345"))
    test_cases[8]["expected_output"] = json.dumps(_lc_ref("789"))
    test_cases[9]["expected_output"] = json.dumps(_lc_ref("9999"))

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
