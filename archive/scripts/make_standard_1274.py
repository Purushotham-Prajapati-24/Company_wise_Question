import json
import os

def generate_json():
    problem_id = 1274
    title = "Number of Ships in a Rectangle"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1274. Number of Ships in a Rectangular Area</h3>
<p>Each ship is located at an integer point on a 2D plane. Each point can contain at most one ship.</p>

<p>You are given a function <code>hasShips(topRight, bottomLeft)</code> where <code>topRight</code> and <code>bottomLeft</code> are <code>Point</code> objects representing the coordinates of the top-right and bottom-left corners of a rectangle. The function returns <code>true</code> if there is at least one ship within the rectangle (including its boundary) and <code>false</code> otherwise.</p>

<p>Given two points <code>topRight</code> and <code>bottomLeft</code>, return the total number of ships in the rectangle. If the rectangle contains more than 100 ships, you can return 100.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://raw.githubusercontent.com/doocs/leetcode/main/solution/1200-1299/1274.Number%20of%20Ships%20in%20a%20Rectangle/images/1445_example_1.png" style="width: 496px; height: 500px;">
<pre><strong>Input:</strong> ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>On the 2D plane, there are at most <code>100</code> ships.</li>
	<li><code>topRight = [x<sub>tr</sub>, y<sub>tr</sub>]</code>, <code>bottomLeft = [x<sub>bl</sub>, y<sub>bl</sub>]</code></li>
	<li><code>0 &lt;= x<sub>bl</sub> &lt;= x<sub>tr</sub> &lt;= 1000</code></li>
	<li><code>0 &lt;= y<sub>bl</sub> &lt;= y<sub>tr</sub> &lt;= 1000</code></li>
	<li><code>hasShips</code> is called at most <code>10000</code> times.</li>
</ul>"""

    input_format = "A list of all ships coordinates, a `topRight` Point, and a `bottomLeft` Point provided as `[ships, topRight, bottomLeft]` in JSON."
    output_format = "An integer representing the number of ships."

    constraints = [
        "0 <= x, y <= 1000",
        "At most 100 ships",
        "hasShips called at most 10000 times"
    ]

    explanation = """To count ships in a rectangular area efficiently:
1. Use an interactive Divide and Conquer approach.
2. Define a recursive function `countShips(tr, bl)`:
   - If `tr.x < bl.x` or `tr.y < bl.y`, return 0.
   - If `!hasShips(tr, bl)`, return 0.
   - If `tr.x == bl.x` and `tr.y == bl.y`, the point must contain a ship (since `hasShips` was true), return 1.
   - Otherwise, split the rectangle into 4 smaller quadrants:
     - Find midpoint `midX = (tr.x + bl.x) // 2` and `midY = (tr.y + bl.y) // 2`.
     - Recursively call `countShips` for each of the 4 quadrants:
       - Top-Right: `countShips([tr.x, tr.y], [midX + 1, midY + 1])`
       - Top-Left: `countShips([midX, tr.y], [bl.x, midY + 1])`
       - Bottom-Right: `countShips([tr.x, midY], [midX + 1, bl.y])`
       - Bottom-Left: `countShips([midX, midY], [bl.x, bl.y])`
   - Sum the results and return."""

    answer = """class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def solve(tr, bl):
            if tr.x < bl.x or tr.y < bl.y:
                return 0
            if not sea.hasShips(tr, bl):
                return 0
            if tr.x == bl.x and tr.y == bl.y:
                return 1
            
            midX = (tr.x + bl.x) // 2
            midY = (tr.y + bl.y) // 2
            
            return (solve(Point(midX, midY), bl) +
                    solve(Point(tr.x, midY), Point(midX + 1, bl.y)) +
                    solve(Point(midX, tr.y), Point(bl.x, midY + 1)) +
                    solve(Point(tr.x, tr.y), Point(midX + 1, midY + 1)))
        
        return solve(topRight, bottomLeft)"""

    boilerplate = {
        "python": """import sys
import json

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Sea:
    def __init__(self, ships_list):
        self.ships = set(tuple(p) for p in ships_list)
        self.calls = 0
    def hasShips(self, tr: 'Point', bl: 'Point') -> bool:
        self.calls += 1
        for x in range(bl.x, tr.x + 1):
            for y in range(bl.y, tr.y + 1):
                if (x, y) in self.ships: return True
        return False

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        ships_list, tr_arr, bl_arr = json.loads(raw)
        sea = Sea(ships_list)
        sol = Solution()
        print(sol.countShips(sea, Point(tr_arr[0], tr_arr[1]), Point(bl_arr[0], bl_arr[1])))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Point {
public:
    int x, y;
};

class Sea {
public:
    bool hasShips(Point topRight, Point bottomLeft);
};

class Solution {
public:
    int countShips(Sea sea, Point topRight, Point bottomLeft) {
        // User logic here
        return 0;
    }
};

int main() {
    return 0;
}""",
        "java": """import java.util.*;

class Point {
    public int x, y;
    Point(int x, int y) { this.x = x; this.y = y; }
}

interface Sea {
    public boolean hasShips(Point topRight, Point bottomLeft);
}

class Solution {
    public int countShips(Sea sea, Point topRight, Point bottomLeft) {
        // User logic her
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {}
}""",
        "javascript": """/**
 * // This is Sea's API interface.
 * // You should not implement it, or speculate about its implementation
 * function Sea() {
 *     /**
 *      * @param {Point} topRight
 *      * @param {Point} bottomLeft
 *      * @return {boolean}
 *      */
 *     this.hasShips = function(topRight, bottomLeft) {
 *         ...
 *     };
 * };
 */

/**
 * // This is Point's API interface.
 * // You should not implement it, or speculate about its implementation
 * function Point(x, y) {
 *     this.x = x;
 *     this.y = y;
 * };
 */

/**
 * @param {Sea} sea
 * @param {Point} topRight
 * @param {Point} bottomLeft
 * @return {number}
 */
var countShips = function(sea, topRight, bottomLeft) {
    
};""",
        "c": """#include <stdio.h>
#include <stdlib.h>

struct Point {
    int x;
    int y;
};

int countShips(void* sea, struct Point topRight, struct Point bottomLeft) {
    // User logic here
    return 0;
}

int main() {
    return 0;
}"""
    }

    def solve(ships_list, tr, bl):
        ships = set(tuple(p) for p in ships_list)
        res = 0
        for x, y in ships:
            if bl[0] <= x <= tr[0] and bl[1] <= y <= tr[1]:
                res += 1
        return res

    test_cases_data = [
        [[[1,1],[2,2],[3,3],[5,5]], [4,4], [0,0]], # Sample 1
        [[[1,1],[1,1]], [2,2], [0,0]],            # Duplicate (if allowed)
        [[[0,0],[1000,1000]], [1000,1000], [0,0]], # Max range
        [[[500,500]], [501,501], [499,499]],        # Single ship
        [[[1,1],[1,2],[1,3]], [1,10], [1,0]],      # Vertical line
        [[[1,1],[2,1],[3,1]], [10,1], [0,1]],      # Horizontal line
        [[], [100,100], [0,0]],                    # No ships
        # Stress tests
        [[[i, i] for i in range(100)], [1000, 1000], [0, 0]], # 100 ships diagonal
        [[[i, 0] for i in range(100)], [1000, 1000], [0, 0]], # 100 ships bottom
        [[[i%10, i//10] for i in range(100)], [10, 10], [0, 0]] # 10x10 grid
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1], t[2]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 1})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Divide and Conquer", "Interactive"], "companyIndex": 0
    }

    output_path = f"1201-1400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
