import json
import os

def generate_json():
    problem_id = 30
    title = "Substring with Concatenation of All Words"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>30. Substring with Concatenation of All Words</h3>
<p>You are given a string <code>s</code> and an array of strings <code>words</code>. All the strings of <code>words</code> are of the <strong>same length</strong>.</p>

<p>A <strong>concatenated substring</strong> in <code>s</code> is a substring that contains all the strings of any permutation of <code>words</code> concatenated.</p>

<ul>
	<li>For example, if <code>words = ["ab","cd","ef"]</code>, then <code>"abcdef"</code>, <code>"abefcd"</code>, <code>"cdabef"</code>, <code>"cdefab"</code>, <code>"efabcd"</code>, and <code>"efcdab"</code> are all concatenated strings. <code>"acdbef"</code> is not a concatenated substring because it is not the concatenation of any permutation of <code>words</code>.</li>
</ul>

<p>Return <em>the starting indices of all the concatenated substrings in </em><code>s</code>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "barfoothefoobarman", words = ["foo","bar"]
<strong>Output:</strong> [0,9]
<strong>Explanation:</strong> 
- Substring starting at index 0 is "barfoo". Concatenation of ["bar","foo"] which is a permutation of words.
- Substring starting at index 9 is "foobar". Concatenation of ["foo","bar"] which is a permutation of words.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "wordgoodgoodgoodword", words = ["word","good","best","word"]
<strong>Output:</strong> []
<strong>Explanation:</strong> Since words.length == 4 and words[i].length == 4, the concatenated substring prefix has to be of length 16. There is no such substring in s.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "barfoobarthefoobarman", words = ["bar","foo","the"]
<strong>Output:</strong> [6,9,12]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words.length &lt;= 5000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li><code>s</code> and <code>words[i]</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "A string s and an array of same-length words."
    output_format = "An array of starting indices of all concatenated substrings."
    
    constraints = [
        "1 <= s.length <= 10^4",
        "1 <= words.length <= 5000",
        "1 <= words[i].length <= 30",
        "Same length words"
    ]
    
    explanation = """To find indices of all concatenated substrings:
1. **Parameters**: Let $L$ be the length of each word and $C$ be the number of words. The total substring length is $L \times C$.
2. **Strategy**: Since all words are length $L$, we can break the search into $L$ separate sliding window passes. Each pass starts at an offset $i \in [0, L-1]$.
3. **Sliding Window**:
   - For each offset $i$, move a window of size $L \times C$ in steps of size $L$.
   - Maintain a frequency map `current_counts` of words inside the sliding window.
   - If a word at the head is not in `words`, reset the window.
   - If a word count exceeds the expected count in `word_counts`, shrink the window from the left until count is acceptable.
   - When the window contains exactly $C$ words, record the starting index.
4. **Complexity**:
   - There are $L$ passes.
   - Each pass scans the string of length $N$ exactly once.
   - **Time**: $O(N)$ (independent of $L$ because total steps across all passes is $N$).
   - **Space**: $O(C \times L)$ to store the frequency map."""
    
    answer = """from collections import Counter

def findSubstring(s, words):
    if not s or not words: return []
    
    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_counts = Counter(words)
    res = []
    
    for i in range(word_len):
        left = i
        right = i
        curr_counts = Counter()
        count = 0
        
        while right + word_len <= len(s):
            word = s[right : right + word_len]
            right += word_len
            
            if word in word_counts:
                curr_counts[word] += 1
                count += 1
                
                while curr_counts[word] > word_counts[word]:
                    left_word = s[left : left + word_len]
                    curr_counts[left_word] -= 1
                    count -= 1
                    left += word_len
                
                if count == num_words:
                    res.append(left)
            else:
                curr_counts.clear()
                count = 0
                left = right
                
    return res"""

    boilerplate = {
        "python": "import sys, json\nfrom collections import Counter\n\ndef findSubstring(s, words):\n    # implementation\n    pass\n\nif __name__ == '__main__':\n    data = json.loads(sys.stdin.read())\n    print(findSubstring(data['s'], data['words']))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> findSubstring(string s, vector<string>& words) {\n        // implementation\n        return {};\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<Integer> findSubstring(String s, String[] words) {\n        // implementation\n        return new ArrayList<>();\n    }\n}",
        "javascript": "/**\n * @param {string} s\n * @param {string[]} words\n * @return {number[]}\n */\nvar findSubstring = function(s, words) {\n    \n};",
        "c": "/**\n * Note: The returned array must be malloced, assume caller calls free().\n */\nint* findSubstring(char* s, char** words, int wordsSize, int* returnSize){\n    \n}"
    }

    test_cases = [
        {"input": '{"s": "barfoothefoobarman", "words": ["foo","bar"]}', "expected_output": "[0,9]", "is_sample": True},
        {"input": '{"s": "wordgoodgoodgoodword", "words": ["word","good","best","word"]}', "expected_output": "[]", "is_sample": True},
        {"input": '{"s": "barfoobarthefoobarman", "words": ["bar","foo","the"]}', "expected_output": "[6,9,12]", "is_sample": True},
        {"input": '{"s": "a", "words": ["a"]}', "expected_output": "[0]", "is_sample": False},
        {"input": '{"s": "ab", "words": ["a", "b"]}', "expected_output": "[0]", "is_sample": False},
        {"input": '{"s": "aaaaa", "words": ["a", "a"]}', "expected_output": "[0,1,2,3]", "is_sample": False},
        {"input": '{"s": "foobarfoobar", "words": ["foo", "bar"]}', "expected_output": "[0,3,6]", "is_sample": False},
        {"input": '{"s": "catbatcat", "words": ["cat", "bat"]}', "expected_output": "[0,3]", "is_sample": False},
        {"input": '{"s": "abcdef", "words": ["abc", "def"]}', "expected_output": "[0]", "is_sample": False},
        {"input": '{"s": "linglingmindrinkmy", "words": ["ling","mind"]}', "expected_output": "[0,4]", "is_sample": False}
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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Hash Table", "String", "Sliding Window"],
        "companyIndex": 0
    }

    output_path = "1-100/30_Substring_with_Concatenation_of_All_Words.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
