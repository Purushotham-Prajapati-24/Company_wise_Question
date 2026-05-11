import json
import os

def generate_json():
    problem_id = 378
    title = "Kth Smallest Element in a Sorted Matrix"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>378. Kth Smallest Element in a Sorted Matrix</h3>
<p>Given an <code>n x n</code> <code>matrix</code> where each of the rows and columns is sorted in ascending order, return <em>the k<sup>th</sup> smallest element in the matrix</em>.</p>

<p>Note that it is the <code>k<sup>th</sup></code> smallest element <strong>in the sorted order</strong>, not the <code>k<sup>th</sup></code> <strong>distinct</strong> element.</p>

<p>You must find a solution with a memory complexity better than <code>O(n<sup>2</sup>)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
<strong>Output:</strong> 13
<strong>Explanation:</strong> The elements in the matrix are [1,5,9,10,11,12,13,<u>13</u>,15], and the 8<sup>th</sup> smallest number is 13.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> matrix = [[-5]], k = 1
<strong>Output:</strong> -5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>All the rows and columns of <code>matrix</code> are <strong>guaranteed</strong> to be sorted in non-decreasing order.</li>
	<li><code>1 &lt;= k &lt;= n<sup>2</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>
<ul>
	<li>Could you solve it with <code>O(n)</code> time complexity? (This is possible for certain constraints but generally $O(n \log n)$ is expected)</li>
	<li>Wait, what if <code>n</code> is very large? Binary search on values is $O(n \log(\text{max-min}))$.</li>
</ul>"""

    input_format = "An `n x n` sorted integer matrix and an integer `k`."
    output_format = "An integer representing the kth smallest element."
    
    constraints = [
        "1 <= n <= 300",
        "-10^9 <= matrix[i][j] <= 10^9",
        "1 <= k <= n^2",
        "Rows and columns are sorted."
    ]
    
    explanation = """To find the $k$-th smallest element in a matrix where rows and columns are sorted, we can use two primary methods:

### Method 1: Min-Heap ($O(K \log N)$)
Since the rows are sorted, we can treat this as "merging $N$ sorted lists." We push the first element of each row into a min-heap. We repeatedly extract the smallest element and push the next element from the same row.
- **Complexity**: $O(K \log N)$. This is efficient for small $K$.

### Method 2: Binary Search on Value Range ($O(N \log (\max - \min))$)
Since the elements are within a range $[\min, \max]$, we can perform a binary search on the **value** of the $k$-th smallest element.
1. **Initialize**: `low = matrix[0][0]`, `high = matrix[n-1][n-1]`.
2. **Search**: While `low < high`:
   - Calculate `mid`.
   - Use a helper function `count_less_equal(mid)` to count how many elements in the matrix are $\le mid$. This can be done in $O(N)$ by moving from the top-right corner down to the left.
   - If `count < k`: `low = mid + 1`.
   - Else: `high = mid`.
3. **Complexity**: $O(N \log (\text{max\_val} - \text{min\_val}))$. This is very efficient for large $N$ (though $N=300$ here).

