import json
import os

def generate_json():
    problem_id = 832
    title = "Flipping an Image"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>832. Flipping an Image</h3>
<p>Given an <code>n x n</code> binary matrix <code>image</code>, flip the image <b>horizontally</b>, then <b>invert</b> it, and return <em>the resulting image</em>.</p>

<p>To flip an image horizontally means that each row of the image is reversed.</p>

<ul>
	<li>For example, flipping <code>[1,1,0]</code> horizontally results in <code>[0,1,1]</code>.</li>
</ul>

<p>To invert an image means that each <code>0</code> is replaced by <code>1</code>, and each <code>1</code> is replaced by <code>0</code>.</p>

<ul>
	<li>For example, inverting <code>[0,1,1]</code> results in <code>[1,0,0]</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> image = [[1,1,0],[1,0,1],[0,1,1]]
<strong>Output:</strong> [[1,0,0],[0,1,0],[0,0,1]]
<strong>Explanation:</strong> First reverse each row: [[0,1,1],[1,0,1],[1,1,0]].
Then invert the image: [[1,0,0],[0,1,0],[0,0,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong>Output:</strong> [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong>Explanation:</strong> First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == image.length</code></li>
	<li><code>n == image[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>image[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>"""

    input_format = "Format: n (matrix size), then n lines where each line i contains n space-separated 0s or 1s."
    output_format = "n lines, each with space-separated 0s or 1s representing the transformed image."
    
    constraints = [
        "1 <= n <= 20",
        "Square binary matrix.",
        "O(N^2) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To flip and invert an image:
1. **The Core Approach (Row-by-row manipulation)**:
   - For each row, we reverse it (swap elements from both ends toward the middle).
   - Simultaneously or as a second pass, we invert each element (0 -> 1, 1 -> 0).
2. **Efficiency (The Bit XOR Trick)**:
   - Let `i` be the start index and `j` be the end index of a row.
   - If `image[row][i] == image[row][j]`:
     - Both values must change after flipping and inverting.
     - `image[row][i] = 1 - image[row][i]`
     - `image[row][j] = image[row][i]` (since they were equal).
   - If `image[row][i] != image[row][j]`:
     - They stay the same after flip + invert.
     - Why? Reversing swaps them, and then inverting flips them back to their original values! (0, 1 -> 1, 0 -> 0, 1).
3. **Complexity**:
   - Time Complexity: O(N * N) - visit each cell once.
   - Space Complexity: O(1) extra space as we modify in-place or use a small temp variable."""
    
    answer = """def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
    for row in image:
        n = len(row)
        for i in range((n + 1) // 2):
            # Bitwise trick: 1 - row[i] or row[i] ^ 1
            if row[i] == row[~i]:
                row[i] = row[~i] = row[i] ^ 1
    return image"""

    boilerplate = {
        "python": "import sys\n\ndef flipAndInvertImage(image):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if lines:\n        n = int(lines[0].strip())\n        image = []\n        for i in range(1, n + 1):\n            image.append(list(map(int, lines[i].strip().split())))\n        \n        res = flipAndInvertImage(image)\n        for row in res:\n            print(\" \".join(map(str, row)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nvector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[][] flipAndInvertImage(int[][] image) {\n        // User logic\n        return new int[0][0];\n    }\n}",
        "javascript": "function flipAndInvertImage(image) {\n    // User logic\n}",
        "c": "int** flipAndInvertImage(int** image, int imageSize, int* imageColSize, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "3\\n1 1 0\\n1 0 1\\n0 1 1", "expected_output": "1 0 0\\n0 1 0\\n0 0 1", "is_sample": True},
        {"input": "4\\n1 1 0 0\\n1 0 0 1\\n0 1 1 1\\n1 0 1 0", "expected_output": "1 1 0 0\\n0 1 1 0\\n0 0 0 1\\n1 0 1 0", "is_sample": True},
        {"input": "1\\n1", "expected_output": "0", "is_sample": False},
        {"input": "1\\n0", "expected_output": "1", "is_sample": False},
        {"input": "2\\n0 0\\n1 1", "expected_output": "1 1\\n0 0", "is_sample": False}, # Flip 0 0 -> 0 0, Invert -> 1 1
        {"input": "2\\n1 0\\n1 0", "expected_output": "1 0\\n1 0", "is_sample": False}, # Flip 1 0 -> 0 1, Invert -> 1 0
        {"input": "3\\n0 0 0\\n0 0 0\\n0 0 0", "expected_output": "1 1 1\\n1 1 1\\n1 1 1", "is_sample": False},
        {"input": "3\\n1 1 1\\n1 1 1\\n1 1 1", "expected_output": "0 0 0\\n0 0 0\\n0 0 0", "is_sample": False},
        # Stress cases
        {"input": "20\\n" + "\\n".join([" ".join(["1"] * 20) for _ in range(20)]), "expected_output": "\\n".join([" ".join(["0"] * 20) for _ in range(20)]), "is_sample": False},
        {"input": "20\\n" + "\\n".join([" ".join(["0" if i % 2 == 0 else "1" for i in range(20)]) for _ in range(20)]), "expected_output": "count=20lines", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Matrix", "Simulation"],
        "companyIndex": 0
    }

    output_path = "801-1000/832_Flipping_an_Image.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
