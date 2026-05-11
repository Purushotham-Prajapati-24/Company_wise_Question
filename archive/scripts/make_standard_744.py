import json
import os

def generate_json():
    problem_id = 744
    title = "Find Smallest Letter Greater Than Target"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>744. Find Smallest Letter Greater Than Target</h3>
<p>You are given an array of characters <code>letters</code> that is sorted in <b>non-decreasing order</b>, and a character <code>target</code>. There are <b>at least two different</b> characters in <code>letters</code>.</p>

<p>Return <em>the smallest character in </em><code>letters</code><em> that is lexicographically greater than </em><code>target</code>. If such a character does not exist, return the first character in <code>letters</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> letters = ["c","f","j"], target = "a"
<strong>Output:</strong> "c"
<strong>Explanation:</strong> The smallest character that is lexicographically greater than 'a' in letters is 'c'.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> letters = ["c","f","j"], target = "c"
<strong>Output:</strong> "f"
<strong>Explanation:</strong> The smallest character that is lexicographically greater than 'c' in letters is 'f'.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> letters = ["x","x","y","y"], target = "z"
<strong>Output:</strong> "x"
<strong>Explanation:</strong> There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= letters.length &lt;= 10<sup>4</sup></code></li>
	<li><code>letters[i]</code> is a lowercase English letter.</li>
	<li><code>letters</code> is sorted in <b>non-decreasing order</b>.</li>
	<li><code>letters</code> contains at least two different characters.</li>
	<li><code>target</code> is a lowercase English letter.</li>
</ul>"""

    input_format = "Two lines: 1) Space-separated characters letters 2) Character target."
    output_format = "A single character representing the result."
    
    constraints = [
        "2 <= letters.length <= 10^4",
        "At least two different characters in input.",
        "O(log N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To find the smallest character strictly greater than the target in a sorted array:
1. **The Core Approach (Binary Search)**:
   - Since the array `letters` is already sorted, we can use binary search to find the "upper bound" (the first character `> target`).
2. **Binary Search Logic**:
   - Maintain `low` and `high` pointers.
   - For `mid = low + (high - low) // 2`:
     - If `letters[mid] > target`, the answer could be at `mid` or earlier; set `high = mid`.
     - Otherwise, the answer must be strictly after `mid`; set `low = mid + 1`.
3. **The Result (Wrap-around)**:
   - If after the search, our index points to the end of the array (indicating no element `> target`), return `letters[0]`.
   - Alternatively, use the modulo operator: `return letters[low % len(letters)]`.
4. **Complexity**:
   - Time Complexity: O(log N).
   - Space Complexity: O(1)."""
    
    answer = """def nextGreatestLetter(letters: list[str], target: str) -> str:
    low, high = 0, len(letters)
    while low < high:
        mid = (low + high) // 2
        if letters[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return letters[low % len(letters)]"""

    boilerplate = {
        "python": "import sys\n\ndef nextGreatestLetter(letters, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        letters = lines[0].strip().split()\n        target = lines[1].strip()\n        print(nextGreatestLetter(letters, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nchar nextGreatestLetter(vector<char>& letters, char target) {\n    // User logic\n    return ' ';\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public char nextGreatestLetter(char[] letters, char target) {\n        // User logic\n        return ' ';\n    }\n}",
        "javascript": "function nextGreatestLetter(letters, target) {\n    // User logic\n}",
        "c": "char nextGreatestLetter(char* letters, int lettersSize, char target) {\n    // User logic\n    return ' ';\n}"
    }

    test_cases = [
        {"input": "c f j\\na", "expected_output": "c", "is_sample": True},
        {"input": "c f j\\nc", "expected_output": "f", "is_sample": True},
        {"input": "x x y y\\nz", "expected_output": "x", "is_sample": True},
        {"input": "a b\\nz", "expected_output": "a", "is_sample": False},
        {"input": "a b c\\nb", "expected_output": "c", "is_sample": False},
        {"input": "e e e e n n\\ne", "expected_output": "n", "is_sample": False},
        {"input": "a a a b b b c c c\\na", "expected_output": "b", "is_sample": False},
        {"input": "c f j\\nd", "expected_output": "f", "is_sample": False},
        # Stress cases
        {"input": " ".join(["a"] * 5000 + ["b"] * 5000) + "\\na", "expected_output": "b", "is_sample": False},
        {"input": " ".join(["a"] * 10000) + "\\nz", "expected_output": "a", "is_sample": False}
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
        "topics": ["Array", "Binary Search"],
        "companyIndex": 0
    }

    output_path = "601-800/744_Find_Smallest_Letter_Greater_Than_Target.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
