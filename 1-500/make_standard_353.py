import json
import os

def generate_json():
    problem_id = 353
    title = "Design Snake Game"
    difficulty = "Medium"
    marks = 10

    html_description = """<h3>353. Design Snake Game</h3>
<p>Design a <a href="https://en.wikipedia.org/wiki/Snake_(video_game)" target="_blank">Snake game</a> that is played on a device with screen size <code>height x width</code>. Play the snake game with given <code>food</code>'s positions.</p>
<p>The snake starts at position <code>(0, 0)</code> with a length of <code>1</code> unit.</p>
<p>You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.</p>
<p>Each food appears one by one on the screen, i.e., the second food will not appear until the first food is eaten by the snake.</p>
<p>When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.</p>
<p>Return the score of the game after applying the given sequence of moves. Return <code>-1</code> if the snake goes out of boundary or bites itself.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> width = 3, height = 2, food = [[1,2],[0,1]], moves = ["R","D","R","U","L","U"]
<strong>Output:</strong> [0,0,1,1,2,-1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>1 &lt;= width, height &lt;= 10<sup>4</sup></code></li>
\t<li><code>1 &lt;= food.length &lt;= 50</code></li>
\t<li><code>food[i].length == 2</code></li>
\t<li><code>0 &lt;= food[i][0] &lt; height</code></li>
\t<li><code>0 &lt;= food[i][1] &lt; width</code></li>
\t<li><code>moves</code> only contains <code>'U'</code>, <code>'D'</code>, <code>'L'</code>, <code>'R'</code>.</li>
</ul>"""

    input_format = (
        "Line 1: `width height` (space-separated).\n"
        "Line 2: food positions as `r1 c1 r2 c2 ...` (space-separated pairs).\n"
        "Line 3: moves as a single string like `R D U L`."
    )
    output_format = "Space-separated scores after each move (0 = alive, -1 = dead)."

    constraints = [
        "1 <= width, height <= 10^4",
        "1 <= food.length <= 50",
        "moves contains only U, D, L, R"
    ]

    explanation = """Simulate the snake using a deque.

### Algorithm:
- Maintain snake body as a `deque` of `(row, col)` positions.
- Maintain a `set` of occupied positions for O(1) self-collision check.
- On each move:
  1. Compute new head position based on direction.
  2. If out of bounds: return -1.
  3. If new head == next food: score++, advance food pointer (don't remove tail).
  4. Else: remove tail from deque and set.
  5. If new head is in body set: return -1 (self-collision).
  6. Add new head to deque and set.

### Complexity: O(1) per move."""

    answer = """from collections import deque

class SnakeGame:
    def __init__(self, width, height, food):
        self.w, self.h = width, height
        self.food = food
        self.fi = 0
        self.snake = deque([(0, 0)])
        self.body = {(0, 0)}
        self.score = 0

    def move(self, direction):
        dr = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
        r, c = self.snake[0]
        dr_, dc_ = dr[direction]
        nr, nc = r + dr_, c + dc_
        if not (0 <= nr < self.h and 0 <= nc < self.w):
            return -1
        # Remove tail first to allow head to move into where tail was
        tail = self.snake[-1]
        self.body.discard(tail)
        if (nr, nc) in self.body:
            return -1
        if self.fi < len(self.food) and [nr, nc] == self.food[self.fi]:
            self.score += 1
            self.fi += 1
            self.body.add(tail)  # re-add tail (snake grows)
        else:
            self.snake.pop()
        self.snake.appendleft((nr, nc))
        self.body.add((nr, nc))
        return self.score"""

    boilerplate = {
        "python": "import sys\nimport re\nfrom collections import deque\n\nclass SnakeGame:\n    def __init__(self, width, height, food):\n        # User logic here\n        pass\n\n    def move(self, direction):\n        # User logic here\n        return 0\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 3:\n        dims = [int(x) for x in re.findall(r'-?\\d+', input_data[0])]\n        w, h = dims[0], dims[1]\n        f_data = [int(x) for x in re.findall(r'-?\\d+', input_data[1])]\n        food = [f_data[i:i+2] for i in range(0, len(f_data), 2)]\n        moves = re.findall(r'\"(.*?)\"', input_data[2])\n        game = SnakeGame(w, h, food)\n        print(' '.join(map(str, [game.move(m) for m in moves])))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <deque>\n#include <set>\n#include <regex>\nusing namespace std;\n\nclass SnakeGame {\npublic:\n    SnakeGame(int width, int height, vector<vector<int>>& food) {\n        // User logic here\n    }\n    int move(string direction) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line1, line2, line3;\n    if (getline(cin, line1) && getline(cin, line2) && getline(cin, line3)) {\n        regex r(\"-?\\\\d+\");\n        auto b1 = sregex_iterator(line1.begin(), line1.end(), r), e1 = sregex_iterator();\n        int w = stoi((*b1++).str()), h = stoi((*b1).str());\n        vector<vector<int>> food;\n        auto b2 = sregex_iterator(line2.begin(), line2.end(), r);\n        while (b2 != e1) {\n            int r_val = stoi((*b2++).str());\n            int c_val = stoi((*b2++).str());\n            food.push_back({r_val, c_val});\n        }\n        regex rm(\"\\\"(.*?)\\\"\");\n        auto bm = sregex_iterator(line3.begin(), line3.end(), rm);\n        vector<string> moves;\n        while (bm != e1) { moves.push_back((*bm++).str(1)); }\n        SnakeGame game(w, h, food);\n        for (int i = 0; i < moves.size(); ++i) cout << game.move(moves[i]) << (i == moves.size() - 1 ? \"\" : \" \");\n        cout << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    static class SnakeGame {\n        public SnakeGame(int width, int height, int[][] food) {\n            // User logic here\n        }\n        public int move(String direction) {\n            // User logic here\n            return 0;\n        }\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String l1 = sc.nextLine(), l2 = sc.nextLine(), l3 = sc.nextLine();\n            Matcher m1 = Pattern.compile(\"-?\\\\d+\").matcher(l1);\n            m1.find(); int w = Integer.parseInt(m1.group()); m1.find(); int h = Integer.parseInt(m1.group());\n            Matcher m2 = Pattern.compile(\"-?\\\\d+\").matcher(l2);\n            List<int[]> foodList = new ArrayList<>();\n            while (m2.find()) {\n                int r = Integer.parseInt(m2.group()); m2.find(); int c = Integer.parseInt(m2.group());\n                foodList.add(new int[]{r, c});\n            }\n            Matcher m3 = Pattern.compile(\"\\\\\\\"(.*?)\\\\\\\"\").matcher(l3);\n            SnakeGame game = new SnakeGame(w, h, foodList.toArray(new int[0][0]));\n            List<String> res = new ArrayList<>();\n            while (m3.find()) res.add(String.valueOf(game.move(m3.group(1))));\n            System.out.println(String.join(\" \", res));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nclass SnakeGame {\n    constructor(width, height, food) {\n        // User logic here\n    }\n    move(direction) {\n        // User logic here\n        return 0;\n    }\n}\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').split('\\n');\n    if (input.length >= 3) {\n        const [w, h] = input[0].match(/-?\\d+/g).map(Number);\n        const f_data = (input[1].match(/-?\\d+/g) || []).map(Number);\n        const food = [];\n        for (let i = 0; i < f_data.length; i += 2) food.push([f_data[i], f_data[i+1]]);\n        const moves = input[2].match(/\\\"(.*?)\\\"/g).map(s => s.slice(1, -1));\n        const game = new SnakeGame(w, h, food);\n        console.log(moves.map(m => game.move(m)).join(' '));\n    }\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint snakeMove(int width, int height, int** food, int foodSize, char* direction, int* snakeR, int* snakeC, int* snakeLen, int* foodIdx, int* score) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char l1[1000], l2[10000], l3[10000];\n    if (fgets(l1, 1000, stdin) && fgets(l2, 10000, stdin) && fgets(l3, 10000, stdin)) {\n        int w, h; sscanf(l1, \"%d %d\", &w, &h);\n        int** foodGrid = malloc(1000 * sizeof(int*)); int fc = 0; char* p = l2;\n        while (*p) {\n            if (isdigit(*p) || *p == '-') {\n                int r = strtol(p, &p, 10);\n                while (*p && !isdigit(*p) && *p != '-') p++;\n                int c = strtol(p, &p, 10);\n                foodGrid[fc] = malloc(2 * sizeof(int));\n                foodGrid[fc][0] = r; foodGrid[fc][1] = c; fc++;\n            } else p++;\n        }\n        char moves[1000][10]; int mc = 0; p = l3;\n        while (*p) {\n            if (*p == '\"') {\n                p++; int i = 0;\n                while (*p && *p != '\"') moves[mc][i++] = *p++;\n                moves[mc][i] = '\\0'; mc++; if (*p) p++;\n            } else p++;\n        }\n        int sR[1000], sC[1000], sL = 1, fI = 0, sc = 0;\n        for (int i = 0; i < mc; i++) printf(\"%d%s\", snakeMove(w, h, foodGrid, fc, moves[i], sR, sC, &sL, &fI, &sc), (i == mc - 1 ? \"\" : \" \"));\n        printf(\"\\n\");\n    }\n    return 0;\n}"
    }


    # Precompute expected outputs
    from collections import deque

    def simulate_snake(w, h, food, moves):
        food_idx = 0
        snake = deque([(0, 0)])
        body = {(0, 0)}
        score = 0
        results = []
        dr_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        for m in moves:
            r, c = snake[0]
            dr, dc = dr_map[m]
            nr, nc = r + dr, c + dc
            if not (0 <= nr < h and 0 <= nc < w):
                results.append(-1)
                break
            tail = snake[-1]
            body.discard(tail)
            if (nr, nc) in body:
                results.append(-1)
                break
            if food_idx < len(food) and [nr, nc] == food[food_idx]:
                score += 1
                food_idx += 1
                body.add(tail)
            else:
                snake.pop()
            snake.appendleft((nr, nc))
            body.add((nr, nc))
            results.append(score)
        return results

    res1 = simulate_snake(3, 2, [[1, 2], [0, 1]], ["R", "D", "R", "U", "L", "U"])
    res2 = simulate_snake(2, 2, [[1, 1]], ["R", "D", "L", "U"])
    res3 = simulate_snake(3, 3, [[2, 0]], ["D", "D"])
    res4 = simulate_snake(2, 2, [], ["R", "D", "L", "U", "R"])
    res5 = simulate_snake(5, 5, [[0, 1], [0, 2], [0, 3], [0, 4]], ["R", "R", "R", "R"])
    stress1_food = [[i, 0] for i in range(1, 50)]
    stress1_moves = ["D"] * 49
    res_s1 = simulate_snake(1, 50, stress1_food, stress1_moves)
    stress2_moves = ["R"] * 9999 + ["U"]
    res_s2 = simulate_snake(10000, 1, [], stress2_moves)
    stress3_food = [[0, i] for i in range(1, 50)]
    stress3_moves = ["R"] * 49 + ["D"]
    res_s3 = simulate_snake(50, 2, stress3_food, stress3_moves)

    def fmt_food(food):
        return " ".join(f"{r} {c}" for r, c in food)

    test_cases = [
        {
            "input": "3 2\n[[1,2],[0,1]]\n[\"R\",\"D\",\"R\",\"U\",\"L\",\"U\"]",
            "expected_output": " ".join(map(str, res1)),
            "is_sample": True
        },
        {
            "input": "2 2\n[[1,1]]\n[\"R\",\"D\",\"L\",\"U\"]",
            "expected_output": " ".join(map(str, res2)),
            "is_sample": True
        },
        {
            "input": "3 3\n[[2,0]]\n[\"D\",\"D\"]",
            "expected_output": " ".join(map(str, res3)),
            "is_sample": False
        },
        {
            "input": "2 2\n[]\n[\"R\",\"D\",\"L\",\"U\",\"R\"]",
            "expected_output": " ".join(map(str, res4)),
            "is_sample": False
        },
        {
            "input": "5 5\n[[0,1],[0,2],[0,3],[0,4]]\n[\"R\",\"R\",\"R\",\"R\"]",
            "expected_output": " ".join(map(str, res5)),
            "is_sample": False
        },
        {
            "input": "1 1\n[]\n[\"R\"]",
            "expected_output": "-1",
            "is_sample": False
        },
        {
            "input": "4 4\n[[1,1],[2,2]]\n[\"D\",\"R\",\"D\",\"R\"]",
            "expected_output": " ".join(map(str, simulate_snake(4, 4, [[1, 1], [2, 2]], ["D", "R", "D", "R"]))),
            "is_sample": False
        },
        {
            "input": "1 50\n" + json.dumps(stress1_food) + "\n" + json.dumps(stress1_moves).replace(" ", ""),
            "expected_output": " ".join(map(str, res_s1)),
            "is_sample": False
        },
        {
            "input": "10000 1\n[]\n" + json.dumps(stress2_moves).replace(" ", ""),
            "expected_output": " ".join(map(str, res_s2)),
            "is_sample": False
        },
        {
            "input": "50 2\n" + json.dumps(stress3_food) + "\n" + json.dumps(stress3_moves).replace(" ", ""),
            "expected_output": " ".join(map(str, res_s3)),
            "is_sample": False
        },
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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Hash Table", "Design", "Queue", "Simulation"],
        "companyIndex": 1
    }

    output_path = "301-500/353_Design_Snake_Game.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
