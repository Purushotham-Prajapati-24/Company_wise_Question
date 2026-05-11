import json
import os

def generate_json():
    problem_id = 119
    title = "Pascal's Triangle II"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>119. Pascal's Triangle II</h3>
<p>Given an integer <code>rowIndex</code>, return the <code>rowIndex<sup>th</sup></code> (<strong>0-indexed</strong>) row of the <strong>Pascal's triangle</strong>.</p>

<p>In <strong>Pascal's triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height: 330px; width: 330px;" />

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> rowIndex = 3
<strong>Output:</strong> [1,3,3,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> rowIndex = 0
<strong>Output:</strong> [1]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> rowIndex = 1
<strong>Output:</strong> [1,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= rowIndex &lt;= 33</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you optimize your algorithm to use only <code>O(rowIndex)</code> extra space?"""

    input_format = "A single integer rowIndex."
    output_format = "A list of integers representing the requested row of Pascal's triangle."
    
    constraints = [
        "0 <= rowIndex <= 33."
    ]
    
    explanation = """To generate the rowIndex-th row of Pascal's Triangle in O(rowIndex) space:
1. **Iterative Update In-Place**:
   - Initialize a row `[1]`.
   - For each increment from `1` to `rowIndex`:
     - Append `1` to the end of the current row.
     - Update the interior elements from right to left (to avoid overwrite issues): `row[j] = row[j] + row[j-1]`.
2. **Mathematical Approach (Alternative)**:
   - Use the formula for combinations: `C(n, k) = C(n, k-1) * (n - k + 1) / k`.
   - This allows generating the row in O(rowIndex) time and O(rowIndex) space without nested loops.
3. **Complexity**:
   - Time Complexity: O(rowIndex) using the formula, or O(rowIndex^2) using iterative loops.
   - Space Complexity: O(rowIndex) as we only store one row."""
    
    answer = """def getRow(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        # Using the combination formula: C(n, k) = C(n, k-1) * (n - k + 1) / k
        # Here n = rowIndex, k = i
        val = row[-1] * (rowIndex - i + 1) // i
        row.append(val)
    return row"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef getRow(rowIndex):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(json.dumps(getRow(int(line))))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\nvector<int> getRow(int rowIndex) {\n    // User logic here\n    return {};\n}\nint main() {\n    int rowIndex;\n    if(cin >> rowIndex) {\n        auto res = getRow(rowIndex);\n        cout << '[';\n        for(int i=0;i<(int)res.size();i++) cout<<res[i]<<(i+1<(int)res.size()?\", \":\"\");\n        cout << \"]\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static List<Integer> getRow(int rowIndex) {\n        // User logic here\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if(sc.hasNextInt()) {\n            List<Integer> res = getRow(sc.nextInt());\n            StringBuilder sb = new StringBuilder(\"[\");\n            for(int i=0;i<res.size();i++) sb.append(res.get(i)).append(i+1<res.size()?\", \":\"\");\n            sb.append(\"]\"); System.out.println(sb);\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction getRow(rowIndex) {\n    // User logic here\n    return [];\n}\nconst line = fs.readFileSync(0,'utf8').trim();\nif(line) console.log(JSON.stringify(getRow(parseInt(line))).replace(/,/g,', '));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\nint* getRow(int rowIndex, int* returnSize) {\n    // User logic here\n    *returnSize = 0; return NULL;\n}\nint main() {\n    int rowIndex;\n    if(scanf(\"%d\",&rowIndex)==1) {\n        int sz=0; int* res=getRow(rowIndex,&sz);\n        printf(\"[\");\n        for(int i=0;i<sz;i++) printf(\"%d%s\",res[i],i+1<sz?\", \":\"\");\n        printf(\"]\\n\");\n        if(res) free(res);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3", "expected_output": "[1, 3, 3, 1]", "is_sample": True},
        {"input": "0", "expected_output": "[1]", "is_sample": True},
        {"input": "1", "expected_output": "[1, 1]", "is_sample": False},
        {"input": "2", "expected_output": "[1, 2, 1]", "is_sample": False},
        {"input": "4", "expected_output": "[1, 4, 6, 4, 1]", "is_sample": False},
        {"input": "5", "expected_output": "[1, 5, 10, 10, 5, 1]", "is_sample": False},
        {"input": "6", "expected_output": "[1, 6, 15, 20, 15, 6, 1]", "is_sample": False},
        # Stress cases
        {"input": "20", "expected_output": "[1, 20, 190, 1140, 4845, 15504, 38760, 77520, 125970, 167960, 184756, 167960, 125970, 77520, 38760, 15504, 4845, 1140, 190, 20, 1]", "is_sample": False},
        {"input": "30", "expected_output": "[1, 30, 435, 4060, 27405, 142506, 593775, 2035800, 5852925, 14307150, 30045015, 54627300, 86493225, 119759850, 145422675, 155117520, 145422675, 119759850, 86493225, 54627300, 30045015, 14307150, 5852925, 2035800, 593775, 142506, 27405, 4060, 435, 30, 1]", "is_sample": False},
        {"input": "33", "expected_output": "[1, 33, 528, 5456, 40920, 237336, 1107568, 4272048, 13884156, 38967148, 92561040, 193536720, 354817320, 573327900, 819039857, 1037450485, 1167131796, 1167131796, 1037450485, 819039857, 573327900, 354817320, 193536720, 92561040, 38967148, 13884156, 4272048, 1107568, 237336, 40920, 5456, 528, 33, 1]", "is_sample": False}
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
        "topics": ["Array", "Math", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1-200/119_Pascal's_Triangle_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
