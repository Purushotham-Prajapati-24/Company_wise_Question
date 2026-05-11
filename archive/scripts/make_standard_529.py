import json
import os

def generate_json():
    problem_id = 529
    title = "Minesweeper"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>529. Minesweeper</h3>
<p>You are given an <code>m x n</code> char matrix <code>board</code> representing the game board where:</p>

<ul>
	<li><code>'M'</code> represents an <strong>unrevealed</strong> mine,</li>
	<li><code>'E'</code> represents an <strong>unrevealed</strong> empty square,</li>
	<li><code>'B'</code> represents a <strong>revealed</strong> blank square that has no adjacent mines,</li>
	<li><code>digit</code> (<code>'1'</code> to <code>'8'</code>) represents how many mines are adjacent to this square, and</li>
	<li><code>'X'</code> represents a <strong>revealed</strong> mine.</li>
</ul>

<p>You are also given an integer array <code>click</code> where <code>click = [click<sub>r</sub>, click<sub>c</sub>]</code> represents the next click position.</p>

<p>Return the board after revealing this position according to the rules (DFS/BFS reveal logic).</p>"""

    input_format = "Two lines: a JSON 2D array of chars `board`, and a JSON array of two integers `click`."
    output_format = "A JSON 2D array of chars representing the updated board."
    
    constraints = [
        "1 <= m, n <= 50",
        "board[i][j] is 'M', 'E', 'B', or '1'-'8'.",
        "click.length == 2"
    ]
    
    explanation = """Use DFS or BFS to reveal the board.
1. If board[r][c] == 'M', change to 'X' and stop.
2. If board[r][c] == 'E', count adjacent mines.
3. If mines > 0, set to digit.
4. If mines == 0, set to 'B' and recursively reveal neighbors."""
    
    answer = """class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        m, n = len(board), len(board[0])
        def get_mines(i, j):
            count = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0: continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                        count += 1
            return count

        def reveal(i, j):
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != 'E':
                return
            mines = get_mines(i, j)
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = 'B'
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0: continue
                        reveal(i + di, j + dj)
        
        reveal(r, c)
        return board"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        # User Logic Here
        return board

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        board = json.loads(raw[0])
        click = json.loads(raw[1])
        sol = Solution()
        print(json.dumps(sol.updateBoard(board, click)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        // User Logic Here
        return board;
    }
};

int main() {
    string b_str, c_str;
    if (getline(cin, b_str) && getline(cin, c_str)) {
        vector<vector<char>> board;
        vector<char> row;
        bool in_row = false;
        for (char c : b_str) {
            if (c == '[') in_row = true;
            else if (c == ']') {
                if (!row.empty()) board.push_back(row);
                row.clear();
            } else if (c == '\"' || c == '\\'') continue;
            else if (isalpha(c) || isdigit(c)) row.push_back(c);
        }
        
        vector<int> click;
        size_t p = 0;
        while ((p = c_str.find_first_of("0123456789", p)) != string::npos) {
            size_t next;
            click.push_back(stoi(c_str.substr(p), &next));
            p += next;
        }
        
        Solution sol;
        vector<vector<char>> res = sol.updateBoard(board, click);
        cout << "[";
        for (int i = 0; i < res.size(); i++) {
            if (i > 0) cout << ",";
            cout << "[";
            for (int j = 0; j < res[i].size(); j++) {
                if (j > 0) cout << ",";
                cout << "\\\"" << res[i][j] << "\\\"";
            }
            cout << "]";
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        // User Logic Here
        return board;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String bStr = sc.nextLine();
            String cStr = sc.hasNextLine() ? sc.nextLine() : "";
            // Parsing log...
            System.out.println("[]");
        }
    }
}""",
        "javascript": """/**
 * @param {character[][]} board
 * @param {number[]} click
 * @return {character[][]}
 */
var updateBoard = function(board, click) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const board = JSON.parse(input[0]);
    const click = JSON.parse(input[1]);
    console.log(JSON.stringify(updateBoard(board, click)).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void updateBoard(char** board, int boardSize, int* boardColSize, int* click, int clickSize) {
    // User Logic Here
}

int main() {
    char b[10000], c[100];
    if (fgets(b, sizeof(b), stdin) && fgets(c, sizeof(c), stdin)) {
        printf("[]\\n");
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]\\n[3,0]', "expected_output": '[["B","E","E","E","E"],["B","E","M","E","E"],["B","E","E","E","E"],["B","E","E","E","E"]]', "is_sample": True},
        {"input": '[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]\\n[1,2]', "expected_output": '[["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]', "is_sample": True},
        {"input": '[["M"]]\\n[0,0]', "expected_output": '[["X"]]', "is_sample": False},
        {"input": '[["E"]]\\n[0,0]', "expected_output": '[["B"]]', "is_sample": False},
        {"input": '[["E","M"],["E","E"]]\\n[1,0]', "expected_output": '[["E","M"],["B","B"]]', "is_sample": False},
        {"input": '[["E","E"],["E","E"]]\\n[0,0]', "expected_output": '[["B","B"],["B","B"]]', "is_sample": False},
        {"input": '[["E","E","E"],["E","M","E"],["E","E","E"]]\\n[0,0]', "expected_output": '[["1","E","E"],["E","M","E"],["E","E","E"]]', "is_sample": False},
        {"input": '[ ["E"] ]\\n[0, 0 ]', "expected_output": '[["B"]]', "is_sample": False},
        {"input": '[["E","E","E"]]\\n[0,1]', "expected_output": '[["B","B","B"]]', "is_sample": False},
        {"input": '[["M","M"],["M","M"]]\\n[0,0]', "expected_output": '[["X","M"],["M","M"]]', "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
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
        "topics": ["Depth-First Search", "Breadth-First Search", "Matrix"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
