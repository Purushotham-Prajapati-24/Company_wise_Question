import json
import os

def generate_json():
    problem_id = 383
    title = "Ransom Note"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>383. Ransom Note</h3>
<p>Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code><em> if </em><code>ransomNote</code><em> can be constructed by using the letters from </em><code>magazine</code><em> and </em><code>false</code><em> otherwise</em>.</p>

<p>Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> ransomNote = "a", magazine = "b"
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "ab"
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "aab"
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code></li>
	<li><code>ransomNote</code> and <code>magazine</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "Two strings: ransomNote and magazine."
    output_format = "A boolean value: true or false."
    
    constraints = ["1 <= ransomNote.length", "magazine.length <= 10^5", "Both strings consist of lowercase English letters."]
    
    explanation = """To determine if `ransomNote` can be constructed from `magazine`:
1. Use a frequency map (or hash table) to count occurrences of each character in `magazine`.
2. Iterate through each character in `ransomNote`.
3. For each character, check if it's available in the map.
4. If available and count > 0, decrement its count.
5. If not available or count == 0, return `false`.
6. If the loop completes, return `true`.

### Complexity:
- **Time Complexity**: $O(N + M)$, where $N$ is the length of `ransomNote` and $M$ is the length of `magazine`.
- **Space Complexity**: $O(1)$ (since there are only 26 lowercase English letters)."""
    
    answer = """from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    counts = Counter(magazine)
    for char in ransomNote:
        if counts[char] <= 0:
            return False
        counts[char] -= 1
    return True"""

    boilerplate = {
        "python": "import sys\nimport json\ndef canConstruct(ransomNote: str, magazine: str) -> bool:\n    # User logic here\n    pass\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        try:\n            r = json.loads(input_data[0])\n            m = json.loads(input_data[1])\n        except:\n            r = input_data[0].strip('\"')\n            m = input_data[1].strip('\"')\n        print(str(canConstruct(r, m)).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <regex>\nusing namespace std;\nbool canConstruct(string ransomNote, string magazine) {\n    // User logic here\n    return true;\n}\nstring parse(string s) {\n    s.erase(0, s.find_first_not_of(\" \\t\\n\\r\"));\n    s.erase(s.find_last_not_of(\" \\t\\n\\r\") + 1);\n    if (s.size() >= 2 && s.front() == '\"' && s.back() == '\"') s = s.substr(1, s.size() - 2);\n    return s;\n}\nint main() {\n    string r, m;\n    if (getline(cin, r) && getline(cin, m)) {\n        cout << (canConstruct(parse(r), parse(m)) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static boolean canConstruct(String ransomNote, String magazine) {\n        // User logic here\n        return true;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String r = sc.nextLine().trim();\n            if (r.startsWith(\"\\\"\") && r.endsWith(\"\\\"\")) r = r.substring(1, r.length() - 1);\n            if (sc.hasNextLine()) {\n                String m = sc.nextLine().trim();\n                if (m.startsWith(\"\\\"\") && m.endsWith(\"\\\"\")) m = m.substring(1, m.length() - 1);\n                System.out.println(canConstruct(r, m));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nconst canConstruct = (ransomNote, magazine) => {\n    // User logic here\n    return true;\n};\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    const parse = s => {\n        s = s.trim();\n        if (s.startsWith('\"') && s.endsWith('\"')) return JSON.parse(s);\n        return s;\n    };\n    console.log(canConstruct(parse(input[0]), parse(input[1])));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\nbool canConstruct(char* ransomNote, char* magazine) {\n    // User logic here\n    return true;\n}\nvoid parse(char* s) {\n    int len = strlen(s);\n    while (len > 0 && (s[len-1] == '\\n' || s[len-1] == '\\r' || s[len-1] == ' ')) s[--len] = '\\0';\n    if (len >= 2 && s[0] == '\"' && s[len-1] == '\"') {\n        memmove(s, s + 1, len - 2);\n        s[len - 2] = '\\0';\n    }\n}\nint main() {\n    char r[200000], m[200000];\n    if (fgets(r, 200000, stdin) && fgets(m, 200000, stdin)) {\n        parse(r); parse(m);\n        printf(\"%s\\n\", canConstruct(r, m) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }
    test_cases = [
        # Sample cases (2)
        {"input": '"a"\n"b"', "expected_output": "false", "is_sample": True},
        {"input": '"aa"\n"aab"', "expected_output": "true", "is_sample": True},
        # Diverse cases (5)
        {"input": '"aa"\n"ab"', "expected_output": "false", "is_sample": False},
        {"input": '""\n"abc"', "expected_output": "true", "is_sample": False},
        {"input": '"abc"\n""', "expected_output": "false", "is_sample": False},
        {"input": '"fffbfg"\n"effjfggeffjgfejjfge"', "expected_output": "true", "is_sample": False},
        {"input": '"bg"\n"efjbdfbdgfjhgalig"', "expected_output": "true", "is_sample": False},
        # Stress cases (3)
        {"input": '"' + "a"*100000 + '"\n"' + "a"*100000 + '"', "expected_output": "true", "is_sample": False},
        {"input": '"' + "a"*100000 + '"\n"' + "b"*100000 + '"', "expected_output": "false", "is_sample": False},
        {"input": '"' + "abcdefghijklmnopqrstuvwxyz"*3846 + '"\n"' + "abcdefghijklmnopqrstuvwxyz"*3847 + '"', "expected_output": "true", "is_sample": False},
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
        "topics": ["Hash Table", "String", "Counting"],
        "companyIndex": 0
    }

    output_path = "301-500/383_Ransom_Note.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
