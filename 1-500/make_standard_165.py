import json
import os

def generate_json():
    problem_id = 165
    title = "Compare Version Numbers"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>165. Compare Version Numbers</h3>
<p>Given two version strings, <code>version1</code> and <code>version2</code>, compare them. A version string consists of <strong>revision numbers</strong> separated by dots <code>'.'</code>. The revision numbers are compared as <strong>integers</strong>, ignoring any leading zeros.</p>

<p>To compare two versions, compare their revision numbers from left to right. If a version string has fewer revisions than the other, treat the missing revision values as <code>0</code>.</p>

<p>Return the following:</p>

<ul>
	<li>If <code>version1 &lt; version2</code>, return <code>-1</code>.</li>
	<li>If <code>version1 &gt; version2</code>, return <code>1</code>.</li>
	<li>Otherwise, return <code>0</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> version1 = "1.2", version2 = "1.10"
<strong>Output:</strong> -1
<strong>Explanation:</strong>
version1's second revision is "2", version2's second revision is "10".
2 &lt; 10, so version1 &lt; version2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> version1 = "1.01", version2 = "1.001"
<strong>Output:</strong> 0
<strong>Explanation:</strong>
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> version1 = "1.0", version2 = "1.0.0.0"
<strong>Output:</strong> 0
<strong>Explanation:</strong>
version1 has fewer revisions, which means the missing revisions are treated as "0".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= version1.length, version2.length &lt;= 500</code></li>
	<li><code>version1</code> and <code>version2</code>&nbsp;only contain digits and <code>'.'</code>.</li>
	<li><code>version1</code> and <code>version2</code> are <strong>valid version numbers</strong>.</li>
	<li>All the given revisions in <code>version1</code> and <code>version2</code> can be stored in a <strong>32-bit integer</strong>.</li>
</ul>"""

    input_format = "Two lines. Line 1: version1. Line 2: version2."
    output_format = "An integer representing the comparison result (-1, 0, or 1)."
    
    constraints = [
        "1 <= version1.length, version2.length <= 500",
        "Valid version format (digits and dots).",
        "Handle missing revisions as 0."
    ]
    
    explanation = """To compare two version strings efficiently:
1. **Split by Dots**: Divide each version string into a list of its revision numbers using the dot (`.`) as a separator.
2. **Iterate through Revisions**:
   - Loop from 0 to the maximum number of revisions present in either string.
   - For each index `i`:
     - Get the numeric value of the revision at index `i`.
     - If the index is beyond the length of a string, assume the value is `0`.
     - Compare the two values:
       - If `v1 < v2`, return `-1`.
       - If `v1 > v2`, return `1`.
3. **Completion**:
   - If the loop finishes without finding a difference, return `0`.
4. **Complexity**:
   - Time Complexity: O(N + M + max(L1, L2)) where N, M are lengths of the strings and L1, L2 are the number of revisions.
   - Space Complexity: O(L1 + L2) to store the lists of revisions."""
    
    answer = """def compareVersion(version1: str, version2: str) -> int:
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    
    n1, n2 = len(v1), len(v2)
    max_len = max(n1, n2)
    
    for i in range(max_len):
        val1 = v1[i] if i < n1 else 0
        val2 = v2[i] if i < n2 else 0
        
        if val1 < val2:
            return -1
        if val1 > val2:
            return 1
            
    return 0"""

    boilerplate = {
        "python": "import sys\n\ndef compareVersion(version1, version2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    v1 = lines[0] if len(lines) > 0 else \"\"\n    v2 = lines[1] if len(lines) > 1 else \"\"\n    print(compareVersion(v1, v2))",
        "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\nint compareVersion(string version1, string version2) {\n    // User logic here\n    return 0;\n}\nint main() {\n    string v1, v2;\n    if (getline(cin, v1)) { if (!v1.empty() && v1.back() == '\\r') v1.pop_back(); }\n    if (getline(cin, v2)) { if (!v2.empty() && v2.back() == '\\r') v2.pop_back(); }\n    cout << compareVersion(v1, v2) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\npublic class Main {\n    public static int compareVersion(String version1, String version2) {\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String v1 = br.readLine(); if (v1 == null) v1 = \"\";\n        String v2 = br.readLine(); if (v2 == null) v2 = \"\";\n        System.out.println(compareVersion(v1, v2));\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction compareVersion(version1, version2) {\n    // User logic here\n    return 0;\n}\nconst lines = fs.readFileSync(0, 'utf8').split('\\n');\nlet v1 = lines.length > 0 ? lines[0] : \"\";\nif (v1.endsWith('\\r')) v1 = v1.slice(0, -1);\nlet v2 = lines.length > 1 ? lines[1] : \"\";\nif (v2.endsWith('\\r')) v2 = v2.slice(0, -1);\nconsole.log(compareVersion(v1, v2));",
        "c": "#include <stdio.h>\n#include <string.h>\nint compareVersion(char* version1, char* version2) {\n    // User logic here\n    return 0;\n}\nint main() {\n    char v1[1005] = {0}, v2[1005] = {0};\n    if (fgets(v1, sizeof(v1), stdin)) {\n        int l = strlen(v1);\n        while (l > 0 && (v1[l-1] == '\\n' || v1[l-1] == '\\r')) v1[--l] = '\\0';\n    }\n    if (fgets(v2, sizeof(v2), stdin)) {\n        int l = strlen(v2);\n        while (l > 0 && (v2[l-1] == '\\n' || v2[l-1] == '\\r')) v2[--l] = '\\0';\n    }\n    printf(\"%d\\n\", compareVersion(v1, v2));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1.2\\n1.10", "expected_output": "-1", "is_sample": True},
        {"input": "1.01\\n1.001", "expected_output": "0", "is_sample": True},
        {"input": "1.0\\n1.0.0.0", "expected_output": "0", "is_sample": True},
        {"input": "7.5.2.4\\n7.5.3", "expected_output": "-1", "is_sample": False},
        {"input": "1.0.1\\n1", "expected_output": "1", "is_sample": False},
        {"input": "0.1\\n1.1", "expected_output": "-1", "is_sample": False},
        {"input": "1.1\\n1.10", "expected_output": "-1", "is_sample": False},
        # Stress cases
        {"input": "1.0.0.0.0.1\\n1.0", "expected_output": "1", "is_sample": False},
        {"input": ".".join(["0"]*100 + ["1"]) + "\\n" + ".".join(["0"]*100 + ["1"]), "expected_output": "0", "is_sample": False},
        {"input": "1." + "1"*498 + "\\n" + "1." + "1"*498, "expected_output": "0", "is_sample": False}
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
        "topics": ["Two Pointers", "String"],
        "companyIndex": 0
    }

    output_path = "1-200/165_Compare_Version_Numbers.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
