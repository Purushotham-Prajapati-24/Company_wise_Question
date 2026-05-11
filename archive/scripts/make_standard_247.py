import json
import os

def generate_json():
    problem_id = 247
    title = "Strobogrammatic Number II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>247. Strobogrammatic Number II</h3>
<p>Given an integer <code>n</code>, return all the strobogrammatic numbers that are of length <code>n</code>. You may return the answer in <strong>any order</strong>.</p>

<p>A <strong>strobogrammatic number</strong> is a number that looks the same when rotated 180 degrees (looked at upside down).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> ["11","69","88","96"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["0","1","8"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 14</code></li>
</ul>"""

    input_format = "A single integer n."
    output_format = "A stringified list of all strobogrammatic numbers of length n."
    
    constraints = [
        "1 <= n <= 14",
        "Number must be strobogrammatic.",
        "No leading zeros allowed except for n=1."
    ]
    
    explanation = """To generate strobogrammatic numbers of length n:
1. **Recursive Construction**: Build numbers from the "inside" out.
2. **Base Cases**:
   - `n = 0`: Return `""` (empty string).
   - `n = 1`: Return `["0", "1", "8"]`.
3. **Recursive Step**:
   - To get numbers of length `n`, recursively get numbers of length `n-2`.
   - For each number `s` from `n-2`, wrap it with all valid strobogrammatic pairs:
     - `1s1`, `8s8`, `6s9`, `9s6`
     - `0s0` (only if the outermost layer is not 0).
4. **Complexity**:
   - Time: O(5^(N/2)) since each step branches by ~5 options.
   - Space: O(N * 5^(N/2)) to store the results."""
    
    answer = """class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(n, final_len):
            if n == 0: return [""]
            if n == 1: return ["0", "1", "8"]
            
            res = []
            prev = helper(n - 2, final_len)
            for s in prev:
                if n != final_len:
                    res.append("0" + s + "0")
                res.append("1" + s + "1")
                res.append("6" + s + "9")
                res.append("8" + s + "8")
                res.append("9" + s + "6")
            return res
            
        return helper(n, n)"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef findStrobogrammatic(n: int):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        n = int(line)\n        res = findStrobogrammatic(n)\n        res.sort()\n        print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nvector<string> findStrobogrammatic(int n) {\n    // User logic\n    return {};\n}\n\nint main() {\n    int n;\n    if (cin >> n) {\n        vector<string> res = findStrobogrammatic(n);\n        sort(res.begin(), res.end());\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); i++) {\n            cout << \"\\\"\" << res[i] << \"\\\"\" << (i == res.size() - 1 ? \"\" : \",\");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public List<String> findStrobogrammatic(int n) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            List<String> res = new Solution().findStrobogrammatic(sc.nextInt());\n            Collections.sort(res);\n            System.out.print(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                System.out.print(\"\\\"\" + res.get(i) + \"\\\"\" + (i == res.size() - 1 ? \"\" : \",\"));\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction findStrobogrammatic(n) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    let res = findStrobogrammatic(parseInt(input));\n    res.sort();\n    console.log(JSON.stringify(res));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint cmp(const void* a, const void* b) {\n    return strcmp(*(const char**)a, *(const char**)b);\n}\n\nchar** findStrobogrammatic(int n, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        int returnSize = 0;\n        char** res = findStrobogrammatic(n, &returnSize);\n        if (res != NULL && returnSize > 0) {\n            qsort(res, returnSize, sizeof(char*), cmp);\n            printf(\"[\");\n            for (int i = 0; i < returnSize; i++) {\n                printf(\"\\\"%s\\\"%s\", res[i], i == returnSize - 1 ? \"\" : \",\");\n            }\n            printf(\"]\\n\");\n        } else {\n            printf(\"[]\\n\");\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2", "expected_output": '["11","69","88","96"]', "is_sample": True},
        {"input": "1", "expected_output": '["0","1","8"]', "is_sample": True},
        {"input": "3", "expected_output": '["101","111","181","609","619","689","808","818","888","906","916","986"]', "is_sample": False},
        {"input": "4", "expected_output": "...", "is_sample": False},
        {"input": "5", "expected_output": "...", "is_sample": False},
        {"input": "2", "expected_output": '["11","69","88","96"]', "is_sample": False},
        {"input": "1", "expected_output": '["0","1","8"]', "is_sample": False},
        # Stress Tests (Max n=14)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_strob2(m, total):
        if m == 0: return [""]
        if m == 1: return ["0", "1", "8"]
        res = []
        p = _solve_strob2(m-2, total)
        for s in p:
            if m != total: res.append("0" + s + "0")
            res.append("1" + s + "1")
            res.append("6" + s + "9")
            res.append("8" + s + "8")
            res.append("9" + s + "6")
        return res

    # Correct results
    test_cases[3] = {"input": "4", "expected_output": json.dumps(sorted(_solve_strob2(4, 4))).replace(' ', ''), "is_sample": False}
    test_cases[4] = {"input": "5", "expected_output": json.dumps(sorted(_solve_strob2(5, 5))).replace(' ', ''), "is_sample": False}
    
    # Stress 8: n=10 (Large number of results)
    test_cases[7] = {"input": "10", "expected_output": json.dumps(sorted(_solve_strob2(10, 10))).replace(' ', ''), "is_sample": False}
    test_cases[8] = {"input": "6", "expected_output": json.dumps(sorted(_solve_strob2(6, 6))).replace(' ', ''), "is_sample": False}
    test_cases[9] = {"input": "8", "expected_output": json.dumps(sorted(_solve_strob2(8, 8))).replace(' ', ''), "is_sample": False}

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
            "time_limit_ms": 2000,
            "memory_limit_mb": 512,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Two Pointers", "String", "Recursion"],
        "companyIndex": 0
    }

    output_path = "201-400/247_Strobogrammatic_Number_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
