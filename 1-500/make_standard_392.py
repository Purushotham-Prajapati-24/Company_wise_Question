import json
import os

def generate_json():
    problem_id = 392
    title = "Is Subsequence"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>392. Is Subsequence</h3>
<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code><em> if </em><code>s</code><em> is a <strong>subsequence</strong> of </em><code>t</code><em>, or </em><code>false</code><em> otherwise.</em></p>

<p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>"ace"</code> is a subsequence of <code>"<u>a</u>b<u>c</u>d<u>e</u>"</code> while <code>"aec"</code> is not).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist only of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<b>Follow up:</b> Suppose there are lots of incoming <code>s</code>, say <code>s1, s2, ..., sk</code> where <code>k >= 10<sup>9</sup></code>, and you want to check one by one to see if <code>t</code> has its subsequence. In this scenario, how would you change your code?"""

    input_format = "Two strings `s` and `t`."
    output_format = "A boolean representing if s is a subsequence of t."
    
    constraints = [
        "0 <= s.length <= 100",
        "0 <= t.length <= 10^4",
        "lowercase English letters only."
    ]
    
    explanation = """To check if a string $s$ is a subsequence of $t$, we can use the **Two-Pointer** approach.

### Algorithm Steps:
1. **Initialize**: Set two pointers `i = 0` (for $s$) and `j = 0` (for $t$).
2. **Iterate**:
   - While both pointers are within bounds:
     - If `s[i] == t[j]`: Increment `i`.
     - Always increment `j`.
3. **Result**: If `i` has reached the end of $s$ (`i == len(s)`), return `true`. Otherwise, return `false`.

### Follow-up (Large number of queries):
If we have billions of strings $s$ to check against a fixed $t$, we should **pre-process** $t$:
- Build a map or a 2D array where `pos[char]` is a list of indices where `char` appears in $t$.
- For each character in $s$, perform binary search on the corresponding list to find the first occurrence after the current pointer index.

### Complexity Analysis:
- **Time Complexity**: $O(T)$, where $T$ is the length of string $t$.
- **Space Complexity**: $O(1)$ extra space."""
    
    answer = """class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
            
        # Two pointers i for s and j for t
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)"""

    answer = """class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def isSubsequence(self, s: str, t: str) -> bool:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        s = input_data[0].strip()\n        t = input_data[1].strip()\n        if s.startswith('\"') and s.endswith('\"'): s = s[1:-1]\n        if t.startswith('\"') and t.endswith('\"'): t = t[1:-1]\n        sol = Solution()\n        print(json.dumps(sol.isSubsequence(s, t)))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    bool isSubsequence(string s, string t) {\n        // User logic here\n        return false;\n    }\n};\n\nint main() {\n    string s, t;\n    if (getline(cin, s) && getline(cin, t)) {\n        if (s.size() >= 2 && s.front() == '\"' && s.back() == '\"') s = s.substr(1, s.size() - 2);\n        if (t.size() >= 2 && t.front() == '\"' && t.back() == '\"') t = t.substr(1, t.size() - 2);\n        Solution sol;\n        cout << (sol.isSubsequence(s, t) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public boolean isSubsequence(String s, String t) {\n        // User logic here\n        return false;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine().trim();\n            String t = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n            if (s.startsWith(\"\\\\\\\"\") && s.endsWith(\"\\\\\\\"\")) s = s.substring(1, s.length() - 1);\n            if (t.startsWith(\"\\\\\\\"\") && t.endsWith(\"\\\\\\\"\")) t = t.substring(1, t.length() - 1);\n            Solution sol = new Solution();\n            System.out.println(sol.isSubsequence(s, t));\n        }\n    }\n}",
        "javascript": "var isSubsequence = function(s, t) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').split('\\\\n');\nif (input.length >= 2) {\n    let s = input[0].trim();\n    let t = input[1].trim();\n    if (s.startsWith('\"') && s.endswith('\"')) s = s.slice(1, -1);\n    if (t.startsWith('\"') && t.endswith('\"')) t = t.slice(1, -1);\n    console.log(isSubsequence(s, t));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdbool.h>\n\nbool isSubsequence(char* s, char* t) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    char s[10005], t[1000005];\n    if (fgets(s, 10005, stdin) && fgets(t, 1000005, stdin)) {\n        s[strcspn(s, \"\\\\n\")] = 0;\n        t[strcspn(t, \"\\\\n\")] = 0;\n        char *s_ptr = s, *t_ptr = t;\n        if (s[0] == '\"') { s_ptr++; s[strlen(s)-1] = 0; }\n        if (t[0] == '\"') { t_ptr++; t[strlen(t)-1] = 0; }\n        printf(\"%s\\\\n\", isSubsequence(s_ptr, t_ptr) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "abc\\nahbgdc", "expected_output": "true", "is_sample": True},
        {"input": "axc\\nahbgdc", "expected_output": "false", "is_sample": True},
        # 5 Diverse
        {"input": "\\nahbgdc", "expected_output": "true", "is_sample": False},
        {"input": "abc\\n", "expected_output": "false", "is_sample": False},
        {"input": "aaaaaa\\nbbaaaa", "expected_output": "false", "is_sample": False},
        {"input": "b\\nabc", "expected_output": "true", "is_sample": False},
        {"input": "abc\\nabc", "expected_output": "true", "is_sample": False},
        # 3 Stress
        {"input": "a" * 100 + "\\n" + "a" * 1000, "expected_output": "true", "is_sample": False},
        {"input": "abc" + "\\n" + "x" * 10000, "expected_output": "false", "is_sample": False},
        {"input": "ace\\n" + "abcde", "expected_output": "true", "is_sample": False}
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
        "topics": ["Two Pointers", "String", "Dynamic Programming"],
        "companyIndex": 1
    }

    output_path = "301-500/392_Is_Subsequence.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
