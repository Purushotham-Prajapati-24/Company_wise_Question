import json
import os

def generate_json():
    problem_id = 884
    title = "Uncommon Words from Two Sentences"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>884. Uncommon Words from Two Sentences</h3>
<p>A <strong>sentence</strong> is a string of single-space separated words where each word consists only of lowercase letters.</p>

<p>A word is <strong>uncommon</strong> if it appears exactly once in one of the sentences, and <strong>does not appear</strong> in the other sentence.</p>

<p>Given two sentences <code>s1</code> and <code>s2</code>, return <em>a list of all the <strong>uncommon words</strong></em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s1 = "this apple is sweet", s2 = "this apple is sour"
<strong>Output:</strong> ["sweet","sour"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s1 = "apple apple", s2 = "banana"
<strong>Output:</strong> ["banana"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 200</code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters and spaces.</li>
	<li><code>s1</code> and <code>s2</code> do not have leading or trailing spaces.</li>
	<li>All the words in <code>s1</code> and <code>s2</code> are separated by a single space.</li>
</ul>
"""

    input_format = "Two strings s1 and s2."
    output_format = "A list of strings."
    
    constraints = [
        "1 <= s1.length, s2.length <= 200",
        "lowercase and spaces only.",
        "Single space separation."
    ]
    
    explanation = """To find all "uncommon" words:
1. **Simplified Definition**:
   - A word is uncommon if it appears **exactly once** in total across *both* sentences.
   - If a word appears more than once in `s1`, it's not uncommon.
   - If it appears in both `s1` and `s2`, it's not uncommon.
2. **Strategy**:
   - Split both `s1` and `s2` into words and combine them into a single list.
   - Use a frequency map (hash map/counter) to count occurrences of each word.
   - Iterate through the map and collect words with a count of `1`.

Complexity:
- Time: O(L1 + L2) where L are string lengths.
- Space: O(W) where W is the number of words."""
    
    answer = """import collections

def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    count = collections.Counter(s1.split())
    count += collections.Counter(s2.split())
    
    return [word for word in count if count[word] == 1]"""

    boilerplate = {
        "python": "import sys\n\ndef uncommonFromSentences(s1, s2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        print(uncommonFromSentences(lines[0].strip(), lines[1].strip()))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n#include <sstream>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<string> uncommonFromSentences(string s1, string s2) {\n        return {};\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public String[] uncommonFromSentences(String s1, String s2) {\n        return new String[0];\n    }\n}",
        "javascript": "var uncommonFromSentences = function(s1, s2) {\n    return [];\n};",
        "c": "char ** uncommonFromSentences(char * s1, char * s2, int* returnSize){\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "this apple is sweet\\nthis apple is sour", "expected_output": ["sweet","sour"], "is_sample": True},
        {"input": "apple apple\\nbanana", "expected_output": ["banana"], "is_sample": True},
        # Diverse cases
        {"input": "a b c\\na b c", "expected_output": [], "is_sample": False},
        {"input": "hello hello hello\\nworld", "expected_output": ["world"], "is_sample": False},
        {"input": "one two three\\nfour five six", "expected_output": ["one", "two", "three", "four", "five", "six"], "is_sample": False},
        {"input": "a\\nb", "expected_output": ["a", "b"], "is_sample": False},
        {"input": "a b\\na c", "expected_output": ["b", "c"], "is_sample": False},
        {"input": "apple juice\\napple", "expected_output": ["juice"], "is_sample": False},
        # Stress cases
        {"input": " ".join(["word"]*100) + "\\nword", "expected_output": [], "is_sample": False},
        {"input": " ".join(["a", "b"]*50) + "\\n" + " ".join(["c", "d"]*50), "expected_output": [], "is_sample": False}
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
        "topics": ["Hash Table", "String"],
        "companyIndex": 0
    }

    output_path = "801-1000/884_Uncommon_Words_from_Two_Sentences.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
