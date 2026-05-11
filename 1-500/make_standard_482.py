import json
import os

def generate_json():
    problem_id = 482
    title = "License Key Formatting"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>482. License Key Formatting</h3>
<p>You are given a license key represented as a string <code>s</code> that consists of only alphanumeric characters and dashes. The string is separated into <code>n + 1</code> groups by <code>n</code> dashes. You are also given an integer <code>k</code>.</p>

<p>We want to reformat the string <code>s</code> such that each group contains exactly <code>k</code> characters, except for the first group, which could be shorter than <code>k</code> but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.</p>

<p>Return <em>the reformatted license key</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "5F3Z-2e-9-w", k = 4
<strong>Output:</strong> "5F3Z-2E9W"
<strong>Explanation:</strong> The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "2-5g-3-J", k = 2
<strong>Output:</strong> "2-5G-3J"
<strong>Explanation:</strong> The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of English letters, digits, and dashes <code>'-'</code>.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Line 1: A string `s` representing the license key.\\nLine 2: An integer `k`."
    output_format = "A string representing the reformatted license key."
    
    constraints = [
        "1 <= s.length <= 10^5",
        "s consists of alphanumeric characters and dashes.",
        "1 <= k <= 10^4"
    ]
    
    explanation = "First, remove all dashes from the string and convert all characters to uppercase. Then, calculate the length of the new string. The first group will have `len % k` characters. The rest of the string is divided into groups of `k` characters separated by dashes."
    
    answer = """class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        n = len(s)
        if n == 0: return ""
        first_group_len = n % k if n % k != 0 else k
        res = [s[:first_group_len]]
        for i in range(first_group_len, n, k):
            res.append(s[i:i+k])
        return "-".join(res)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def licenseKeyFormatting(self, s: str, k: int) -> str:\n        # User logic here\n        return \"\"\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().strip().splitlines()\n    if len(lines) >= 2:\n        s = lines[0].strip()\n        if (s.startswith('\"') and s.endswith('\"')) or (s.startswith(\"'\") and s.endswith(\"'\")):\n            s = s[1:-1]\n        k = int(lines[1].strip())\n        sol = Solution()\n        print(json.dumps(sol.licenseKeyFormatting(s, k)))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    string licenseKeyFormatting(string s, int k) {\n        // User logic here\n        return \"\";\n    }\n};\n\nint main() {\n    string s; if (getline(cin, s)) {\n        if (!s.empty() && (s.front() == '\"' || s.front() == '\\'')) s = s.substr(1, s.size() - 2);\n        int k; if (cin >> k) {\n            Solution sol; string res = sol.licenseKeyFormatting(s, k);\n            cout << \"\\\"\" << res << \"\\\"\" << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public String licenseKeyFormatting(String s, int k) {\n        // User logic here\n        return \"\";\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine().trim();\n            if (s.startsWith(\"\\\"\") && s.endsWith(\"\\\"\")) s = s.substring(1, s.length() - 1);\n            if (sc.hasNextInt()) {\n                int k = sc.nextInt();\n                System.out.println(\"\\\"\" + new Solution().licenseKeyFormatting(s, k) + \"\\\"\");\n            }\n        }\n    }\n}",
        "javascript": "/**\n * @param {string} s\n * @param {number} k\n * @return {string}\n */\nvar licenseKeyFormatting = function(s, k) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim().split('\\n');\nif (input.length >= 2) {\n    let s = input[0].trim();\n    if ((s.startsWith('\"') && s.endsWith('\"')) || (s.startsWith(\"'\") && s.endsWith(\"'\"))) s = s.slice(1, -1);\n    const k = parseInt(input[1].trim());\n    console.log(JSON.stringify(licenseKeyFormatting(s, k)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* licenseKeyFormatting(char* s, int k) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    printf(\"\\\"\\\"\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "5F3Z-2e-9-w\n4", "expected_output": "\"5F3Z-2E9W\"", "is_sample": True},
        {"input": "2-5g-3-J\n2", "expected_output": "\"2-5G-3J\"", "is_sample": True},
        {"input": "a-a-a-a\n1", "expected_output": "\"A-A-A-A\"", "is_sample": False},
        {"input": "a-a-a-a\n2", "expected_output": "\"AA-AA\"", "is_sample": False},
        {"input": "---abca--\n2", "expected_output": "\"AB-CA\"", "is_sample": False},
        {"input": "abc\n4", "expected_output": "\"ABC\"", "is_sample": False},
        {"input": "  1-a-b-c  \n1", "expected_output": "\"1-A-B-C\"", "is_sample": False},
        {"input": "---\n1", "expected_output": "\"\"", "is_sample": False},
        {"input": "a\n2", "expected_output": "\"A\"", "is_sample": False},
        {"input": "aaaa-bbbb\n4", "expected_output": "\"AAAA-BBBB\"", "is_sample": False}
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
        "topics": ["String"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_License_Key_Formatting.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
