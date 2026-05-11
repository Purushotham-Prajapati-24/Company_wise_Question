import json
import os

def generate_json():
    problem_id = 425
    title = "Word Squares"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>425. Word Squares</h3>
<p>Given an array of <strong>unique</strong> strings <code>words</code>, return <em>all the </em><strong>word squares</strong><em> that can be formed from </em><code>words</code>. You can return the answer in <strong>any order</strong>.</p>

<p>A sequence of strings forms a <strong>word square</strong> if the <code>k<sup>th</sup></code> row and column read the same string, where <code>0 &lt;= k &lt; max(numRows, numColumns)</code>.</p>

<ul>
	<li>For example, the sequence <code>["ball","area","lead","lady"]</code> forms a word square because each word reads the same horizontally and vertically.</li>
</ul>

<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["area","lead","wall","lady","ball"]
<strong>Output:</strong> [["ball","area","lead","lady"],["wall","area","lead","lady"]]
<strong>Explanation:</strong>
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["abat","baba","atan","atal"]
<strong>Output:</strong> [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
<strong>Explanation:</strong>
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 4</code></li>
	<li>All <code>words[i]</code> have the same length.</li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
	<li>All <code>words[i]</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A JSON array of unique strings `words`."
    output_format = "A JSON array of arrays of strings representing all possible word squares."
    
    constraints = [
        "1 <= words.length <= 1000",
        "1 <= words[i].length <= 4",
        "All words have the same length.",
        "Words consist of lowercase English letters.",
        "All words are unique."
    ]
    
    explanation = """A word square of size N x N must satisfy square[i][j] == square[j][i].
This means if we have already chosen the first 'i' rows, the next row (row 'i') must start with a prefix formed by the characters at square[0][i], square[1][i], ..., square[i-1][i].
We can use a Trie or a hash map to quickly look up all words that start with a given prefix to efficiently build the square row by row using backtracking."""
    
    answer = """class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        prefixes = {}
        for w in words:
            for i in range(n):
                prefix = w[:i]
                if prefix not in prefixes:
                    prefixes[prefix] = []
                prefixes[prefix].append(w)
        
        results = []
        
        def backtrack(step, current_square):
            if step == n:
                results.append(list(current_square))
                return
            
            prefix = "".join([word[step] for word in current_square])
            if prefix not in prefixes:
                return
            
            for candidate in prefixes[prefix]:
                current_square.append(candidate)
                backtrack(step + 1, current_square)
                current_square.pop()
        
        for word in words:
            backtrack(1, [word])
            
        return results"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def wordSquares(self, words: list[str]) -> list[list[str]]:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        try:\n            words = json.loads(raw_input)\n            sol = Solution()\n            result = sol.wordSquares(words)\n            print(json.dumps(result).replace(\" \", \"\"))\n        except:\n            pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<vector<string>> wordSquares(vector<string>& words) {\n        // User logic here\n        return {};\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<string> words;\n        int i = 0;\n        while (i < line.length()) {\n            if (line[i] == '\"') {\n                int j = i + 1;\n                while (j < line.length() && line[j] != '\"') j++;\n                words.push_back(line.substr(i + 1, j - i - 1));\n                i = j;\n            }\n            i++;\n        }\n        Solution sol;\n        vector<vector<string>> res = sol.wordSquares(words);\n        cout << \"[\";\n        for (int k = 0; k < res.size(); k++) {\n            if (k > 0) cout << \",\";\n            cout << \"[\";\n            for (int l = 0; l < res[k].size(); l++) {\n                if (l > 0) cout << \",\";\n                cout << \"\\\\\\\"\" << res[k][l] << \"\\\\\\\"\";\n            }\n            cout << \"]\";\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<List<String>> wordSquares(String[] words) {\n        // User logic here\n        return new ArrayList<>();\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine();\n            List<String> wordList = new ArrayList<>();\n            int i = 0;\n            while (i < line.length()) {\n                if (line.charAt(i) == '\"') {\n                    int j = i + 1;\n                    while (j < line.length() && line.charAt(j) != '\"') j++;\n                    wordList.add(line.substring(i + 1, j));\n                    i = j;\n                }\n                i++;\n            }\n            Solution sol = new Solution();\n            List<List<String>> res = sol.wordSquares(wordList.toArray(new String[0]));\n            StringBuilder sb = new StringBuilder();\n            sb.append(\"[\");\n            for (int k = 0; k < res.size(); k++) {\n                if (k > 0) sb.append(\",\");\n                sb.append(\"[\");\n                for (int l = 0; l < res.get(k).size(); l++) {\n                    if (l > 0) sb.append(\",\");\n                    sb.append(\"\\\\\\\"\").append(res.get(k).get(l)).append(\"\\\\\\\"\");\n                }\n                sb.append(\"]\");\n            }\n            sb.append(\"]\");\n            System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "/**\n * @param {string[]} words\n * @return {string[][]}\n */\nvar wordSquares = function(words) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const words = JSON.parse(input);\n    const result = wordSquares(words);\n    console.log(JSON.stringify(result).replace(/ /g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the arrays are returned as *returnColumnSizes array.\n * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().\n */\nchar*** wordSquares(char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char line[100000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* words[1000];\n        int wordsSize = 0;\n        int i = 0;\n        while (line[i]) {\n            if (line[i] == '\"') {\n                int j = i + 1;\n                while (line[j] && line[j] != '\"') j++;\n                line[j] = '\\\\0';\n                words[wordsSize++] = line + i + 1;\n                i = j;\n            }\n            i++;\n        }\n        int returnSize = 0;\n        int* returnColumnSizes = NULL;\n        char*** res = wordSquares(words, wordsSize, &returnSize, &returnColumnSizes);\n        printf(\"[\");\n        for (int k = 0; k < returnSize; k++) {\n            if (k > 0) printf(\",\");\n            printf(\"[\");\n            for (int l = 0; l < returnColumnSizes[k]; l++) {\n                if (l > 0) printf(\",\");\n                printf(\"\\\\\\\"%s\\\\\\\"\", res[k][l]);\n            }\n            printf(\"]\");\n        }\n        printf(\"]\\\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["area","lead","wall","lady","ball"]', "expected_output": '[["ball","area","lead","lady"],["wall","area","lead","lady"]]', "is_sample": True},
        {"input": '["abat","baba","atan","atal"]', "expected_output": '[["baba","abat","baba","atan"],["baba","abat","baba","atal"]]', "is_sample": True},
        {"input": '["a"]', "expected_output": '[["a"]]', "is_sample": False},
        {"input": '["ab", "ba"]', "expected_output": '[["ab","ba"],["ba","ab"]]', "is_sample": False},
        {"input": '["abcd","bcde","cdef","defg"]', "expected_output": '[]', "is_sample": False},
        {"input": '["wall","area","lead","lady","ball","abcd"]', "expected_output": '[["ball","area","lead","lady"],["wall","area","lead","lady"]]', "is_sample": False},
        {"input": '["ball",  "area",  "lead", "lady"]', "expected_output": '[["ball","area","lead","lady"]]', "is_sample": False}, # anomalous spaces
        {"input": '[ "a", "b" ]', "expected_output": '[["a"],["b"]]', "is_sample": False}, # anomalous spaces
        # Stress
        {"input": '["poll","oils","lily","lays"]', "expected_output": '[["poll","oils","lily","lays"]]', "is_sample": False},
        {"input": '[]', "expected_output": '[]', "is_sample": False}
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
        "topics": ["Trie", "Backtracking"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
