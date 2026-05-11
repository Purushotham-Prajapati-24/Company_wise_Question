import json
import os

def generate_json():
    problem_id = 211
    title = "Design Add and Search Words Data Structure"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>211. Design Add and Search Words Data Structure</h3>
<p>Design a data structure that supports adding new words and finding if a string matches any previously added string.</p>

<p>Implement the <code>WordDictionary</code> class:</p>

<ul>
	<li><code>WordDictionary()</code>&nbsp;Initializes the object.</li>
	<li><code>void addWord(word)</code> Adds <code>word</code> to the data structure, it can be matched later.</li>
	<li><code>bool search(word)</code>&nbsp;Returns <code>true</code> if there is any string in the data structure that matches <code>word</code>&nbsp;or <code>false</code> otherwise. <code>word</code> may contain dots <code>'.'</code> where dots can be matched with any letter.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
<strong>Output</strong>
[null,null,null,null,false,true,true,true]

<strong>Explanation</strong>
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 25</code></li>
	<li><code>word</code> in <code>addWord</code> consists of lowercase English letters.</li>
	<li><code>word</code> in <code>search</code> consist of <code>'.'</code> or lowercase English letters.</li>
	<li>There will be at most <strong>2 dots</strong> in <code>word</code> for <code>search</code> queries.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>addWord</code> and <code>search</code>.</li>
</ul>"""

    input_format = "Line 1: Command names. Line 2: Arguments for each command."
    output_format = "A list of return values (null for void, true/false for boolean)."
    
    constraints = [
        "word length: [1, 25]",
        "lowercase English letters and dots.",
        "10,000 calls max.",
        "Max 2 dots per search query.",
        "DFS/Recursion likely needed for wildcard support."
    ]
    
    explanation = """To implement a WordDictionary with wildcard support:
1. **Trie Structure**:
   - Use a Trie where each node has a dictionary of children and an `is_word` flag.
2. **`addWord` Method**:
   - Standard Trie insertion. Traverse character by character, creating nodes as needed.
3. **`search` Method (Wildcard Support)**:
   - Use a recursive helper function `match(word_index, node)`.
   - If `word[word_index]` is a character:
     - Check the corresponding child. If it exists, recurse.
   - If `word[word_index]` is a `'.'`:
     - Iterate through **all** existing children of the current node.
     - For each child, recurse: `match(word_index + 1, child)`.
     - If any recursive call returns `true`, return `true`.
