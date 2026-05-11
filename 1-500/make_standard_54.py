import json
import os

def generate_json():
    problem_id = 54
    title = "Spiral Matrix"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>54. Spiral Matrix</h3>
<p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the </em><code>matrix</code><em> in spiral order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>"""

    input_format = "A 2D array of integers matrix."
    output_format = "An array of integers in spiral order."
    
    constraints = [
        "1 <= m, n <= 10",
        "-100 <= matrix[i][j] <= 100"
    ]
    
    explanation = """To traverse a matrix in spiral order:
1. **Define Boundaries**: `top = 0`, `bottom = m-1`, `left = 0`, `right = n-1`.
2. **Loop**: While `top <= bottom` and `left <= right`:
   - Traverse **Right**: From `left` to `right` along `top`. Increment `top`.
   - Traverse **Down**: From `top` to `bottom` along `right`. Decrement `right`.
   - If `top <= bottom`:
     - Traverse **Left**: From `right` to `left` along `bottom`. Decrement `bottom`.
   - If `left <= right`:
     - Traverse **Up**: From `bottom` to `top` along `left`. Increment `left`.
3. **Complexity**:
   - **Time**: $O(M \times N)$
   - **Space**: $O(1)$ additional space (result array excluded)."""
    
    answer = """def spiralOrder(matrix):
    if not matrix: return []
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Right
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        
        # Down
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            
        if left <= right:
            # Up
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
    return res"""

    boilerplate = {
        "python": "import sys, re, json\n\ndef spiralOrder(matrix):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if not data:\n        print(\"[]\")\n    else:\n        try:\n            matrix = json.loads(data)\n            if not (isinstance(matrix, list) and matrix and isinstance(matrix[0], list)):\n                raise ValueError\n        except:\n            rows = []\n            if '[' in data:\n                matches = re.findall(r'\\[([^\\[\\]]+)\\]', data)\n                for m in matches:\n                    row = [int(x) for x in re.findall(r'-?\\d+', m)]\n                    if row: rows.append(row)\n            else:\n                for line in data.splitlines():\n                    row = [int(x) for x in re.findall(r'-?\\d+', line)]\n                    if row: rows.append(row)\n            matrix = rows\n        print(json.dumps(spiralOrder(matrix)).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> spiralOrder(vector<vector<int>>& matrix) {\n        // User Logic Here\n        return {};\n    }\n};\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \"\\n\";\n    vector<vector<int>> matrix;\n    regex row_rgx(\"\\\\[([^\\\\[\\\\]]+)\\\\]\");\n    auto row_begin = sregex_iterator(input.begin(), input.end(), row_rgx);\n    auto row_end = sregex_iterator();\n    if (row_begin != row_end) {\n        for (auto i = row_begin; i != row_end; ++i) {\n            string row_str = i->str(1);\n            regex num_rgx(\"-?\\\\d+\");\n            vector<int> row;\n            auto num_begin = sregex_iterator(row_str.begin(), row_str.end(), num_rgx);\n            auto num_end = sregex_iterator();\n            for (auto j = num_begin; j != num_end; ++j) row.push_back(stoi(j->str()));\n            if (!row.empty()) matrix.push_back(row);\n        }\n    } else {\n        stringstream ss(input);\n        while (getline(ss, line)) {\n            regex num_rgx(\"-?\\\\d+\");\n            vector<int> row;\n            auto num_begin = sregex_iterator(line.begin(), line.end(), num_rgx);\n            auto num_end = sregex_iterator();\n            for (auto j = num_begin; j != num_end; ++j) row.push_back(stoi(j->str()));\n            if (!row.empty()) matrix.push_back(row);\n        }\n    }\n    Solution sol;\n    vector<int> res = sol.spiralOrder(matrix);\n    cout << \"[\";\n    for (size_t i = 0; i < res.size(); i++) cout << res[i] << (i == res.size() - 1 ? \"\" : \",\");\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public List<Integer> spiralOrder(int[][] matrix) {\n        // User Logic Here\n        return new ArrayList<>();\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\"\\n\");\n        String input = sb.toString();\n        List<int[]> matrixList = new ArrayList<>();\n        Matcher mRow = Pattern.compile(\"\\\\[([^\\\\[\\\\]]+)\\\\]\").matcher(input);\n        boolean foundRows = false;\n        while (mRow.find()) {\n            foundRows = true;\n            Matcher mNum = Pattern.compile(\"-?\\\\d+\").matcher(mRow.group(1));\n            List<Integer> row = new ArrayList<>();\n            while (mNum.find()) row.add(Integer.parseInt(mNum.group()));\n            if (!row.isEmpty()) {\n                int[] r = new int[row.size()];\n                for (int i = 0; i < row.size(); i++) r[i] = row.get(i);\n                matrixList.add(r);\n            }\n        }\n        if (!foundRows) {\n            for (String line : input.split(\"\\n\")) {\n                Matcher mNum = Pattern.compile(\"-?\\\\d+\").matcher(line);\n                List<Integer> row = new ArrayList<>();\n                while (mNum.find()) row.add(Integer.parseInt(mNum.group()));\n                if (!row.isEmpty()) {\n                    int[] r = new int[row.size()];\n                    for (int i = 0; i < row.size(); i++) r[i] = row.get(i);\n                    matrixList.add(r);\n                }\n            }\n        }\n        int[][] matrix = new int[matrixList.size()][];\n        for (int i = 0; i < matrixList.size(); i++) matrix[i] = matrixList.get(i);\n        Solution sol = new Solution();\n        List<Integer> res = sol.spiralOrder(matrix);\n        System.out.println(res.toString().replace(\" \", \"\"));\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number[][]} matrix\n * @return {number[]}\n */\nvar spiralOrder = function(matrix) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    let matrix = [];\n    try {\n        const parsed = JSON.parse(input);\n        if (Array.isArray(parsed) && parsed.length > 0 && Array.isArray(parsed[0])) matrix = parsed;\n    } catch (e) {}\n    if (matrix.length === 0) {\n        const rowMatches = input.match(/\\\\[([^\\\\[\\\\]]+)\\\\]/g);\n        if (rowMatches) matrix = rowMatches.map(r => (r.match(/-?\\d+/g) || []).map(Number));\n        else matrix = input.split('\\n').map(l => (l.match(/-?\\d+/g) || []).map(Number)).filter(r => r.length > 0);\n    }\n    console.log(JSON.stringify(spiralOrder(matrix)).replace(/\\s/g, ''));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {\n    // User Logic Here\n    return NULL;\n}\n\nint main() {\n    int max_rows = 100, max_cols = 100;\n    int** matrix = malloc(max_rows * sizeof(int*));\n    int* colSizes = malloc(max_rows * sizeof(int));\n    int m = 0;\n    char line[4096];\n    while (m < max_rows && fgets(line, sizeof(line), stdin)) {\n        int* row = malloc(max_cols * sizeof(int));\n        int n = 0, found = 0, sign = 1;\n        long long current = 0;\n        char* p = line;\n        while (*p) {\n            if (isdigit(*p)) {\n                if (!found) { found = 1; current = *p - '0'; } else current = current * 10 + (*p - '0');\n            } else if (*p == '-') {\n                if (found) { if (n < max_cols) row[n++] = (int)(current * sign); found = 0; sign = 1; }\n                if (isdigit(*(p+1))) { sign = -1; }\n            } else {\n                if (found) { if (n < max_cols) row[n++] = (int)(current * sign); found = 0; sign = 1; }\n            }\n            p++;\n        }\n        if (found) { if (n < max_cols) row[n++] = (int)(current * sign); }\n        if (n > 0) { matrix[m] = row; colSizes[m++] = n; } else free(row);\n    }\n    int returnSize = 0;\n    int* res = spiralOrder(matrix, m, colSizes, &returnSize);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) printf(\"%d%s\", res[i], (i == returnSize - 1 ? \"\" : \",\"));\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3\n4 5 6\n7 8 9", "expected_output": "[1,2,3,6,9,8,7,4,5]", "is_sample": True},
        {"input": "1 2 3 4\n5 6 7 8\n9 10 11 12", "expected_output": "[1,2,3,4,8,12,11,10,9,5,6,7]", "is_sample": True},
        {"input": "1", "expected_output": "[1]", "is_sample": False},
        {"input": "1 2\n3 4", "expected_output": "[1,2,4,3]", "is_sample": False},
        {"input": "1 2 3", "expected_output": "[1,2,3]", "is_sample": False},
        {"input": "1\n2\n3", "expected_output": "[1,2,3]", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "[1,2,3,4,5]", "is_sample": False},
        {"input": "1\n2\n3\n4\n5", "expected_output": "[1,2,3,4,5]", "is_sample": False},
        {"input": "1 2\n3 4\n5 6", "expected_output": "[1,2,4,6,5,3]", "is_sample": False},
        {"input": "10 20\n30 40", "expected_output": "[10,20,40,30]", "is_sample": False}
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
        "topics": ["Array", "Matrix", "Simulation"],
        "companyIndex": 0
    }

    output_path = "1-200/54_Spiral_Matrix.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
