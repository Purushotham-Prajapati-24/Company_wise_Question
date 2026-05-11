import json
import os

def generate_json():
    problem_id = 472
    title = "Concatenated Words"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>472. Concatenated Words</h3>
<p>Given an array of strings <code>words</code> (<strong>without duplicates</strong>), return <em>all the <strong>concatenated words</strong> in the given array of words</em>.</p>

<p>A <strong>concatenated word</strong> is defined as a string that is comprised entirely of at least two shorter words (or the same word more than once) in the given array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
<strong>Output:</strong> ["catsdogcats","dogcatsdog","ratcatdogcat"]
<strong>Explanation:</strong> "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["cat","dog","catdog"]
<strong>Output:</strong> ["catdog"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
	<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
	<li>Total length of all words in <code>words</code> does not exceed <code>10<sup>5</sup></code>.</li>
</ul>"""

    input_format = "Line 1: A JSON array of strings `words`."
    output_format = "A JSON array of strings representing the concatenated words."
    
    constraints = [
        "1 <= words.length <= 10^4",
        "1 <= words[i].length <= 30",
        "words[i] consists of only lowercase English letters.",
        "All words are unique."
    ]
    
    explanation = "Use a Set for fast lookup of words. For each word, check if it can be formed by concatenating two or more shorter words from the set using DFS or dynamic programming. To avoid self-concatenation infinite recursion, temporarily remove the word from the set or ensure the segments are strictly shorter."
    
    answer = """class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        memo = {}

        def can_form(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set:
                    if suffix in word_set or can_form(suffix):
                        memo[word] = True
                        return True
            memo[word] = False
            return False

        res = []
        for w in words:
            if can_form(w):
                res.append(w)
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:\n        # User logic here\n        return []\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        words = json.loads(line)\n        sol = Solution()\n        res = sol.findAllConcatenatedWordsInADict(words)\n        print(json.dumps(sorted(res)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <sstream>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {\n        // User logic here\n        return {};\n    }\n};\n\nint main() {\n    string line; if (getline(cin, line)) {\n        vector<string> words; stringstream ss(line); string word;\n        while (getline(ss, word, '\"')) {\n            if (word != \"[\" && word != \",\" && word != \"]\" && word != \" \") {\n                words.push_back(word);\n                getline(ss, word, '\"');\n            }\n        }\n        Solution sol; vector<string> res = sol.findAllConcatenatedWordsInADict(words);\n        sort(res.begin(), res.end());\n        cout << \"[\";\n        for (int i = 0; i < res.size(); i++) {\n            cout << \"\\\"\" << res[i] << \"\\\"\" << (i == res.size() - 1 ? \"\" : \",\");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<String> findAllConcatenatedWordsInADict(String[] words) {\n        // User logic here\n        return new ArrayList<>();\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            line = line.substring(1, line.length() - 1);\n            String[] words = line.split(\",\\\\s*\");\n            for (int i = 0; i < words.length; i++) words[i] = words[i].replace(\"\\\"\", \"\").trim();\n            List<String> res = new Solution().findAllConcatenatedWordsInADict(words);\n            Collections.sort(res);\n            System.out.println(Arrays.toString(res.toArray()).replace(\", \", \",\"));\n        }\n    }\n}",
        "javascript": "/**\n * @param {string[]} words\n * @return {string[]}\n */\nvar findAllConcatenatedWordsInADict = function(words) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const words = JSON.parse(input);\n    const res = findAllConcatenatedWordsInADict(words);\n    console.log(JSON.stringify(res.sort()));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar** findAllConcatenatedWordsInADict(char** words, int wordsSize, int* returnSize) {\n    // User logic here\n    *returnSize = 0; return NULL;\n}\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[\"cat\",\"cats\",\"catsdogcats\",\"dog\",\"dogcatsdog\",\"hippopotamuses\",\"rat\",\"ratcatdogcat\"]", "expected_output": "[\"catsdogcats\", \"dogcatsdog\", \"ratcatdogcat\"]", "is_sample": True},
        {"input": "[\"cat\",\"dog\",\"catdog\"]", "expected_output": "[\"catdog\"]", "is_sample": True},
        {"input": "[\"a\",\"b\",\"ab\"]", "expected_output": "[\"ab\"]", "is_sample": False},
        {"input": "[\"a\",\"b\",\"c\",\"abc\"]", "expected_output": "[\"abc\"]", "is_sample": False},
        {"input": "[\"a\",\"aa\",\"aaa\"]", "expected_output": "[\"aa\", \"aaa\"]", "is_sample": False},
        {"input": "[\"a\",\"b\",\"c\",\"ab\",\"abc\",\"bc\"]", "expected_output": "[\"ab\", \"abc\", \"bc\"]", "is_sample": False},
        {"input": "[\"abc\"]", "expected_output": "[]", "is_sample": False},
        {"input": "[\"ba\",\"na\",\"bana\",\"banana\"]", "expected_output": "[\"bana\", \"banana\"]", "is_sample": False},
        {"input": "[\"prefix\",\"suffix\",\"prefixsuffix\"]", "expected_output": "[\"prefixsuffix\"]", "is_sample": False},
        {"input": "[\"x\",\"y\",\"z\",\"xyz\"]", "expected_output": "[\"xyz\"]", "is_sample": False}
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
        "topics": ["Array", "String", "Dynamic Programming", "DFS", "Trie"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Concatenated_Words.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
