import json
import os

def generate_json():
    problem_id = 944
    title = "Delete Columns to Make Sorted"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>944. Delete Columns to Make Sorted</h3>
<p>You are given an array of <code>n</code> strings <code>strs</code>, all of the same length.</p>

<p>The strings can be arranged such that there is one on each line, making a grid. For example, if <code>strs = ["abc", "bce", "cae"]</code>, it can be arranged as:</p>

<pre>
abc
bce
cae
</pre>

<p>You want to <strong>delete</strong> the columns that are <strong>not sorted lexicographically</strong>. In the above example (0-indexed), columns 0 (\'a\', \'b\', \'c\') and 2 (\'c\', \'e\', \'e\') are sorted while column 1 (\'b\', \'c\', \'a\') is not, so you would delete column 1.</p>

<p>Return <em>the number of columns that you will delete</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> strs = ["cba","daf","ghi"]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The grid looks like this:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> strs = ["a","b"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The grid looks like this:
  a
  b
Column 0 is sorted, so nothing to delete.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> strs = ["zyx","wvu","tsr"]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The grid looks like this:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == strs.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 1000</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single line containing space-separated strings of equal length."
    output_format = "An integer representing the number of columns to delete."
    
    constraints = [
        "1 <= n <= 100",
        "1 <= strs[i].length <= 1,000",
        "All strings have the same length.",
        "O(N * L) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To find the number of columns that need to be deleted:
1. **Column-wise Traversal**:
   - Imagine the strings stacked on top of each other.
   - For each column index `j` from 0 to `L-1` (where `L` is the length of each string):
     - Iterate through each row `i` from 1 to `n-1`.
     - Check if the character at current row `i` and column `j` is smaller than the character at the previous row `i-1` and the same column `j`.
2. **Identification**:
   - If for any row `i`, `strs[i][j] < strs[i-1][j]`, the entire column `j` is unsorted.
   - Increment a counter for every such unsorted column identified.
3. **Complexity**:
   - Time Complexity: O(N * L) where N is number of strings and L is length of each string. Every character is checked once.
   - Space Complexity: O(1) as we only use a counter and loop indices."""
    
    answer = """def minDeletionSize(strs: list[str]) -> int:
    count = 0
    num_rows = len(strs)
    num_cols = len(strs[0])
    for j in range(num_cols):
        for i in range(1, num_rows):
            if strs[i][j] < strs[i-1][j]:
                count += 1
                break
    return count"""

    boilerplate = {
        "python": "import sys\n\ndef minDeletionSize(strs):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        strs = line.split()\n        print(minDeletionSize(strs))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint minDeletionSize(vector<string>& strs) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int minDeletionSize(String[] strs) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function minDeletionSize(strs) {\n    // User logic\n}",
        "c": "int minDeletionSize(char** strs, int strsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "cba daf ghi", "expected_output": "1", "is_sample": True},
        {"input": "a b", "expected_output": "0", "is_sample": True},
        {"input": "zyx wvu tsr", "expected_output": "3", "is_sample": True},
        {"input": "abc def ghi", "expected_output": "0", "is_sample": False},
        {"input": "aaa bbb ccc", "expected_output": "0", "is_sample": False},
        {"input": "captain america", "expected_output": "7", "is_sample": False},
        {"input": "abc abc abc", "expected_output": "0", "is_sample": False},
        {"input": "xyz abc", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": " ".join(["a" * 1000] * 100), "expected_output": "0", "is_sample": False},
        {"input": " ".join(["z" * 1000 if i % 2 == 0 else "a" * 1000 for i in range(100)]), "expected_output": "1000", "is_sample": False}
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
        "topics": ["Array", "String"],
        "companyIndex": 0
    }

    output_path = "801-1000/944_Delete_Columns_to_Make_Sorted.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
