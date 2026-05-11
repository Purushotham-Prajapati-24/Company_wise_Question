import json
import os

def generate_json():
    problem_id = 463
    title = "Island Perimeter"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>463. Island Perimeter</h3>
<p>You are given <code>row x col</code> <code>grid</code> representing a map where <code>grid[i][j] = 1</code> represents&nbsp;land and <code>grid[i][j] = 0</code> represents water.</p>

<p>Grid cells are connected <strong>horizontally/vertically</strong> (not diagonally). The <code>grid</code> is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).</p>

<p>The island doesn't have "lakes", i.e., the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px;" />
<pre><strong>Input:</strong> grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
<strong>Output:</strong> 16
<strong>Explanation:</strong> The perimeter is the 16 yellow edges in the image above.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> grid = [[1]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> grid = [[1,0]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>row == grid.length</code></li>
	<li><code>col == grid[i].length</code></li>
	<li><code>1 &lt;= row, col &lt;= 100</code></li>
	<li><code>grid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
	<li>There is exactly one island in <code>grid</code>.</li>
</ul>"""

    input_format = "Line 1: A JSON 2D array `grid` where 1 represents land and 0 represents water."
    output_format = "An integer representing the perimeter of the island."
    
    constraints = [
        "1 <= row, col <= 100",
        "grid[i][j] is 0 or 1",
        "There is exactly one island."
    ]
    
    explanation = "Iterate through each cell in the grid. If a cell is land (1), add 4 to the perimeter. Then, check its neighbors (top and left). For each adjacent land cell, subtract 2 from the perimeter (as those two cells share an edge)."
    
    answer = """class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
        return perimeter"""

    boilerplate = {
        "python": r"""import sys
import json

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        # User Logic Here
        return 0

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        grid = json.loads(line)
        sol = Solution()
        print(sol.islandPerimeter(grid))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        // User Logic Here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<vector<int>> grid;
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
                        grid.push_back(row);
                    }
                    i++;
                }
            }
            i++;
        }
        Solution sol;
        cout << sol.islandPerimeter(grid) << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public int islandPerimeter(int[][] grid) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            String[] rowParts = line.substring(1, line.length() - 1).split("\\\\],\\\\s*\\\\[");
            List<int[]> gridList = new ArrayList<>();
            for (String rowPart : rowParts) {
                String cleanRow = rowPart.replaceAll("[\\\\[\\\\]]", "");
                if (cleanRow.isEmpty()) continue;
                String[] nums = cleanRow.split(",\\\\s*");
                int[] row = new int[nums.length];
                for (int i = 0; i < nums.length; i++) row[i] = Integer.parseInt(nums[i]);
                gridList.add(row);
            }
            int[][] grid = gridList.toArray(new int[0][]);
            Solution sol = new Solution();
            System.out.println(sol.islandPerimeter(grid));
        }
    }
}""",
        "javascript": r"""/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const grid = JSON.parse(input);
    console.log(islandPerimeter(grid));
}""",
        "c": r"""#include <stdio.h>
#include <stdlib.h>

int islandPerimeter(int** grid, int gridSize, int* gridColSize) {
    // User Logic Here
    return 0;
}

int main() {
    // Manual parsing logic for 2D array...
    printf("0\n");
    return 0;
}"""
    }

    test_cases = [
        {"input": "[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]", "expected_output": "16", "is_sample": True},
        {"input": "[[1]]", "expected_output": "4", "is_sample": True},
        {"input": "[[1,0]]", "expected_output": "4", "is_sample": True},
        {"input": "[[1,1],[1,1]]", "expected_output": "8", "is_sample": False},
        {"input": "[[0,1,0],[1,1,1],[0,1,0]]", "expected_output": "12", "is_sample": False},
        {"input": "[[1,1,1]]", "expected_output": "8", "is_sample": False},
        {"input": "[[1],[1],[1]]", "expected_output": "8", "is_sample": False},
        {"input": "[[0,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,1]]", "expected_output": "14", "is_sample": False},
        {"input": "[[1,1,1,1],[1,0,0,1],[1,1,1,1]]", "expected_output": "22", "is_sample": False},
        {"input": json.dumps([[1 if (i+j)%2==0 else 0 for j in range(10)] for i in range(10)][:1]), "expected_output": "22", "is_sample": False} # Simple row case
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
        "topics": ["Array", "Hash Table", "Matrix", "Depth-First Search", "Breadth-First Search"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Island_Perimeter.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
