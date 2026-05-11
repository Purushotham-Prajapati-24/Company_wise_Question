import json
import os

def generate_json():
    problem_id = 135
    title = "Candy"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>135. Candy</h3>
<p>There are <code>n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code>ratings</code>.</p>

<p>You are giving candies to these children subjected to the following requirements:</p>

<ul>
	<li>Each child must have at least one candy.</li>
	<li>Children with a higher rating get more candies than their neighbors.</li>
</ul>

<p>Return <em>the minimum number of candies you need to have to distribute the candies to the children</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> ratings = [1,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> ratings = [1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == ratings.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing an array of ratings."
    output_format = "An integer representing the minimum number of candies."
    
    constraints = [
        "1 <= n <= 2 * 10^4",
        "0 <= ratings[i] <= 2 * 10^4"
    ]
    
    explanation = """To minimize the candies distributed:
1. **Two-Pass Greedy**:
   - **Forward Pass**: Initialize `candies` array with 1 for each child. Iterate from left to right. If a child's rating is higher than their predecessor (`ratings[i] > ratings[i-1]`), set `candies[i] = candies[i-1] + 1`.
   - **Backward Pass**: Iterate from right to left. If a child's rating is higher than their successor (`ratings[i] > ratings[i+1]`), set `candies[i] = max(candies[i], candies[i+1] + 1)`.
2. **Summation**: The total candies is the sum of the `candies` array after both passes.
3. **Complexity**:
   - Time Complexity: O(N) for two linear passes.
   - Space Complexity: O(N) to store the candy count for each child."""
    
    answer = """class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # Forward pass: check left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
                
        # Backward pass: check right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
                
        return sum(candies)"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef candy(ratings):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if not line: sys.exit()\n    ratings = json.loads(line)\n    print(candy(ratings))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <numeric>\n#include <algorithm>\n#include <sstream>\nusing namespace std;\nint candy(vector<int>& ratings){\n    // User logic here\n    return 0;\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    line=line.substr(1,line.size()-2);\n    stringstream ss(line); string t; vector<int> r;\n    while(getline(ss,t,',')) if(!t.empty()) r.push_back(stoi(t));\n    cout<<candy(r)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int candy(int[] ratings) {\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine().trim();\n        line=line.substring(1,line.length()-1);\n        String[] parts=line.split(\",\");\n        int[] r=new int[parts.length];\n        for(int i=0;i<parts.length;i++) r[i]=Integer.parseInt(parts[i].trim());\n        System.out.println(candy(r));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction candy(ratings){\n    // User logic here\n    return 0;\n}\nconst line=fs.readFileSync(0,'utf8').trim();\nconsole.log(candy(JSON.parse(line)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint candy(int* ratings, int ratingsSize){\n    // User logic here\n    return 0;\n}\nint main(){\n    char buf[500000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int arr[20001],cnt=0; char*tok=strtok(buf,\"[],\\n\\r \");\n    while(tok&&cnt<20001){arr[cnt++]=atoi(tok);tok=strtok(NULL,\"[],\\n\\r \");}\n    printf(\"%d\\n\",candy(arr,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "[1,0,2]", "expected_output": "5", "is_sample": True},
        {"input": "[1,2,2]", "expected_output": "4", "is_sample": True},
        {"input": "[1,1,1,1]", "expected_output": "4", "is_sample": False},
        {"input": "[1,2,3,4,5]", "expected_output": "15", "is_sample": False},
        {"input": "[5,4,3,2,1]", "expected_output": "15", "is_sample": False},
        {"input": "[1,3,2,2,1]", "expected_output": "7", "is_sample": False},
        {"input": "[1,2,8,7,6,5,4]", "expected_output": "18", "is_sample": False},
        # Stress Tests (N=20000)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(ratings):
        n = len(ratings)
        c = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]: c[i] = c[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]: c[i] = max(c[i], c[j:=i+1]+1 if True else 0) # simplified logic
            if ratings[i] > ratings[i+1]: c[i] = max(c[i], c[i+1] + 1)
        return sum(c)

    # Stress 8: Strictly increasing
    r8 = list(range(20000))
    test_cases[7] = {"input": json.dumps(r8), "expected_output": str(_solve(r8)), "is_sample": False}
    # Stress 9: Strictly decreasing
    r9 = list(range(20000, 0, -1))
    test_cases[8] = {"input": json.dumps(r9), "expected_output": str(_solve(r9)), "is_sample": False}
    # Stress 10: Mountain shape
    r10 = list(range(10000)) + list(range(10000, 0, -1))
    test_cases[9] = {"input": json.dumps(r10), "expected_output": str(_solve(r10)), "is_sample": False}

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
        "topics": ["Array", "Greedy"],
        "companyIndex": 0
    }

    output_path = "1-200/135_Candy.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
