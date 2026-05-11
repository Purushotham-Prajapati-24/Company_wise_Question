import json
import os

def generate_json():
    problem_id = 46
    title = "Permutations"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>46. Permutations</h3>
<p>Given an array <code>nums</code> of distinct integers, return <em>all the possible permutations</em>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [[0,1],[1,0]]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 6</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A single line containing space-separated distinct integers for the array 'nums'."
    output_format = "A list of lists containing all possible permutations of the input array."
    
    constraints = [
        "1 <= nums.length <= 6",
        "-10 <= nums[i] <= 10",
        "All integers in nums are unique."
    ]
    
    explanation = """To generate all permutations of an array of distinct integers, a backtracking approach with in-place swapping is highly efficient:
1. Define a recursive helper function `backtrack(start)` which aims to generate all permutations for the suffix beginning at index `start`.
2. **Base Case**: If `start` reaches the length of the array, all positions have been filled. A copy of the current state of the array represents a unique permutation. Add it to our result list.
3. **Recursive Step**:
   - For every index `i` from `start` to `n - 1`:
     - Swap the element at `nums[start]` with the element at `nums[i]`. This effectively "chooses" `nums[i]` to be at the current `start` position.
     - Recursively call `backtrack(start + 1)` to generate permutations for the remaining elements.
     - **Backtrack**: Swap `nums[start]` and `nums[i]` back to their original positions. This restoration step allows us to try placing a different element at the `start` position in the next iteration.
4. The initial call is `backtrack(0)`.

Time Complexity: O(n * n!) where n is the number of elements. There are n! permutations, and each takes O(n) time to copy into the result.
Space Complexity: O(n) for the recursion stack."""
    
    answer = """def permute(nums):
    res = []
    
    def backtrack(start):
        if start == len(nums):
            res.append(list(nums))
            return
            
        for i in range(start, len(nums)):
            # Swap to place each element at the current 'start' position
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            # Backtrack to restore the original state
            nums[start], nums[i] = nums[i], nums[start]
            
    backtrack(0)
    return res"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\nimport re\n\ndef permute(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    print(permute(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nvector<vector<int>> permute(vector<int>& nums) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    vector<int> all_nums;\n    while (getline(cin, line)) {\n        for (char &c : line) if (c == ',' || c == '[' || c == ']' || c == '=' || c == ':' || c == '\"' || c == '{' || c == '}') c = ' ';\n        stringstream ss(line);\n        string part;\n        while (ss >> part) {\n            try { all_nums.push_back(stoi(part)); } catch(...) {}\n        }\n    }\n    auto res = permute(all_nums);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        cout << \"[\";\n        for (int j = 0; j < (int)res[i].size(); j++) {\n            cout << res[i][j];\n            if (j + 1 < (int)res[i].size()) cout << \", \";\n        }\n        cout << \"]\";\n        if (i + 1 < (int)res.size()) cout << \", \";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<Integer>> permute(int[] nums) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> allNums = new ArrayList<>();\n        while (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[^0-9-]\", \"\");\n            if (!s.isEmpty()) try { allNums.add(Integer.parseInt(s)); } catch(Exception e) {}\n        }\n        int[] nums = new int[allNums.size()];\n        for (int i = 0; i < allNums.size(); i++) nums[i] = allNums.get(i);\n        List<List<Integer>> res = permute(nums);\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < res.size(); i++) {\n            sb.append(\"[\");\n            List<Integer> perm = res.get(i);\n            for (int j = 0; j < perm.size(); j++) {\n                sb.append(perm.get(j));\n                if (j + 1 < perm.size()) sb.append(\", \");\n            }\n            sb.append(\"]\");\n            if (i + 1 < res.size()) sb.append(\", \");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction permute(nums) {\n    // User logic here\n    return [];\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst allNums = (data.match(/-?\\d+/g) || []).map(Number);\nconst res = permute(allNums);\nconsole.log('[' + res.map(p => '[' + p.join(', ') + ']').join(', ') + ']');",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\nint** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {\n    // User logic here\n    *returnSize = 0;\n    *returnColumnSizes = NULL;\n    return NULL;\n}\n\nint main() {\n    int* all_nums = malloc(1000 * sizeof(int));\n    int count = 0;\n    char line[1000];\n    while (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                all_nums[count++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    int returnSize = 0;\n    int* returnColumnSizes = NULL;\n    int** res = permute(all_nums, count, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"[\");\n        for (int j = 0; j < returnColumnSizes[i]; j++) {\n            printf(\"%d\", res[i][j]);\n            if (j + 1 < returnColumnSizes[i]) printf(\", \");\n        }\n        printf(\"]\");\n        if (i + 1 < returnSize) printf(\", \");\n    }\n    printf(\"]\\n\");\n    free(all_nums);\n    return 0;\n}"
    }

    def _permute(nums):
        res = []
        def backtrack(start):
            if start == len(nums):
                res.append(list(nums))
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return res

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 3", "expected_output": str(_permute([1,2,3])), "is_sample": True},
        {"input": "0 1", "expected_output": str(_permute([0,1])), "is_sample": True},
        # Middle five: Diverse cases
        {"input": "1", "expected_output": "[[1]]", "is_sample": False},
        {"input": "10 -10", "expected_output": str(_permute([10, -10])), "is_sample": False},
        {"input": "-1 0 1", "expected_output": str(_permute([-1, 0, 1])), "is_sample": False},
        {"input": "5 4 3", "expected_output": str(_permute([5, 4, 3])), "is_sample": False},
        {"input": "1 2 3 4", "expected_output": str(_permute([1, 2, 3, 4])), "is_sample": False},
        # Last three: Stress tests
        {"input": "1 2 3 4 5 6", "expected_output": str(_permute([1, 2, 3, 4, 5, 6])), "is_sample": False},
        {"input": "-3 -2 -1 0 1 2", "expected_output": str(_permute([-3, -2, -1, 0, 1, 2])), "is_sample": False},
        {"input": "0 1 2 3 4 5", "expected_output": str(_permute([0, 1, 2, 3, 4, 5])), "is_sample": False}
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
        "topics": ["Array", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-200/46_Permutations.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
