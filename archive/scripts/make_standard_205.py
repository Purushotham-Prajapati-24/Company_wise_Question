import json
import os

def generate_json():
    problem_id = 205
    title = "Isomorphic Strings"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>205. Isomorphic Strings</h3>
<p>Given two strings <code>s</code> and <code>t</code>, <em>determine if they are isomorphic</em>.</p>

<p>Two strings <code>s</code> and <code>t</code> are isomorphic if the characters in <code>s</code> can be replaced to get <code>t</code>.</p>

<p>All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "egg", t = "add"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "foo", t = "bar"
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "paper", t = "title"
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>t.length == s.length</code></li>
	<li><code>s</code> and <code>t</code> consist of any valid ASCII character.</li>
</ul>"""

    input_format = "Two lines. Line 1: string s. Line 2: string t."
    output_format = "true if the strings are isomorphic, false otherwise."
    
    constraints = [
        "1 <= s.length <= 5 * 10^4",
        "t.length == s.length",
        "O(N) time complexity expected.",
        "Must handle all ASCII characters."
    ]
    
    explanation = """To determine if two strings are isomorphic:
1. **Bijective Mapping**:
   - Each character in `s` must map to a unique character in `t`.
   - Each character in `t` must map back to a unique character in `s`.
2. **Implementation**:
   - Use two hash maps (or arrays of size 256 for ASCII) to store the mapping from `s` to `t` and from `t` to `s`.
   - Iterate through both strings simultaneously:
     - For characters `c1` in `s` and `c2` in `t`:
       - If `c1` is already mapped to something other than `c2`, or `c2` is already mapped to something other than `c1`, return `false`.
       - Otherwise, update the mappings.
3. **Complexity**:
   - Time Complexity: O(N) where N is the length of the strings.
   - Space Complexity: O(1) if we consider the character set size (256) as constant."""
    
    answer = """def isIsomorphic(s: str, t: str) -> bool:
    mapST, mapTS = {}, {}
    for c1, c2 in zip(s, t):
        if (c1 in mapST and mapST[c1] != c2) or \\
           (c2 in mapTS and mapTS[c2] != c1):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True"""

    boilerplate = {
        "python": "import sys\n\ndef isIsomorphic(s, t):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        print(\"true\" if isIsomorphic(lines[0], lines[1]) else \"false\")",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n\nusing namespace std;\n\nbool isIsomorphic(string s, string t) {\n    // User logic\n    return false;\n}\n\nint main() {\n    string s, t;\n    if (getline(cin, s) && getline(cin, t)) {\n        cout << (isIsomorphic(s, t) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public boolean isIsomorphic(String s, String t) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String s = br.readLine();\n        String t = br.readLine();\n        if (s != null && t != null) {\n            System.out.println(new Solution().isIsomorphic(s, t) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isIsomorphic(s, t) {\n    // User logic\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    console.log(isIsomorphic(input[0], input[1]) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\nbool isIsomorphic(char* s, char* t) {\n    // User logic\n    return false;\n}\n\nint main() {\n    char s[100000], t[100000];\n    if (fgets(s, sizeof(s), stdin) && fgets(t, sizeof(t), stdin)) {\n        s[strcspn(s, \"\\r\\n\")] = 0;\n        t[strcspn(t, \"\\r\\n\")] = 0;\n        printf(\"%s\\n\", isIsomorphic(s, t) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "egg\\nadd", "expected_output": "true", "is_sample": True},
        {"input": "foo\\nbar", "expected_output": "false", "is_sample": True},
        {"input": "paper\\ntitle", "expected_output": "true", "is_sample": True},
        {"input": "ab\\naa", "expected_output": "false", "is_sample": False},
        {"input": "aa\\nab", "expected_output": "false", "is_sample": False},
        {"input": "badc\\nbaba", "expected_output": "false", "is_sample": False},
        {"input": "a\\na", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "a"*50000 + "\\n" + "b"*50000, "expected_output": "true", "is_sample": False},
        {"input": "abcdefghij"*5000 + "\\n" + "klmnopqrst"*5000, "expected_output": "true", "is_sample": False},
        {"input": "abcdefghij"*5000 + "\\n" + "klmnopprst"*5000, "expected_output": "false", "is_sample": False}
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
        "topics": ["Hash Table", "String"],
        "companyIndex": 0
    }

    output_path = "1-200/205_Isomorphic_Strings.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
