import json
import os

def generate_json():
    problem_id = 277
    title = "Find the Celebrity"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>277. Find the Celebrity</h3>
<p>Suppose you are at a party with <code>n</code> people (labeled from <code>0</code> to <code>n - 1</code>) and among them, there may exist one celebrity. The definition of a celebrity is that all the other <code>n - 1</code> people know him/her but he/she does not know any of them.</p>

<p>You are provided with a helper function <code>bool knows(a, b)</code> that tells you whether <code>a</code> knows <code>b</code>. Implement a function <code>int findCelebrity(int n)</code>, your task is to find the celebrity (or return -1 if there is no celebrity).</p>

<p>There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> graph = [[1,1,0],[0,1,0],[1,1,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There are three people labeled 0, 1 and 2. knows(0, 1) is True, knows(2, 1) is True. And knows(1, 0) is False, knows(1, 2) is False. So person 1 is the celebrity.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> graph = [[1,0,1],[1,1,0],[0,1,1]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> knows(0, 2) is True, knows(1, 0) is True and knows(2, 1) is True. Everyone knows someone, so there is no celebrity.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == graph.length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>knows(a, b)</code> is <code>O(1)</code>.</li>
</ul>"""

    input_format = "A stringified 2D array (graph) representing the people's relationships."
    output_format = "The label of the celebrity as an integer, or -1."
    
    constraints = [
        "2 <= n <= 100",
        "knows(a, b) is O(1)."
    ]
    
    explanation = """To find the celebrity in O(n) calls to `knows(a, b)`:
1. **Find a Candidate**: Start with a candidate `person = 0`. Iterate through all other people `i`. If `knows(person, i)` is true, it means `person` cannot be the celebrity, and `i` might be. So update `candidate = i`. 
2. **Elimination Logic**: Each call to `knows(a, b)` eliminates one person:
   - If `knows(a, b)` is True, `a` cannot be the celebrity (as a celebrity knows no one).
   - If `knows(a, b)` is False, `b` cannot be the celebrity (as every person knows the celebrity).
3. **Verify Candidate**: After finding a potential `candidate`, you must verify that:
   - Everyone else knows the candidate: `knows(i, candidate)` is True for all `i != candidate`.
   - The candidate knows no one: `knows(candidate, i)` is False for all `i != candidate`.
4. **Complexity**:
   - Time: O(N) calls to `knows`.
   - Space: O(1)."""
    
    answer = """# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        
        # Step 1: Find a candidate. 
        # For each comparison, we eliminate one person.
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
                
        # Step 2: Verification. 
        # Check if everyone knows the candidate and the candidate doesn't know anyone.
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
                
        return candidate"""

    boilerplate = {
        "python": "import sys\nimport re\n\ngraph_global = []\n\ndef knows(a: int, b: int) -> bool:\n    return bool(graph_global[a][b])\n\ndef findCelebrity(n: int) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Find the matrix part\n    matrix_match = re.search(r'\\[\\s*\\[.*\\]\\s*\\]', raw_input, re.DOTALL)\n    if matrix_match:\n        matrix_str = matrix_match.group(0)\n        rows = re.findall(r'\\[([^\\[\\]]*)\\]', matrix_str[1:-1])\n        graph_global = [[int(x) for x in re.findall(r'\\d+', r)] for r in rows]\n    else:\n        # Fallback: just find all numbers and try to make a square\n        nums = [int(x) for x in re.findall(r'\\d+', raw_input)]\n        n = int(len(nums)**0.5)\n        graph_global = [nums[i*n:(i+1)*n] for i in range(n)]\n        \n    if graph_global:\n        print(findCelebrity(len(graph_global)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <cmath>\n\nusing namespace std;\n\nvector<vector<int>> graph_global;\nbool knows(int a, int b) {\n    return graph_global[a][b] == 1;\n}\n\nint findCelebrity(int n) {\n    // User logic here\n    return -1;\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    regex re_row(R\"(\\[([^\\[\\]]*)\\])\");\n    auto row_begin = sregex_iterator(input.begin(), input.end(), re_row);\n    auto row_end = sregex_iterator();\n    \n    vector<vector<int>> temp_graph;\n    for (sregex_iterator i = row_begin; i != row_end; ++i) {\n        string row_str = i->str(1);\n        vector<int> row_nums;\n        regex re_num(R\"(\\d+)\");\n        auto num_begin = sregex_iterator(row_str.begin(), row_str.end(), re_num);\n        auto num_end = sregex_iterator();\n        for (sregex_iterator j = num_begin; j != num_end; ++j) {\n            row_nums.push_back(stoi(j->str()));\n        }\n        if (!row_nums.empty()) temp_graph.push_back(row_nums);\n    }\n    \n    if (temp_graph.size() > 0 && temp_graph[0].size() != temp_graph.size()) {\n        // Handle the case where the whole input was treated as one flat list or something\n        // Usually happens if outer brackets were missing\n    }\n\n    graph_global = temp_graph;\n    cout << findCelebrity(graph_global.size()) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    static int[][] graph_global;\n    \n    public static boolean knows(int a, int b) {\n        return graph_global[a][b] == 1;\n    }\n\n    public int findCelebrity(int n) {\n        // User logic here\n        return -1;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        \n        List<int[]> rows = new ArrayList<>();\n        Pattern pRow = Pattern.compile(\"\\\\[([^\\\\[\\\\]]*)\\\\]\");\n        Matcher mRow = pRow.matcher(input);\n        \n        while (mRow.find()) {\n            String rowContent = mRow.group(1);\n            List<Integer> rowNums = new ArrayList<>();\n            Matcher mNum = Pattern.compile(\"\\\\d+\").matcher(rowContent);\n            while (mNum.find()) {\n                rowNums.add(Integer.parseInt(mNum.group()));\n            }\n            if (!rowNums.isEmpty()) {\n                int[] r = new int[rowNums.size()];\n                for (int i = 0; i < rowNums.size(); i++) r[i] = rowNums.get(i);\n                rows.add(r);\n            }\n        }\n        \n        if (rows.isEmpty()) return;\n        \n        graph_global = new int[rows.size()][rows.get(0).length];\n        for (int i = 0; i < rows.size(); i++) graph_global[i] = rows.get(i);\n        \n        System.out.println(new Solution().findCelebrity(rows.size()));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nlet graph_global = [];\nfunction knows(a, b) {\n    return graph_global[a][b] === 1;\n}\n\nfunction findCelebrity(n) {\n    // User logic here\n    return -1;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst rowMatches = input.match(/\\[([^\\[\\]]*)\\]/g);\nif (rowMatches) {\n    graph_global = rowMatches.map(row => {\n        const nums = row.match(/\\d+/g);\n        return nums ? nums.map(Number) : [];\n    }).filter(row => row.length > 0);\n    \n    // If it's a single flat array in multiple brackets, we might need to filter\n    if (graph_global.length > 0) {\n        console.log(findCelebrity(graph_global.length));\n    }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n#include <stdbool.h>\n\nint** graph_global;\nint graph_size;\n\nbool knows(int a, int b) {\n    return graph_global[a][b] == 1;\n}\n\nint findCelebrity(int n) {\n    // User logic here\n    return -1;\n}\n\nint main() {\n    static char buffer[1000000];\n    if (fread(buffer, 1, 999999, stdin) > 0) {\n        int row = 0;\n        graph_global = malloc(500 * sizeof(int*));\n        char* p = buffer;\n        while (*p) {\n            if (*p == '[') {\n                char* end = strchr(p, ']');\n                if (end) {\n                    *end = '\\0';\n                    int* currentRow = malloc(500 * sizeof(int));\n                    int col = 0;\n                    char* numPtr = p + 1;\n                    while (*numPtr) {\n                        if (isdigit(*numPtr)) {\n                            currentRow[col++] = atoi(numPtr);\n                            while (isdigit(*numPtr)) numPtr++;\n                        } else {\n                            numPtr++;\n                        }\n                    }\n                    if (col > 0) graph_global[row++] = currentRow;\n                    *end = ']';\n                    p = end + 1;\n                } else p++;\n            } else p++;\n        }\n        // Simple check to avoid outer brackets being counted as a row\n        if (row > 1 && row > (int)strtol(buffer + (strspn(buffer, \" \")), NULL, 10)) {\n            // Likely correct\n        }\n        printf(\"%d\\n\", findCelebrity(row));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,1,0],[0,1,0],[1,1,1]]", "expected_output": "1", "is_sample": True},
        {"input": "[[1,0,1],[1,1,0],[0,1,1]]", "expected_output": "-1", "is_sample": True},
        {"input": "[[1,1],[1,1]]", "expected_output": "-1", "is_sample": False},
        {"input": "[[1,0],[1,1]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,1],[0,1]]", "expected_output": "0", "is_sample": False},
        {"input": "[[1,1,1],[0,1,0],[0,1,1]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,0,0],[0,1,0],[0,0,1]]", "expected_output": "-1", "is_sample": False},
        # Stress cases
        {"input": "[[1 if i==j or j==50 else 0 for j in range(100)] for i in range(100)]", "expected_output": "50", "is_sample": False},
        {"input": "[[1 for j in range(100)] for i in range(100)]", "expected_output": "-1", "is_sample": False},
        {"input": "[[1 if i==j else 0 for j in range(100)] for i in range(100)]", "expected_output": "-1", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Greedy", "Graph"],
        "companyIndex": 0
    }

    output_path = "201-400/277_Find_the_Celebrity.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
