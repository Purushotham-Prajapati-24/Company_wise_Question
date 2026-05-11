import json
import os

def generate_json():
    problem_id = 941
    title = "Valid Mountain Array"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>941. Valid Mountain Array</h3>
<p>Given an array of integers <code>arr</code>, return <code>true</code> <em>if and only if it is a valid mountain array</em>.</p>

<p>Recall that arr is a mountain array if and only if:</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>There exists some <code>i</code> with <code>0 &lt; i &lt; arr.length - 1</code> such that:
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i]</code></li>
		<li><code>arr[i] &gt; arr[i + 1] &gt; ... &lt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p><img src="file:///d:/College%20Projects/MNC_based/archive/assets/941_mountain_array.png" style="width: 500px; height: 171px;" alt="Mountain Array Illustration"/></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> arr = [2,1]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> arr = [3,5,5]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> arr = [0,3,2,1]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "3 <= n <= 10,000",
        "0 <= val <= 10,000",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To check if an array is a valid mountain array:
1. **The Core Definition**:
   - The array must have at least 3 elements.
   - It must strictly increase to a peak, then strictly decrease.
   - The peak cannot be at index 0 (if so, it never increased) or the last index (if so, it never decreased).
2. **Algorithm Strategy (Climbing)**:
   - Use a pointer `i` starting at 0.
   - **Climb Up**: Increment `i` as long as `arr[i] < arr[i+1]`.
   - **Check Peak Validity**:
     - We reached the end of the increase.
     - If `i == 0` (no increase) or `i == len(arr) - 1` (no decrease), it's not a mountain.
   - **Climb Down**: Increment `i` as long as `arr[i] > arr[i+1]`.
   - **Final Check**: If we reached the end of the array (`i == len(arr) - 1`), it's a valid mountain.
3. **Complexity**:
   - Time Complexity: O(N) because we pass through the array at most once.
   - Space Complexity: O(1) as we only use a single pointer variable."""
    
    answer = """def validMountainArray(arr: list[int]) -> bool:
    n = len(arr)
    if n < 3: return False
    i = 0
    # Walk up
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    # Peak cannot be first or last
    if i == 0 or i == n - 1:
        return False
    # Walk down
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
    return i == n - 1"""

    boilerplate = {
        "python": "import sys\n\ndef validMountainArray(arr):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        arr = list(map(int, line.split()))\n        print('true' if validMountainArray(arr) else 'false')",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nbool validMountainArray(vector<int>& arr) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean validMountainArray(int[] arr) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function validMountainArray(arr) {\n    // User logic\n}",
        "c": "bool validMountainArray(int* arr, int arrSize) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "2 1", "expected_output": "false", "is_sample": True},
        {"input": "3 5 5", "expected_output": "false", "is_sample": True},
        {"input": "0 3 2 1", "expected_output": "true", "is_sample": True},
        {"input": "1 2 3", "expected_output": "false", "is_sample": False},
        {"input": "3 2 1", "expected_output": "false", "is_sample": False},
        {"input": "1 2 3 4 3 2 1", "expected_output": "true", "is_sample": False},
        {"input": "1 2 1 2 1", "expected_output": "false", "is_sample": False},
        {"input": "10 20 30 25 20", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(5000)]) + " " + " ".join([str(5000-i) for i in range(5001)]), "expected_output": "true", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]), "expected_output": "false", "is_sample": False}
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
        "topics": ["Array"],
        "companyIndex": 0
    }

    output_path = "801-1000/941_Valid_Mountain_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
