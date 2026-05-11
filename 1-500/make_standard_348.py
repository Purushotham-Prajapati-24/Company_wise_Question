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
        "python": "import sys\nimport json\nimport re\n\nclass TicTacToe:\n    def __init__(self, n: int):\n        # User logic here\n        pass\n\n    def move(self, row: int, col: int, player: int) -> int:\n        # User logic here\n        return 0\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    # Lethal parsing: find all commands and all bracketed number groups\n    commands = re.findall(r'\"([^\"]*)\"', input_data)\n    val_groups = re.findall(r'\\[([^\\]]*)\\]', input_data)\n    \n    obj = None\n    res = []\n    for i in range(len(commands)):\n        cmd = commands[i]\n        nums = [int(x) for x in re.findall(r'-?\\d+', val_groups[i])]\n        \n        if cmd == \"TicTacToe\":\n            obj = TicTacToe(nums[0])\n            res.append(None)\n        elif cmd == \"move\":\n            res.append(obj.move(nums[0], nums[1], nums[2]))\n            \n    print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nclass TicTacToe {\npublic:\n    TicTacToe(int n) {\n        // User logic here\n    }\n    \n    int move(int row, int col, int player) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n\n    regex cmd_re(R\"(\"([^\"]*)\")\");\n    regex val_re(R\"(\\[([^\\]]*)\\])\");\n    \n    auto cmd_begin = sregex_iterator(input.begin(), input.end(), cmd_re);\n    auto val_begin = sregex_iterator(input.begin(), input.end(), val_re);\n    auto end = sregex_iterator();\n\n    TicTacToe* obj = nullptr;\n    cout << \"[\";\n    bool first = true;\n    \n    for (auto i = cmd_begin, j = val_begin; i != end && j != end; ++i, ++j) {\n        if (!first) cout << \",\";\n        first = false;\n        \n        string cmd = (*i)[1].str();\n        string val_str = (*j)[1].str();\n        vector<int> nums;\n        regex num_re(R\"(-?\\d+)\");\n        for (sregex_iterator k(val_str.begin(), val_str.end(), num_re), ke; k != ke; ++k) {\n            nums.push_back(stoi(k->str()));\n        }\n\n        if (cmd == \"TicTacToe\") {\n            obj = new TicTacToe(nums[0]);\n            cout << \"null\";\n        } else {\n            cout << obj->move(nums[0], nums[1], nums[2]);\n        }\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TicTacToe {\n    public TicTacToe(int n) {\n        // User logic here\n    }\n    \n    public int move(int row, int col, int player) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        String input = sc.hasNext() ? sc.next() : \"\";\n\n        List<String> commands = new ArrayList<>();\n        Matcher m1 = Pattern.compile(\"\\\"([^\\\"]*)\\\"\").matcher(input);\n        while (m1.find()) commands.add(m1.group(1));\n\n        List<String> valGroups = new ArrayList<>();\n        Matcher m2 = Pattern.compile(\"\\\\[([^\\\\]]*)\\\\]\").matcher(input);\n        while (m2.find()) valGroups.add(m2.group(1));\n\n        TicTacToe obj = null;\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < commands.size(); i++) {\n            if (i > 0) sb.append(\",\");\n            String cmd = commands.get(i);\n            List<Integer> nums = new ArrayList<>();\n            Matcher m3 = Pattern.compile(\"-?\\\\d+\").matcher(valGroups.get(i));\n            while (m3.find()) nums.add(Integer.parseInt(m3.group()));\n\n            if (cmd.equals(\"TicTacToe\")) {\n                obj = new TicTacToe(nums.get(0));\n                sb.append(\"null\");\n            } else {\n                sb.append(obj.move(nums.get(0), nums.get(1), nums.get(2)));\n            }\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "\"use strict\";\n\nconst fs = require('fs');\n\nclass TicTacToe {\n    /**\n     * @param {number} n\n     */\n    constructor(n) {\n        // User logic here\n    }\n\n    /**\n     * @param {number} row\n     * @param {number} col\n     * @param {number} player\n     * @return {number}\n     */\n    move(row, col, player) {\n        // User logic here\n    }\n}\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const commands = input.match(/\"([^\"]*)\"/g).map(s => s.slice(1, -1));\n    const args = input.match(/\\[([^\\]]*)\\]/g).map(s => JSON.parse(s));\n\n    let obj = null;\n    const res = commands.map((cmd, i) => {\n        if (cmd === \"TicTacToe\") {\n            obj = new TicTacToe(args[i][0]);\n            return null;\n        } else {\n            return obj.move(args[i][0], args[i][1], args[i][2]);\n        }\n    });\n    console.log(JSON.stringify(res).replace(/ /g, ''));\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\ntypedef struct {\n    // User logic here\n} TicTacToe;\n\nTicTacToe* ticTacToeCreate(int n) {\n    // User logic here\n    return NULL;\n}\n\nint ticTacToeMove(TicTacToe* obj, int row, int col, int player) {\n    // User logic here\n    return 0;\n}\n\nvoid ticTacToeFree(TicTacToe* obj) {\n    // User logic here\n}\n\nint main() {\n    static char buffer[1000000];\n    int len = fread(buffer, 1, 999999, stdin); buffer[len] = '\\0';\n\n    printf(\"[\");\n    int first = 1;\n    TicTacToe* obj = NULL;\n\n    char *cmd_ptr = buffer;\n    char *val_ptr = buffer;\n\n    while ((cmd_ptr = strchr(cmd_ptr, '\"')) != NULL) {\n        if (!first) printf(\",\");\n        first = 0;\n\n        cmd_ptr++;\n        char *cmd_end = strchr(cmd_ptr, '\"');\n        *cmd_end = '\\0';\n        char *cmd = cmd_ptr;\n        cmd_ptr = cmd_end + 1;\n\n        val_ptr = strchr(val_ptr, '[');\n        val_ptr++;\n        \n        if (strcmp(cmd, \"TicTacToe\") == 0) {\n            int n = atoi(val_ptr);\n            obj = ticTacToeCreate(n);\n            printf(\"null\");\n        } else {\n            int r = atoi(val_ptr);\n            val_ptr = strchr(val_ptr, ',') + 1;\n            int c = atoi(val_ptr);\n            val_ptr = strchr(val_ptr, ',') + 1;\n            int p = atoi(val_ptr);\n            printf(\"%d\", ticTacToeMove(obj, r, c, p));\n        }\n        val_ptr = strchr(val_ptr, ']');\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
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
