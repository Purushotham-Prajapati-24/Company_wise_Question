import json
import os

def generate_json():
    problem_id = 241
    title = "Different Ways to Add Parentheses"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>241. Different Ways to Add Parentheses</h3>
<p>Given a string <code>expression</code> of numbers and operators, return <em>all possible results from computing all the different possible ways to group numbers and operators</em>. You may return the answer in <strong>any order</strong>.</p>

<p>The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed <code>10<sup>4</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> expression = "2-1-1"
<strong>Output:</strong> [0,2]
<strong>Explanation:</strong>
((2-1)-1) = 0 
(2-(1-1)) = 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> expression = "2*3-4*5"
<strong>Output:</strong> [-34,-14,-10,-10,10]
<strong>Explanation:</strong>
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 20</code></li>
	<li><code>expression</code> consists of digits and the operators <code>'+'</code>, <code>'-'</code>, and <code>'*'</code>.</li>
	<li>All the integer values in the input expression are in the range <code>[0, 99]</code>.</li>
</ul>"""

    input_format = "A single string representing the expression."
    output_format = "A single line containing space-separated integers representing all possible results (sorted in ascending order for consistency)."
    
    constraints = [
        "Expression length: [1, 20]",
        "Operators: +, -, *",
        "Numbers: [0, 99]",
        "Output values: 32-bit signed integers.",
        "Total results: <= 10^4."
    ]
    
    explanation = """To find all possible results of an expression by grouping elements with parentheses:
1. **Divide and Conquer**:
   - For every operator in the expression, split the expression into two halves: `left` and `right`.
   - Recursively find all possible results for the `left` part and the `right` part.
   - Combine the results from the left and right using the current operator.
2. **Base Case**:
   - If the expression contains no operators, it's just a number. Return the number as a single-element list.
3. **Memoization**:
   - Use a cache (dictionary or map) to store the results of sub-expressions to avoid redundant calculations.
4. **Complexity**:
   - Time Complexity: O(Catalan Number * N) in the worst case, though limited by constraints.
   - Space Complexity: O(Total results)."""
    
    answer = """def diffWaysToCompute(expression: str) -> list[int]:
    memo = {}
    
    def solve(expr):
        if expr in memo:
            return memo[expr]
        
        res = []
        for i in range(len(expr)):
            if expr[i] in "+-*":
                left = solve(expr[:i])
                right = solve(expr[i+1:])
                for l in left:
                    for r in right:
                        if expr[i] == '+':
                            res.append(l + r)
                        elif expr[i] == '-':
                            res.append(l - r)
                        elif expr[i] == '*':
                            res.append(l * r)
        
        if not res: # No operators found
            res.append(int(expr))
            
        memo[expr] = res
        return res
        
    final_res = solve(expression)
    return sorted(final_res)"""

    boilerplate = {
        "python": "import sys\n\ndef diffWaysToCompute(expression):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    expr = sys.stdin.read().strip()\n    if expr:\n        ans = diffWaysToCompute(expr)\n        print(\" \".join(map(str, sorted(ans))))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nvector<int> diffWaysToCompute(string expression) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string expr;\n    if (cin >> expr) {\n        vector<int> res = diffWaysToCompute(expr);\n        sort(res.begin(), res.end());\n        for (int i = 0; i < res.size(); i++) {\n            cout << res[i] << (i == res.size() - 1 ? \"\" : \" \");\n        }\n        cout << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public List<Integer> diffWaysToCompute(String expression) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String expr = br.readLine();\n        if (expr != null && !expr.trim().isEmpty()) {\n            List<Integer> res = new Solution().diffWaysToCompute(expr.trim());\n            Collections.sort(res);\n            for (int i = 0; i < res.size(); i++) {\n                System.out.print(res.get(i) + (i == res.size() - 1 ? \"\" : \" \"));\n            }\n            System.out.println();\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction diffWaysToCompute(expression) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    const res = diffWaysToCompute(input);\n    res.sort((a, b) => a - b);\n    console.log(res.join(\" \"));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint compare(const void* a, const void* b) {\n    return (*(int*)a - *(int*)b);\n}\n\nint* diffWaysToCompute(char* expression, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char expr[100];\n    if (scanf(\"%s\", expr) == 1) {\n        int size = 0;\n        int* res = diffWaysToCompute(expr, &size);\n        qsort(res, size, sizeof(int), compare);\n        for (int i = 0; i < size; i++) {\n            printf(\"%d%s\", res[i], i == size - 1 ? \"\" : \" \");\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2-1-1", "expected_output": "0 2", "is_sample": True},
        {"input": "2*3-4*5", "expected_output": "-34 -14 -10 -10 10", "is_sample": True},
        {"input": "11", "expected_output": "11", "is_sample": True},
        {"input": "2+3", "expected_output": "5", "is_sample": False},
        {"input": "0*1", "expected_output": "0", "is_sample": False},
        {"input": "1-1*1+1", "expected_output": "-1 0 0 1", "is_sample": False},
        {"input": "10+10+10", "expected_output": "30 30", "is_sample": False},
        # Stress cases
        {"input": "1-1-1-1-1", "expected_output": "-3 -1 -1 1 1 1 3 3 5", "is_sample": False},
        {"input": "2*2*2*2*2", "expected_output": "32 32 32 32 32 32 32 32 32 32 32 32 32 32", "is_sample": False},
        {"input": "1+2*3-4", "expected_output": "-7 -1 3 3 5", "is_sample": False}
    ]
    
    # Correcting stress case outputs (sorting as per standard)
    def _solve(expr):
        memo = {}
        def s(e):
            if e in memo: return memo[e]
            r = []
            for i in range(len(e)):
                if e[i] in "+-*":
                    L, R = s(e[:i]), s(e[i+1:])
                    for a in L:
                        for b in R:
                            if e[i] == '+': r.append(a+b)
                            elif e[i] == '-': r.append(a-b)
                            else: r.append(a*b)
            if not r: r.append(int(e))
            memo[e] = r
            return r
        return " ".join(map(str, sorted(s(expr))))

    test_cases[5]["expected_output"] = _solve("1-1*1+1")
    test_cases[7]["expected_output"] = _solve("1-1-1-1-1")
    test_cases[8]["expected_output"] = _solve("2*2*2*2*2")
    test_cases[9]["expected_output"] = _solve("1+2*3-4")

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
        "topics": ["Math", "String", "Dynamic Programming", "Recursion", "Memoization"],
        "companyIndex": 0
    }

    output_path = "1-200/241_Different_Ways_to_Add_Parentheses.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
