import json
import os
import collections

def generate_json():
    problem_id = 451
    title = "Sort Characters By Frequency"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>451. Sort Characters By Frequency</h3>
<p>Given a string <code>s</code>, sort it in <strong>decreasing order</strong> based on the <strong>frequency</strong> of the characters. The <strong>frequency</strong> of a character is the number of times it appears in the string.</p>

<p>Return <em>the sorted string</em>. If there are multiple answers, return <em>any of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "tree"
<strong>Output:</strong> "eert"
<strong>Explanation:</strong> 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "cccaaa"
<strong>Output:</strong> "aaaccc"
<strong>Explanation:</strong> Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "Aabb"
<strong>Output:</strong> "bbAa"
<strong>Explanation:</strong> "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of uppercase and lowercase English letters and digits.</li>
</ul>"""

    input_format = "A single string `s`."
    output_format = "A string representing the characters sorted by frequency."
    
    constraints = [
        "1 <= s.length <= 5 * 10^5",
        "s consists of alphanumeric characters."
    ]
    
    explanation = "Count the frequency of each character using a hash map. Sort the characters based on their frequency in descending order. Construct the result string by repeating each character its frequency number of times."
    
    answer = """import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        # Sort characters by frequency (desc)
        sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        res = []
        for char, freq in sorted_chars:
            res.append(char * freq)
        return "".join(res)"""

    boilerplate = {
        "python": "import sys\nimport json\nimport collections\n\nclass Solution:\n    def frequencySort(self, s: str) -> str:\n        # User logic here\n        return \"\"\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        if raw_input.startswith(('\"', \"'\")) and raw_input.endswith(('\"', \"'\")):\n            s = raw_input[1:-1]\n        else:\n            s = raw_input\n        sol = Solution()\n        print(json.dumps(sol.frequencySort(s)))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <unordered_map>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    string frequencySort(string s) {\n        // User logic here\n        return \"\";\n    }\n};\n\nint main() {\n    string s;\n    if (getline(cin, s)) {\n        if (!s.empty() && (s.front() == '\"' || s.front() == '\\'')) {\n            s = s.substr(1, s.size() - 2);\n        }\n        Solution sol;\n        cout << \"\\\"\" << sol.frequencySort(s) << \"\\\"\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public String frequencySort(String s) {\n        // User logic here\n        return \"\";\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine().trim();\n            if (s.length() >= 2 && s.startsWith(\"\\\"\") && s.endsWith(\"\\\"\")) {\n                s = s.substring(1, s.length() - 1);\n            }\n            Solution sol = new Solution();\n            System.out.println(\"\\\"\" + sol.frequencySort(s) + \"\\\"\");\n        }\n    }\n}",
        "javascript": "var frequencySort = function(s) {\n    // User logic here\n};\n\nconst fs = require('fs');\nlet input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    if ((input.startsWith('\"') && input.endsWith('\"')) || (input.startsWith(\"'\") && input.endsWith(\"'\"))) {\n        input = input.slice(1, -1);\n    }\n    console.log(JSON.stringify(frequencySort(input)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* frequencySort(char* s) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    char s[500005];\n    if (fgets(s, 500005, stdin)) {\n        s[strcspn(s, \"\\n\")] = 0;\n        char *p = s;\n        if (*p == '\"') {\n            p++;\n            s[strlen(s)-1] = 0;\n        }\n        printf(\"\\\"%s\\\"\\n\", frequencySort(p));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "tree", "expected_output": "\"eert\"", "is_sample": True},
        {"input": "cccaaa", "expected_output": "\"aaaccc\"", "is_sample": True},
        {"input": "Aabb", "expected_output": "\"bbAa\"", "is_sample": True},
        {"input": "a", "expected_output": "\"a\"", "is_sample": False},
        {"input": "22111", "expected_output": "\"11122\"", "is_sample": False},
        {"input": "loveleetcode", "expected_output": "\"eeeeoollvvtd\"", "is_sample": False},
        {"input": "  raeaere  ", "expected_output": "\"eeeeaar\"", "is_sample": False},
        {"input": "Mississippi", "expected_output": "\"iiiippppsssM\"", "is_sample": False},
        {"input": "1234567890", "expected_output": "\"0123456789\"", "is_sample": False},
        {"input": "a" * 100, "expected_output": "\"" + "a" * 100 + "\"", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Sorting", "Heap (Priority Queue)", "Bucket Sort"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Sort_Characters_By_Frequency.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
