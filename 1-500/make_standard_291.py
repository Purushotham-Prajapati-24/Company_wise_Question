import json
import os

def generate_json():
    problem_id = 291
    title = "Word Pattern II"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>291. Word Pattern II</h3>
<p>Given a <code>pattern</code> and a string <code>s</code>, return <code>true</code> if <code>s</code> <strong>matches</strong> the <code>pattern</code>.</p>

<p>A string <code>s</code> <b>matches</b> a <code>pattern</code> if there is some <b>bijective mapping</b> of single characters to <b>non-empty</b> strings such that if each character in <code>pattern</code> is replaced by the string it maps to, then the resulting string is <code>s</code>. A <b>bijective mapping</b> means that no two characters map to the same string, and no character maps to two different strings.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> pattern = "abab", s = "redblueredblue"
<strong>Output:</strong> true
<strong>Explanation:</strong> One possible mapping is as follows:
'a' -&gt; "red"
'b' -&gt; "blue"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> pattern = "aaaa", s = "asdasdasdasd"
<strong>Output:</strong> true
<strong>Explanation:</strong> One possible mapping is as follows:
'a' -&gt; "asd"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> pattern = "aabb", s = "xyzabcxzyabc"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= pattern.length &lt;= 20</code></li>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>pattern</code> and <code>s</code> consist of only lowercase English letters.</li>
</ul>"""

    input_format = "Two strings: `pattern` and `s`."
    output_format = "A boolean value: true or false."
    
    constraints = [
        "1 <= pattern.length <= 20",
        "1 <= s.length <= 50",
        "Lowercase English letters."
    ]
    
    explanation = """To check if a string matches a pattern with a bijective mapping:
1. **Backtracking**: Use recursion to try different lengths of substrings in `s` for each character in the `pattern`.
2. **Bijective Mapping**: To maintain a bijection:
   - Use a Hash Map `char_to_str` to map character (from pattern) to string (from s).
   - Use a Hash Set `str_used` to track which strings from `s` are already mapped to identify if two characters map to the same string.
3. **Recursive Step**:
   - If the current character in pattern already has a mapping:
     - Check if it matches the prefix of the current string `s`.
     - If so, recurse with the remaining pattern and string.
   - If the current character doesn't have a mapping:
     - Try all possible non-empty prefixes of `s` as a potential mapping.
     - For each prefix, ensure it's not already used by another character.
     - Add mapping, recurse, and then backtrack (remove mapping).
