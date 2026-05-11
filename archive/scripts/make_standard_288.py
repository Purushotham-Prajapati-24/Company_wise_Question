import json
import collections
import os

def generate_json():
    problem_id = 288
    title = "Unique Word Abbreviation"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>288. Unique Word Abbreviation</h3>
<p>An abbreviation of a word follows the form &lt;first letter&gt;&lt;number of letters in-between&gt;&lt;last letter&gt;. Below are some examples of word abbreviations:</p>

<pre>
a) it                      --&gt; it (no abbreviation)
b) d|og                    --&gt; d1g
c) i|nternationalizatio|n  --&gt; i18n
d) l|ocalizatio|n          --&gt; l10n
</pre>

<p>Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no <strong>other</strong> word from the dictionary has the same abbreviation.</p>

<p>Implement the <code>ValidWordAbbr</code> class:</p>
<ul>
	<li><code>ValidWordAbbr(String[] dictionary)</code> Initializes the object with a <code>dictionary</code> of words.</li>
	<li><code>boolean isUnique(String word)</code> Returns <code>true</code> if the word's abbreviation is unique in the <code>dictionary</code>, and <code>false</code> otherwise.</li>
</ul>

<p>A word's abbreviation is unique if:</p>
<ol>
	<li>There is no word in <code>dictionary</code> such that their abbreviations are equal.</li>
	<li>OR for all words in <code>dictionary</code> such that their abbreviations are equal, then those words are <strong>equal</strong> to <code>word</code>.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
<strong>Output:</strong>
[null, false, true, false, true, true]

<strong>Explanation:</strong>
ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
validWordAbbr.isUnique("dear"); // return false, dictionary word "deer" and "door" have abbreviation "d2r"
validWordAbbr.isUnique("cart"); // return true, no words in the dictionary have abbreviation "c2t"
validWordAbbr.isUnique("cane"); // return false, dictionary word "cake" and "card" have different abbreviation
validWordAbbr.isUnique("make"); // return true, no words in the dictionary have abbreviation "m2e"
validWordAbbr.isUnique("cake"); // return true, because "cake" is already in the dictionary and its abbreviation "c2e" is not shared with other words
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= dictionary.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 20</code></li>
	<li><code>dictionary[i]</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= word.length &lt;= 20</code></li>
	<li><code>word</code> consists of lowercase English letters.</li>
	<li>At most <code>5000</code> calls will be made to <code>isUnique</code>.</li>
</ul>"""

    input_format = "A list of strings for dictionary and a word to check."
    output_format = "A boolean value: true or false."
    
    constraints = [
        "1 <= dictionary.length <= 30,000",
        "At most 5000 calls to isUnique."
    ]
    
    explanation = """To determine if a word's abbreviation is unique within a dictionary:
1. **Abbreviation logic**: A word's abbreviation is formed by taking the first character, the number of characters in between, and the last character. If the word length is <= 2, it's just the word itself.
2. **Pre-processing**: Store the dictionary in a Hash Map. The key is the abbreviation, and the value is a set of unique words in the dictionary that map to that abbreviation.
3. **Uniqueness check**: For a given `word` with abbreviation `abbr`:
   - If `abbr` is not in our Hash Map, it's unique (returns true).
   - If `abbr` is in the map:
     - It's unique only if all words in the set are identical to the query `word`. 
     - This means `len(set) == 1` and the only word in the set is `word`.
4. **Complexity**:
   - Time: O(D * L) for pre-processing (where D is dictionary size and L is word length), and O(L) for each `isUnique` call.
   - Space: O(D * L) to store the dictionary abbreviations."""
    
    answer = """import collections

class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        # 1. Pre-process the dictionary into abbreviations
        self.abbr_map = collections.defaultdict(set)
        for s in dictionary:
            abbr = self.get_abbr(s)
            self.abbr_map[abbr].add(s)

    def isUnique(self, word: str) -> bool:
        # 2. Get the abbreviation of the target word
        abbr = self.get_abbr(word)
        # 3. Apply the uniqueness rules
        # Rule: Unique if abbreviation not in dictionary OR 
        # abbreviation only maps to the query word itself. 
        if abbr not in self.abbr_map:
            return True
        words_in_dict = self.abbr_map[abbr]
        return len(words_in_dict) == 1 and word in words_in_dict

    def get_abbr(self, s):
        if len(s) <= 2:
            return s
        return s[0] + str(len(s) - 2) + s[-1]"""

    boilerplate = {
        "python": "import sys\nimport json\nimport collections\n\nclass ValidWordAbbr:\n    def __init__(self, dictionary):\n        # User logic here\n        pass\n    def isUnique(self, word):\n        # User logic here\n        return False\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        dictionary = json.loads(lines[0])\n        queries = json.loads(lines[1])\n        obj = ValidWordAbbr(dictionary)\n        results = [obj.isUnique(w) for w in queries]\n        print(json.dumps(results))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <unordered_set>\n#include <string>\nusing namespace std;\n\nclass ValidWordAbbr {\npublic:\n    ValidWordAbbr(vector<string>& dictionary) {\n        // User logic here\n    }\n    bool isUnique(string word) {\n        // User logic here\n        return false;\n    }\n};\n\nint main() {\n    // Stub: Requires JSON parsing for full harness\n    cout << \"[]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class ValidWordAbbr {\n    public ValidWordAbbr(String[] dictionary) {\n        // User logic here\n    }\n    public boolean isUnique(String word) {\n        // User logic here\n        return false;\n    }\n    public static void main(String[] args) {\n        System.out.println(\"[]\");\n    }\n}",
        "javascript": "const fs = require('fs');\nconst lines = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nconst dictionary = JSON.parse(lines[0]);\nconst queries = JSON.parse(lines[1]);\n\nvar ValidWordAbbr = function(dictionary) {\n    // User logic here\n};\nValidWordAbbr.prototype.isUnique = function(word) {\n    // User logic here\n    return false;\n};\n\nconst obj = new ValidWordAbbr(dictionary);\nconsole.log(JSON.stringify(queries.map(w => obj.isUnique(w))));",
        "c": "#include <stdio.h>\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": '[["deer", "door", "cake", "card"]]\\n["dear","cart","cane","make","cake"]', "expected_output": "[false, true, false, true, true]", "is_sample": True},
        {"input": '[["it"]]\\n["it"]', "expected_output": "[true]", "is_sample": False},
        {"input": '[["a", "a"]]\\n["a"]', "expected_output": "[true]", "is_sample": False},
        {"input": '[["abc", "abc"]]\\n["abc"]', "expected_output": "[true]", "is_sample": False},
        {"input": '[["hello", "hallo"]]\\n["hello"]', "expected_output": "[false]", "is_sample": False},
        {"input": '[["apple", "pear"]]\\n["banana"]', "expected_output": "[true]", "is_sample": False},
        {"input": '[["longwordabbreviation", "longwordabbreviation"]]\\n["longwordabbreviation"]', "expected_output": "[true]", "is_sample": False},
        # Stress cases
        {"input": '[["word" + str(i) for i in range(1000)]]\\n["word1"]', "expected_output": "[true]", "is_sample": False},
        {"input": '[["a" + "b"*18 + "c" for _ in range(300)] + ["abc"]]\\n["abc"]', "expected_output": "...", "is_sample": False},
        {"input": '[["ab" for _ in range(1000)]]\\n["ab"]', "expected_output": "[true]", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "String", "Design"],
        "companyIndex": 0
    }

    output_path = "201-400/288_Unique_Word_Abbreviation.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
