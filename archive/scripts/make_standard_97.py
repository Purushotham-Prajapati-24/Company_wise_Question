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
        "python": "import sys\n\ndef isInterleave(s1, s2, s3):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    # Handle potentially empty lines\n    s1 = lines[0].strip() if len(lines) > 0 else \"\"\n    s2 = lines[1].strip() if len(lines) > 1 else \"\"\n    s3 = lines[2].strip() if len(lines) > 2 else \"\"\n    print(str(isInterleave(s1, s2, s3)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nbool isInterleave(string s1, string s2, string s3) {\n    // User logic\n    return false;\n}\n\nint main() {\n    string s1, s2, s3;\n    getline(cin, s1);\n    getline(cin, s2);\n    getline(cin, s3);\n    if(isInterleave(s1, s2, s3)) cout << \"true\" << endl;\n    else cout << \"false\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isInterleave(String s1, String s2, String s3) {\n        // User logic\n        return false;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String s1 = sc.hasNextLine() ? sc.nextLine() : \"\";\n        String s2 = sc.hasNextLine() ? sc.nextLine() : \"\";\n        String s3 = sc.hasNextLine() ? sc.nextLine() : \"\";\n        System.out.println(isInterleave(s1, s2, s3));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isInterleave(s1, s2, s3) {\n    // User logic\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n').map(s => s.trim());\nconst [s1, s2, s3] = [input[0] || \"\", input[1] || \"\", input[2] || \"\"];\nconsole.log(isInterleave(s1, s2, s3).toString());",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdbool.h>\n\nbool isInterleave(char* s1, char* s2, char* s3) {\n    // User logic\n    return false;\n}\n\nint main() {\n    char s1[201] = \"\", s2[201] = \"\", s3[401] = \"\";\n    if (fgets(s1, sizeof(s1), stdin)) { int l = strlen(s1); if (l > 0 && s1[l-1] == '\\n') s1[l-1] = '\\0'; }\n    if (fgets(s2, sizeof(s2), stdin)) { int l = strlen(s2); if (l > 0 && s2[l-1] == '\\n') s2[l-1] = '\\0'; }\n    if (fgets(s3, sizeof(s3), stdin)) { int l = strlen(s3); if (l > 0 && s3[l-1] == '\\n') s3[l-1] = '\\0'; }\n    printf(\"%s\\n\", isInterleave(s1, s2, s3) ? \"true\" : \"false\");\n    return 0;\n}"
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
