import json
import os

def generate_json():
    problem_id = 1122
    title = "Relative Sort Array"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1122. Relative Sort Array</h3>
<p>Given two arrays <code>arr1</code> and <code>arr2</code>, the elements of <code>arr2</code> are distinct, and all elements in <code>arr2</code> are also in <code>arr1</code>.</p>

<p>Sort the elements of <code>arr1</code> such that the relative ordering of items in <code>arr1</code> are the same as in <code>arr2</code>. Elements that do not appear in <code>arr2</code> should be placed at the end of <code>arr1</code> in <strong>ascending</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
<strong>Output:</strong> [2,2,2,1,4,3,3,9,6,7,19]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
<strong>Output:</strong> [22,28,8,6,17,44]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= arr1[i], arr2[i] &lt;= 1000</code></li>
	<li>All the elements of <code>arr2</code> are <strong>distinct</strong>.</li>
	<li>Each <code>arr2[i]</code> is in <code>arr1</code>.</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated arr1. Line 2: space-separated arr2."
    output_format = "A single line containing space-separated integers for the relative-sorted array."
    
    constraints = [
        "1 <= arr1.length, arr2.length <= 1000",
        "0 <= arr1[i], arr2[i] <= 1000",
        "arr2 elements are distinct and in arr1.",
        "O(N + M + MaxVal) time complexity.",
        "O(MaxVal) space complexity."
    ]
    
    explanation = """To sort `arr1` relative to `arr2` efficiently:
1. **Counting Sort Approach**:
   - Since the range of values is small (0-1000), we can use a frequency map (an array of size 1001).
   - Count the frequency of every element in `arr1`.
2. **First Pass (Relative Order)**:
   - Iterate through the elements of `arr2` in order.
   - For each element, append it to the result list as many times as it appeared in `arr1` (using the count from the frequency map).
   - Set the count for that element to 0 in the frequency map to mark it as processed.
3. **Second Pass (Remaining Elements)**:
   - Iterate through the frequency map from index 0 to 1000.
   - If a count is greater than 0, it means the element was in `arr1` but not in `arr2`.
   - Append these elements to the result list (this automatically keeps them in ascending order).
4. **Complexity**:
   - Time Complexity: O(N + M + MaxVal) where N is len(arr1), M is len(arr2), and MaxVal is 1000.
   - Space Complexity: O(MaxVal) for the frequency array."""
    
    answer = """def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    count = [0] * 1001
    for x in arr1:
        count[x] += 1
    
    res = []
    for x in arr2:
        while count[x] > 0:
            res.append(x)
            count[x] -= 1
            
    for i in range(1001):
        while count[i] > 0:
            res.append(i)
            count[i] -= 1
            
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef relativeSortArray(arr1, arr2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        arr1 = list(map(int, lines[0].split()))\n        arr2 = list(map(int, lines[1].split()))\n        res = relativeSortArray(arr1, arr2)\n        print(\" \".join(map(str, res)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nvector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[] relativeSortArray(int[] arr1, int[] arr2) {\n        // User logic\n        return new int[0];\n    }\n}",
        "javascript": "function relativeSortArray(arr1, arr2) {\n    // User logic\n}",
        "c": "int* relativeSortArray(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "2 3 1 3 2 4 6 7 9 2 19\\n2 1 4 3 9 6", "expected_output": "2 2 2 1 4 3 3 9 6 7 19", "is_sample": True},
        {"input": "28 6 22 8 44 17\\n22 28 8 6", "expected_output": "22 28 8 6 17 44", "is_sample": True},
        {"input": "1 1 1\\n1", "expected_output": "1 1 1", "is_sample": True},
        {"input": "2 2 3\\n2", "expected_output": "2 2 3", "is_sample": False},
        {"input": "10 2 3 10\\n2 10", "expected_output": "2 10 10 3", "is_sample": False},
        {"input": "4 4 4\\n4", "expected_output": "4 4 4", "is_sample": False},
        {"input": "1 3 5 2 4 6\\n1 2", "expected_output": "1 2 3 4 5 6", "is_sample": False},
        # Stress cases
        {"input": " ".join(["5"]*1000) + "\\n5", "expected_output": " ".join(["5"]*1000), "is_sample": False},
        {"input": " ".join([str(i) for i in range(1001)]) + "\\n" + " ".join([str(1000 - i) for i in range(1001)]), "expected_output": " ".join([str(1000 - i) for i in range(1001)]), "is_sample": False},
        {"input": " ".join(["0"]*500 + ["1000"]*500) + "\\n0", "expected_output": " ".join(["0"]*500 + ["1000"]*500), "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Sorting", "Counting Sort"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1122_Relative_Sort_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
