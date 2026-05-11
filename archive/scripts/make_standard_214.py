import json
import os

def generate_json():
    problem_id = 214
    title = "Shortest Palindrome"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>214. Shortest Palindrome</h3>
<p>You are given a string <code>s</code>. You can convert <code>s</code> to a palindrome by adding characters in front of it.</p>

<p>Return <em>the shortest palindrome you can find by performing this transformation</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aacecaaa"
<strong>Output:</strong> "aaacecaaa"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcd"
<strong>Output:</strong> "dcbabcd"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters only.</li>
</ul>"""

    input_format = "A single string s."
    output_format = "The shortest palindrome obtainable by adding characters to the front."
    
    constraints = [
        "0 <= s.length <= 5 * 10^4",
        "Lowercase English letters only.",
        "O(N) time complexity expected."
    ]
    
    explanation = """To find the shortest palindrome by adding characters to the front:
1. **Identify the Goal**:
   - We need to find the **longest palindromic prefix** of the string `s`.
   - Once we find it, say `s[0:k]`, the shortest palindrome is `s[k:n].reverse() + s`.
2. **KMP-based Optimization**:
   - Concatenate `s`, a separator `#`, and the reverse of `s`: `combined = s + "#" + s[::-1]`.
   - Compute the **Partial Match Table** (also known as the `next` array in KMP) for this combined string.
   - The last value in the table represents the length of the longest prefix of `combined` that is also a suffix of `combined`.
   - Because the second half of `combined` is the reverse of `s`, this match gives exactly the length of the longest palindromic prefix of `s`.
3. **Complexity**:
   - Time Complexity: O(N) to compute the KMP table.
   - Space Complexity: O(N) to store the reversed string and table."""
    
    answer = """def shortestPalindrome(s: str) -> str:
    if not s:
        return ""
    # Create combined string: s + separator + reverse(s)
    rev_s = s[::-1]
    combined = s + "#" + rev_s
    
    # KMP Partial Match Table (LPS)
    n = len(combined)
    lps = [0] * n
    for i in range(1, n):
        j = lps[i-1]
        while j > 0 and combined[i] != combined[j]:
            j = lps[j-1]
        if combined[i] == combined[j]:
            j += 1
        lps[i] = j
        
    # Longest palindromic prefix length is lps[-1]
    add_len = len(s) - lps[-1]
    return rev_s[:add_len] + s"""

    boilerplate = {
        "python": "import sys\n\ndef shortestPalindrome(s):\n    # User logic here\n    return \"\"\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    print(shortestPalindrome(s))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nstring shortestPalindrome(string s) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    string s;\n    if (cin >> s) {\n        cout << shortestPalindrome(s) << endl;\n    } else {\n        cout << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public String shortestPalindrome(String s) {\n        // User logic\n        return \"\";\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String s = br.readLine();\n        if (s == null) s = \"\";\n        System.out.println(new Solution().shortestPalindrome(s.trim()));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction shortestPalindrome(s) {\n    // User logic\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconsole.log(shortestPalindrome(input));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* shortestPalindrome(char* s) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    char s[100000];\n    if (scanf(\"%s\", s) == 1) {\n        printf(\"%s\\n\", shortestPalindrome(s));\n    } else {\n        printf(\"\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "aacecaaa", "expected_output": "aaacecaaa", "is_sample": True},
        {"input": "abcd", "expected_output": "dcbabcd", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "a", "expected_output": "a", "is_sample": False},
        {"input": "aa", "expected_output": "aa", "is_sample": False},
        {"input": "ab", "expected_output": "bab", "is_sample": False},
        {"input": "abbac", "expected_output": "cabbac", "is_sample": False},
        # Stress cases
        {"input": "a"*50000, "expected_output": "a"*50000, "is_sample": False},
        {"input": "ab"*25000, "expected_output": "ba" + "ab"*25000 if not "abab" else "b" + "ab"*25000, "is_sample": False},
        {"input": "z"*1000 + "a"*10, "expected_output": "..." , "is_sample": False}
    ]
    
    # Correcting stress case 9/10 logic
    def _solve(s):
        if not s: return ""
        r = s[::-1]
        c = s + "#" + r
        lps = [0] * len(c)
        for i in range(1, len(c)):
            j = lps[i-1]
            while j > 0 and c[i] != c[j]: j = lps[j-1]
            if c[i] == c[j]: j += 1
            lps[i] = j
        return r[:len(s)-lps[-1]] + s
        
    test_cases[8]["expected_output"] = _solve("ab"*25000)
    test_cases[9]["expected_output"] = _solve("z"*1000 + "a"*10)

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
        "topics": ["String", "Rolling Hash", "String Matching", "Hash Function"],
        "companyIndex": 0
    }

    output_path = "1-200/214_Shortest_Palindrome.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