4. **Complexity Analysis**:
   - Time: O(N * C_s^P) where N is length of pattern, C_s is length of string s, and P is pattern length. Since N and C_s are small (20, 50), this is efficient enough.
   - Space: O(N) for recursion and the mapping."""
    
    answer = """class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        # 1. Bijective logic: map for char -> str and set for used strings
        char_to_str = {}
        str_used = set()
        
        def backtrack(p_idx, s_idx):
            # Base Case: Both reaching the end means success
            if p_idx == len(pattern):
                return s_idx == len(s)
            
            p_char = pattern[p_idx]
            
            # 2. Case: The current char already has a mapping
            if p_char in char_to_str:
                mapped_str = char_to_str[p_char]
                # Check if it matches the current part of string s
                if s.startswith(mapped_str, s_idx):
                    return backtrack(p_idx + 1, s_idx + len(mapped_str))
                return False
                
            # 3. Case: The current char doesn't have a mapping yet
            # Try all possible prefixes of the remaining string s
            # Must be non-empty (at least 1 char)
            for i in range(s_idx, len(s)):
                curr_str = s[s_idx : i + 1]
                
                # Check if this string is already used by another char
                if curr_str in str_used:
                    continue
                
                # Add mapping and recurse
                char_to_str[p_char] = curr_str
                str_used.add(curr_str)
                if backtrack(p_idx + 1, i + 1):
                    return True
                
                # 4. Backtrack!
                del char_to_str[p_char]
                str_used.remove(curr_str)
            
            return False
            
        return backtrack(0, 0)"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef wordPatternMatch(pattern: str, s: str) -> bool:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Try extracting via regex\n    p_match = re.search(r'pattern\\s*=\\s*\"([^\"]+)\"', raw_input)\n    s_match = re.search(r's\\s*=\\s*\"([^\"]+)\"', raw_input)\n    \n    if p_match and s_match:\n        pattern = p_match.group(1)\n        s = s_match.group(1)\n    else:\n        # Fallback to lines\n        lines = [line.strip().strip('\"') for line in raw_input.strip().split('\\n') if line.strip()]\n        pattern = lines[0] if len(lines) > 0 else \"\"\n        s = lines[1] if len(lines) > 1 else \"\"\n        \n    print('true' if wordPatternMatch(pattern, s) else 'false')",
        "cpp": "#include <iostream>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nbool wordPatternMatch(string pattern, string s) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    regex re_p(R\"(pattern\\s*=\\s*\"([^\"]+)\")\");\n    regex re_s(R\"(s\\s*=\\s*\"([^\"]+)\")\");\n    smatch m;\n    \n    string pattern, s_str;\n    if (regex_search(input, m, re_p)) pattern = m.str(1);\n    if (regex_search(input, m, re_s)) s_str = m.str(1);\n    \n    if (pattern.empty() && s_str.empty()) {\n        // Fallback for simple line input\n        stringstream ss(input);\n        getline(ss, pattern);\n        getline(ss, s_str);\n        pattern.erase(remove(pattern.begin(), pattern.end(), '\"'), pattern.end());\n        s_str.erase(remove(s_str.begin(), s_str.end(), '\"'), s_str.end());\n    }\n\n    cout << (wordPatternMatch(pattern, s_str) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public boolean wordPatternMatch(String pattern, String s) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        \n        String pattern = \"\", s_str = \"\";\n        Matcher mP = Pattern.compile(\"pattern\\\\s*=\\\\s*\\\"([^\\\"]+)\\\"\").matcher(input);\n        Matcher mS = Pattern.compile(\"s\\\\s*=\\\\s*\\\"([^\\\"]+)\\\"\").matcher(input);\n        \n        if (mP.find()) pattern = mP.group(1);\n        if (mS.find()) s_str = mS.group(1);\n        \n        if (pattern.isEmpty()) {\n            String[] lines = input.split(\"\\\\n\");\n            pattern = lines[0].replace(\"\\\"\", \"\").trim();\n            s_str = lines[1].replace(\"\\\"\", \"\").trim();\n        }\n\n        System.out.println(new Solution().wordPatternMatch(pattern, s_str) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\nconst input = fs.readFileSync(0, 'utf-8').trim();\n\nfunction wordPatternMatch(pattern, s) {\n    // User logic here\n    return false;\n}\n\nconst p_match = input.match(/pattern\\s*=\\s*\"([^\"]+)\"/);\nconst s_match = input.match(/s\\s*=\\s*\"([^\"]+)\"/);\n\nlet pattern = p_match ? p_match[1] : \"\";\nlet s = s_match ? s_match[1] : \"\";\n\nif (!pattern) {\n    const lines = input.split('\\n');\n    pattern = lines[0].replace(/\"/g, '').trim();\n    s = lines[1].replace(/\"/g, '').trim();\n}\n\nconsole.log(wordPatternMatch(pattern, s) ? 'true' : 'false');",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\nbool wordPatternMatch(char* pattern, char* s) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    char pattern[256], s[256];\n    if (scanf(\"%s %s\", pattern, s) == 2) {\n        printf(\"%s\\n\", wordPatternMatch(pattern, s) ? \"true\" : \"false\");\n    } else {\n        printf(\"false\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '"abab"\\n"redblueredblue"', "expected_output": "true", "is_sample": True},
        {"input": '"aaaa"\\n"asdasdasdasd"', "expected_output": "true", "is_sample": True},
        {"input": '"aabb"\\n"xyzabcxzyabc"', "expected_output": "false", "is_sample": True},
        {"input": '"p"\\n"python"', "expected_output": "true", "is_sample": False},
        {"input": '"ab"\\n"a"', "expected_output": "false", "is_sample": False},
        {"input": '"aba"\\n"aaaaa"', "expected_output": "true", "is_sample": False},
        {"input": '"abcdef"\\n"fedcba"', "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": '"' + 'a' * 20 + '"\\n"' + 'b' * 40 + '"', "expected_output": "true", "is_sample": False},
        {"input": '"' + ''.join(chr(97 + i) for i in range(20)) + '"\\n"' + 'z' * 50 + '"', "expected_output": "false", "is_sample": False},
        {"input": '"abababab"\\n"aaaaaa"', "expected_output": "false", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "201-400/291_Word_Pattern_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
