import json
import os

def generate_json():
    problem_id = 79
    title = "Word Search"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>79. Word Search</h3>
<p>Given an <code>m x n</code> grid of characters <code>board</code> and a string <code>word</code>, return <code>true</code> if <code>word</code> exists in the grid.</p>

<p>The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n = board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 6</code></li>
	<li><code>1 &lt;= word.length &lt;= 15</code></li>
	<li><code>board</code> and <code>word</code> consist of only lowercase and uppercase English letters.</li>
</ul>"""

    input_format = "Line 1: m n (rows and columns). Next m lines: n space-separated characters. Last line: the word to search."
    output_format = "A boolean string 'True' or 'False'."
    
    constraints = [
        "1 <= m, n <= 6",
        "1 <= word.length <= 15",
        "All characters are English letters."
    ]
    
    explanation = """To check if a word exists in a character grid:
1. **Backtracking (DFS)**:
   - Iterate through every cell in the grid.
   - If the first character of the word matches the cell, start a DFS from that cell.
   - In the recursive `dfs(r, c, index)` function:
     - Base Case: If `index == len(word)`, return `True` (all characters matched).
     - Boundary/Match Check: If `r, c` are out of bounds or `board[r][c] != word[index]`, return `False`.
     - Marking: Temporarily mark the current cell as visited (e.g., using a non-letter character like `#`) to avoid reusing it in the same word path.
     - Recursion: Check all 4 adjacent neighbors (up, down, left, right) for the next character: `dfs(r+1, c, index+1) or ...`.
     - Backtrack: Restore the original character in the cell so it can be used in other potential paths.
