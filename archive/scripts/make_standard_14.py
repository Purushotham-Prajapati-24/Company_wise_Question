import json
import os

def generate_json():
    problem_id = 14
    title = "Longest Common Prefix"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>14. Longest Common Prefix</h3>
<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters.</li>
</ul>
"""

    input_format = "A single line containing space-separated strings 'strs'."
    output_format = "A string representing the longest common prefix."
    
    constraints = [
        "1 <= strs.length <= 200",
        "0 <= strs[i].length <= 200",
        "strs[i] consists of lowercase English letters."
    ]
    
    explanation = """To find the longest common prefix across multiple strings:
1. Handle edge cases (empty list or single string).
2. Sort the list of strings lexicographically. This puts the most different strings (at the first and last position) in a way that the common prefix must be shared between them.
3. Compare only the first and last strings in the sorted list.
4. Iterate through the characters of both strings simultaneously until they differ or one ends.
5. The matching substring from the start is the longest common prefix.

Alternatively, vertical scanning (checking each character index across all strings) is another valid O(S) approach where S is the sum of characters in all strings."""
    
    answer = """def longestCommonPrefix(strs):
    if not strs: return ""
    strs.sort()
    first = strs[0]
    last = strs[-1]
    res = ""
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]: break
        res += first[i]
    return res"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef longestCommonPrefix(strs):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip().split()\n    print(longestCommonPrefix(data))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nstring longestCommonPrefix(vector<string>& strs) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    string s;\n    vector<string> strs;\n    while (cin >> s) strs.push_back(s);\n    cout << longestCommonPrefix(strs) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static String longestCommonPrefix(String[] strs) {\n        // User logic\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<String> list = new ArrayList<>();\n        while (sc.hasNext()) {\n            list.add(sc.next());\n        }\n        String[] strs = list.toArray(new String[0]);\n        System.out.println(longestCommonPrefix(strs));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction longestCommonPrefix(strs) {\n    // User logic\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    console.log(longestCommonPrefix(input));\n} else {\n    console.log(longestCommonPrefix([]));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* longestCommonPrefix(char** strs, int strsSize) {\n    // User logic\n    return \"\"; \n}\n\nint main() {\n    char s[205];\n    char* strs[205];\n    int size = 0;\n    while (scanf(\"%204s\", s) == 1 && size < 205) {\n        strs[size] = strdup(s);\n        size++;\n    }\n    char* res = longestCommonPrefix(strs, size);\n    printf(\"%s\\n\", res ? res : \"\");\n    // Assume memory managed by user or OS\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "flower flow flight", "expected_output": "fl", "is_sample": True},
        {"input": "dog racecar car", "expected_output": "", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "interspecies interstellar interstate", "expected_output": "inters", "is_sample": False},
        {"input": "apple ape april", "expected_output": "ap", "is_sample": False},
        {"input": "a", "expected_output": "a", "is_sample": False},
        {"input": "ab a", "expected_output": "a", "is_sample": False},
        {"input": "throne throne throne", "expected_output": "throne", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(["a" * 200] * 200), "expected_output": "a" * 200, "is_sample": False},
        {"input": " ".join(["a" * 199 + "b"] + ["a" * 200] * 199), "expected_output": "a" * 199, "is_sample": False},
        {"input": " ".join([chr(97 + (i % 26)) for i in range(200)]), "expected_output": "", "is_sample": False}
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
        "topics": ["String", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/14_Longest_Common_Prefix.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
