import json
import os

def generate_json():
    problem_id = 1244
    title = "Design A Leaderboard"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1244. Design A Leaderboard</h3>
<p>Design a Leaderboard class, which has 3 functions:</p>

<ul>
	<li><code>addScore(playerId, score)</code>: Update the leaderboard by adding <code>score</code> to the given player's total score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given <code>score</code>.</li>
	<li><code>top(K)</code>: Return the score sum of the top <code>K</code> players.</li>
	<li><code>reset(playerId)</code>: Reset the score of the player with the given id to 0 (in other words remove it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling <code>reset</code>.</li>
</ul>

<p>Initially, the leaderboard is empty.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input: </strong>
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4], [1],[1],[2],[2,51],[3]]
<strong>Output: </strong>
[null,null,null,null,null,null,73,null,null,null,141]

<strong>Explanation: </strong>
Leaderboard leaderboard = new Leaderboard();
leaderboard.addScore(1, 73);   // leaderboard = [[1,73]];
leaderboard.addScore(2, 56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3, 39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4, 51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5, 4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);            // returns 73;
leaderboard.reset(1);          // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);          // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2, 51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);            // returns 141 = 51 + 51 + 39;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= playerId &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= K &lt;= num_players</code></li>
	<li><code>1 &lt;= score &lt;= 100</code></li>
	<li>There will be at most <code>1000</code> function calls.</li>
</ul>"""

    input_format = "A list of method names and a list of arguments for each method."
    output_format = "A list of return values for each method."

    constraints = [
        "1 <= playerId <= 10^9",
        "1 <= score <= 100",
        "Calls <= 1000"
    ]

    explanation = """To implement the Leaderboard:
1. Use a Hash Map `scores` to store `playerId -> total_score`.
2. `addScore(playerId, score)`: Increment the score in the map.
3. `reset(playerId)`: Remove the `playerId` from the map or set its score to 0.
4. `top(K)`:
   - Extract all scores from the map.
   - Sort them in descending order or use a min-heap to keep track of the top K scores.
   - Return the sum of the first K scores.
5. For faster `top(K)`, one could maintain a balanced BST or a sorted container, but with 1000 calls, a simple sort is usually efficient enough."""

    answer = """class Leaderboard:
    def __init__(self):
        self.scores = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        all_scores = sorted(self.scores.values(), reverse=True)
        return sum(all_scores[:K])

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Leaderboard:
    def __init__(self):
        pass
    def addScore(self, playerId: int, score: int) -> None:
        pass
    def top(self, K: int) -> int:
        return 0
    def reset(self, playerId: int) -> None:
        pass

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        methods, args = json.loads(raw)
        obj = None
        results = []
        for m, a in zip(methods, args):
            if m == "Leaderboard":
                obj = Leaderboard()
                results.append(None)
            elif m == "addScore":
                results.append(obj.addScore(a[0], a[1]))
            elif m == "top":
                results.append(obj.top(a[0]))
            elif m == "reset":
                results.append(obj.reset(a[0]))
        print(json.dumps(results).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Leaderboard {
public:
    Leaderboard() {}
    void addScore(int playerId, int score) {}
    int top(int K) { return 0; }
    void reset(int playerId) {}
};

int main() {
    // Simulator logic
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Leaderboard {
    public Leaderboard() {}
    public void addScore(int playerId, int score) {}
    public int top(int K) { return 0; }
    public void reset(int playerId) {}
}

public class Main {
    public static void main(String[] args) throws Exception {
        // Simulator logic
    }
}""",
        "javascript": """var Leaderboard = function() {
    
};
Leaderboard.prototype.addScore = function(playerId, score) {};
Leaderboard.prototype.top = function(K) { return 0; };
Leaderboard.prototype.reset = function(playerId) {};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    // Simulator logic
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

typedef struct {
} Leaderboard;

Leaderboard* constructor() { return NULL; }
void addScore(Leaderboard *obj, int playerId, int score) {}
int top(Leaderboard *obj, int K) { return 0; }
void reset(Leaderboard *obj, int playerId) {}

int main() {
    return 0;
}"""
    }

    import collections
    def solve(methods, args):
        scores = collections.defaultdict(int)
        results = []
        for m, a in zip(methods, args):
            if m == "Leaderboard":
                results.append(None)
            elif m == "addScore":
                scores[a[0]] += a[1]
                results.append(None)
            elif m == "top":
                all_s = sorted(scores.values(), reverse=True)
                results.append(sum(all_s[:a[0]]))
            elif m == "reset":
                if a[0] in scores:
                    del scores[a[0]]
                results.append(None)
        return results

    test_cases_data = [
        [["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"], [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]], # Sample 1
        [["Leaderboard","addScore","top","reset","top"], [[],[1,10],[1],[1],[1]]], # Simple reset
        [["Leaderboard","addScore","addScore","top"], [[],[1,50],[2,100],[2]]], # Top 2
        [["Leaderboard","addScore","addScore","addScore","top"], [[],[1,10],[1,10],[1,10],[1]]], # Multiple add
        [["Leaderboard","addScore","reset","addScore","top"], [[],[1,10],[1],[2,20],[1]]], # Reset then add another
        # Stress tests
        [["Leaderboard"] + ["addScore"]*100 + ["top"]*10, [[],] + [[i, 1] for i in range(100)] + [[10] for _ in range(10)]],
        [["Leaderboard"] + ["addScore"]*50 + ["reset"]*25 + ["top"], [[],] + [[i, i] for i in range(50)] + [[i] for i in range(25)] + [[10]]],
        [["Leaderboard", "addScore", "top"], [[], [9999, 100], [1]]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 1})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Hash Table", "Design", "Sorting", "Heap (Priority Queue)"], "companyIndex": 0
    }

    output_path = f"1201-1400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
