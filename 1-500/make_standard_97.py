import json
import os

def generate_json():
    problem_id = 97
    title = "Interleaving String"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>97. Interleaving String</h3>
<p>Given strings <code>s1</code>, <code>s2</code>, and <code>s3</code>, find whether <code>s3</code> is formed by an <strong>interleaving</strong> of <code>s1</code> and <code>s2</code>.</p>

<p>An <strong>interleaving</strong> of two strings <code>s</code> and <code>t</code> is a configuration where <code>s</code> and <code>t</code> are divided into <code>n</code> and <code>m</code> substrings respectively, such that:</p>

<ul>
	<li><code>s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub></code></li>
	<li><code>t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub></code></li>
	<li><code>|n - m| &lt;= 1</code></li>
	<li>The <strong>interleaving</strong> is <code>s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ...</code> or <code>t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...</code></li>
</ul>

<p><strong>Note:</strong> <code>a + b</code> is the concatenation of strings <code>a</code> and <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg" style="width: 561px; height: 203px;" />
<pre>
<strong>Input:</strong> s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
<strong>Output:</strong> true
<strong>Explanation:</strong> One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
We can also intercalate s1 and s2 in other ways.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s1 = "", s2 = "", s3 = ""
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>0 &lt;= s3.length &lt;= 200</code></li>
	<li><code>s1</code>, <code>s2</code>, and <code>s3</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it using only <code>O(s2.length)</code> additional memory space? """

    input_format = "Line 1: string s1. Line 2: string s2. Line 3: string s3. (Lines may be empty)."
    output_format = "A boolean (true/false) representing if s3 is an interleaving of s1 and s2."
    
    constraints = [
        "0 <= s1.length, s2.length <= 100",
        "0 <= s3.length <= 200",
        "Strings consist of lowercase English letters."
    ]
    
    explanation = """To determine if s3 is an interleaving of s1 and s2:
1. **Dynamic Programming**:
   - Let `dp[i][j]` be a boolean indicating whether `s3[:i+j]` is an interleaving of `s1[:i]` and `s2[:j]`.
   - Base Case: `dp[0][0] = True` (two empty strings form an empty string).
   - Recursive Transitions:
     - `dp[i][j]` is true if:
       1. `dp[i-1][j]` is true AND `s1[i-1] == s3[i+j-1]` (interleaving by taking a char from s1).
       2. `dp[i][j-1]` is true AND `s2[j-1] == s3[i+j-1]` (interleaving by taking a char from s2).
2. **Memory Optimization**:
   - Since `dp[i][j]` only depends on `dp[i-1][j]` and `dp[i][j-1]`, we can reduce the 2D array to a 1D array of size `len(s2) + 1`.
