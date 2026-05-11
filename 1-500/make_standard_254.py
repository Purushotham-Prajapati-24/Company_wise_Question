import json
import os
import math

def generate_json():
    problem_id = 254
    title = "Factor Combinations"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>254. Factor Combinations</h3>
<p>Numbers can be regarded as the product of their factors.</p>

<p>For example, <code>8 = 2 x 2 x 2 = 2 x 4</code>.</p>

<p>Given an integer <code>n</code>, return <em>all possible combinations of its factors</em>. You may return the answer in <strong>any order</strong>.</p>

<p><strong>Notes:</strong></p>

<ul>
	<li>You should <b>not</b> include <code>1</code> and <code>n</code>.</li>
	<li>Factors in a combination must be in <strong>non-decreasing</strong> order to avoid duplicate permutations.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 12
<strong>Output:</strong> [[2,2,3],[2,6],[3,4]]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 37
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 4:</strong></p>
<pre><strong>Input:</strong> n = 32
<strong>Output:</strong> [[2,2,2,2,2],[2,2,2,4],[2,2,8],[2,16],[4,4],[4,8]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>7</sup></code></li>
</ul>"""

    input_format = "A single integer n."
    output_format = "A stringified 2D array of all possible factor combinations."
    
    constraints = [
        "1 <= n <= 10,000,000",
        "Result must exclude combinations of only [n] or [1, n].",
        "Factors must be non-decreasing."
    ]
    
    explanation = """To find all factor combinations while avoiding duplicates:
1. **Backtracking (DFS)**: Maintain a `start` factor (initially 2).
2. **Logic**:
   - For a given target `n`, loop from `i = start` to `sqrt(n)`.
   - If `i` is a factor:
     - The first combination is `[i, n // i]`.
     - Then, recursively find combinations for `n // i` starting from `i` (to ensure non-decreasing order) and prepend `i`.
3. **Corner Cases**: If `n <= 1`, return empty list immediately.
4. **Complexity**: O(2^sqrt(n)) worst case but efficient in practice due to factor properties."""
    
    answer = """import math

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(target, start):
            res = []
            for i in range(start, int(math.sqrt(target)) + 1):
                if target % i == 0:
                    res.append([i, target // i])
                    sub = backtrack(target // i, i)
                    for s in sub:
                        res.append([i] + s)
            return res
            
        return backtrack(n, 2)"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef getFactors(n: int) -> list[list[int]]:\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    match = re.search(r'\\d+', raw_input)\n    if match:\n        n = int(match.group())\n        res = getFactors(n)\n        def sort_key(x): return (len(x), x)\n        res.sort(key=sort_key)\n        print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nvector<vector<int>> getFactors(int n) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    regex re_num(\"\\\\d+\");\n    smatch match;\n    if (regex_search(input, match, re_num)) {\n        int n = stoi(match.str());\n        vector<vector<int>> res = getFactors(n);\n        sort(res.begin(), res.end(), [](const vector<int>& a, const vector<int>& b) {\n            if (a.size() != b.size()) return a.size() < b.size();\n            for (size_t i = 0; i < a.size(); i++) {\n                if (a[i] != b[i]) return a[i] < b[i];\n            }\n            return false;\n        });\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); i++) {\n            cout << \"[\";\n            for (size_t j = 0; j < res[i].size(); j++) {\n                cout << res[i][j] << (j == res[i].size() - 1 ? \"\" : \",\");\n            }\n            cout << \"]\" << (i == res.size() - 1 ? \"\" : \",\");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public List<List<Integer>> getFactors(int n) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        Matcher m = Pattern.compile(\"\\\\d+\").matcher(input);\n        if (m.find()) {\n            int n = Integer.parseInt(m.group());\n            List<List<Integer>> res = new Solution().getFactors(n);\n            res.sort((a, b) -> {\n                if (a.size() != b.size()) return Integer.compare(a.size(), b.size());\n                for (int i = 0; i < a.size(); i++) {\n                    if (!a.get(i).equals(b.get(i))) return Integer.compare(a.get(i), b.get(i));\n                }\n                return 0;\n            });\n            StringBuilder resultSb = new StringBuilder(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                resultSb.append(\"[\");\n                for (int j = 0; j < res.get(i).size(); j++) {\n                    resultSb.append(res.get(i).get(j)).append(j == res.get(i).size() - 1 ? \"\" : \",\");\n                }\n                resultSb.append(\"]\").append(i == res.size() - 1 ? \"\" : \",\");\n            }\n            resultSb.append(\"]\");\n            System.out.println(resultSb.toString());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction getFactors(n) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst match = input.match(/\\d+/);\nif (match) {\n    let res = getFactors(parseInt(match[0]));\n    res.sort((a, b) => {\n        if (a.length !== b.length) return a.length - b.length;\n        for (let i = 0; i < a.length; i++) {\n            if (a[i] !== b[i]) return a[i] - b[i];\n        }\n        return 0;\n    });\n    console.log(JSON.stringify(res).replace(/\\s+/g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\nint cmp(const void* a, const void* b) {\n    int* rowA = *(int**)a;\n    int* rowB = *(int**)b;\n    int lenA = rowA[0];\n    int lenB = rowB[0];\n    if (lenA != lenB) return lenA - lenB;\n    for (int i = 1; i <= lenA; i++) {\n        if (rowA[i] != rowB[i]) return rowA[i] - rowB[i];\n    }\n    return 0;\n}\n\nint** getFactors(int n, int* returnSize, int** returnColumnSizes) {\n    *returnSize = 0;\n    *returnColumnSizes = NULL;\n    return NULL;\n}\n\nint main() {\n    static char buffer[1000];\n    int bytes = fread(buffer, 1, sizeof(buffer)-1, stdin);\n    buffer[bytes] = '\\0';\n    \n    char* p = buffer;\n    while (*p && !isdigit(*p)) p++;\n    if (*p) {\n        int n = atoi(p);\n        int returnSize = 0;\n        int* returnColumnSizes = NULL;\n        int** res = getFactors(n, &returnSize, &returnColumnSizes);\n        \n        if (returnSize == 0) {\n            printf(\"[]\\n\");\n            return 0;\n        }\n        \n        int** sortWrapper = (int**)malloc(returnSize * sizeof(int*));\n        for (int i = 0; i < returnSize; i++) {\n            sortWrapper[i] = (int*)malloc((returnColumnSizes[i] + 1) * sizeof(int));\n            sortWrapper[i][0] = returnColumnSizes[i];\n            for (int j = 0; j < returnColumnSizes[i]; j++) {\n                sortWrapper[i][j+1] = res[i][j];\n            }\n        }\n        \n        qsort(sortWrapper, returnSize, sizeof(int*), cmp);\n        \n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"[\");\n            for (int j = 0; j < sortWrapper[i][0]; j++) {\n                printf(\"%d%s\", sortWrapper[i][j+1], j == sortWrapper[i][0] - 1 ? \"\" : \",\");\n            }\n            printf(\"]%s\", i == returnSize - 1 ? \"\" : \",\");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1", "expected_output": "[]", "is_sample": True},
        {"input": "12", "expected_output": '[[2,6],[2,2,3],[3,4]]', "is_sample": True},
        {"input": "37", "expected_output": "[]", "is_sample": True},
        {"input": "32", "expected_output": '[[2,16],[2,2,8],[2,2,2,4],[2,2,2,2,2],[4,8],[4,4]]', "is_sample": True},
        {"input": "100", "expected_output": '[[2,50],[2,2,25],[2,2,5,5],[2,5,10],[4,25],[4,5,5],[5,20],[10,10]]', "is_sample": False},
        {"input": "8", "expected_output": '[[2,4],[2,2,2]]', "is_sample": False},
        {"input": "2384", "expected_output": "...", "is_sample": False},
        # Stress Tests (Up to 1e7)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_factors(n):
        if n <= 1: return []
        def dfs(t, s):
            r = []
            for i in range(s, int(math.sqrt(t)) + 1):
                if t % i == 0:
                    r.append([i, t // i])
                    for sub in dfs(t // i, i): r.append([i] + sub)
            return r
        return dfs(n, 2)

    def _sort_res(r):
        return sorted(r, key=lambda x: (len(x), x))

    test_cases[6] = {"input": "2384", "expected_output": json.dumps(_sort_res(_solve_factors(2384))).replace(' ', ''), "is_sample": False}
    # Stress 8: Large prime
    test_cases[7] = {"input": "9999991", "expected_output": "[]", "is_sample": False}
    # Stress 9: Highly composite
    test_cases[8] = {"input": "72072", "expected_output": json.dumps(_sort_res(_solve_factors(72072))).replace(' ', ''), "is_sample": False}
    # Stress 10: 1e7
    test_cases[9] = {"input": "10000000", "expected_output": json.dumps(_sort_res(_solve_factors(10000000))).replace(' ', ''), "is_sample": False}

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
        "topics": ["Math", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "201-400/254_Factor_Combinations.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
