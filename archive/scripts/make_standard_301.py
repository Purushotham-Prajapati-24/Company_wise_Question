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
        "python": "import sys\nimport json\n\ndef removeInvalidParentheses(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    result = removeInvalidParentheses(s)\n    print(json.dumps(sorted(result)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_set>\n#include <queue>\n#include <algorithm>\nusing namespace std;\n\nvector<string> removeInvalidParentheses(string s) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string s;\n    getline(cin, s);\n    vector<string> res = removeInvalidParentheses(s);\n    sort(res.begin(), res.end());\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        if (i) cout << \",\";\n        cout << \"\\\"\" << res[i] << \"\\\"\";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<String> removeInvalidParentheses(String s) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String s = sc.nextLine().trim();\n        List<String> res = new Solution().removeInvalidParentheses(s);\n        Collections.sort(res);\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < res.size(); i++) {\n            if (i > 0) sb.append(\",\");\n            sb.append(\"\\\"\").append(res.get(i)).append(\"\\\"\");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction removeInvalidParentheses(s) {\n    // User logic here\n    return [];\n}\n\nconst s = fs.readFileSync(0, 'utf-8').trim();\nconst res = removeInvalidParentheses(s).sort();\nconsole.log(JSON.stringify(res));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar** removeInvalidParentheses(char* s, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char s[30];\n    if (fgets(s, sizeof(s), stdin)) {\n        int len = strlen(s);\n        if (len > 0 && s[len-1] == '\\n') s[len-1] = '\\0';\n    }\n    int returnSize = 0;\n    char** res = removeInvalidParentheses(s, &returnSize);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        if (i) printf(\",\");\n        printf(\"\\\"%s\\\"\", res[i]);\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
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
