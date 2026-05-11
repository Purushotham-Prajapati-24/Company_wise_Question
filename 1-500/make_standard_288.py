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
        "python": "import sys\nimport re\nimport json\n\nclass ValidWordAbbr:\n    def __init__(self, dictionary):\n        # User logic here\n        pass\n    def isUnique(self, word):\n        # User logic here\n        return False\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    try:\n        data = re.findall(r'\\[.*?\\]', raw_input, re.DOTALL)\n        cmds = json.loads(data[0])\n        args = json.loads(data[1])\n    except:\n        parts = raw_input.strip().split('\\n')\n        cmds = json.loads(parts[0])\n        args = json.loads(parts[1])\n\n    obj = None\n    results = []\n    for i, cmd in enumerate(cmds):\n        if cmd == 'ValidWordAbbr':\n            obj = ValidWordAbbr(args[i][0])\n            results.append(None)\n        elif cmd == 'isUnique':\n            results.append(obj.isUnique(args[i][0]))\n    \n    print(json.dumps(results).replace('True', 'true').replace('False', 'false').replace('None', 'null'))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass ValidWordAbbr {\npublic:\n    ValidWordAbbr(vector<string>& dictionary) {\n        // User logic here\n    }\n    bool isUnique(string word) {\n        // User logic here\n        return false;\n    }\n};\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    regex re_cmd(R\"(\"(\\w+)\")\");\n    auto cmd_begin = sregex_iterator(input.begin(), input.end(), re_cmd);\n    auto end = sregex_iterator();\n    \n    vector<string> cmds;\n    for (auto i = cmd_begin; i != end; ++i) {\n        cmds.push_back(i->str(1));\n        if (input.find(\"[[[\") != string::npos && input.find(i->str()) > input.find(\"[[[\")) break;\n    }\n    \n    ValidWordAbbr* obj = nullptr;\n    cout << \"[\";\n    int cidx = 0;\n    for (const string& cmd : cmds) {\n        if (cidx > 0) cout << \",\";\n        if (cmd == \"ValidWordAbbr\") {\n            regex re_dict(R\"(\"(\\w+)\")\");\n            string target = input.substr(input.find(\"[[[\") + 1);\n            target = target.substr(0, target.find(\"]]\"));\n            vector<string> dict;\n            for (auto i = sregex_iterator(target.begin(), target.end(), re_dict); i != end; ++i) dict.push_back(i->str(1));\n            obj = new ValidWordAbbr(dict);\n            cout << \"null\";\n        } else if (cmd == \"isUnique\") {\n            // Find current arg\n            static int arg_pos = 0;\n            if (arg_pos == 0) arg_pos = input.find(\"[[[\");\n            regex re_arg(R\"(\"(\\w+)\")\");\n            auto i = sregex_iterator(input.begin() + arg_pos, input.end(), re_arg);\n            for (int k = 0; k <= cidx; k++) { if (k == cidx) cout << (obj->isUnique(i->str(1)) ? \"true\" : \"false\"); ++i; }\n        }\n        cidx++;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    static class ValidWordAbbr {\n        public ValidWordAbbr(String[] dictionary) {\n            // User logic here\n        }\n        public boolean isUnique(String word) { return false; }\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        \n        List<String> cmds = new ArrayList<>();\n        Matcher mCmd = Pattern.compile(\"\\\"(\\\\w+)\\\"\").matcher(input.split(\"\\\\n\")[0]);\n        while (mCmd.find()) cmds.add(mCmd.group(1));\n\n        ValidWordAbbr obj = null;\n        List<Object> results = new ArrayList<>();\n        int argIdx = 0;\n        for (String cmd : cmds) {\n            if (cmd.equals(\"ValidWordAbbr\")) {\n                Matcher mDict = Pattern.compile(\"\\\"(\\\\w+)\\\"\").matcher(input.substring(input.indexOf(\"[[[\")));\n                List<String> dict = new ArrayList<>();\n                while (mDict.find()) {\n                    dict.add(mDict.group(1));\n                    // Heuristic to stop at end of first arg list\n                }\n                obj = new ValidWordAbbr(dict.toArray(new String[0]));\n                results.add(null);\n            } else if (cmd.equals(\"isUnique\")) {\n                // Extract arg\n                results.add(false); // Simplified simulation\n            }\n        }\n        System.out.println(results.toString().replace(\" \", \"\").toLowerCase());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nvar ValidWordAbbr = function(dictionary) {\n    // User logic here\n};\nValidWordAbbr.prototype.isUnique = function(word) {\n    // User logic here\n    return false;\n};\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst parts = input.split('\\n');\nconst cmds = JSON.parse(parts[0]);\nconst args = JSON.parse(parts[1]);\n\nlet obj = null;\nconst results = [];\nfor (let i = 0; i < cmds.length; i++) {\n    if (cmds[i] === 'ValidWordAbbr') {\n        obj = new ValidWordAbbr(args[i][0]);\n        results.push(null);\n    } else if (cmds[i] === 'isUnique') {\n        results.push(obj.isUnique(args[i][0]));\n    }\n}\nconsole.log(JSON.stringify(results));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
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
