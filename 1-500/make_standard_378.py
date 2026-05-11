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
        "python": "import sys\nimport re\ndef kthSmallest(matrix, k):\n    # User logic here\n    pass\nif __name__ == '__main__':\n    input_data = sys.stdin.read()\n    all_nums = list(map(int, re.findall(r'-?\\d+', input_data)))\n    if all_nums:\n        k = all_nums[-1]\n        elements = all_nums[:-1]\n        n = int(len(elements)**0.5)\n        matrix = [elements[i*n:(i+1)*n] for i in range(n)]\n        print(kthSmallest(matrix, k))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <cmath>\nusing namespace std;\nint kthSmallest(vector<vector<int>>& matrix, int k) {\n    // User logic here\n    return 0;\n}\nint main() {\n    string input((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());\n    regex re(\"-?\\\\d+\");\n    sregex_iterator it(input.begin(), input.end(), re), end;\n    vector<int> all_nums;\n    while (it != end) all_nums.push_back(stoi((it++)->str()));\n    if (!all_nums.empty()) {\n        int k = all_nums.back();\n        all_nums.pop_back();\n        int n = sqrt(all_nums.size());\n        vector<vector<int>> matrix(n, vector<int>(n));\n        for (int i = 0; i < n; i++)\n            for (int j = 0; j < n; j++)\n                matrix[i][j] = all_nums[i * n + j];\n        cout << kthSmallest(matrix, k) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\npublic class Main {\n    public static int kthSmallest(int[][] matrix, int k) {\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        List<Integer> allNums = new ArrayList<>();\n        while (m.find()) allNums.add(Integer.parseInt(m.group()));\n        if (!allNums.isEmpty()) {\n            int k = allNums.get(allNums.size() - 1);\n            allNums.remove(allNums.size() - 1);\n            int n = (int) Math.sqrt(allNums.size());\n            int[][] matrix = new int[n][n];\n            for (int i = 0; i < n; i++)\n                for (int j = 0; j < n; j++)\n                    matrix[i][j] = allNums.get(i * n + j);\n            System.out.println(kthSmallest(matrix, k));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nconst kthSmallest = (matrix, k) => {\n    // User logic here\n    return 0;\n};\nconst input = fs.readFileSync(0, 'utf8');\nconst allNums = (input.match(/-?\\d+/g) || []).map(Number);\nif (allNums.length > 0) {\n    const k = allNums.pop();\n    const n = Math.sqrt(allNums.length);\n    const matrix = [];\n    for (let i = 0; i < n; i++) matrix.push(allNums.slice(i * n, (i + 1) * n));\n    console.log(kthSmallest(matrix, k));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <math.h>\nint kthSmallest(int** matrix, int matrixSize, int* matrixColSize, int k) {\n    // User logic here\n    return 0;\n}\nint main() {\n    char *buf = malloc(1000000);\n    int bytes = fread(buf, 1, 1000000, stdin);\n    buf[bytes] = '\\0';\n    int *all_nums = malloc(100000 * sizeof(int)), count = 0;\n    char *p = buf;\n    while (*p) {\n        if (isdigit(*p) || (*p == '-' && isdigit(*(p+1)))) {\n            all_nums[count++] = strtol(p, &p, 10);\n        } else p++;\n    }\n    if (count > 0) {\n        int k = all_nums[count - 1];\n        int total_elements = count - 1;\n        int n = sqrt(total_elements);\n        int **matrix = malloc(n * sizeof(int*));\n        int *colSizes = malloc(n * sizeof(int));\n        for (int i = 0; i < n; i++) {\n            matrix[i] = malloc(n * sizeof(int));\n            colSizes[i] = n;\n            for (int j = 0; j < n; j++) matrix[i][j] = all_nums[i * n + j];\n        }\n        printf(\"%d\\n\", kthSmallest(matrix, n, colSizes, k));\n    }\n    return 0;\n}"
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
