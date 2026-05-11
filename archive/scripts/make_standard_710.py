import json
import os

def generate_json():
    problem_id = 710
    title = "Random Pick with Blacklist"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>710. Random Pick with Blacklist</h3>
<p>You are given an integer <code>n</code> and an array of <strong>unique</strong> integers <code>blacklist</code>. Design an algorithm to pick a random integer in the range <code>[0, n - 1]</code> that is <strong>not</strong> in <code>blacklist</code>. Any non-blacklisted integer must be <strong>equally likely</strong> to be returned.</p>

<p>Optimize your algorithm such that it minimizes the number of calls to the <strong>built-in</strong> random function of your language.</p>

<p>Implement the <code>Solution</code> class:</p>

<ul>
	<li><code>Solution(int n, int[] blacklist)</code> Initializes the object with the integer <code>n</code> and the blacklisted integers <code>blacklist</code>.</li>
	<li><code>int pick()</code> Returns a random integer in the range <code>[0, n - 1]</code> and not in <code>blacklist</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]
<strong>Output</strong>
[null, 0, 4, 1, 6, 6, 4, 0]

<strong>Explanation</strong>
Solution solution = new Solution(7, [2, 3, 5]);
solution.pick(); // return 0, any number from [0,1,4,6] is ok. All outputs have equal probability of 1/4.
solution.pick(); // return 4
solution.pick(); // return 1
solution.pick(); // return 6
solution.pick(); // return 6
solution.pick(); // return 4
solution.pick(); // return 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= blacklist.length &lt;= min(10<sup>4</sup>, n - 1)</code></li>
	<li><code>0 &lt;= blacklist[i] &lt; n</code></li>
	<li>All the values of <code>blacklist</code> are <strong>unique</strong>.</li>
	<li>At most <code>2 * 10<sup>4</sup></code> calls will be made to <code>pick</code>.</li>
</ul>"""

    input_format = "A series of method calls and their arguments."
    output_format = "A list of results corresponding to each method call."
    
    constraints = ["1 <= n <= 10^9", "0 <= blacklist.length <= 10", "000", "At most 20", "000 calls to pick()."]
    
    explanation = """HARD problem on ."""
    
    answer = """import random
class Solution:
    def __init__(self, n: int, blacklist: list[int]):
        self.m = n - len(blacklist)
        self.mapping = {}
        blacklist_set = set(blacklist)
        
        # Numbers in [m, n-1] that are NOT blacklisted
        last = n - 1
        for x in blacklist:
            if x < self.m:
                while last in blacklist_set:
                    last -= 1
                self.mapping[x] = last
                last -= 1

    def pick(self) -> int:
        idx = random.randrange(self.m)
        return self.mapping.get(idx, idx)"""

    boilerplate = {
        "python": "import sys\n\ndef __init__(n: int, blacklist: list[int]):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    n: int = input_data[0] if len(input_data) > 0 else \"\"\n    blacklist: list[int] = input_data[1] if len(input_data) > 1 else \"\"\n    print(__init__(n: int, blacklist: list[int]))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint __init__(string n: int, string blacklist: list[int]) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string n: int; cin >> n: int;\n    string blacklist: list[int]; cin >> blacklist: list[int];\n    cout << __init__(n: int, blacklist: list[int]) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
