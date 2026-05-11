import json
import os


def generate_json():
    problem_id = 391
    title = "Perfect Rectangle"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>391. Perfect Rectangle</h3>
<p>Given an array <code>rectangles</code> where <code>rectangles[i] = [x<sub>i</sub>, y<sub>i</sub>, a<sub>i</sub>, b<sub>i</sub>]</code> represents an axis-aligned rectangle. The bottom-left point of the rectangle is <code>(x<sub>i</sub>, y<sub>i</sub>)</code> and the top-right point is <code>(a<sub>i</sub>, b<sub>i</sub>)</code>.</p>

<p>Return <code>true</code> <em>if all the rectangles together form an exact cover of a rectangular region</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg" style="width: 300px; height: 294px;" />
<pre><strong>Input:</strong> rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
<strong>Output:</strong> true
<strong>Explanation:</strong> All 5 rectangles together form an exact cover of a rectangular region.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perfectrec2-plane.jpg" style="width: 300px; height: 294px;" />
<pre><strong>Input:</strong> rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Because there is a gap between the two rectangular regions.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg" style="width: 300px; height: 294px;" />
<pre><strong>Input:</strong> rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Because two of the rectangles overlap with each other.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= rectangles.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>rectangles[i].length == 4</code></li>
	<li><code>-10<sup>5</sup> &lt;= x<sub>i</sub>, y<sub>i</sub>, a<sub>i</sub>, b<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = """A list of rectangles where each rectangle is [x, y, a, b]."""
    output_format = """A boolean value."""
    
    constraints = ["1 <= rectangles.length <= 2 * 10^4", "Coordinate values between -10^5 and 10^5."]
    
    explanation = """To determine if a set of rectangles forms a perfect rectangle (an exact cover of a larger rectangular region):
1. **Area Check**: The sum of the areas of all individual rectangles must equal the area of the bounding box formed by the minimum and maximum coordinates $(x1, y1)$ and $(x2, y2)$.
   - Area sum $= \sum (a_i - x_i) \times (b_i - y_i)$.
   - Bounding area $= (x2 - x1) \times (y2 - y1)$.
2. **Corner Consistency**: 
   - Every point in the set of all rectangles' corners must appear an even number of times, EXCEPT for the four corners of the final bounding box, which must each appear exactly once.
   - If any point appears more than 4 times (for very complex overlaps) or an odd number of times (except the 4 main corners), it violates the perfect cover property.

### Algorithm Steps:
1. Initialize `area_sum = 0`. Track `min_x, min_y, max_x, max_y`.
2. Use a set or hash map to track the count of each corner $(x_i, y_i), (x_i, b_i), (a_i, y_i), (a_i, b_i)$.
3. For each rectangle:
   - Calculate area and update bounding box.
   - For each of its 4 corners, toggle it in a set (or check counts). If using a set, an even number of appearances means the point is removed.
4. After processing all rectangles:
   - Check if `area_sum` matches the bounding box area.
   - Check if the set contains exactly the 4 bounding box corners.

### Complexity:
- **Time Complexity**: $O(N)$, where $N$ is the number of rectangles.
- **Space Complexity**: $O(N)$ for the set/map of corners."""
    
    answer = """def isPerfectRectangle(rectangles):
    import collections
    corners = collections.defaultdict(int)
    area = 0
    x1, y1 = float('inf'), float('inf')
    x2, y2 = float('-inf'), float('-inf')
    
    for r in rectangles:
        x, y, a, b = r
        area += (a - x) * (b - y)
        x1, y1 = min(x1, x), min(y1, y)
        x2, y2 = max(x2, a), max(y2, b)
        
        for p in [(x, y), (x, b), (a, y), (a, b)]:
            corners[p] += 1
            
    if area != (x2 - x1) * (y2 - y1):
        return False
    
    expected_corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
    for p, count in corners.items():
        if p in expected_corners:
            if count != 1: return False
        else:
            if count % 2 != 0: return False
            
    return True"""

    answer = """class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')
        corners = set()
        
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
            
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
                    
        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        if corners != expected_corners:
            return False
            
        return area == (max_x - min_x) * (max_y - min_y)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        # User Logic Here
        pass

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        try:
            rects = json.loads(line)
        except:
            if line.startswith('"') and line.endswith('"'):
                line = line[1:-1].replace('\\"', '"')
            rects = json.loads(line)
        sol = Solution()
        print(json.dumps(sol.isRectangleCover(rects)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        // User Logic Here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        if (line.size() >= 2 && line.front() == '"' && line.back() == '"') {
             line = line.substr(1, line.size()-2);
        }
        
        vector<vector<int>> rects;
        string inner = "";
        bool inArray = false;
        for (char c : line) {
            if (c == '[') {
                if (inArray) inner = "";
                inArray = true;
            } else if (c == ']') {
                if (inner != "") {
                    vector<int> r;
                    stringstream ss(inner);
                    string val;
                    while (getline(ss, val, ',')) r.push_back(stoi(val));
                    if (r.size() == 4) rects.push_back(r);
                    inner = "";
                }
                inArray = false;
            } else if (inArray) {
                inner += c;
            }
        }
        Solution sol;
        cout << (sol.isRectangleCover(rects) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        // User Logic Here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            if (line.startsWith("\\\"")) line = line.substring(1, line.length()-1).replace("\\\\\\\"", "\\\"");
            
            List<int[]> list = new ArrayList<>();
            if (line.length() > 2) {
                line = line.substring(1, line.length()-1); // remove outer []
                int i = 0;
                while (i < line.length()) {
                    if (line.charAt(i) == '[') {
                        int j = i;
                        while (j < line.length() && line.charAt(j) != ']') j++;
                        String content = line.substring(i+1, j);
                        String[] parts = content.split(",");
                        int[] r = new int[parts.length];
                        for (int k=0; k<parts.length; k++) r[k] = Integer.parseInt(parts[k].trim());
                        list.add(r);
                        i = j + 1;
                    } else {
                        i++;
                    }
                }
            }
            int[][] rects = list.toArray(new int[0][0]);
            Solution sol = new Solution();
            System.out.println(sol.isRectangleCover(rects));
        }
    }
}""",
        "javascript": """var isRectangleCover = function(rectangles) {
    // User Logic Here
};

const fs = require('fs');
let input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    if (input.startsWith('"')) {
        try { input = JSON.parse(input); } catch(e) { input = input.slice(1, -1); }
    }
    const rects = typeof input === 'string' ? JSON.parse(input) : input;
    console.log(isRectangleCover(rects));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isRectangleCover(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    // User Logic Here
    return false;
}

int main() {
    char* line = malloc(1000005);
    if (fgets(line, 1000005, stdin)) {
        int** rects = malloc(20000 * sizeof(int*));
        int count = 0;
        char* token = strtok(line, "[], ");
        while (token != NULL) {
            rects[count] = malloc(4 * sizeof(int));
            rects[count][0] = atoi(token);
            rects[count][1] = atoi(strtok(NULL, "[], "));
            rects[count][2] = atoi(strtok(NULL, "[], "));
            rects[count][3] = atoi(strtok(NULL, "[], "));
            count++;
            token = strtok(NULL, "[], ");
        }
        int* colSize = malloc(count * sizeof(int));
        for (int i=0; i<count; i++) colSize[i] = 4;
        printf("%s\\n", isRectangleCover(rects, count, colSize) ? "true" : "false");
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]", "expected_output": "true", "is_sample": True},
        {"input": "[[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]", "expected_output": "false", "is_sample": True},
        # 5 Diverse
        {"input": "[[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4]]", "expected_output": "false", "is_sample": False},
        {"input": "[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]", "expected_output": "true", "is_sample": False},
        {"input": "[[1,1,3,3]]", "expected_output": "true", "is_sample": False},
        {"input": "[[1,1,2,2],[1,1,2,2]]", "expected_output": "false", "is_sample": False},
        {"input": "[[0,0,1,1],[0,1,3,2],[1,0,2,1]]", "expected_output": "false", "is_sample": False},
        # 3 Stress
        {"input": "[[1,1,2,2],[2,1,3,2],[1,2,2,3],[2,2,3,3]]", "expected_output": "true", "is_sample": False},
        {"input": "[[0,0,1,1],[1,1,2,2]]", "expected_output": "false", "is_sample": False},
        {"input": "[[0,0,4,4],[0,0,1,1],[1,1,2,2],[2,2,3,3],[3,3,4,4]]", "expected_output": "false", "is_sample": False}
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 1
    }

    output_path = "301-500/391_Perfect_Rectangle.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
