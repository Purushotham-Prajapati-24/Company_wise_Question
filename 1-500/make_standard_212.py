import json
import os

def generate_json():
    problem_id = 212
    title = "Word Search II"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>212. Word Search II</h3>
<p>Given an <code>m x n</code> <code>board</code> of characters and a list of strings <code>words</code>, return <em>all words on the board</em>.</p>

<p>Each word must be constructed from letters of sequentially adjacent cells, where <strong>adjacent cells</strong> are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search1.jpg" style="width: 322px; height: 322px;" />
<pre>
<strong>Input:</strong> board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
<strong>Output:</strong> ["eat","oath"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search2.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>Input:</strong> board = [["a","b"],["c","d"]], words = ["abcb"]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 12</code></li>
	<li><code>board[i][j]</code> is a lowercase English letter.</li>
	<li><code>1 &lt;= words.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
	<li>All the strings of <code>words</code> are unique.</li>
</ul>"""

    input_format = "Line 1: m and n. Next m lines: row characters (space-separated or joined). Final line: space-separated words."
    output_format = "Space-separated found words."
    
    constraints = [
        "Board size: [1, 12] x [1, 12]",
        "Words: up to 30,000",
        "Word length: up to 10",
        "O(M*N * 4 * 3^(L-1)) time complexity expected, where L is word length.",
        "Must use Trie for efficiency."
    ]
    
    explanation = """To find all words from a list on a 2D board:
1. **Represent Words in a Trie**:
   - Insert all words from the `words` list into a Trie.
   - For each node in the Trie, store the corresponding word (if it ends there) to avoid re-constructing it.
2. **Backtracking on the Board**:
   - Iterate through each cell `(r, c)` on the board.
   - Start a DFS/backtracking search from `(r, c)` if `board[r][c]` is a child of the Trie root.
3. **DFS Steps**:
   - Mark the current cell as visited (e.g., replace with '#').
   - Explore neighbors (Up, Down, Left, Right).
   - If a neighbor's character exists in the Trie node's children, continue recursing.
   - If a word is found (node has a `word` property), add it to the results and **nullify/remove** the word from the Trie to avoid duplicates.
   - **Optimization**: After visiting a node, if it becomes a leaf (no more children), remove it from the Trie to prune unnecessary searches.
4. **Complexity**:
   - Time Complexity: O(M * N * 3^L) where M, N are board dimensions and L is max word length.
   - Space Complexity: O(Total characters in words) for the Trie."""
    
    answer = """class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class WordSearchSolver:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Step 1: Build Trie
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w
            
        rows, cols = len(board), len(board[0])
        res = []
        
        def backtrack(r, c, node):
            char = board[r][c]
            curr_node = node.children[char]
            
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None # Avoid duplicates
            
            # Optimization: Pruning leaf nodes
            # We don't remove nodes immediately to keep it simple, 
            # but usually we'd mark the node to prune.
            
            board[r][c] = "#"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    backtrack(nr, nc, curr_node)
            board[r][c] = char
            
            # Pruning strategy
            if not curr_node.children:
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    backtrack(r, c, root)
                    
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef findWords(board, words):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_text = sys.stdin.read()\n    nums = re.findall(r'\\d+', input_text)\n    if len(nums) >= 2:\n        m, n = int(nums[0]), int(nums[1])\n        strings = re.findall(r'[a-zA-Z]+', input_text)\n        board_chars = []\n        words = []\n        for s in strings:\n            if len(board_chars) < m * n:\n                for char in s:\n                    if len(board_chars) < m * n: board_chars.append(char)\n            else:\n                words.append(s)\n        board = [board_chars[i:i+n] for i in range(0, len(board_chars), n)]\n        print(json.dumps(sorted(findWords(board, words))))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n#include <regex>\n\nusing namespace std;\n\nvector<string> findWords(vector<vector<char>>& board, vector<string>& words) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string input((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());\n    regex num_re(\"\\\\d+\");\n    auto num_begin = sregex_iterator(input.begin(), input.end(), num_re);\n    auto num_end = sregex_iterator();\n    if (num_begin != num_end) {\n        int m = stoi(num_begin->str());\n        num_begin++;\n        if (num_begin != num_end) {\n            int n = stoi(num_begin->str());\n            regex word_re(\"[a-zA-Z]+\");\n            auto word_begin = sregex_iterator(input.begin(), input.end(), word_re);\n            vector<char> board_chars;\n            vector<string> words;\n            for (sregex_iterator i = word_begin; i != num_end; ++i) {\n                string s = i->str();\n                if (board_chars.size() < (size_t)m * n) {\n                    for (char c : s) if (board_chars.size() < (size_t)m * n) board_chars.push_back(c);\n                } else {\n                    words.push_back(s);\n                }\n            }\n            vector<vector<char>> board(m, vector<char>(n));\n            for (int i = 0; i < m; i++) {\n                for (int j = 0; j < n; j++) board[i][j] = board_chars[i * n + j];\n            }\n            vector<string> res = findWords(board, words);\n            sort(res.begin(), res.end());\n            cout << \"[\";\n            for (size_t i = 0; i < res.size(); i++) {\n                cout << \"\\\"\" << res[i] << \"\\\"\" << (i == res.size() - 1 ? \"\" : \", \");\n            }\n            cout << \"]\" << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public List<String> findWords(char[][] board, String[] words) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        StringBuilder sb = new StringBuilder();\n        String line;\n        while ((line = br.readLine()) != null) sb.append(line).append(\" \");\n        String input = sb.toString();\n        \n        Matcher m_num = Pattern.compile(\"\\\\d+\").matcher(input);\n        if (m_num.find()) {\n            int m = Integer.parseInt(m_num.group());\n            if (m_num.find()) {\n                int n = Integer.parseInt(m_num.group());\n                Matcher m_word = Pattern.compile(\"[a-zA-Z]+\").matcher(input);\n                List<Character> boardChars = new ArrayList<>();\n                List<String> words = new ArrayList<>();\n                while (m_word.find()) {\n                    String s = m_word.group();\n                    if (boardChars.size() < m * n) {\n                        for (char c : s.toCharArray()) if (boardChars.size() < m * n) boardChars.add(c);\n                    } else {\n                        words.add(s);\n                    }\n                }\n                char[][] board = new char[m][n];\n                for (int i = 0; i < m; i++) {\n                    for (int j = 0; j < n; j++) board[i][j] = boardChars.get(i * n + j);\n                }\n                List<String> res = new Solution().findWords(board, words.toArray(new String[0]));\n                Collections.sort(res);\n                System.out.println(res.toString());\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction findWords(board, words) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst nums = input.match(/\\d+/g);\nif (nums && nums.length >= 2) {\n    const m = parseInt(nums[0]);\n    const n = parseInt(nums[1]);\n    const strings = input.match(/[a-zA-Z]+/g) || [];\n    const boardChars = [];\n    const words = [];\n    for (const s of strings) {\n        if (boardChars.length < m * n) {\n            for (const char of s) if (boardChars.length < m * n) boardChars.push(char);\n        } else {\n            words.push(s);\n        }\n    }\n    const board = [];\n    for (let i = 0; i < m; i++) board.push(boardChars.slice(i * n, (i + 1) * n));\n    const res = findWords(board, words).sort();\n    console.log(JSON.stringify(res));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nchar** findWords(char** board, int boardSize, int* boardColSize, char** words, int wordsSize, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    static char input[1000000];\n    int len = fread(input, 1, sizeof(input) - 1, stdin);\n    input[len] = '\\0';\n    \n    char* p = input;\n    while (*p && !isdigit(*p)) p++;\n    if (!*p) return 0;\n    int m = strtol(p, &p, 10);\n    while (*p && !isdigit(*p)) p++;\n    if (!*p) return 0;\n    int n = strtol(p, &p, 10);\n    \n    char* boardChars = malloc(m * n);\n    int bCount = 0;\n    char** words = malloc(1000 * sizeof(char*));\n    int wCount = 0;\n    \n    while (*p) {\n        if (isalpha(*p)) {\n            char* start = p;\n            while (isalpha(*p)) p++;\n            int wLen = p - start;\n            if (bCount < m * n) {\n                for (int i = 0; i < wLen && bCount < m * n; i++) boardChars[bCount++] = start[i];\n            } else {\n                words[wCount] = malloc(wLen + 1);\n                strncpy(words[wCount], start, wLen);\n                words[wCount][wLen] = '\\0';\n                wCount++;\n            }\n        } else p++;\n    }\n    \n    char** board = malloc(m * sizeof(char*));\n    int* colSizes = malloc(m * sizeof(int));\n    for (int i = 0; i < m; i++) {\n        board[i] = malloc(n);\n        memcpy(board[i], boardChars + i * n, n);\n        colSizes[i] = n;\n    }\n    \n    int returnSize;\n    char** res = findWords(board, m, colSizes, words, wCount, &returnSize);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"\\\"%s\\\"%s\", res[i], i == returnSize - 1 ? \"\" : \", \");\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": '4 4\\noaan\\netae\\nihkr\\niflv\\noath pea eat rain', "expected_output": "eat oath", "is_sample": True},
        {"input": '2 2\\nab\\ncd\\nabcb', "expected_output": "", "is_sample": True},
        {"input": '1 1\\na\\na', "expected_output": "a", "is_sample": False},
        {"input": '2 2\\naa\\naa\\naaaa', "expected_output": "aaaa", "is_sample": False},
        {"input": '3 3\\nabc\\ndef\\nghi\\nabcfi h g adg', "expected_output": "abcfi adg g h", "is_sample": False},
        {"input": '1 2\\nab\\na b ba', "expected_output": "a b ba", "is_sample": False},
        {"input": '4 4\\naaaa\\naaaa\\naaaa\\naaaa\\na aaaa aaaaaaaaaaaaaaa', "expected_output": "a aaaa", "is_sample": False},
        # Stress cases
        {"input": '12 12\\n' + '\\n'.join(['a'*12]*12) + '\\n' + ' '.join(['a'*i for i in range(1, 11)]), "expected_output": " ".join(['a'*i for i in range(1, 11)]), "is_sample": False},
        {"input": '2 2\\nab\\ncd\\nefgh', "expected_output": "", "is_sample": False},
        {"input": '4 4\\n' + '\\n'.join(['abcd','efgh','ijkl','mnop']) + '\\n' + 'abcd efgh abef aei mnj', "expected_output": "abcd aei efgh", "is_sample": False}
    ]
    
    # Sort expected outputs for consistency
    for tc in test_cases:
        if tc["expected_output"]:
            tc["expected_output"] = " ".join(sorted(tc["expected_output"].split()))

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
        "topics": ["Array", "String", "Backtracking", "Trie", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/212_Word_Search_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
