import json
import os

def generate_json():
    problem_id = 246
    title = "Strobogrammatic Number"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>246. Strobogrammatic Number</h3>
<p>Given a string <code>num</code> which represents an integer, return <code>true</code> <em>if</em> <code>num</code> <em>is a <strong>strobogrammatic number</strong></em>.</p>

<p>A <strong>strobogrammatic number</strong> is a number that looks the same when rotated 180 degrees (looked at upside down).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = "69"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = "88"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> num = "962"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 50</code></li>
	<li><code>num</code> consists of only digits.</li>
	<li><code>num</code> does not contain any leading zeros except for zero itself.</li>
</ul>"""

    input_format = "A single string num."
    output_format = "A boolean (true/false)."
    
    constraints = [
        "1 <= count of digits <= 50",
        "num only contains digits.",
        "Must look the same after 180-degree rotation."
    ]
    
    explanation = """To check if a number is strobogrammatic:
1. **Valid Rotations**: In standard digital fonts, digits that can be rotated 180° and remain digits are:
   - `0 -> 0`, `1 -> 1`, `8 -> 8` (identity)
   - `6 -> 9`, `9 -> 6` (inversions)
   - Other digits (`2, 3, 4, 5, 7`) become invalid.
2. **Two Pointers**: Compare digits from beginning and end towards the middle.
3. **Check**:
   - For each pair `(left, right)`, they must belong to the valid rotation set: `{"00", "11", "88", "69", "96"}`.
4. **Complexity**: O(N) where N is string length."""
    
    answer = """class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strob_map = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in strob_map or strob_map[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef isStrobogrammatic(num: str) -> bool:\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Find a sequence of digits, potentially in quotes\n    match = re.search(r'\"?(\\d+)\"?', raw_input)\n    if match:\n        print(\"true\" if isStrobogrammatic(match.group(1)) else \"false\")",
        "cpp": "#include <iostream>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nbool isStrobogrammatic(string num) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    regex re_num(r'\"?(\\d+)\"?');\n    smatch m;\n    if (regex_search(input, m, re_num)) {\n        cout << (isStrobogrammatic(m[1].str()) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public boolean isStrobogrammatic(String num) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        Pattern p = Pattern.compile(\"\\\"?(\\\\d+)\\\"?\");\n        Matcher m = p.matcher(input);\n        if (m.find()) {\n            System.out.println(new Solution().isStrobogrammatic(m.group(1)) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isStrobogrammatic(num) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst match = input.match(/\"?(\\d+)\"?/);\nif (match) {\n    console.log(isStrobogrammatic(match[1]) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n#include <ctype.h>\n\nbool isStrobogrammatic(char* num) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    static char buffer[1000];\n    int bytes = fread(buffer, 1, sizeof(buffer)-1, stdin);\n    buffer[bytes] = '\\0';\n    \n    char* p = buffer;\n    while (*p && !isdigit(*p)) p++;\n    if (*p) {\n        char* start = p;\n        while (*p && isdigit(*p)) p++;\n        *p = '\\0';\n        printf(\"%s\\n\", isStrobogrammatic(start) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "69", "expected_output": "true", "is_sample": True},
        {"input": "88", "expected_output": "true", "is_sample": True},
        {"input": "962", "expected_output": "false", "is_sample": False},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "0", "expected_output": "true", "is_sample": False},
        {"input": "818", "expected_output": "true", "is_sample": False},
        {"input": "609", "expected_output": "true", "is_sample": False},
        {"input": "1" + "0"*48 + "1", "expected_output": "true", "is_sample": False},
        {"input": "6" + "8"*48 + "9", "expected_output": "true", "is_sample": False},
        {"input": "8" * 50, "expected_output": "true", "is_sample": False}
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
        "topics": ["Two Pointers", "String"],
        "companyIndex": 0
    }

    output_path = "201-400/246_Strobogrammatic_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
