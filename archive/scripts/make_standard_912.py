import json
import os

def generate_json():
    problem_id = 912
    title = "Sort an Array"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>912. Sort an Array</h3>
<p>Given an array of integers <code>nums</code>, sort the array in ascending order and return it.</p>

<p>You must solve the problem without using any built-in functions in <code>O(n log n)</code> time complexity and with the smallest space complexity possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,2,3,1]
<strong>Output:</strong> [1,2,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,1,1,2,0,0]
<strong>Output:</strong> [0,0,1,1,2,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-5 * 10<sup>4</sup> &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An integer n, followed by n space-separated integers."
    output_format = "n space-separated integers in ascending order."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def sortArray(nums):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
    
    return merge_sort(nums)"""

    boilerplate = {
        "python": "import sys\n\ndef merge(left, right):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    left = input_data[0] if len(input_data) > 0 else \"\"\n    right = input_data[1] if len(input_data) > 1 else \"\"\n    print(merge(left, right))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint merge(string left, string right) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string left; cin >> left;\n    string right; cin >> right;\n    cout << merge(left, right) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
