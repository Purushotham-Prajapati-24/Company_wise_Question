import json
import os

def generate_json():
    problem_id = 262
    title = "Trips and Users"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>262. Trips and Users</h3>
<p>Table: <code>Trips</code></p>
<pre>
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| client_id   | int      |
| driver_id   | int      |
| city_id     | int      |
| status      | enum     |
| request_at  | varchar  |
+-------------+----------+
id is the primary key column for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
</pre>
<p>Table: <code>Users</code></p>
<pre>
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| users_id    | int      |
| banned      | enum     |
| role        | enum     |
+-------------+----------+
users_id is the primary key column for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM type of ('Yes', 'No').
</pre>
<p>The <strong>cancellation rate</strong> is computed by dividing the number of cancelled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.</p>
<p>Write a SQL query to find the <strong>cancellation rate</strong> of requests with unbanned users (both client and driver must not be banned) each day between <code>"2013-10-01"</code> and <code>"2013-10-03"</code>. Round <code>Cancellation Rate</code> to <strong>two decimal points</strong>.</p>
<p>Return the result table in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> 
Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status              | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+
Users table:
+----------+--------+--------+
| users_id | banned | role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+
<strong>Output:</strong> 
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+
</pre>"""

    input_format = "Two JSON strings: a list of trips and a list of users."
    output_format = "A JSON list of day and cancellation rate."
    
    constraints = ["Date range: 2013-10-01 to 2013-10-03", "Both client and driver must be unbanned", "Round to 2 decimal points"]
    
    explanation = """HARD problem on ."""
    
    answer = """def cancellation_rate(trips, users):
    unbanned = {u['users_id'] for u in users if u['banned'] == 'No'}
    dates = ["2013-10-01", "2013-10-02", "2013-10-03"]
    stats = {d: [0, 0] for d in dates} # [cancelled, total]
    
    for t in trips:
        if t['request_at'] in stats and t['client_id'] in unbanned and t['driver_id'] in unbanned:
            stats[t['request_at']][1] += 1
            if t['status'].startswith('cancelled'):
                stats[t['request_at']][0] += 1
    
    result = []
    for d in dates:
        cancelled, total = stats[d]
        rate = round(cancelled / total, 2) if total > 0 else 0.0
        result.append({"Day": d, "Cancellation Rate": format(rate, '.2f')})
    return result"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef parse_ascii_table(text):\n    lines = text.strip().split('\\n')\n    if not lines: return []\n    # Find header and separator\n    header_line = -1\n    for i, line in enumerate(lines):\n        if '|' in line and not any(c in line for c in '+-'):\n            header_line = i\n            break\n    if header_line == -1: return []\n    \n    cols = [c.strip() for c in lines[header_line].split('|') if c.strip()]\n    data = []\n    for i in range(header_line + 1, len(lines)):\n        line = lines[i]\n        if '|' in line and not any(c in line for c in '+-'):\n            vals = [v.strip() for v in line.split('|') if v.strip()]\n            if len(vals) == len(cols):\n                row = {}\n                for j in range(len(cols)):\n                    v = vals[j]\n                    if v.isdigit(): v = int(v)\n                    row[cols[j]] = v\n                data.append(row)\n    return data\n\ndef cancellation_rate(trips, users):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    trips_part = \"\"\n    users_part = \"\"\n    \n    if \"Trips table:\" in raw_input:\n        parts = re.split(r'Users table:', raw_input)\n        trips_part = parts[0]\n        users_part = parts[1] if len(parts) > 1 else \"\"\n    \n    if trips_part and users_part:\n        trips = parse_ascii_table(trips_part)\n        users = parse_ascii_table(users_part)\n    else:\n        # Fallback to JSON\n        try:\n            lines = raw_input.strip().split('\\n')\n            trips = json.loads(lines[0])\n            users = json.loads(lines[1])\n        except:\n            trips, users = [], []\n            \n    print(json.dumps(cancellation_rate(trips, users)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <map>\n#include <iomanip>\n\nusing namespace std;\n\nint main() {\n    // Simplistic mock for SQL-like logic in C++\n    cout << \"[]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        System.out.println(\"[]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction parseAsciiTable(text) {\n    const lines = text.trim().split('\\n');\n    const headerLineIdx = lines.findIndex(l => l.includes('|') && !/[+-]/.test(l));\n    if (headerLineIdx === -1) return [];\n    const cols = lines[headerLineIdx].split('|').map(s => s.trim()).filter(s => s.length > 0);\n    const data = [];\n    for (let i = headerLineIdx + 1; i < lines.length; i++) {\n        const line = lines[i];\n        if (line.includes('|') && !/[+-]/.test(line)) {\n            const vals = line.split('|').map(s => s.trim()).filter(s => s.length > 0);\n            if (vals.length === cols.length) {\n                const row = {};\n                cols.forEach((col, j) => {\n                    const v = vals[j];\n                    row[col] = /^\\d+$/.test(v) ? parseInt(v) : v;\n                });\n                data.push(row);\n            }\n        }\n    }\n    return data;\n}\n\nfunction cancellation_rate(trips, users) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nlet trips = [], users = [];\nif (input.includes(\"Trips table:\")) {\n    const parts = input.split(\"Users table:\");\n    trips = parseAsciiTable(parts[0]);\n    users = parseAsciiTable(parts[1] || \"\");\n} else {\n    try {\n        const lines = input.trim().split('\\n');\n        trips = JSON.parse(lines[0]);\n        users = JSON.parse(lines[1]);\n    } catch(e) {}\n}\nconsole.log(JSON.stringify(cancellation_rate(trips, users)));",
        "c": "#include <stdio.h>\nint main() { printf(\"[]\\n\"); return 0; }"
    }

    test_cases = [{"input": '[{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}, {"id": 2, "client_id": 2, "driver_id": 11, "city_id": 1, "status": "cancelled_by_driver", "request_at": "2013-10-01"}, {"id": 3, "client_id": 3, "driver_id": 12, "city_id": 6, "status": "completed", "request_at": "2013-10-01"}, {"id": 4, "client_id": 4, "driver_id": 13, "city_id": 6, "status": "cancelled_by_client", "request_at": "2013-10-01"}, {"id": 5, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-02"}, {"id": 6, "client_id": 2, "driver_id": 11, "city_id": 6, "status": "completed", "request_at": "2013-10-02"}, {"id": 7, "client_id": 3, "driver_id": 12, "city_id": 6, "status": "completed", "request_at": "2013-10-02"}, {"id": 8, "client_id": 2, "driver_id": 12, "city_id": 12, "status": "completed", "request_at": "2013-10-03"}, {"id": 9, "client_id": 3, "driver_id": 10, "city_id": 12, "status": "completed", "request_at": "2013-10-03"}, {"id": 10, "client_id": 4, "driver_id": 13, "city_id": 12, "status": "cancelled_by_driver", "request_at": "2013-10-03"}]\\n[{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 2, "banned": "Yes", "role": "client"}, {"users_id": 3, "banned": "No", "role": "client"}, {"users_id": 4, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}, {"users_id": 11, "banned": "No", "role": "driver"}, {"users_id": 12, "banned": "No", "role": "driver"}, {"users_id": 13, "banned": "No", "role": "driver"}]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "0.33"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.50"}]', "is_sample": True},
        {"input": '[]\\n[]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "0.00"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.00"}]', "is_sample": True},
        {"input": '[{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}]\\n[{"users_id": 1, "banned": "Yes", "role": "client"}]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "0.00"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.00"}]', "is_sample": False},
        {"input": '[{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "cancelled_by_client", "request_at": "2013-10-01"}]\\n[{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "1.00"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.00"}]', "is_sample": False},
        {"input": '[{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-02"}]\\n[{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "0.00"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.00"}]', "is_sample": False},
        {"input": '[{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}, {"id": 2, "client_id": 2, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}]\\n[{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 2, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "0.00"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.00"}]', "is_sample": False},
        {"input": '[{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "cancelled_by_driver", "request_at": "2013-10-01"}, {"id": 2, "client_id": 2, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}]\\n[{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 2, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "0.50"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.00"}]', "is_sample": False},
        {"input": '[{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}, {"id": 2, "client_id": 1, "driver_id": 11, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}, {"id": 3, "client_id": 1, "driver_id": 12, "city_id": 1, "status": "cancelled_by_client", "request_at": "2013-10-01"}]\\n[{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}, {"users_id": 11, "banned": "No", "role": "driver"}, {"users_id": 12, "banned": "No", "role": "driver"}]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "0.33"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.00"}]', "is_sample": False},
        {"input": '[{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-01"}]\\n[{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "Yes", "role": "driver"}]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "0.00"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.00"}]', "is_sample": False},
        {"input": '[{"id": 1, "client_id": 1, "driver_id": 10, "city_id": 1, "status": "cancelled_by_client", "request_at": "2013-10-03"}, {"id": 2, "client_id": 2, "driver_id": 10, "city_id": 1, "status": "completed", "request_at": "2013-10-03"}]\\n[{"users_id": 1, "banned": "No", "role": "client"}, {"users_id": 2, "banned": "No", "role": "client"}, {"users_id": 10, "banned": "No", "role": "driver"}]', "expected_output": '[{"Day": "2013-10-01", "Cancellation Rate": "0.00"}, {"Day": "2013-10-02", "Cancellation Rate": "0.00"}, {"Day": "2013-10-03", "Cancellation Rate": "0.50"}]', "is_sample": False}]

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
        "topics": ["Database"],
        "companyIndex": 0
    }

    output_path = "1-1000/262_Trips_and_Users.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
