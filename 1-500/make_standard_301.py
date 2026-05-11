import json
import os

def generate_json():
    problem_id = 301
    title = "Remove Invalid Parentheses"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>301. Remove Invalid Parentheses</h3>
<p>Given a string <code>s</code> that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid. Return <em>all possible unique results</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "()())()"
<strong>Output:</strong> ["(())()","()()()"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "(a)())()"
<strong>Output:</strong> ["(a)()()","(a)())()"]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = ")("
<strong>Output:</strong> [""]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 25</code></li>
	<li><code>s</code> consists of lowercase English letters and parentheses <code>'('</code> and <code>')'</code>.</li>
	<li>There will be at most <code>20</code> parentheses in <code>s</code>.</li>
</ul>"""

    input_format = "A string `s` containing parentheses and letters."
    output_format = "A list of strings representing unique valid results."
    
    constraints = [
        "1 <= s.length <= 25",
        "At most 20 parentheses."
    ]
    
    explanation = """To find all unique valid results with minimum removals:
1. **BFS Approach**: This is ideal for finding the "minimum" of something. 
2. **Level-by-Level**:
   - Start with the initial string in a queue.
   - At each level, check if any strings in the queue are valid.
   - If yes, collect all valid strings and stop (this is the level with minimum removals).
   - If no valid strings are found, generate the next level by removing one parenthesis from each string in the current queue.
3. **Validity Check**: Use a counter to verify if a string has balanced parentheses.
4. **Uniqueness**: Use a `visited` set to avoid processing the same string multiple times.
5. **Complexity Analysis**:
   - Time: O(2^N) in the worst case (though many branches are pruned). With N <= 25, this is acceptable.
   - Space: O(2^N) for the queue and visited set."""
    
    answer = """class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            cnt = 0
            for char in string:
                if char == '(':
                    cnt += 1
                elif char == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        # BFS approach
        queue = {s}
        while queue:
            # Check if any string in the current level is valid
            valid = list(filter(is_valid, queue))
            if valid:
                return valid
            
            # Generate next level by removing one parenthesis
            next_queue = set()
            for string in queue:
                for i in range(len(string)):
                    if string[i] in "()":
                        next_queue.add(string[:i] + string[i+1:])
            queue = next_queue
            
        return [""]"""

    boilerplate = {
        "python": "import sys\nimport re\nimport json\n\ndef removeInvalidParentheses(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    # Lethal parsing: find content inside quotes or after '=' \n    match = re.search(r'\"(.*?)\"', raw_input)\n    if match:\n        s = match.group(1)\n    else:\n        s = raw_input.split('=')[-1].strip().strip('\"')\n    \n    result = removeInvalidParentheses(s)\n    print(json.dumps(sorted(result)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nvector<string> removeInvalidParentheses(string s) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string line, input;\n    while(getline(cin, line)) input += line;\n    regex re_str(\"\\\"(.*?)\\\"\");\n    smatch match;\n    string s;\n    if (regex_search(input, match, re_str)) {\n        s = match[1];\n    } else {\n        size_t pos = input.find('=');\n        if (pos != string::npos) s = input.substr(pos + 1);\n        else s = input;\n        s.erase(remove(s.begin(), s.end(), '\"'), s.end());\n        s.erase(0, s.find_first_not_of(\" \\t\\n\\r\"));\n        s.erase(s.find_last_not_of(\" \\t\\n\\r\") + 1);\n    }\n    vector<string> res = removeInvalidParentheses(s);\n    sort(res.begin(), res.end());\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        if (i) cout << \",\";\n        cout << \"\\\"\" << res[i] << \"\\\"\";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public List<String> removeInvalidParentheses(String s) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb_input = new StringBuilder();\n        while(sc.hasNextLine()) sb_input.append(sc.nextLine());\n        String input = sb_input.toString();\n        \n        String s = \"\";\n        Matcher m = Pattern.compile(\"\\\\\\\"(.*?)\\\\\\\"\").matcher(input);\n        if (m.find()) {\n            s = m.group(1);\n        } else {\n            s = input.contains(\"=\") ? input.substring(input.indexOf(\"=\") + 1) : input;\n            s = s.replace(\"\\\"\", \"\").trim();\n        }\n        \n        List<String> res = new Solution().removeInvalidParentheses(s);\n        Collections.sort(res);\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < res.size(); i++) {\n            if (i > 0) sb.append(\",\");\n            sb.append(\"\\\"\").append(res.get(i)).append(\"\\\"\");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction removeInvalidParentheses(s) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nlet s = \"\";\nconst match = input.match(/\\\"(.*?)\\\"/);\nif (match) {\n    s = match[1];\n} else {\n    s = input.includes('=') ? input.split('=')[1] : input;\n    s = s.replace(/\\\"/g, '').trim();\n}\n\nconst res = removeInvalidParentheses(s).sort();\nconsole.log(JSON.stringify(res));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar** removeInvalidParentheses(char* s, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char buf[1024];\n    if (fgets(buf, sizeof(buf), stdin)) {\n        char *start = strchr(buf, '\"');\n        char *end = start ? strrchr(start + 1, '\"') : NULL;\n        char s[1024] = {0};\n        if (start && end) {\n            strncpy(s, start + 1, end - start - 1);\n        } else {\n            char *eq = strchr(buf, '=');\n            strcpy(s, eq ? eq + 1 : buf);\n            char *p = s; \n            while(*p) { if(*p == '\"' || *p == '\\n' || *p == '\\r') *p = ' '; p++; }\n        }\n        // Trim\n        char *ts = s; while(*ts == ' ') ts++;\n        char *te = ts + strlen(ts) - 1; while(te > ts && *te == ' ') *te-- = '\\0';\n\n        int returnSize = 0;\n        char** res = removeInvalidParentheses(ts, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            if (i) printf(\",\");\n            printf(\"\\\"%s\\\"\", res[i]);\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "()())()", "expected_output": '["(())()", "()()()"]', "is_sample": True},
        {"input": "(a)())()", "expected_output": '["(a)()()", "(a)())()"]', "is_sample": True},
        {"input": ")(", "expected_output": '[""]', "is_sample": True},
        {"input": "x(", "expected_output": '["x"]', "is_sample": False},
        {"input": "()", "expected_output": '["()"]', "is_sample": False},
        {"input": "(((", "expected_output": '[""]', "is_sample": False},
        {"input": ")))", "expected_output": '[""]', "is_sample": False},
        {"input": "(())((()())())", "expected_output": '["(())((()())())"]', "is_sample": False},
        {"input": "()()()()()()()()()()", "expected_output": '["()()()()()()()()()()"]', "is_sample": False},
        {"input": "(((((((((((((((())", "expected_output": '["()"]', "is_sample": False}
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
        "topics": ["String", "Backtracking", "Breadth-First Search"],
        "companyIndex": 0
    }

    output_path = "201-400/301_Remove_Invalid_Parentheses.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
