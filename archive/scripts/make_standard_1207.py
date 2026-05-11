import json
import os

def generate_json():
    problem_id = 1207
    title = "Unique Number of Occurrences"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1207. Unique Number of Occurrences</h3>
<p>Given an array of integers <code>arr</code>, return <code>true</code> <em>if the number of occurrences of each value in the array is <strong>unique</strong> or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,2,1,1,3]
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [-3,0,1,-3,1,1,1,-3,10,0]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>-1000 &lt;= arr[i] &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers for the arr array."
    output_format = "A string 'true' if the frequency of each element is unique, 'false' otherwise."
    
    constraints = [
        "1 <= arr.length <= 1000",
        "-1000 <= arr[i] <= 1000",
        "O(N) time complexity.",
        "O(N) space complexity."
    ]
    
    explanation = """To determine if the frequencies of elements in an array are unique:
1. **Count Frequencies**:
   - Use a hash map (or dictionary) to store the count of each element in the array.
   - For every number `num` in `arr`, increment `counts[num]`.
2. **Collect Frequencies**:
   - Extract the values from the hash map (the actual frequency numbers).
3. **Check for Uniqueness**:
   - Convert the list of frequencies into a set.
   - If the size of the set is equal to the number of distinct elements (the number of keys in our hash map), then all frequencies were unique.
4. **Complexity**:
   - Time Complexity: O(N) to iterate through the array once and then through the hash map.
   - Space Complexity: O(N) to store the hash map and the set of frequencies."""
    
    answer = """from collections import Counter
def uniqueOccurrences(arr: list[int]) -> bool:
    counts = Counter(arr)
    freqs = counts.values()
    return len(freqs) == len(set(freqs))"""

    boilerplate = {
        "python": "import sys\nfrom collections import Counter\n\ndef uniqueOccurrences(arr):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        arr = list(map(int, line.split()))\n        print(str(uniqueOccurrences(arr)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <unordered_set>\n\nusing namespace std;\n\nbool uniqueOccurrences(vector<int>& arr) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean uniqueOccurrences(int[] arr) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function uniqueOccurrences(arr) {\n    // User logic\n}",
        "c": "bool uniqueOccurrences(int* arr, int arrSize) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "1 2 2 1 1 3", "expected_output": "true", "is_sample": True},
        {"input": "1 2", "expected_output": "false", "is_sample": True},
        {"input": "-3 0 1 -3 1 1 1 -3 10 0", "expected_output": "true", "is_sample": True},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "5 5 5 5 3 3 2 2", "expected_output": "false", "is_sample": False},
        {"input": "-1 -1 -2 -2", "expected_output": "false", "is_sample": False},
        {"input": "100 200 300 100 300 100", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1000)]), "expected_output": "false", "is_sample": False}, # All freq 1
        {"input": " ".join([str(0)] * 1000), "expected_output": "true", "is_sample": False}, # Single freq 1000
        {"input": " ".join([str(i//2) for i in range(1000)]), "expected_output": "false", "is_sample": False} # All freq 2
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "1201-1400/1207_Unique_Number_of_Occurrences.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