3. **Complexity**:
   - Time Complexity: O(M * N) where M and N are lengths of s1 and s2.
   - Space Complexity: O(min(M, N)) with optimization."""
    
    answer = """def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
        
    n, m = len(s1), len(s2)
    # Optimization: ensure s2 is the smaller one for O(min(N, M)) space
    if m > n:
        s1, s2 = s2, s1
        n, m = m, n
        
    dp = [False] * (m + 1)
    dp[0] = True
    
    # Initialization for the first row (interleaving with only s2)
    for j in range(1, m + 1):
        dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        
    for i in range(1, n + 1):
        # Update dp[0] for each row (interleaving with only s1)
        dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
        for j in range(1, m + 1):
            dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
            
    return dp[m]"""

    boilerplate = {
        "python": "import sys, re\n\nclass Solution:\n    def isInterleave(self, s1, s2, s3):\n        # User Logic Here\n        pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    # Lethal: Extract 3 strings from quotes or lines\n    matches = re.findall(r'\"(.*?)\"', data)\n    if len(matches) >= 3:\n        s1, s2, s3 = matches[:3]\n    else:\n        lines = data.splitlines()\n        s1 = lines[0].strip() if len(lines) > 0 else \"\"\n        s2 = lines[1].strip() if len(lines) > 1 else \"\"\n        s3 = lines[2].strip() if len(lines) > 2 else \"\"\n    \n    sol = Solution()\n    print(str(sol.isInterleave(s1, s2, s3)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    bool isInterleave(string s1, string s2, string s3) {\n        // User Logic Here\n        return false;\n    }\n};\n\nint main() {\n    string input, line;\n    vector<string> s;\n    while(getline(cin, line)) input += line + \"\\n\";\n    \n    regex rgx(\"\\\"(.*?)\\\"\");\n    auto words_begin = sregex_iterator(input.begin(), input.end(), rgx);\n    auto words_end = sregex_iterator();\n    \n    for (auto i = words_begin; i != words_end && s.size() < 3; ++i) s.push_back((*i)[1].str());\n    \n    if (s.size() < 3) {\n        s.clear();\n        size_t pos = 0, next;\n        while ((next = input.find('\\n', pos)) != string::npos && s.size() < 3) {\n            string row = input.substr(pos, next - pos);\n            size_t first = row.find_first_not_of(\" \\t\\r\");\n            size_t last = row.find_last_not_of(\" \\t\\r\");\n            s.push_back((first == string::npos) ? \"\" : row.substr(first, last - first + 1));\n            pos = next + 1;\n        }\n    }\n    \n    while(s.size() < 3) s.push_back(\"\");\n    \n    Solution sol;\n    cout << (sol.isInterleave(s[0], s[1], s[2]) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public boolean isInterleave(String s1, String s2, String s3) {\n        // User Logic Here\n        return false;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\"\\n\");\n        String input = sb.toString();\n        \n        List<String> s = new ArrayList<>();\n        Matcher m = Pattern.compile(\"\\\"(.*?)\\\"\").matcher(input);\n        while (m.find() && s.size() < 3) s.add(m.group(1));\n        \n        if (s.size() < 3) {\n            s.clear();\n            String[] lines = input.split(\"\\n\");\n            for (int i = 0; i < 3; i++) {\n                s.add(i < lines.length ? lines[i].trim() : \"\");\n            }\n        }\n        \n        System.out.println(new Solution().isInterleave(s.get(0), s.get(1), s.get(2)));\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {string} s1\n * @param {string} s2\n * @param {string} s3\n * @return {boolean}\n */\nvar isInterleave = function(s1, s2, s3) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const matches = input.match(/\"(.*?)\"/g);\n    let s1, s2, s3;\n    if (matches && matches.length >= 3) {\n        [s1, s2, s3] = matches.map(m => m.slice(1, -1));\n    } else {\n        const lines = input.split(/\\r?\\n/);\n        s1 = (lines[0] || \"\").trim();\n        s2 = (lines[1] || \"\").trim();\n        s3 = (lines[2] || \"\").trim();\n    }\n    console.log(isInterleave(s1, s2, s3));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdbool.h>\n#include <stdlib.h>\n\nbool isInterleave(char* s1, char* s2, char* s3) {\n    // User Logic Here\n    return false;\n}\n\nvoid trim(char* str) {\n    char* end = str + strlen(str) - 1;\n    while(end >= str && (*end == '\\n' || *end == '\\r' || *end == ' ')) *end-- = '\\0';\n}\n\nint main() {\n    char s1[1000] = \"\", s2[1000] = \"\", s3[2000] = \"\";\n    if (fgets(s1, 1000, stdin)) trim(s1);\n    if (fgets(s2, 1000, stdin)) trim(s2);\n    if (fgets(s3, 2000, stdin)) trim(s3);\n    printf(\"%s\\n\", isInterleave(s1, s2, s3) ? \"true\" : \"false\");\n    return 0;\n}"
    }

    def _solve(s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
        n, m = len(s1), len(s2)
        dp = [False] * (m + 1)
        dp[0] = True
        for j in range(1, m + 1): dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, n + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, m + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[m]

    test_cases = [
        {"input": "aabcc\ndbbca\naadbbcbcac", "expected_output": "true", "is_sample": True},
        {"input": "aabcc\ndbbca\naadbbbaccc", "expected_output": "false", "is_sample": True},
        {"input": "\n\n", "expected_output": "true", "is_sample": True},
        {"input": "a\nb\nab", "expected_output": "true", "is_sample": False},
        {"input": "a\nb\nba", "expected_output": "true", "is_sample": False},
        {"input": "a\nb\nac", "expected_output": "false", "is_sample": False},
        {"input": "abc\ndef\nabdceg", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": "a"*100 + "\n" + "b"*100 + "\n" + "ab"*100, "expected_output": "true", "is_sample": False},
        {"input": "a"*100 + "\n" + "b"*100 + "\n" + "a"*100 + "b"*100, "expected_output": "true", "is_sample": False},
        {"input": "a"*100 + "\n" + "b"*100 + "\n" + "b"*100 + "a"*100, "expected_output": "true", "is_sample": False}
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
        "topics": ["DP", "String"],
        "companyIndex": 0
    }

    output_path = "1-200/97_Interleaving_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
