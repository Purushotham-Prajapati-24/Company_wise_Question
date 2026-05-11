import json
import os

def generate_json():
    problem_id = 242
    title = "Valid Anagram"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>242. Valid Anagram</h3>
<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if</em> <code>t</code> <em>is an anagram of</em> <code>s</code>, <em>and</em> <code>false</code> <em>otherwise</em>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "anagram", t = "nagaram"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "rat", t = "car"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>"""

    input_format = "Two lines: first string `s`, then string `t` (each in double quotes)."
    output_format = "A boolean value: `true` or `false`."
    
    constraints = [
        "1 <= s.length, t.length <= 50,000",
        "Strings consist of lowercase English letters."
    ]
    
    explanation = """To check if two strings are anagrams, we need to ensure they have the same characters with the same frequencies:
1. **Character Counting**: We can use a hash map or an array of size 26 (since only lowercase English letters are used) to count the occurrences of each character in string `s`.
2. **Frequency Comparison**: Iterate through string `t` and decrement the counts. If any count becomes negative, or if the final counts are not all zero, the strings are not anagrams.
3. **Optimized Approach**: Since we only have 26 letters, using a fixed-size array is more space-efficient than a hash map. Sorting both strings and comparing is also an option but takes O(n log n) time."""
    
    answer = """import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counts = collections.Counter(s)
        for char in t:
            if counts[char] == 0:
                return False
            counts[char] -= 1
            
        return True"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef isAnagram(s, t):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        try:\n            s = json.loads(lines[0])\n            t = json.loads(lines[1])\n        except:\n            s = lines[0].strip().strip('\"')\n            t = lines[1].strip().strip('\"')\n        print(\"true\" if isAnagram(s, t) else \"false\")",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nbool isAnagram(string s, string t) {\n    // User logic\n    return false;\n}\n\nstring clean(string s) {\n    if (s.size() >= 2 && s.front() == '\"' && s.back() == '\"') {\n        return s.substr(1, s.size() - 2);\n    }\n    return s;\n}\n\nint main() {\n    string s, t;\n    if (cin >> s >> t) {\n        cout << (isAnagram(clean(s), clean(t)) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public boolean isAnagram(String s, String t) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) throws IOException {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String s = sc.next().replace(\"\\\"\", \"\");\n            if (sc.hasNext()) {\n                String t = sc.next().replace(\"\\\"\", \"\");\n                System.out.println(new Solution().isAnagram(s, t) ? \"true\" : \"false\");\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isAnagram(s, t) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\r?\\n/);\nif (input.length >= 2) {\n    const s = input[0].replace(/\"/g, '');\n    const t = input[1].replace(/\"/g, '');\n    console.log(isAnagram(s, t) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\nbool isAnagram(char* s, char* t) {\n    // User logic\n    return false;\n}\n\nvoid clean(char* s) {\n    int n = strlen(s);\n    if (n >= 2 && s[0] == '\"' && s[n-1] == '\"') {\n        for (int i = 0; i < n - 2; i++) s[i] = s[i+1];\n        s[n-2] = '\\0';\n    }\n}\n\nint main() {\n    char s[50005], t[50005];\n    if (scanf(\"%s %s\", s, t) == 2) {\n        clean(s);\n        clean(t);\n        printf(\"%s\\n\", isAnagram(s, t) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '"anagram"\\n"nagaram"', "expected_output": "true", "is_sample": True},
        {"input": '"rat"\\n"car"', "expected_output": "false", "is_sample": True},
        {"input": '"a"\\n"a"', "expected_output": "true", "is_sample": False},
        {"input": '"ab"\\n"a"', "expected_output": "false", "is_sample": False},
        {"input": '"aa"\\n"bb"', "expected_output": "false", "is_sample": False},
        {"input": '"aabbcc"\\n"abcabc"', "expected_output": "true", "is_sample": False},
        {"input": '"abcdefg"\\n"gfedcba"', "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": '"' + 'a' * 50000 + '"\\n"' + 'a' * 50000 + '"', "expected_output": "true", "is_sample": False},
        {"input": '"' + 'a' * 49999 + 'b"\\n"' + 'a' * 49999 + 'c"', "expected_output": "false", "is_sample": False},
        {"input": '"' + ''.join(chr(97 + i % 26) for i in range(50000)) + '"\\n"' + ''.join(chr(97 + i % 26) for i in reversed(range(50000))) + '"', "expected_output": "true", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Sorting"],
        "companyIndex": 0
    }

    output_path = "201-400/242_Valid_Anagram.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
