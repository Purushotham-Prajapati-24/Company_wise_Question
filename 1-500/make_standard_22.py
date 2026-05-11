import json
import os

def generate_json():
    problem_id = 22
    title = "Generate Parentheses"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>22. Generate Parentheses</h3>
<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>"""

    input_format = "A single integer 'n'."
    output_format = "A list of strings representing all valid combinations of parentheses."
    
    constraints = [
        "1 <= n <= 8"
    ]
    
    explanation = """Use backtracking to build the combinations.
Keep track of the number of open and closed parentheses used.
An open parenthesis can be added if the count is less than n.
A closed parenthesis can be added if the count is less than the count of open parentheses."""
    
    answer = """def generateParenthesis(n):
    res = []
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)
    backtrack("", 0, 0)
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef generateParenthesis(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        n = int(data.replace('[','').replace(']','').split('=')[-1].strip())\n        res = generateParenthesis(n)\n        print(json.dumps(res).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nvector<string> generateParenthesis(int n) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        string clean = \"\";\n        for(char c : line) if(isdigit(c)) clean += c;\n        if(!clean.empty()) {\n            int n = stoi(clean);\n            vector<string> res = generateParenthesis(n);\n            cout << \"[\";\n            for (int i = 0; i < res.size(); i++) {\n                cout << \"\\\"\" << res[i] << \"\\\"\";\n                if (i < res.size() - 1) cout << \", \";\n            }\n            cout << \"]\" << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<String> generateParenthesis(int n) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine().replaceAll(\"[^0-9]\", \"\");\n        if (!line.isEmpty()) {\n            int n = Integer.parseInt(line);\n            List<String> res = generateParenthesis(n);\n            System.out.print(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                System.out.print(\"\\\"\" + res.get(i) + \"\\\"\");\n                if (i < res.size() - 1) System.out.print(\", \");\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction generateParenthesis(n) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconst n = parseInt(input.replace(/[^0-9]/g, ''), 10);\nif (!isNaN(n)) {\n    const res = generateParenthesis(n);\n    process.stdout.write(JSON.stringify(res).split(',').join(', ') + '\\n');\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nchar** generateParenthesis(int n, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char line[100];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p && !isdigit(*p)) p++;\n        if (*p) {\n            int n = atoi(p);\n            int returnSize = 0;\n            char** res = generateParenthesis(n, &returnSize);\n            printf(\"[\");\n            for (int i = 0; i < returnSize; i++) {\n                printf(\"\\\"%s\\\"\", res[i]);\n                if (i < returnSize - 1) printf(\", \");\n            }\n            printf(\"]\\n\");\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3", "expected_output": "[\"((()))\", \"(()())\", \"(())()\", \"()(())\", \"()()()\"]", "is_sample": True},
        {"input": "1", "expected_output": "[\"()\"]", "is_sample": True},
        {"input": "2", "expected_output": "[\"(())\", \"()()\"]", "is_sample": False},
        {"input": "4", "expected_output": "[\"(((())))\", \"((()()))\", \"((())())\", \"((()))()\", \"(()(()))\", \"(()()())\", \"(()())()\", \"(()) (())\", \"(())()()\", \"()((()))\", \"()(()())\", \"()(())()\", \"()()(())\", \"()()()()\"]", "is_sample": False},
        {"input": "0", "expected_output": "[]", "is_sample": False},
        {"input": "5", "expected_output": json.dumps(answer if 'n' in locals() else []).replace(',', ', '), "is_sample": False},
        {"input": "6", "expected_output": "[]", "is_sample": False},
        {"input": "7", "expected_output": "[]", "is_sample": False},
        {"input": "8", "expected_output": "[]", "is_sample": False},
        {"input": "1", "expected_output": "[\"()\"]", "is_sample": False}
    ]
    # Correct the test cases outputs using the logic
    def _gen_ref(n):
        if n == 0: return []
        res = []
        def backtrack(s, l, r):
            if len(s) == 2*n: res.append(s); return
            if l < n: backtrack(s+"(", l+1, r)
            if r < l: backtrack(s+")", l, r+1)
        backtrack("", 0, 0)
        return res
    
    for i in range(len(test_cases)):
        n_val = int(test_cases[i]["input"])
        test_cases[i]["expected_output"] = json.dumps(_gen_ref(n_val)).replace(',', ', ')

    data = {
        "question_id": problem_id,
        "question_title": title,
        "difficulty": difficulty,
        "marks": marks,
        "question_text": html_description,
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
        "topics": ["String", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-200/22_Generate_Parentheses.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
