import json
import os

def generate_json():
    problem_id = 752
    title = "Open the Lock"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>752. Open the Lock</h3>
<p>You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: <code>'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'</code>. The wheels can rotate freely and wrap around: for example we can turn <code>'9'</code> to be <code>'0'</code>, or <code>'0'</code> to be <code>'9'</code>. Each move consists of turning one wheel one slot.</p>

<p>The lock initially starts at <code>'0000'</code>, a string representing the state of the 4 wheels.</p>

<p>You are given a list of <code>deadends</code> dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.</p>

<p>Given a <code>target</code> representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> deadends = ["0201","0101","0102","1212","2002"], target = "0202"
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> deadends = ["8888"], target = "0009"
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can turn the last wheel in reverse to move from "0000" -> "0009".
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
<strong>Output:</strong> -1
<strong>Explanation:</strong> We cannot reach the target without getting stuck.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= deadends.length &lt;= 500</code></li>
	<li><code>deadends[i].length == 4</code></li>
	<li><code>target.length == 4</code></li>
	<li><code>target</code> <b>will not</b> be in the list <code>deadends</code>.</li>
	<li><code>target</code> and <code>deadends[i]</code> consist of digits only.</li>
</ul>"""

    input_format = "Two lines: 1) Space-separated deadend strings 2) Target string."
    output_format = "A single integer: minimum number of turns or -1."
    
    constraints = [
        "1 <= deadends.length <= 500",
        "Target is reachable in O(10^4) states.",
        "O(10^4 * 8) time complexity (N states * 8 neighbors per state).",
        "O(10^4) space for visited and BFS queue."
    ]
    
    explanation = """To find the shortest number of turns to open the lock:
1. **The Core Approach (Breadth-First Search)**:
   - This is a shortest path problem in an unweighted graph where each lock state is a node and each valid turn is an edge.
   - BFS is ideal for finding the minimum number of steps to reach a target.
2. **State Management**:
   - Use a `visited` set (initialized with `deadends`) to keep track of seen states and avoid dead ends.
   - The queue will store pairs of `(current_code, turns)`.
3. **Neighbor Generation**:
   - For a state like `"0000"`, there are 8 neighbors:
     - Each of the 4 digits can be turned forward (`+1`) or backward (`-1`).
     - Example: '0' -> '1' or '9'.
4. **Special Cases**:
   - If `"0000"` is in the `deadends` list, return -1 immediately.
   - If `"0000"` is already the `target`, return 0.
5. **Complexity**:
   - Number of states = 10^4 (0000 to 9999).
   - Each state has 8 neighbors.
   - Total operations: O(10^4 * 8). Space: O(10^4) to store visited states."""
    
    answer = """from collections import deque

def openLock(deadends: list[str], target: str) -> int:
    dead = set(deadends)
    if "0000" in dead: return -1
    if target == "0000": return 0
    
    queue = deque([("0000", 0)])
    visited = {"0000"}
    
    while queue:
        code, turns = queue.popleft()
        if code == target:
            return turns
        
        for i in range(4):
            digit = int(code[i])
            for d in [-1, 1]:
                new_digit = (digit + d) % 10
                new_code = code[:i] + str(new_digit) + code[i+1:]
                if new_code not in dead and new_code not in visited:
                    visited.add(new_code)
                    queue.append((new_code, turns + 1))
                    
    return -1"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\ndef openLock(deadends, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        deadends = lines[0].strip().split()\n        target = lines[1].strip()\n        print(openLock(deadends, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_set>\n#include <queue>\n\nusing namespace std;\n\nint openLock(vector<string>& deadends, string target) {\n    // User logic\n    return -1;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int openLock(String[] deadends, String target) {\n        // User logic\n        return -1;\n    }\n}",
        "javascript": "function openLock(deadends, target) {\n    // User logic\n}",
        "c": "int openLock(char** deadends, int deadendsSize, char* target) {\n    // User logic\n    return -1;\n}"
    }

    test_cases = [
        {"input": "0201 0101 0102 1212 2002\\n0202", "expected_output": "6", "is_sample": True},
        {"input": "8888\\n0009", "expected_output": "1", "is_sample": True},
        {"input": "8887 8889 8878 8898 8788 8988 7888 9888\\n8888", "expected_output": "-1", "is_sample": True},
        {"input": "0000\\n8888", "expected_output": "-1", "is_sample": False},
        {"input": "empty\\n0000", "expected_output": "0", "is_sample": False}, # 'empty' placeholder
        {"input": "0001\\n0002", "expected_output": "4", "is_sample": False},
        {"input": "0201 0101 0102 1212 2002\\n0000", "expected_output": "0", "is_sample": False},
        {"input": "9999\\n0000", "expected_output": "0", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i).zfill(4) for i in range(1, 400)]) + "\\n9999", "expected_output": "4", "is_sample": False},
        {"input": "0001 0010 0100 1000 0009 0090 0900 9000\\n1111", "expected_output": "-1", "is_sample": False}
    ]
    # Update special case
    test_cases[4]["input"] = "1111\\n0000" # One harmless deadend
    test_cases[4]["expected_output"] = "0"

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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Hash Table", "String", "BFS"],
        "companyIndex": 0
    }

    output_path = "601-800/752_Open_the_Lock.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
