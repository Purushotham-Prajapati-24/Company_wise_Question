import json
import os

def generate_json():
    problem_id = 208
    title = "Implement Trie (Prefix Tree)"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>208. Implement Trie (Prefix Tree)</h3>
<p>A <a href="https://en.wikipedia.org/wiki/Trie" target="_blank"><strong>trie</strong></a> (pronounced as "try") or <strong>prefix tree</strong> is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.</p>

<p>Implement the Trie class:</p>

<ul>
	<li><code>Trie()</code> Initializes the trie object.</li>
	<li><code>void insert(String word)</code> Inserts the string <code>word</code> into the trie.</li>
	<li><code>boolean search(String word)</code> Returns <code>true</code> if the string <code>word</code> is in the trie (i.e., was inserted before), and <code>false</code> otherwise.</li>
	<li><code>boolean startsWith(String prefix)</code> Returns <code>true</code> if there is a previously inserted string <code>word</code> that has the prefix <code>prefix</code>, and <code>false</code> otherwise.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
<strong>Output</strong>
[null, null, true, false, true, null, true]

<strong>Explanation</strong>
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
	<li><code>word</code> and <code>prefix</code> consist only of lowercase English letters.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls in total will be made to <code>insert</code>, <code>search</code>, and <code>startsWith</code>.</li>
</ul>"""

    input_format = "Line 1: Command names. Line 2: String arguments for each command."
    output_format = "A list of return values (null for void, true/false for boolean)."
    
    constraints = [
        "word length: [1, 2000]",
        "lowercase English letters only.",
        "30,000 calls max.",
        "Efficient prefix lookup required."
    ]
    
    explanation = """To implement a Trie (Prefix Tree):
1. **Node Structure**:
   - Each node contains a collection (like a dictionary or fixed-size array) of children nodes.
   - An `is_end` flag marks if a sequence of characters ending at this node forms a complete word.
2. **Method logic**:
   - `insert`: Traverse the trie character by character, creating new nodes if they don't exist. Mark the final node as `is_end = true`.
   - `search`: Traverse the prefix. If any character is missing, return `false`. After the traversal, check if the final node has `is_end = true`.
   - `startsWith`: Traverse the prefix. If the entire prefix can be followed, return `true` regardless of whether the final node marks the end of a word.
