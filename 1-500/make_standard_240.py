import json
import os

def generate_json():
    problem_id = 240
    title = "Search a 2D Matrix II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>240. Search a 2D Matrix II</h3>
<p>Write an efficient algorithm that searches for a <code>target</code> value in an <code>m x n</code> integer matrix <code>matrix</code>. This matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted in ascending from left to right.</li>
	<li>Integers in each column are sorted in ascending from top to bottom.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg" style="width: 300px; height: 300px;" />
<pre><strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg" style="width: 300px; height: 300px;" />
<pre><strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>All the integers in each row are <strong>sorted</strong> in ascending order.</li>
	<li>All the integers in each column are <strong>sorted</strong> in ascending order.</li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Two lines: first, an m x n 2D array of integers; second, an integer target."
    output_format = "A boolean (true/false)."
    
    constraints = [
        "1 <= m, n <= 300",
        "Rows and columns sorted.",
        "O(m + n) time complexity required."
    ]
    
    explanation = """To search in an m x n matrix where both rows and columns are sorted effectively:
1. **Start from Top-Right Corner**: Start at `(0, n-1)`.
2. **Logic**:
   - If `matrix[row][col] == target`, return `true`.
   - If `matrix[row][col] > target`, the current column can't contain the target (since all elements below are even larger), so decrement `col` (move left).
   - If `matrix[row][col] < target`, the current row can't contain the target (since all elements left are even smaller), so increment `row` (move down).
3. **Complexity**:
   - Time: O(M + N) where M is rows and N is columns.
   - Space: O(1)."""
    
    answer = """class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
                
        return False"""

    boilerplate = {
        "python": "import sys\nimport re\nimport json\n\ndef searchMatrix(matrix, target):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Try JSON parsing first for robustness\n    try:\n        # Split to separate matrix and target\n        parts = raw_input.strip().split('\\n')\n        if len(parts) >= 2:\n            matrix = json.loads(parts[0])\n            target = int(re.search(r'-?\\d+', parts[1]).group())\n            print(\"true\" if searchMatrix(matrix, target) else \"false\")\n            sys.exit(0)\n    except:\n        pass\n        \n    # Fallback to lethal regex extraction\n    nums = [int(x) for x in re.findall(r'-?\\d+', raw_input)]\n    if not nums: sys.exit(0)\n    \n    bracket_count = raw_input.count('[')\n    if bracket_count > 0:\n        m = max(1, bracket_count - 1)\n        target = nums[-1]\n        n = (len(nums) - 1) // m\n        matrix = [nums[i*n : (i+1)*n] for i in range(m)]\n    else:\n        if len(nums) >= 3:\n            m, n = nums[0], nums[1]\n            target = nums[-1]\n            matrix = []\n            for i in range(m):\n                matrix.append(nums[2 + i*n : 2 + (i+1)*n])\n        else:\n            sys.exit(0)\n            \n    print(\"true\" if searchMatrix(matrix, target) else \"false\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nbool searchMatrix(vector<vector<int>>& matrix, int target) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    regex re(\"-?\\\\d+\");\n    auto words_begin = sregex_iterator(input.begin(), input.end(), re);\n    auto words_end = sregex_iterator();\n    vector<int> nums;\n    for (sregex_iterator i = words_begin; i != words_end; ++i) nums.push_back(stoi(i->str()));\n    if (nums.empty()) return 0;\n    \n    int m_val, n_val, target_val, start_idx;\n    int bracket_count = 0;\n    for (char c : input) if (c == '[') bracket_count++;\n    \n    if (bracket_count > 0) {\n        m_val = max(1, bracket_count - 1);\n        target_val = nums.back();\n        n_val = (nums.size() - 1) / m_val;\n        start_idx = 0;\n    } else {\n        if (nums.size() < 3) return 0;\n        m_val = nums[0];\n        n_val = nums[1];\n        target_val = nums.back();\n        start_idx = 2;\n    }\n    \n    vector<vector<int>> matrix(m_val, vector<int>(n_val));\n    for (int i = 0; i < m_val; i++) {\n        for (int j = 0; j < n_val; j++) {\n            if (start_idx + i * n_val + j < nums.size()) {\n                matrix[i][j] = nums[start_idx + i * n_val + j];\n            }\n        }\n    }\n    cout << (searchMatrix(matrix, target_val) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public boolean searchMatrix(int[][] matrix, int target) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Pattern p = Pattern.compile(\"-?\\\\d+\");\n        Matcher m_matcher = p.matcher(input);\n        List<Integer> nums = new ArrayList<>();\n        while (m_matcher.find()) nums.add(Integer.parseInt(m_matcher.group()));\n        if (nums.isEmpty()) return;\n        \n        int m_val, n_val, target_val, startIdx;\n        int bracketCount = 0;\n        for (char c : input.toCharArray()) if (c == '[') bracketCount++;\n        \n        if (bracketCount > 0) {\n            m_val = Math.max(1, bracketCount - 1);\n            target_val = nums.get(nums.size() - 1);\n            n_val = (nums.size() - 1) / m_val;\n            startIdx = 0;\n        } else {\n            if (nums.size() < 3) return;\n            m_val = nums.get(0);\n            n_val = nums.get(1);\n            target_val = nums.get(nums.size() - 1);\n            startIdx = 2;\n        }\n        \n        int[][] matrix = new int[m_val][n_val];\n        for (int i = 0; i < m_val; i++) {\n            for (int j = 0; j < n_val; j++) {\n                if (startIdx + i * n_val + j < nums.size()) {\n                    matrix[i][j] = nums.get(startIdx + i * n_val + j);\n                }\n            }\n        }\n        System.out.println(new Solution().searchMatrix(matrix, target_val) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction searchMatrix(matrix, target) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst nums = (input.match(/-?\\d+/g) || []).map(Number);\nif (nums.length > 0) {\n    let m_val, n_val, target_val, startIdx;\n    const bracketCount = (input.match(/\\[/g) || []).length;\n    \n    if (bracketCount > 0) {\n        m_val = Math.max(1, bracketCount - 1);\n        target_val = nums[nums.length - 1];\n        n_val = Math.floor((nums.length - 1) / m_val);\n        startIdx = 0;\n    } else {\n        m_val = nums[0];\n        n_val = nums[1];\n        target_val = nums[nums.length - 1];\n        startIdx = 2;\n    }\n    \n    const matrix = [];\n    for (let i = 0; i < m_val; i++) {\n        matrix.push(nums.slice(startIdx + i * n_val, startIdx + (i + 1) * n_val));\n    }\n    console.log(searchMatrix(matrix, target_val) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <ctype.h>\n\nbool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    static char buffer[1000000];\n    int bytesRead = fread(buffer, 1, sizeof(buffer) - 1, stdin);\n    buffer[bytesRead] = '\\0';\n    int* nums = (int*)malloc(100000 * sizeof(int));\n    int numsSize = 0;\n    char* ptr = buffer;\n    while (*ptr) {\n        if (isdigit(*ptr) || (*ptr == '-' && isdigit(*(ptr+1)))) {\n            nums[numsSize++] = (int)strtol(ptr, &ptr, 10);\n        } else ptr++;\n    }\n    if (numsSize == 0) return 0;\n    \n    int m_val, n_val, target_val, startIdx;\n    int bracketCount = 0;\n    for (int i = 0; buffer[i]; i++) if (buffer[i] == '[') bracketCount++;\n    \n    if (bracketCount > 0) {\n        m_val = (bracketCount - 1 > 0) ? (bracketCount - 1) : 1;\n        target_val = nums[numsSize - 1];\n        n_val = (numsSize - 1) / m_val;\n        startIdx = 0;\n    } else {\n        if (numsSize < 3) return 0;\n        m_val = nums[0]; n_val = nums[1];\n        target_val = nums[numsSize - 1];\n        startIdx = 2;\n    }\n    \n    int** matrix = (int**)malloc(m_val * sizeof(int*));\n    int* colSizes = (int*)malloc(m_val * sizeof(int));\n    for (int i = 0; i < m_val; i++) {\n        matrix[i] = (int*)malloc(n_val * sizeof(int));\n        colSizes[i] = n_val;\n        for (int j = 0; j < n_val; j++) {\n            if (startIdx + i * n_val + j < numsSize) {\n                matrix[i][j] = nums[startIdx + i * n_val + j];\n            }\n        }\n    }\n    printf(\"%s\\n\", searchMatrix(matrix, m_val, colSizes, target_val) ? \"true\" : \"false\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\\n5", "expected_output": "true", "is_sample": True},
        {"input": "[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\\n20", "expected_output": "false", "is_sample": True},
        {"input": "[[1,1]]\\n1", "expected_output": "true", "is_sample": False},
        {"input": "[[1]]\\n0", "expected_output": "false", "is_sample": False},
        {"input": "[[-5]]\\n-5", "expected_output": "true", "is_sample": False},
        {"input": "[[1,2,3],[4,5,6],[7,8,9]]\\n5", "expected_output": "true", "is_sample": False},
        {"input": "[[1,2,3],[4,5,6],[7,8,9]]\\n10", "expected_output": "false", "is_sample": False},
        # Stress Tests (300x300)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    # Stress 8: 300x300 all same 7, target 7
    m8 = [[7]*300 for _ in range(300)]
    test_cases[7] = {"input": json.dumps(m8) + "\\n7", "expected_output": "true", "is_sample": False}
    # Stress 9: 300x300 sequential, target 90000
    m9 = [[i*300 + j for j in range(300)] for i in range(300)]
    test_cases[8] = {"input": json.dumps(m9) + "\\n90000", "expected_output": "false", "is_sample": False}
    # Stress 10: 300x300 sparse diagonal, target 1
    m10 = [[0]*300 for _ in range(300)]
    m10[299][299] = 1
    test_cases[9] = {"input": json.dumps(m10) + "\\n1", "expected_output": "true", "is_sample": False}

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
        "topics": ["Array", "Binary Search", "Divide and Conquer", "Matrix"],
        "companyIndex": 0
    }

    output_path = "201-400/240_Search_a_2D_Matrix_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