2. **Complexity**:
   - Time Complexity: O(M * N * 3^L), where M*N is the grid size and L is the word length. Each step has 3 directions to explore (excluding the one we came from).
   - Space Complexity: O(L) for the recursion stack."""
    
    answer = """def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False
        
        temp = board[r][c]
        board[r][c] = '#'  # Mark as visited
        
        # Explore neighbors
        res = (backtrack(r + 1, c, i + 1) or 
               backtrack(r - 1, c, i + 1) or 
               backtrack(r, c + 1, i + 1) or 
               backtrack(r, c - 1, i + 1))
        
        board[r][c] = temp  # Backtrack
        return res

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False"""

    boilerplate = {
        "python": "import sys, re\n\ndef exist(board, word):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    nums = [int(x) for x in re.findall(r'\\d+', data)]\n    all_strs = re.findall(r'[A-Za-z]+', data)\n    if len(nums) >= 2:\n        m, n = nums[0], nums[1]\n        board = []\n        idx = 0\n        for i in range(m):\n            board.append(list(all_strs[idx : idx + n]))\n            idx += n\n        word = all_strs[idx]\n        print(exist(board, word))\n    else:\n        # Fallback for LeetCode style board=[[\"A\"]], word=\"A\"\n        word = all_strs[-1]\n        board_strs = all_strs[:-1]\n        # Assuming square board if dimensions are missing, or logic to split\n        # But usually m, n are provided in this dataset's test cases\n        print(exist(board_strs, word))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    bool exist(vector<vector<char>>& board, string word) {\n        // User Logic Here\n        return false;\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex d_rgx(\"\\\\d+\");\n    auto d_begin = sregex_iterator(input.begin(), input.end(), d_rgx);\n    auto d_end = sregex_iterator();\n    vector<int> nums;\n    for (auto i = d_begin; i != d_end; ++i) nums.push_back(stoi(i->str()));\n    \n    regex s_rgx(\"[A-Za-z]+\");\n    auto s_begin = sregex_iterator(input.begin(), input.end(), s_rgx);\n    auto s_end = sregex_iterator();\n    vector<string> all_strs;\n    for (auto i = s_begin; i != s_end; ++i) all_strs.push_back(i->str());\n\n    if(nums.size() >= 2) {\n        int m = nums[0], n = nums[1];\n        vector<vector<char>> board(m, vector<char>(n));\n        int idx = 0;\n        for(int i=0; i<m; i++) for(int j=0; j<n; j++) board[i][j] = all_strs[idx++][0];\n        Solution sol;\n        cout << (sol.exist(board, all_strs[idx]) ? \"True\" : \"False\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public boolean exist(char[][] board, String word) {\n        // User Logic Here\n        return false;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        List<Integer> nums = new ArrayList<>();\n        Matcher nm = Pattern.compile(\"\\\\d+\").matcher(input);\n        while (nm.find()) nums.add(Integer.parseInt(nm.group()));\n        \n        List<String> all_strs = new ArrayList<>();\n        Matcher sm = Pattern.compile(\"[A-Za-z]+\").matcher(input);\n        while (sm.find()) all_strs.add(sm.group());\n\n        if (nums.size() >= 2) {\n            int m = nums.get(0), n = nums.get(1);\n            char[][] board = new char[m][n];\n            int idx = 0;\n            for(int i=0; i<m; i++) for(int j=0; j<n; j++) board[i][j] = all_strs.get(idx++).charAt(0);\n            System.out.println(new Solution().exist(board, all_strs.get(idx)) ? \"True\" : \"False\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {character[][]} board\n * @param {string} word\n * @return {boolean}\n */\nvar exist = function(board, word) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    const nums = (input.match(/\\d+/g) || []).map(Number);\n    const all_strs = input.match(/[A-Za-z]+/g) || [];\n    if (nums.length >= 2) {\n        const m = nums[0], n = nums[1];\n        const board = [];\n        let idx = 0;\n        for(let i=0; i<m; i++) {\n            board.push(all_strs.slice(idx, idx + n).map(s => s[0]));\n            idx += n;\n        }\n        console.log(exist(board, all_strs[idx]) ? \"True\" : \"False\");\n    }\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n\nbool exist(char** board, int boardSize, int* boardColSize, char* word) {\n    // User Logic Here\n    return false;\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) == 2) {\n        char** board = malloc(m * sizeof(char*));\n        int* colSizes = malloc(m * sizeof(int));\n        char cell[10];\n        for (int i = 0; i < m; i++) {\n            board[i] = malloc(n * sizeof(char));\n            colSizes[i] = n;\n            for (int j = 0; j < n; j++) {\n                scanf(\"%s\", cell);\n                board[i][j] = cell[0];\n            }\n        }\n        char word[100];\n        scanf(\"%s\", word);\n        printf(\"%s\\n\", exist(board, m, colSizes, word) ? \"True\" : \"False\");\n    }\n    return 0;\n}"
    }

    def _solve(board, word):
        rows, cols = len(board), len(board[0])
        def backtrack(r, c, i):
            if i == len(word): return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]: return False
            temp = board[r][c]
            board[r][c] = '#'
            res = (backtrack(r+1, c, i+1) or backtrack(r-1, c, i+1) or 
                   backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1))
            board[r][c] = temp
            return res
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0): return True
        return False

    def format_input(board, word):
        m = len(board)
        n = len(board[0])
        lines = [f"{m} {n}"]
        for row in board:
            lines.append(" ".join(row))
        lines.append(word)
        return "\n".join(lines)

    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    test_cases = [
        {"input": format_input(board1, "ABCCED"), "expected_output": str(_solve([r[:] for r in board1], "ABCCED")), "is_sample": True},
        {"input": format_input(board1, "SEE"), "expected_output": str(_solve([r[:] for r in board1], "SEE")), "is_sample": True},
        {"input": format_input(board1, "ABCB"), "expected_output": str(_solve([r[:] for r in board1], "ABCB")), "is_sample": False},
        {"input": format_input([["A"]], "A"), "expected_output": str(_solve([["A"]], "A")), "is_sample": False},
        {"input": format_input([["A"]], "B"), "expected_output": str(_solve([["A"]], "B")), "is_sample": False},
        {"input": format_input([["A","B"],["C","D"]], "ACDB"), "expected_output": str(_solve([["A","B"],["C","D"]], "ACDB")), "is_sample": False},
        {"input": format_input([["A","B"],["C","D"]], "ABCD"), "expected_output": str(_solve([["A","B"],["C","D"]], "ABCD")), "is_sample": False},
        # Stress cases
        {"input": format_input([["A"]*6 for _ in range(6)], "A"*15), "expected_output": str(_solve([["A"]*6 for _ in range(6)], "A"*15)), "is_sample": False},
        {"input": format_input([["A"]*6 for _ in range(6)], "A"*14 + "B"), "expected_output": str(_solve([["A"]*6 for _ in range(6)], "A"*14 + "B")), "is_sample": False},
        {"input": format_input([["A","B"]*3 for _ in range(6)], "ABABABABABABABA"), "expected_output": str(_solve([["A","B"]*3 for _ in range(6)], "ABABABABABABABA")), "is_sample": False}
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
        "topics": ["Array", "Backtracking", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/79_Word_Search.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
