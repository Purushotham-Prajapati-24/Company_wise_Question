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
        "python": "import sys\nimport re\nimport json\n\ndef shortestDistance(wordsDict, word1, word2):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Find the array part\n    arr_match = re.search(r'\\[.*?\\]', raw_input, re.DOTALL)\n    if arr_match:\n        wordsDict = json.loads(arr_match.group(0))\n        # Find the remaining two words after the array\n        after_arr = raw_input[arr_match.end():]\n        # Find all strings in quotes first\n        matches = re.findall(r'\"([^\"]*)\"', after_arr)\n        if len(matches) >= 2:\n            word1, word2 = matches[0], matches[1]\n        else:\n            # Fallback to alpha sequences\n            words = re.findall(r'[a-zA-Z]+', after_arr)\n            # Filter out labels like word1, word2\n            words = [w for w in words if w not in [\"word1\", \"word2\", \"word\"]]\n            if len(words) >= 2:\n                word1, word2 = words[0], words[1]\n            else:\n                sys.exit(0)\n        print(shortestDistance(wordsDict, word1, word2))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nint shortestDistance(vector<string>& wordsDict, string word1, string word2) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    // Parse array: strings inside [ ... ]\n    size_t start = input.find('[');\n    size_t end = input.find(']', start);\n    if (start == string::npos || end == string::npos) return 0;\n    \n    string arr_part = input.substr(start, end - start + 1);\n    string rest = input.substr(end + 1);\n    \n    vector<string> wordsDict;\n    regex re_quoted(\"\\\"([^\\\"]*)\\\"\");\n    auto q_begin = sregex_iterator(arr_part.begin(), arr_part.end(), re_quoted);\n    auto q_end = sregex_iterator();\n    for (sregex_iterator i = q_begin; i != q_end; ++i) wordsDict.push_back((*i)[1].str());\n    \n    vector<string> targets;\n    auto t_begin = sregex_iterator(rest.begin(), rest.end(), re_quoted);\n    for (sregex_iterator i = t_begin; i != q_end; ++i) targets.push_back((*i)[1].str());\n    \n    string w1, w2;\n    if (targets.size() >= 2) {\n        w1 = targets[0]; w2 = targets[1];\n    } else {\n        regex re_word(\"[a-zA-Z]+\");\n        auto w_begin = sregex_iterator(rest.begin(), rest.end(), re_word);\n        for (sregex_iterator i = w_begin; i != q_end; ++i) {\n            string s = i->str();\n            if (s != \"word1\" && s != \"word2\" && s != \"word\") targets.push_back(s);\n        }\n        if (targets.size() >= 2) {\n            w1 = targets[0]; w2 = targets[1];\n        } else return 0;\n    }\n    \n    cout << shortestDistance(wordsDict, w1, w2) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int shortestDistance(String[] wordsDict, String word1, String word2) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        int start = input.indexOf(\"[\");\n        int end = input.indexOf(\"]\", start);\n        if (start == -1 || end == -1) return;\n        \n        String arrPart = input.substring(start, end + 1);\n        String rest = input.substring(end + 1);\n        \n        List<String> wordsDict = new ArrayList<>();\n        Pattern p_quoted = Pattern.compile(\"\\\"([^\\\"]*)\\\"\");\n        Matcher m_arr = p_quoted.matcher(arrPart);\n        while (m_arr.find()) wordsDict.add(m_arr.group(1));\n        \n        List<String> targets = new ArrayList<>();\n        Matcher m_rest = p_quoted.matcher(rest);\n        while (m_rest.find()) targets.add(m_rest.group(1));\n        \n        String w1 = \"\", w2 = \"\";\n        if (targets.size() >= 2) {\n            w1 = targets.get(0); w2 = targets.get(1);\n        } else {\n            Pattern p_word = Pattern.compile(\"[a-zA-Z]+\");\n            Matcher m_word = p_word.matcher(rest);\n            while (m_word.find()) {\n                String s = m_word.group();\n                if (!s.equals(\"word1\") && !s.equals(\"word2\") && !s.equals(\"word\")) targets.add(s);\n            }\n            if (targets.size() >= 2) {\n                w1 = targets.get(0); w2 = targets.get(1);\n            } else return;\n        }\n        System.out.println(new Solution().shortestDistance(wordsDict.toArray(new String[0]), w1, w2));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction shortestDistance(wordsDict, word1, word2) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst arrMatch = input.match(/\\[.*?\\]/s);\nif (arrMatch) {\n    const wordsDict = JSON.parse(arrMatch[0]);\n    const rest = input.slice(arrMatch.index + arrMatch[0].length);\n    const quoted = rest.match(/\"([^\"]*)\"/g);\n    let w1, w2;\n    if (quoted && quoted.length >= 2) {\n        w1 = quoted[0].replace(/\"/g, '');\n        w2 = quoted[1].replace(/\"/g, '');\n    } else {\n        const words = (rest.match(/[a-zA-Z]+/g) || []).filter(w => ![\"word1\", \"word2\", \"word\"].includes(w));\n        if (words.length >= 2) {\n            w1 = words[0]; w2 = words[1];\n        } else process.exit(0);\n    }\n    console.log(shortestDistance(wordsDict, w1, w2));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint shortestDistance(char** wordsDict, int wordsDictSize, char* word1, char* word2) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    static char buffer[1000000];\n    int bytes = fread(buffer, 1, sizeof(buffer)-1, stdin);\n    buffer[bytes] = '\\0';\n    \n    char** words = (char**)malloc(30005 * sizeof(char*));\n    int size = 0;\n    \n    char* p = strchr(buffer, '[');\n    if (!p) return 0;\n    char* end = strchr(p, ']');\n    if (!end) return 0;\n    \n    char* ptr = p;\n    while (ptr < end) {\n        if (*ptr == '\"') {\n            ptr++;\n            char* start = ptr;\n            while (ptr < end && *ptr != '\"') ptr++;\n            int len = ptr - start;\n            words[size] = (char*)malloc(len + 1);\n            strncpy(words[size], start, len); words[size][len] = '\\0';\n            size++;\n        }\n        ptr++;\n    }\n    \n    char* rest = end + 1;\n    char w1[100], w2[100];\n    int target_count = 0;\n    ptr = rest;\n    while (*ptr) {\n        if (*ptr == '\"') {\n            ptr++;\n            char* start = ptr;\n            while (*ptr && *ptr != '\"') ptr++;\n            int len = ptr - start;\n            if (target_count == 0) {\n                strncpy(w1, start, len); w1[len] = '\\0'; target_count++;\n            } else if (target_count == 1) {\n                strncpy(w2, start, len); w2[len] = '\\0'; target_count++; break;\n            }\n        } else if (isalpha(*ptr)) {\n            char* start = ptr;\n            while (*ptr && isalpha(*ptr)) ptr++;\n            int len = ptr - start;\n            char temp[100]; strncpy(temp, start, len); temp[len] = '\\0';\n            if (strcmp(temp, \"word1\") != 0 && strcmp(temp, \"word2\") != 0 && strcmp(temp, \"word\") != 0) {\n                if (target_count == 0) {\n                    strcpy(w1, temp); target_count++;\n                } else if (target_count == 1) {\n                    strcpy(w2, temp); target_count++; break;\n                }\n            }\n            ptr--; // compensate for loop ptr++\n        }\n        ptr++;\n    }\n    \n    if (target_count == 2) {\n        printf(\"%d\\n\", shortestDistance(words, size, w1, w2));\n    }\n    \n    return 0;\n}"
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
