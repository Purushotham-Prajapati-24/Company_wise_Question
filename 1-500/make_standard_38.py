import json
import os

def generate_json():
    problem_id = 38
    title = "Count and Say"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>38. Count and Say</h3>
<p>The <strong>count-and-say</strong> sequence is a sequence of digit strings defined by the recursive formula:</p>

<ul>
	<li><code>countAndSay(1) = "1"</code></li>
	<li><code>countAndSay(n)</code> is the run-length encoding of <code>countAndSay(n - 1)</code>.</li>
</ul>

<p>The <a href="http://en.wikipedia.org/wiki/Run-length_encoding" target="_blank">run-length encoding</a> (RLE) is a string of concatenated 'count-digit' pairs, where each group of consecutive identical digits is replaced by the count of the digit followed by the digit itself. To convert a digit string into RLE, group the identical digits together, then for each group specify the number of digits and the digit.</p>

<p>For example, the run-length encoding of <code>"3322251"</code> is <code>"23321511"</code> (two 3's, three 2's, one 5, and one 1).</p>

<p>Given a positive integer <code>n</code>, return the <code>n<sup>th</sup></code> term of the <strong>count-and-say</strong> sequence.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-input">n = 4</span></p>

<p><strong>Output:</strong> <span class="example-output">"1211"</span></p>

<p><strong>Explanation:</strong></p>

<pre>
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
</pre>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-input">n = 1</span></p>

<p><strong>Output:</strong> <span class="example-output">"1"</span></p>

<p><strong>Explanation:</strong></p>

<p>This is the base case.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 30</code></li>
</ul>
"""

    input_format = "A single integer 'n'."
    output_format = "A string representing the nth term of the count-and-say sequence."
    
    constraints = [
        "1 <= n <= 30"
    ]
    
    explanation = """To generate the nth term of the count-and-say sequence:
1. Start with the base case: term 1 is "1".
2. To find each subsequent term up to n:
   - Perform run-length encoding (RLE) on the previous term.
   - Iterate through the previous string from left to right.
   - For every group of consecutive identical digits:
     - Count the number of digits in the group.
     - Append the count followed by the digit value to a new string.
3. The resulting string after the nth step is the answer.
4. Using an iterative approach avoids recursion depth issues and is efficient for n up to 30.

Time Complexity: O(L) per term, where L is the length of the string. The length grows significantly with n.
Space Complexity: O(L) to store the current and next terms."""
    
    answer = """def countAndSay(n):
    res = "1"
    for _ in range(n - 1):
        next_res = []
        i = 0
        while i < len(res):
            count = 1
            while i + 1 < len(res) and res[i] == res[i + 1]:
                i += 1
                count += 1
            next_res.append(str(count))
            next_res.append(res[i])
            i += 1
        res = "".join(next_res)
    return res"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport re\n\ndef countAndSay(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = re.findall(r'\\d+', data)\n    if nums:\n        print(countAndSay(int(nums[0])))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <regex>\n\nusing namespace std;\n\nstring countAndSay(int n) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    string data;\n    string line;\n    while (getline(cin, line)) data += line + \" \";\n    smatch m;\n    regex e(\"\\\\d+\");\n    if (regex_search(data, m, e)) {\n        cout << countAndSay(stoi(m.str())) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Main {\n    public static String countAndSay(int n) {\n        // User logic here\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        Matcher m = Pattern.compile(\"\\\\d+\").matcher(sb.toString());\n        if (m.find()) {\n            System.out.println(countAndSay(Integer.parseInt(m.group())));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction countAndSay(n) {\n    // User logic here\n    return \"\";\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst match = data.match(/\\d+/);\nif (match) {\n    console.log(countAndSay(parseInt(match[0], 10)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nchar* countAndSay(int n) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    int n;\n    while (scanf(\"%*[^0-9]%d\", &n) == 1 || scanf(\"%d\", &n) == 1) {\n        char* res = countAndSay(n);\n        printf(\"%s\\n\", res);\n        return 0;\n    }\n    return 0;\n}"
    }

    def _countSay(n):
        s = "1"
        for _ in range(n-1):
            next_s = []
            i = 0
            while i < len(s):
                c = 1
                while i + 1 < len(s) and s[i] == s[i+1]:
                    i += 1
                    c += 1
                next_s.append(str(c))
                next_s.append(s[i])
                i += 1
            s = "".join(next_s)
        return s

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "4", "expected_output": "1211", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "2", "expected_output": "11", "is_sample": False},
        {"input": "3", "expected_output": "21", "is_sample": False},
        {"input": "5", "expected_output": "111221", "is_sample": False},
        {"input": "6", "expected_output": "312211", "is_sample": False},
        {"input": "7", "expected_output": "13112221", "is_sample": False},
        # Last three: Stress tests
        {"input": "10", "expected_output": _countSay(10), "is_sample": False},
        {"input": "15", "expected_output": _countSay(15), "is_sample": False},
        {"input": "30", "expected_output": _countSay(30), "is_sample": False}
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
        "topics": ["String"],
        "companyIndex": 0
    }

    output_path = "1-200/38_Count_and_Say.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