3. **Complexity**:
   - Time Complexity: O(L) for each operation, where L is the length of the word/prefix.
   - Space Complexity: O(T) where T is the total number of characters across all words, though nodes are often shared for common prefixes."""
    
    answer = """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True"""

    # Boilerplate with command driver
    boilerplate = {
        "python": "import sys\nimport json\n\nclass Trie:\n    def __init__(self):\n        pass\n    def insert(self, word):\n        pass\n    def search(self, word):\n        return False\n    def startsWith(self, prefix):\n        return False\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        cmds = json.loads(lines[0])\n        args = json.loads(lines[1])\n        res = []\n        obj = None\n        for c, a in zip(cmds, args):\n            if c == \"Trie\":\n                obj = Trie()\n                res.append(\"null\")\n            elif c == \"insert\":\n                obj.insert(a[0])\n                res.append(\"null\")\n            elif c == \"search\":\n                res.append(\"true\" if obj.search(a[0]) else \"false\")\n            elif c == \"startsWith\":\n                res.append(\"true\" if obj.startsWith(a[0]) else \"false\")\n        print(\"[\" + \", \".join(res) + \"]\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nclass Trie {\npublic:\n    Trie() {}\n    void insert(string word) {}\n    bool search(string word) { return false; }\n    bool startsWith(string prefix) { return false; }\n};\n\nvector<string> parseStrings(string s) {\n    vector<string> res;\n    s = s.substr(1, s.length() - 2);\n    stringstream ss(s);\n    string item;\n    while (getline(ss, item, ',')) {\n        size_t start = item.find('\"');\n        if (start != string::npos) {\n            size_t end = item.find('\"', start + 1);\n            res.push_back(item.substr(start + 1, end - start - 1));\n        } else {\n            res.push_back(item);\n        }\n    }\n    return res;\n}\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        vector<string> cmds = parseStrings(line1);\n        // Basic parsing for arguments - in a real scenario this needs to be more robust\n        // For Trie, we know args are either empty or have one string\n        Trie* obj = nullptr;\n        cout << \"[\";\n        int argIdx = 0;\n        for (int i = 0; i < cmds.size(); i++) {\n            if (cmds[i].find(\"Trie\") != string::npos) {\n                obj = new Trie();\n                cout << \"null\";\n            } else {\n                // Extract word from line2\n                size_t start = line2.find('\"', argIdx);\n                size_t end = line2.find('\"', start + 1);\n                string word = line2.substr(start + 1, end - start - 1);\n                argIdx = end + 1;\n                if (cmds[i].find(\"insert\") != string::npos) {\n                    obj->insert(word);\n                    cout << \"null\";\n                } else if (cmds[i].find(\"search\") != string::npos) {\n                    cout << (obj->search(word) ? \"true\" : \"false\");\n                } else if (cmds[i].find(\"startsWith\") != string::npos) {\n                    cout << (obj->startsWith(word) ? \"true\" : \"false\");\n                }\n            }\n            if (i < cmds.size() - 1) cout << \", \";\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass Trie {\n    public Trie() {}\n    public void insert(String word) {}\n    public boolean search(String word) { return false; }\n    public boolean startsWith(String prefix) { return false; }\n}\n\npublic class Solution {\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 == null || line2 == null) return;\n        String[] cmds = line1.substring(1, line1.length() - 1).split(\",\");\n        Trie obj = null;\n        StringBuilder sb = new StringBuilder(\"[\");\n        int argIdx = 0;\n        for (int i = 0; i < cmds.length; i++) {\n            String cmd = cmds[i].trim().replace(\"\\\"\", \"\");\n            if (cmd.equals(\"Trie\")) {\n                obj = new Trie();\n                sb.append(\"null\");\n            } else {\n                int start = line2.indexOf(\"\\\"\", argIdx);\n                int end = line2.indexOf(\"\\\"\", start + 1);\n                String word = line2.substring(start + 1, end);\n                argIdx = end + 1;\n                if (cmd.equals(\"insert\")) {\n                    obj.insert(word);\n                    sb.append(\"null\");\n                } else if (cmd.equals(\"search\")) {\n                    sb.append(obj.search(word) ? \"true\" : \"false\");\n                } else {\n                    sb.append(obj.startsWith(word) ? \"true\" : \"false\");\n                }\n            }\n            if (i < cmds.length - 1) sb.append(\", \");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nvar Trie = function() {};\nTrie.prototype.insert = function(word) {};\nTrie.prototype.search = function(word) { return false; };\nTrie.prototype.startsWith = function(prefix) { return false; };\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    const cmds = JSON.parse(input[0]);\n    const args = JSON.parse(input[1]);\n    let obj = null;\n    let res = [];\n    for (let i = 0; i < cmds.length; i++) {\n        if (cmds[i] === \"Trie\") {\n            obj = new Trie();\n            res.push(\"null\");\n        } else if (cmds[i] === \"insert\") {\n            obj.insert(args[i][0]);\n            res.push(\"null\");\n        } else if (cmds[i] === \"search\") {\n            res.push(obj.search(args[i][0]) ? \"true\" : \"false\");\n        } else if (cmds[i] === \"startsWith\") {\n            res.push(obj.startsWith(args[i][0]) ? \"true\" : \"false\");\n        }\n    }\n    console.log(\"[\" + res.join(\", \") + \"]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\ntypedef struct {} Trie;\nTrie* trieCreate() { return NULL; }\nvoid trieInsert(Trie* obj, char* word) {}\nbool trieSearch(Trie* obj, char* word) { return false; }\nbool trieStartsWith(Trie* obj, char* prefix) { return false; }\nvoid trieFree(Trie* obj) {}\n\nint main() {\n    char line1[10000], line2[10000];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        printf(\"[\");\n        char* token = strtok(line1, \"[],\\\" \");\n        Trie* obj = NULL;\n        int argIdx = 0;\n        bool first = true;\n        while (token) {\n            if (!first) printf(\", \");\n            first = false;\n            if (strcmp(token, \"Trie\") == 0) {\n                obj = trieCreate();\n                printf(\"null\");\n            } else {\n                // Extract word from line2 manually per token\n                while (line2[argIdx] != '\"' && line2[argIdx] != '\\0') argIdx++;\n                if (line2[argIdx] == '\"') {\n                    argIdx++;\n                    int start = argIdx;\n                    while (line2[argIdx] != '\"' && line2[argIdx] != '\\0') argIdx++;\n                    char* word = strndup(line2 + start, argIdx - start);\n                    argIdx++;\n                    if (strcmp(token, \"insert\") == 0) {\n                        trieInsert(obj, word);\n                        printf(\"null\");\n                    } else if (strcmp(token, \"search\") == 0) {\n                        printf(\"%s\", trieSearch(obj, word) ? \"true\" : \"false\");\n                    } else if (strcmp(token, \"startsWith\") == 0) {\n                        printf(\"%s\", trieStartsWith(obj, word) ? \"true\" : \"false\");\n                    }\n                    free(word);\n                }\n            }\n            token = strtok(NULL, \"[],\\\" \");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["Trie", "insert", "search", "search", "startsWith", "insert", "search"]\\n[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]', "expected_output": "[null, null, true, false, true, null, true]", "is_sample": True},
        {"input": '["Trie", "insert", "search", "startsWith"]\\n[[], ["hello"], ["hello"], ["hell"]]', "expected_output": "[null, null, true, true]", "is_sample": True},
        {"input": '["Trie", "startsWith"]\\n[[], ["a"]]', "expected_output": "[null, false]", "is_sample": False},
        {"input": '["Trie", "insert", "search"]\\n[[], ["a"], ["a"]]', "expected_output": "[null, null, true]", "is_sample": False},
        {"input": '["Trie", "insert", "search", "insert", "search"]\\n[[], ["app"], ["app"], ["apple"], ["apple"]]', "expected_output": "[null, null, true, null, true]", "is_sample": False},
        {"input": '["Trie", "search"]\\n[[], ["abc"]]', "expected_output": "[null, false]", "is_sample": False},
        {"input": '["Trie", "insert", "startsWith", "startsWith", "startsWith"]\\n[[], ["hotdog"], ["h"], ["hot"], ["dog"]]', "expected_output": "[null, null, true, true, false]", "is_sample": False},
        # Stress cases
        {"input": '["Trie"] + ["insert"]*10 + ["search"]*10\\n[[]] + [["a"*i] for i in range(1,11)] + [["a"*i] for i in range(1,11)]', "expected_output": "...", "is_sample": False},
        {"input": '["Trie", "insert", "search", "startsWith"]\\n[[], ["longestwordever"], ["longestwordever"], ["longest"]]', "expected_output": "[null, null, true, true]", "is_sample": False},
        {"input": '["Trie", "search"]\\n[[], [""]]', "expected_output": "[null, false]", "is_sample": False}
    ]
    
    # Simple fix for stress case 8 logic (Manually calculate expected list)
    s8_res = ["null"] + ["null"]*10 + ["true"]*10
    test_cases[7]["expected_output"] = "[" + ", ".join(s8_res) + "]"
    test_cases[7]["input"] = '["Trie", ' + ', '.join(['"insert"']*10) + ', ' + ', '.join(['"search"']*10) + ']\\n' + '[[], ' + ', '.join(['["' + 'a'*i + '"]' for i in range(1,11)]) + ', ' + ', '.join(['["' + 'a'*i + '"]' for i in range(1,11)]) + ']'

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

    output_path = "1-200/208_Implement_Trie_Prefix_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
