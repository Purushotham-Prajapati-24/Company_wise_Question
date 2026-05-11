import json
import os

def generate_json():
    problem_id = 27
    title = "Remove Element"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>27. Remove Element</h3>
<p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong>. The order of the elements may be changed. Then return <em>the number of elements in </em><code>nums</code><em> which are not equal to </em><code>val</code>.</p>
<p>Consider the number of elements in <code>nums</code> which are not equal to <code>val</code> be <code>k</code>, to get accepted, you need to do the following things:</p>
<ul>
	<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the elements which are not equal to <code>val</code>. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
	<li>Return <code>k</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [3,2,2,3], val = 3
<strong>Output:</strong> 2, nums = [2,2,_,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [0,1,2,2,3,0,4,2], val = 2
<strong>Output:</strong> 5, nums = [0,1,4,0,3,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 100</code></li>
</ul>"""

    input_format = "Line 1: A list of integers representing the array. Line 2: An integer val."
    output_format = "The number of elements not equal to val (k)."
    
    constraints = [
        "0 <= nums.length <= 100",
        "0 <= nums[i] <= 50",
        "0 <= val <= 100"
    ]
    
    explanation = """Use two pointers: i to track the current element and k to track the position of the next element not equal to val.
Iterate through the array. Whenever an element is not equal to val, place it at index k and increment k.
Return k."""
    
    answer = """def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef removeElement(nums, val):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if not input_data: sys.exit()\n    \n    nums_raw = input_data[0].strip()\n    val_raw = input_data[1].strip() if len(input_data) > 1 else \"0\"\n    \n    nums = [int(x) for x in re.findall(r'-?\\d+', nums_raw)]\n    val = int(re.search(r'-?\\d+', val_raw).group())\n    \n    k = removeElement(nums, val)\n    print(k)",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nint removeElement(vector<int>& nums, int val) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line1, line2;\n    if (!getline(cin, line1)) return 0;\n    if (!getline(cin, line2)) line2 = \"0\";\n    \n    for (char &c : line1) if (c == '[' || c == ']' || c == ',') c = ' ';\n    stringstream ss1(line1);\n    string part;\n    vector<int> nums;\n    while (ss1 >> part) {\n        if (part == \"nums\" || part == \"=\") continue;\n        nums.push_back(stoi(part));\n    }\n    \n    for (char &c : line2) if (c == 'v' || c == 'a' || c == 'l' || c == '=') c = ' ';\n    stringstream ss2(line2);\n    int val; ss2 >> val;\n    \n    int k = removeElement(nums, val);\n    cout << k << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int removeElement(int[] nums, int val) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line1 = sc.nextLine().replaceAll(\"[\\\\[\\\\]=,nums]\", \" \").trim();\n        String[] parts = line1.split(\"\\\\s+\");\n        List<Integer> list = new ArrayList<>();\n        for (String p : parts) if (!p.isEmpty()) list.add(Integer.parseInt(p));\n        int[] nums = new int[list.size()];\n        for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n        \n        int val = 0;\n        if (sc.hasNextLine()) {\n            String line2 = sc.nextLine().replaceAll(\"[^0-9-]\", \"\").trim();\n            if (!line2.isEmpty()) val = Integer.parseInt(line2);\n        }\n        \n        int k = removeElement(nums, val);\n        System.out.println(k);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction removeElement(nums, val) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length === 0) process.exit(0);\n\nconst nums_raw = input[0];\nconst val_raw = input[1] || \"0\";\n\nconst nums = (nums_raw.match(/-?\\d+/g) || []).map(Number);\nconst val = parseInt(val_raw.match(/-?\\d+/)[0]);\n\nconst k = removeElement(nums, val);\nconsole.log(k);",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\nint removeElement(int* nums, int numsSize, int val) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char line1[10000], line2[100];\n    if (!fgets(line1, sizeof(line1), stdin)) return 0;\n    if (!fgets(line2, sizeof(line2), stdin)) strcpy(line2, \"0\");\n    \n    int* nums = malloc(10000 * sizeof(int));\n    int numsSize = 0;\n    char* p = line1;\n    while (*p) {\n        while (*p && !isdigit(*p) && *p != '-') p++;\n        if (*p) {\n            nums[numsSize++] = atoi(p);\n            if (*p == '-') p++;\n            while (*p && isdigit(*p)) p++;\n        }\n    }\n    \n    int val = 0;\n    p = line2;\n    while (*p && !isdigit(*p) && *p != '-') p++;\n    if (*p) val = atoi(p);\n    \n    int k = removeElement(nums, numsSize, val);\n    printf(\"%d\\n\", k);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[3,2,2,3]\n3", "expected_output": "2", "is_sample": True},
        {"input": "[0,1,2,2,3,0,4,2]\n2", "expected_output": "5", "is_sample": True},
        {"input": "[1,2,3,4,5]\n6", "expected_output": "5", "is_sample": False},
        {"input": "[1,1,1,1]\n1", "expected_output": "0", "is_sample": False},
        {"input": "[]\n0", "expected_output": "0", "is_sample": False},
        {"input": "[1]\n1", "expected_output": "0", "is_sample": False},
        {"input": "[1]\n2", "expected_output": "1", "is_sample": False},
        {"input": "[2,2,2]\n2", "expected_output": "0", "is_sample": False},
        {"input": "[1,2,3,4,5]\n3", "expected_output": "4", "is_sample": False},
        {"input": "[5,5,5,5,5]\n5", "expected_output": "0", "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
        "question_title": title,
        "difficulty": difficulty,
        "marks": marks,
        "question_text": html_description,
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

    output_path = "1-200/27_Remove_Element.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
