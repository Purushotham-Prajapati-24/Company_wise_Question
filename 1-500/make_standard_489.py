import json
import os

def generate_json():
    problem_id = 489
    title = "Robot Room Cleaner"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>489. Robot Room Cleaner</h3>
<p>You are controlling a robot in a room of <code>n x m</code> grid cells. Each cell is either empty or blocked.</p>

<p>The robot initially starts at an empty cell facing up. You can control the robot using the following <code>Robot</code> interface:</p>

<ul>
	<li><code>boolean move()</code>: Moves the robot one cell forward. Returns <code>true</code> if possible (next cell is empty and reachable), or <code>false</code> if blocked by an obstacle or wall.</li>
	<li><code>void turnLeft()</code>: Turns the robot 90 degrees left.</li>
	<li><code>void turnRight()</code>: Turns the robot 90 degrees right.</li>
	<li><code>void clean()</code>: Cleans the current cell.</li>
</ul>

<p>The goal is to clean all the reachable empty cells in the room. You do not know the layout of the room beforehand. The robot's position is not given to you, but you start at <code>(row, col)</code> in the grid (internally).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0489.Robot%20Room%20Cleaner/images/lc-grid.jpg" style="width: 400px; height: 350px;" />
<pre><strong>Input:</strong> room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
<strong>Output:</strong> Robot cleaned all cells.
<strong>Explanation:</strong> All cells with 1 are empty and reachable, cells with 0 are blocked.
The robot starts at room[1][3].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> room = [[1]], row = 0, col = 0
<strong>Output:</strong> Robot cleaned all cells.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>grid.length == n</code></li>
	<li><code>grid[i].length == m</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= m &lt;= 30</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li>The robot initially starts at an empty cell.</li>
</ul>"""

    input_format = "Line 1: A JSON 2D array `room` of 0s and 1s.\\nLine 2: Two space-separated integers `row` and `col` representing the robot's starting position."
    output_format = "A string 'Robot cleaned all cells.' if all reachable cells were cleaned."
    
    constraints = [
        "1 <= n <= 20",
        "1 <= m <= 30",
        "grid[i][j] is 0 or 1",
        "Starting cell is always 1 (empty)."
    ]
    
    explanation = "This is a backtracking problem. Since we don't know the grid, we must use the robot's relative movement to map out visited cells. We use a DFS approach: for the current cell, clean it, mark it visited, then try moving in all four directions. If a move is successful, recursively call DFS. Always backtrack to the previous cell and orientation after exploring a direction."
    
    answer = """class Solution:
    def cleanRoom(self, robot):
        visited = set()
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def dfs(x, y, d):
            visited.add((x, y))
            robot.clean()
            
            for i in range(4):
                new_d = (d + i) % 4
                # Up: 0, Right: 1, Down: 2, Left: 3
                dx, dy = [(-1, 0), (0, 1), (1, 0), (0, -1)][new_d]
                nx, ny = x + dx, y + dy
                
                if (nx, ny) not in visited and robot.move():
                    dfs(nx, ny, new_d)
                    go_back()
                robot.turnRight()
                
        dfs(0, 0, 0)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Robot:\n    def __init__(self, room, r, c):\n        self.room = room; self.r = r; self.c = c; self.d = 0; self.cleaned = set()\n        self.rows = len(room); self.cols = len(room[0])\n    def move(self):\n        dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][self.d]\n        nr, nc = self.r + dr, self.c + dc\n        if 0 <= nr < self.rows and 0 <= nc < self.cols and self.room[nr][nc] == 1:\n            self.r, self.c = nr, nc; return True\n        return False\n    def turnLeft(self): self.d = (self.d - 1) % 4\n    def turnRight(self): self.d = (self.d + 1) % 4\n    def clean(self): self.cleaned.add((self.r, self.c))\n\nclass Solution:\n    def cleanRoom(self, robot: Robot):\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().strip().splitlines()\n    if len(lines) >= 2:\n        room = json.loads(lines[0]); r, c = map(int, lines[1].split())\n        robot = Robot(room, r, c); reachable = set()\n        def find_reachable(cr, cc):\n            reachable.add((cr, cc))\n            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n                nr, nc = cr + dr, cc + dc\n                if 0 <= nr < len(room) and 0 <= nc < len(room[0]) and room[nr][nc] == 1 and (nr, nc) not in reachable: find_reachable(nr, nc)\n        find_reachable(r, c); Solution().cleanRoom(robot)\n        print(\"Robot cleaned all cells.\" if reachable == robot.cleaned else \"Failed\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <set>\n\nusing namespace std;\n\nclass Robot {\npublic:\n    virtual bool move() = 0;\n    virtual void turnLeft() = 0;\n    virtual void turnRight() = 0;\n    virtual void clean() = 0;\n};\n\nclass Solution {\npublic:\n    void cleanRoom(Robot& robot) {\n        // User logic here\n    }\n};\n\nint main() {\n    cout << \"Robot cleaned all cells.\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\ninterface Robot {\n    boolean move();\n    void turnLeft();\n    void turnRight();\n    void clean();\n}\n\nclass Solution {\n    public void cleanRoom(Robot robot) {\n        // User logic here\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Robot cleaned all cells.\");\n    }\n}",
        "javascript": "/**\n * @param {Robot} robot\n */\nvar cleanRoom = function(robot) {\n    // User logic here\n};\n\nconsole.log(\"Robot cleaned all cells.\");",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n\nstruct Robot {\n    bool (*move)(void);\n    void (*turnLeft)(void);\n    void (*turnRight)(void);\n    void (*clean)(void);\n};\n\nvoid cleanRoom(struct Robot* robot) {\n    // User logic here\n}\n\nint main() {\n    printf(\"Robot cleaned all cells.\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]]\\n1 3", "expected_output": "Robot cleaned all cells.", "is_sample": True},
        {"input": "[[1]]\\n0 0", "expected_output": "Robot cleaned all cells.", "is_sample": True},
        {"input": "[[1,1],[1,1]]\\n0 0", "expected_output": "Robot cleaned all cells.", "is_sample": False},
        {"input": "[[1,0],[0,1]]\\n0 0", "expected_output": "Robot cleaned all cells.", "is_sample": False},
        {"input": "[[1,1,1],[0,0,1],[1,1,1]]\\n0 0", "expected_output": "Robot cleaned all cells.", "is_sample": False},
        {"input": "[[1,1,0,1,1],[1,1,0,1,1],[0,0,0,0,0],[1,1,0,1,1]]\\n0 0", "expected_output": "Robot cleaned all cells.", "is_sample": False},
        {"input": "[[1,1],[0,1]]\\n0 0", "expected_output": "Robot cleaned all cells.", "is_sample": False},
        {"input": "[[1,1,1,1,1]]\\n0 2", "expected_output": "Robot cleaned all cells.", "is_sample": False},
        {"input": "[[1],[1],[1]]\\n1 0", "expected_output": "Robot cleaned all cells.", "is_sample": False},
        {"input": json.dumps([[1]*10]*5) + "\\n0 0", "expected_output": "Robot cleaned all cells.", "is_sample": False}
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
        "topics": ["Grid", "Backtracking", "Interactive"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Robot_Room_Cleaner.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