### Complexity Analysis:
- **Time Complexity**: $O(N \log V)$ where $V = \text{max\_val} - \text{min\_val}$.
- **Space Complexity**: $O(1)$."""
    
    answer = """def kthSmallest(matrix, k):
    n = len(matrix)
    low, high = matrix[0][0], matrix[n-1][n-1]
    
    def count_less_equal(mid):
        count = 0
        r, c = 0, n - 1
        while r < n and c >= 0:
            if matrix[r][c] <= mid:
                count += (c + 1)
                r += 1
            else:
                c -= 1
        return count

    while low < high:
        mid = low + (high - low) // 2
        if count_less_equal(mid) < k:
            low = mid + 1
        else:
            high = mid
            
    return low"""

    boilerplate = {
        "python": (
            "import sys\n"
            "import json\n\n"
            "def kthSmallest(matrix, k):\n"
            "    # User logic here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    lines = sys.stdin.read().strip().splitlines()\n"
            "    if len(lines) >= 2:\n"
            "        matrix = json.loads(lines[0])\n"
            "        k = json.loads(lines[1])\n"
            "        print(kthSmallest(matrix, k))\n"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <string>\n"
            "using namespace std;\n\n"
            "int kthSmallest(vector<vector<int>>& matrix, int k) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "}\n\n"
            "int main() {\n"
            "    string line;\n"
            "    if (getline(cin, line)) {\n"
            "        vector<vector<int>> matrix;\n"
            "        vector<int> curr;\n"
            "        int i = 0, n = line.length();\n"
            "        while (i < n) {\n"
            "            if (line[i] == '-' || (line[i] >= '0' && line[i] <= '9')) {\n"
            "                int v = 0, sign = 1;\n"
            "                if (line[i] == '-') { sign = -1; i++; }\n"
            "                while (i < n && line[i] >= '0' && line[i] <= '9') {\n"
            "                    v = v * 10 + (line[i] - '0'); i++;\n"
            "                }\n"
            "                curr.push_back(v * sign);\n"
            "            } else if (line[i] == ']') {\n"
            "                if (!curr.empty() || (i > 0 && line[i-1] == '[')) {\n"
            "                    matrix.push_back(curr);\n"
            "                    curr.clear();\n"
            "                }\n"
            "                i++;\n"
            "            } else { i++; }\n"
            "        }\n"
            "        if (getline(cin, line)) {\n"
            "            int target = 0, sign = 1, j = 0;\n"
            "            while (j < line.length() && (line[j] < '0' || line[j] > '9') && line[j] != '-') j++;\n"
            "            if (j < line.length() && line[j] == '-') { sign = -1; j++; }\n"
            "            while (j < line.length() && line[j] >= '0' && line[j] <= '9') {\n"
            "                target = target * 10 + (line[j] - '0'); j++;\n"
            "            }\n"
            "            target *= sign;\n"
            "            cout << kthSmallest(matrix, target) << endl;\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        ),
        "java": (
            "import java.util.*;\n\n"
            "public class Main {\n"
            "    public static int kthSmallest(int[][] matrix, int k) {\n"
            "        // User logic here\n"
            "        return 0;\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextLine()) {\n"
            "            String line = sc.nextLine().trim();\n"
            "            List<int[]> matrixList = new ArrayList<>();\n"
            "            int i = 0, n = line.length();\n"
            "            List<Integer> curr = new ArrayList<>();\n"
            "            while (i < n) {\n"
            "                char c = line.charAt(i);\n"
            "                if (c == '-' || (c >= '0' && c <= '9')) {\n"
            "                    int v = 0, sign = 1;\n"
            "                    if (c == '-') { sign = -1; i++; }\n"
            "                    while (i < n && line.charAt(i) >= '0' && line.charAt(i) <= '9') {\n"
            "                        v = v * 10 + (line.charAt(i) - '0'); i++;\n"
            "                    }\n"
            "                    curr.add(v * sign);\n"
            "                } else if (c == ']') {\n"
            "                    if (!curr.isEmpty() || (i > 0 && line.charAt(i-1) == '[')) {\n"
            "                        matrixList.add(curr.stream().mapToInt(Integer::intValue).toArray());\n"
            "                        curr.clear();\n"
            "                    }\n"
            "                    i++;\n"
            "                } else { i++; }\n"
            "            }\n"
            "            int[][] matrix = matrixList.toArray(new int[0][]);\n"
            "            if (sc.hasNextLine()) {\n"
            "                int k = Integer.parseInt(sc.nextLine().trim());\n"
            "                System.out.println(kthSmallest(matrix, k));\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "var kthSmallest = function(matrix, k) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "};\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').trim().split('\\n');\n"
            "    if (input.length >= 2) {\n"
            "        const matrix = JSON.parse(input[0].trim());\n"
            "        const k = JSON.parse(input[1].trim());\n"
            "        console.log(kthSmallest(matrix, k));\n"
            "    }\n"
            "}\n"
            "main();\n"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n\n"
            "int kthSmallest(int** matrix, int matrixSize, int* matrixColSize, int k) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "}\n\n"
            "int main() {\n"
            "    char buf[20000];\n"
            "    if (fgets(buf, sizeof(buf), stdin)) {\n"
            "        int* rows[1000];\n"
            "        int colSizes[1000];\n"
            "        int rowCount = 0;\n"
            "        int temp[1000];\n"
            "        int tempCount = 0;\n"
            "        int i = 0;\n"
            "        while (buf[i]) {\n"
            "            if (buf[i] == '-' || (buf[i] >= '0' && buf[i] <= '9')) {\n"
            "                int v = 0, sign = 1;\n"
            "                if (buf[i] == '-') { sign = -1; i++; }\n"
            "                while (buf[i] >= '0' && buf[i] <= '9') {\n"
            "                    v = v * 10 + (buf[i] - '0'); i++;\n"
            "                }\n"
            "                temp[tempCount++] = v * sign;\n"
            "            } else if (buf[i] == ']') {\n"
            "                if (tempCount > 0 || (i > 0 && buf[i-1] == '[')) {\n"
            "                    rows[rowCount] = (int*)malloc(tempCount * sizeof(int));\n"
            "                    memcpy(rows[rowCount], temp, tempCount * sizeof(int));\n"
            "                    colSizes[rowCount] = tempCount;\n"
            "                    rowCount++;\n"
            "                    tempCount = 0;\n"
            "                }\n"
            "                i++;\n"
            "            } else { i++; }\n"
            "        }\n"
            "        if (fgets(buf, sizeof(buf), stdin)) {\n"
            "            int k = atoi(buf);\n"
            "            printf(\"%d\\n\", kthSmallest(rows, rowCount, colSizes, k));\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        )
    }

    test_cases = [
        {"input": "[[1,5,9],[10,11,13],[12,13,15]]\\n8", "expected_output": "13", "is_sample": True},
        {"input": "[[-5]]\\n1", "expected_output": "-5", "is_sample": True},
        {"input": "[[1,2],[3,4]]\\n2", "expected_output": "2", "is_sample": False},
        {"input": "[[1,2],[3,4]]\\n3", "expected_output": "3", "is_sample": False},
        {"input": "[[1,2,3],[1,2,3],[1,2,3]]\\n5", "expected_output": "2", "is_sample": False},
        {"input": "[[-10,-5],[-2,0]]\\n2", "expected_output": "-5", "is_sample": False},
        {"input": "[[1,10,20],[2,15,30],[5,25,100]]\\n5", "expected_output": "10", "is_sample": False},
        {"input": json.dumps([[i+j for j in range(20)] for i in range(20)]) + "\\n100", "expected_output": "18", "is_sample": False},
        {"input": json.dumps([[0]*20 for _ in range(20)]) + "\\n400", "expected_output": "0", "is_sample": False},
        {"input": json.dumps([[i*j+1 for j in range(10)] for i in range(10)]) + "\\n50", "expected_output": "10", "is_sample": False},
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
        "topics": ["Array", "Binary Search", "Sorting", "Heap (Priority Queue)", "Matrix"],
        "companyIndex": 1
    }

    output_path = "301-500/378_Kth_Smallest_Element_in_a_Sorted_Matrix.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
