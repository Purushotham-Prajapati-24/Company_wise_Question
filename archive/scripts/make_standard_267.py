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
        "python": "import sys\nimport json\n\ndef generatePalindromes(s: str) -> list[str]:\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if not data: sys.exit()\n    res = generatePalindromes(data[0])\n    res.sort()\n    print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nvector<string> generatePalindromes(string s) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string s;\n    if (cin >> s) {\n        vector<string> res = generatePalindromes(s);\n        sort(res.begin(), res.end());\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); i++) {\n            cout << \"\\\"\" << res[i] << \"\\\"\" << (i == res.size() - 1 ? \"\" : \",\");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<String> generatePalindromes(String s) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String s = sc.next();\n            List<String> res = new Solution().generatePalindromes(s);\n            Collections.sort(res);\n            StringBuilder sb = new StringBuilder(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                sb.append(\"\\\"\").append(res.get(i)).append(\"\\\"\").append(i == res.size() - 1 ? \"\" : \",\");\n            }\n            sb.append(\"]\");\n            System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction generatePalindromes(s) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    let res = generatePalindromes(input[0]);\n    res.sort();\n    console.log(JSON.stringify(res));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint cmp(const void* a, const void* b) {\n    return strcmp(*(const char**)a, *(const char**)b);\n}\n\nchar** generatePalindromes(char* s, int* returnSize) {\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char s[20];\n    if (scanf(\"%19s\", s) == 1) {\n        int returnSize = 0;\n        char** res = generatePalindromes(s, &returnSize);\n        if (returnSize > 0) {\n            qsort(res, returnSize, sizeof(char*), cmp);\n        }\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"\\\"%s\\\"%s\", res[i], i == returnSize - 1 ? \"\" : \",\");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
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
