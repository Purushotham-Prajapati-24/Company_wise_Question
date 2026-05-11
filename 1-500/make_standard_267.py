import json
import os

def generate_json():
    problem_id = 267
    title = "Palindrome Permutation II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>267. Palindrome Permutation II</h3>
<p>Given a string <code>s</code>, return <em>all the palindromic permutations (without duplicates) of it</em>. Return an empty list if no palindromic permutation can be formed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aabb"
<strong>Output:</strong> ["abba","baab"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 <= s.length <= 16</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>"""

    input_format = "A single string s."
    output_format = "A list of strings representing unique palindromic permutations."
    
    constraints = ["1 <= s.length <= 16", "s consists of lowercase English letters"]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """import collections\n\nclass Solution:\n    def generatePalindromes(self, s: str) -> List[str]:\n        counts = collections.Counter(s)\n        odd_chars = [c for c, count in counts.items() if count % 2 == 1]\n        if len(odd_chars) > 1:\n            return []\n        \n        mid = odd_chars[0] if odd_chars else \"\"\n        half = []\n        for c, count in counts.items():\n            half.extend([c] * (count // 2))\n        \n        result = []\n        def backtrack(path, used):\n            if len(path) == len(half):\n                h = \"\".join(path)\n                result.append(h + mid + h[::-1])\n                return\n            \n            for i in range(len(half)):\n                if used[i] or (i > 0 and half[i] == half[i-1] and not used[i-1]):\n                    continue\n                used[i] = True\n                path.append(half[i])\n                backtrack(path, used)\n                path.pop()\n                used[i] = False\n        \n        half.sort()\n        backtrack([], [False] * len(half))\n        return result"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef generatePalindromes(s: str) -> list[str]:\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    match = re.search(r's\\s*=\\s*\"([^\"]+)\"', raw_input)\n    if match:\n        s = match.group(1)\n    else:\n        s = raw_input.strip().split()[-1] if raw_input.strip().split() else \"\"\n        if s.startswith('s='): s = s.split('=')[-1]\n        s = s.strip('\"')\n    \n    res = generatePalindromes(s)\n    res.sort()\n    print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <regex>\n\nusing namespace std;\n\nvector<string> generatePalindromes(string s) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    string s;\n    regex re_s(R\"(s\\s*=\\s*\"([^\"]+)\")\");\n    smatch match;\n    if (regex_search(input, match, re_s)) {\n        s = match[1];\n    } else {\n        size_t last_quote = input.find_last_of('\"');\n        if (last_quote != string::npos) {\n            size_t start_quote = input.find_last_of('\"', last_quote - 1);\n            if (start_quote != string::npos) s = input.substr(start_quote + 1, last_quote - start_quote - 1);\n        } else {\n            size_t eq = input.find('=');\n            if (eq != string::npos) s = input.substr(eq + 1);\n            else s = input;\n            // trim\n            s.erase(0, s.find_first_not_of(\" \\t\\n\\r\"));\n            s.erase(s.find_last_not_of(\" \\t\\n\\r\") + 1);\n        }\n    }\n\n    vector<string> res = generatePalindromes(s);\n    sort(res.begin(), res.end());\n    cout << \"[\";\n    for (size_t i = 0; i < res.size(); i++) {\n        cout << \"\\\"\" << res[i] << \"\\\"\" << (i == res.size() - 1 ? \"\" : \",\");\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public List<String> generatePalindromes(String s) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (sc.hasNext()) {\n            String input = sc.next();\n            String s = \"\";\n            Matcher m = Pattern.compile(\"s\\\\s*=\\\\s*\\\"([^\\\"]+)\\\"\").matcher(input);\n            if (m.find()) {\n                s = m.group(1);\n            } else {\n                s = input.trim();\n                if (s.contains(\"=\")) s = s.substring(s.lastIndexOf(\"=\") + 1).trim();\n                s = s.replace(\"\\\"\", \"\");\n            }\n            \n            List<String> res = new Solution().generatePalindromes(s);\n            Collections.sort(res);\n            StringBuilder sb = new StringBuilder(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                sb.append(\"\\\"\").append(res.get(i)).append(\"\\\"\").append(i == res.size() - 1 ? \"\" : \",\");\n            }\n            sb.append(\"]\");\n            System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction generatePalindromes(s) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst match = input.match(/s\\s*=\\s*\"([^\"]+)\"/);\nlet s = \"\";\nif (match) {\n    s = match[1];\n} else {\n    s = input.trim().split(/\\s+/).pop();\n    if (s.includes('=')) s = s.split('=').pop();\n    s = s.replace(/\"/g, '');\n}\n\nlet res = generatePalindromes(s);\nres.sort();\nconsole.log(JSON.stringify(res));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nchar* trim(char* str) {\n    char* end;\n    while(isspace((unsigned char)*str)) str++;\n    if(*str == 0) return str;\n    end = str + strlen(str) - 1;\n    while(end > str && isspace((unsigned char)*end)) end--;\n    end[1] = '\\0';\n    return str;\n}\n\nint cmp(const void* a, const void* b) {\n    return strcmp(*(const char**)a, *(const char**)b);\n}\n\nchar** generatePalindromes(char* s, int* returnSize) {\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    static char buffer[1000000];\n    if (fread(buffer, 1, 999999, stdin) > 0) {\n        char *s_ptr = strstr(buffer, \"s =\");\n        if (!s_ptr) s_ptr = strstr(buffer, \"s=\");\n        char s[1000];\n        if (s_ptr) {\n            char *start = strchr(s_ptr, '\"');\n            if (start) {\n                char *end = strchr(start + 1, '\"');\n                if (end) {\n                    strncpy(s, start + 1, end - start - 1);\n                    s[end - start - 1] = '\\0';\n                }\n            }\n        } else {\n            strcpy(s, trim(buffer));\n        }\n\n        int returnSize = 0;\n        char** res = generatePalindromes(s, &returnSize);\n        if (returnSize > 0) {\nqsort(res, returnSize, sizeof(char*), cmp);\n        }\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"\\\"%s\\\"%s\", res[i], i == returnSize - 1 ? \"\" : \",\");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [{"input": "aabb", "expected_output": '["abba","baab"]', "is_sample": True},
        {"input": "abc", "expected_output": "[]", "is_sample": True},
        {"input": "a", "expected_output": '["a"]', "is_sample": False},
        {"input": "aa", "expected_output": '["aa"]', "is_sample": False},
        {"input": "aaa", "expected_output": '["aaa"]', "is_sample": False},
        {"input": "aabbc", "expected_output": '["abcba","bacab"]', "is_sample": False},
        {"input": "aaaaa", "expected_output": '["aaaaa"]', "is_sample": False},
        {"input": "abcabc", "expected_output": '["abccba","acbbca","bacabc","bcacba","cabbac","cbaabc"]', "is_sample": False},
        {"input": "aabbcc", "expected_output": '["abccba","acbbca","bacabc","bcacba","cabbac","cbaabc"]', "is_sample": False},
        {"input": "abcde", "expected_output": "[]", "is_sample": False}]

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

    output_path = "1-1000/267_Palindrome_Permutation_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
