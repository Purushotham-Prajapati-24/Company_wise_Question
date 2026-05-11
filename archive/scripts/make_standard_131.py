import json
import os

def generate_json():
    problem_id = 131
    title = "Palindrome Partitioning"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>131. Palindrome Partitioning</h3>
<p>Given a string <code>s</code>, partition <code>s</code> such that every substring of the partition is a <strong>palindrome</strong>. Return <em>all possible palindrome partitioning of </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>"""

    input_format = "A single line containing the string s."
    output_format = "A stringified 2D array representing all valid palindrome partitions."
    
    constraints = [
        "1 <= s.length <= 16",
        "s contains only lowercase English letters."
    ]
    
    explanation = """To find all possible palindrome partitions:
1. **Backtracking**: Use recursion to explore all possible partition points.
2. **Palindrome Check**: For each potential substring, check if it is a palindrome.
3. **Recursive Step**: If a substring is a palindrome, recursively partition the remainder of the string.
4. **Base Case**: If the current index reaches the end of the string, a valid partition has been found; add it to the result list.
5. **Optimization**: Precompute all possible palindromes using a 2D DP table to avoid redundant $O(N)$ checks.
6. **Complexity**:
   - Time Complexity: O(N * 2^N), where N is the length of the string (at most 16). There are $2^{N-1}$ total possible partitions.
   - Space Complexity: O(N^2) for the DP table and O(N) for backtracking recursion stack."""
    
    answer = """class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        
        # Precompute palindrome DP table
        dp = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True
        
        def backtrack(start, path):
            if start == n:
                res.append(list(path))
                return
            
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef partition(s: str):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    if not s: sys.exit()\n    print(json.dumps(partition(s)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\nusing namespace std;\n\nvector<vector<string>> partition(string s) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<String>> partition(String s) {\n        // User logic\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) {\n    }\n}",
        "javascript": "/**\n * @param {string} s\n * @return {string[][]}\n */\nvar partition = function(s) {\n    // User logic\n};",
        "c": "char*** partition(char* s, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "aab", "expected_output": '[["a", "a", "b"], ["aa", "b"]]', "is_sample": True},
        {"input": "a", "expected_output": '[["a"]]', "is_sample": True},
        {"input": "ab", "expected_output": '[["a", "b"]]', "is_sample": False},
        {"input": "aba", "expected_output": '[["a", "b", "a"], ["aba"]]', "is_sample": False},
        {"input": "racecar", "expected_output": '[["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "cec", "a", "r"], ["r", "aceca", "r"], ["racecar"]]', "is_sample": False},
        {"input": "efe", "expected_output": '[["e", "f", "e"], ["efe"]]', "is_sample": False},
        {"input": "cdd", "expected_output": '[["c", "d", "d"], ["c", "dd"]]', "is_sample": False},
        # Stress Tests (N=16)
        {"input": "aaaaaaaaaaaaaaaa", "expected_output": "...", "is_sample": False},
        {"input": "abcdefghijklmnop", "expected_output": '[["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]]', "is_sample": False},
        {"input": "abacaba" * 2 + "ab", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(s):
        r = []
        n = len(s)
        def is_pal(sub): return sub == sub[::-1]
        def bt(st, p):
            if st == n: r.append(list(p)); return
            for ed in range(st + 1, n + 1):
                if is_pal(s[st:ed]):
                    p.append(s[st:ed]); bt(ed, p); p.pop()
        bt(0, [])
        return r

    test_cases[7]["expected_output"] = json.dumps(_solve("a" * 16))
    test_cases[9]["expected_output"] = json.dumps(_solve("abacaba" * 2 + "ab"))

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
        "topics": ["String", "Dynamic Programming", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-200/131_Palindrome_Partitioning.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
