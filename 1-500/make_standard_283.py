import json
import os

def generate_json():
    problem_id = 283
    title = "Move Zeroes"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>283. Move Zeroes</h3>
<p>Given an integer array <code>nums</code>, move all <code>0</code>'s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<b>Follow up:</b> Could you minimize the total number of operations performed?"""

    input_format = "A single line containing space-separated integers for the array nums."
    output_format = "A single line containing space-separated integers with zeroes moved to the end."
    
    constraints = [
        "1 <= nums.length <= 10^4",
        "-2^31 <= nums[i] <= 2^31 - 1",
        "Must be in-place (O(1) extra space).",
        "Maintain relative order of non-zero elements.",
        "O(N) time complexity."
    ]
    
    explanation = """To move zeroes to the end in-place while maintaining order:
1. **Two Pointers Approach**:
   - Use a pointer `last_non_zero` to track the position where the next non-zero element should be placed.
   - Iterate through the array with a `current` pointer.
   - If `nums[current]` is non-zero:
     - Swap `nums[current]` with `nums[last_non_zero]`.
     - Increment `last_non_zero`.
2. **Advantages**:
   - By swapping, we automatically move the zero found at `last_non_zero` forward and keep the non-zero element at the correct relative position.
   - This minimizes the number of writes compared to a "copy then fill with zeroes" approach if there are many non-zero elements.
3. **Complexity**:
   - Time Complexity: O(N).
   - Space Complexity: O(1)."""
    
    answer = """def moveZeroes(nums: list[int]) -> None:
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1"""

    boilerplate = {
        "python": "import sys\nimport re\nimport json\n\ndef moveZeroes(nums: list[int]) -> None:\n    # User logic here (modify nums in-place)\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    match = re.search(r'\\[([^\\]]*)\\]', raw_input)\n    if match:\n        nums = [int(x) for x in re.findall(r'-?\\d+', match.group(1))]\n    else:\n        nums = [int(x) for x in re.findall(r'-?\\d+', raw_input)]\n    \n    moveZeroes(nums)\n    print(json.dumps(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nvoid moveZeroes(vector<int>& nums) {\n    // User logic here\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    regex re_nums(R\"(\\[([^\\]]*)\\])\");\n    smatch match;\n    vector<int> nums;\n    string target_str = input;\n    if (regex_search(input, match, re_nums)) target_str = match.str(1);\n    \n    regex re_digit(R\"(-?\\d+)\");\n    auto words_begin = sregex_iterator(target_str.begin(), target_str.end(), re_digit);\n    auto words_end = sregex_iterator();\n    for (sregex_iterator i = words_begin; i != words_end; ++i) nums.push_back(stoi(i->str()));\n    \n    moveZeroes(nums);\n    cout << \"[\";\n    for (size_t i = 0; i < nums.size(); i++) {\n        cout << nums[i] << (i == nums.size() - 1 ? \"\" : \",\");\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public void moveZeroes(int[] nums) {\n        // User logic here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        \n        Matcher m = Pattern.compile(\"\\\\[([^\\\\]]*)\\\\]\").matcher(input);\n        String targetStr = input;\n        if (m.find()) targetStr = m.group(1);\n        \n        List<Integer> list = new ArrayList<>();\n        Matcher mNum = Pattern.compile(\"(-?\\\\d+)\").matcher(targetStr);\n        while (mNum.find()) list.add(Integer.parseInt(mNum.group()));\n        \n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        new Solution().moveZeroes(nums);\n        System.out.println(Arrays.toString(nums).replace(\" \", \"\"));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction moveZeroes(nums) {\n    // User logic here\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst match = input.match(/\\[([^\\]]*)\\]/);\nconst targetStr = match ? match[1] : input;\nconst nums = (targetStr.match(/-?\\d+/g) || []).map(Number);\n\nmoveZeroes(nums);\nconsole.log(JSON.stringify(nums));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nvoid moveZeroes(int* nums, int numsSize) {\n    // User logic here\n}\n\nint main() {\n    static char buffer[100000];\n    if (fread(buffer, 1, 99999, stdin) > 0) {\n        int nums[10000];\n        int count = 0;\n        char *p = strchr(buffer, '[');\n        if (!p) p = buffer;\n        while (*p && *p != ']') {\n            if (isdigit(*p) || (*p == '-' && isdigit(*(p+1)))) {\n                nums[count++] = atoi(p);\n                while (*p && (isdigit(*p) || *p == '-')) p++;\n            } else p++;\n        }\n        moveZeroes(nums, count);\n        printf(\"[\");\n        for (int i = 0; i < count; i++) {\n            printf(\"%d%s\", nums[i], (i == count - 1 ? \"\" : \",\"));\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "0 1 0 3 12", "expected_output": "1 3 12 0 0", "is_sample": True},
        {"input": "0", "expected_output": "0", "is_sample": True},
        {"input": "42", "expected_output": "42", "is_sample": True},
        {"input": "0 0 1", "expected_output": "1 0 0", "is_sample": False},
        {"input": "1 0 0", "expected_output": "1 0 0", "is_sample": False},
        {"input": "1 2 3", "expected_output": "1 2 3", "is_sample": False},
        {"input": "0 0 0", "expected_output": "0 0 0", "is_sample": False},
        # Stress cases
        {"input": " ".join(["0"]*10000), "expected_output": " ".join(["0"]*10000), "is_sample": False},
        {"input": " ".join(["1"]*10000), "expected_output": " ".join(["1"]*10000), "is_sample": False},
        {"input": " ".join(["0", "1"]*5000), "expected_output": " ".join(["1"]*5000 + ["0"]*5000), "is_sample": False}
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
        "topics": ["Array", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "201-400/283_Move_Zeroes.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
