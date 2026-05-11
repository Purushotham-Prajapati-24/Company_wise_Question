import json
import os

def generate_json():
    problem_id = 278
    title = "First Bad Version"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>278. First Bad Version</h3>
<p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.</p>

<p>Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.</p>

<p>You are given an API <code>bool isBadVersion(version)</code> which returns whether <code>version</code> is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5, bad = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
call isBadVersion(3) -&gt; false
call isBadVersion(5) -&gt; true
call isBadVersion(4) -&gt; true
Then 4 is the first bad version.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, bad = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= bad &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "Two lines. Line 1: n. Line 2: bad (the target result)."
    output_format = "An integer representing the first bad version."
    
    constraints = [
        "1 <= bad <= n <= 2^31 - 1",
        "O(log N) time complexity.",
        "O(1) space complexity.",
        "Minimize calls to isBadVersion API."
    ]
    
    explanation = """To find the first bad version with the minimum number of API calls:
1. **Binary Search**:
   - The versions form a monotonically increasing sequence of "good" followed by "bad": `G, G, G, B, B, B`.
   - Use binary search in the range `[1, n]`.
   - Calculate `mid = low + (high - low) // 2`.
   - If `isBadVersion(mid)` is true, then the first bad version is either `mid` or somewhere to its left. Set `high = mid`.
   - If `isBadVersion(mid)` is false, then the first bad version must be to the right of `mid`. Set `low = mid + 1`.
2. **Result**:
   - The loop continues until `low == high`, which will be the first bad version.
3. **Complexity**:
   - Time Complexity: O(log N).
   - Space Complexity: O(1)."""
    
    answer = """# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(n: int) -> int:
    low = 1
    high = n
    
    while low < high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
            
    return low"""

    boilerplate = {
        "python": "import sys\n\nbad_global = 0\n\ndef isBadVersion(version: int) -> bool:\n    return version >= bad_global\n\ndef firstBadVersion(n: int) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        n = int(lines[0])\n        bad_global = int(lines[1])\n        print(firstBadVersion(n))",
        "cpp": "#include <iostream>\nusing namespace std;\n\nint BAD;\nbool isBadVersion(int version) { return version >= BAD; }\n\nint firstBadVersion(int n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    cin >> n >> BAD;\n    cout << firstBadVersion(n) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    static int BAD;\n    boolean isBadVersion(int version) { return version >= BAD; }\n    public int firstBadVersion(int n) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        BAD = sc.nextInt();\n        System.out.println(new Solution().firstBadVersion(n));\n    }\n}",
        "javascript": "const fs = require('fs');\nconst lines = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nconst n = parseInt(lines[0]);\nconst BAD = parseInt(lines[1]);\nfunction isBadVersion(v) { return v >= BAD; }\n\nfunction firstBadVersion(n) {\n    // User logic\n    return 0;\n}\n\nconsole.log(firstBadVersion(n));",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n\nint BAD;\nbool isBadVersion(int version) { return version >= BAD; }\n\nint firstBadVersion(int n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    scanf(\"%d %d\", &n, &BAD);\n    printf(\"%d\\n\", firstBadVersion(n));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "5\\n4", "expected_output": "4", "is_sample": True},
        {"input": "1\\n1", "expected_output": "1", "is_sample": True},
        {"input": "2\\n1", "expected_output": "1", "is_sample": True},
        {"input": "2\\n2", "expected_output": "2", "is_sample": False},
        {"input": "100\\n50", "expected_output": "50", "is_sample": False},
        {"input": "100\\n1", "expected_output": "1", "is_sample": False},
        {"input": "100\\n100", "expected_output": "100", "is_sample": False},
        # Stress cases
        {"input": "2147483647\\n2147483647", "expected_output": "2147483647", "is_sample": False},
        {"input": "2147483647\\n1", "expected_output": "1", "is_sample": False},
        {"input": "2147483647\\n1073741824", "expected_output": "1073741824", "is_sample": False}
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
        "topics": ["Binary Search", "Interactive"],
        "companyIndex": 0
    }

    output_path = "1-200/278_First_Bad_Version.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
