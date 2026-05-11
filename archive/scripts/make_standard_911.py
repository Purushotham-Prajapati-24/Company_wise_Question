import json
import os

def generate_json():
    problem_id = 911
    title = "Online Election"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>911. Online Election</h3>
<p>You are given two integer arrays <code>persons</code> and <code>times</code>. In an election, the <code>i<sup>th</sup></code> vote was cast for <code>persons[i]</code> at time <code>times[i]</code>.</p>

<p>For each query at a time <code>t</code>, find the person that was leading the election at time <code>t</code>.</p>

<p>Votes cast at time <code>t</code> will count towards the query at time <code>t</code>. If there is a tie for the most votes, the most recently cast vote (among those tied) wins.</p>

<p>Implement the <code>TopVotedCandidate</code> class:</p>

<ul>
	<li><code>TopVotedCandidate(int[] persons, int[] times)</code> Initializes the object with the <code>persons</code> and <code>times</code> arrays.</li>
	<li><code>int q(int t)</code> Returns the number of the person that was leading the election at time <code>t</code> according to the mentioned rules.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
<strong>Output</strong>
[null, 0, 1, 1, 0, 0, 1]

<strong>Explanation</strong>
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as person 1 is the most recent to tie with 3 votes)
topVotedCandidate.q(15); // return 0
topVotedCandidate.q(24); // return 0
topVotedCandidate.q(8); // return 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= persons.length &lt;= 5000</code></li>
	<li><code>times.length == persons.length</code></li>
	<li><code>0 &lt;= persons[i] &lt; persons.length</code></li>
	<li><code>0 &lt;= times[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>times</code> is sorted in a strictly increasing order.</li>
	<li><code>times[0] &lt;= t &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>q</code>.</li>
</ul>"""

    input_format = "An integer n for votes, n persons, n times, an integer m for queries, m query times."
    output_format = "m space-separated integers representing leading candidates."
    
    constraints = ["Votes: 1 to 5", "000.", "Persons: 0 to n-1.", "Times: strictly increasing up to 10^9.", "Queries: up to 10", "000.", "Tie rule: Most recently cast vote wins."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """import bisect

class TopVotedCandidate:
    def __init__(self, persons, times):
        self.times = times
        self.leads = []
        count = {}
        lead = -1
        max_votes = 0
        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= max_votes:
                max_votes = count[p]
                lead = p
            self.leads.append(lead)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leads[idx]"""

    boilerplate = {
        "python": "import sys\n\ndef __init__(persons, times):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    persons = input_data[0] if len(input_data) > 0 else \"\"\n    times = input_data[1] if len(input_data) > 1 else \"\"\n    print(__init__(persons, times))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint __init__(string persons, string times) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string persons; cin >> persons;\n    string times; cin >> times;\n    cout << __init__(persons, times) << endl;\n    return 0;\n}",
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
