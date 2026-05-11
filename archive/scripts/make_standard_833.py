import json
import os

def generate_json():
    problem_id = 833
    title = "Find And Replace in String"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>833. Find And Replace in String</h3>
<p>You are given a <strong>0-indexed</strong> string <code>s</code> that you must perform <code>k</code> replacement operations on. The replacement operations are given as three arrays: <code>indices</code>, <code>sources</code>, and <code>targets</code>, all of length <code>k</code>.</p>

<p>To perform the <code>i<sup>th</sup></code> replacement operation:</p>

<ol>
	<li>Check if the <strong>substring</strong> <code>s[indices[i] : indices[i] + sources[i].length()]</code> equals <code>sources[i]</code>.</li>
	<li>If it does not match, <strong>do nothing</strong>.</li>
	<li>If it does match, <strong>replace</strong> that substring with <code>targets[i]</code>.</li>
</ol>

<p>All replacement operations must occur <strong>simultaneously</strong>, meaning the replacement operations should not affect the indexing of each other. The test cases will be generated such that the replacements will <strong>not overlap</strong>.</p>

<ul>
	<li>For example, if <code>s = "abc"</code>, <code>indices = [0, 1]</code>, <code>sources = ["ab","bc"]</code>, the replacement operations overlap, and this case will <strong>not</strong> occur.</li>
</ul>

<p>Return <em>the <strong>resulting string</strong> after performing all replacement operations</em>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters in a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/12/833-ex1.png" style="width: 411px; height: 251px;" />
<pre>
<strong>Input:</strong> s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
<strong>Output:</strong> "eeebffff"
<strong>Explanation:</strong>
"a" occurs at index 0 in s, so it is replaced by "eee".
"cd" occurs at index 2 in s, so it is replaced by "ffff".
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/12/833-ex2-1.png" style="width: 411px; height: 251px;" />
<pre>
<strong>Input:</strong> s = "abcd", indices = [0, 2], sources = ["eee", "cd"], targets = ["ffff", "ee"]
<strong>Output:</strong> "abfee"
<strong>Explanation:</strong>
"eee" does not occur at index 0 in s, so we do nothing.
"cd" occurs at index 2 in s, so it is replaced by "ee".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>k == indices.length == sources.length == targets.length</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>0 &lt;= indices[i] &lt; s.length</code></li>
	<li><code>1 &lt;= sources[i].length, targets[i].length &lt;= 50</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>sources[i]</code> and <code>targets[i]</code> consist of only lowercase English letters.</li>
</ul>"""

    input_format = "A string s, an integer k, k indices, k sources, and k targets."
    output_format = "The modified string."
    
    constraints = ["1 <= s.length <= 1000", "1 <= k <= 100", "Replacements do not overlap."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def findReplaceString(s, indices, sources, targets):
    lookup = {}
    for i, idx in enumerate(indices):
        if s[idx:idx+len(sources[i])] == sources[i]:
            lookup[idx] = (len(sources[i]), targets[i])
    
    res = []
    i = 0
    while i < len(s):
        if i in lookup:
            res.append(lookup[i][1])
            i += lookup[i][0]
        else:
            res.append(s[i])
            i += 1
    return "".join(res)"""

    boilerplate = {
        "python": "import sys\n\ndef findReplaceString(s, indices, sources, targets):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    s = input_data[0] if len(input_data) > 0 else \"\"\n    indices = input_data[1] if len(input_data) > 1 else \"\"\n    sources = input_data[2] if len(input_data) > 2 else \"\"\n    targets = input_data[3] if len(input_data) > 3 else \"\"\n    print(findReplaceString(s, indices, sources, targets))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint findReplaceString(string s, string indices, string sources, string targets) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string s; cin >> s;\n    string indices; cin >> indices;\n    string sources; cin >> sources;\n    string targets; cin >> targets;\n    cout << findReplaceString(s, indices, sources, targets) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
