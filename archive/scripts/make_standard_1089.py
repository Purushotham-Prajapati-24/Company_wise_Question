import json
import os

def generate_json():
    problem_id = 1089
    title = "Duplicate Zeros"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1089. Duplicate Zeros</h3>
<p>Given a fixed-length integer array <code>arr</code>, duplicate each occurrence of zero, shifting the remaining elements to the right.</p>

<p><strong>Note</strong> that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything from the function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,0,2,3,0,4,5,0]
<strong>Output:</strong> [1,0,0,2,3,0,0,4]
<strong>Explanation:</strong> After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3]
<strong>Output:</strong> [1,2,3]
<strong>Explanation:</strong> After calling your function, the input array is modified to: [1,2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 9</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers for the arr array."
    output_format = "A single line containing space-separated integers for the modified array."
    
    constraints = [
        "1 <= arr.length <= 10^4",
        "0 <= arr[i] <= 9",
        "Modify the array in-place.",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To duplicate zeros in-place without using extra space for a new array:
1. **Count Possible Duplications**:
   - First pass: Determine how many zeros can actually be duplicated within the original length.
   - We use two pointers: `i` for the source array and `n - 1` for the virtual expanded array boundary.
   - If we find a `0`, we virtually move the boundary twice; otherwise, once.
2. **Handle the Boundary Zero**:
   - If a zero exactly hits the edge of the original size but can't be duplicated (due to lack of space), handle it as a special case.
3. **Second Pass (Fill from End)**:
   - Walk backward from the last element that fits in the virtual expanded range.
   - Copy the elements to their new positions.
   - When a zero is encountered, write it twice in the modified output area.
4. **Complexity**:
   - Time Complexity: O(N) to traverse the array twice.
   - Space Complexity: O(1) as we modify the input array using pointers."""
    
    answer = """def duplicateZeros(arr: list[int]) -> None:
    n = len(arr)
    possible_dups = 0
    last = n - 1
    
    # First pass to find how many zeros can be duplicated
    i = 0
    while i <= last - possible_dups:
        if arr[i] == 0:
            # Special case for zero at the edge
            if i == last - possible_dups:
                arr[last] = 0
                last -= 1
                break
            possible_dups += 1
        i += 1
        
    # Second pass backward
    write_idx = last
    for read_idx in range(last - possible_dups, -1, -1):
        if arr[read_idx] == 0:
            arr[write_idx] = 0
            arr[write_idx - 1] = 0
            write_idx -= 2
        else:
            arr[write_idx] = arr[read_idx]
            write_idx -= 1"""

    boilerplate = {
        "python": "import sys\n\ndef duplicateZeros(arr):\n    # User logic here (modify array in-place)\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        arr = list(map(int, line.split()))\n        duplicateZeros(arr)\n        print(\" \".join(map(str, arr)))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid duplicateZeros(vector<int>& arr) {\n    // User logic\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public void duplicateZeros(int[] arr) {\n        // User logic\n    }\n}",
        "javascript": "function duplicateZeros(arr) {\n    // User logic\n}",
        "c": "void duplicateZeros(int* arr, int arrSize) {\n    // User logic\n}"
    }

    test_cases = [
        {"input": "1 0 2 3 0 4 5 0", "expected_output": "1 0 0 2 3 0 0 4", "is_sample": True},
        {"input": "1 2 3", "expected_output": "1 2 3", "is_sample": True},
        {"input": "0 0 0", "expected_output": "0 0 0", "is_sample": True},
        {"input": "0 1 7 6 0 2 0 7", "expected_output": "0 0 1 7 6 0 0 2", "is_sample": False},
        {"input": "1 0 1", "expected_output": "1 0 0", "is_sample": False},
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": "8 4 5 0 0 0 0 7", "expected_output": "8 4 5 0 0 0 0 0", "is_sample": False},
        # Stress cases
        {"input": " ".join(["5"]*10000), "expected_output": " ".join(["5"]*10000), "is_sample": False},
        {"input": " ".join(["0"]*10000), "expected_output": " ".join(["0"]*10000), "is_sample": False},
        {"input": " ".join(["1", "0"]*5000), "expected_output": " ".join(["1", "0", "0"]*3333 + ["1"]), "is_sample": False}
    ]
    # Refining stress case 10 expected
    def solve(arr):
        res = []
        for x in arr:
            res.append(x)
            if x == 0: res.append(0)
        return res[:len(arr)]
    
    test_cases[9]["expected_output"] = " ".join(map(str, solve([1,0]*5000)))

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
        "topics": ["Array", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1089_Duplicate_Zeros.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
