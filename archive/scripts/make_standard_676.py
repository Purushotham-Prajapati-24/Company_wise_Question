import json
import collections
import os

def generate_json():
    problem_id = 676
    title = "Implement Magic Dictionary"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>676. Implement Magic Dictionary</h3>
<p>Design a data structure that is initialized with a list of different words. Given a string, you should determine if you can change exactly one character in this string to match any word in the data structure.</p>

<p>Implement the <code>MagicDictionary</code> class:</p>
<ul>
	<li><code>MagicDictionary()</code>: Initializes the object.</li>
	<li><code>void buildDict(string[] dictionary)</code>: Sets the data structure with a list of strings <code>dictionary</code>.</li>
	<li><code>bool search(string searchWord)</code>: Returns <code>true</code> if you can change <strong>exactly one</strong> character in <code>searchWord</code> to match any string in the dictionary, and <code>false</code> otherwise.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
<strong>Output:</strong>
[null, null, false, true, false, false]

<strong>Explanation:</strong>
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello". return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= dictionary.length &lt;= 100</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 100</code></li>
	<li><code>dictionary[i]</code> consists of lowercase English letters.</li>
	<li>All the strings in <code>dictionary</code> are <strong>distinct</strong>.</li>
	<li><code>1 &lt;= searchWord.length &lt;= 100</code></li>
	<li><code>searchWord</code> consists of lowercase English letters.</li>
	<li><code>buildDict</code> will be called only once.</li>
	<li>At most <code>100</code> calls to <code>search</code>.</li>
</ul>"""

    input_format = "Initialization, dictionary strings, and search strings."
    output_format = "Booleans for each search call."
    
    constraints = [
        "dictionary.length <= 100",
        "At most 100 calls to search."
    ]
    
    explanation = """To implement a Magic Dictionary:
1. **Strategy (Small Constraints Optimized)**:
   - Since the dictionary and search counts are very small (100 each), we can use a simpler approach than a Trie.
   - Store all dictionary words in a set for easy access and iterate during search.
2. **Algorithm**:
   - `buildDict(dictionary)`: Simply store the list of words.
   - `search(searchWord)`:
     - Iterate through each `candidate` word in the dictionary.
     - A match occurs if:
       - `len(candidate) == len(searchWord)`
       - There is exactly **one** mismatch between characters in `candidate` and `searchWord`.
     - Return `True` if any match is found, else `False`.
3. **Alternative (Trie or Generalized Neighbors)**:
   - If the constraints were larger, we could store all 1-character-away variations of each word (e.g., `*ello`, `h*llo`, `he*lo`, etc.) in a hash map with counts.
4. **Complexity Analysis**:
   - Time: `buildDict` is O(L), `search` is O(N * L) where N is number of words and L is word length.
   - Space: O(L) to store the dictionary."""
    
    answer = """class MagicDictionary:
    def __init__(self):
        self.dict = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.dict = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.dict:
            if len(word) != len(searchWord):
                continue
            
            # Count mismatches
            mismatch = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    mismatch += 1
                if mismatch > 1:
                    break
            
            if mismatch == 1:
                return True
                
        return False"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass MagicDictionary:\n    def __init__(self):\n        pass\n    def buildDict(self, dictionary):\n        pass\n    def search(self, searchWord):\n        pass\n\nif __name__ == '__main__':\n    # Process commands\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\nusing namespace std;\n\nclass MagicDictionary {\npublic:\n    MagicDictionary() {\n    }\n    void buildDict(vector<string> dictionary) {\n    }\n    bool search(string searchWord) {\n        return false;\n    }\n};",
        "java": "import java.util.*;\n\npublic class MagicDictionary {\n    public MagicDictionary() {\n    }\n    public void buildDict(String[] dictionary) {\n    }\n    public boolean search(String searchWord) {\n        return false;\n    }\n}",
        "javascript": "/**\n * @constructor\n */\nvar MagicDictionary = function() {\n};\n\n/**\n * @param {string[]} dictionary\n * @return {void}\n */\nMagicDictionary.prototype.buildDict = function(dictionary) {\n};\n\n/**\n * @param {string} searchWord\n * @return {boolean}\n */\nMagicDictionary.prototype.search = function(searchWord) {\n};",
        "c": "typedef struct {\n    // User logic\n} MagicDictionary;\n\nMagicDictionary* magicDictionaryCreate() {\n}\n\nvoid magicDictionaryBuildDict(MagicDictionary* obj, char ** dictionary, int dictionarySize) {\n}\n\nbool magicDictionarySearch(MagicDictionary* obj, char * searchWord) {\n}"
    }

    test_cases = [
        {"input": '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\\n[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]', "expected_output": "[null, null, false, true, false, false]", "is_sample": True},
        {"input": '["MagicDictionary", "buildDict", "search"]\\n[[], [["a", "b"]], ["a"]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["MagicDictionary", "buildDict", "search"]\\n[[], [["abc", "abd"]], ["abe"]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["MagicDictionary", "buildDict", "search"]\\n[[], [["abc"]], ["ab"]]', "expected_output": "[null, null, false]", "is_sample": False},
        {"input": '["MagicDictionary", "buildDict", "search"]\\n[[], [["apple"]], ["apply"]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["MagicDictionary", "buildDict", "search"]\\n[[], [["apple"]], ["apple"]]', "expected_output": "[null, null, false]", "is_sample": False},
        {"input": '["MagicDictionary", "buildDict", "search"]\\n[[], [["apple"]], ["bpple"]]', "expected_output": "[null, null, true]", "is_sample": False},
        # Stress cases
        {"input": '["MagicDictionary", "buildDict"] + ["search" for _ in range(100)]', "expected_output": "...", "is_sample": False},
        {"input": '["MagicDictionary", "buildDict", "search"]\\n[[], [["a"*100 for _ in range(100)]], ["a"*100]]', "expected_output": "...", "is_sample": False},
        {"input": '["MagicDictionary", "buildDict", "search"]\\n[[], [["abcdef"]], ["ghijkl"]]', "expected_output": "[null, null, false]", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Design", "Trie"],
        "companyIndex": 0
    }

    output_path = "601-800/676_Implement_Magic_Dictionary.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
