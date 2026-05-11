import json
import os

def generate_json():
    problem_id = 1002
    title = "Find Common Characters"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1002. Find Common Characters</h3>
<p>Given a string array <code>words</code>, return <em>an array of all characters that show up in all strings within the </em><code>words</code><em> (including duplicates)</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> words = ["bella","label","roller"]
<strong>Output:</strong> ["e","l","l"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> words = ["cool","lock","cook"]
<strong>Output:</strong> ["c","o"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single line containing space-separated strings."
    output_format = "The common characters, space-separated, in any order."
    
    constraints = [
        "1 <= words.length <= 100",
        "1 <= words[i].length <= 100",
        "Lowercase English letters.",
        "O(N * W) time complexity.",
        "O(1) extra space (excluding result)."
    ]
    
    explanation = """To find the common characters appearing in all strings:
1. **The Insight (Frequency Intersection)**:
   - A character is common if it appears in *every* word.
   - For each word, the count of a character in the final result is the *minimum* count of that character across all words.
2. **Algorithm Strategy**:
   - Initialize a frequency array `min_counts` (size 26) with the character counts from the first word.
   - For every subsequent word in `words`:
     - Calculate its character counts in another temporary frequency array (`current_counts`).
     - Update `min_counts[i] = min(min_counts[i], current_counts[i])` for each individual character `i` (from 'a' to 'z').
3. **Conclusion**:
   - For each character from 'a' to 'z', add it to the result list `min_counts[char]` number of times.
4. **Complexity**:
   - Time Complexity: O(N * W), where N is number of words and W is the maximum length of a word.
   - Space Complexity: O(1) for frequency arrays (fixed at 26)."""
    
    answer = """def commonChars(words: list[str]) -> list[str]:
    # Initialize counts from the first word
    min_counts = [0] * 26
    for char in words[0]:
        min_counts[ord(char) - ord('a')] += 1
        
    # Update with subsequent words
    for i in range(1, len(words)):
        current_counts = [0] * 26
        for char in words[i]:
            current_counts[ord(char) - ord('a')] += 1
        for j in range(26):
            min_counts[j] = min(min_counts[j], current_counts[j])
            
    # Collect results
    res = []
    for i in range(26):
        for _ in range(min_counts[i]):
            res.append(chr(i + ord('a')))
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef commonChars(words):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        words = line.split()\n        ans = commonChars(words)\n        print(\" \".join(ans))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nvector<string> commonChars(vector<string>& words) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<String> commonChars(String[] words) {\n        // User logic\n        return new ArrayList<>();\n    }\n}",
        "javascript": "function commonChars(words) {\n    // User logic\n}",
        "c": "char** commonChars(char** words, int wordsSize, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "bella label roller", "expected_output": "e l l", "is_sample": True},
        {"input": "cool lock cook", "expected_output": "c o", "is_sample": True},
        {"input": "abc bcd cde", "expected_output": "c", "is_sample": False},
        {"input": "aaaa aaaa aaaa", "expected_output": "a a a a", "is_sample": False},
        {"input": "xyz abc", "expected_output": "", "is_sample": False},
        {"input": "apple pear plum", "expected_output": "p", "is_sample": False},
        {"input": "dog cat bird", "expected_output": "", "is_sample": False},
        {"input": "common common common", "expected_output": "c o m m o n", "is_sample": False},
        # Stress cases
        {"input": " ".join(["abcdefghijklmnopqrstuvwxyz"] * 100), "expected_output": "a b c d e f g h i j k l m n o p q r s t u v w x y z", "is_sample": False},
        {"input": " ".join(["a" * 100] * 100), "expected_output": " ".join(["a"]*100), "is_sample": False}
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
        "topics": ["Array", "Hash Table", "String"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1002_Find_Common_Characters.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
