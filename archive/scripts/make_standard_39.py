import json
import os

def generate_json():
    problem_id = 39
    title = "Combination Sum"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>39. Combination Sum</h3>
<p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return <em>a list of all <strong>unique combinations</strong> of </em><code>candidates</code><em> where the chosen numbers sum to </em><code>target</code><em>.</em> You may return the combinations in <strong>any order</strong>.</p>

<p>The <strong>same</strong> number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>. Two combinations are unique if the <strong>frequency</strong> of at least one of the chosen numbers is different.</p>

<p>The test cases are generated such that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>2 &lt;= candidates[i] &lt;= 40</code></li>
	<li>All elements of <code>candidates</code> are <strong>distinct</strong>.</li>
	<li><code>1 &lt;= target &lt;= 40</code></li>
</ul>"""

    input_format = "Line 1: Space-separated integers for the array 'candidates'.\nLine 2: An integer 'target'."
    output_format = "A list of lists containing all unique combinations that sum to 'target'."
    
    constraints = [
        "1 <= candidates.length <= 30",
        "2 <= candidates[i] <= 40",
        "All elements in candidates are distinct.",
        "1 <= target <= 40"
    ]
    
    explanation = """To find all unique combinations that sum up to a target value using candidates an unlimited number of times:
1. Sort the `candidates` array. Sorting helps in early termination of the recursion (pruning).
2. Use a backtracking function `backtrack(start_index, current_combination, remaining_target)`:
   - If `remaining_target == 0`: We found a valid combination. Add a copy of `current_combination` to the results.
   - If `remaining_target < 0`: The current combination's sum exceeds the target. Return immediately.
   - Iterate through `candidates` starting from `start_index` to avoid duplicate combinations:
     - If the `current_candidate` is greater than `remaining_target`, we can stop iterating for the current call because all subsequent candidates are even larger (due to sorting).
     - Include the `current_candidate` in the `current_combination`.
     - Recurse with the same `start_index` (allowing the same number to be reused) and `remaining_target - current_candidate`.
     - After recursion, remove the last element (backtrack) to explore the next candidate.
3. Returning combinations in any order is acceptable.

