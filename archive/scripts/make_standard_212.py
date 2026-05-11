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
        "python": "import sys\n\ndef findWords(board, words):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if lines:\n        first = lines[0].split()\n        m, n = int(first[0]), int(first[1])\n        board = [list(lines[i+1]) for i in range(m)]\n        words = lines[m+1].split()\n        results = sorted(findWords(board, words))\n        print(\" \".join(results))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <sstream>\n\nusing namespace std;\n\nvector<string> findWords(vector<vector<char>>& board, vector<string>& words) {\n    // User logic\n    return {};\n}\n\nint main() {\n    int m, n;\n    if (cin >> m >> n) {\n        vector<vector<char>> board(m, vector<char>(n));\n        for (int i = 0; i < m; i++) {\n            string row;\n            cin >> row;\n            for (int j = 0; j < n; j++) board[i][j] = row[j];\n        }\n        string line;\n        getline(cin, line); // consume leftover newline\n        if (getline(cin, line)) {\n            stringstream ss(line);\n            string word;\n            vector<string> words;\n            while (ss >> word) words.push_back(word);\n            vector<string> res = findWords(board, words);\n            sort(res.begin(), res.end());\n            for (int i = 0; i < res.size(); i++) {\n                cout << res[i] << (i == res.size() - 1 ? \"\" : \" \");\n            }\n            cout << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public List<String> findWords(char[][] board, String[] words) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String first = br.readLine();\n        if (first == null) return;\n        String[] mn = first.trim().split(\"\\\\s+\");\n        int m = Integer.parseInt(mn[0]);\n        int n = Integer.parseInt(mn[1]);\n        char[][] board = new char[m][n];\n        for (int i = 0; i < m; i++) {\n            String row = br.readLine().trim();\n            for (int j = 0; j < n; j++) board[i][j] = row.charAt(j);\n        }\n        String wordsLine = br.readLine();\n        if (wordsLine != null) {\n            String[] words = wordsLine.trim().split(\"\\\\s+\");\n            List<String> res = new Solution().findWords(board, words);\n            Collections.sort(res);\n            for (int i = 0; i < res.size(); i++) {\n                System.out.print(res.get(i) + (i == res.size() - 1 ? \"\" : \" \"));\n            }\n            System.out.println();\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction findWords(board, words) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 1) {\n    const [m, n] = input[0].trim().split(/\\\\s+/).map(Number);\n    let board = [];\n    for (let i = 0; i < m; i++) {\n        board.push(input[i+1].trim().split(''));\n    }\n    const words = input[m+1] ? input[m+1].trim().split(/\\\\s+/) : [];\n    let res = findWords(board, words).sort();\n    console.log(res.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar** findWords(char** board, int boardSize, int* boardColSize, char** words, int wordsSize, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint compare(const void* a, const void* b) {\n    return strcmp(*(const char**)a, *(const char**)b);\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) == 2) {\n        char** board = (char**)malloc(m * sizeof(char*));\n        int* colSize = (int*)malloc(m * sizeof(int));\n        for (int i = 0; i < m; i++) {\n            board[i] = (char*)malloc((n + 1) * sizeof(char));\n            scanf(\"%s\", board[i]);\n            colSize[i] = n;\n        }\n        int wordCapacity = 1000;\n        char** words = (char**)malloc(wordCapacity * sizeof(char*));\n        int wordCount = 0;\n        char tmp[100];\n        while (scanf(\"%s\", tmp) == 1) {\n            if (wordCount >= wordCapacity) {\n                wordCapacity *= 2;\n                words = (char**)realloc(words, wordCapacity * sizeof(char*));\n            }\n            words[wordCount++] = strdup(tmp);\n        }\n        int returnSize;\n        char** res = findWords(board, m, colSize, words, wordCount, &returnSize);\n        qsort(res, returnSize, sizeof(char*), compare);\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%s%s\", res[i], i == returnSize - 1 ? \"\" : \" \");\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}"
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
