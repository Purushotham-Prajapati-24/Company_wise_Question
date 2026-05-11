import json
import os

def generate_json():
    problem_id = 217
    title = "Contains Duplicate"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>217. Contains Duplicate</h3>
<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,3,3,4,3,2,4,2]
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers for the array nums."
    output_format = "true if the array contains any duplicates, false otherwise."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "-10^9 <= nums[i] <= 10^9",
        "O(N) time complexity expected.",
        "O(N) space complexity expected."
    ]
    
    explanation = """To detect if an array contains any duplicates:
1. **Hash Set Approach**:
   - Create an empty hash set (or hash map) to store seen elements.
   - Iterate through each number in the array:
     - Check if the number already exists in the set.
     - If it does, a duplicate is found; return `true`.
     - Otherwise, add the number to the set and continue.
   - If the loop finishes without finding a duplicate, return `false`.
2. **Alternative (Sorting)**:
   - Sort the array in O(N log N) time.
   - Iterate through the sorted array once and check if any adjacent elements are the same.
   - Return `true` if found, else `false`.
3. **Complexity**:
   - Hash Set: O(N) time, O(N) space.
   - Sorting: O(N log N) time, O(1) or O(N) space depending on the sort implementation."""
    
    answer = """def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef containsDuplicate(nums):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', raw_input)]\n    if nums:\n        print(\"true\" if containsDuplicate(nums) else \"false\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nbool containsDuplicate(vector<int>& nums) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    string input;\n    string line;\n    while (getline(cin, line)) input += line + \" \";\n    regex re(\"-?\\\\d+\");\n    auto words_begin = sregex_iterator(input.begin(), input.end(), re);\n    auto words_end = sregex_iterator();\n    vector<int> nums;\n    for (sregex_iterator i = words_begin; i != words_end; ++i) {\n        nums.push_back(stoi(i->str()));\n    }\n    if (!nums.empty()) {\n        cout << (containsDuplicate(nums) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public boolean containsDuplicate(int[] nums) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        Pattern p = Pattern.compile(\"-?\\\\d+\");\n        Matcher m = p.matcher(sb.toString());\n        List<Integer> list = new ArrayList<>();\n        while (m.find()) {\n            list.add(Integer.parseInt(m.group()));\n        }\n        if (!list.isEmpty()) {\n            int[] nums = new int[list.size()];\n            for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n            System.out.println(new Solution().containsDuplicate(nums) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction containsDuplicate(nums) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst nums = (input.match(/-?\\d+/g) || []).map(Number);\nif (nums.length > 0) {\n    console.log(containsDuplicate(nums) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <ctype.h>\n\nbool containsDuplicate(int* nums, int numsSize) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    int cap = 100000, size = 0;\n    int* nums = (int*)malloc(cap * sizeof(int));\n    static char buffer[1000000];\n    int bytesRead = fread(buffer, 1, sizeof(buffer) - 1, stdin);\n    buffer[bytesRead] = '\\0';\n    char* ptr = buffer;\n    while (*ptr) {\n        if (isdigit(*ptr) || (*ptr == '-' && isdigit(*(ptr + 1)))) {\n            if (size >= cap) { cap *= 2; nums = (int*)realloc(nums, cap * sizeof(int)); }\n            nums[size++] = (int)strtol(ptr, &ptr, 10);\n        } else {\n            ptr++;\n        }\n    }\n    if (size > 0) {\n        printf(\"%s\\n\", containsDuplicate(nums, size) ? \"true\" : \"false\");\n    }\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 1", "expected_output": "true", "is_sample": True},
        {"input": "1 2 3 4", "expected_output": "false", "is_sample": True},
        {"input": "1 1 1 3 3 4 3 2 4 2", "expected_output": "true", "is_sample": True},
        {"input": "0", "expected_output": "false", "is_sample": False},
        {"input": "1 -1 2 -2", "expected_output": "false", "is_sample": False},
        {"input": "1000000 1000000", "expected_output": "true", "is_sample": False},
        {"input": "1 " + " ".join([str(i) for i in range(2, 101)]) + " 1", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(100000)]), "expected_output": "false", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100000)] + ["0"]), "expected_output": "true", "is_sample": False},
        {"input": " ".join(["42"]*100000), "expected_output": "true", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/217_Contains_Duplicate.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
