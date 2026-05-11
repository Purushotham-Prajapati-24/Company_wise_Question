import json
import os

def generate_json():
    problem_id = 80
    title = "Remove Duplicates from Sorted Array II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>80. Remove Duplicates from Sorted Array II</h3>
<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove some duplicates <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> such that each unique element appears <strong>at most twice</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>

<p>Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong>first part</strong> of the array <code>nums</code>. More formally, if there are <code>k</code> elements after removing the duplicates, then the first <code>k</code> elements of <code>nums</code> should hold the final result. It does not matter what you leave beyond the first <code>k</code> elements.</p>

<p>Return <code>k</code><em> after placing the final result in the first </em><code>k</code><em> slots of </em><code>nums</code>.</p>

<p>Do <strong>not</strong> allocate extra space for another array. You must do this by <strong>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3]
<strong>Output:</strong> 5, nums = [1,1,2,2,3,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2, and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,0,1,1,1,1,2,3,3]
<strong>Output:</strong> 7, nums = [0,0,1,1,2,3,3,_,_]
<strong>Explanation:</strong> Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3, and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>"""

    input_format = "A single line containing n followed by n integers, or just space-separated integers. We'll use space-separated integers for simplicity in the STDIN parsing."
    output_format = "The count k, followed by the first k elements of the modified array."
    
    constraints = [
        "1 <= nums.length <= 3 * 10^4",
        "-10^4 <= nums[i] <= 10^4",
        "nums is sorted in non-decreasing order."
    ]
    
    explanation = """To remove duplicates from a sorted array such that each element appears at most twice:
1. **Two Pointers Approach**:
   - Use a pointer `k` to track the position where the next valid element should be placed.
   - Iterate through the array with a pointer/variable `n`.
   - For each element `n`:
     - If `k < 2` (first two elements are always kept) or `n > nums[k-2]` (current element is different from the one two positions back), it means this element is allowed.
     - Place `n` at `nums[k]` and increment `k`.
   - The key insight is that since the array is sorted, if `n` is greater than `nums[k-2]`, it must be distinct from at least one of the previous two slots, ensuring no more than two occurrences of the same value.
2. **Complexity**:
   - Time Complexity: O(N) where N is the length of the array.
   - Space Complexity: O(1) as modifications are done in-place."""
    
    answer = """def removeDuplicates(nums):
    if not nums: return 0
    k = 0
    for n in nums:
        if k < 2 or n > nums[k-2]:
            nums[k] = n
            k += 1
    return k"""

    boilerplate = {
        "python": "import sys, re\n\ndef removeDuplicates(nums):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    k = removeDuplicates(nums)\n    print(k)\n    print(*(nums[:k]))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int removeDuplicates(vector<int>& nums) {\n        // User Logic Here\n        return 0;\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(\"-?\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    vector<int> nums;\n    while(iter != end) { nums.push_back(stoi((*iter).str())); iter++; }\n    Solution sol;\n    int k = sol.removeDuplicates(nums);\n    cout << k << endl;\n    for(int i=0; i<k; i++) cout << nums[i] << (i == k-1 ? \"\" : \" \");\n    cout << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int removeDuplicates(int[] nums) {\n        // User Logic Here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        List<Integer> list = new ArrayList<>();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        while (m.find()) list.add(Integer.parseInt(m.group()));\n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        int k = new Solution().removeDuplicates(nums);\n        System.out.println(k);\n        for (int i = 0; i < k; i++) System.out.print(nums[i] + (i == k - 1 ? \"\" : \" \"));\n        System.out.println();\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number[]} nums\n * @return {number}\n */\nvar removeDuplicates = function(nums) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    const nums = (input.match(/-?\\d+/g) || []).map(Number);\n    const k = removeDuplicates(nums);\n    console.log(k);\n    console.log(nums.slice(0, k).join(' '));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint removeDuplicates(int* nums, int numsSize) {\n    // User Logic Here\n    return 0;\n}\n\nint main() {\n    int* nums = malloc(30001 * sizeof(int));\n    int count = 0;\n    while (scanf(\"%d\", &nums[count]) == 1) count++;\n    int k = removeDuplicates(nums, count);\n    printf(\"%d\\n\", k);\n    for (int i = 0; i < k; i++) printf(\"%d%s\", nums[i], (i == k - 1 ? \"\" : \" \"));\n    printf(\"\\n\");\n    free(nums);\n    return 0;\n}"
    }

    def _solve(nums):
        if not nums: return 0, []
        k = 0
        arr = list(nums)
        for n in arr:
            if k < 2 or n > arr[k-2]:
                arr[k] = n
                k += 1
        return k, arr[:k]

    def format_output(res):
        k, arr = res
        return f"{k}\n" + " ".join(map(str, arr))

    test_cases = [
        {"input": "1 1 1 2 2 3", "expected_output": format_output(_solve([1,1,1,2,2,3])), "is_sample": True},
        {"input": "0 0 1 1 1 1 2 3 3", "expected_output": format_output(_solve([0,0,1,1,1,1,2,3,3])), "is_sample": True},
        {"input": "1 1 1 1", "expected_output": format_output(_solve([1,1,1,1])), "is_sample": False},
        {"input": "1 2 3", "expected_output": format_output(_solve([1,2,3])), "is_sample": False},
        {"input": "10", "expected_output": format_output(_solve([10])), "is_sample": False},
        {"input": "1 1 2 2 3 3", "expected_output": format_output(_solve([1,1,2,2,3,3])), "is_sample": False},
        {"input": "1 1 1 2 2 2 3 3 3", "expected_output": format_output(_solve([1,1,1,2,2,2,3,3,3])), "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"] * 1000), "expected_output": format_output(_solve([1] * 1000)), "is_sample": False},
        {"input": " ".join(map(str, range(1000))), "expected_output": format_output(_solve(list(range(1000)))), "is_sample": False},
        {"input": " ".join([str(i) for i in range(500) for _ in range(3)]), "expected_output": format_output(_solve([i for i in range(500) for _ in range(3)])), "is_sample": False}
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

    output_path = "1-200/80_Remove_Duplicates_from_Sorted_Array_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
