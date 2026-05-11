import json
import os

def generate_json():
    problem_id = 555
    title = "Split Concatenated Strings"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>555. Split Concatenated Strings</h3>
<p>You are given a list of strings <code>strs</code>. You can concatenate these strings into a loop, maintaining their relative order. For each individual string, you have the option to either keep it as is or reverse it before concatenating.</p>

<p>After forming a loop, you must "cut" the loop at any position to form a regular (linear) string. Your goal is to find the <strong>lexicographically largest</strong> string possible among all valid cuts.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = ["abc", "xyz"]
<strong>Output:</strong> "zyxcba"
<strong>Explanation:</strong>
Step 1: Decide for each string ("abc", "cba") and ("xyz", "zyx").
To maximize, we choose "cba" and "zyx".
Step 2: Form a loop: "cbazyx".
Step 3: Cut the loop at any position.
The lexicographically largest cut is "zyxcba".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = ["abc"]
<strong>Output:</strong> "cba"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 1000</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 1000</code></li>
	<li><code>1 &lt;= sum(strs[i].length) &lt;= 1000</code></li>
</ul>
"""

    input_format = "A single line containing space-separated strings for 'strs'."
    output_format = "A single string representing the lexicographically largest result."
    
    constraints = [
        "1 <= strs.length <= 1000",
        "1 <= sum(strs[i].length) <= 1000",
        "Lowercase English letters only."
    ]
    
    explanation = """To find the lexicographically largest cut:
1. For each string in `strs`, it's almost always optimal to pick the lexicographically larger of its normal and reversed versions to be in the "middle" of the final cut string.
2. Pre-process all strings by replacing each `s` with `max(s, s[::-1])`.
3. Iterate through each string `strs[i]` as the one where the cut will occur:
   - For `strs[i]`, try all possible cut points in its original version AND its reversed version.
   - For each cut, form the linear string: `suffix + middle_part + prefix`.
   - `middle_part` is the concatenation of the pre-processed version of all subsequent strings, followed by all preceding strings.
4. Keep track of the overall maximum linear string."""
    
    answer = """def splitLoopedString(strs):
    strs = [max(s, s[::-1]) for s in strs]
    ans = ""
    for i, s in enumerate(strs):
        other = "".join(strs[i+1:] + strs[:i])
        for body in (s, s[::-1]):
            for k in range(len(body)):
                ans = max(ans, body[k:] + other + body[:k])
    return ans"""

    boilerplate = {
        "python": "import sys\\n\\ndef splitLoopedString(strs):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    line = sys.stdin.read().strip()\\n    if line:\\n        strs = line.split()\\n        print(splitLoopedString(strs))",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <string>\\n#include <algorithm>\\n\\nusing namespace std;\\n\\nclass Solution { public: string splitLoopedString(vector<string>& strs) { return \"\"; } };",
        "java": "class Solution { public String splitLoopedString(String[] strs) { return \"\"; } }",
        "javascript": "const fs = require('fs');",
        "c": "char* splitLoopedString(char** strs, int strsSize) { }"
    }

    test_cases = [
        {"input": "abc xyz", "expected_output": "zyxcba", "is_sample": True},
        {"input": "abc", "expected_output": "cba", "is_sample": True},
        {"input": "a b c", "expected_output": "cba", "is_sample": False},
        {"input": "apple banana", "expected_output": "plebananaap", "is_sample": False},
        {"input": "ab cd ef", "expected_output": "fecdab", "is_sample": False},
        {"input": "xyz abc", "expected_output": "zyxcba", "is_sample": False},
        {"input": "aaaa bbbb", "expected_output": "bbbbbaaaa", "is_sample": False},
        {"input": "ab ab", "expected_output": "baab", "is_sample": False},
        {"input": "z y x", "expected_output": "zyx", "is_sample": False},
        {"input": "aba bca", "expected_output": "cbabaa", "is_sample": False}
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
        "topics": ["Array", "String", "Greedy"],
        "companyIndex": 0
    }

    output_path = "401-600/555_Split_Concatenated_Strings.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
