import json
import os

def generate_json():
    problem_id = 1064
    title = "Fixed Point"
    difficulty = "Easy"
    marks = 5
    
    html_description = """<h3>1064. Fixed Point</h3>
<p>Given an array of distinct integers <code>arr</code> that is sorted in ascending order, return the smallest index <code>i</code> that satisfies <code>arr[i] == i</code>. If no such index exists, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [-10,-5,0,3,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> For the given array, arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3, thus the index 3 is a fixed point.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [0,2,5,8,17]
<strong>Output:</strong> 0
<strong>Explanation:</strong> arr[0] = 0, thus the index 0 is a fixed point.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [-10,-5,3,4,7,9]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no such i such that arr[i] == i, thus the output is -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt; 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Can you solve it in <code>O(log n)</code> time complexity?
"""

    input_format = "A single line containing space-separated integers for the sorted array arr."
    output_format = "An integer representing the smallest index i where arr[i] == i, or -1."
    
    constraints = [
        "1 <= arr.length <= 10,000",
        "-10^9 <= arr[i] <= 10^9",
        "arr is sorted in ascending order.",
        "arr contains distinct integers.",
        "O(log N) time complexity is required."
    ]
    
    explanation = """To find the smallest index `i` such that `arr[i] == i` in a sorted array of distinct integers:
1. **The Insight**:
   - Because the array is sorted and all elements are distinct, the function $f(i) = arr[i] - i$ is **non-decreasing**. 
   - Specifically, if $arr[i] < i$, then for all $j < i$, $arr[j]$ must also be less than $j$. If $arr[i] > i$, then for all $j > i$, $arr[j]$ must be greater than $j$.
   - This monotonicity allows us to use **Binary Search**.
2. **Algorithm Strategy**:
   - We search for the first index where $arr[i] == i$.
   - Initialize `low = 0`, `high = n - 1`, and `ans = -1`.
   - While `low <= high`:
     - `mid = (low + high) // 2`
     - If `arr[mid] >= mid`:
       - If `arr[mid] == mid`, we record this as a potential answer: `ans = mid`.
       - Because we want the **smallest** index, we continue searching in the left half: `high = mid - 1`.
     - Else (`arr[mid] < mid`):
       - We must look in the right half: `low = mid + 1`.
3. **Complexity**:
   - Time Complexity: $O(\log N)$ due to binary search.
   - Space Complexity: $O(1)$ extra space."""
    
    answer = """def fixedPoint(arr: list[int]) -> int:
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= mid:
            if arr[mid] == mid:
                ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans"""

    boilerplate = {
        "python": "import sys\n\ndef fixedPoint(arr):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        arr = list(map(int, line.split()))\n        print(fixedPoint(arr))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint fixedPoint(vector<int>& arr) {\n    // User logic\n    return -1;\n}",
        "java": "public class Solution {\n    public int fixedPoint(int[] arr) {\n        // User logic\n        return -1;\n    }\n}",
        "javascript": "function fixedPoint(arr) {\n    // User logic\n}",
        "c": "int fixedPoint(int* arr, int arrSize) {\n    // User logic\n    return -1;\n}"
    }

    test_cases = [
        {"input": "-10 -5 0 3 7", "expected_output": "3", "is_sample": True},
        {"input": "0 2 5 8 17", "expected_output": "0", "is_sample": True},
        {"input": "-10 -5 3 4 7 9", "expected_output": "-1", "is_sample": True},
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": "1", "expected_output": "-1", "is_sample": False},
        {"input": "-1 1 3 5 7", "expected_output": "1", "is_sample": False},
        {"input": "-1 0 1 2 4", "expected_output": "4", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(10000)]), "expected_output": "0", "is_sample": False},
        {"input": " ".join([str(i-10000) for i in range(10000)]), "expected_output": "-1", "is_sample": False},
        {"input": " ".join([str(i-5000) for i in range(10000)]), "expected_output": "5000", "is_sample": False}
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
        "topics": ["Array", "Binary Search"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1064_Fixed_Point.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
