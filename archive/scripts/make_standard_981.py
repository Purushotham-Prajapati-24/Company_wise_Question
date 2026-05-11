import json
import os

def generate_json():
    problem_id = 981
    title = "Time Based Key-Value Store"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>981. Time Based Key-Value Store</h3>
<p>Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.</p>

<p>Implement the <code>TimeMap</code> class:</p>

<ul>
	<li><code>TimeMap()</code> Initializes the object of the data structure.</li>
	<li><code>void set(String key, String value, int timestamp)</code> Stores the key <code>key</code> with the value <code>value</code> at the given time <code>timestamp</code>.</li>
	<li><code>String get(String key, int timestamp)</code> Returns a value such that <code>set</code> was called previously, with <code>timestamp_prev &lt;= timestamp</code>. If there are multiple such values, it returns the value associated with the largest <code>timestamp_prev</code>. If there are no values, it returns <code>""</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong>
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
<strong>Output:</strong>
[null, null, "bar", "bar", null, "bar2", "bar2"]
<strong>Explanation:</strong>
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= key.length, value.length &lt;= 100</code></li>
	<li><code>key</code> and <code>value</code> consist of lowercase English letters and digits.</li>
	<li><code>1 &lt;= timestamp &lt;= 10<sup>7</sup></code></li>
	<li>All the timestamps <code>timestamp</code> of <code>set</code> are strictly increasing.</li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>set</code> and <code>get</code>.</li>
</ul>
"""

    input_format = "List of method calls and their arguments."
    output_format = "List of results for each method call."
    
    constraints = [
        "TS up to 10^7",
        "Strictly increasing timestamps in set",
        "Up to 200,000 calls"
    ]
    
    explanation = """To implement the TimeMap efficiently:
1. **The Core Question**:
   - We need to store values associated with keys and timestamps, and retrieve the value at a given timestamp or the most recent previous one.
2. **The Observation**:
   - Since `set` calls arrive in strictly increasing timestamp order, the values for each key will naturally be sorted by timestamp.
3. **The Design**:
   - Use a hash map where keys are strings and values are lists of `(timestamp, value)` pairs.
4. **Operations**:
   - `set(key, value, timestamp)`:
     - Append `(timestamp, value)` to the list for that `key`.
     - Time Complexity: O(1).
   - `get(key, timestamp)`:
     - Perform a binary search (specifically, `bisect_right` or finding the greatest element $\le$ target) on the list for that `key`.
     - Time Complexity: O(log N) where N is the number of times `set` was called for that key.
5. **Result Retrieval**:
   - If a valid index is found from the binary search, return the associated value.
   - Otherwise, return `""`.

Complexity:
- Time: `set` O(1), `get` O(log N).
- Space: O(N * (K+V)) where N is the total number of entries."""
    
    answer = """import bisect

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        idx = bisect.bisect_right(arr, (timestamp, chr(127)))
        if idx == 0:
            return ""
        return arr[idx - 1][1]"""

    boilerplate = {
        "python": "import sys\nimport json\nimport bisect\n\nclass TimeMap:\n    def __init__(self):\n        pass\n    def set(self, key, value, timestamp):\n        pass\n    def get(self, key, timestamp):\n        pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n#include <algorithm>\n\nusing namespace std;\n\nclass TimeMap {\npublic:\n    TimeMap() {}\n    void set(string key, string value, int timestamp) {}\n    string get(string key, int timestamp) {\n        return \"\";\n    }\n};",
        "java": "import java.util.*;\n\nclass TimeMap {\n    public TimeMap() {}\n    public void set(String key, String value, int timestamp) {}\n    public String get(String key, int timestamp) {\n        return \"\";\n    }\n}",
        "javascript": "var TimeMap = function() {};\nTimeMap.prototype.set = function(key, value, timestamp) {};\nTimeMap.prototype.get = function(key, timestamp) {};",
        "c": "typedef struct {\n} TimeMap;\nTimeMap* timeMapCreate() {\n}\nvoid timeMapSet(TimeMap* obj, char* key, char* value, int timestamp) {\n}\nchar* timeMapGet(TimeMap* obj, char* key, int timestamp) {\n}\nvoid timeMapFree(TimeMap* obj) {\n}"
    }

    test_cases = [
        {"input": '["TimeMap", "set", "get", "get", "set", "get", "get"]\\n[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]', "expected_output": "[null, null, \"bar\", \"bar\", null, \"bar2\", \"bar2\"]", "is_sample": True},
        # Diverse cases
        {"input": '["TimeMap", "set", "get"]\\n[[], ["k1", "v1", 10], ["k1", 5]]', "expected_output": '[null, null, ""]', "is_sample": False},
        {"input": '["TimeMap", "set", "set", "get"]\\n[[], ["k", "v1", 10], ["k", "v2", 20], ["k", 15]]', "expected_output": '[null, null, null, "v1"]', "is_sample": False},
        {"input": '["TimeMap", "set", "set", "get"]\\n[[], ["k", "v1", 10], ["k", "v2", 20], ["k", 25]]', "expected_output": '[null, null, null, "v2"]', "is_sample": False},
        {"input": '["TimeMap", "get"]\\n[[], ["key", 100]]', "expected_output": '[null, ""]', "is_sample": False},
        {"input": '["TimeMap", "set", "get"]\\n[[], ["a", "alpha", 1], ["b", 1]]', "expected_output": '[null, null, ""]', "is_sample": False},
        {"input": '["TimeMap", "set", "set", "get"]\\n[[], ["a", "v1", 2], ["a", "v2", 4], ["a", 4]]', "expected_output": '[null, null, null, "v2"]', "is_sample": False},
        {"input": '["TimeMap", "set", "set", "get"]\\n[[], ["a", "x", 1], ["a", "y", 2], ["a", 2]]', "expected_output": '[null, null, null, "y"]', "is_sample": False},
        {"input": '["TimeMap", "set", "set", "get"]\\n[[], ["key", "high", 1000], ["key", "low", 500], ["key", 750]]', "expected_output": '[null, null, null, "low"]', "is_sample": False},
        {"input": '["TimeMap", "set", "get", "set", "get"]\\n[[], ["k", "a", 1], ["k", 2], ["k", "b", 3], ["k", 4]]', "expected_output": '[null, null, "a", null, "b"]', "is_sample": False}
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
        "topics": ["Hash Table", "String", "Binary Search", "Design"],
        "companyIndex": 0
    }

    output_path = "standardized_json/801-1000/981_Time_Based_Key-Value_Store.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
