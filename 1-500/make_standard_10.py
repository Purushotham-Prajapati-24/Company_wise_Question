import json
import os

def generate_json():
    problem_id = 10
    title = "Regular Expression Matching"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>10. Regular Expression Matching</h3>
<p>Given an input string <code>s</code> and a pattern <code>p</code>, implement regular expression matching with support for <code>'.'</code> and <code>'*'</code> where:</p>

<ul>
	<li><code>'.'</code> Matches any single character.</li>
	<li><code>'*'</code> Matches zero or more of the preceding element.</li>
</ul>

<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "aa", p = "a"
<strong>Output:</strong> false
<strong>Explanation:</strong> "a" does not match the entire string "aa".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "aa", p = "a*"
<strong>Output:</strong> true
<strong>Explanation:</strong> '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "ab", p = ".*"
<strong>Output:</strong> true
<strong>Explanation:</strong> ".*" means "zero or more (*) of any character (.)".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>1 &lt;= p.length &lt;= 20</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
	<li><code>p</code> contains only lowercase English letters, <code>'.'</code>, and <code>'*'</code>.</li>
	<li>It is guaranteed for each appearance of the character <code>'*'</code>, there will be a previous valid character to match.</li>
</ul>
"""

    input_format = "Line 1: String 's'.\nLine 2: Pattern 'p'."
    output_format = "true or false."
    
    constraints = [
        "1 <= s.length <= 20",
        "1 <= p.length <= 20",
        "s contains only lowercase English letters",
        "p contains only lowercase letters, '.', and '*'",
        "Each '*' has a preceding valid character."
    ]
    
    explanation = """To implement Regular Expression Matching with '.' and '*':
1. Use Dynamic Programming (Top-Down or Bottom-Up) to avoid redundant computations.
2. Define dp(i, j) as whether s[i:] matches p[j:].
3. Base Case: If j is the length of p, return True if i is the length of s, else False.
4. For each state (i, j):
   - Check if the first characters match: first_match = (i < len(s) and p[j] in {s[i], '.'}).
   - If the next character in p (j + 1) is '*':
     - Case 1 (Match zero): dp(i, j + 2).
     - Case 2 (Match one or more): first_match and dp(i + 1, j).
   - If the next character is not '*':
     - first_match and dp(i + 1, j + 1).
5. Memoize results to achieve O(M*N) time and space complexity."""
    
    answer = """def isMatch(s, p):
    memo = {}
    def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if j == len(p): return i == len(s)
        
        first_match = i < len(s) and p[j] in [s[i], '.']
        
        if j + 1 < len(p) and p[j+1] == '*':
            ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
        else:
            ans = first_match and dp(i + 1, j + 1)
            
        memo[(i, j)] = ans
        return ans
    return dp(0, 0)"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef isMatch(s: str, p: str) -> bool:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().splitlines()\n    if len(data) >= 2:\n        def clean(x):\n            x = x.strip()\n            if (x.startswith('\"') and x.endswith('\"')) or (x.startswith(\"'\") and x.endswith(\"'\")):\n                x = x[1:-1]\n            return x\n        s = clean(data[0])\n        p = clean(data[1])\n        print(str(isMatch(s, p)).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nbool isMatch(string s, string p) {\n    // User logic here\n    return false;\n}\n\nstring clean(string x) {\n    x.erase(0, x.find_first_not_of(\" \\t\\n\\r\"));\n    x.erase(x.find_last_not_of(\" \\t\\n\\r\") + 1);\n    if (x.size() >= 2 && ((x.front() == '\"' && x.back() == '\"') || (x.front() == '\\'' && x.back() == '\\''))) {\n        x = x.substr(1, x.size() - 2);\n    }\n    return x;\n}\n\nint main() {\n    string s, p;\n    if (getline(cin, s) && getline(cin, p)) {\n        cout << (isMatch(clean(s), clean(p)) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isMatch(String s, String p) {\n        // User logic here\n        return false;\n    }\n\n    private static String clean(String x) {\n        x = x.trim();\n        if (x.length() >= 2 && ((x.startsWith(\"\\\"\") && x.endsWith(\"\\\"\")) || (x.startsWith(\"'\") && x.endsWith(\"'\")))) {\n            x = x.substring(1, x.length() - 1);\n        }\n        return x;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine();\n            if (sc.hasNextLine()) {\n                String p = sc.nextLine();\n                System.out.println(isMatch(clean(s), clean(p)) ? \"true\" : \"false\");\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isMatch(s, p) {\n    // User logic here\n    return false;\n}\n\nfunction clean(x) {\n    x = x.trim();\n    if ((x.startsWith('\"') && x.endsWith('\"')) || (x.startsWith(\"'\") && x.endsWith(\"'\"))) {\n        x = x.substring(1, x.length - 1);\n    }\n    return x;\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    console.log(isMatch(clean(input[0]), clean(input[1])) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <ctype.h>\n#include <stdbool.h>\n\nbool isMatch(char* s, char* p) {\n    // User logic here\n    return false;\n}\n\nchar* clean(char* x) {\n    while(isspace(*x)) x++;\n    int len = strlen(x);\n    while(len > 0 && isspace(x[len-1])) { x[len-1] = 0; len--; }\n    if (len >= 2 && ((x[0] == '\"' && x[len-1] == '\"') || (x[0] == '\\'' && x[len-1] == '\\''))) {\n        x[len-1] = 0;\n        x++;\n    }\n    return x;\n}\n\nint main() {\n    char s[2000], p[2000];\n    if (fgets(s, sizeof(s), stdin) && fgets(p, sizeof(p), stdin)) {\n        s[strcspn(s, \"\\r\\n\")] = 0;\n        p[strcspn(p, \"\\r\\n\")] = 0;\n        printf(\"%s\\n\", isMatch(clean(s), clean(p)) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "aa\na", "expected_output": "false", "is_sample": True},
        {"input": "aa\na*", "expected_output": "true", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "ab\n.*", "expected_output": "true", "is_sample": False},
        {"input": "aab\nc*a*b", "expected_output": "true", "is_sample": False},
        {"input": "mississippi\nmis*is*p*.", "expected_output": "false", "is_sample": False},
        {"input": "aaa\na*a", "expected_output": "true", "is_sample": False},
        {"input": "aaa\nab*a*c*a", "expected_output": "true", "is_sample": False},
        # Last three: Stress tests
        {"input": "aaaaaaaaaaaaaaaaaaaa\na*a*a*a*a*a*a*a*a*a*", "expected_output": "true", "is_sample": False},
        {"input": "aaaaaaaaaaaaaaaaaaab\na*a*a*a*a*a*a*a*a*a*", "expected_output": "false", "is_sample": False},
        {"input": "a\n.*.*.*.*.*.*.*.*.*.*", "expected_output": "true", "is_sample": False}
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
        "topics": ["String", "Dynamic Programming", "Recursion"],
        "companyIndex": 0
    }

    output_path = "1-200/10_Regular_Expression_Matching.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
