import json
import os

def generate_json():
    problem_id = 120
    title = "Triangle"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>120. Triangle</h3>
<p>Given a <code>triangle</code> array, return <em>the minimum path sum from top to bottom</em>.</p>

<p>For each step, you may move to an adjacent number of the row below. More formally, if you are at index <code>i</code> on the current row, you may move to either index <code>i</code> or index <code>i + 1</code> on the next row.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The triangle looks like:
   <u>2</u>
  <u>3</u> 4
 6 <u>5</u> 7
4 <u>1</u> 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> triangle = [[-10]]
<strong>Output:</strong> -10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= triangle.length &lt;= 200</code></li>
	<li><code>triangle[0].length == 1</code></li>
	<li><code>triangle[i].length == triangle[i - 1].length + 1</code></li>
	<li><code>-10<sup>4</sup> &lt;= triangle[i][j] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do this using only <code>O(n)</code> extra space, where <code>n</code> is the total number of rows in the triangle? """

    input_format = "A single line containing a bracketed array of arrays representing the triangle."
    output_format = "An integer representing the minimum path sum."
    
    constraints = [
        "1 <= triangle.length <= 200",
        "-10^4 <= triangle[i][j] <= 10^4."
    ]
    
    explanation = """To find the minimum path sum in a triangle using O(N) space:
1. **Dynamic Programming (Bottom-Up)**:
   - Instead of starting from the top, start from the **bottom-most row**.
   - The "minimum path sum" from any node in the second-to-last row is its own value plus the minimum of its two children in the row below.
   - We can use a 1D array `dp` initialized with the values of the last row.
   - For each row `i` from `n-2` down to `0`:
     - Update `dp[j] = triangle[i][j] + min(dp[j], dp[j+1])` for all elements in that row.
   - Finally, `dp[0]` will contain the result.
2. **Space Efficiency**:
   - By updating the `dp` array in-place (or using an array of size `N`), we achieve O(N) space complexity where `N` is the number of rows.
3. **Complexity**:
   - Time Complexity: O(N^2) where N is the number of rows (total elements visited once).
   - Space Complexity: O(N) for the DP array."""
    
    answer = """def minimumTotal(triangle):
    n = len(triangle)
    # Start with the last row
    dp = list(triangle[-1])
    
    # Iterate from the second-to-last row up to the top
    for row in range(n - 2, -1, -1):
        for col in range(row + 1):
            dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
            
    return dp[0]"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef minimumTotal(triangle):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(minimumTotal(json.loads(line)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <sstream>\nusing namespace std;\nint minimumTotal(vector<vector<int>>& triangle) {\n    // User logic here\n    return 0;\n}\nint main() {\n    string line; if(!getline(cin,line)){return 0;}\n    // Parse [[a],[b,c],...] stripping brackets/spaces\n    string s; for(char c:line) if(c!=' ')s+=c;\n    vector<vector<int>> tri; vector<int> row;\n    int i=0,n=s.size();\n    while(i<n){\n        if(s[i]=='['){ if(i>0&&s[i-1]!='[') row.clear(); i++; }\n        else if(s[i]==']'){ if(!row.empty()){tri.push_back(row);row.clear();} i++; }\n        else if(s[i]==','){ i++; }\n        else{\n            int sign=1; if(s[i]=='-'){sign=-1;i++;}\n            int num=0; while(i<n&&isdigit(s[i])) num=num*10+(s[i++]-'0');\n            row.push_back(sign*num);\n        }\n    }\n    // Remove the extra outer wrapper if any\n    vector<vector<int>> t; for(auto&r:tri) if(!r.empty()) t.push_back(r);\n    cout << minimumTotal(t) << endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int minimumTotal(List<List<Integer>> triangle) {\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if(!sc.hasNextLine()) return;\n        String line = sc.nextLine().replaceAll(\"\\\\s\",\"\");\n        List<List<Integer>> tri = new ArrayList<>();\n        // parse [[a],[b,c]] format\n        int i=1; // skip outer '[' \n        while(i<line.length()-1){\n            if(line.charAt(i)=='['){ \n                int end=line.indexOf(']',i); \n                String inner=line.substring(i+1,end);\n                List<Integer> row=new ArrayList<>();\n                if(!inner.isEmpty()) for(String x:inner.split(\",\")) row.add(Integer.parseInt(x));\n                tri.add(row); i=end+2;\n            } else i++;\n        }\n        System.out.println(minimumTotal(tri));\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction minimumTotal(triangle) {\n    // User logic here\n    return 0;\n}\nconst line = fs.readFileSync(0,'utf8').trim();\nif(line) console.log(minimumTotal(JSON.parse(line)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n#define MIN(a,b) ((a)<(b)?(a):(b))\nint minimumTotal(int** triangle, int triangleSize, int* triangleColSizes) {\n    // User logic here\n    return 0;\n}\nint main() {\n    char buf[200000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    // Extract all numbers in order\n    int flat[20201]; int cnt=0; char*p=buf;\n    while(*p){\n        if(isdigit(*p)||(*p=='-'&&isdigit(*(p+1)))){\n            int sign=1; if(*p=='-'){sign=-1;p++;}\n            int num=0; while(isdigit(*p)) num=num*10+(*p++)-'0';\n            flat[cnt++]=sign*num;\n        } else p++;\n    }\n    // Reconstruct triangle: row i has i+1 elements\n    int rows=0; int tmp=cnt;\n    while(tmp>0){tmp-=rows+1;rows++;}\n    int** tri=(int**)malloc(rows*sizeof(int*));\n    int* colSz=(int*)malloc(rows*sizeof(int));\n    int idx=0;\n    for(int i=0;i<rows;i++){\n        tri[i]=(int*)malloc((i+1)*sizeof(int));\n        colSz[i]=i+1;\n        for(int j=0;j<=i;j++) tri[i][j]=flat[idx++];\n    }\n    printf(\"%d\\n\",minimumTotal(tri,rows,colSz));\n    for(int i=0;i<rows;i++) free(tri[i]); free(tri); free(colSz);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[2],[3,4],[6,5,7],[4,1,8,3]]", "expected_output": "11", "is_sample": True},
        {"input": "[[-10]]", "expected_output": "-10", "is_sample": True},
        {"input": "[[1],[2,3]]", "expected_output": "3", "is_sample": False},
        {"input": "[[1],[3,2]]", "expected_output": "3", "is_sample": False},
        {"input": "[[1],[2,3],[4,5,6]]", "expected_output": "7", "is_sample": False},
        {"input": "[[-1],[2,3],[1,-1,-3]]", "expected_output": "-2", "is_sample": False},
        {"input": "[[5],[4,6],[3,5,7]]", "expected_output": "12", "is_sample": False},
        # Stress cases
        {"input": json.dumps([[i]*(i+1) for i in range(200)]), "expected_output": str(sum(range(200))), "is_sample": False},
        {"input": json.dumps([[10000]*(i+1) for i in range(200)]), "expected_output": "2000000", "is_sample": False},
        {"input": json.dumps([[-10000]*(i+1) for i in range(200)]), "expected_output": "-2000000", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1-200/120_Triangle.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