Time Complexity: O(N^(T/M + 1)) where N is the number of candidates, T is the target value, and M is the minimal value among candidates.
Space Complexity: O(T/M) for the recursion depth."""
    
    answer = """def combinationSum(candidates, target):
    res = []
    candidates.sort()
    
    def backtrack(start, curr, remain):
        if remain == 0:
            res.append(list(curr))
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break
            curr.append(candidates[i])
            backtrack(i, curr, remain - candidates[i])
            curr.pop()
    
    backtrack(0, [], target)
    return res"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef combinationSum(candidates, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    cand_data = input_data[0].strip() if len(input_data) > 0 else \"\"\n    target_data = input_data[1].strip() if len(input_data) > 1 else \"0\"\n    candidates = [int(x) for x in cand_data.split()]\n    target = int(target_data)\n    print(combinationSum(candidates, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nvector<vector<int>> combinationSum(vector<int>& candidates, int target) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<int> candidates;\n        stringstream ss(line);\n        int num;\n        while (ss >> num) candidates.push_back(num);\n        int target;\n        if (cin >> target) {\n            auto res = combinationSum(candidates, target);\n            cout << \"[\";\n            for (int i = 0; i < (int)res.size(); i++) {\n                cout << \"[\";\n                for (int j = 0; j < (int)res[i].size(); j++) {\n                    cout << res[i][j];\n                    if (j + 1 < (int)res[i].size()) cout << \", \";\n                }\n                cout << \"]\";\n                if (i + 1 < (int)res.size()) cout << \", \";\n            }\n            cout << \"]\" << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<Integer>> combinationSum(int[] candidates, int target) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            String[] parts = line.isEmpty() ? new String[0] : line.split(\"\\\\s+\");\n            int[] candidates = new int[parts.length];\n            for (int i = 0; i < parts.length; i++) candidates[i] = Integer.parseInt(parts[i]);\n            if (sc.hasNextInt()) {\n                int target = sc.nextInt();\n                List<List<Integer>> res = combinationSum(candidates, target);\n                StringBuilder sb = new StringBuilder(\"[\");\n                for (int i = 0; i < res.size(); i++) {\n                    sb.append(\"[\");\n                    List<Integer> combo = res.get(i);\n                    for (int j = 0; j < combo.size(); j++) {\n                        sb.append(combo.get(j));\n                        if (j + 1 < combo.size()) sb.append(\", \");\n                    }\n                    sb.append(\"]\");\n                    if (i + 1 < res.size()) sb.append(\", \");\n                }\n                sb.append(\"]\");\n                System.out.println(sb.toString());\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction combinationSum(candidates, target) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const candidates = input[0].trim().split(/\\s+/).map(Number);\n    const target = parseInt(input[1].trim(), 10);\n    const res = combinationSum(candidates, target);\n    console.log('[' + res.map(combo => '[' + combo.join(', ') + ']').join(', ') + ']');\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n// User implements logic; return 2D array via returnColumnSizes + returnSize\nint** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {\n    // User logic here\n    *returnSize = 0;\n    *returnColumnSizes = NULL;\n    return NULL;\n}\n\nint main() {\n    char line[5000];\n    if (fgets(line, sizeof(line), stdin)) {\n        int capacity = 100, size = 0;\n        int* candidates = (int*)malloc(capacity * sizeof(int));\n        char* token = strtok(line, \" \\t\\r\\n\");\n        while (token) {\n            if (size == capacity) { capacity *= 2; candidates = (int*)realloc(candidates, capacity * sizeof(int)); }\n            candidates[size++] = atoi(token);\n            token = strtok(NULL, \" \\t\\r\\n\");\n        }\n        int target;\n        if (scanf(\"%d\", &target) == 1) {\n            int returnSize = 0;\n            int* returnColumnSizes = NULL;\n            int** res = combinationSum(candidates, size, target, &returnSize, &returnColumnSizes);\n            printf(\"[\");\n            for (int i = 0; i < returnSize; i++) {\n                printf(\"[\");\n                for (int j = 0; j < returnColumnSizes[i]; j++) {\n                    printf(\"%d\", res[i][j]);\n                    if (j + 1 < returnColumnSizes[i]) printf(\", \");\n                }\n                printf(\"]\");\n                if (i + 1 < returnSize) printf(\", \");\n                if (res[i]) free(res[i]);\n            }\n            printf(\"]\\n\");\n            if (returnColumnSizes) free(returnColumnSizes);\n            if (res) free(res);\n        }\n        free(candidates);\n    }\n    return 0;\n}"
    }

    def _combSum(candidates, target):
        res = []
        candidates.sort()
        def backtrack(start, curr, remain):
            if remain == 0:
                res.append(list(curr))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain: break
                curr.append(candidates[i])
                backtrack(i, curr, remain - candidates[i])
                curr.pop()
        backtrack(0, [], target)
        return res

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "2 3 6 7\n7", "expected_output": str(_combSum([2,3,6,7], 7)), "is_sample": True},
        {"input": "2 3 5\n8", "expected_output": str(_combSum([2,3,5], 8)), "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "2\n1", "expected_output": "[]", "is_sample": False},
        {"input": "10 1\n3", "expected_output": str(_combSum([10,1], 3)), "is_sample": False},
        {"input": "7 3 2\n18", "expected_output": str(_combSum([7,3,2], 18)), "is_sample": False},
        {"input": "8 7 4 3\n11", "expected_output": str(_combSum([8,7,4,3], 11)), "is_sample": False},
        {"input": "3 12\n12", "expected_output": str(_combSum([3,12], 12)), "is_sample": False},
        # Last three: Stress tests
        {"input": "2 3\n40", "expected_output": str(_combSum([2,3], 40)), "is_sample": False},
        {"input": "40\n40", "expected_output": "[[40]]", "is_sample": False},
        {"input": "39 41\n40", "expected_output": "[]", "is_sample": False}
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

    output_path = "1-200/39_Combination_Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
