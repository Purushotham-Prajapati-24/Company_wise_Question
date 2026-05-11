import json
import os

def generate_json():
    problem_id = 427
    title = "Construct Quad Tree"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>427. Construct Quad Tree</h3>
<p>Given a <code>n * n</code> matrix <code>grid</code> of <code>0's</code> and <code>1's</code> only. We want to represent <code>grid</code> with a Quad Tree.</p>

<p>Return <em>the root of the Quad Tree representing </em><code>grid</code>.</p>

<p>A Quad Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:</p>
<ul>
	<li><code>val</code>: True if the node represents a grid of 1's or False if the node represents a grid of 0's.</li>
	<li><code>isLeaf</code>: True if the node is leaf node on the tree or False if the node has the four children.</li>
</ul>

<pre>
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
</pre>

<p>We can construct a Quad Tree from a two-dimensional area using the following steps:</p>

<ol>
	<li>If the current grid has the same value (i.e all <code>1's</code> or all <code>0's</code>) set <code>isLeaf</code> True and set <code>val</code> to the value of the grid and set the four children to Null and stop.</li>
	<li>If the current grid has different values, set <code>isLeaf</code> to False and set <code>val</code> to any value and divide the current grid into four sub-grids.</li>
	<li>Recurse for each of the four sub-grids with the appropriate area.</li>
</ol>

<p>The Quad Tree format is used to represent a binary tree. Each node is represented by a pair of <code>[isLeaf, val]</code> where <strong>val</strong> is <code>1</code> if <code>val</code> is True and <code>0</code> if <code>val</code> is False.</p>"""

    input_format = "A 2D matrix `grid` (JSON array of arrays)."
    output_format = "A list of Quad Tree nodes in level-order traversal format `[isLeaf, val]`."
    
    constraints = [
        "n == grid.length == grid[i].length",
        "n == 2^x where 0 <= x <= 6",
        "grid[i][j] is either 0 or 1."
    ]
    
    explanation = """Construct the Quad Tree recursively. For each grid segment, check if all elements are identical. If yes, return a leaf node. Otherwise, split the grid into four quadrants and recursively build the four children nodes."""
    
    answer = """class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r, c, size):
            if size == 1:
                return Node(grid[r][c] == 1, True)
            
            mid = size // 2
            tl = build(r, c, mid)
            tr = build(r, c + mid, mid)
            bl = build(r + mid, c, mid)
            br = build(r + mid, c + mid, mid)
            
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and \\
               tl.val == tr.val == bl.val == br.val:
                return Node(tl.val, True)
            
            return Node(True, False, tl, tr, bl, br)
            
        return build(0, 0, len(grid))"""

    boilerplate = {
        "python": """import sys
import json

class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        # User Logic Here
        pass

def serialize(root):
    if not root: return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            res.append([1 if node.isLeaf else 0, 1 if node.val else 0])
            if not node.isLeaf:
                queue.extend([node.topLeft, node.topRight, node.bottomLeft, node.bottomRight])
        else:
            res.append(None)
    # Remove trailing Nones
    while res and res[-1] is None: res.pop()
    return res

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        grid = json.loads(raw_input)
        sol = Solution()
        root = sol.construct(grid)
        print(json.dumps(serialize(root)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    Node(bool _val, bool _isLeaf) : val(_val), isLeaf(_isLeaf), topLeft(NULL), topRight(NULL), bottomLeft(NULL), bottomRight(NULL) {}
};

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        // User Logic Here
        return NULL;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<vector<int>> grid;
        int i = 0;
        int n = 0;
        while (i < line.length()) {
            if (line[i] == '[') {
                int j = i + 1;
                while (j < line.length() && line[j] != '[') j++;
                if (j < line.length()) {
                   // found a row
                   vector<int> row;
                   int k = j + 1;
                   while (k < line.length() && line[k] != ']') {
                       if (isdigit(line[k])) {
                           row.push_back(line[k] - '0');
                       }
                       k++;
                   }
                   grid.push_back(row);
                   i = k;
                } else break;
            }
            i++;
        }
        Solution sol;
        Node* root = sol.construct(grid);
        // Serialization logic...
        cout << \"[]\" << endl; 
    }
    return 0;
}""",
        "java": """import java.util.*;

class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft, topRight, bottomLeft, bottomRight;
    public Node(boolean _val, boolean _isLeaf) { val = _val; isLeaf = _isLeaf; }
}

class Solution {
    public Node construct(int[][] grid) {
        // User Logic Here
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        // I/O logic...
    }
}""",
        "javascript": """function Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight) {
    this.val = val;
    this.isLeaf = isLeaf;
    this.topLeft = topLeft;
    this.topRight = topRight;
    this.bottomLeft = bottomLeft;
    this.bottomRight = bottomRight;
}

var construct = function(grid) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const grid = JSON.parse(input);
    const root = construct(grid);
    // serialize and print...
    console.log(\"[]\");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node {
    bool val;
    bool isLeaf;
    struct Node* topLeft;
    struct Node* topRight;
    struct Node* bottomLeft;
    struct Node* bottomRight;
};

struct Node* construct(int** grid, int gridSize, int* gridColSize) {
    // User Logic Here
    return NULL;
}

int main() {
    return 0;
}"""
    }

    test_cases = [
        {"input": "[[0,1],[1,0]]", "expected_output": "[[0,1],[1,0],[1,1],[1,1],[1,0]]", "is_sample": True},
        {"input": "[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]", "expected_output": "[[0,1],[1,1],[0,1],[1,1],[1,0],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[0,1],[1,1],[1,1],[1,1],[1,1],[1,0],[1,0],[1,0],[1,0],[1,1],[1,1],[1,1],[1,1]]", "is_sample": True},
        {"input": "[[1]]", "expected_output": "[[1,1]]", "is_sample": False},
        {"input": "[[0]]", "expected_output": "[[1,0]]", "is_sample": False},
        {"input": "[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]", "expected_output": "[[1,1]]", "is_sample": False},
        {"input": "[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]", "expected_output": "[[1,0]]", "is_sample": False},
        {"input": "[[1,0],[1,0]]", "expected_output": "[[0,1],[1,1],[1,0],[1,1],[1,0]]", "is_sample": False},
        {"input": "[[1,1],[0,0]]", "expected_output": "[[0,1],[1,1],[1,1],[1,0],[1,0]]", "is_sample": False},
        {"input": "[ [1, 1], [0, 0] ]", "expected_output": "[[0,1],[1,1],[1,1],[1,0],[1,0]]", "is_sample": False}, # Spaces
        {"input": "[[0,0,1,1],[0,0,1,1],[1,1,0,0],[1,1,0,0]]", "expected_output": "[[0,1],[1,0],[1,1],[1,1],[1,0]]", "is_sample": False}
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
        "topics": ["Matrix", "Divide and Conquer", "Tree"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
