import json
import os

def generate_json():
    problem_id = 91
    title = "Decode Ways"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>91. Decode Ways</h3>
<p>A message containing letters from <code>A-Z</code> can be <strong>encoded</strong> into numbers using the following mapping:</p>

<pre>
'A' -&gt; "1"
'B' -&gt; "2"
...
'Z' -&gt; "26"
</pre>

<p>To <strong>decode</strong> an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, <code>"11106"</code> can be mapped into:</p>

<ul>
	<li><code>"AAJF"</code> with the grouping <code>(1 1 10 6)</code></li>
	<li><code>"KJF"</code> with the grouping <code>(11 10 6)</code></li>
</ul>

<p>Note that the grouping <code>(1 11 06)</code> is invalid because <code>"06"</code> cannot be mapped into <code>'F'</code> since <code>"6"</code> is different from <code>"06"</code>.</p>

<p>Given a string <code>s</code> containing only digits, return <em>the <strong>number</strong> of ways to <strong>decode</strong> it</em>.</p>

<p>The test cases are generated so that the answer fits in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "12"
<strong>Output:</strong> 2
<strong>Explanation:</strong> "12" could be decoded as "AB" (1 2) or "L" (12).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "226"
<strong>Output:</strong> 3
<strong>Explanation:</strong> "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "06"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> contains only digits and may contain leading zero(s).</li>
</ul>"""

    input_format = "A single line containing the digit string s."
    output_format = "An integer representing the number of ways to decode the message."
    
    constraints = [
        "1 <= s.length <= 100",
        "s contains only digits."
    ]
    
    explanation = """To count the number of ways to decode a digit string:
1. **Dynamic Programming**:
   - Let `dp[i]` be the number of ways to decode the substring `s[:i]`.
   - Base Cases:
     - `dp[0] = 1` (an empty string has one way to be decoded: as nothing).
     - `dp[1] = 1` if `s[0] != '0'`, otherwise 0.
   - For `i` from 2 to `n`:
     - **Check one-digit decoding**: If `s[i-1]` is between '1' and '9', then `dp[i] += dp[i-1]`.
     - **Check two-digit decoding**: If the substring `s[i-2:i]` is between '10' and '26', then `dp[i] += dp[i-2]`.
2. **Complexity**:
   - Time Complexity: O(N) where N is the length of the string.
   - Space Complexity: O(N) for the `dp` array (can be optimized to O(1))."""
    
    answer = """def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        # One-digit decoding
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        
        # Two-digit decoding
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
            
    return dp[n]"""

    boilerplate = {
        "python": "import sys, re\n\nclass Solution:\n    def numDecodings(self, s):\n        # User Logic Here\n        pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    # Lethal: Match within quotes or fallback to first continuous string\n    match = re.search(r'\"(.*?)\"', data)\n    s = match.group(1) if match else data.split()[0] if data.split() else \"\"\n    sol = Solution()\n    print(sol.numDecodings(s))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int numDecodings(string s) {\n        // User Logic Here\n        return 0;\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(\"\\\"(.*?)\\\"\");\n    smatch m;\n    string s;\n    if (regex_search(input, m, rgx)) {\n        s = m[1].str();\n    } else {\n        size_t start = input.find_first_not_of(\" \\t\\n\\r\");\n        size_t end = input.find_first_of(\" \\t\\n\\r\", start);\n        if (start != string::npos) s = input.substr(start, end - start);\n    }\n    Solution sol;\n    cout << sol.numDecodings(s) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int numDecodings(String s) {\n        // User Logic Here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"\\\"(.*?)\\\"\").matcher(input);\n        String s = \"\";\n        if (m.find()) {\n            s = m.group(1);\n        } else {\n            String[] parts = input.trim().split(\"\\\\s+\");\n            if (parts.length > 0) s = parts[0];\n        }\n        System.out.println(new Solution().numDecodings(s));\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {string} s\n * @return {number}\n */\nvar numDecodings = function(s) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    const match = input.match(/\"(.*?)\"/);\n    const s = match ? match[1] : (input.split(/\\s+/)[0] || \"\");\n    console.log(numDecodings(s));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nint numDecodings(char* s) {\n    // User Logic Here\n    return 0;\n}\n\nint main() {\n    char input[1000];\n    if (!fgets(input, 1000, stdin)) return 0;\n    char* s = input;\n    char* start = strchr(input, '\"');\n    if (start) {\n        char* end = strchr(start + 1, '\"');\n        if (end) {\n            *end = '\\0';\n            s = start + 1;\n        }\n    } else {\n        s = strtok(input, \" \\t\\n\\r\");\n    }\n    if (s) printf(\"%d\\n\", numDecodings(s));\n    return 0;\n}"
    }

    def _solve(s):
        if not s or s[0] == '0': return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i-1] != '0': dp[i] += dp[i-1]
            two = int(s[i-2:i])
            if 10 <= two <= 26: dp[i] += dp[i-2]
        return dp[n]

    test_cases = [
        {"input": "12", "expected_output": "2", "is_sample": True},
        {"input": "226", "expected_output": "3", "is_sample": True},
        {"input": "06", "expected_output": "0", "is_sample": True},
        {"input": "10", "expected_output": "1", "is_sample": False},
        {"input": "2101", "expected_output": "1", "is_sample": False},
        {"input": "1111", "expected_output": "5", "is_sample": False},
        {"input": "301", "expected_output": "0", "is_sample": False},
        # Stress cases
        {"input": "1"*30, "expected_output": str(_solve("1"*30)), "is_sample": False},
        {"input": "2"*30, "expected_output": str(_solve("2"*30)), "is_sample": False},
        {"input": "12"*15, "expected_output": str(_solve("12"*15)), "is_sample": False}
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
        "topics": ["String", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1-200/91_Decode_Ways.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
