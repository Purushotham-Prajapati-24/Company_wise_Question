import json
import os

def generate_json():
    problem_id = 118
    title = "Pascal's Triangle"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>118. Pascal's Triangle</h3>
<p>Given an integer <code>numRows</code>, return the first <code>numRows</code> of <strong>Pascal's triangle</strong>.</p>

<p>In <strong>Pascal's triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height: 330px; width: 330px;" />

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> numRows = 5
<strong>Output:</strong> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> numRows = 1
<strong>Output:</strong> [[1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= numRows &lt;= 30</code></li>
</ul>"""

    input_format = "A single integer numRows."
    output_format = "A list of lists representing Pascal's triangle."
    
    constraints = [
        "1 <= numRows <= 30."
    ]
    
    explanation = """To generate Pascal's Triangle:
1. **Iterative Construction**:
   - The first row is always `[1]`.
   - Each subsequent row `i` starts and ends with `1`.
   - Any inner element at index `j` in row `i` is the sum of elements at indices `j-1` and `j` in the previous row `i-1`.
2. **Implementation Details**:
   - Initialize the `triangle` list.
   - Loop from `0` to `numRows - 1`.
   - For each row, calculate elements based on the previous row.
3. **Complexity**:
   - Time Complexity: O(numRows^2) as we generate every element once.
   - Space Complexity: O(numRows^2) to store the result."""
    
    answer = """def generate(numRows):
    if numRows == 0:
        return []
        
    triangle = [[1]]
    
    for i in range(1, numRows):
        prev_row = triangle[-1]
        new_row = [1]
        
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
            
        new_row.append(1)
        triangle.append(new_row)
        
    return triangle"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef generate(numRows):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(json.dumps(generate(int(line))))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\nusing namespace std;\nvector<vector<int>> generate(int numRows) { return {}; }\nint main() {\n    int numRows;\n    if(cin >> numRows) {\n        vector<vector<int>> res = generate(numRows);\n        cout << \"[\";\n        for(int i=0;i<(int)res.size();i++){\n            cout << \"[\";\n            for(int j=0;j<(int)res[i].size();j++) cout << res[i][j] << (j+1<(int)res[i].size() ? \", \" : \"\");\n            cout << \"]\" << (i+1<(int)res.size() ? \", \" : \"\");\n        }\n        cout << \"]\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static List<List<Integer>> generate(int numRows) { return new ArrayList<>(); }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in);\n        if(sc.hasNextInt()) {\n            List<List<Integer>> res = generate(sc.nextInt());\n            StringBuilder sb=new StringBuilder(\"[\");\n            for(int i=0;i<res.size();i++){\n                sb.append(\"[\");\n                for(int j=0;j<res.get(i).size();j++) sb.append(res.get(i).get(j)).append(j+1<res.get(i).size() ? \", \" : \"\");\n                sb.append(\"]\").append(i+1<res.size() ? \", \" : \"\");\n            }\n            sb.append(\"]\"); System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction generate(numRows) { return []; }\nconst tokens = fs.readFileSync(0,'utf8').trim().split(/\\s+/);\nif(tokens.length>0 && tokens[0]!==''){\n  const numRows = parseInt(tokens[0]);\n  console.log(JSON.stringify(generate(numRows)).replace(/,/g, \", \"));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\nint** generate(int numRows, int* returnSize, int** returnColumnSizes) { *returnSize=0; return NULL; }\nint main() {\n    int numRows;\n    if(scanf(\"%d\", &numRows)==1) {\n        int returnSize=0; int* returnColumnSizes=NULL;\n        int** res = generate(numRows, &returnSize, &returnColumnSizes);\n        printf(\"[\");\n        for(int i=0;i<returnSize;i++){\n            printf(\"[\");\n            for(int j=0;j<returnColumnSizes[i];j++) printf(\"%d%s\", res[i][j], j+1<returnColumnSizes[i] ? \", \" : \"\");\n            printf(\"]%s\", i+1<returnSize ? \", \" : \"\");\n            if(res[i]) free(res[i]);\n        }\n        printf(\"]\\n\");\n        if(res) free(res);\n        if(returnColumnSizes) free(returnColumnSizes);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "5", "expected_output": "[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]", "is_sample": True},
        {"input": "1", "expected_output": "[[1]]", "is_sample": True},
        {"input": "2", "expected_output": "[[1], [1, 1]]", "is_sample": False},
        {"input": "3", "expected_output": "[[1], [1, 1], [1, 2, 1]]", "is_sample": False},
        {"input": "4", "expected_output": "[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]", "is_sample": False},
        {"input": "6", "expected_output": "[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]", "is_sample": False},
        {"input": "7", "expected_output": "[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]", "is_sample": False},
        # Stress cases
        {"input": "20", "expected_output": "...", "is_sample": False},
        {"input": "25", "expected_output": "...", "is_sample": False},
        {"input": "30", "expected_output": "...", "is_sample": False}
    ]
    
    # Generate stress outputs
    def _solve(n):
        if n == 0: return []
        t = [[1]]
        for i in range(1, n):
            p = t[-1]
            r = [1]
            for j in range(1, i): r.append(p[j-1] + p[j])
            r.append(1)
            t.append(r)
        return t

    test_cases[7]["expected_output"] = str(_solve(20))
    test_cases[8]["expected_output"] = str(_solve(25))
    test_cases[9]["expected_output"] = str(_solve(30))

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
        "topics": ["Array", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1-200/118_Pascal's_Triangle.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
