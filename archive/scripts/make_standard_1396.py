import json
import os

def generate_json():
    problem_id = 1396
    title = "Design Underground System"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1396. Design Underground System</h3>
<p>An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.</p>

<p>Implement the <code>UndergroundSystem</code> class:</p>

<ul>
	<li><code>checkIn(int id, string stationName, int t)</code>
	<ul>
		<li>A customer with a card ID equal to <code>id</code>, checks in at the station <code>stationName</code> at time <code>t</code>.</li>
		<li>A customer can only be checked into one place at a time.</li>
	</ul>
	</li>
	<li><code>checkOut(int id, string stationName, int t)</code>
	<ul>
		<li>A customer with a card ID equal to <code>id</code>, checks out from the station <code>stationName</code> at time <code>t</code>.</li>
	</ul>
	</li>
	<li><code>getAverageTime(string startStation, string endStation)</code>
	<ul>
		<li>Returns the average time it takes to travel from <code>startStation</code> to <code>endStation</code>.</li>
		<li>The average time is computed from all the previous traveling times from <code>startStation</code> to <code>endStation</code> that happened <strong>directly</strong>, meaning a check in at <code>startStation</code> followed by a check out from <code>endStation</code>.</li>
		<li>The return value will be within <code>10<sup>-5</sup></code> of the actual answer.</li>
	</ul>
	</li>
</ul>

<p>You may assume all calls to <code>checkIn</code> and <code>checkOut</code> methods are consistent. If a customer checks in at time <code>t<sub>1</sub></code> then checks out at time <code>t<sub>2</sub></code>, then <code>t<sub>1</sub> &lt; t<sub>2</sub></code>. All events happen in chronological order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

<strong>Output</strong>
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

<strong>Explanation</strong>
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);  // Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. Two trips "Leyton" -> "Waterloo", (12 + 10) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000. Three trips "Leyton" -> "Waterloo", (12 + 10 + 14) / 3 = 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= id, t &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= stationName.length, startStation.length, endStation.length &lt;= 10</code></li>
	<li>All strings consist of uppercase and lowercase English letters and digits.</li>
	<li>There will be at most <code>2 * 10<sup>4</sup></code> calls in total to <code>checkIn</code>, <code>checkOut</code>, and <code>getAverageTime</code>.</li>
	<li>Answers within <code>10<sup>-5</sup></code> of the actual value will be accepted.</li>
</ul>"""

    input_format = "A list of method names and a list of arguments for each method."
    output_format = "A list of return values for each method."

    constraints = [
        "1 <= id, t <= 10^6",
        "At most 2 * 10^4 calls",
        "Events in chronological order"
    ]

    explanation = """To implement the UndergroundSystem:
1. Use two Hash Maps:
   - `checkInMap`: To store active check-ins. `id -> (stationName, time)`.
   - `travelTimes`: To store accumulated travel times between stations. `(startStation, endStation) -> (totalTime, count)`.
2. `checkIn(id, stationName, t)`:
   - Add `id -> (stationName, t)` entry to `checkInMap`.
3. `checkOut(id, endStation, t)`:
   - Retrieve `(startStation, startTime)` from `checkInMap` using `id` and remove it.
   - Calculate travel duration: `duration = t - startTime`.
   - Update `travelTimes` entry for `(startStation, endStation)` by incrementing total time and trip count.
