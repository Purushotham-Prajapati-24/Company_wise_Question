import json
import os

def generate_json():
    problem_id = 75
    title = "Sort Colors"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>75. Sort Colors</h3>
<p>Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> </strong>so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>

<p>We will use the integers <code>0</code>, <code>1</code>, and <code>2</code> to represent the color red, white, and blue, respectively.</p>

<p>You must solve this problem without using the library's sort function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,0,1]
<strong>Output:</strong> [0,1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> is either <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you come up with a one-pass algorithm using only constant extra space?</p>"""

    input_format = "A single line containing space-separated integers representing colors (0, 1, 2)."
    output_format = "A single line containing the sorted colors separated by space."
    
    constraints = [
        "1 <= n <= 300",
        "nums[i] is 0, 1, or 2.",
        "Must sort in-place without built-in sort functions.",
        "One-pass O(n) time and O(1) space preferred."
    ]
    
    explanation = """To sort colors (0s, 1s, and 2s) in a single pass with constant space:
1. **Dutch National Flag Algorithm**: Use three pointers to partition the array into four sections: 0s, 1s, unknown, and 2s.
   - `low`: Points to the next position for 0.
   - `mid`: Points to the current element being processed.
   - `high`: Points to the next position for 2.
2. **Algorithm**:
   - Initialize `low = 0`, `mid = 0`, and `high = n - 1`.
   - While `mid <= high`:
     - If `nums[mid] == 0`: Swap `nums[low]` and `nums[mid]`, then increment both `low` and `mid`.
     - If `nums[mid] == 1`: Already in the correct middle section, just increment `mid`.
     - If `nums[mid] == 2`: Swap `nums[mid]` and `nums[high]`, then decrement `high`. Do NOT increment `mid` yet, as the new `nums[mid]` needs to be evaluated.
3. **Complexity**:
   - Time Complexity: O(n), as each element is visited at most once.
   - Space Complexity: O(1), for the three pointers."""
    
    answer = """def sortColors(nums):
    # Dutch National Flag Algorithm
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            # Move 0 to the low section
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # 1 is already in the correct relative section
            mid += 1
        else:
            # Move 2 to the high section
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Do not increment mid, need to check the swapped value
    return nums"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys, re\n\ndef sortColors(nums):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    nums = [int(x) for x in re.findall(r'\\d+', data)]\n    sortColors(nums)\n    print('[' + ', '.join(map(str, nums)) + ']')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    void sortColors(vector<int>& nums) {\n        // User Logic Here\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(\"\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    vector<int> nums;\n    while(iter != end) { nums.push_back(stoi((*iter).str())); iter++; }\n    Solution sol;\n    sol.sortColors(nums);\n    cout << \"[\";\n    for(int i=0; i<nums.size(); i++) cout << nums[i] << (i == nums.size()-1 ? \"\" : \", \");\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public void sortColors(int[] nums) {\n        // User Logic Here\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        List<Integer> list = new ArrayList<>();\n        Matcher m = Pattern.compile(\"\\\\d+\").matcher(input);\n        while (m.find()) list.add(Integer.parseInt(m.group()));\n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        new Solution().sortColors(nums);\n        System.out.print(\"[\");\n        for (int i = 0; i < nums.length; i++) {\n            System.out.print(nums[i] + (i == nums.length - 1 ? \"\" : \", \"));\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number[]} nums\n * @return {void} Do not return anything, modify nums in-place instead.\n */\nvar sortColors = function(nums) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    const nums = (input.match(/\\d+/g) || []).map(Number);\n    sortColors(nums);\n    console.log(JSON.stringify(nums).replace(/,/g, ', '));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nvoid sortColors(int* nums, int numsSize) {\n    // User Logic Here\n}\n\nint main() {\n    int* nums = malloc(1000 * sizeof(int));\n    int count = 0;\n    while (scanf(\"%d\", &nums[count]) == 1) count++;\n    sortColors(nums, count);\n    printf(\"[\");\n    for (int i = 0; i < count; i++) printf(\"%d%s\", nums[i], (i == count - 1 ? \"\" : \", \"));\n    printf(\"]\\n\");\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "2 0 2 1 1 0", "expected_output": "0 0 1 1 2 2", "is_sample": True},
        {"input": "2 0 1", "expected_output": "0 1 2", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "2", "expected_output": "2", "is_sample": False},
        {"input": "1 0 2", "expected_output": "0 1 2", "is_sample": False},
        {"input": "0 0 0", "expected_output": "0 0 0", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(["2", "1", "0"] * 100), "expected_output": " ".join(["0"] * 100 + ["1"] * 100 + ["2"] * 100), "is_sample": False},
        {"input": " ".join(["0"] * 100 + ["1"] * 100 + ["2"] * 100), "expected_output": " ".join(["0"] * 100 + ["1"] * 100 + ["2"] * 100), "is_sample": False},
        {"input": " ".join(["2"] * 150 + ["0"] * 150), "expected_output": " ".join(["0"] * 150 + ["2"] * 150), "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/75_Sort_Colors.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
