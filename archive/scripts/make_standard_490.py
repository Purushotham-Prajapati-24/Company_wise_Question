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
        "python": r"""import sys
import json
import collections

class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        # User Logic Here
        return False

if __name__ == '__main__':
    lines = sys.stdin.read().strip().splitlines()
    if len(lines) >= 3:
        maze = json.loads(lines[0])
        start = json.loads(lines[1])
        destination = json.loads(lines[2])
        sol = Solution()
        print(json.dumps(sol.hasPath(maze, start, destination)))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        // User Logic Here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<vector<int>> maze;
        // Simple manual parsing for 2D array
        string rowStr;
        bool inRow = false;
        vector<int> currentRow;
        for (char c : line) {
            if (c == '[') {
                if (!inRow) inRow = true;
                else {currentRow.clear();}
            } else if (c == ']') {
                if (!currentRow.empty() || line.find("[]", line.find_last_of("[")) == string::npos) {
                    maze.push_back(currentRow);
                    currentRow.clear();
                }
            } else if (isdigit(c) || c == '-') {
                string num;
                num += c;
                // Simplified... in reality need to handle multi-digit
            }
        }
        // Actually, for maze, better manual parsing:
        maze.clear();
        int i = 0;
        while(i < line.length()){
            if(line[i] == '['){
                i++;
                while(i < line.length() && line[i] != ']'){
                    if(line[i] == '['){
                        i++;
                        vector<int> row;
                        string cur = "";
                        while(i < line.length() && line[i] != ']'){
                            if(isdigit(line[i]) || line[i] == '-') cur += line[i];
                            else if(line[i] == ',' && !cur.empty()){
                                row.push_back(stoi(cur));
                                cur = "";
                            }
                            i++;
                        }
                        if(!cur.empty()) row.push_back(stoi(cur));
                        maze.push_back(row);
                    }
                    i++;
                }
            }
            i++;
        }

        vector<int> start(2), dest(2);
        string sLine, dLine;
        getline(cin, sLine);
        getline(cin, dLine);
        auto parseArr = [](string s){
            vector<int> res; string cur;
            for(char c: s) if(isdigit(c) || c=='-') cur+=c; else if(c==',' && !cur.empty()){ res.push_back(stoi(cur)); cur=""; }
            if(!cur.empty()) res.push_back(stoi(cur));
            return res;
        };
        start = parseArr(sLine);
        dest = parseArr(dLine);

        Solution sol;
        cout << (sol.hasPath(maze, start, dest) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        // User Logic Here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String mazeLine = sc.nextLine();
            // Robust parsing of 2D array
            String[] rowParts = mazeLine.substring(1, mazeLine.length() - 1).split("\\\\],\\\\s*\\\\[");
            List<int[]> mazeList = new ArrayList<>();
            for (String rowPart : rowParts) {
                String cleanRow = rowPart.replaceAll("[\\\\[\\\\]]", "");
                if (cleanRow.isEmpty()) continue;
                String[] nums = cleanRow.split(",\\\\s*");
                int[] row = new int[nums.length];
                for (int i = 0; i < nums.length; i++) row[i] = Integer.parseInt(nums[i]);
                mazeList.add(row);
            }
            int[][] maze = mazeList.toArray(new int[0][]);
            
            int[] start = new int[2];
            String sLine = sc.nextLine();
            String[] sParts = sLine.replaceAll("[\\\\[\\\\]\\\\s]", "").split(",");
            start[0] = Integer.parseInt(sParts[0]); start[1] = Integer.parseInt(sParts[1]);
            
            int[] dest = new int[2];
            String dLine = sc.nextLine();
            String[] dParts = dLine.replaceAll("[\\\\[\\\\]\\\\s]", "").split(",");
            dest[0] = Integer.parseInt(dParts[0]); dest[1] = Integer.parseInt(dParts[1]);
            
            Solution sol = new Solution();
            System.out.println(sol.hasPath(maze, start, dest));
        }
    }
}""",
        "javascript": r"""/**
 * @param {number[][]} maze
 * @param {number[]} start
 * @param {number[]} destination
 * @return {boolean}
 */
var hasPath = function(maze, start, destination) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\n');
if (input.length >= 3) {
    const maze = JSON.parse(input[0]);
    const start = JSON.parse(input[1]);
    const destination = JSON.parse(input[2]);
    console.log(hasPath(maze, start, destination));
}""",
        "c": r"""#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool hasPath(int** maze, int mazeSize, int* mazeColSize, int* start, int startSize, int* destination, int destinationSize) {
    // User Logic Here
    return false;
}

int main() {
    // Manual parsing logic for 2D array and start/dest...
    printf("false\n");
    return 0;
}"""
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
