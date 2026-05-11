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
        "python": (
            "import sys\n"
            "import json\n\n"
            "def canConstruct(ransomNote: str, magazine: str) -> bool:\n"
            "    # User logic here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    raw_input = sys.stdin.read().strip()\n"
            "    if raw_input:\n"
            "        lines = raw_input.split('\\n')\n"
            "        if len(lines) >= 2:\n"
            "            r = json.loads(lines[0])\n"
            "            m = json.loads(lines[1])\n"
            "            print(str(canConstruct(r, m)).lower())\n"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <string>\n"
            "#include <algorithm>\n\n"
            "using namespace std;\n\n"
            "bool canConstruct(string ransomNote, string magazine) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "}\n\n"
            "string stripQuotes(string s) {\n"
            "    if (!s.empty() && s.back() == '\\r') s.pop_back();\n"
            "    if (s.length() >= 2 && s.front() == '\"' && s.back() == '\"') {\n"
            "        return s.substr(1, s.length() - 2);\n"
            "    }\n"
            "    return s;\n"
            "}\n\n"
            "int main() {\n"
            "    string r, m;\n"
            "    if (getline(cin, r)) {\n"
            "        r = stripQuotes(r);\n"
            "        if (getline(cin, m)) {\n"
            "            m = stripQuotes(m);\n"
            "            cout << (canConstruct(r, m) ? \"true\" : \"false\") << endl;\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        ),
        "java": (
            "import java.util.*;\n\n"
            "class Solution {\n"
            "    public boolean canConstruct(String ransomNote, String magazine) {\n"
            "        // User logic here\n"
            "        return true;\n"
            "    }\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextLine()) {\n"
            "            String r = sc.nextLine();\n"
            "            if (r.startsWith(\"\\\"\") && r.endsWith(\"\\\"\")) {\n"
            "                r = r.substring(1, r.length() - 1);\n"
            "            }\n"
            "            if (sc.hasNextLine()) {\n"
            "                String m = sc.nextLine();\n"
            "                if (m.startsWith(\"\\\"\") && m.endsWith(\"\\\"\")) {\n"
            "                    m = m.substring(1, m.length() - 1);\n"
            "                }\n"
            "                Solution sol = new Solution();\n"
            "                System.out.println(sol.canConstruct(r, m));\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        "javascript": (
            "/**\n"
            " * @param {string} ransomNote\n"
            " * @param {string} magazine\n"
            " * @return {boolean}\n"
            " */\n"
            "var canConstruct = function(ransomNote, magazine) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "};\n\n"
            "const fs = require('fs');\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').trim().split('\\n');\n"
            "    if (input.length >= 2) {\n"
            "        const r = JSON.parse(input[0]);\n"
            "        const m = JSON.parse(input[1]);\n"
            "        console.log(canConstruct(r, m) ? 'true' : 'false');\n"
            "    }\n"
            "}\n"
            "main();\n"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <stdbool.h>\n"
            "#include <string.h>\n\n"
            "bool canConstruct(char* ransomNote, char* magazine) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "}\n\n"
            "void stripQuotes(char* s) {\n"
            "    int len = strlen(s);\n"
            "    if (len > 0 && s[len-1] == '\\n') s[--len] = '\\0';\n"
            "    if (len > 0 && s[len-1] == '\\r') s[--len] = '\\0';\n"
            "    if (len >= 2 && s[0] == '\"' && s[len-1] == '\"') {\n"
            "        memmove(s, s + 1, len - 2);\n"
            "        s[len - 2] = '\\0';\n"
            "    }\n"
            "}\n\n"
            "int main() {\n"
            "    char r[200000];\n"
            "    char m[200000];\n"
            "    if (fgets(r, sizeof(r), stdin)) {\n"
            "        stripQuotes(r);\n"
            "        if (fgets(m, sizeof(m), stdin)) {\n"
            "            stripQuotes(m);\n"
            "            if (canConstruct(r, m)) {\n"
            "                printf(\"true\\n\");\n"
            "            } else {\n"
            "                printf(\"false\\n\");\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        )
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
