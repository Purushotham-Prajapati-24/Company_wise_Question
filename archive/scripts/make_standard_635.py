import json
import os

def generate_json():
    problem_id = 635
    title = "Design Log Storage System"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>635. Design Log Storage System</h3>
<p>You are given several logs, each log contains a unique id and timestamp. Timestamp is a string that has the following format: <code>Year:Month:Day:Hour:Minute:Second</code>, for example, <code>2017:01:01:23:59:59</code>. All domains are zero-padded decimal numbers.</p>

<p>Design a log storage system to implement the following functions:</p>

<ul>
	<li><code>void put(int id, string timestamp)</code>: Inputs a log's unique id and timestamp.</li>
	<li><code>int[] retrieve(string start, string end, string granularity)</code>: Returns the ids of the logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, transcription of a log's timestamp with <code>granularity</code> means the remaining domains of the timestamp after that granularity will be ignored. For example, if <code>granularity = "Day"</code>, it means we only care about the year, month and day of the timestamps.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
<strong>Output:</strong>
[null, null, null, null, [3, 2, 1], [2, 1]]

<strong>Explanation:</strong>
LogSystem logSystem = new LogSystem();
logSystem.put(1, "2017:01:01:23:59:59");
logSystem.put(2, "2017:01:01:22:59:59");
logSystem.put(3, "2016:01:01:00:00:00");

// return [3,2,1], because you need to return all logs between 2016 and 2017.
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year");

// return [2,1], because you need to return all logs between 2016:01:01:01 and 2017:01:01:23.
// Log 3 is not within the range because its hour is 00, which is before 01.
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour");
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= id &lt;= 300</code></li>
	<li><code>1 &lt;= put.length &lt;= 300</code></li>
	<li><code>1 &lt;= retrieve.length &lt;= 300</code></li>
	<li>There will be at most <code>300</code> logs.</li>
	<li>The range between <code>start</code> and <code>end</code> will be at most <code>200</code>.</li>
</ul>"""

    input_format = "Commands and arguments for put and retrieve."
    output_format = "Integer IDs for retrieve results."
    
    constraints = [
        "Logs up to 300.",
        "Timestamps strings follow fixed format."
    ]
    
    explanation = """To design the Log Storage System with variable granularity:
1. **Normalization**:
   - Timestamps are already zero-padded and in `YYYY:MM:DD:HH:MM:SS` format. This means string comparison correctly reflects chronological order.
   - For any given granularity (Year, Month, Day, Hour, Minute, Second), determine how many characters to keep from the timestamp string.
2. **Setup**:
   - Store all logs in a list `(id, timestamp)`.
   - Map each granularity to its ending index in the timestamp string:
     - `Year: 4` (e.g., `2017`)
     - `Month: 7` (e.g., `2017:01`)
     - `Day: 10` (e.g., `2017:01:01`)
     - `Hour: 13` (e.g., `2017:01:01:23`)
     - `Minute: 16` (e.g., `2017:01:01:23:59`)
     - `Second: 19` (e.g., `2017:01:01:23:59:59`)
3. **Execution for `retrieve(start, end, granularity)`**:
   - Slice the `start` and `end` strings up to the character index corresponding to the granularity.
   - Iterate through all stored logs.
   - Slice the log's timestamp up to the same index.
   - If `start_slice <= log_slice <= end_slice`, return the log's ID.
4. **Complexity Analysis**:
   - `put`: O(1) to append to list.
   - `retrieve`: O(N) where N is the number of logs.
   - Space: O(N) to store logs."""
    
    answer = """class LogSystem:
    def __init__(self):
        self.logs = []
        self.indices = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.indices[granularity]
        start_cut = start[:idx]
        end_cut = end[:idx]
        
        res = []
        for lid, ts in self.logs:
            if start_cut <= ts[:idx] <= end_cut:
                res.append(lid)
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass LogSystem:\n    def __init__(self):\n        pass\n    def put(self, id, timestamp):\n        pass\n    def retrieve(self, start, end, granularity):\n        pass\n\nif __name__ == '__main__':\n    # Process commands\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <map>\nusing namespace std;\n\nclass LogSystem {\npublic:\n    LogSystem() {\n    }\n    void put(int id, string timestamp) {\n    }\n    vector<int> retrieve(string start, string end, string granularity) {\n        return {};\n    }\n};",
        "java": "import java.util.*;\n\npublic class LogSystem {\n    public LogSystem() {\n    }\n    public void put(int id, String timestamp) {\n    }\n    public List<Integer> retrieve(String start, String end, String granularity) {\n        return new ArrayList<>();\n    }\n}",
        "javascript": "/**\n * @constructor\n */\nvar LogSystem = function() {\n};\n\n/**\n * @param {number} id\n * @param {string} timestamp\n * @return {void}\n */\nLogSystem.prototype.put = function(id, timestamp) {\n};\n\n/**\n * @param {string} start\n * @param {string} end\n * @param {string} granularity\n * @return {number[]}\n */\nLogSystem.prototype.retrieve = function(start, end, granularity) {\n};",
        "c": "typedef struct {\n    // User logic\n} LogSystem;\n\nLogSystem* logSystemCreate() {\n}\n\nvoid logSystemPut(LogSystem* obj, int id, char * timestamp) {\n}\n\nint* logSystemRetrieve(LogSystem* obj, char * start, char * end, char * granularity, int* returnSize) {\n}"
    }

    test_cases = [
        {"input": '["LogSystem", "put", "put", "put", "retrieve", "retrieve"]\\n[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]', "expected_output": "[null, null, null, null, [3, 2, 1], [2, 1]]", "is_sample": True},
        {"input": '["LogSystem", "put", "retrieve"]\\n[[], [1, "2017:01:01:23:59:59"], ["2017:01:01:23:59:59", "2017:01:01:23:59:59", "Second"]]', "expected_output": "[null, null, [1]]", "is_sample": False},
        {"input": '["LogSystem", "put", "retrieve"]\\n[[], [1, "2000:01:01:00:00:00"], ["2001:01:01:00:00:00", "2002:01:01:00:00:00", "Year"]]', "expected_output": "[null, null, []]", "is_sample": False},
        {"input": '["LogSystem", "put", "put", "retrieve"]\\n[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:02:23:59:59"], ["2017:01:01:00:00:00", "2017:01:01:23:59:59", "Day"]]', "expected_output": "[null, null, null, [1]]", "is_sample": False},
        # Stress cases
        {"input": '["LogSystem"] + ["put" for _ in range(300)] + ["retrieve"]', "expected_output": "...", "is_sample": False},
        {"input": '["LogSystem", "put", "retrieve"]\\n[[], [1, "2017:12:31:23:59:59"], ["2017:12:31:23:59:59", "2018:01:01:00:00:00", "Minute"]]', "expected_output": "...", "is_sample": False},
        {"input": '["LogSystem", "put", "retrieve"]\\n[[], [1, "2017:01:01:23:59:59"], ["2017:01:01:23:59:59", "2017:01:01:23:59:59", "Year"]]', "expected_output": "...", "is_sample": False}
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
        "topics": ["Hash Table", "Design", "String"],
        "companyIndex": 0
    }

    output_path = "601-800/635_Design_Log_Storage_System.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
