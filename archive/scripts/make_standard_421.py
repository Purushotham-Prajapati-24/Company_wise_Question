import json
import os

def generate_json():
    problem_id = 421
    title = "Maximum XOR of Two Numbers in an Array"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>421. Maximum XOR of Two Numbers in an Array</h3>
<p>Given an integer array <code>nums</code>, return <em>the maximum result of </em><code>nums[i] XOR nums[j]</code>, where <code>0 &lt;= i &lt;= j &lt; n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,10,5,25,2,8]
<strong>Output:</strong> 28
<strong>Explanation:</strong> The maximum result is 5 XOR 25 = 28.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [14,70,53,83,49,91,36,80,92,51,66,70]
<strong>Output:</strong> 127
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "An array of integers nums."
    output_format = "An integer representing the maximum XOR result."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def findMaximumXOR(nums):
    max_xor = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = {num & mask for num in nums}
        
        target = max_xor | (1 << i)
        for p in prefixes:
            if (p ^ target) in prefixes:
                max_xor = target
                break
    return max_xor"""

    boilerplate = {
        "python": "import sys\n\ndef findMaximumXOR(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    nums = input_data[0].strip() if len(input_data) > 0 else \"\"\n    print(findMaximumXOR(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint findMaximumXOR(string nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string nums; cin >> nums;\n    cout << findMaximumXOR(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "[3,10,5,25,2,8]", "expected_output": "28", "is_sample": True},
        {"input": "[14,70,53,83,49,91,36,80,92,51,66,70]", "expected_output": "127", "is_sample": True},
        {"input": "[0]", "expected_output": "0", "is_sample": False},
        {"input": "[1,2,3,4,5]", "expected_output": "7", "is_sample": False},
        {"input": "[8,10,2]", "expected_output": "10", "is_sample": False},
        {"input": "[100,200,300]", "expected_output": "484", "is_sample": False},
        {"input": "[1,1,1,1]", "expected_output": "0", "is_sample": False},]

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
