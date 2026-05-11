import json
import os

def generate_json():
    problem_id = 490
    title = "The Maze"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>490. The Maze</h3>
<p>There is a ball in a <code>maze</code> with empty spaces (represented as <code>0</code>) and walls (represented as <code>1</code>). The ball can go through the empty spaces by rolling <strong>up, down, left or right</strong>, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.</p>

<p>Given the <code>m x n</code> <code>maze</code>, the ball's <code>start</code> position and the <code>destination</code>, where <code>start = [start<sub>row</sub>, start<sub>col</sub>]</code> and <code>destination = [destination<sub>row</sub>, destination<sub>col</sub>]</code>, return <code>true</code> if the ball can stop at the destination, otherwise return <code>false</code>.</p>

<p>You may assume that <strong>the borders of the maze are all walls</strong> (see examples).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/03/31/maze1-1-grid.jpg" style="width: 573px; height: 573px;" />
<pre><strong>Input:</strong> maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> One possible way is : left -> down -> left -> down -> right -> down -> right.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/03/31/maze1-2-grid.jpg" style="width: 573px; height: 573px;" />
<pre><strong>Input:</strong> maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == maze.length</code></li>
	<li><code>n == maze[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>maze[i][j]</code> is <code>0</code> or <code>1</code>.</li>
	<li><code>start.length == 2</code></li>
	<li><code>destination.length == 2</code></li>
	<li><code>0 &lt;= start<sub>row</sub>, destination<sub>row</sub> &lt; m</code></li>
	<li><code>0 &lt;= start<sub>col</sub>, destination<sub>col</sub> &lt; n</code></li>
    <li>Both the ball and the destination exist in an empty space, and they will not be at the same position initially.</li>
</ul>"""

    input_format = "Line 1: A JSON 2D array `maze`.\\nLine 2: A JSON array `start` of size 2.\\nLine 3: A JSON array `destination` of size 2."
    output_format = "A boolean value `true` if the ball can stop at the destination, otherwise `false`."
    
    constraints = [
        "1 <= m, n <= 100",
        "maze[i][j] is 0 or 1",
        "0 <= start_row, destination_row < m",
        "0 <= start_col, destination_col < n"
    ]
    
    explanation = "This problem can be solved using BFS or DFS. The key is in the movement logic: instead of moving one Step at a time, the ball rolls until it hits a wall. Only the stopping positions are considered as nodes in the graph traversal."
    
    answer = """import collections

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        queue = collections.deque([tuple(start)])
        visited = {tuple(start)}
        dest = tuple(destination)
        
        while queue:
            r, c = queue.popleft()
            if (r, c) == dest:
                return True
                
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r, c
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr+dr][nc+dc] == 0:
                    nr += dr
                    nc += dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:\n        # User logic here\n        return False\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().strip().splitlines()\n    if len(lines) >= 3:\n        maze = json.loads(lines[0])\n        start = json.loads(lines[1])\n        destination = json.loads(lines[2])\n        sol = Solution()\n        print(json.dumps(sol.hasPath(maze, start, destination)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <sstream>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {\n        // User logic here\n        return false;\n    }\n};\n\nint main() {\n    string line; if (getline(cin, line)) {\n        vector<vector<int>> maze; int i = 0;\n        while (i < line.length()) {\n            if (line[i] == '[') {\n                i++; if (i < line.length() && line[i] == '[') {\n                    vector<int> row; string cur; i++;\n                    while (i < line.length() && line[i] != ']') {\n                        if (isdigit(line[i]) || line[i] == '-') cur += line[i];\n                        else if (line[i] == ',' && !cur.empty()) { row.push_back(stoi(cur)); cur = \"\"; }\n                        i++;\n                    } if (!cur.empty()) row.push_back(stoi(cur));\n                    maze.push_back(row);\n                }\n            } i++;\n        }\n        vector<int> start(2), dest(2); string sLine, dLine; getline(cin, sLine); getline(cin, dLine);\n        auto parseArr = [](string s) { vector<int> res; string cur; for (char c : s) if (isdigit(c) || c == '-') cur += c; else if (c == ',' && !cur.empty()) { res.push_back(stoi(cur)); cur = \"\"; } if (!cur.empty()) res.push_back(stoi(cur)); return res; };\n        start = parseArr(sLine); dest = parseArr(dLine);\n        Solution sol; cout << (sol.hasPath(maze, start, dest) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public boolean hasPath(int[][] maze, int[] start, int[] destination) {\n        // User logic here\n        return false;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String mazeLine = sc.nextLine();\n            String[] rowParts = mazeLine.substring(1, mazeLine.length() - 1).split(\"\\\\],\\\\s*\\\\[\");\n            List<int[]> mazeList = new ArrayList<>();\n            for (String rowPart : rowParts) {\n                String cleanRow = rowPart.replaceAll(\"[\\\\[\\\\]]\", \"\");\n                if (cleanRow.isEmpty()) continue;\n                String[] nums = cleanRow.split(\",\\\\s*\");\n                int[] row = new int[nums.length];\n                for (int i = 0; i < nums.length; i++) row[i] = Integer.parseInt(nums[i]);\n                mazeList.add(row);\n            }\n            int[][] maze = mazeList.toArray(new int[0][]);\n            int[] start = new int[2]; String sLine = sc.nextLine();\n            String[] sParts = sLine.replaceAll(\"[\\\\[\\\\]\\\\s]\", \"\").split(\",\");\n            start[0] = Integer.parseInt(sParts[0]); start[1] = Integer.parseInt(sParts[1]);\n            int[] dest = new int[2]; String dLine = sc.nextLine();\n            String[] dParts = dLine.replaceAll(\"[\\\\[\\\\]\\\\s]\", \"\").split(\",\");\n            dest[0] = Integer.parseInt(dParts[0]); dest[1] = Integer.parseInt(dParts[1]);\n            System.out.println(new Solution().hasPath(maze, start, dest));\n        }\n    }\n}",
        "javascript": "/**\n * @param {number[][]} maze\n * @param {number[]} start\n * @param {number[]} destination\n * @return {boolean}\n */\nvar hasPath = function(maze, start, destination) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim().split('\\n');\nif (input.length >= 3) {\n    const maze = JSON.parse(input[0]);\n    const start = JSON.parse(input[1]);\n    const destination = JSON.parse(input[2]);\n    console.log(hasPath(maze, start, destination));\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <stdlib.h>\n\nbool hasPath(int** maze, int mazeSize, int* mazeColSize, int* start, int startSize, int* destination, int destinationSize) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    printf(\"false\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\\n[0,4]\\n[4,4]", "expected_output": "true", "is_sample": True},
        {"input": "[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\\n[0,4]\\n[3,2]", "expected_output": "false", "is_sample": True},
        {"input": "[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]\\n[4,3]\\n[0,1]", "expected_output": "false", "is_sample": True},
        {"input": "[[0,0],[0,0]]\\n[0,0]\\n[1,1]", "expected_output": "true", "is_sample": False},
        {"input": "[[0,1],[1,0]]\\n[0,0]\\n[1,1]", "expected_output": "false", "is_sample": False},
        {"input": "[[0,0,0],[0,1,0],[0,0,0]]\\n[0,0]\\n[2,2]", "expected_output": "true", "is_sample": False},
        {"input": "[[0,0,0],[0,1,0],[0,0,0]]\\n[0,0]\\n[1,1]", "expected_output": "false", "is_sample": False}, # Cannot stop at (1,1)
        {"input": "[[0,0,0,0],[0,0,0,0]]\\n[0,0]\\n[0,3]", "expected_output": "true", "is_sample": False},
        {"input": "[[0,0,0,0],[0,0,0,0]]\\n[0,0]\\n[1,0]", "expected_output": "true", "is_sample": False},
        {"input": json.dumps([[0]*10 for _ in range(10)]) + "\\n[0,0]\\n[9,9]", "expected_output": "true", "is_sample": False}
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
        "topics": ["Depth-First Search", "Breadth-First Search", "Graph"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_The_Maze.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
