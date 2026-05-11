import json
import os

def generate_json():
    problem_id = 766
    title = "Toeplitz Matrix"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>766. Toeplitz Matrix</h3>
<p>Given an <code>m x n</code> <code>matrix</code>, return <em><code>true</code> if the matrix is Toeplitz. Otherwise, return <code>false</code>.</em></p>

<p>A matrix is <strong>Toeplitz</strong> if every diagonal from top-left to bottom-right has the same elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
<strong>Output:</strong> true
<strong>Explanation:</strong>
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> matrix = [[1,2],[2,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong>
The diagonal "[1, 2]" has different elements.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>m == matrix.length</code></li>
    <li><code>n == matrix[i].length</code></li>
    <li><code>1 &lt;= m, n &lt;= 20</code></li>
    <li><code>0 &lt;= matrix[i][j] &lt;= 99</code></li>
</ul>"""

    input_format = "A single line containing the 2D JSON array `matrix`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= m, n <= 20",
        "0 <= matrix[i][j] <= 99"
    ]

    explanation = """To check if a matrix is Toeplitz, we can simply iterate through all elements except the first row and the first column. For each element matrix[i][j], check if it is equal to its top-left neighbor matrix[i-1][j-1]. If all elements match their top-left neighbors, it is a Toeplitz matrix."""

    answer = """class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        matrix = json.loads(raw)
        sol = Solution()
        print("true" if sol.isToeplitzMatrix(matrix) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        // User logic here
        return false;
    }
};

vector<vector<int>> parse2DArray(string input) {
    vector<vector<int>> res;
    size_t i = 1;
    while (i < input.length() - 1) {
        if (input[i] == '[') {
            vector<int> row;
            i++;
            while (input[i] != ']') {
                if (isdigit(input[i])) {
                    int val = 0;
                    while (isdigit(input[i])) { val = val * 10 + (input[i] - '0'); i++; }
                    row.push_back(val);
                } else {
                    i++;
                }
            }
            res.push_back(row);
            i++;
        } else {
            i++;
        }
    }
    return res;
}

int main() {
    string input;
    if (getline(cin, input)) {
        vector<vector<int>> matrix = parse2DArray(input);
        Solution sol;
        cout << (sol.isToeplitzMatrix(matrix) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        // User logic here
        return false;
    }
}

public class Main {
    static int[][] parse2DArray(String raw) {
        raw = raw.trim();
        if (raw.length() < 2) return new int[0][0];
        raw = raw.substring(1, raw.length() - 1).trim();
        if (raw.isEmpty()) return new int[0][0];
        
        List<int[]> resList = new ArrayList<>();
        int i = 0;
        while (i < raw.length()) {
            if (raw.charAt(i) == '[') {
                int j = i;
                while (raw.charAt(j) != ']') j++;
                String rowStr = raw.substring(i + 1, j);
                if (rowStr.trim().isEmpty()) {
                    resList.add(new int[0]);
                } else {
                    String[] parts = rowStr.split(",");
                    int[] row = new int[parts.length];
                    for (int k = 0; k < parts.length; k++) {
                        row[k] = Integer.parseInt(parts[k].trim());
                    }
                    resList.add(row);
                }
                i = j + 1;
            } else {
                i++;
            }
        }
        int[][] res = new int[resList.size()][];
        for (int k = 0; k < resList.size(); k++) res[k] = resList.get(k);
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String input = sc.nextLine().trim();
            int[][] matrix = parse2DArray(input);
            Solution sol = new Solution();
            System.out.println(sol.isToeplitzMatrix(matrix) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var isToeplitzMatrix = function(matrix) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const matrix = JSON.parse(input);
    console.log(isToeplitzMatrix(matrix) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

bool isToeplitzMatrix(int** matrix, int matrixSize, int* matrixColSize) {
    // User logic here
    return false;
}

int** parse2DArray(char* input, int* outSize, int** outColSizes) {
    int cap = 10, size = 0, i = 0;
    int** res = (int**)malloc(cap * sizeof(int*));
    int* cols = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (input[i] == '[') {
            i++;
            if (input[i] == '[') continue;
            int rcap = 10, csize = 0;
            int* row = (int*)malloc(rcap * sizeof(int));
            while (input[i] && input[i] != ']') {
                if (isdigit(input[i])) {
                    int val, off = 0;
                    sscanf(input+i, "%d%n", &val, &off);
                    if (!off) { i++; continue; }
                    if (csize == rcap) { rcap *= 2; row = realloc(row, rcap * sizeof(int)); }
                    row[csize++] = val;
                    i += off;
                } else {
                    i++;
                }
            }
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int*)); cols = realloc(cols, cap * sizeof(int)); }
            res[size] = row;
            cols[size++] = csize;
        }
        i++;
    }
    *outSize = size;
    *outColSizes = cols;
    return res;
}

int main() {
    char input[50000];
    if (fgets(input, sizeof(input), stdin)) {
        int matrixSize;
        int* colSizes;
        int** matrix = parse2DArray(input, &matrixSize, &colSizes);
        printf("%s\\n", isToeplitzMatrix(matrix, matrixSize, colSizes) ? "true" : "false");
        for(int i=0; i<matrixSize; i++) free(matrix[i]);
        free(matrix);
        free(colSizes);
    }
    return 0;
}"""
    }

    def solve(matrix):
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

    test_cases_data = [
        [[1,2,3,4],[5,1,2,3],[9,5,1,2]],
        [[1,2],[2,2]],
        [[1]],
        [[1,2],[3,1],[4,3]],
        [[1,1,1,1,1]],
        [[1],[2],[3],[4]],
        [[10, 20], [30, 10]],
        [[x-y for y in range(20)] for x in range(20)],
        [[((x-y) % 5 + 5) % 5 for y in range(20)] for x in range(20)],
        [[1 for _ in range(20)] for _ in range(20)]
    ]

    test_cases = []
    for i, matrix in enumerate(test_cases_data):
        inp = json.dumps(matrix).replace(" ", "")
        out = "true" if solve(matrix) else "false"
        is_sample = i < 2
        test_cases.append({"input": inp, "expected_output": out, "is_sample": is_sample})

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
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Matrix"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
