import json
import os

def generate_json():
    problem_id = 44
    title = "Wildcard Matching"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>44. Wildcard Matching</h3>
<p>Given an input string (<code>s</code>) and a pattern (<code>p</code>), implement wildcard pattern matching with support for <code>'?'</code> and <code>'*'</code> where:</p>

<ul>
	<li><code>'?'</code> Matches any single character.</li>
	<li><code>'*'</code> Matches any sequence of characters (including the empty sequence).</li>
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
<strong>Input:</strong> s = "aa", p = "*"
<strong>Output:</strong> true
<strong>Explanation:</strong> "*" matches any sequence.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "cb", p = "?a"
<strong>Output:</strong> false
<strong>Explanation:</strong> '?' matches 'c', but the second letter is 'a', which does not match 'b'.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length, p.length &lt;= 2000</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
	<li><code>p</code> contains only lowercase English letters, <code>'?'</code> or <code>'*'</code>.</li>
</ul>"""

    input_format = "A single line containing the string 's' and the pattern 'p' separated by a space. If 's' is an empty string, the line starts with a space."
    output_format = "A string 'true' or 'false' indicating whether 's' matches the pattern 'p'."
    
    constraints = [
        "0 <= s.length, p.length <= 2000",
        "s contains only lowercase English letters.",
        "p contains lowercase English letters, '?' or '*'"
    ]
    
    explanation = """To implement wildcard pattern matching with '?' and '*':
1. A greedy approach with two pointers and backtracking is more efficient than standard Dynamic Programming.
2. Initialize pointers `si` (for string `s`) and `pi` (for pattern `p`) at 0.
3. Keep track of the most recent '*' seen in the pattern (`star_idx`) and the position in the string when we decided to try matching '*' with an empty sequence (`s_tmp_idx`).
4. While `si < len(s)`:
   - Match: If `p[pi]` matches `s[si]` (exact match or `?`), increment both.
   - New Star: If `p[pi] == '*'`, record the star's index and the current string index as a backup, then increment `pi`.
   - Backtrack: If it's a mismatch but a star was seen previously, reset the pattern pointer `pi` to just after the star, increment the backup `s_tmp_idx` (letting the star match one more character), and set `si` to this new backup index.
   - Mismatch: If no star was seen, return `false`.
5. After matching the entire string, ensure any remaining characters in the pattern are also '*':
   - If a non-'*' character remains in the pattern, the match fails.
6. Return `true` if `pi` reaches the end of the pattern.

Time Complexity: O(N * M) in the worst case (e.g., matching 'aaaaaaaaaa' with '*aaaaa'), but O(N) on average for most practical patterns.
Space Complexity: O(1) as we only use pointers and integer variables."""
    
    answer = """def isMatch(s, p):
    si, pi = 0, 0
    star_idx, s_tmp_idx = -1, -1
    
    while si < len(s):
        # Match case
        if pi < len(p) and (p[pi] == '?' or p[pi] == s[si]):
            si += 1
            pi += 1
        # Star case
        elif pi < len(p) and p[pi] == '*':
            star_idx = pi
            s_tmp_idx = si
            pi += 1
        # Backtrack case
        elif star_idx != -1:
            pi = star_idx + 1
            s_tmp_idx += 1
            si = s_tmp_idx
        # No match possible
        else:
            return False
            
    # Check remaining pattern
    while pi < len(p) and p[pi] == '*':
        pi += 1
        
    return pi == len(p)"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef isMatch(s, p):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip().split()\n    if not data:\n        print(\"true\" if isMatch(\"\", \"\") else \"false\")\n    elif len(data) == 1:\n        # Handle case where one is empty\n        pass \n    else:\n        s, p = data[0], data[1]\n        print(str(isMatch(s, p)).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n\nusing namespace std;\n\nbool isMatch(string s, string p) {\n    // User logic\n    return true;\n}\n\nint main() {\n    string s, p;\n    if (cin >> s >> p) {\n        cout << (isMatch(s, p) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isMatch(String s, String p) {\n        // User logic\n        return true;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String s = sc.next();\n            String p = sc.hasNext() ? sc.next() : \"\";\n            System.out.println(isMatch(s, p));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isMatch(s, p) {\n    // User logic\n    return true;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nif (input.length >= 2) {\n    console.log(isMatch(input[0], input[1]));\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\nbool isMatch(char* s, char* p) {\n    // User logic\n    return true;\n}\n\nint main() {\n    char s[2001], p[2001];\n    if (scanf(\"%s %s\", s, p) == 2) {\n        printf(\"%s\\n\", isMatch(s, p) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "aa a", "expected_output": "false", "is_sample": True},
        {"input": "aa *", "expected_output": "true", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "cb ?a", "expected_output": "false", "is_sample": False},
        {"input": "adceb *a*b", "expected_output": "true", "is_sample": False},
        {"input": "acdcb a*c?b", "expected_output": "false", "is_sample": False},
        {"input": "abc ???", "expected_output": "true", "is_sample": False},
        {"input": "a *", "expected_output": "true", "is_sample": False},
        # Last three: Stress tests
        {"input": "a"*2000 + " *a", "expected_output": "true", "is_sample": False},
        {"input": "a"*1999 + "b " + "*a*c", "expected_output": "false", "is_sample": False},
        {"input": "ab"*1000 + " *a*b*a*b", "expected_output": "true", "is_sample": False}
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
        "topics": ["String", "Dynamic Programming", "Greedy", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-200/44_Wildcard_Matching.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
