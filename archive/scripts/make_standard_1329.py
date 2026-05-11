import json
import os
import collections

def generate_json():
    problem_id = 1329
    title = "Sort the Matrix Diagonally"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>1329. Sort the Matrix Diagonally</h3>
<p>A <strong>matrix diagonal</strong> is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the end of the matrix. For example, the matrix diagonal starting from <code>mat[2][0]</code>, where <code>mat</code> is a <code>6 x 3</code> matrix, includes cells <code>mat[2][0]</code>, <code>mat[3][1]</code>, and <code>mat[4][2]</code>.</p>

<p>Given an <code>m x n</code> matrix <code>mat</code> of integers, sort each <strong>matrix diagonal</strong> in ascending order and return the resulting matrix.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/21/1482_example_1_2.png" style="width: 500px; height: 198px;" />
<pre>
<strong>Input:</strong> mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
<strong>Output:</strong> [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
<strong>Output:</strong> [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 100</code></li>
</ul>"""

    input_format = "An m x n matrix of integers."
    output_format = "An m x n matrix where diagonals are sorted."
    
    constraints = [
        "1 <= m, n <= 100",
        "1 <= mat[i][j] <= 100"
    ]
    
    explanation = """To sort each diagonal in a matrix:
1. **Identify Diagonals**: A shared property of all cells on the same diagonal (top-left to bottom-right) is that the difference between their indices `i - j` is constant.
2. **Collect Values**: Iterate through the matrix and store the values of each diagonal in a hash map where the key is `i - j`.
3. **Sort Values**: Sort the list of values associated with each key in the hash map.
4. **Redistribute Values**: Iterate through the matrix again and replace each cell `mat[i][j]` with the next smallest value from the sorted list corresponding to its diagonal key `i - j`.
5. **Complexity**:
   - **Time**: $O(M \times N \times \log(\min(M, N)))$ because sorting each diagonal takes $\log$ of the diagonal length ($\min(M, N)$).
   - **Space**: $O(M \times N)$ to store the values of the diagonals."""
    
    answer = """import collections

def diagonalSort(mat):
    m, n = len(mat), len(mat[0])
    diagonals = collections.defaultdict(list)
    
    # Group by i - j
    for i in range(m):
        for j in range(n):
            diagonals[i - j].append(mat[i][j])
            
    # Sort each group
    for d in diagonals:
        diagonals[d].sort(reverse=True) # Pop from end for O(1)
        
    # Put back
    for i in range(m):
        for j in range(n):
            mat[i][j] = diagonals[i - j].pop()
            
    return mat"""

    boilerplate = {
        "python": "import sys, json\n\ndef diagonalSort(mat):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        mat = json.loads(line)\n        result = diagonalSort(mat)\n        print(json.dumps(result))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <unordered_map>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {\n        // implementation\n        return mat;\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public int[][] diagonalSort(int[][] mat) {\n        // implementation\n        return mat;\n    }\n}",
        "javascript": "/**\n * @param {number[][]} mat\n * @return {number[][]}\n */\nvar diagonalSort = function(mat) {\n    \n};",
        "c": "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the arrays are returned as *returnColumnSizes array.\n * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().\n */\nint** diagonalSort(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes){\n    \n}"
    }

    test_cases = [
        {"input": "[[3,3,1,1],[2,2,1,2],[1,1,1,2]]", "expected_output": "[[1,1,1,1],[1,2,2,2],[1,2,3,3]]", "is_sample": True},
        {"input": "[[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]", "expected_output": "[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]", "is_sample": True},
        {"input": "[[1]]", "expected_output": "[[1]]", "is_sample": False},
        {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[[1,2,3],[4,5,6],[7,8,9]]", "is_sample": False}, # Already sorted
        {"input": "[[9,8,7],[6,5,4],[3,2,1]]", "expected_output": "[[1,2,7],[3,5,8],[3,6,9]]", "is_sample": False}, # Reversed
        {"input": "[[5,5],[5,5]]", "expected_output": "[[5,5],[5,5]]", "is_sample": False},
        {"input": "[[100] * 100 for _ in range(100)]", "expected_output": "[[100] * 100 for _ in range(100)]", "is_sample": False}, # Stress Max
        {"input": "[[1,1,1],[1,1,1]]", "expected_output": "[[1,1,1],[1,1,1]]", "is_sample": False},
        {"input": "[list(range(100,0,-1)) for _ in range(100)]", "expected_output": "None", "is_sample": False}, # Large varied
        {"input": "[[i+j for j in range(5)] for i in range(5)]", "expected_output": "None", "is_sample": False}
    ]

    # Process test cases with None
    test_cases[4]["expected_output"] = "[[1,2,7],[3,5,8],[3,6,9]]" # Let's re-verify: d[0]=[9,5,1]->[1,5,9], d[-1]=[6,2]->[2,6], d[1]=[8,4]->[4,8]... 
    # Actually let's manually calculate for 4:
    # mat = [[9,8,7],
    #        [6,5,4],
    #        [3,2,1]]
    # d(0): 9, 5, 1 -> 1, 5, 9
    # d(1): 8, 4 -> 4, 8
    # d(2): 7 -> 7
    # d(-1): 6, 2 -> 2, 6
    # d(-2): 3 -> 3
    # Result:
    # [[1, 4, 7],
    #  [2, 5, 8],
    #  [3, 6, 9]]
    test_cases[4]["expected_output"] = "[[1,4,7],[2,5,8],[3,6,9]]"

    # Stress case 7
    test_cases[6]["input"] = json.dumps([[100] * 100 for _ in range(100)])
    test_cases[6]["expected_output"] = json.dumps([[100] * 100 for _ in range(100)])
    
    # Large varied 9
    import random
    mat_random = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
    test_cases[8]["input"] = json.dumps(mat_random)
    # To compute gold:
    gold = [row[:] for row in mat_random]
    m, n = 10, 10
    diags = collections.defaultdict(list)
    for i in range(m):
        for j in range(n):
            diags[i-j].append(gold[i][j])
    for d in diags: diags[d].sort(reverse=True)
    for i in range(m):
        for j in range(n):
            gold[i][j] = diags[i-j].pop()
    test_cases[8]["expected_output"] = json.dumps(gold)
    
    # Arithmetic 10
    mat_arith = [[i+j for j in range(5)] for i in range(5)]
    test_cases[9]["input"] = json.dumps(mat_arith)
    test_cases[9]["expected_output"] = json.dumps(mat_arith) # Diagonals i+j have constant i-j? No. 
    # wait. i-j is constant. i+j is NOT constant.
    # so for mat_arith, diags i-j:
    # d(0): (0,0)=0, (1,1)=2, (2,2)=4 -> sorted 0,2,4. Already sorted.
    # So expected is indeed mat_arith.

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
        "topics": ["Array", "Matrix", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1201-1400/1329_Sort_the_Matrix_Diagonally.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
