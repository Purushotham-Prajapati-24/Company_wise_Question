import json
import os

def generate_json():
    problem_id = 447
    title = "Number of Boomerangs"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>447. Number of Boomerangs</h3>
<p>You are given <code>n</code> <code>points</code> in the plane that are all <strong>distinct</strong>, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. A <strong>boomerang</strong> is a tuple of points <code>(i, j, k)</code> such that the distance between <code>i</code> and <code>j</code> equals the distance between <code>i</code> and <code>k</code> (<strong>the order of the tuple matters</strong>).</p>

<p>Return <em>the number of boomerangs</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> points = [[0,0],[1,0],[2,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> points = [[1,1]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == points.length</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>All the points are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A JSON 2D array of integers `points`."
    output_format = "An integer representing the number of boomerangs."
    
    constraints = [
        "n == points.length",
        "1 <= n <= 500",
        "points[i].length == 2",
        "-10^4 <= xi, yi <= 10^4",
        "All the points are unique."
    ]
    
    explanation = "Iterate through each point `i` and treat it as the 'head' of the boomerang. For each other point `j`, calculate the squared distance `d(i, j)`. Store the frequency of each distance in a hash map. For each distance that appears `f` times, the number of boomerangs with `i` as the head is `f * (f - 1)`."
    
    answer = """from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for p1 in points:
            dists = defaultdict(int)
            for p2 in points:
                d = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
                dists[d] += 1
            for d in dists:
                f = dists[d]
                total += f * (f - 1)
        return total"""

    boilerplate = {
        "python": """import sys
import json
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        # User Logic Here
        return 0

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        points = json.loads(raw_input)
        sol = Solution()
        print(sol.numberOfBoomerangs(points))""",
        "cpp": """#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        // User Logic Here
        return 0;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        // Parse 2D array...
        cout << 0 << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int numberOfBoomerangs(int[][] points) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        // I/O parsing...
    }
}""",
        "javascript": """/**
 * @param {number[][]} points
 * @return {number}
 */
var numberOfBoomerangs = function(points) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const points = JSON.parse(input);
    console.log(numberOfBoomerangs(points));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int numberOfBoomerangs(int** points, int pointsSize, int* pointsColSize) {
    // User Logic Here
    return 0;
}

int main() {
    return 0;
}"""
    }

    test_cases = [
        {"input": "[[0,0],[1,0],[2,0]]", "expected_output": "2", "is_sample": True},
        {"input": "[[1,1],[2,2],[3,3]]", "expected_output": "2", "is_sample": True},
        {"input": "[[1,1]]", "expected_output": "0", "is_sample": False},
        {"input": "[[0,0],[1,0],[0,1],[-1,0],[0,-1]]", "expected_output": "20", "is_sample": False},
        {"input": "[[1,1],[1,2],[2,1]]", "expected_output": "2", "is_sample": False},
        {"input": "[[0,0],[1,1],[2,2],[3,3],[4,4]]", "expected_output": "12", "is_sample": False},
        {"input": "[[0,0],[1,1],[1,-1],[-1,1],[-1,-1]]", "expected_output": "12", "is_sample": False},
        {"input": "[[0,0],[1,0],[0,1]]", "expected_output": "2", "is_sample": False},
        {"input": "[ [0,0], [1,0], [-1,0] ]", "expected_output": "2", "is_sample": False}, # Whitebox
        {"input": "[[0,0],[3,4],[0,5],[4,3],[5,0]]", "expected_output": "8", "is_sample": False}
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
        "topics": ["Hash Table", "Math"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Number_of_Boomerangs.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
