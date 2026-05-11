import json
import os

def generate_json():
    problem_id = 243
    title = "Shortest Word Distance"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>243. Shortest Word Distance</h3>
<p>Given an array of strings <code>wordsDict</code> and two <strong>distinct</strong> strings <code>word1</code> and <code>word2</code>, return <em>the shortest distance between these two words in the list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= wordsDict.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= wordsDict[i].length &lt;= 10</code></li>
	<li><code>wordsDict[i]</code> consists of lowercase English letters.</li>
	<li><code>word1</code> and <code>word2</code> are in <code>wordsDict</code>.</li>
	<li><code>word1 != word2</code>.</li>
</ul>"""

    input_format = "Three lines: first, an array of strings; second, string word1; third, string word2."
    output_format = "An integer representing the shortest distance."
    
    constraints = [
        "2 <= count of words <= 30,000",
        "word1 and word2 are in the dictionary and are distinct.",
        "One-pass traversal expected."
    ]
    
    explanation = """To find the shortest distance in O(N):
1. **Pointers**: Maintain two indices, `p1` and `p2`, initialized to `-1`.
2. **One Pass**: Iterate through the dictionary once.
3. **Logic**:
   - If current word is `word1`, update `p1 = current_index`.
   - If current word is `word2`, update `p2 = current_index`.
   - Whenever both `p1` and `p2` have been set (not `-1`), calculate `abs(p1 - p2)` and update the minimum distance found so far.
4. **Complexity**:
   - Time: O(N) where N is the length of `wordsDict`.
   - Space: O(1)."""
    
    answer = """class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1 = p2 = -1
        min_dist = len(wordsDict)
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                p1 = i
            elif word == word2:
                p2 = i
            
            if p1 != -1 and p2 != -1:
                min_dist = min(min_dist, abs(p1 - p2))
                
        return min_dist"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef shortestDistance(wordsDict, word1, word2):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        wordsDict = json.loads(lines[0])\n        word1 = lines[1].strip()\n        word2 = lines[2].strip()\n        print(shortestDistance(wordsDict, word1, word2))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint shortestDistance(vector<string>& wordsDict, string word1, string word2) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<string> words;\n        string word;\n        bool inQuotes = false;\n        for (char c : line) {\n            if (c == '\"') {\n                if (inQuotes) {\n                    words.push_back(word);\n                    word = \"\";\n                }\n                inQuotes = !inQuotes;\n            } else if (inQuotes) {\n                word += c;\n            }\n        }\n        string word1, word2;\n        if (getline(cin, word1) && getline(cin, word2)) {\n            cout << shortestDistance(words, word1, word2) << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int shortestDistance(String[] wordsDict, String word1, String word2) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null) {\n            List<String> dict = new ArrayList<>();\n            StringBuilder word = new StringBuilder();\n            boolean inQuotes = false;\n            for (char c : line.toCharArray()) {\n                if (c == '\"') {\n                    if (inQuotes) {\n                        dict.add(word.toString());\n                        word.setLength(0);\n                    }\n                    inQuotes = !inQuotes;\n                } else if (inQuotes) {\n                    word.append(c);\n                }\n            }\n            String word1 = br.readLine();\n            String word2 = br.readLine();\n            if (word1 != null && word2 != null) {\n                System.out.println(new Solution().shortestDistance(dict.toArray(new String[0]), word1, word2));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction shortestDistance(wordsDict, word1, word2) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\r?\\n/);\nif (input.length >= 3) {\n    let wordsDict = JSON.parse(input[0]);\n    let word1 = input[1];\n    let word2 = input[2];\n    console.log(shortestDistance(wordsDict, word1, word2));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint shortestDistance(char** wordsDict, int wordsDictSize, char* word1, char* word2) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char line[1000000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char** words = (char**)malloc(30005 * sizeof(char*));\n        int size = 0;\n        char* p = line;\n        while (*p) {\n            if (*p == '\"') {\n                p++;\n                char* start = p;\n                while (*p && *p != '\"') p++;\n                *p = '\\0';\n                words[size++] = strdup(start);\n            }\n            if (*p) p++;\n        }\n        char word1[55], word2[55];\n        if (scanf(\"%s %s\", word1, word2) == 2) {\n            printf(\"%d\\n\", shortestDistance(words, size, word1, word2));\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["practice", "makes", "perfect", "coding", "makes"]\\ncoding\\npractice', "expected_output": "3", "is_sample": True},
        {"input": '["practice", "makes", "perfect", "coding", "makes"]\\nmakes\\ncoding', "expected_output": "1", "is_sample": True},
        {"input": '["a", "b", "c", "d", "a", "b"]\\na\\nb', "expected_output": "1", "is_sample": False},
        {"input": '["a", "b", "c", "d", "a", "b"]\\na\\nd', "expected_output": "1", "is_sample": False},
        {"input": '["a", "x", "y", "z", "b", "c", "d", "a"]\\na\\nb', "expected_output": "3", "is_sample": False},
        {"input": '["a", "a", "b"]\\na\\nb', "expected_output": "1", "is_sample": False},
        {"input": '["x", "y", "x", "z", "y"]\\nx\\ny', "expected_output": "1", "is_sample": False},
        # Stress Tests (30,000 words)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_dist(words, w1, w2):
        p1 = p2 = -1
        ans = len(words)
        for i, w in enumerate(words):
            if w == w1: p1 = i
            elif w == w2: p2 = i
            if p1 != -1 and p2 != -1: ans = min(ans, abs(p1-p2))
        return ans

    # Stress 8: 30,000 words, words at extreme ends
    w8 = ["a"] + ["mid"]*29998 + ["b"]
    test_cases[7] = {"input": json.dumps(w8) + "\\na\\nb", "expected_output": str(_solve_dist(w8, "a", "b")), "is_sample": False}
    # Stress 9: Alternate target words
    w9 = ["a", "b"] * 15000
    test_cases[8] = {"input": json.dumps(w9) + "\\na\\nb", "expected_output": "1", "is_sample": False}
    # Stress 10: Mixed list
    w10 = ["x"] * 10000 + ["a"] + ["x"] * 10000 + ["b"] + ["x"] * 9998
    test_cases[9] = {"input": json.dumps(w10) + "\\na\\nb", "expected_output": "10001", "is_sample": False}

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
        "topics": ["Array", "String"],
        "companyIndex": 0
    }

    output_path = "201-400/243_Shortest_Word_Distance.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
