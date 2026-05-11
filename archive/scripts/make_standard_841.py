import json
import os

def generate_json():
    problem_id = 841
    title = "Keys and Rooms"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>841. Keys and Rooms</h3>
<p>There are <code>n</code> rooms labeled from <code>0</code> to <code>n - 1</code> and all the rooms are locked except for room <code>0</code>. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.</p>

<p>When you visit a room, you may find a set of <b>distinct keys</b> in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.</p>

<p>Given an array <code>rooms</code> where <code>rooms[i]</code> is the set of keys that you can obtain if you visited room <code>i</code>, return <code>true</code> <em>if you can visit <b>all</b> the rooms, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> rooms = [[1],[2],[3],[]]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
We start in room 0, and collect key 1.
We use key 1 to enter room 1, and collect key 2.
We use key 2 to enter room 2, and collect key 3.
We use key 3 to enter room 3.
Since we were able to enter every room, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> rooms = [[1,3],[3,0,1],[2],[0]]
<strong>Output:</strong> false
<strong>Explanation:</strong> We can not enter room 2 since the only key that unlocks it is in room 2 itself.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == rooms.length</code></li>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= rooms[i].length &lt;= 1000</code></li>
	<li><code>1 &lt;= sum(rooms[i].length) &lt;= 3000</code></li>
	<li><code>0 &lt;= rooms[i][j] &lt; n</code></li>
	<li>All the values of <code>rooms[i]</code> are <b>unique</b>.</li>
</ul>"""

    input_format = "Format: n (rooms), then n lines where line i contains space-separated keys found in room i."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "2 <= n <= 1000",
        "Total keys across all rooms <= 3000",
        "O(N + E) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To determine if all rooms can be visited:
1. **The Graph Theory Perspective**:
   - Each room is a node, and a key for room B found in room A is a directed edge from A to B.
   - We need to determine if all nodes in the graph are reachable from node 0.
2. **Algorithm Strategy (BFS or DFS)**:
   - Use a `visited` set to track which rooms we have entered.
   - Start a traversal (BFS or DFS) from room 0.
   - Mark room 0 as visited and add it to the queue/stack.
   - While the queue/stack is not empty:
     - Pop a room `u`.
     - For every key `v` in room `u`:
       - If room `v` has not been visited:
         - Mark `v` as visited and add it to the traversal structure.
   - After the traversal, compare the size of the `visited` set to the total number of rooms `n`.
3. **Complexity**:
   - Time Complexity: O(N + E) where N is the number of rooms and E is the total number of keys (edges).
   - Space Complexity: O(N) for the `visited` set and the traversal queue."""
    
    answer = """def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    visited = {0}
    stack = [0]
    while stack:
        room = stack.pop()
        for key in rooms[room]:
            if key not in visited:
                visited.add(key)
                stack.append(key)
    return len(visited) == len(rooms)"""

    boilerplate = {
        "python": "import sys\n\ndef canVisitAllRooms(rooms):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if lines:\n        n = int(lines[0].strip())\n        rooms = []\n        for i in range(1, n + 1):\n            if i < len(lines):\n                line = lines[i].strip()\n                rooms.append(list(map(int, line.split())) if line else [])\n            else:\n                rooms.append([])\n        print('true' if canVisitAllRooms(rooms) else 'false')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <stack>\n#include <unordered_set>\n\nusing namespace std;\n\nbool canVisitAllRooms(vector<vector<int>>& rooms) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean canVisitAllRooms(List<List<Integer>> rooms) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function canVisitAllRooms(rooms) {\n    // User logic\n}",
        "c": "bool canVisitAllRooms(int** rooms, int roomsSize, int* roomsColSize) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "4\\n1\\n2\\n3\\n", "expected_output": "true", "is_sample": True},
        {"input": "4\\n1 3\\n3 0 1\\n2\\n0", "expected_output": "false", "is_sample": True},
        {"input": "2\\n1\\n0", "expected_output": "true", "is_sample": False},
        {"input": "2\\n\\n", "expected_output": "false", "is_sample": False},
        {"input": "3\\n1 2\\n\\n", "expected_output": "true", "is_sample": False},
        {"input": "3\\n1\\n\\n2", "expected_output": "false", "is_sample": False},
        {"input": "5\\n1\\n2\\n3\\n4\\n", "expected_output": "true", "is_sample": False},
        {"input": "5\\n1\\n2\\n0\\n4\\n", "expected_output": "false", "is_sample": False}, # Cycle 0-1-2-0, room 3,4 unreachable
        # Stress cases
        {"input": "1000\\n" + "\\n".join([str(i+1) if i < 999 else "" for i in range(1000)]), "expected_output": "true", "is_sample": False},
        {"input": "1000\\n" + "\\n".join(["" for _ in range(1000)]), "expected_output": "false", "is_sample": False}
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
        "topics": ["DFS", "BFS", "Graph"],
        "companyIndex": 0
    }

    output_path = "801-1000/841_Keys_and_Rooms.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
