import json
import os

def generate_json():
    problem_id = 758
    title = "Bold Words in String"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>758. Bold Words in String</h3>
<p>Given a set of keywords <code>words</code> and a string <code>s</code>, make all appearances of all keywords in <code>s</code> bold. Any letters between <code>&lt;b&gt;</code> and <code>&lt;/b&gt;</code> tags become bold.</p>

<p>The resulting string should use the least number of tags possible, and of course the tags should form a valid combination.</p>

<p>For example, given <code>words = ["ab", "bc"]</code> and <code>s = "aabcd"</code>, we should return <code>"a&lt;b&gt;abc&lt;/b&gt;d"</code>. Note that returning <code>"a&lt;b&gt;ab&lt;/b&gt;&lt;b&gt;bc&lt;/b&gt;d"</code> would use more tags, so it is incorrect.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["ab","bc"], s = "aabcd"
<strong>Output:</strong> "a&lt;b&gt;abc&lt;/b&gt;d"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["ab","cb"], s = "aabcd"
<strong>Output:</strong> "a&lt;b&gt;ab&lt;/b&gt;cd"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>0 &lt;= words.length &lt;= 50</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>s</code> and <code>words[i]</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/add-bold-tag-in-string/" target="_blank">616. Add Bold Tag in String</a>."""

    input_format = "A list of strings `words` and a string `s`."
    output_format = "A string with HTML bold tags inserted."
    
    constraints = [
        "1 <= s.length <= 500",
        "0 <= words.length <= 50",
        "1 <= words[i].length <= 10"
    ]
    
    explanation = """To bold the occurrences of words in the string `s`:
1. **Masking Strategy**:
   - Create a boolean mask `is_bold` of size `len(s)` initialized to `False`.
2. **Algorithm**:
   - For each word in `words`:
     - Find all its occurrences in `s`.
     - For each occurrence from index `i` to `i + len(word)`, mark `is_bold[j] = True`.
3. **Merging and Tagging**:
   - Iterate through the boolean mask `is_bold`.
   - Identify contiguous segments of `True`.
   - Wrap these segments with `<b>` and `</b>` tags.
   - If `is_bold[i]` is `True` and `is_bold[i-1]` was `False` (or it's the start), insert `<b>`.
   - If `is_bold[i]` is `True` and `is_bold[i+1]` is `False` (or it's the end), insert `</b>`.
4. **Complexity Analysis**:
   - Time: O(S * W * L) where S is string length, W is number of words, and L is max word length.
   - Space: O(S) for the mask."""
    
    answer = """class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        n = len(s)
        is_bold = [False] * n
        
        # 1. Mark occurrences
        for word in words:
            start = 0
            while True:
                idx = s.find(word, start)
                if idx == -1: break
                for k in range(idx, idx + len(word)):
                    is_bold[k] = True
                start = idx + 1
                
        # 2. Build result with tags
        res = []
        for i in range(n):
            # Check if bold segment starts here
            if is_bold[i] and (i == 0 or not is_bold[i-1]):
                res.append("<b>")
            
            res.append(s[i])
            
            # Check if bold segment ends here
            if is_bold[i] and (i == n-1 or not is_bold[i+1]):
                res.append("</b>")
                
        return "".join(res)"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef boldWords(words, s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Handle input conversion\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\nusing namespace std;\n\nstring boldWords(vector<string>& words, string s) {\n    // User logic here\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public String boldWords(String[] words, String s) {\n        // User logic\n    }\n}",
        "javascript": "/**\n * @param {string[]} words\n * @param {string} s\n * @return {string}\n */\nvar boldWords = function(words, s) {\n    // User logic here\n};",
        "c": "char * boldWords(char ** words, int wordsSize, char * s) {\n    // User logic here\n}"
    }

    test_cases = [
        {"input": '["ab","bc"]\\n"aabcd"', "expected_output": '"a<b>abc</b>d"', "is_sample": True},
        {"input": '["ab","cb"]\\n"aabcd"', "expected_output": '"a<b>ab</b>cd"', "is_sample": True},
        {"input": '[]\\n"hello"', "expected_output": '"hello"', "is_sample": False},
        {"input": '["h", "e", "l", "o"]\\n"hello"', "expected_output": '"<b>hello</b>"', "is_sample": False},
        {"input": '["hello"]\\n"hello"', "expected_output": '"<b>hello</b>"', "is_sample": False},
        {"input": '["aa", "aa"]\\n"aaa"', "expected_output": '"<b>aaa</b>"', "is_sample": False},
        {"input": '["cc", "aa"]\\n"aacc"', "expected_output": '"<b>aacc</b>"', "is_sample": False},
        {"input": '["abc", "xyz"]\\n"abcdefxyz"', "expected_output": '"<b>abc</b>def<b>xyz</b>"', "is_sample": False},
        # Stress cases
        {"input": '["a"*10 for _ in range(50)]\\n"a"*500', "expected_output": '"<b>' + "a"*500 + '</b>"', "is_sample": False},
        {"input": '["ab" for _ in range(50)]\\n"abab"*100', "expected_output": '"<b>' + "abab"*100 + '</b>"', "is_sample": False},
        {"input": '["1", "2"]\\n"33333"', "expected_output": '"33333"', "is_sample": False}
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
        "topics": ["Array", "Hash Table", "String", "Trie", "String Matching"],
        "companyIndex": 0
    }

    output_path = "601-800/758_Bold_Words_in_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
