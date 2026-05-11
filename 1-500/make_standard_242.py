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
        "python": "import sys\nimport re\n\ndef isAnagram(s, t):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Try to find two quoted strings first\n    matches = re.findall(r'\"([^\"]*)\"', raw_input)\n    if len(matches) < 2:\n        # Fallback to finding sequences of characters if not quoted\n        # Filter out common labels like 's', 't', 'input'\n        all_words = re.findall(r'[a-z]+', raw_input.lower())\n        # Heuristic: find the two longest words or the ones after labels\n        # For simplicity, we'll assume they are the words after 's=' and 't='\n        # or just the last two words if labels exist.\n        # More robust: find matches for s=... t=...\n        s_match = re.search(r's\\s*=\\s*\"?([a-z]+)\"?', raw_input)\n        t_match = re.search(r't\\s*=\\s*\"?([a-z]+)\"?', raw_input)\n        if s_match and t_match:\n            s, t = s_match.group(1), t_match.group(1)\n        else:\n            # Last resort: just take all words and hope for the best\n            # If there are exactly two words, take them. \n            # If more, try to exclude 's', 't', 'true', 'false'\n            words = [w for w in all_words if w not in [\"s\", \"t\", \"true\", \"false\"]]\n            if len(words) >= 2:\n                s, t = words[0], words[1]\n            else:\n                sys.exit(0)\n    else:\n        s, t = matches[0], matches[1]\n        \n    print(\"true\" if isAnagram(s, t) else \"false\")",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nbool isAnagram(string s, string t) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    regex re_quoted(\"\\\"([^\\\"]*)\\\"\");\n    auto q_begin = sregex_iterator(input.begin(), input.end(), re_quoted);\n    auto q_end = sregex_iterator();\n    \n    string s, t;\n    vector<string> matches;\n    for (sregex_iterator i = q_begin; i != q_end; ++i) matches.push_back((*i)[1].str());\n    \n    if (matches.size() >= 2) {\n        s = matches[0]; t = matches[1];\n    } else {\n        regex re_word(\"[a-z]+\");\n        auto w_begin = sregex_iterator(input.begin(), input.end(), re_word);\n        vector<string> words;\n        for (sregex_iterator i = w_begin; i != q_end; ++i) {\n            string w = i->str();\n            if (w != \"s\" && w != \"t\" && w != \"true\" && w != \"false\") words.push_back(w);\n        }\n        if (words.size() >= 2) {\n            s = words[0]; t = words[1];\n        } else return 0;\n    }\n    \n    cout << (isAnagram(s, t) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public boolean isAnagram(String s, String t) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        List<String> matches = new ArrayList<>();\n        Pattern p_quoted = Pattern.compile(\"\\\"([^\\\"]*)\\\"\");\n        Matcher m_quoted = p_quoted.matcher(input);\n        while (m_quoted.find()) matches.add(m_quoted.group(1));\n        \n        String s = \"\", t = \"\";\n        if (matches.size() >= 2) {\n            s = matches.get(0); t = matches.get(1);\n        } else {\n            Pattern p_word = Pattern.compile(\"[a-z]+\");\n            Matcher m_word = p_word.matcher(input.toLowerCase());\n            List<String> words = new ArrayList<>();\n            while (m_word.find()) {\n                String w = m_word.group();\n                if (!w.equals(\"s\") && !w.equals(\"t\") && !w.equals(\"true\") && !w.equals(\"false\")) words.add(w);\n            }\n            if (words.size() >= 2) {\n                s = words.get(0); t = words.get(1);\n            } else return;\n        }\n        System.out.println(new Solution().isAnagram(s, t) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isAnagram(s, t) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst matches = input.match(/\"([^\"]*)\"/g);\n\nlet s, t;\nif (matches && matches.length >= 2) {\n    s = matches[0].replace(/\"/g, '');\n    t = matches[1].replace(/\"/g, '');\n} else {\n    const words = (input.toLowerCase().match(/[a-z]+/g) || []).filter(w => ![\"s\", \"t\", \"true\", \"false\"].includes(w));\n    if (words.length >= 2) {\n        s = words[0]; t = words[1];\n    } else process.exit(0);\n}\n\nconsole.log(isAnagram(s, t) ? \"true\" : \"false\");",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n#include <ctype.h>\n#include <stdlib.h>\n\nbool isAnagram(char* s, char* t) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    static char buffer[1000000];\n    int bytes = fread(buffer, 1, sizeof(buffer)-1, stdin);\n    buffer[bytes] = '\\0';\n    \n    char *s = (char*)malloc(100000 * sizeof(char));\n    char *t = (char*)malloc(100000 * sizeof(char));\n    int s_len = 0, t_len = 0;\n    \n    // Find first two sequences of lowercase letters, ignoring 's' and 't' as labels\n    char* ptr = buffer;\n    int word_count = 0;\n    while (*ptr) {\n        if (islower(*ptr)) {\n            char* start = ptr;\n            while (islower(*ptr)) ptr++;\n            int len = ptr - start;\n            if (len == 1 && (*start == 's' || *start == 't')) continue;\n            if (len == 4 && strncmp(start, \"true\", 4) == 0) continue;\n            if (len == 5 && strncmp(start, \"false\", 5) == 0) continue;\n            \n            if (word_count == 0) {\n                strncpy(s, start, len); s[len] = '\\0';\n                word_count++;\n            } else if (word_count == 1) {\n                strncpy(t, start, len); t[len] = '\\0';\n                word_count++;\n                break;\n            }\n        } else ptr++;\n    }\n    \n    if (word_count == 2) {\n        printf(\"%s\\n\", isAnagram(s, t) ? \"true\" : \"false\");\n    }\n    \n    free(s); free(t);\n    return 0;\n}"
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
