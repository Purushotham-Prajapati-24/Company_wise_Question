import json
import os

def generate_json():
    problem_id = 163
    title = "Missing Ranges"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>163. Missing Ranges</h3>
<p>You are given an inclusive range <code>[lower, upper]</code> and a <strong>sorted unique</strong> integer array <code>nums</code>, where all elements are within the inclusive range.</p>

<p>A number <code>x</code> is considered <strong>missing</strong> if <code>x</code> is in the range <code>[lower, upper]</code> and <code>x</code> is not in <code>nums</code>.</p>

<p>Return <em>the <strong>shortest sorted</strong> list of ranges that <strong>exactly covers all the missing numbers</strong></em>. That is, no element of <code>nums</code> is included in any of the ranges, and each missing number is covered by one of the ranges.</p>

<p>Each range <code>[a, b]</code> in the list should be output as:</p>
<ul>
	<li><code>"a->b"</code> if <code>a != b</code></li>
	<li><code>"a"</code> if <code>a == b</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,3,50,75], lower = 0, upper = 99
<strong>Output:</strong> ["2","4->49","51->74","76->99"]
<strong>Explanation:</strong> The ranges are:
[2,2] --&gt; "2"
[4,49] --&gt; "4-&gt;49"
[51,74] --&gt; "51-&gt;74"
[76,99] --&gt; "76-&gt;99"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1], lower = -1, upper = -1
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no missing numbers as nums covers the entire range.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>9</sup> &lt;= lower &lt;= upper &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>lower &lt;= nums[i] &lt;= upper</code></li>
	<li>All the values of <code>nums</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "Three lines. Line 1: space-separated integers nums. Line 2: integer lower. Line 3: integer upper."
    output_format = "A JSON list of strings representing the missing ranges."
    
    constraints = [
        "-10^9 <= lower <= upper <= 10^9",
        "0 <= nums.length <= 100",
        "lower <= nums[i] <= upper",
        "nums is sorted and unique."
    ]
    
    explanation = """To find the missing ranges within [lower, upper]:
1. **Helper Function**:
   - Define a function `getRange(start, end)` that returns "start" if `start == end`, and "start->end" otherwise.
2. **Logic**:
   - Initialize `next_val = lower`.
   - Iterate through each number `n` in `nums`:
     - If `n > next_val`, it means there's a missing range from `next_val` to `n - 1`. Add it to the result.
     - Update `next_val = n + 1`.
   - After the loop, if `next_val <= upper`, there's a final missing range from `next_val` to `upper`. Add it to the result.
3. **Complexity**:
   - Time Complexity: O(N) where N is the length of `nums`.
   - Space Complexity: O(N) to store the result ranges."""
    
    answer = """def findMissingRanges(nums, lower, upper):
    def get_range(start, end):
        if start == end:
            return str(start)
        return str(start) + "->" + str(end)
        
    res = []
    next_val = lower
    
    for n in nums:
        if n > next_val:
            res.append(get_range(next_val, n - 1))
        next_val = n + 1
        
    if next_val <= upper:
        res.append(get_range(next_val, upper))
        
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef findMissingRanges(nums, lower, upper):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    nums = []\n    if len(lines) > 0 and lines[0].strip():\n        nums = list(map(int, lines[0].split()))\n    lower = int(lines[1]) if len(lines) > 1 and lines[1].strip() else 0\n    upper = int(lines[2]) if len(lines) > 2 and lines[2].strip() else 0\n    res = findMissingRanges(nums, lower, upper)\n    if res is None:\n        res = []\n    print(json.dumps(res))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\nusing namespace std;\nvector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {\n    // User logic here\n    return {};\n}\nint main() {\n    string line;\n    vector<int> nums;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int x;\n        while (ss >> x) nums.push_back(x);\n    }\n    int lower = 0, upper = 0;\n    if (getline(cin, line)) lower = stoi(line);\n    if (getline(cin, line)) upper = stoi(line);\n    vector<string> res = findMissingRanges(nums, lower, upper);\n    cout << \"[\";\n    for(size_t i=0; i<res.size(); ++i) {\n        cout << \"\\\"\" << res[i] << \"\\\"\";\n        if(i < res.size()-1) cout << \",\";\n    }\n    cout << \"]\\n\";\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\npublic class Main {\n    public static List<String> findMissingRanges(int[] nums, int lower, int upper) {\n        // User logic here\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) throws Exception {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        List<Integer> list = new ArrayList<>();\n        if (line1 != null && !line1.trim().isEmpty()) {\n            String[] parts = line1.trim().split(\"\\\\s+\");\n            for (String p : parts) list.add(Integer.parseInt(p));\n        }\n        int[] nums = new int[list.size()];\n        for(int i=0; i<list.size(); i++) nums[i] = list.get(i);\n        String line2 = br.readLine();\n        int lower = (line2 != null && !line2.trim().isEmpty()) ? Integer.parseInt(line2.trim()) : 0;\n        String line3 = br.readLine();\n        int upper = (line3 != null && !line3.trim().isEmpty()) ? Integer.parseInt(line3.trim()) : 0;\n        List<String> res = findMissingRanges(nums, lower, upper);\n        if (res == null) res = new ArrayList<>();\n        System.out.print(\"[\");\n        for(int i=0; i<res.size(); i++) {\n            System.out.print(\"\\\"\" + res.get(i) + \"\\\"\");\n            if(i < res.size()-1) System.out.print(\",\");\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction findMissingRanges(nums, lower, upper) {\n    // User logic here\n    return [];\n}\nconst lines = fs.readFileSync(0, 'utf8').split('\\n');\nlet nums = [];\nif (lines.length > 0 && lines[0].trim() !== '') {\n    nums = lines[0].trim().split(/\\s+/).map(Number);\n}\nlet lower = lines.length > 1 && lines[1].trim() !== '' ? parseInt(lines[1], 10) : 0;\nlet upper = lines.length > 2 && lines[2].trim() !== '' ? parseInt(lines[2], 10) : 0;\nconst res = findMissingRanges(nums, lower, upper);\nconsole.log(JSON.stringify(res || []));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nchar** findMissingRanges(int* nums, int numsSize, int lower, int upper, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\nint main() {\n    char line[100000];\n    int capacity = 1000;\n    int* nums = (int*)malloc(capacity * sizeof(int));\n    int numsSize = 0;\n    if (fgets(line, sizeof(line), stdin)) {\n        char* token = strtok(line, \" \\t\\r\\n\");\n        while (token != NULL) {\n            if (numsSize >= capacity) {\n                capacity *= 2;\n                nums = (int*)realloc(nums, capacity * sizeof(int));\n            }\n            nums[numsSize++] = atoi(token);\n            token = strtok(NULL, \" \\t\\r\\n\");\n        }\n    }\n    int lower = 0, upper = 0;\n    if (fgets(line, sizeof(line), stdin)) lower = atoi(line);\n    if (fgets(line, sizeof(line), stdin)) upper = atoi(line);\n    int returnSize = 0;\n    char** res = findMissingRanges(nums, numsSize, lower, upper, &returnSize);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"\\\"%s\\\"\", res[i]);\n        if (i < returnSize - 1) printf(\",\");\n        free(res[i]);\n    }\n    printf(\"]\\n\");\n    free(res);\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "0 1 3 50 75\\n0\\n99", "expected_output": "[\"2\", \"4->49\", \"51->74\", \"76->99\"]", "is_sample": True},
        {"input": "-1\\n-1\\n-1", "expected_output": "[]", "is_sample": True},
        {"input": "\\n1\\n1", "expected_output": "[\"1\"]", "is_sample": False},
        {"input": "\\n-10\\n10", "expected_output": "[\"-10->10\"]", "is_sample": False},
        {"input": "5\\n0\\n10", "expected_output": "[\"0->4\", \"6->10\"]", "is_sample": False},
        {"input": "0 10\\n0\\n10", "expected_output": "[\"1->9\"]", "is_sample": False},
        {"input": "0\\n0\\n0", "expected_output": "[]", "is_sample": False},
        # Stress cases
        {"input": "\\n-1000000000\\n1000000000", "expected_output": "[\"-1000000000->1000000000\"]", "is_sample": False},
        {"input": (" ".join([str(i) for i in range(100)])) + "\\n0\\n100", "expected_output": "[\"100\"]", "is_sample": False},
        {"input": (" ".join([str(i*2) for i in range(50)])) + "\\n0\\n100", "expected_output": json.dumps([str(i*2+1) if i*2+1 == i*2+1 else "" for i in range(50)] + ["99->100"]).replace('""', ''), "is_sample": False}
    ]
    
    # Manual fix for last few test cases expected output
    test_cases[9]["expected_output"] = json.dumps([str(i*2+1) for i in range(50)] + ["99->100"]) # Wait, if nums is [0, 2, ..., 98], upper is 100. ranges are 1, 3, ..., 99->100.
    test_cases[9]["expected_output"] = json.dumps([str(i*2+1) for i in range(49)] + ["99->100"])

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
        "topics": ["Array", "Simulation"],
        "companyIndex": 0
    }

    output_path = "1-200/163_Missing_Ranges.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
