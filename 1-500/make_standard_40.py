import json
import os

def generate_json():
    problem_id = 40
    title = "Combination Sum II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>40. Combination Sum II</h3>
<p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sum to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong>&nbsp;The solution set must not contain duplicate combinations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> candidates = [10,1,2,7,6,1,5], target = 8
<strong>Output:</strong> 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> candidates = [2,5,2,1,2], target = 5
<strong>Output:</strong> 
[
[1,2,2],
[5]
]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;= candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>"""

    input_format = "An array of candidate integers and a target sum."
    output_format = "A list of unique combinations."
    
    constraints = [
        "1 <= candidates.length <= 100",
        "1 <= candidates[i] <= 50",
        "1 <= target <= 30"
    ]
    
    explanation = """To find all unique combinations sum to target:
1. **Sort Candidates**: Sorting help us handle duplicates and enables pruning.
2. **Backtracking**:
   - `backtrack(start, target, path)`:
   - If `target == 0`, add `path` to result.
   - For $i \in [start, len(candidates)-1]$:
     - If `candidates[i] > target`, break (pruning).
     - If $i > start$ and `candidates[i] == candidates[i-1]`, skip to avoid duplicate combinations.
     - `backtrack(i + 1, target - candidates[i], path + [candidates[i]])`.
3. **Complexity**:
   - **Time**: $O(2^N)$ in worst case, but heavily pruned.
   - **Space**: $O(N)$ for recursion depth."""
    
    answer = """def combinationSum2(candidates, target):
    candidates.sort()
    res = []
    
    def backtrack(start, target, path):
        if target == 0:
            res.append(list(path))
            return
            
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue
            # Pruning
            if candidates[i] > target:
                break
                
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)
            path.pop()
            
    backtrack(0, target, [])
    return res"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef combinationSum2(candidates, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    if len(nums) >= 2:\n        target = nums.pop()\n        print(combinationSum2(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nvector<vector<int>> combinationSum2(vector<int>& candidates, int target) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    vector<int> all_nums;\n    while (getline(cin, line)) {\n        for (char &c : line) if (c == ',' || c == '[' || c == ']' || c == '=' || c == ':' || c == '\"' || c == '{' || c == '}') c = ' ';\n        stringstream ss(line);\n        string part;\n        while (ss >> part) {\n            if (part == \"candidates\" || part == \"target\") continue;\n            try { all_nums.push_back(stoi(part)); } catch(...) {}\n        }\n    }\n    if (all_nums.size() >= 2) {\n        int target = all_nums.back();\n        all_nums.pop_back();\n        auto res = combinationSum2(all_nums, target);\n        cout << \"[\";\n        for (int i = 0; i < (int)res.size(); i++) {\n            cout << \"[\";\n            for (int j = 0; j < (int)res[i].size(); j++) {\n                cout << res[i][j];\n                if (j + 1 < (int)res[i].size()) cout << \", \";\n            }\n            cout << \"]\";\n            if (i + 1 < (int)res.size()) cout << \", \";\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<Integer>> combinationSum2(int[] candidates, int target) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> allNums = new ArrayList<>();\n        while (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[^0-9-]\", \"\");\n            if (!s.isEmpty()) try { allNums.add(Integer.parseInt(s)); } catch(Exception e) {}\n        }\n        if (allNums.size() >= 2) {\n            int target = allNums.get(allNums.size() - 1);\n            int[] candidates = new int[allNums.size() - 1];\n            for (int i = 0; i < allNums.size() - 1; i++) candidates[i] = allNums.get(i);\n            List<List<Integer>> res = combinationSum2(candidates, target);\n            StringBuilder sb = new StringBuilder(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                sb.append(\"[\");\n                List<Integer> combo = res.get(i);\n                for (int j = 0; j < combo.size(); j++) {\n                    sb.append(combo.get(j));\n                    if (j + 1 < combo.size()) sb.append(\", \");\n                }\n                sb.append(\"]\");\n                if (i + 1 < res.size()) sb.append(\", \");\n            }\n            sb.append(\"]\");\n            System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction combinationSum2(candidates, target) {\n    // User logic here\n    return [];\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst allNums = (data.match(/-?\\d+/g) || []).map(Number);\nif (allNums.length >= 2) {\n    const target = allNums.pop();\n    const res = combinationSum2(allNums, target);\n    console.log('[' + res.map(combo => '[' + combo.join(', ') + ']').join(', ') + ']');\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint** combinationSum2(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {\n    // User logic here\n    *returnSize = 0;\n    *returnColumnSizes = NULL;\n    return NULL;\n}\n\nint main() {\n    int* all_nums = malloc(100000 * sizeof(int));\n    int count = 0;\n    char line[1000];\n    while (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                all_nums[count++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    if (count >= 2) {\n        int target = all_nums[count-1];\n        int returnSize = 0;\n        int* returnColumnSizes = NULL;\n        int** res = combinationSum2(all_nums, count - 1, target, &returnSize, &returnColumnSizes);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"[\");\n            for (int j = 0; j < returnColumnSizes[i]; j++) {\n                printf(\"%d\", res[i][j]);\n                if (j + 1 < returnColumnSizes[i]) printf(\", \");\n            }\n            printf(\"]\");\n            if (i + 1 < returnSize) printf(\", \");\n        }\n        printf(\"]\\n\");\n    }\n    free(all_nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": '{"candidates": [10,1,2,7,6,1,5], "target": 8}', "expected_output": "[[1,1,6],[1,2,5],[1,7],[2,6]]", "is_sample": True},
        {"input": '{"candidates": [2,5,2,1,2], "target": 5}', "expected_output": "[[1,2,2],[5]]", "is_sample": True},
        {"input": '{"candidates": [1,1,1], "target": 3}', "expected_output": "[[1,1,1]]", "is_sample": False},
        {"input": '{"candidates": [1,1,1], "target": 2}', "expected_output": "[[1,1]]", "is_sample": False},
        {"input": '{"candidates": [5,5,5], "target": 10}', "expected_output": "[[5,5]]", "is_sample": False},
        {"input": '{"candidates": [1,2,3], "target": 10}', "expected_output": "[]", "is_sample": False},
        {"input": '{"candidates": [1,2,3,4,5], "target": 5}', "expected_output": "[[1,4],[2,3],[5]]", "is_sample": False},
        {"input": '{"candidates": [10], "target": 10}', "expected_output": "[[10]]", "is_sample": False},
        {"input": '{"candidates": [1,2,3,5], "target": 5}', "expected_output": "[[2,3],[5]]", "is_sample": False},
        {"input": '{"candidates": [1,1,2,2], "target": 4}', "expected_output": "[[1,1,2],[2,2]]", "is_sample": False}
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

    output_path = "1-100/40_Combination_Sum_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
