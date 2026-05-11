import json
import os

def generate_json():
    problem_id = 881
    title = "Boats to Save People"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>881. Boats to Save People</h3>
<p>You are given an array <code>people</code> where <code>people[i]</code> is the weight of the <code>i<sup>th</sup></code> person, and an <strong>infinite number of boats</strong> where each boat can carry a maximum weight of <code>limit</code>. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most <code>limit</code>.</p>

<p>Return <em>the minimum number of boats to carry every given person</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> people = [1,2], limit = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 boat (1, 2)
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> people = [3,2,2,1], limit = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 boats (1, 2), (2) and (3)
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> people = [3,5,3,4], limit = 5
<strong>Output:</strong> 4
<strong>Explanation:</strong> 4 boats (3), (3), (4), (5)
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= people[i] &lt;= limit &lt;= 3 * 10<sup>4</sup></code></li>
</ul>
"""

    input_format = "An integer array people and an integer limit."
    output_format = "Minimum number of boats."
    
    constraints = [
        "1 <= people.length <= 50000",
        "1 <= people[i] <= limit <= 30000",
        "Max 2 people per boat."
    ]
    
    explanation = """To minimize the number of boats:
1. **The Strategy (Greedy Pairing)**:
   - Sort the `people` array by weight in ascending order.
   - Use two pointers: `i` for the lightest person and `j` for the heaviest person.
2. **Logic**:
   - Every boat MUST carry at least the heaviest remaining person `people[j]`.
   - Check if the lightest person `people[i]` can fit in the same boat:
     - If `people[i] + people[j] <= limit`, then they both can share the boat. Increment `i`.
   - In either case, the boat is sent off with the heaviest person on it. Decrement `j`.
   - Increment the total `boats` count in each step.
   - Repeat until all people are handled (`i > j`).

Complexity:
- Time: O(N log N) for sorting.
- Space: O(1) extra (ignoring space used by sorting algorithm)."""
    
    answer = """def numRescueBoats(people: list[int], limit: int) -> int:
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0
    while i <= j:
        # Heaviest always takes a boat
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        boats += 1
    return boats"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef numRescueBoats(people, limit):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        people = json.loads(lines[0].strip())\n        limit = int(lines[1].strip())\n        print(numRescueBoats(people, limit))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int numRescueBoats(vector<int>& people, int limit) {\n        return 0;\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public int numRescueBoats(int[] people, int limit) {\n        return 0;\n    }\n}",
        "javascript": "var numRescueBoats = function(people, limit) {\n    return 0;\n};",
        "c": "int numRescueBoats(int* people, int peopleSize, int limit){\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2]\\n3", "expected_output": "1", "is_sample": True},
        {"input": "[3,2,2,1]\\n3", "expected_output": "3", "is_sample": True},
        {"input": "[3,5,3,4]\\n5", "expected_output": "4", "is_sample": True},
        # Diverse cases
        {"input": "[5,1,4,2,3]\\n5", "expected_output": "3", "is_sample": False},
        {"input": "[1,1,1,1,1]\\n2", "expected_output": "3", "is_sample": False},
        {"input": "[3,3,3,3]\\n3", "expected_output": "4", "is_sample": False},
        {"input": "[1,2,3,4,5,6]\\n6", "expected_output": "3", "is_sample": False},
        {"input": "[2,4,3,3,3]\\n5", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": "[30000]*50000\\n30000", "expected_output": "50000", "is_sample": False},
        {"input": "[1]*50000\\n30000", "expected_output": "25000", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Sorting", "Greedy"],
        "companyIndex": 0
    }

    output_path = "801-1000/881_Boats_to_Save_People.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
