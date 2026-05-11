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
        "python": "import sys, json\n\ndef combinationSum2(candidates, target):\n    # implementation\n    pass\n\nif __name__ == '__main__':\n    data = json.loads(sys.stdin.read())\n    print(combinationSum2(data['candidates'], data['target']))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {\n        // implementation\n        return {};\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<List<Integer>> combinationSum2(int[] candidates, int target) {\n        // implementation\n        return new ArrayList<>();\n    }\n}",
        "javascript": "/**\n * @param {number[]} candidates\n * @param {number} target\n * @return {number[][]}\n */\nvar combinationSum2 = function(candidates, target) {\n    \n};",
        "c": "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the arrays are returned as *returnColumnSizes array.\n * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().\n */\nint** combinationSum2(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes){\n    \n}"
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
