import json
import os

def generate_json():
    problem_id = 399
    title = "Evaluate Division"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>399. Evaluate Division</h3>
<p>You are given an array of variable pairs <code>equations</code> and an array of real numbers <code>values</code>, where <code>equations[i] = [A<sub>i</sub>, B<sub>i</sub>]</code> and <code>values[i]</code> represent the equation <code>A<sub>i</sub> / B<sub>i</sub> = values[i]</code>. Each <code>A<sub>i</sub></code> or <code>B<sub>i</sub></code> is a string that represents a single variable.</p>

<p>You are also given some <code>queries</code>, where <code>queries[j] = [C<sub>j</sub>, D<sub>j</sub>]</code> represents the <code>j<sup>th</sup></code> query where you must find the answer for <code>C<sub>j</sub> / D<sub>j</sub> = ?</code>.</p>

<p>Return <em>the answers to all queries</em>. If a single answer cannot be determined, return <code>-1.0</code>.</p>

<p><strong>Note:</strong> The input is always valid. You may assume that the evaluation will not result in division by zero and that there is no contradiction.</p>

<p><strong>Note:</strong>&nbsp;The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
<strong>Output:</strong> [6.00000,0.50000,-1.00000,1.00000,-1.00000]
<strong>Explanation:</strong> 
Given: <em>a / b = 2.0</em>, <em>b / c = 3.0</em>
queries are: <em>a / c = ?</em>, <em>b / a = ?</em>, <em>a / e = ?</em>, <em>a / a = ?</em>, <em>x / x = ?</em> 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined , so the answer cannot be determined for x / x.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
<strong>Output:</strong> [3.75000,0.40000,5.00000,0.20000]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
<strong>Output:</strong> [0.50000,2.00000,-1.00000,-1.00000]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= equations.length &lt;= 20</code></li>
	<li><code>equations[i].length == 2</code></li>
	<li><code>1 &lt;= A<sub>i</sub>.length, B<sub>i</sub>.length &lt;= 5</code></li>
	<li><code>values.length == equations.length</code></li>
	<li><code>0.0 &lt; values[i] &lt;= 20.0</code></li>
	<li><code>1 &lt;= queries.length &lt;= 20</code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>1 &lt;= C<sub>j</sub>.length, D<sub>j</sub>.length &lt;= 5</code></li>
	<li><code>A<sub>i</sub>, B<sub>i</sub>, C<sub>j</sub>, D<sub>j</sub></code> consist of lower case English letters and digits.</li>
