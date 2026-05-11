import json
import os

def generate_json():
    problem_id = 418
    title = "Sentence Screen Fitting"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>418. Sentence Screen Fitting</h3>
<p>Given a <code>rows x cols</code> screen and a <code>sentence</code> represented as a list of strings, return <em>the number of times the given sentence can be fitted on the screen.</em></p>

<p>The order of words in the sentence must remained unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> sentence = ["hello","world"], rows = 2, cols = 8
<strong>Output:</strong> 1
<strong>Explanation:</strong>
hello---
world---
The character '-' means an empty space on the screen.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> sentence = ["a", "bcd", "e"], rows = 3, cols = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong>
a-bcd- 
e-a---
bcd-e-
The character '-' means an empty space on the screen.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> sentence = ["I", "had", "apple", "pie"], rows = 4, cols = 5
<strong>Output:</strong> 1
<strong>Explanation:</strong>
I-had
apple
pie-I
had--
The character '-' means an empty space on the screen.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= sentence.length &lt;= 100</code></li>
	<li><code>1 &lt;= sentence[i].length &lt;= 10</code></li>
	<li><code>sentence[i]</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= rows, cols &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A list of strings `sentence` and integers `rows` and `cols`."
    output_format = "An integer."
    
    constraints = [
        "1 <= sentence.length <= 100",
        "1 <= rows, cols <= 10,000"
    ]
    
    explanation = """Concatenate the sentence with spaces and treat it as a repeating string. Use a pointer to track the current position in the concatenated string."""
    
    answer = """class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        start = 0
        n = len(s)
        for _ in range(rows):
            start += cols
            if s[start % n] == " ":
                start += 1
            else:
                while start > 0 and s[(start - 1) % n] != " ":
                    start -= 1
        return start // n"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        sentence = json.loads(lines[0].strip())\n        rows = int(lines[1].strip())\n        cols = int(lines[2].strip())\n        sol = Solution()\n        print(json.dumps(sol.wordsTyping(sentence, rows, cols)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int wordsTyping(vector<string>& sentence, int rows, int cols) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line;\n    int rows, cols;\n    if (getline(cin, line)) {\n        if (!line.empty() && line.front() == '[') line = line.substr(1, line.size() - 2);\n        stringstream ss(line);\n        string val;\n        vector<string> sentence;\n        while (getline(ss, val, ',')) {\n            while(!val.empty() && (val.front() == ' ' || val.front() == '\"')) val.erase(0, 1);\n            while(!val.empty() && (val.back() == ' ' || val.back() == '\"')) val.pop_back();\n            if(!val.empty()) sentence.push_back(val);\n        }\n        if (cin >> rows >> cols) {\n            Solution sol;\n            cout << sol.wordsTyping(sentence, rows, cols) << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int wordsTyping(String[] sentence, int rows, int cols) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            if (line.startsWith(\"[\")) line = line.substring(1, line.length() - 1);\n            String[] parts = line.split(\",\");\n            String[] sentence = new String[parts.length];\n            for (int i = 0; i < parts.length; i++) {\n                String s = parts[i].trim();\n                if (s.startsWith(\"\\\\\\\"\")) s = s.substring(1, s.length() - 1);\n                if (s.endsWith(\"\\\\\\\"\")) s = s.substring(0, s.length() - 1);\n                sentence[i] = s;\n            }\n            if (sc.hasNextInt()) {\n                int rows = sc.nextInt();\n                if (sc.hasNextInt()) {\n                    int cols = sc.nextInt();\n                    Solution sol = new Solution();\n                    System.out.println(sol.wordsTyping(sentence, rows, cols));\n                }\n            }\n        }\n    }\n}",
        "javascript": "var wordsTyping = function(sentence, rows, cols) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').split('\\\\n');\nif (input.length >= 3) {\n    const sentence = JSON.parse(input[0].trim());\n    const rows = parseInt(input[1].trim());\n    const cols = parseInt(input[2].trim());\n    console.log(JSON.stringify(wordsTyping(sentence, rows, cols)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint wordsTyping(char** sentence, int sentenceSize, int rows, int cols) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["hello","world"]\n2\n8', "expected_output": "1", "is_sample": True},
        {"input": '["a", "bcd", "e"]\n3\n6', "expected_output": "2", "is_sample": True},
        {"input": '["I", "had", "apple", "pie"]\n4\n5', "expected_output": "1", "is_sample": False},
        {"input": '["f", "p", "a"]\n8\n7', "expected_output": "10", "is_sample": False},
        {"input": '["hello"]\n10\n10', "expected_output": "20", "is_sample": False},
        {"input": '["a","b","c"]\n1\n1', "expected_output": "0", "is_sample": False},
        {"input": '["a","b","c"]\n1\n5', "expected_output": "1", "is_sample": False},
        # 3 Stress
        {"input": '["a"]\n10000\n10000', "expected_output": "50000000", "is_sample": False},
        {"input": '["abc","def","ghi"]\n10000\n10', "expected_output": "8333", "is_sample": False},
        {"input": '["a"]*100\n10000\n10000', "expected_output": "500000", "is_sample": False}
    ]
    test_cases[9]["input"] = json.dumps(["a"]*100) + "\n10000\n10000"

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
        "topics": ["Dynamic Programming", "String"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Sentence_Screen_Fitting.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
