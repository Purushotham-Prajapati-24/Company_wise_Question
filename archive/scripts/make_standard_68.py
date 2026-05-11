import json
import os

def generate_json():
    problem_id = 68
    title = "Text Justification"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>68. Text Justification</h3>
<p>Given an array of strings <code>words</code> and a width <code>maxWidth</code>, format the text such that each line has exactly <code>maxWidth</code> characters and is fully (left and right) justified.</p>

<p>You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces <code>' '</code> when necessary so that each line has exactly <code>maxWidth</code> characters.</p>

<p>Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.</p>

<p>For the last line of text, it should be left-justified, and no extra space is inserted between words.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>A word is defined as a character sequence consisting of non-space characters only.</li>
	<li>Each word's length is guaranteed to be greater than <code>0</code> and not exceed <code>maxWidth</code>.</li>
	<li>The input array <code>words</code> contains at least one word.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
<strong>Output:</strong>
[
&nbsp;  "This    is    an",
&nbsp;  "example  of text",
&nbsp;  "justification.  "
]</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
<strong>Output:</strong>
[
&nbsp; "What   must   be",
&nbsp; "acknowledgment  ",
&nbsp; "shall be        "
]
<strong>Explanation:</strong> Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
<strong>Output:</strong>
[
&nbsp; "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 300</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>words[i]</code> consists of English letters and symbols.</li>
	<li><code>1 &lt;= maxWidth &lt;= 100</code></li>
	<li><code>words[i].length &lt;= maxWidth</code></li>
</ul>"""

    input_format = "An integer 'maxWidth' on the first line, followed by a space-separated list of words on the second line."
    output_format = "A list of formatted strings, each of length 'maxWidth'."
    
    constraints = [
        "1 <= words.length <= 300",
        "1 <= words[i].length <= 20",
        "1 <= maxWidth <= 100",
        "words[i].length <= maxWidth"
    ]
    
    explanation = """To format text with greedy packing and full/left justification:
1. **Greedy Line Selection**: Iterate through the words and keep track of how many words can fit into a line of width `maxWidth`. A line must have at least one space between words.
2. **Justification Strategy**:
   - **Case 1: Fully Justified**: If a line is not the last line and has more than one word, distribute the total number of required spaces (`maxWidth - length_of_letters`) between the words.
     - Calculate `num_spaces = maxWidth - letter_count`.
     - Calculate `gaps = num_words - 1`.
     - Spaces between each word: `avg_spaces = num_spaces // gaps`.
     - Extra spaces to distribute from the left: `extra_spaces = num_spaces % gaps`.
   - **Case 2: Left Justified**: If a line is the last line or contains only one word, append words with a single space between them and pad the remainder of the line with spaces to reach `maxWidth`.
3. **Complexity**:
   - Time Complexity: O(N), where N is the total number of characters across all words, as each word is processed once during line grouping and once for formatting.
   - Space Complexity: O(N) or O(maxWidth * num_lines) to store the result."""
    
    answer = """def fullJustify(words, maxWidth):
    res = []
    current_line = []
    current_len = 0
    
    for word in words:
        # Check if adding the word (plus a mandatory space) exceeds maxWidth
        if current_len + len(word) + len(current_line) > maxWidth:
            # Justify the current line
            if len(current_line) == 1:
                res.append(current_line[0].ljust(maxWidth))
            else:
                num_spaces = maxWidth - current_len
                avg_spaces = num_spaces // (len(current_line) - 1)
                extra_spaces = num_spaces % (len(current_line) - 1)
                
                line_str = \"\"
                for i in range(len(current_line) - 1):
                    line_str += current_line[i]
                    # Distribute spaces evenly, putting more on the left if necessary
                    line_str += \" \" * (avg_spaces + (1 if i < extra_spaces else 0))
                line_str += current_line[-1]
                res.append(line_str)
            
            # Reset for next line
            current_line = [word]
            current_len = len(word)
        else:
            current_line.append(word)
            current_len += len(word)
            
    # Handle the last line (left-justified)
    last_line = \" \".join(current_line).ljust(maxWidth)
    res.append(last_line)
    
    return res"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef fullJustify(words, maxWidth):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().splitlines()\n    if len(data) >= 2:\n        maxWidth = int(data[0].strip())\n        words = data[1].strip().split()\n        print(fullJustify(words, maxWidth))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nvector<string> fullJustify(vector<string>& words, int maxWidth) {\n    // User logic\n    return {};\n}\n\nint main() {\n    int maxWidth; cin >> maxWidth; cin.ignore();\n    string word;\n    vector<string> words;\n    while (cin >> word) words.push_back(word);\n    auto res = fullJustify(words, maxWidth);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        cout << \"'\" << res[i] << \"'\";\n        if (i + 1 < (int)res.size()) cout << \", \";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<String> fullJustify(String[] words, int maxWidth) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int maxWidth = sc.nextInt();\n        List<String> wordList = new ArrayList<>();\n        while (sc.hasNext()) wordList.add(sc.next());\n        List<String> res = fullJustify(wordList.toArray(new String[0]), maxWidth);\n        System.out.print(\"[\");\n        for (int i = 0; i < res.size(); i++) {\n            System.out.print(\"'\" + res.get(i) + \"'\");\n            if (i + 1 < res.size()) System.out.print(\", \");\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction fullJustify(words, maxWidth) {\n    // User logic\n    return [];\n}\n\nconst lines = fs.readFileSync(0, 'utf8').trim().split('\\n');\nconst maxWidth = parseInt(lines[0]);\nconst words = lines.slice(1).join(' ').trim().split(/\\s+/);\nconst res = fullJustify(words, maxWidth);\nconsole.log('[' + res.map(s => \"'\" + s + \"'\").join(', ') + ']');",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar** fullJustify(char** words, int wordsSize, int maxWidth, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int maxWidth; scanf(\"%d\", &maxWidth);\n    char buff[300][21];\n    int wordsSize = 0;\n    while (wordsSize < 300 && scanf(\"%20s\", buff[wordsSize]) == 1) wordsSize++;\n    char** words = (char**)malloc(wordsSize * sizeof(char*));\n    for (int i = 0; i < wordsSize; i++) words[i] = buff[i];\n    int returnSize = 0;\n    char** res = fullJustify(words, wordsSize, maxWidth, &returnSize);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"'%s'\", res[i]);\n        if (i + 1 < returnSize) printf(\", \");\n        if (res[i]) free(res[i]);\n    }\n    printf(\"]\\n\");\n    if (res) free(res);\n    free(words);\n    return 0;\n}"
    }

    def _solve(words, maxWidth):
        res, cur, cur_len = [], [], 0
        for w in words:
            if cur_len + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    res.append(cur[0].ljust(maxWidth))
                else:
                    num_spaces = maxWidth - cur_len
                    avg = num_spaces // (len(cur)-1)
                    rem = num_spaces % (len(cur)-1)
                    s = ""
                    for i in range(len(cur)-1):
                        s += cur[i] + " " * (avg + (1 if i < rem else 0))
                    s += cur[-1]
                    res.append(s)
                cur, cur_len = [w], len(w)
            else:
                cur.append(w)
                cur_len += len(w)
        res.append(" ".join(cur).ljust(maxWidth))
        return res

    sample1_words = ["This", "is", "an", "example", "of", "text", "justification."]
    sample2_words = ["What","must","be","acknowledgment","shall","be"]
    sample3_words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "16\\n" + " ".join(sample1_words), "expected_output": str(_solve(sample1_words, 16)), "is_sample": True},
        {"input": "16\\n" + " ".join(sample2_words), "expected_output": str(_solve(sample2_words, 16)), "is_sample": True},
        # Middle five: Diverse cases
        {"input": "20\\n" + " ".join(sample3_words), "expected_output": str(_solve(sample3_words, 20)), "is_sample": False},
        {"input": "1\\na", "expected_output": "['a']", "is_sample": False},
        {"input": "2\\na", "expected_output": "['a ']", "is_sample": False},
        {"input": "6\\nListen to many, speak to a few.", "expected_output": str(_solve(["Listen","to","many,","speak","to","a","few."], 6)), "is_sample": False},
        {"input": "1\\nA B C D E", "expected_output": "['A', 'B', 'C', 'D', 'E']", "is_sample": False},
        # Last three: Stress tests
        {"input": "100\\n" + " ".join(["word"] * 50), "expected_output": str(_solve(["word"] * 50, 100)), "is_sample": False},
        {"input": "1\\n" + " ".join(["a"] * 100), "expected_output": str(["a"] * 100), "is_sample": False},
        {"input": "100\\nthisisanextremelylongword", "expected_output": str(["thisisanextremelylongword".ljust(100)]), "is_sample": False}
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
        "topics": ["Array", "String", "Simulation"],
        "companyIndex": 0
    }

    output_path = "1-200/68_Text_Justification.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
