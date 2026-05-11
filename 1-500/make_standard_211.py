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
        "python": "import sys\nimport json\n\nclass WordDictionary:\n    def __init__(self):\n        # User logic here\n        pass\n    def addWord(self, word):\n        # User logic here\n        pass\n    def search(self, word):\n        # User logic here\n        return False\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        commands = json.loads(input_data[0])\n        arguments = json.loads(input_data[1])\n        obj = None\n        results = []\n        for cmd, arg in zip(commands, arguments):\n            if cmd == \"WordDictionary\":\n                obj = WordDictionary()\n                results.append(None)\n            elif cmd == \"addWord\":\n                obj.addWord(arg[0])\n                results.append(None)\n            elif cmd == \"search\":\n                results.append(obj.search(arg[0]))\n        print(json.dumps(results).replace('True', 'true').replace('False', 'false').replace('None', 'null'))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nclass WordDictionary {\npublic:\n    WordDictionary() {\n        // User logic here\n    }\n    void addWord(string word) {\n        // User logic here\n    }\n    bool search(string word) {\n        // User logic here\n        return false;\n    }\n};\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        // Basic parsing for commands and arguments\n        vector<string> cmds;\n        size_t pos = 0;\n        while ((pos = line1.find('\"', pos)) != string::npos) {\n            size_t end = line1.find('\"', pos + 1);\n            cmds.push_back(line1.substr(pos + 1, end - pos - 1));\n            pos = end + 1;\n        }\n\n        WordDictionary* obj = nullptr;\n        vector<string> results;\n        size_t argPos = 0;\n        for (const string& cmd : cmds) {\n            if (cmd == \"WordDictionary\") {\n                obj = new WordDictionary();\n                results.push_back(\"null\");\n                argPos = line2.find(']', argPos) + 1;\n            } else if (cmd == \"addWord\") {\n                size_t s = line2.find('\"', argPos);\n                size_t e = line2.find('\"', s + 1);\n                obj->addWord(line2.substr(s + 1, e - s - 1));\n                results.push_back(\"null\");\n                argPos = e + 1;\n            } else if (cmd == \"search\") {\n                size_t s = line2.find('\"', argPos);\n                size_t e = line2.find('\"', s + 1);\n                results.push_back(obj->search(line2.substr(s + 1, e - s - 1)) ? \"true\" : \"false\");\n                argPos = e + 1;\n            }\n        }\n        cout << \"[\";\n        for (int i = 0; i < results.size(); i++) {\n            cout << results[i] << (i == results.size() - 1 ? \"\" : \", \");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass WordDictionary {\n    public WordDictionary() {\n        // User logic here\n    }\n    public void addWord(String word) {\n        // User logic here\n    }\n    public boolean search(String word) {\n        // User logic here\n        return false;\n    }\n}\n\npublic class Solution {\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 == null || line2 == null) return;\n\n        List<String> cmds = new ArrayList<>();\n        int pos = 0;\n        while ((pos = line1.indexOf('\"', pos)) != -1) {\n            int end = line1.indexOf('\"', pos + 1);\n            cmds.add(line1.substring(pos + 1, end));\n            pos = end + 1;\n        }\n\n        WordDictionary obj = null;\n        List<String> results = new ArrayList<>();\n        int argPos = 0;\n        for (String cmd : cmds) {\n            if (cmd.equals(\"WordDictionary\")) {\n                obj = new WordDictionary();\n                results.add(\"null\");\n                argPos = line2.indexOf(']', argPos) + 1;\n            } else {\n                int s = line2.indexOf('\"', argPos);\n                int e = line2.indexOf('\"', s + 1);\n                String word = line2.substring(s + 1, e);\n                if (cmd.equals(\"addWord\")) {\n                    obj.addWord(word);\n                    results.add(\"null\");\n                } else {\n                    results.add(obj.search(word) ? \"true\" : \"false\");\n                }\n                argPos = e + 1;\n            }\n        }\n        System.out.println(\"[\" + String.join(\", \", results) + \"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction WordDictionary() {\n    // User logic here\n}\nWordDictionary.prototype.addWord = function(word) {\n    // User logic here\n};\nWordDictionary.prototype.search = function(word) {\n    // User logic here\n    return false;\n};\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    const cmds = JSON.parse(input[0]);\n    const args = JSON.parse(input[1]);\n    let obj = null;\n    let results = [];\n    for (let i = 0; i < cmds.length; i++) {\n        if (cmds[i] === \"WordDictionary\") {\n            obj = new WordDictionary();\n            results.add(null);\n        } else if (cmds[i] === \"addWord\") {\n            obj.addWord(args[i][0]);\n            results.add(null);\n        } else if (cmds[i] === \"search\") {\n            results.add(obj.search(args[i][0]));\n        }\n    }\n    console.log(JSON.stringify(results).replace(/null/g, 'null'));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\ntypedef struct {\n    // User logic here\n} WordDictionary;\n\nWordDictionary* wordDictionaryCreate() {\n    // User logic here\n    return NULL;\n}\n\nvoid wordDictionaryAddWord(WordDictionary* obj, char* word) {\n    // User logic here\n}\n\nbool wordDictionarySearch(WordDictionary* obj, char* word) {\n    // User logic here\n    return false;\n}\n\nvoid wordDictionaryFree(WordDictionary* obj) {\n    // User logic here\n}\n\nint main() {\n    char line1[10000], line2[10000];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        printf(\"[\");\n        WordDictionary* obj = NULL;\n        int argIdx = 0;\n        bool first = true;\n        char* cmd = strtok(line1, \"[],\\\" \");\n        while (cmd) {\n            if (!first) printf(\", \");\n            first = false;\n            if (strcmp(cmd, \"WordDictionary\") == 0) {\n                obj = wordDictionaryCreate();\n                printf(\"null\");\n            } else {\n                while (line2[argIdx] != '\"' && line2[argIdx] != '\\0') argIdx++;\n                if (line2[argIdx] == '\"') {\n                    argIdx++;\n                    int start = argIdx;\n                    while (line2[argIdx] != '\"' && line2[argIdx] != '\\0') argIdx++;\n                    char word[200];\n                    int len = argIdx - start;\n                    strncpy(word, line2 + start, len);\n                    word[len] = '\\0';\n                    argIdx++;\n                    if (strcmp(cmd, \"addWord\") == 0) {\n                        wordDictionaryAddWord(obj, word);\n                        printf(\"null\");\n                    } else if (strcmp(cmd, \"search\") == 0) {\n                        printf(\"%s\", wordDictionarySearch(obj, word) ? \"true\" : \"false\");\n                    }\n                }\n            }\n            cmd = strtok(NULL, \"[],\\\" \");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
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
