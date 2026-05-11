import json
import os

def generate_json():
    problem_id = 409
    title = "Longest Palindrome"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>409. Longest Palindrome</h3>
<p>Given a string <code>s</code> which consists of lowercase or uppercase English letters, return <em>the length of the longest <strong>palindrome</strong></em>&nbsp;that can be built with those letters.</p>

<p>Letters are <strong>case sensitive</strong>, for example,&nbsp;<code>"Aa"</code> is not considered a palindrome here.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abccccdd"
<strong>Output:</strong> 7
<strong>Explanation:</strong> One longest palindrome that can be built is "dccaccd", whose length is 7.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The longest palindrome that can be built is "a", whose length is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of lowercase <b>and/or</b> uppercase English letters.</li>
</ul>"""

    input_format = "A string `s`."
    output_format = "Length of the longest palindrome."
    
    constraints = [
        "1 <= s.length <= 2000",
        "Uppercase and lowercase are distinct."
    ]
    
    explanation = """To build the longest palindrome from a set of characters, we only care about their frequencies.

### Key Observation:
- Any character that appears an **even** number of times (say $2n$) can be fully used in a palindrome (placed $n$ on the left and $n$ on the right).
- Any character that appears an **odd** number of times (say $2n+1$) can contribute $2n$ characters to the symmetry.
- If there is at least one character with an odd frequency, we can pick **one** such character to be the center of the palindrome.

### Algorithm Steps:
1. **Count Frequencies**: Count all characters in the string $s$.
2. **Calculate Length**:
   - `total_length = 0`
   - For each character frequency `count`:
     - `total_length += (count // 2) * 2` (Add the largest even part)
3. **Handle the Center**:
   - If `total_length` is less than `len(s)`, it means there was at least one odd count available. Add $1$ for the center element.
4. **Return**: `total_length`.

### Complexity Analysis:
- **Time Complexity**: $O(N)$, where $N$ is the length of the string.
- **Space Complexity**: $O(1)$ extra space, as the character set is limited (52 characters for lowercase and uppercase English)."""
    
    answer = """class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        res = 0
        odd_found = False
        for char in counts:
            res += (counts[char] // 2) * 2
            if counts[char] % 2 == 1:
                odd_found = True
                
        return res + 1 if odd_found else res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def longestPalindrome(self, s: str) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        s = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.longestPalindrome(s)))",
        "cpp": "class Solution {\npublic:\n    int longestPalindrome(string s) {\n        // Your logic here\n        return 0;\n    }\n};",
        "java": "public class Solution {\n    public int longestPalindrome(String s) {\n        // Your logic here\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {string} s\n * @return {number}\n */\nvar longestPalindrome = function(s) {\n    // Your logic here\n};",
        "c": "int longestPalindrome(char* s) {\n    // Your logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": '"abccccdd"', "expected_output": "7", "is_sample": True},
        {"input": '"a"', "expected_output": "1", "is_sample": True},
        {"input": '"Aa"', "expected_output": "1", "is_sample": False},
        {"input": '"aa"', "expected_output": "2", "is_sample": False},
        {"input": '"aaaa"', "expected_output": "4", "is_sample": False},
        {"input": '"bbccaa"', "expected_output": "6", "is_sample": False},
        {"input": '"abcde"', "expected_output": "1", "is_sample": False},
        {"input": '"ababa"', "expected_output": "5", "is_sample": False},
        # Stress cases
        {"input": '"a"*2000', "expected_output": "2000", "is_sample": False},
        {"input": '"a"*1000 + "b"*1000', "expected_output": "2000", "is_sample": False},
        {"input": '"a"*1999 + "b"', "expected_output": "1999", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Greedy"],
        "companyIndex": 1
    }

    output_path = "301-500/409_Longest_Palindrome.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
