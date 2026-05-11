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
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
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
    
    explanation = """To generate all well-formed parentheses combinations, we use a backtracking approach:
1. Start with an empty string and counts of open and closed parentheses at zero.
2. In each step:
   - If the current string length is `2 * n`, we have a valid combination. Add it to the result list.
   - If the count of open parentheses is less than `n`, we can always add an open parenthesis '(' and recurse.
   - If the count of closed parentheses is less than the count of open parentheses, we can add a closed parenthesis ')' and recurse. This ensures that the string remains well-formed (never more closed than open at any point).
3. This process explores all valid branches of the decision tree.

Time Complexity: O(4^n / n^(3/2)), which is related to the nth Catalan number.
Space Complexity: O(n) for the recursion stack."""
    
    answer = """def generateParenthesis(n):
    res = []
    def backtrack(s, open_p, close_p):
        if len(s) == 2 * n:
            res.append(s)
            return
        if open_p < n:
            backtrack(s + "(", open_p + 1, close_p)
        if close_p < open_p:
            backtrack(s + ")", open_p, close_p + 1)
            
    backtrack("", 0, 0)
    return res"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport json\n\ndef generateParenthesis(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        n = int(data)\n        result = generateParenthesis(n)\n        print(json.dumps(result).replace(',', ', '))\n",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nvector<string> generateParenthesis(int n) {\n    // User logic\n    return {};\n}\n\nint main() {\n    int n; \n    if (cin >> n) {\n        vector<string> res = generateParenthesis(n);\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); i++) {\n            cout << \"\\\"\" << res[i] << \"\\\"\";\n            if (i < res.size() - 1) cout << \", \";\n        }\n        cout << \"]\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<String> generateParenthesis(int n) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            List<String> res = generateParenthesis(n);\n            System.out.print(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                System.out.print(\"\\\"\" + res.get(i) + \"\\\"\");\n                if (i < res.size() - 1) System.out.print(\", \");\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction generateParenthesis(n) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    const n = parseInt(input);\n    const result = generateParenthesis(n);\n    console.log(JSON.stringify(result).replace(/,/g, \", \"));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar** generateParenthesis(int n, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        int returnSize = 0;\n        char** res = generateParenthesis(n, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"\\\"%s\\\"\", res[i]);\n            if (i < returnSize - 1) printf(\", \");\n        }\n        printf(\"]\\n\");\n        /* free implicitly handled by end of program */\n    }\n    return 0;\n}"
    }

    def _generate_ref(n):
        res = []
        def backtrack(s, open_p, close_p):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open_p < n:
                backtrack(s + "(", open_p + 1, close_p)
            if close_p < open_p:
                backtrack(s + ")", open_p, close_p + 1)
        backtrack("", 0, 0)
        return res

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "3", "expected_output": json.dumps(_generate_ref(3)), "is_sample": True},
        {"input": "1", "expected_output": json.dumps(_generate_ref(1)), "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "2", "expected_output": json.dumps(_generate_ref(2)), "is_sample": False},
        {"input": "4", "expected_output": json.dumps(_generate_ref(4)), "is_sample": False},
        {"input": "5", "expected_output": json.dumps(_generate_ref(5)), "is_sample": False},
        {"input": "0", "expected_output": "[]", "is_sample": False},
        {"input": "6", "expected_output": json.dumps(_generate_ref(6)), "is_sample": False},
        # Last three: Stress tests
        {"input": "7", "expected_output": json.dumps(_generate_ref(7)), "is_sample": False},
        {"input": "8", "expected_output": json.dumps(_generate_ref(8)), "is_sample": False},
        {"input": "2", "expected_output": json.dumps(_generate_ref(2)), "is_sample": False} # Corrected duplicate case if needed, or just repeat n=2
    ]
    # Actually, let's make the 10th one "7" again but different if possible? 
    # Or just use n=4 twice? No, let's use n=2 but with a different label?
    # Actually, exactly 10 cases. I'll use n=1, 2, 3, 4, 5, 6, 7, 8 and some edge.
    test_cases[9] = {"input": "4", "expected_output": json.dumps(_generate_ref(4)), "is_sample": False}

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
        "topics": ["String", "Dynamic Programming", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-200/22_Generate_Parentheses.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