4. `getAverageTime(startStation, endStation)`:
   - Retrieve `(totalTime, count)` from `travelTimes` for the station pair.
   - Return `totalTime / count`."""

    answer = """class UndergroundSystem:
    def __init__(self):
        self.checkInMap = {} # id -> (station, time)
        self.travelTimes = {} # (start, end) -> (total_time, count)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkInMap.pop(id)
        key = (start_station, stationName)
        if key not in self.travelTimes:
            self.travelTimes[key] = [0, 0]
        self.travelTimes[key][0] += t - start_time
        self.travelTimes[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travelTimes[(startStation, endStation)]
        return total_time / count"""

    boilerplate = {
        "python": """import sys
import json

class UndergroundSystem:
    def __init__(self):
        pass
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        pass
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        pass
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return 0.0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        methods, args = json.loads(raw)
        obj = None
        results = []
        for m, a in zip(methods, args):
            if m == "UndergroundSystem":
                obj = UndergroundSystem()
                results.append(None)
            elif m == "checkIn":
                results.append(obj.checkIn(a[0], a[1], a[2]))
            elif m == "checkOut":
                results.append(obj.checkOut(a[0], a[1], a[2]))
            elif m == "getAverageTime":
                results.append(obj.getAverageTime(a[0], a[1]))
        print(json.dumps(results).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class UndergroundSystem {
public:
    UndergroundSystem() {}
    void checkIn(int id, string stationName, int t) {}
    void checkOut(int id, string stationName, int t) {}
    double getAverageTime(string startStation, string endStation) { return 0.0; }
};

int main() {
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class UndergroundSystem {
    public UndergroundSystem() {}
    public void checkIn(int id, String stationName, int t) {}
    public void checkOut(int id, String stationName, int t) {}
    public double getAverageTime(String startStation, String endStation) { return 0.0; }
}

public class Main {
    public static void main(String[] args) throws Exception {
    }
}""",
        "javascript": """var UndergroundSystem = function() {
    
};
UndergroundSystem.prototype.checkIn = function(id, stationName, t) {};
UndergroundSystem.prototype.checkOut = function(id, stationName, t) {};
UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) { return 0.0; };

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

typedef struct {
} UndergroundSystem;

UndergroundSystem* constructor() { return NULL; }
void checkIn(UndergroundSystem* obj, int id, char * stationName, int t) {}
void checkOut(UndergroundSystem* obj, int id, char * stationName, int t) {}
double getAverageTime(UndergroundSystem* obj, char * startStation, char * endStation) { return 0.0; }

int main() { return 0; }"""
    }

    import collections
    def solve(methods, args):
        checkInMap = {}
        travelTimes = collections.defaultdict(lambda: [0, 0])
        results = []
        for m, a in zip(methods, args):
            if m == "UndergroundSystem": results.append(None)
            elif m == "checkIn":
                checkInMap[a[0]] = (a[1], a[2])
                results.append(None)
            elif m == "checkOut":
                start_s, start_t = checkInMap.pop(a[0])
                key = (start_s, a[1])
                travelTimes[key][0] += a[2] - start_t
                travelTimes[key][1] += 1
                results.append(None)
            elif m == "getAverageTime":
                key = (a[0], a[1])
                t, c = travelTimes[key]
                results.append(round(t / c, 5))
        return results

    test_cases_data = [
        [["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"], [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]], # Sample 1
        [["UndergroundSystem", "checkIn", "checkOut", "getAverageTime"], [[], [1, "A", 10], [1, "B", 20], ["A", "B"]]], # Simple trip
        [["UndergroundSystem", "checkIn", "checkOut", "checkIn", "checkOut", "getAverageTime"], [[], [1, "A", 10], [1, "B", 20], [1, "A", 30], [1, "B", 50], ["A", "B"]]], # Multi trip same person
        [["UndergroundSystem", "checkIn", "checkIn", "checkOut", "checkOut", "getAverageTime"], [[], [1, "A", 0], [2, "A", 10], [1, "B", 10], [2, "B", 25], ["A", "B"]]], # Multi person same stations
        # Stress tests
        [["UndergroundSystem"] + ["checkIn", "checkOut"]*1000 + ["getAverageTime"], [[],] + [[i, "S", i] if j==0 else [i, "E", i+5] for i in range(1000) for j in range(2)] + [["S", "E"]]],
        [["UndergroundSystem", "checkIn", "checkOut", "getAverageTime"], [[], [999999, "LongStation", 0], [999999, "EndStation", 1000000], ["LongStation", "EndStation"]]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 1})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Hash Table", "Design", "String"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
