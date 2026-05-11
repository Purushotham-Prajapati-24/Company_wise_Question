import json
import os

def generate_json():
    problem_id = 332
    title = "Reconstruct Itinerary"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>332. Reconstruct Itinerary</h3>
<p>You are given a list of airline tickets where <code>tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.</p>

<p>All of the tickets belong to a man who departs from <code>"JFK"</code>, thus, the itinerary must begin with <code>"JFK"</code>. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.</p>

<ul>
	<li>For example, the itinerary <code>["JFK", "LGA"]</code> has a smaller lexical order than <code>["JFK", "LGB"]</code>.</li>
</ul>

<p>You may assume all tickets form at least one valid itinerary. You must use all the tickets exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg" style="width: 382px; height: 222px;" />
<pre><strong>Input:</strong> tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
<strong>Output:</strong> ["JFK","MUC","LHR","SFO","SJC"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg" style="width: 222px; height: 382px;" />
<pre><strong>Input:</strong> tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
<strong>Output:</strong> ["JFK","ATL","JFK","SFO","ATL","SFO"]
<strong>Explanation:</strong> Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= tickets.length &lt;= 300</code></li>
	<li><code>tickets[i].length == 2</code></li>
	<li><code>from<sub>i</sub>.length == 3</code></li>
	<li><code>to<sub>i</sub>.length == 3</code></li>
	<li><code>from<sub>i</sub></code> and <code>to<sub>i</sub></code> consist of uppercase English letters.</li>
	<li>All tickets form at least one valid itinerary.</li>
</ul>"""

    input_format = "A 2D array of strings `tickets`."
    output_format = "A list of strings representing the reconstructed itinerary."
    
    constraints = [
        "1 <= tickets.length <= 300",
        "Itinerary must start from 'JFK'."
    ]
    
    explanation = """To reconstruct the itinerary using all tickets exactly once while ensuring the smallest lexical order, we use **Hierholzer's Algorithm** to find an **Eulerian Path** in a directed graph.

### Key Strategy:
- **Directed Graph**: Represent airports as nodes and tickets as directed edges.
- **Lexical Order**: Sort the destination airports for each departure airport in descending order (to pop from the end efficiently in $O(1)$) or ascending order (if using a queue).
- **Eulerian Path**: An Eulerian path visits every edge exactly once. Since a valid itinerary is guaranteed, we and we start at "JFK", this is a classic Eulerian Path problem.

### Algorithm Steps:
1. **Build Adjacency List**: Store edges in a hash map where keys are departure airports and values are a list of destination airports. Sort these destination lists in **reverse alphabetical order**.
2. **Post-Order DFS (Hierholzer's)**:
   - Start DFS from "JFK".
   - For the current airport, while it has outgoing edges:
     - Pop the lexically smallest destination (the last element of the sorted list) and recurse.
   - After visiting all possible destinations from the current airport, add the current airport to the result.
3. **Result Construction**: The result will be in reverse order (since we append after the recursion). Reverse the list and return it.

### Complexity Analysis:
- **Time Complexity**: $O(E \log E)$, where $E$ is the number of tickets, due to initial sorting of destination lists. The DFS visits each edge exactly once.
- **Space Complexity**: $O(V + E)$ to store the graph and the recursion stack."""
    
    answer = """import collections

class Solution:
    def findItinerary(self, tickets: List[List[int]]) -> List[str]:
        # Build graph and sort destinations in reverse lexical order
        adj = collections.defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            adj[u].append(v)
            
        itinerary = []
        
        def dfs(airport):
            while adj[airport]:
                next_dest = adj[airport].pop()
                dfs(next_dest)
            # Post-order: add to itinerary when all paths are explored
            itinerary.append(airport)
            
        dfs("JFK")
        return itinerary[::-1]"""

    boilerplate = {
        "python": "import sys\nimport json\nimport collections\n\nclass Solution:\n    def findItinerary(self, tickets: list[list[str]]) -> list[str]:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        tickets = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.findItinerary(tickets)).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <map>\n#include <set>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<string> findItinerary(vector<vector<string>>& tickets) {\n        // Your logic here\n        return {};\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<vector<string>> tickets;\n        int i = 0;\n        while (i < line.length()) {\n            if (line[i] == '[') {\n                i++;\n                bool is_inner = false;\n                int j = i;\n                while (j < line.length() && (line[j] == ' ' || line[j] == ',')) j++;\n                if (j < line.length() && line[j] == '\"') is_inner = true;\n                if (is_inner) {\n                    vector<string> tup;\n                    while (i < line.length() && line[i] != ']') {\n                        if (line[i] == '\"') {\n                            i++;\n                            string s = \"\";\n                            while (i < line.length() && line[i] != '\"') {\n                                s += line[i++];\n                            }\n                            tup.push_back(s);\n                        }\n                        i++;\n                    }\n                    tickets.push_back(tup);\n                }\n            } else {\n                i++;\n            }\n        }\n        Solution sol;\n        vector<string> res = sol.findItinerary(tickets);\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); ++i) {\n            cout << \"\\\"\" << res[i] << \"\\\"\" << (i < res.size() - 1 ? \",\" : \"\");\n        }\n        cout << \"]\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<String> findItinerary(List<List<String>> tickets) {\n        // Your logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        if (scanner.hasNextLine()) {\n            String line = scanner.nextLine();\n            List<List<String>> tickets = new ArrayList<>();\n            int i = 0;\n            while (i < line.length()) {\n                if (line.charAt(i) == '[') {\n                    i++;\n                    boolean isInner = false;\n                    int j = i;\n                    while (j < line.length() && (line.charAt(j) == ' ' || line.charAt(j) == ',')) j++;\n                    if (j < line.length() && line.charAt(j) == '\"') isInner = true;\n                    if (isInner) {\n                        List<String> tup = new ArrayList<>();\n                        while (i < line.length() && line.charAt(i) != ']') {\n                            if (line.charAt(i) == '\"') {\n                                i++;\n                                StringBuilder s = new StringBuilder();\n                                while (i < line.length() && line.charAt(i) != '\"') {\n                                    s.append(line.charAt(i++));\n                                }\n                                tup.add(s.toString());\n                            }\n                            i++;\n                        }\n                        tickets.add(tup);\n                    }\n                } else {\n                    i++;\n                }\n            }\n            Solution sol = new Solution();\n            List<String> res = sol.findItinerary(tickets);\n            System.out.print(\"[\");\n            for (int k = 0; k < res.size(); k++) {\n                System.out.print(\"\\\"\" + res.get(k) + \"\\\"\" + (k < res.size() - 1 ? \",\" : \"\"));\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "/**\n * @param {string[][]} tickets\n * @return {string[]}\n */\nvar findItinerary = function(tickets) {\n    // Your logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync('/dev/stdin', 'utf-8').trim();\nif (input) {\n    const tickets = JSON.parse(input);\n    console.log(JSON.stringify(findItinerary(tickets)).replace(/ /g, ''));\n}",
        "c": "/**\n * Note: The returned array must be malloced, assume caller calls free().\n */\nchar** findItinerary(char*** tickets, int ticketsSize, int* ticketsColSize, int* returnSize) {\n    // Your logic here\n    return NULL;\n}\n\nint main() {\n    char line[500000];\n    if (fgets(line, sizeof(line), stdin)) {\n        int capacity = 500;\n        char*** tickets = malloc(capacity * sizeof(char**));\n        int* ticketsColSize = malloc(capacity * sizeof(int));\n        int size = 0;\n        char* ptr = line;\n        while (*ptr) {\n            if (*ptr == '[') {\n                ptr++;\n                char* check = ptr;\n                while (*check == ' ' || *check == ',') check++;\n                if (*check == '\"') {\n                    int colCap = 10;\n                    tickets[size] = malloc(colCap * sizeof(char*));\n                    int colSize = 0;\n                    while (*ptr && *ptr != ']') {\n                        if (*ptr == '\"') {\n                            ptr++;\n                            char* start = ptr;\n                            while (*ptr && *ptr != '\"') ptr++;\n                            int len = ptr - start;\n                            char* str = malloc(len + 1);\n                            strncpy(str, start, len);\n                            str[len] = '\\0';\n                            tickets[size][colSize++] = str;\n                        }\n                        if (*ptr != ']') ptr++;\n                    }\n                    ticketsColSize[size] = colSize;\n                    size++;\n                    if (size >= capacity) {\n                        capacity *= 2;\n                        tickets = realloc(tickets, capacity * sizeof(char**));\n                        ticketsColSize = realloc(ticketsColSize, capacity * sizeof(int));\n                    }\n                }\n            } else {\n                ptr++;\n            }\n        }\n        int returnSize = 0;\n        char** res = findItinerary(tickets, size, ticketsColSize, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"\\\"%s\\\"%s\", res[i], i < returnSize - 1 ? \",\" : \"\");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]', "expected_output": '["JFK","MUC","LHR","SFO","SJC"]', "is_sample": True},
        {"input": '[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]', "expected_output": '["JFK","ATL","JFK","SFO","ATL","SFO"]', "is_sample": True},
        {"input": '[["JFK","ABC"],["JFK","DEF"],["ABC","JFK"]]', "expected_output": '["JFK","ABC","JFK","DEF"]', "is_sample": False},
        {"input": '[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]', "expected_output": '["JFK","NRT","JFK","KUL"]', "is_sample": False},
        {"input": '[["JFK","B"],["JFK","A"],["B","A"],["A","JFK"],["A","B"]]', "expected_output": '["JFK","A","B","A","JFK","A","B"]', "is_sample": False},
        {"input": '[["JFK","A"],["A","B"],["B","A"]]', "expected_output": '["JFK","A","B","A"]', "is_sample": False},
        {"input": '[["JFK","LGA"]]', "expected_output": '["JFK","LGA"]', "is_sample": False},
                # Stress cases
        {"input": "[[\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"], [\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"], [\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"], [\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"], [\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"], [\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"], [\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"], [\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"], [\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"], [\"JFK\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"JFK\"], [\"JFK\", \"ATL\"], [\"ATL\", \"SFO\"], [\"SFO\", \"JFK\"]]", "expected_output": "[\"JFK\", \"ATL\", \"JFK\", \"ATL\", \"JFK\", \"ATL\", \"JFK\", \"ATL\", \"JFK\", \"ATL\", \"JFK\", \"ATL\", \"JFK\", \"ATL\", \"JFK\", \"ATL\", \"JFK\", \"ATL\", \"JFK\", \"ATL\", \"JFK\", \"SFO\", \"ATL\", \"SFO\", \"ATL\", \"SFO\", \"ATL\", \"SFO\", \"ATL\", \"SFO\", \"ATL\", \"SFO\", \"ATL\", \"SFO\", \"ATL\", \"SFO\", \"ATL\", \"SFO\", \"ATL\", \"SFO\", \"ATL\", \"SFO\", \"JFK\", \"SFO\", \"JFK\", \"SFO\", \"JFK\", \"SFO\", \"JFK\", \"SFO\", \"JFK\", \"SFO\", \"JFK\", \"SFO\", \"JFK\", \"SFO\", \"JFK\", \"SFO\", \"JFK\", \"SFO\", \"JFK\"]", "is_sample": False},
        {"input": "[[\"JFK\", \"KUL\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"], [\"JFK\", \"NRT\"], [\"NRT\", \"JFK\"]]", "expected_output": "[\"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"NRT\", \"JFK\", \"KUL\"]", "is_sample": False},
        {"input": "[[\"JFK\", \"A0\"], [\"A0\", \"JFK\"], [\"JFK\", \"A1\"], [\"A1\", \"JFK\"], [\"JFK\", \"A2\"], [\"A2\", \"JFK\"], [\"JFK\", \"A3\"], [\"A3\", \"JFK\"], [\"JFK\", \"A4\"], [\"A4\", \"JFK\"], [\"JFK\", \"A5\"], [\"A5\", \"JFK\"], [\"JFK\", \"A6\"], [\"A6\", \"JFK\"], [\"JFK\", \"A7\"], [\"A7\", \"JFK\"], [\"JFK\", \"A8\"], [\"A8\", \"JFK\"], [\"JFK\", \"A9\"], [\"A9\", \"JFK\"], [\"JFK\", \"A10\"], [\"A10\", \"JFK\"], [\"JFK\", \"A11\"], [\"A11\", \"JFK\"], [\"JFK\", \"A12\"], [\"A12\", \"JFK\"], [\"JFK\", \"A13\"], [\"A13\", \"JFK\"], [\"JFK\", \"A14\"], [\"A14\", \"JFK\"], [\"JFK\", \"A15\"], [\"A15\", \"JFK\"], [\"JFK\", \"A16\"], [\"A16\", \"JFK\"], [\"JFK\", \"A17\"], [\"A17\", \"JFK\"], [\"JFK\", \"A18\"], [\"A18\", \"JFK\"], [\"JFK\", \"A19\"], [\"A19\", \"JFK\"], [\"JFK\", \"A20\"], [\"A20\", \"JFK\"], [\"JFK\", \"A21\"], [\"A21\", \"JFK\"], [\"JFK\", \"A22\"], [\"A22\", \"JFK\"], [\"JFK\", \"A23\"], [\"A23\", \"JFK\"], [\"JFK\", \"A24\"], [\"A24\", \"JFK\"], [\"JFK\", \"A25\"], [\"A25\", \"JFK\"], [\"JFK\", \"A26\"], [\"A26\", \"JFK\"], [\"JFK\", \"A27\"], [\"A27\", \"JFK\"], [\"JFK\", \"A28\"], [\"A28\", \"JFK\"], [\"JFK\", \"A29\"], [\"A29\", \"JFK\"], [\"JFK\", \"A30\"], [\"A30\", \"JFK\"], [\"JFK\", \"A31\"], [\"A31\", \"JFK\"], [\"JFK\", \"A32\"], [\"A32\", \"JFK\"], [\"JFK\", \"A33\"], [\"A33\", \"JFK\"], [\"JFK\", \"A34\"], [\"A34\", \"JFK\"], [\"JFK\", \"A35\"], [\"A35\", \"JFK\"], [\"JFK\", \"A36\"], [\"A36\", \"JFK\"], [\"JFK\", \"A37\"], [\"A37\", \"JFK\"], [\"JFK\", \"A38\"], [\"A38\", \"JFK\"], [\"JFK\", \"A39\"], [\"A39\", \"JFK\"], [\"JFK\", \"A40\"], [\"A40\", \"JFK\"], [\"JFK\", \"A41\"], [\"A41\", \"JFK\"], [\"JFK\", \"A42\"], [\"A42\", \"JFK\"], [\"JFK\", \"A43\"], [\"A43\", \"JFK\"], [\"JFK\", \"A44\"], [\"A44\", \"JFK\"], [\"JFK\", \"A45\"], [\"A45\", \"JFK\"], [\"JFK\", \"A46\"], [\"A46\", \"JFK\"], [\"JFK\", \"A47\"], [\"A47\", \"JFK\"], [\"JFK\", \"A48\"], [\"A48\", \"JFK\"], [\"JFK\", \"A49\"], [\"A49\", \"JFK\"], [\"JFK\", \"A50\"], [\"A50\", \"JFK\"], [\"JFK\", \"A51\"], [\"A51\", \"JFK\"], [\"JFK\", \"A52\"], [\"A52\", \"JFK\"], [\"JFK\", \"A53\"], [\"A53\", \"JFK\"], [\"JFK\", \"A54\"], [\"A54\", \"JFK\"], [\"JFK\", \"A55\"], [\"A55\", \"JFK\"], [\"JFK\", \"A56\"], [\"A56\", \"JFK\"], [\"JFK\", \"A57\"], [\"A57\", \"JFK\"], [\"JFK\", \"A58\"], [\"A58\", \"JFK\"], [\"JFK\", \"A59\"], [\"A59\", \"JFK\"], [\"JFK\", \"A60\"], [\"A60\", \"JFK\"], [\"JFK\", \"A61\"], [\"A61\", \"JFK\"], [\"JFK\", \"A62\"], [\"A62\", \"JFK\"], [\"JFK\", \"A63\"], [\"A63\", \"JFK\"], [\"JFK\", \"A64\"], [\"A64\", \"JFK\"], [\"JFK\", \"A65\"], [\"A65\", \"JFK\"], [\"JFK\", \"A66\"], [\"A66\", \"JFK\"], [\"JFK\", \"A67\"], [\"A67\", \"JFK\"], [\"JFK\", \"A68\"], [\"A68\", \"JFK\"], [\"JFK\", \"A69\"], [\"A69\", \"JFK\"], [\"JFK\", \"A70\"], [\"A70\", \"JFK\"], [\"JFK\", \"A71\"], [\"A71\", \"JFK\"], [\"JFK\", \"A72\"], [\"A72\", \"JFK\"], [\"JFK\", \"A73\"], [\"A73\", \"JFK\"], [\"JFK\", \"A74\"], [\"A74\", \"JFK\"], [\"JFK\", \"A75\"], [\"A75\", \"JFK\"], [\"JFK\", \"A76\"], [\"A76\", \"JFK\"], [\"JFK\", \"A77\"], [\"A77\", \"JFK\"], [\"JFK\", \"A78\"], [\"A78\", \"JFK\"], [\"JFK\", \"A79\"], [\"A79\", \"JFK\"], [\"JFK\", \"A80\"], [\"A80\", \"JFK\"], [\"JFK\", \"A81\"], [\"A81\", \"JFK\"], [\"JFK\", \"A82\"], [\"A82\", \"JFK\"], [\"JFK\", \"A83\"], [\"A83\", \"JFK\"], [\"JFK\", \"A84\"], [\"A84\", \"JFK\"], [\"JFK\", \"A85\"], [\"A85\", \"JFK\"], [\"JFK\", \"A86\"], [\"A86\", \"JFK\"], [\"JFK\", \"A87\"], [\"A87\", \"JFK\"], [\"JFK\", \"A88\"], [\"A88\", \"JFK\"], [\"JFK\", \"A89\"], [\"A89\", \"JFK\"], [\"JFK\", \"A90\"], [\"A90\", \"JFK\"], [\"JFK\", \"A91\"], [\"A91\", \"JFK\"], [\"JFK\", \"A92\"], [\"A92\", \"JFK\"], [\"JFK\", \"A93\"], [\"A93\", \"JFK\"], [\"JFK\", \"A94\"], [\"A94\", \"JFK\"], [\"JFK\", \"A95\"], [\"A95\", \"JFK\"], [\"JFK\", \"A96\"], [\"A96\", \"JFK\"], [\"JFK\", \"A97\"], [\"A97\", \"JFK\"], [\"JFK\", \"A98\"], [\"A98\", \"JFK\"], [\"JFK\", \"A99\"], [\"A99\", \"JFK\"]]", "expected_output": "[\"JFK\", \"A0\", \"JFK\", \"A1\", \"JFK\", \"A10\", \"JFK\", \"A11\", \"JFK\", \"A12\", \"JFK\", \"A13\", \"JFK\", \"A14\", \"JFK\", \"A15\", \"JFK\", \"A16\", \"JFK\", \"A17\", \"JFK\", \"A18\", \"JFK\", \"A19\", \"JFK\", \"A2\", \"JFK\", \"A20\", \"JFK\", \"A21\", \"JFK\", \"A22\", \"JFK\", \"A23\", \"JFK\", \"A24\", \"JFK\", \"A25\", \"JFK\", \"A26\", \"JFK\", \"A27\", \"JFK\", \"A28\", \"JFK\", \"A29\", \"JFK\", \"A3\", \"JFK\", \"A30\", \"JFK\", \"A31\", \"JFK\", \"A32\", \"JFK\", \"A33\", \"JFK\", \"A34\", \"JFK\", \"A35\", \"JFK\", \"A36\", \"JFK\", \"A37\", \"JFK\", \"A38\", \"JFK\", \"A39\", \"JFK\", \"A4\", \"JFK\", \"A40\", \"JFK\", \"A41\", \"JFK\", \"A42\", \"JFK\", \"A43\", \"JFK\", \"A44\", \"JFK\", \"A45\", \"JFK\", \"A46\", \"JFK\", \"A47\", \"JFK\", \"A48\", \"JFK\", \"A49\", \"JFK\", \"A5\", \"JFK\", \"A50\", \"JFK\", \"A51\", \"JFK\", \"A52\", \"JFK\", \"A53\", \"JFK\", \"A54\", \"JFK\", \"A55\", \"JFK\", \"A56\", \"JFK\", \"A57\", \"JFK\", \"A58\", \"JFK\", \"A59\", \"JFK\", \"A6\", \"JFK\", \"A60\", \"JFK\", \"A61\", \"JFK\", \"A62\", \"JFK\", \"A63\", \"JFK\", \"A64\", \"JFK\", \"A65\", \"JFK\", \"A66\", \"JFK\", \"A67\", \"JFK\", \"A68\", \"JFK\", \"A69\", \"JFK\", \"A7\", \"JFK\", \"A70\", \"JFK\", \"A71\", \"JFK\", \"A72\", \"JFK\", \"A73\", \"JFK\", \"A74\", \"JFK\", \"A75\", \"JFK\", \"A76\", \"JFK\", \"A77\", \"JFK\", \"A78\", \"JFK\", \"A79\", \"JFK\", \"A8\", \"JFK\", \"A80\", \"JFK\", \"A81\", \"JFK\", \"A82\", \"JFK\", \"A83\", \"JFK\", \"A84\", \"JFK\", \"A85\", \"JFK\", \"A86\", \"JFK\", \"A87\", \"JFK\", \"A88\", \"JFK\", \"A89\", \"JFK\", \"A9\", \"JFK\", \"A90\", \"JFK\", \"A91\", \"JFK\", \"A92\", \"JFK\", \"A93\", \"JFK\", \"A94\", \"JFK\", \"A95\", \"JFK\", \"A96\", \"JFK\", \"A97\", \"JFK\", \"A98\", \"JFK\", \"A99\", \"JFK\"]", "is_sample": False}
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
        "topics": ["Depth-First Search", "Graph", "Eulerian Circuit"],
        "companyIndex": 1
    }

    output_path = "301-500/332_Reconstruct_Itinerary.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
