import json
import os

def generate_json():
    problem_id = 756
    title = "Pyramid Transition Matrix"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>756. Pyramid Transition Matrix</h3>
<p>You are stacking blocks to form a pyramid. Each block has a color which is represented by a single letter. A block may be placed on top of two <strong>adjacent</strong> blocks if and only if the triple of colors formed by the three blocks is in an <code>allowed</code> pattern.</p>

<p>For example, if the two adjacent blocks are colors <code>A</code> and <code>B</code>, and the allowed patterns include <code>"ABC"</code>, then a block of color <code>C</code> may be placed on top of the two blocks.</p>

<p>We start with a bottom row of colors <code>bottom</code>. We want to build the pyramid to the top, where each row has one less block than the one below it. Return <code>true</code><em> if we can build the pyramid all the way to the top, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/08/26/pyramid1-grid.jpg" style="width: 250px; height: 180px;" />
<pre>
<strong>Input:</strong> bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
<strong>Output:</strong> true
<strong>Explanation:</strong>
The allowed patterns form the triples (B, C, G) and (C, D, E).
We can place "G" on top of "BC" and "E" on top of "CD". Now the new row is "GE".
There is an allowed pattern "GEA", so we can place "A" on top of "GE".
The pyramid is:
    A
   G E
  B C D
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/08/26/pyramid2-grid.jpg" style="width: 250px; height: 180px;" />
<pre>
<strong>Input:</strong> bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
<strong>Output:</strong> false
<strong>Explanation:</strong>
We cannot build the pyramid because no pattern allows for a block on top of "BA" in the second row.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= bottom.length &lt;= 6</code></li>
	<li><code>0 &lt;= allowed.length &lt;= 216</code></li>
	<li><code>allowed[i].length == 3</code></li>
	<li>The letters in <code>bottom</code> and <code>allowed[i]</code> are from <code>{'A', 'B', 'C', 'D', 'E', 'F', 'G'}</code>.</li>
	<li>All <code>allowed[i]</code> are unique.</li>
</ul>
"""

    input_format = "A string for bottom and a JSON array of strings for allowed."
    output_format = "A boolean value (true/false)."
    
    constraints = [
        "2 <= bottom.length <= 6",
        "0 <= allowed.length <= 216",
        "allowed[i].length == 3",
        "Input letters are from {'A', 'B', 'C', 'D', 'E', 'F', 'G'}"
    ]
    
    explanation = """To determine if a pyramid can be built:
1. **The Representation**: Use a dictionary `transitions` where `transitions[(A, B)]` is a list of characters `C` such that `ABC` is allowed.
2. **The Algorithm (Recursive DFS with Memoization)**:
   - `build(row)`: A recursive function that tries to form all possible next rows from the current `row`.
   - If `row.length == 1`, return `true` (top reached).
   - Use a sub-function `getNextRow(row, index, next_row_acc)` to generate all possible next rows through backtracking. For each adjacent pair `(row[index], row[index+1])`, try placing each allowed character `C` and recurse for the next index.
   - Memoize the state `(row)` to avoid redundant computations.
3. **Optimizations**:
   - Since `bottom.length` is small ($6$), the state space is manageable.
   - Use bitmasking or sets for faster transition lookups if necessary, though a simple map works well here.

Complexity:
- Time: O(K^N) in the worst case where K is number of color choices and N is height.
- Space: O(State Space) for memoization."""
    
    answer = """def pyramidTransition(bottom: str, allowed: list[str]) -> bool:
    from collections import defaultdict
    trans = defaultdict(list)
    for triple in allowed:
        trans[(triple[0], triple[1])].append(triple[2])
    
    memo = {}
    
    def solve(row):
        if len(row) == 1:
            return True
        if row in memo:
            return memo[row]
            
        next_rows = []
        def get_next_rows(idx, current_next):
            if idx == len(row) - 1:
                next_rows.append("".join(current_next))
                return
            
            pair = (row[idx], row[idx+1])
            if pair in trans:
                for char in trans[pair]:
                    current_next.append(char)
                    get_next_rows(idx + 1, current_next)
                    current_next.pop()
        
        get_next_rows(0, [])
        for nr in next_rows:
            if solve(nr):
                memo[row] = True
                return True
        
        memo[row] = False
        return False

    return solve(bottom)"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef pyramidTransition(bottom, allowed):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        bottom = lines[0].strip()\n        allowed = json.loads(lines[1].strip())\n        print(str(pyramidTransition(bottom, allowed)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nbool pyramidTransition(string bottom, vector<string>& allowed) {\n    return false;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public boolean pyramidTransition(String bottom, List<String> allowed) {\n        return false;\n    }\n}",
        "javascript": "var pyramidTransition = function(bottom, allowed) {\n    return false;\n};",
        "c": "bool pyramidTransition(char* bottom, char** allowed, int allowedSize) {\n    return false;\n}"
    }

    test_cases = [
        {"input": "BCD\\n[\"BCG\", \"CDE\", \"GEA\", \"FFF\"]", "expected_output": "true", "is_sample": True},
        {"input": "AABA\\n[\"AAA\", \"AAB\", \"ABA\", \"ABB\", \"BAC\"]", "expected_output": "false", "is_sample": True},
        # Diverse cases
        {"input": "AAAA\\n[\"AAA\"]", "expected_output": "true", "is_sample": False},
        {"input": "ABC\\n[]", "expected_output": "false", "is_sample": False},
        {"input": "AB\\n[\"ABC\", \"ABD\"]", "expected_output": "true", "is_sample": False},
        {"input": "GAB\\n[\"GAA\", \"GAC\", \"ABA\", \"AAC\"]", "expected_output": "true", "is_sample": False},
        {"input": "ABCDEF\\n[]", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": "ABCDEF\\n[\"ABB\", \"BCC\", \"CDD\", \"DEE\", \"EFF\", \"FGG\"]", "expected_output": "true", "is_sample": False},
        {"input": "AAAAAA\\n[\"AAA\"]", "expected_output": "true", "is_sample": False},
        {"input": "BAAAAB\\n[\"BAA\", \"AAA\", \"AAB\"]", "expected_output": "true", "is_sample": False}
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
        "topics": ["Depth-First Search", "Bit Manipulation", "Memoization"],
        "companyIndex": 0
    }

    output_path = "601-800/756_Pyramid_Transition_Matrix.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
