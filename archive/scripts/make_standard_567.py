import json
import os

def generate_json():
    problem_id = 567
    title = "Permutation in String"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>567. Permutation in String</h3>
<p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code><em> if </em><code>s2</code><em> contains a permutation of </em><code>s1</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>'s permutations is the substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = "ab", s2 = "eidbaooo"
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 ("ba").
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = "ab", s2 = "eidboaoo"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "Two lines: 1) s1 2) s2."
    output_format = "The string 'true' or 'false'."
    
    constraints = [
        "1 <= s1.length, s2.length <= 10^4",
        "Lowercase English letters only.",
        "O(N) time complexity.",
        "O(1) extra space (fixed alphabet size)."
    ]
    
    explanation = """To check if $s2$ contains a permutation of $s1$:
1. **The Permutation Property**:
   - Two strings are permutations of each other if they have the same character counts.
2. **Sliding Window**:
   - Use a sliding window of size $len(s1)$ over $s2$.
   - Maintain a frequency map for $s1$ and a frequency map for the current window in $s2$.
   - Since the characters are only lowercase English letters, a fixed-size array of 26 integers suffices for both maps.
3. **Optimized Update**:
   - Instead of re-calculating the map for every window position, increment the count for the character entering the window and decrement for the character leaving the window.
   - After each move, compare the two frequency maps. If they are identical, return `true`.
4. **Complexity**:
   - Time Complexity: O(N) where N is the length of $s2$.
   - Space Complexity: O(1) as the maps have a constant size of 26."""
    
    answer = """def checkInclusion(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 > n2: return False
    
    count1 = [0] * 26
    count2 = [0] * 26
    for i in range(n1):
        count1[ord(s1[i]) - ord('a')] += 1
        count2[ord(s2[i]) - ord('a')] += 1
        
    if count1 == count2: return True
    
    for i in range(n1, n2):
        count2[ord(s2[i]) - ord('a')] += 1
        count2[ord(s2[i - n1]) - ord('a')] -= 1
        if count1 == count2:
            return True
            
    return False"""

    boilerplate = {
        "python": "import sys\n\ndef checkInclusion(s1, s2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        print(str(checkInclusion(lines[0].strip(), lines[1].strip())).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nbool checkInclusion(string s1, string s2) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean checkInclusion(String s1, String s2) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function checkInclusion(s1, s2) {\n    // User logic\n}",
        "c": "bool checkInclusion(char* s1, char* s2) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "ab\\neidbaooo", "expected_output": "true", "is_sample": True},
        {"input": "ab\\neidboaoo", "expected_output": "false", "is_sample": True},
        {"input": "adc\\ndcda", "expected_output": "true", "is_sample": False},
        {"input": "hello\\nooolleoooleh", "expected_output": "false", "is_sample": False},
        {"input": "abc\\nabc", "expected_output": "true", "is_sample": False},
        {"input": "abc\\ndef", "expected_output": "false", "is_sample": False},
        {"input": "aaaa\\naaaaa", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "a\\n" + "b" * 10000, "expected_output": "false", "is_sample": False},
        {"input": "abcdefg\\n" + "gfedcba", "expected_output": "true", "is_sample": False},
        {"input": "a" * 5000 + "\\n" + "a" * 10000, "expected_output": "true", "is_sample": False}
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
        "topics": ["Hash Table", "Two Pointers", "String", "Sliding Window"],
        "companyIndex": 0
    }

    output_path = "401-600/567_Permutation_in_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
