import json
import os

def generate_json():
    problem_id = 3001
    title = "Minimum Moves to Capture Queen"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>3001. Minimum Moves to Capture Queen</h3>
<p>There is a <strong>8 x 8</strong> chessboard containing three pieces: a <strong>white rook</strong>, a <strong>white bishop</strong>, and a <strong>black queen</strong>.</p>

<p>You are given six integers <code>a</code>, <code>b</code>, <code>c</code>, <code>d</code>, <code>e</code>, and <code>f</code> where:</p>

<ul>
	<li><code>(a, b)</code> is the position of the white rook.</li>
	<li><code>(c, d)</code> is the position of the white bishop.</li>
	<li><code>(e, f)</code> is the position of the black queen.</li>
</ul>

<p>Given that the rook and bishop can move any number of steps and they <strong>cannot</strong> jump over other pieces, return <em>the <strong>minimum</strong> number of moves the white pieces need to capture the black queen.</em></p>

<p><strong>Note:</strong></p>

<ul>
	<li>The rook can capture the queen if they are in the same row or column and there is no piece between them.</li>
	<li>The bishop can capture the queen if they are in the same diagonal and there is no piece between them.</li>
	<li>The queen does not move.</li>
	<li>The white pieces can move independently.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/21/ex1.png" style="width: 600px; height: 600px;" />
<pre>
<strong>Input:</strong> a = 1, b = 1, c = 8, d = 8, e = 2, f = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can move the white rook from (1, 1) to (1, 3) in the first move. Then, we can move the white rook from (1, 3) to (2, 3) in the second move, capturing the black queen.
It can be shown that making the capture in less than 2 moves is impossible.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/21/ex1.png" style="width: 600px; height: 600px;" />
<pre>
<strong>Input:</strong> a = 5, b = 3, c = 3, d = 4, e = 5, f = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can move the white rook from (5, 3) to (5, 2) in one move, capturing the black queen.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a, b, c, d, e, f &lt;= 8</code></li>
	<li>No two pieces are on the same square.</li>
</ul>
"""

    input_format = "Six integers `a, b, c, d, e, f` provided as `[a, b, c, d, e, f]` in JSON."
    output_format = "An integer representing the minimum moves."

    constraints = [
        "1 <= a, b, c, d, e, f <= 8",
        "No two pieces are on same square"
    ]

    explanation = """To capture the queen:
1. The minimum moves is either 1 or 2. It's never 0 (no two pieces on same square) and always <= 2 (Rook can reach any square in 2 moves).
2. Check if Rook can reach Queen in 1 move:
   - Same row (`a == e`) or same column (`b == f`).
   - If same row, ensure Bishop `(c, d)` is not blocking the path.
   - If same column, ensure Bishop `(c, d)` is not blocking the path.
3. Check if Bishop can reach Queen in 1 move:
   - Same diagonal (`abs(c - e) == abs(d - f)`).
   - Ensure Rook `(a, b)` is not blocking the diagonal path.
4. If either can capture in 1 move, return 1.
5. Otherwise, return 2."""

    answer = """class Solution:
    def minMovesToCaptureQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # Rook (a,b), Bishop (c,d), Queen (e,f)
        
        # Rook can capture if same row or col and bishop NOT in between
        if a == e:
            if not (c == a and min(b, f) < d < max(b, f)):
                return 1
        if b == f:
            if not (d == b and min(a, e) < c < max(a, e)):
                return 1
        
        # Bishop can capture if same diagonal and rook NOT in between
        if abs(c - e) == abs(d - f):
            # Check if rook is on the same diagonal between bishop and queen
            if abs(c - a) == abs(d - b) and abs(a - e) == abs(b - f):
                # Is rook in between?
                if (min(c, e) < a < max(c, e)) and (min(d, f) < b < max(d, f)):
                    pass # Blocked
                else:
                    return 1
            else:
                return 1
        
        return 2"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minMovesToCaptureQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        vals = json.loads(raw)
        sol = Solution()
        print(sol.minMovesToCaptureQueen(*vals))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minMovesToCaptureQueen(int a, int b, int c, int d, int e, int f) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        Solution sol;
        cout << sol.minMovesToCaptureQueen(j[0], j[1], j[2], j[3], j[4], j[5]) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int minMovesToCaptureQueen(int a, int b, int c, int d, int e, int f) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            int[] data = mapper.readValue(sc.nextLine(), int[].class);
            System.out.println(new Solution().minMovesToCaptureQueen(data[0], data[1], data[2], data[3], data[4], data[5]));
        }
    }
}""",
        "javascript": """var minMovesToCaptureQueen = function(a, b, c, d, e, f) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [a, b, c, d, e, f] = JSON.parse(input);
    console.log(minMovesToCaptureQueen(a, b, c, d, e, f));
}""",
        "c": """#include <stdio.h>

int minMovesToCaptureQueen(int a, int b, int c, int d, int e, int f) {
    // User logic here
    return 0;
}

int main() {
    int a, b, c, d, e, f;
    int ch;
    while ((ch = getchar()) != EOF && ch != '[');
    if (scanf("%d", &a) == 1) {
        while ((ch = getchar()) != EOF && ch != ',');
        scanf("%d", &b);
        while ((ch = getchar()) != EOF && ch != ',');
        scanf("%d", &c);
        while ((ch = getchar()) != EOF && ch != ',');
        scanf("%d", &d);
        while ((ch = getchar()) != EOF && ch != ',');
        scanf("%d", &e);
        while ((ch = getchar()) != EOF && ch != ',');
        scanf("%d", &f);
        printf("%d\\n", minMovesToCaptureQueen(a, b, c, d, e, f));
    }
    return 0;
}"""
    }

    def solve(a, b, c, d, e, f):
        if a == e:
            if not (c == a and min(b, f) < d < max(b, f)): return 1
        if b == f:
            if not (d == b and min(a, e) < c < max(a, e)): return 1
        if abs(c - e) == abs(d - f):
            if abs(c - a) == abs(d - b) and abs(a - e) == abs(b - f) and min(c, e) < a < max(c, e) and min(d, f) < b < max(d, f):
                pass
            else: return 1
        return 2

    test_cases_data = [
        [1, 1, 8, 8, 2, 3], # Sample 1
        [5, 3, 3, 4, 5, 2], # Sample 2
        [1, 1, 2, 2, 8, 8], # Bishop blocked by rook actually no rook at 1,1 queen at 8,8 bishop at 2,2. Rook is NOT in between.
        [1, 1, 5, 5, 8, 8], # Bishop and Queen at 5,5 and 8,8. Diagonal.
        [4, 4, 1, 1, 8, 8], # Rook at 4,4 blocks Bishop at 1,1 from Queen at 8,8
        [4, 4, 4, 1, 4, 8], # Bishop at 4,1 blocks Rook at 4,4 from Queen at 4,8
        [1, 1, 3, 3, 1, 8], # Rook (1,1) can reach Queen (1,8)
        # Stress tests
        [1, 1, 8, 1, 1, 8],
        [8, 8, 1, 1, 1, 8],
        [1, 1, 3, 3, 5, 5]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(*t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Simulation"], "companyIndex": 0
    }

    output_path = f"2801-3000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