4. **Complexity**:
   - Time Complexity:
     - `addWord`: O(L) where L is word length.
     - `search`: O(M^L) in worst-case (many wildcards), but constrained by "max 2 dots" and short word lengths.
   - Space Complexity: O(Total characters) to store the Trie."""
    
    answer = """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            curr = node
            for i in range(idx, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.is_word
            
        return dfs(0, self.root)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass WordDictionary:\n    def __init__(self):\n        pass\n    def addWord(self, word):\n        pass\n    def search(self, word):\n        return False\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        cmds = json.loads(lines[0])\n        args = json.loads(lines[1])\n        res = []\n        obj = None\n        for c, a in zip(cmds, args):\n            if c == \"WordDictionary\":\n                obj = WordDictionary()\n                res.append(\"null\")\n            elif c == \"addWord\":\n                obj.addWord(a[0])\n                res.append(\"null\")\n            elif c == \"search\":\n                res.append(\"true\" if obj.search(a[0]) else \"false\")\n        print(\"[\" + \", \".join(res) + \"]\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nclass WordDictionary {\npublic:\n    WordDictionary() {}\n    void addWord(string word) {}\n    bool search(string word) { return false; }\n};\n\nvector<string> parseStrings(string s) {\n    vector<string> res;\n    s = s.substr(1, s.length() - 2);\n    stringstream ss(s);\n    string item;\n    while (getline(ss, item, ',')) {\n        size_t start = item.find('\"');\n        if (start != string::npos) {\n            size_t end = item.find('\"', start + 1);\n            res.push_back(item.substr(start + 1, end - start - 1));\n        } else {\n            res.push_back(item);\n        }\n    }\n    return res;\n}\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        vector<string> cmds = parseStrings(line1);\n        WordDictionary* obj = nullptr;\n        cout << \"[\";\n        int argIdx = 0;\n        for (int i = 0; i < cmds.size(); i++) {\n            if (cmds[i].find(\"WordDictionary\") != string::npos) {\n                obj = new WordDictionary();\n                cout << \"null\";\n            } else {\n                size_t start = line2.find('\"', argIdx);\n                size_t end = line2.find('\"', start + 1);\n                string word = line2.substr(start + 1, end - start - 1);\n                argIdx = end + 1;\n                if (cmds[i].find(\"addWord\") != string::npos) {\n                    obj->addWord(word);\n                    cout << \"null\";\n                } else if (cmds[i].find(\"search\") != string::npos) {\n                    cout << (obj->search(word) ? \"true\" : \"false\");\n                }\n            }\n            if (i < (int)cmds.size() - 1) cout << \", \";\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass WordDictionary {\n    public WordDictionary() {}\n    public void addWord(String word) {}\n    public boolean search(String word) { return false; }\n}\n\npublic class Solution {\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 == null || line2 == null) return;\n        String[] cmds = line1.substring(1, line1.length() - 1).split(\",\");\n        WordDictionary obj = null;\n        StringBuilder sb = new StringBuilder(\"[\");\n        int argIdx = 0;\n        for (int i = 0; i < cmds.length; i++) {\n            String cmd = cmds[i].trim().replace(\"\\\"\", \"\");\n            if (cmd.equals(\"WordDictionary\")) {\n                obj = new WordDictionary();\n                sb.append(\"null\");\n            } else {\n                int start = line2.indexOf(\"\\\"\", argIdx);\n                int end = line2.indexOf(\"\\\"\", start + 1);\n                String word = line2.substring(start + 1, end);\n                argIdx = end + 1;\n                if (cmd.equals(\"addWord\")) {\n                    obj.addWord(word);\n                    sb.append(\"null\");\n                } else if (cmd.equals(\"search\")) {\n                    sb.append(obj.search(word) ? \"true\" : \"false\");\n                }\n            }\n            if (i < cmds.length - 1) sb.append(\", \");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nvar WordDictionary = function() {};\nWordDictionary.prototype.addWord = function(word) {};\nWordDictionary.prototype.search = function(word) { return false; };\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    const cmds = JSON.parse(input[0]);\n    const args = JSON.parse(input[1]);\n    let obj = null;\n    let res = [];\n    for (let i = 0; i < cmds.length; i++) {\n        if (cmds[i] === \"WordDictionary\") {\n            obj = new WordDictionary();\n            res.push(\"null\");\n        } else if (cmds[i] === \"addWord\") {\n            obj.addWord(args[i][0]);\n            res.push(\"null\");\n        } else if (cmds[i] === \"search\") {\n            res.push(obj.search(args[i][0]) ? \"true\" : \"false\");\n        }\n    }\n    console.log(\"[\" + res.join(\", \") + \"]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\ntypedef struct {} WordDictionary;\nWordDictionary* wordDictionaryCreate() { return NULL; }\nvoid wordDictionaryAddWord(WordDictionary* obj, char* word) {}\nbool wordDictionarySearch(WordDictionary* obj, char* word) { return false; }\nvoid wordDictionaryFree(WordDictionary* obj) {}\n\nint main() {\n    char line1[10000], line2[10000];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        printf(\"[\");\n        char* token = strtok(line1, \"[],\\\" \");\n        WordDictionary* obj = NULL;\n        int argIdx = 0;\n        bool first = true;\n        while (token) {\n            if (!first) printf(\", \");\n            first = false;\n            if (strcmp(token, \"WordDictionary\") == 0) {\n                obj = wordDictionaryCreate();\n                printf(\"null\");\n            } else {\n                while (line2[argIdx] != '\"' && line2[argIdx] != '\\0') argIdx++;\n                if (line2[argIdx] == '\"') {\n                    argIdx++;\n                    int start = argIdx;\n                    while (line2[argIdx] != '\"' && line2[argIdx] != '\\0') argIdx++;\n                    char* word = strndup(line2 + start, argIdx - start);\n                    argIdx++;\n                    if (strcmp(token, \"addWord\") == 0) {\n                        wordDictionaryAddWord(obj, word);\n                        printf(\"null\");\n                    } else if (strcmp(token, \"search\") == 0) {\n                        printf(\"%s\", wordDictionarySearch(obj, word) ? \"true\" : \"false\");\n                    }\n                    free(word);\n                }\n            }\n            token = strtok(NULL, \"[],\\\" \");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]', "expected_output": "[null, null, null, null, false, true, true, true]", "is_sample": True},
        {"input": '["WordDictionary", "addWord", "search"]\\n[[], ["a"], ["."]]', "expected_output": "[null, null, true]", "is_sample": True},
        {"input": '["WordDictionary", "search"]\\n[[], ["a"]]', "expected_output": "[null, false]", "is_sample": False},
        {"input": '["WordDictionary", "addWord", "addWord", "search"]\\n[[], ["abc"], ["def"], ["..."]]', "expected_output": "[null, null, null, true]", "is_sample": False},
        {"input": '["WordDictionary", "addWord", "search"]\\n[[], ["apple"], ["apple"]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["WordDictionary", "addWord", "search"]\\n[[], ["apple"], ["app.."]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["WordDictionary", "addWord", "search"]\\n[[], ["apple"], ["...le"]]', "expected_output": "[null, null, true]", "is_sample": False},
        # Stress cases
        {"input": '["WordDictionary", "addWord", "search"]\\n[[], ["' + 'a'*25 + '"], ["' + 'a'*25 + '"]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["WordDictionary", "addWord", "search"]\\n[[], ["' + 'a'*25 + '"], ["' + '.'*2 + 'a'*23 + '"]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["WordDictionary", "search"]\\n[[], ["' + '.'*25 + '"]]', "expected_output": "[null, false]", "is_sample": False}
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
        "topics": ["String", "Depth-First Search", "Design", "Trie"],
        "companyIndex": 0
    }

    output_path = "1-200/211_Design_Add_and_Search_Words_Data_Structure.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