</ul>"""

    input_format = "Equations, values, and queries."
    output_format = "A list of floating point answers."
    
    constraints = [
        "1 <= equations.length <= 20",
        "values.length == equations.length",
        "1 <= queries.length <= 20"
    ]
    
    explanation = """This problem can be modeled as a **Directed Graph** where variables are nodes and equations $A/B = v$ are edges with weight $v$ (and $B/A = 1/v$). Use DFS or BFS to find a path between variables in the queries."""
    
    answer = """class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            
        def dfs(start, end, visited):
            if start not in graph or end not in graph: return -1.0
            if start == end: return 1.0
            visited.add(start)
            for neighbor, val in graph[start].items():
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return val * res
            return -1.0
            
        return [dfs(u, v, set()) for u, v in queries]"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        equations = json.loads(lines[0].strip())\n        values = json.loads(lines[1].strip())\n        queries = json.loads(lines[2].strip())\n        sol = Solution()\n        print(json.dumps(sol.calcEquation(equations, values, queries)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n#include <unordered_set>\n#include <sstream>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {\n        // User logic here\n        return {};\n    }\n};\n\nvector<string> parseStrings(string s) {\n    if (s.empty()) return {};\n    if (s.front() == '[') s = s.substr(1, s.size()-2);\n    vector<string> res;\n    stringstream ss(s);\n    string val;\n    while (getline(ss, val, ',')) {\n        while(!val.empty() && (val.front() == ' ' || val.front() == '\"')) val.erase(0, 1);\n        while(!val.empty() && (val.back() == ' ' || val.back() == '\"')) val.pop_back();\n        if (!val.empty()) res.push_back(val);\n    }\n    return res;\n}\n\nvector<vector<string>> parsePairs(string s) {\n    vector<vector<string>> res;\n    if (s.size() >= 2) s = s.substr(1, s.size()-2);\n    size_t pos = 0;\n    while ((pos = s.find('[')) != string::npos) {\n        size_t end = s.find(']', pos);\n        res.push_back(parseStrings(s.substr(pos + 1, end - pos - 1)));\n        s.erase(0, end + 1);\n    }\n    return res;\n}\n\nint main() {\n    string eqLine, valLine, qLine;\n    if (getline(cin, eqLine) && getline(cin, valLine) && getline(cin, qLine)) {\n        vector<vector<string>> equations = parsePairs(eqLine);\n        \n        vector<double> values;\n        if (valLine.size() >= 2) valLine = valLine.substr(1, valLine.size()-2);\n        stringstream ss(valLine);\n        string v;\n        while (getline(ss, v, ',')) {\n            if (!v.empty()) values.push_back(stod(v));\n        }\n\n        vector<vector<string>> queries = parsePairs(qLine);\n\n        Solution sol;\n        vector<double> results = sol.calcEquation(equations, values, queries);\n        cout << \"[\";\n        for (int i=0; i<results.size(); i++) {\n            cout << results[i] << (i == results.size()-1 ? \"\" : \",\");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {\n        // User logic here\n        return new double[0];\n    }\n}\n\npublic class Main {\n    private static List<String> parseStrings(String s) {\n        s = s.trim();\n        if (s.startsWith(\"[\")) s = s.substring(1, s.length()-1);\n        List<String> res = new ArrayList<>();\n        String[] parts = s.split(\",\");\n        for (String p : parts) {\n            p = p.trim();\n            if (p.startsWith(\"\\\\\\\"\")) p = p.substring(1, p.length()-1);\n            if (p.endsWith(\"\\\\\\\"\")) p = p.substring(0, p.length()-1);\n            if (!p.isEmpty()) res.add(p);\n        }\n        return res;\n    }\n\n    private static List<List<String>> parsePairs(String s) {\n        List<List<String>> res = new ArrayList<>();\n        s = s.trim();\n        if (s.startsWith(\"[\")) s = s.substring(1, s.length()-1);\n        int start = 0;\n        while ((start = s.indexOf(\"[\", start)) != -1) {\n            int end = s.indexOf(\"]\", start);\n            res.add(parseStrings(s.substring(start + 1, end)));\n            start = end + 1;\n        }\n        return res;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            List<List<String>> equations = parsePairs(sc.nextLine());\n            \n            String vLine = sc.nextLine().trim();\n            if (vLine.startsWith(\"[\")) vLine = vLine.substring(1, vLine.length()-1);\n            String[] vParts = vLine.split(\",\");\n            double[] values = new double[vParts.length];\n            for (int i=0; i<vParts.length; i++) values[i] = Double.parseDouble(vParts[i].trim());\n\n            List<List<String>> queries = parsePairs(sc.nextLine());\n\n            Solution sol = new Solution();\n            double[] resultsArr = sol.calcEquation(equations, values, queries);\n            System.out.print(\"[\");\n            for (int i=0; i<resultsArr.length; i++) {\n                System.out.print(resultsArr[i] + (i == resultsArr.length-1 ? \"\" : \", \"));\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "var calcEquation = function(equations, values, queries) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').split('\\\\n');\nif (input.length >= 3) {\n    const equations = JSON.parse(input[0].trim());\n    const values = JSON.parse(input[1].trim());\n    const queries = JSON.parse(input[2].trim());\n    console.log(JSON.stringify(calcEquation(equations, values, queries)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\ndouble* calcEquation(char*** equations, int equationsSize, int* equationsColSize, double* values, int valuesSize, char*** queries, int queriesSize, int* queriesColSize, int* returnSize) {\n    // User logic here\n    return NULL;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": '[["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]', "expected_output": "[6.0,0.5,-1.0,1.0,-1.0]", "is_sample": True},
        {"input": '[["a","b"],["b","c"],["bc","cd"]]\n[1.5,2.5,5.0]\n[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]', "expected_output": "[3.75,0.4,5.0,0.2]", "is_sample": True},
        # 5 Diverse
        {"input": '[["a","b"]]\n[0.5]\n[["a","b"],["b","a"],["a","c"],["x","y"]]', "expected_output": "[0.5,2.0,-1.0,-1.0]", "is_sample": False},
        {"input": '[["a","b"],["c","d"]]\n[2.0, 3.0]\n[["a","c"]]', "expected_output": "[-1.0]", "is_sample": False},
        {"input": '[["a","b"],["b","a"]]\n[1.0, 1.0]\n[["a","b"]]', "expected_output": "[1.0]", "is_sample": False},
        {"input": '[["a","b"],["b","c"]]\n[2.0, 3.0]\n[["a","c"]]', "expected_output": "[6.0]", "is_sample": False},
        {"input": '[["x1","x2"],["x2","x3"],["x3","x4"]]\n[3.0, 0.5, 2.0]\n[["x1","x4"],["x4","x1"]]', "expected_output": "[3.0,0.3333333333333333]", "is_sample": False},
        # 3 Stress
        {"input": '[["a","b"]]\n[2e-5]\n[["b","a"]]', "expected_output": "[50000.0]", "is_sample": False},
        {"input": '[["a","b"],["b","c"],["c","d"],["d","e"],["e","f"]]\n[2.0, 2.0, 2.0, 2.0, 2.0]\n[["a","f"],["f","a"]]', "expected_output": "[32.0,0.03125]", "is_sample": False},
        {"input": '[["a","b"],["c","d"]]\n[1.0,1.0]\n[["a","a"],["b","b"],["c","c"],["d","d"]]', "expected_output": "[1.0,1.0,1.0,1.0]", "is_sample": False}
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
        "topics": ["Array", "String", "Graph", "DFS", "BFS", "Union Find"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Evaluate_Division.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
