import json
import os

def generate_json():
    problem_id = 815
    title = "Bus Routes"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>815. Bus Routes</h3>
<p>You are given an array <code>routes</code> where <code>routes[i]</code> is a bus route that the <code>i<sup>th</sup></code> bus repeats forever.</p>

<ul>
	<li>For example, if <code>routes[0] = [1, 5, 7]</code>, this means that the <code>0<sup>th</sup></code> bus travels in the sequence <code>1 &rarr; 5 &rarr; 7 &rarr; 1 &rarr; 5 &rarr; 7 &rarr; ...</code> forever.</li>
</ul>

<p>You start at the bus stop <code>source</code> (you are not on any bus initially), and you want to go to the bus stop <code>target</code>. You can travel between bus stops by buses only.</p>

<p>Return <em>the least number of buses you must take to reach </em><code>target</code>. Return <code>-1</code> if it is not possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> routes = [[1,2,7],[3,6,7]], source = 1, target = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> routes = [[7,12],[4,5,15],[6,15,19],[9,12,13]], source = 15, target = 12
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= routes.length &lt;= 500</code>.</li>
	<li><code>1 &lt;= routes[i].length &lt;= 1000</code>.</li>
	<li>All the values of <code>routes[i]</code> are <strong>unique</strong>.</li>
	<li><code>sum(routes[i].length) &lt;= 10<sup>5</sup></code>.</li>
	<li><code>0 &lt;= routes[i][j] &lt; 10<sup>6</sup></code>.</li>
	<li><code>0 &lt;= source, target &lt; 10<sup>6</sup></code>.</li>
</ul>"""

    input_format = "An integer r (number of routes), followed by r routes (each route starts with length l_i, then l_i stops), then source and target."
    output_format = "An integer representing the least number of buses or -1."
    
    constraints = []
    
    explanation = """HARD problem on ."""
    
    answer = """from collections import deque, defaultdict
def numBusesToDestination(routes, source, target):
    if source == target: return 0
    stop_to_buses = defaultdict(list)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].append(i)
    
    q = deque([(source, 0)])
    visited_stops = {source}
    visited_buses = set()
    
    while q:
        stop, count = q.popleft()
        if stop == target: return count
        for bus_idx in stop_to_buses[stop]:
            if bus_idx not in visited_buses:
                visited_buses.add(bus_idx)
                for next_stop in routes[bus_idx]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, count + 1))
    return -1"""

    boilerplate = {
        "python": "import sys\n\ndef numBusesToDestination(routes, source, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    routes = input_data[0] if len(input_data) > 0 else \"\"\n    source = input_data[1] if len(input_data) > 1 else \"\"\n    target = input_data[2] if len(input_data) > 2 else \"\"\n    print(numBusesToDestination(routes, source, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint numBusesToDestination(string routes, string source, string target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string routes; cin >> routes;\n    string source; cin >> source;\n    string target; cin >> target;\n    cout << numBusesToDestination(routes, source, target) << endl;\n    return 0;\n}",
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
