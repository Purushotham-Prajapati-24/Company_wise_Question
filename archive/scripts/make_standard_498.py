import json
import os

def generate_json():
    problem_id = 498
    title = "Diagonal Traverse"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>498. Diagonal Traverse</h3>
<p>Given an <code>m x n</code> matrix <code>mat</code>, return <em>an array of all the elements of the array in a diagonal order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg" style="width: 334px; height: 334px;" />
<pre><strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,4,7,5,3,6,8,9]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> mat = [[1,2],[3,4]]
<strong>Output:</strong> [1,2,3,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= mat[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "Line 1: A JSON 2D array `mat` (matrix of integers)."
    output_format = "A JSON array of integers representing the diagonal traversal."
    
    constraints = [
        "1 <= m, n <= 10^4",
        "1 <= m * n <= 10^4",
        "-10^5 <= mat[i][j] <= 10^5"
    ]
    
    explanation = "The diagonals are identified by the sum of indices `i + j`. Diagonals with even sums are traversed upwards, and diagonals with odd sums are traversed downwards. We can iterate through all possible sums from `0` to `m + n - 2`, and for each sum, determine the starting row and column based on the traversal direction."
    
    answer = """class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]: return []
        m, n = len(mat), len(mat[0])
        res = []
        for s in range(m + n - 1):
            if s % 2 == 0:
                # Upward
                r = min(s, m - 1)
                c = s - r
                while r >= 0 and c < n:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                # Downward
                c = min(s, n - 1)
                r = s - c
                while c >= 0 and r < m:
                    res.append(mat[r][c])
                    r += 1
                    c -= 1
        return res"""

    boilerplate = {
        "python": r"""import sys
import json

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        # User Logic Here
        return []

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        mat = json.loads(line)
        sol = Solution()
        print(json.dumps(sol.findDiagonalOrder(mat)))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        // User Logic Here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<vector<int>> mat;
        int i = 0;
        while(i < line.length()){
            if(line[i] == '['){
                i++;
                while(i < line.length() && line[i] != ']'){
                    if(line[i] == '['){
                        i++;
                        vector<int> row;
                        string cur = "";
                        while(i < line.length() && line[i] != ']'){
                            if(isdigit(line[i]) || line[i] == '-') cur += line[i];
                            else if(line[i] == ',' && !cur.empty()){
                                row.push_back(stoi(cur));
                                cur = "";
                            }
                            i++;
                        }
                        if(!cur.empty()) row.push_back(stoi(cur));
                        mat.push_back(row);
                    }
                    i++;
                }
            }
            i++;
        }
        Solution sol;
        vector<int> res = sol.findDiagonalOrder(mat);
        cout << "[";
        for (int j = 0; j < res.size(); j++) {
            cout << res[j] << (j == res.size() - 1 ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        // User Logic Here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            if (line.equals("[]")) { System.out.println("[]"); return; }
            String[] rowParts = line.substring(1, line.length() - 1).split("\\\\],\\\\s*\\\\[");
            List<int[]> list = new ArrayList<>();
            for (String rowPart : rowParts) {
                String cleanRow = rowPart.replaceAll("[\\\\[\\\\]]", "");
                if (cleanRow.isEmpty()) continue;
                String[] nums = cleanRow.split(",\\\\s*");
                int[] row = new int[nums.length];
                for (int i = 0; i < nums.length; i++) row[i] = Integer.parseInt(nums[i]);
                list.add(row);
            }
            int[][] mat = list.toArray(new int[0][]);
            Solution sol = new Solution();
            int[] res = sol.findDiagonalOrder(mat);
            System.out.println(Arrays.toString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": r"""/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findDiagonalOrder = function(mat) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const mat = JSON.parse(input);
    console.log(JSON.stringify(findDiagonalOrder(mat)));
}""",
        "c": r"""#include <stdio.h>
#include <stdlib.h>

int* findDiagonalOrder(int** mat, int matSize, int* matColSize, int* returnSize) {
    // User Logic Here
    *returnSize = 0;
    return NULL;
}

int main() {
    // Manual parsing logic for 2D array...
    printf("[]\n");
    return 0;
}"""
    }

    test_cases = [
        {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[1, 2, 4, 7, 5, 3, 6, 8, 9]", "is_sample": True},
        {"input": "[[1,2],[3,4]]", "expected_output": "[1, 2, 3, 4]", "is_sample": True},
        {"input": "[[5]]", "expected_output": "[5]", "is_sample": False},
        {"input": "[[1,2,3]]", "expected_output": "[1, 2, 3]", "is_sample": False},
        {"input": "[[1],[2],[3]]", "expected_output": "[1, 2, 3]", "is_sample": False},
        {"input": "[[-1]]", "expected_output": "[-1]", "is_sample": False},
        {"input": "[[1,2],[3,4],[5,6]]", "expected_output": "[1, 2, 3, 5, 4, 6]", "is_sample": False},
        {"input": "[[1,2,3],[4,5,6]]", "expected_output": "[1, 2, 4, 5, 3, 6]", "is_sample": False},
        {"input": "[[1,1],[1,1]]", "expected_output": "[1, 1, 1, 1]", "is_sample": False},
        {"input": json.dumps([[i*j for j in range(10)] for i in range(1)] ), "expected_output": json.dumps([0]*10), "is_sample": False}
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
        "topics": ["Array", "Matrix", "Simulation"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Diagonal_Traverse.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
