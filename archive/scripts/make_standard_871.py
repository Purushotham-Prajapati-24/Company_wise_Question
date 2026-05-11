import json
import os

def generate_json():
    problem_id = 871
    title = "Minimum Number of Refueling Stops"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>871. Minimum Number of Refueling Stops</h3>
<p>A car travels from a starting position to a destination which is <code>target</code> miles away. Along the way, there are gas stations. Each <code>station[i] = [position<sub>i</sub>, fuel<sub>i</sub>]</code> represents a gas station that is <code>position<sub>i</sub></code> miles from the starting position and has <code>fuel<sub>i</sub></code> liters of gas.</p>

<p>The car starts with <code>startFuel</code> liters of gas. It uses one liter of gas per mile. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.</p>

<p>What is the minimum number of refueling stops the car must make in order to reach its destination? If it cannot reach the destination, return <code>-1</code>.</p>

<p>Note that if the car reaches a gas station with <code>0</code> fuel left, the car can still refuel there. If the car reaches the destination with <code>0</code> fuel left, it is still considered to have arrived.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = 1, startFuel = 1, stations = []
<strong>Output:</strong> 0
<strong>Explanation:</strong> We can reach the target without refueling.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = 100, startFuel = 1, stations = [[10,100]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> We can not reach the 10-mile mark.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We start with 10 liters of fuel.
We drive to the 10-mile mark, consuming 10 liters of fuel. We stop and refuel, adding 60 liters of fuel. Now we have 60 liters of fuel.
We drive to the 60-mile mark, consuming 50 liters of fuel and having 10 liters left. We stop and refuel, adding 40 liters of fuel. Now we have 50 liters of fuel.
We drive to the 100-mile mark.
We made 2 refueling stops along the way, so we return 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target, startFuel &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= stations.length &lt;= 500</code></li>
	<li><code>1 &lt;= position<sub>i</sub> &lt; position<sub>i+1</sub> &lt; target</code></li>
	<li><code>1 &lt;= fuel<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Three space-separated integers target, startFuel, and n (number of stations), followed by n pairs of [position, fuel]."
    output_format = "An integer representing the minimum stops or -1."
    
    constraints = ["1 <= target", "startFuel <= 10^9", "0 <= stations.length <= 500", "Positions are strictly increasing."]
    
    explanation = """HARD problem on ."""
    
    answer = """import heapq
def minRefuelStops(target, startFuel, stations):
    pq = []
    stations.append([target, 0])
    
    res = 0
    curr_fuel = startFuel
    prev_pos = 0
    for pos, fuel in stations:
        curr_fuel -= (pos - prev_pos)
        while pq and curr_fuel < 0:
            curr_fuel += -heapq.heappop(pq)
            res += 1
        if curr_fuel < 0: return -1
        heapq.heappush(pq, -fuel)
        prev_pos = pos
        
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef minRefuelStops(target, startFuel, stations):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    target = input_data[0] if len(input_data) > 0 else \"\"\n    startFuel = input_data[1] if len(input_data) > 1 else \"\"\n    stations = input_data[2] if len(input_data) > 2 else \"\"\n    print(minRefuelStops(target, startFuel, stations))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint minRefuelStops(string target, string startFuel, string stations) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string target; cin >> target;\n    string startFuel; cin >> startFuel;\n    string stations; cin >> stations;\n    cout << minRefuelStops(target, startFuel, stations) << endl;\n    return 0;\n}",
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
