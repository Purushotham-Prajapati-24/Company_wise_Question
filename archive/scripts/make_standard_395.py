import json
import os

def generate_json():
    problem_id = 395
    title = "Longest Substring with At Least K Repeating Characters"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>395. Longest Substring with At Least K Repeating Characters</h3>
<p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the length of the longest substring of</em> <code>s</code> <em>such that the frequency of each character in this substring is greater than or equal to</em> <code>k</code>.</p>

<p>If no such substring exists, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aaabb", k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest substring is "aaa", as 'a' is repeated 3 times.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "ababbc", k = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A string `s` and an integer `k`."
    output_format = "An integer representing the maximum length."
    
    constraints = [
        "1 <= s.length <= 10,000",
        "1 <= k <= 100,000",
        "Lowercase English letters only."
    ]
    
    explanation = """To find the longest substring where every character appears at least $k$ times, we can use a **Divide and Conquer** approach.

### Key Observation:
- Any character that appears fewer than $k$ times in the current string **cannot** be part of the valid substring.
- Such a character acts as a "barrier." We can split the string by this character and recursively check each chunk.

### Algorithm Steps:
1. **Count Frequencies**: Count all characters in the current string $s$.
2. **Find Splitting Index**: Find the first character whose frequency is less than $k$.
3. **Base Case**: If no such character is found, the entire current string is valid. Return `len(s)`.
4. **Recursive Step**:
   - If a character `c` with `count[c] < k` is found at index `i`:
   - Split the string into substrings using `c` as the delimiter.
   - Return the maximum result from recursively calling the function on each of these substrings.

### Complexity Analysis:
- **Time Complexity**: $O(N \cdot 26)$ or $O(N^2)$ in the worst case (e.g. `abcdefg...` with $k=2$), but in practice $O(N \cdot |\Sigma|)$ where $|\Sigma|=26$.
- **Space Complexity**: $O(N)$ for the recursion stack and substring copies."""
    
    answer = """class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
            
        # Count character frequencies
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Find the first character that acts as a boundary
        for char in count:
            if count[char] < k:
                # Divide and Conquer: split by the invalid character
                res = 0
                for sub in s.split(char):
                    res = max(res, self.longestSubstring(sub, k))
                return res
                
        # If all characters meet the frequency requirement, return the length
        return n"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def longestSubstring(self, s: str, k: int) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        data = json.loads(raw_input)\n        s = data['s']\n        k = data['k']\n        sol = Solution()\n        print(json.dumps(sol.longestSubstring(s, k)))",
        "cpp": "class Solution {\npublic:\n    int longestSubstring(string s, int k) {\n        // Your logic here\n        return 0;\n    }\n};",
        "java": "public class Solution {\n    public int longestSubstring(String s, int k) {\n        // Your logic here\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {string} s\n * @param {number} k\n * @return {number}\n */\nvar longestSubstring = function(s, k) {\n    // Your logic here\n};",
        "c": "int longestSubstring(char* s, int k) {\n    // Your logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": '{"s": "aaabb", "k": 3}', "expected_output": "3", "is_sample": True},
        {"input": '{"s": "ababbc", "k": 2}', "expected_output": "5", "is_sample": True},
        {"input": '{"s": "abc", "k": 2}', "expected_output": "0", "is_sample": False},
        {"input": '{"s": "aaaaa", "k": 5}', "expected_output": "5", "is_sample": False},
        {"input": '{"s": "ababbc", "k": 3}', "expected_output": "0", "is_sample": False},
        {"input": '{"s": "ababacb", "k": 3}', "expected_output": "0", "is_sample": False},
        {"input": '{"s": "weitong", "k": 2}', "expected_output": "0", "is_sample": False},
        # Stress cases
        {"input": '{"s": "a" * 5000 + "b" * 5000, "k": 5000}', "expected_output": "10000", "is_sample": False},
        {"input": '{"s": "a" * 5000 + "c" + "b" * 4999, "k": 5000}', "expected_output": "5000", "is_sample": False},
        {"input": '{"s": "abcd", "k": 1}', "expected_output": "4", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Sliding Window", "Divide and Conquer"],
        "companyIndex": 1
    }

    output_path = "301-500/395_Longest_Substring_with_At_Least_K_Repeating_Characters.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
