import json
import os

def generate_json():
    problem_id = 72
    title = "Edit Distance"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>72. Edit Distance</h3>
<p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of operations required to convert <code>word1</code> to <code>word2</code></em>.</p>

<p>You have the following three operations permitted on a word:</p>

<ul>
	<li>Insert a character</li>
	<li>Delete a character</li>
	<li>Replace a character</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = "horse", word2 = "ros"
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace 'h' with 'r')
rorse -&gt; rose (remove 'r')
rose -&gt; ros (remove 'e')
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = "intention", word2 = "execution"
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove 't')
inention -&gt; enention (replace 'i' with 'e')
enention -&gt; exention (replace 'n' with 'x')
exention -&gt; exection (replace 'n' with 'c')
exection -&gt; execution (insert 'u')
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "Two lines, the first containing 'word1' and the second containing 'word2'. (Either line can be empty)."
    output_format = "An integer representing the minimum number of edit operations."
    
    constraints = [
        "0 <= word1.length, word2.length <= 500",
        "word1 and word2 consist of lowercase English letters."
    ]
    
    explanation = """To find the Edit Distance (Levenshtein Distance) between two strings:
1. **Dynamic Programming Setup**: Let `dp[i][j]` be the minimum operations to convert the prefix `word1[0...i-1]` to `word2[0...j-1]`.
2. **Base Cases**:
   - `dp[0][j] = j`: Converting an empty string to a string of length `j` requires `j` insertions.
   - `dp[i][0] = i`: Converting a string of length `i` to an empty string requires `i` deletions.
3. **Recurrence Relation**:
   - If `word1[i-1] == word2[j-1]`: The last characters match, so no new operation is needed. `dp[i][j] = dp[i-1][j-1]`.
   - If they don't match, we take the minimum of three possible operations:
     - `Insert`: `dp[i][j-1] + 1`
     - `Delete`: `dp[i-1][j] + 1`
     - `Replace`: `dp[i-1][j-1] + 1`
4. **Optimization**: Since each state `dp[i][j]` only depends on `dp[i-1][j-1]`, `dp[i-1][j]`, and `dp[i][j-1]`, we can optimize the space complexity from O(M*N) to O(N) using a 1D array.
5. **Complexity**:
   - Time Complexity: O(M * N), where M and N are lengths of `word1` and `word2`.
   - Space Complexity: O(min(M, N)) with space optimization."""
    
    answer = """def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    # Ensure n is the smaller dimension for space optimization
    if m < n:
        word1, word2 = word2, word1
        m, n = n, m
        
    # prev_row represents dp[i-1]
    dp = list(range(n + 1))
    
    for i in range(1, m + 1):
        prev_diag = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if word1[i-1] == word2[j-1]:
                dp[j] = prev_diag
            else:
                # min(Delete, Insert, Replace)
                dp[j] = 1 + min(dp[j], dp[j-1], prev_diag)
            prev_diag = temp
            
    return dp[n]"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef minDistance(word1, word2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    word1 = lines[0].strip() if len(lines) > 0 else \"\"\n    word2 = lines[1].strip() if len(lines) > 1 else \"\"\n    print(minDistance(word1, word2))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nint minDistance(string word1, string word2) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string s1, s2;\n    getline(cin, s1);\n    getline(cin, s2);\n    cout << minDistance(s1, s2) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int minDistance(String word1, String word2) {\n        // User logic\n        return 0;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String s1 = sc.hasNextLine() ? sc.nextLine() : \"\";\n        String s2 = sc.hasNextLine() ? sc.nextLine() : \"\";\n        System.out.println(minDistance(s1, s2));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction minDistance(word1, word2) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nconst s1 = input[0] ? input[0].trim() : \"\";\nconst s2 = input[1] ? input[1].trim() : \"\";\nconsole.log(minDistance(s1, s2));",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nint minDistance(char* word1, char* word2) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char s1[501], s2[501];\n    s1[0] = s2[0] = '\\0';\n    if (fgets(s1, sizeof(s1), stdin)) {\n        int l = strlen(s1); if (l > 0 && s1[l-1] == '\\n') s1[l-1] = '\\0';\n    }\n    if (fgets(s2, sizeof(s2), stdin)) {\n        int l = strlen(s2); if (l > 0 && s2[l-1] == '\\n') s2[l-1] = '\\0';\n    }\n    printf(\"%d\\n\", minDistance(s1, s2));\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "horse\\nros", "expected_output": "3", "is_sample": True},
        {"input": "intention\\nexecution", "expected_output": "5", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "abc\\nabc", "expected_output": "0", "is_sample": False},
        {"input": "\\n", "expected_output": "0", "is_sample": False},
        {"input": "a\\n", "expected_output": "1", "is_sample": False},
        {"input": "\\nb", "expected_output": "1", "is_sample": False},
        {"input": "zoologicoo\\nzoogit", "expected_output": "5", "is_sample": False},
        # Last three: Stress tests
        {"input": "a"*500 + "\\n" + "b"*500, "expected_output": "500", "is_sample": False},
        {"input": "dinitrophenylhydrazine\\nbenzalphenylhydrazone", "expected_output": "7", "is_sample": False},
        {"input": "pneumonoultramicroscopicsilicovolcanoconiosis\\nultramicroscopically", "expected_output": "27", "is_sample": False}
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

    output_path = "1-200/72_Edit_Distance.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
