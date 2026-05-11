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
        "python": """import sys
import json

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # User Logic Here
        pass

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 3:
        equations = json.loads(lines[0].strip())
        values = json.loads(lines[1].strip())
        queries = json.loads(lines[2].strip())
        sol = Solution()
        print(json.dumps(sol.calcEquation(equations, values, queries)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <sstream>

using namespace std;

class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        // User Logic Here
        return {};
    }
};

vector<string> parseStrings(string s) {
    if (s.empty()) return {};
    if (s.front() == '[') s = s.substr(1, s.size()-2);
    vector<string> res;
    stringstream ss(s);
    string val;
    while (getline(ss, val, ',')) {
        while(!val.empty() && (val.front() == ' ' || val.front() == '"')) val.erase(0, 1);
        while(!val.empty() && (val.back() == ' ' || val.back() == '"')) val.pop_back();
        if (!val.empty()) res.push_back(val);
    }
    return res;
}

vector<vector<string>> parsePairs(string s) {
    vector<vector<string>> res;
    if (s.size() >= 2) s = s.substr(1, s.size()-2);
    size_t pos = 0;
    while ((pos = s.find('[')) != string::npos) {
        size_t end = s.find(']', pos);
        res.push_back(parseStrings(s.substr(pos + 1, end - pos - 1)));
        s.erase(0, end + 1);
    }
    return res;
}

int main() {
    string eqLine, valLine, qLine;
    if (getline(cin, eqLine) && getline(cin, valLine) && getline(cin, qLine)) {
        vector<vector<string>> equations = parsePairs(eqLine);
        
        vector<double> values;
        if (valLine.size() >= 2) valLine = valLine.substr(1, valLine.size()-2);
        stringstream ss(valLine);
        string v;
        while (getline(ss, v, ',')) {
            if (!v.empty()) values.push_back(stod(v));
        }

        vector<vector<string>> queries = parsePairs(qLine);

        Solution sol;
        vector<double> results = sol.calcEquation(equations, values, queries);
        cout << "[";
        for (int i=0; i<results.size(); i++) {
            cout << results[i] << (i == results.size()-1 ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        // User Logic Here
        return new double[0];
    }
}

public class Main {
    private static List<String> parseStrings(String s) {
        s = s.trim();
        if (s.startsWith("[")) s = s.substring(1, s.length()-1);
        List<String> res = new ArrayList<>();
        String[] parts = s.split(",");
        for (String p : parts) {
            p = p.trim();
            if (p.startsWith("\\\"")) p = p.substring(1, p.length()-1);
            if (p.endsWith("\\\"")) p = p.substring(0, p.length()-1);
            if (!p.isEmpty()) res.add(p);
        }
        return res;
    }

    private static List<List<String>> parsePairs(String s) {
        List<List<String>> res = new ArrayList<>();
        s = s.trim();
        if (s.startsWith("[")) s = s.substring(1, s.length()-1);
        int start = 0;
        while ((start = s.indexOf("[", start)) != -1) {
            int end = s.indexOf("]", start);
            res.add(parseStrings(s.substring(start + 1, end)));
            start = end + 1;
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            List<List<String>> equations = parsePairs(sc.nextLine());
            
            String vLine = sc.nextLine().trim();
            if (vLine.startsWith("[")) vLine = vLine.substring(1, vLine.length()-1);
            String[] vParts = vLine.split(",");
            double[] values = new double[vParts.length];
            for (int i=0; i<vParts.length; i++) values[i] = Double.parseDouble(vParts[i].trim());

            List<List<String>> queries = parsePairs(sc.nextLine());

            Solution sol = new Solution();
            double[] resultsArr = sol.calcEquation(equations, values, queries);
            System.out.print("[");
            for (int i=0; i<resultsArr.length; i++) {
                System.out.print(resultsArr[i] + (i == resultsArr.length-1 ? "" : ", "));
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """var calcEquation = function(equations, values, queries) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 3) {
    const equations = JSON.parse(input[0].trim());
    const values = JSON.parse(input[1].trim());
    const queries = JSON.parse(input[2].trim());
    console.log(JSON.stringify(calcEquation(equations, values, queries)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double* calcEquation(char*** equations, int equationsSize, int* equationsColSize, double* values, int valuesSize, char*** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    // User Logic Here
    return NULL;
}

int main() {
    return 0;
}"""
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
