import json
import os

def generate_json():
    problem_id = 348
    title = "Design Tic-Tac-Toe"
    difficulty = "Medium"
    marks = 10

    html_description = """<h3>348. Design Tic-Tac-Toe</h3>
<p>Assume the following rules are for the tic-tac-toe game on an <code>n x n</code> board between two players:</p>
<ol>
\t<li>A move is guaranteed to be valid and is placed on an empty block.</li>
\t<li>Once a winning condition is reached, no more moves are allowed.</li>
\t<li>A player who succeeds in placing <code>n</code> of their marks in a horizontal, vertical, or diagonal row wins the game.</li>
</ol>
<p>Implement the <code>TicTacToe</code> class:</p>
<ul>
\t<li><code>TicTacToe(int n)</code> Initializes the object with the size of the board <code>n</code>.</li>
\t<li><code>int move(int row, int col, int player)</code> Indicates that the player with id <code>player</code> makes a move at the cell <code>(row, col)</code> of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return <code>0</code> if there is <strong>no winner</strong> after the move, or Player <code>1</code> or Player <code>2</code> if <strong>player</strong> has won after the move.</li>
</ul>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
<strong>Output</strong>
[null, 0, 0, 0, 0, 0, 0, 1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>2 &lt;= n &lt;= 100</code></li>
\t<li>player is <code>1</code> or <code>2</code>.</li>
\t<li><code>0 &lt;= row, col &lt; n</code></li>
\t<li><code>(row, col)</code> are <strong>unique</strong> for each different call to <code>move</code>.</li>
\t<li>At most <code>n<sup>2</sup></code> calls will be made to <code>move</code>.</li>
</ul>"""

    input_format = (
        "Line 1: board size `n`.\n"
        "Each subsequent line: `row col player` representing a move.\n"
        "Output the result of each move (0 = no winner, 1 or 2 = winner)."
    )
    output_format = "One integer per line: 0 (no winner yet), 1 (player 1 wins), or 2 (player 2 wins) after each move."

    constraints = [
        "2 <= n <= 100",
        "player is 1 or 2",
        "0 <= row, col < n",
        "(row, col) are unique per call",
        "At most n^2 calls to move"
    ]

    explanation = """Use row, column, and diagonal counters for O(1) per move.

### Algorithm:
- Maintain `rows[n]`, `cols[n]`, `diag`, `anti_diag` for each player (or use +1/-1 for p1/p2).
- On each `move(row, col, player)`:
  - Increment (player=1) or decrement (player=2) the counters.
  - If any counter reaches `n` or `-n`, that player wins.

### Complexity:
- **Time**: O(1) per move.
- **Space**: O(n) — for row/column vectors."""

    answer = """class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [[0]*n, [0]*n]
        self.cols = [[0]*n, [0]*n]
        self.diag = [0, 0]
        self.anti = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        n, p = self.n, player - 1
        self.rows[p][row] += 1
        self.cols[p][col] += 1
        if row == col:
            self.diag[p] += 1
        if row + col == n - 1:
            self.anti[p] += 1
        if (self.rows[p][row] == n or self.cols[p][col] == n or
                self.diag[p] == n or self.anti[p] == n):
            return player
        return 0"""

    boilerplate = {
        "python": (
            "import sys\n\n"
            "class TicTacToe:\n"
            "    def __init__(self, n):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def move(self, row, col, player):\n"
            "        # User logic here\n"
            "        return 0\n\n"
            "if __name__ == '__main__':\n"
            "    input_data = sys.stdin.read().splitlines()\n"
            "    if len(input_data) > 0:\n"
            "        n = int(input_data[0].strip())\n"
            "        obj = TicTacToe(n)\n"
            "        for line in input_data[1:]:\n"
            "            if line.strip():\n"
            "                parts = line.split()\n"
            "                if len(parts) >= 3:\n"
            "                    row, col, player = int(parts[0]), int(parts[1]), int(parts[2])\n"
            "                    print(obj.move(row, col, player))"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "using namespace std;\n\n"
            "class TicTacToe {\n"
            "public:\n"
            "    TicTacToe(int n) {\n"
            "        // User logic here\n"
            "    }\n"
            "    int move(int row, int col, int player) {\n"
            "        // User logic here\n"
            "        return 0;\n"
            "    }\n"
            "};\n\n"
            "int main() {\n"
            "    int n;\n"
            "    if (cin >> n) {\n"
            "        TicTacToe obj(n);\n"
            "        int row, col, player;\n"
            "        while (cin >> row >> col >> player) {\n"
            "            cout << obj.move(row, col, player) << endl;\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "java": (
            "import java.util.*;\n\n"
            "class TicTacToe {\n"
            "    public TicTacToe(int n) {\n"
            "        // User logic here\n"
            "    }\n"
            "    public int move(int row, int col, int player) {\n"
            "        // User logic here\n"
            "        return 0;\n"
            "    }\n"
            "}\n\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextInt()) {\n"
            "            int n = sc.nextInt();\n"
            "            TicTacToe obj = new TicTacToe(n);\n"
            "            while (sc.hasNextInt()) {\n"
            "                int row = sc.nextInt();\n"
            "                int col = sc.nextInt();\n"
            "                int player = sc.nextInt();\n"
            "                System.out.println(obj.move(row, col, player));\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "class TicTacToe {\n"
            "    constructor(n) {\n"
            "        // User logic here\n"
            "    }\n"
            "    move(row, col, player) {\n"
            "        // User logic here\n"
            "        return 0;\n"
            "    }\n"
            "}\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').split(/\\s+/);\n"
            "    if (input.length > 0 && input[0] !== '') {\n"
            "        let idx = 0;\n"
            "        const n = parseInt(input[idx++]);\n"
            "        const obj = new TicTacToe(n);\n"
            "        while (idx + 2 < input.length) {\n"
            "            if (input[idx] === '') { idx++; continue; }\n"
            "            const row = parseInt(input[idx++]);\n"
            "            const col = parseInt(input[idx++]);\n"
            "            const player = parseInt(input[idx++]);\n"
            "            if (!isNaN(row)) {\n"
            "                process.stdout.write(obj.move(row, col, player) + '\\n');\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
            "main();"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n\n"
            "typedef struct {\n"
            "    // User definition here\n"
            "} TicTacToe;\n\n"
            "TicTacToe* ticTacToeCreate(int n) {\n"
            "    // User logic here\n"
            "    return NULL;\n"
            "}\n\n"
            "int ticTacToeMove(TicTacToe* obj, int row, int col, int player) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "}\n\n"
            "int main() {\n"
            "    int n;\n"
            "    if (scanf(\"%d\", &n) == 1) {\n"
            "        TicTacToe* obj = ticTacToeCreate(n);\n"
            "        int row, col, player;\n"
            "        while (scanf(\"%d %d %d\", &row, &col, &player) == 3) {\n"
            "            printf(\"%d\\n\", ticTacToeMove(obj, row, col, player));\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
    }

    test_cases = [
        # 2 sample cases (from LeetCode example)
        {
            "input": "3\n0 0 1\n0 2 2\n2 2 1\n1 1 2\n2 0 1\n1 0 2\n2 1 1",
            "expected_output": "0\n0\n0\n0\n0\n0\n1",
            "is_sample": True
        },
        {
            "input": "2\n0 0 1\n1 1 2\n0 1 1",
            "expected_output": "0\n0\n1",
            "is_sample": True
        },
        # 5 diverse cases
        {
            "input": "3\n0 0 1\n1 1 1\n2 2 1",
            "expected_output": "0\n0\n1",
            "is_sample": False
        },
        {
            "input": "3\n0 0 2\n0 1 2\n0 2 2",
            "expected_output": "0\n0\n2",
            "is_sample": False
        },
        {
            "input": "3\n2 0 1\n1 1 1\n0 2 1",
            "expected_output": "0\n0\n1",
            "is_sample": False
        },
        {
            "input": "4\n0 0 1\n1 1 1\n2 2 1\n3 3 1",
            "expected_output": "0\n0\n0\n1",
            "is_sample": False
        },
        {
            "input": "2\n0 0 1\n0 1 2\n1 0 2\n1 1 1",
            "expected_output": "0\n0\n0\n0",
            "is_sample": False
        },
        # 3 stress cases (100x100 board, filling a row/col/diag)
        {
            "input": "100\n" + "\n".join(f"0 {c} 1" for c in range(100)),
            "expected_output": "\n".join(["0"] * 99 + ["1"]),
            "is_sample": False
        },
        {
            "input": "100\n" + "\n".join(f"{r} 0 2" for r in range(100)),
            "expected_output": "\n".join(["0"] * 99 + ["2"]),
            "is_sample": False
        },
        {
            "input": "100\n" + "\n".join(f"{i} {i} 1" for i in range(100)),
            "expected_output": "\n".join(["0"] * 99 + ["1"]),
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
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Hash Table", "Design", "Matrix"],
        "companyIndex": 1
    }

    output_path = "301-500/348_Design_Tic_Tac_Toe.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
