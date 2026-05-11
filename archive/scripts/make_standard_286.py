import json
import collections
import os

def generate_json():
    problem_id = 286
    title = "Walls and Gates"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>286. Walls and Gates</h3>
<p>You are given a <code>m x n</code> 2D grid initialized with these three possible values:</p>

<ul>
	<li><code>-1</code>: A wall or an obstacle.</li>
	<li><code>0</code>: A gate.</li>
	<li><code>INF</code>: Infinity means an empty room. We use the value <code>2<sup>31</sup> - 1 = 2147483647</code> to represent <code>INF</code> as you may assume that the distance to a gate is less than <code>2147483647</code>.</li>
</ul>

<p>Fill each empty room with the distance to its <em>nearest gate</em>. If it is impossible to reach a gate, it should be filled with <code>INF</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/03/grid.jpg" style="width: 500px; height: 181px;" />
<pre><strong>Input:</strong> rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
<strong>Output:</strong> [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> rooms = [[-1]]
<strong>Output:</strong> [[-1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == rooms.length</code></li>
	<li><code>n == rooms[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 250</code></li>
	<li><code>rooms[i][j]</code> is <code>-1</code>, <code>0</code>, or <code>2147483647</code>.</li>
</ul>"""

    input_format = "A stringified 2D array of integers `rooms`."
    output_format = "A stringified 2D array with updated distances."
    
    constraints = [
        "1 <= m, n <= 250",
        "Values are -1, 0, or INF (2147483647)."
    ]
    
    explanation = """To fill empty rooms with the distance to the nearest gate efficiently:
1. **Multi-source BFS**: We use Breadth-First Search (BFS) starting from all gates simultaneously.
2. **Initialization**:
   - Find all gates (0) and add their coordinates `(r, c)` to a queue.
3. **Traversal**:
   - While the queue is not empty, pop a coordinate.
   - For each of its 4 neighbors (up, down, left, right):
     - If the neighbor is an empty room (`INF`), set its distance to `current_distance + 1` and add its coordinates to the queue.
4. **Final State**: Since BFS processes nodes level-by-level, the first time we reach an empty room, we've found its shortest distance to a gate.
5. **Complexity Analysis**:
   - Time: O(M * N) since we visit each cell at most once.
   - Space: O(M * N) in the worst case for the queue."""
    
    answer = """import collections

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
            
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque()
        
        # 1. Add all gates to the queue as starting points
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    
        # 2. Perform multi-source BFS
        while queue:
            r, c = queue.popleft()
            # Try all 4 directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                # Check boundaries and if it's an unvisited empty room
                if (0 <= nr < m and 0 <= nc < n and 
                    rooms[nr][nc] == 2147483647):
                    # 3. Mark the distance and add to queue
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))"""

    boilerplate = {
        "python": "import sys\nimport json\nimport collections\n\ndef wallsAndGates(rooms: list[list[int]]) -> None:\n    # User logic here (modify rooms in-place)\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        rooms = json.loads(input_data)\n        wallsAndGates(rooms)\n        print(json.dumps(rooms))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n#include <climits>\nusing namespace std;\n\nvoid wallsAndGates(vector<vector<int>>& rooms) {\n    // User logic here\n}\n\nint main() {\n    string all, line;\n    while (getline(cin, line)) all += line;\n    // Parse JSON 2D array\n    vector<vector<int>> rooms;\n    vector<int> row;\n    string num;\n    bool neg = false;\n    for (char c : all) {\n        if (c == '[') { neg = false; num = \"\"; }\n        else if (c == ']') {\n            if (!num.empty()) { row.push_back((neg?-1:1)*stoi(num)); num = \"\"; neg = false; }\n            if (!row.empty()) { rooms.push_back(row); row.clear(); }\n        }\n        else if (c == ',') {\n            if (!num.empty()) { row.push_back((neg?-1:1)*stoi(num)); num = \"\"; neg = false; }\n        }\n        else if (c == '-') neg = true;\n        else if (isdigit(c)) num += c;\n    }\n    wallsAndGates(rooms);\n    cout << '[';\n    for (int i = 0; i < (int)rooms.size(); i++) {\n        if (i) cout << ',';\n        cout << '[';\n        for (int j = 0; j < (int)rooms[i].size(); j++) {\n            if (j) cout << ',';\n            cout << rooms[i][j];\n        }\n        cout << ']';\n    }\n    cout << ']' << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public void wallsAndGates(int[][] rooms) {\n        // User logic here\n    }\n\n    public static void main(String[] args) throws Exception {\n        Scanner sc = new Scanner(System.in);\n        String all = sc.useDelimiter(\"\\\\A\").next().trim();\n        // Parse JSON 2D array\n        all = all.replaceAll(\"\\\\s\", \"\");\n        all = all.substring(1, all.length()-1); // remove outer []\n        String[] rowStrs = all.split(\"\\\\],\\\\[\");\n        int[][] rooms = new int[rowStrs.length][];\n        for (int i = 0; i < rowStrs.length; i++) {\n            String r = rowStrs[i].replaceAll(\"[\\\\[\\\\]]\", \"\");\n            String[] parts = r.split(\",\");\n            rooms[i] = new int[parts.length];\n            for (int j = 0; j < parts.length; j++) rooms[i][j] = Integer.parseInt(parts[j]);\n        }\n        new Solution().wallsAndGates(rooms);\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < rooms.length; i++) {\n            if (i > 0) sb.append(',');\n            sb.append('[');\n            for (int j = 0; j < rooms[i].length; j++) {\n                if (j > 0) sb.append(',');\n                sb.append(rooms[i][j]);\n            }\n            sb.append(']');\n        }\n        sb.append(']');\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\nconst rooms = JSON.parse(fs.readFileSync(0, 'utf-8').trim());\n\nfunction wallsAndGates(rooms) {\n    // User logic here\n}\n\nwallsAndGates(rooms);\nconsole.log(JSON.stringify(rooms));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nvoid wallsAndGates(int** rooms, int roomsSize, int* roomsColSize) {\n    // User logic here\n}\n\nint main() {\n    // For competitive use, input parsing of 2D JSON is done via Python/JS harness\n    // Stub main for C\n    printf(\"[]\\n\");\n    return 0;\n}"
    }

    INF = 2147483647
    test_cases = [
        {"input": "[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]", "expected_output": "[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]", "is_sample": True},
        {"input": "[[-1]]", "expected_output": "[[-1]]", "is_sample": True},
        {"input": "[[0]]", "expected_output": "[[0]]", "is_sample": False},
        {"input": "[[2147483647]]", "expected_output": "[[2147483647]]", "is_sample": False},
        {"input": "[[0,2147483647]]", "expected_output": "[[0,1]]", "is_sample": False},
        {"input": "[[0, -1, 2147483647]]", "expected_output": "[[0, -1, 2147483647]]", "is_sample": False},
        {"input": "[[0, 2147483647, 2147483647]]", "expected_output": "[[0, 1, 2]]", "is_sample": False},
        # Stress cases
        {"input": "[[0 if i==j==0 else 2147483647 for j in range(250)] for i in range(250)]", "expected_output": "...", "is_sample": False},
        {"input": "[[0 if i%50==0 and j%50==0 else 2147483647 for j in range(250)] for i in range(250)]", "expected_output": "...", "is_sample": False},
        {"input": "[[-1 for j in range(250)] for i in range(250)]", "expected_output": "...", "is_sample": False}
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
        "topics": ["Array", "Breadth-First Search", "Matrix"],
        "companyIndex": 0
    }

    output_path = "201-400/286_Walls_and_Gates.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
