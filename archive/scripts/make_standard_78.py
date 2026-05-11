import json
import os

def generate_json():
    problem_id = 78
    title = "Subsets"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>78. Subsets</h3>
<p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible</em> <span data-keyword="subset"><strong><em>subsets</em></strong></span> <em>(the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A single line containing space-separated unique integers."
    output_format = "A list of lists representing the power set (all possible subsets)."
    
    constraints = [
        "1 <= nums.length <= 10",
        "-10 <= nums[i] <= 10",
        "All numbers are unique."
    ]
    
    explanation = """To generate the power set (all possible subsets) of a set of unique elements:
1. **Iterative Approach (Cascading)**:
   - Start with an initial result list containing only the empty subset: `[[]]`.
   - Iterate through each number in the input array `nums`.
   - For each number, iterate through the *existing* subsets in the result list and create a new subset by adding the current number to each.
   - Append these new subsets to the result list.
   - This effectively doubles the number of subsets with each element added.
2. **Backtracking Approach**:
   - Define a recursive function `backtrack(start, current_path)`.
   - Add the `current_path` to the result list.
   - Loop from `start` to the end of `nums`:
     - Add `nums[i]` to `current_path`.
     - Recurse with `backtrack(i + 1, current_path)`.
     - Remove `nums[i]` from `current_path` to backtrack.
3. **Complexity**:
   - Time Complexity: O(N * 2^N), because there are 2^N subsets and we spend O(N) to copy each subset into the final result.
   - Space Complexity: O(N * 2^N) to store the total number of subsets."""
    
    answer = """def subsets(nums):
    res = [[]]
    for n in nums:
        # For every number, create new subsets by adding it to existing ones
        res += [curr + [n] for curr in res]
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef subsets(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        nums = [int(x) for x in data]\n        print(subsets(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<vector<int>> subsets(vector<int>& nums) {\n    // User logic\n    return {};\n}\n\nint main() {\n    int val;\n    vector<int> nums;\n    while (cin >> val) nums.push_back(val);\n    auto res = subsets(nums);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        cout << \"[\";\n        for (int j = 0; j < (int)res[i].size(); j++) {\n            cout << res[i][j];\n            if (j + 1 < (int)res[i].size()) cout << \", \";\n        }\n        cout << \"]\";\n        if (i + 1 < (int)res.size()) cout << \", \";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<Integer>> subsets(int[] nums) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        System.out.println(subsets(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction subsets(nums) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/).map(Number);\nconsole.log(JSON.stringify(subsets(input)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int buff[10], size = 0;\n    while (size < 10 && scanf(\"%d\", &buff[size]) == 1) size++;\n    int returnSize = 0;\n    int* colSizes = NULL;\n    int** res = subsets(buff, size, &returnSize, &colSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"[\");\n        for (int j = 0; j < colSizes[i]; j++) {\n            printf(\"%d\", res[i][j]);\n            if (j + 1 < colSizes[i]) printf(\", \");\n        }\n        printf(\"]\");\n        if (i + 1 < returnSize) printf(\", \");\n        if (res[i]) free(res[i]);\n    }\n    printf(\"]\\n\");\n    if (colSizes) free(colSizes);\n    if (res) free(res);\n    return 0;\n}"
    }

    def _solve(nums):
        res = [[]]
        for n in nums:
            res += [curr + [n] for curr in res]
        return res

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 3", "expected_output": str(_solve([1, 2, 3])), "is_sample": True},
        {"input": "0", "expected_output": str(_solve([0])), "is_sample": True},
        # Middle five: Diverse cases
        {"input": "1 2", "expected_output": str(_solve([1, 2])), "is_sample": False},
        {"input": "-1 1", "expected_output": str(_solve([-1, 1])), "is_sample": False},
        {"input": "10 -10", "expected_output": str(_solve([10, -10])), "is_sample": False},
        {"input": "7 8 9", "expected_output": str(_solve([7, 8, 9])), "is_sample": False},
        {"input": "1 3 5 7", "expected_output": str(_solve([1, 3, 5, 7])), "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(1, 11)]), "expected_output": str(_solve(list(range(1, 11)))), "is_sample": False},
        {"input": " ".join([str(i) for i in range(-5, 5)]), "expected_output": str(_solve(list(range(-5, 5)))), "is_sample": False},
        {"input": "10 9 8 7 6 5 4 3 2 1", "expected_output": str(_solve([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), "is_sample": False}
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
        "topics": ["Array", "Backtracking", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "1-200/78_Subsets.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
