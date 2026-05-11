import json
import os

def generate_json():
    problem_id = 583
    title = "Delete Operation for Two Strings"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>583. Delete Operation for Two Strings</h3>
<p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of <strong>steps</strong> required to make</em> <code>word1</code> <em>and</em> <code>word2</code> <em>the same</em>.</p>

<p>In one <strong>step</strong>, you can delete exactly one character in either string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> word1 = "sea", word2 = "eat"
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> word1 = "leetcode", word2 = "etco"
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> and <code>word2</code> consist of only lowercase English letters.</li>
</ul>
"""

    input_format = "Two lines: first, word1; second, word2."
    output_format = "A single integer representing the minimum deletions."
    
    constraints = [
        "1 <= word1.length, word2.length <= 500",
        "Lowercase English letters only."
    ]
    
    explanation = """To make two strings the same with minimum deletions:
1. Find the Longest Common Subsequence (LCS) of `word1` and `word2`.
2. The minimum deletions required will be `len(word1) + len(word2) - 2 * LCS`.
3. LCS can be solved using dynamic programming in O(m*n) time."""
    
    answer = """def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    lcs = dp[m][n]
    return m + n - 2 * lcs"""

    boilerplate = {
        "python": "import sys\\n\\ndef minDistance(word1, word2):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    # Custom input handler\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <string>\\n#include <algorithm>\\n\\nusing namespace std;\\n\\nclass Solution { public: int minDistance(string word1, string word2) { return 0; } };",
        "java": "class Solution { public int minDistance(String word1, String word2) { return 0; } }",
        "javascript": "const fs = require('fs');",
        "c": "int minDistance(char* word1, char* word2) { }"
    }

    test_cases = [
        {"input": "sea\\neat", "expected_output": "2", "is_sample": True},
        {"input": "leetcode\\netco", "expected_output": "4", "is_sample": True},
        {"input": "a\\nb", "expected_output": "2", "is_sample": False},
        {"input": "same\\nsame", "expected_output": "0", "is_sample": False},
        {"input": "abc\\ndef", "expected_output": "6", "is_sample": False},
        {"input": "algorithm\\nalgo", "expected_output": "5", "is_sample": False},
        {"input": "intention\\nexecution", "expected_output": "8", "is_sample": False},
        {"input": ("a" * 500) + "\\n" + ("b" * 500), "expected_output": "1000", "is_sample": False},
        {"input": ("abcdefghij" * 50) + "\\n" + ("jihgfedcba" * 50), "expected_output": "900", "is_sample": False},
        {"input": ("abcde" * 100) + "\\n" + ("edcba" * 100), "expected_output": "800", "is_sample": False}
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

    output_path = "401-600/583_Delete_Operation_for_Two_Strings.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
