import json
import os

def generate_json():
    problem_id = 1661
    title = "Average Time of Process per Machine"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1661. Average Time of Process per Machine</h3>
<p>The <code>Activity</code> log tracks the start and end times of various processes running on different machines. Each machine carries out several processes. Each process has a starting activity and an ending activity.</p>

<p>The time taken to complete a process is defined as the <code>end_timestamp - start_timestamp</code>.</p>

<p>You are given a list of activities, where each activity contains:</p>
<ul>
    <li><code>machine_id</code>: The ID of the machine.</li>
    <li><code>process_id</code>: The ID of the process.</li>
    <li><code>activity_type</code>: Either 'start' or 'end'.</li>
    <li><code>timestamp</code>: A float representing the time the activity occurred.</li>
</ul>

<p>Calculate the average time each machine takes to complete a process. The average time is the total time for all processes on that machine divided by the number of processes.</p>

<p>Return a list of results containing <code>machine_id</code> and the calculated <code>processing_time</code> (average), rounded to 3 decimal places. The order of the results does not matter.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> activities = [
  {"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 0.712},
  {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 1.520},
  {"machine_id": 0, "process_id": 1, "activity_type": "start", "timestamp": 3.140},
  {"machine_id": 0, "process_id": 1, "activity_type": "end", "timestamp": 4.120},
  {"machine_id": 1, "process_id": 0, "activity_type": "start", "timestamp": 0.550},
  {"machine_id": 1, "process_id": 0, "activity_type": "end", "timestamp": 1.550},
  {"machine_id": 1, "process_id": 1, "activity_type": "start", "timestamp": 0.430},
  {"machine_id": 1, "process_id": 1, "activity_type": "end", "timestamp": 1.420},
  {"machine_id": 2, "process_id": 0, "activity_type": "start", "timestamp": 4.100},
  {"machine_id": 2, "process_id": 0, "activity_type": "end", "timestamp": 4.512},
  {"machine_id": 2, "process_id": 1, "activity_type": "start", "timestamp": 2.500},
  {"machine_id": 2, "process_id": 1, "activity_type": "end", "timestamp": 5.000}
]
<strong>Output:</strong> [
  {"machine_id": 0, "processing_time": 0.894},
  {"machine_id": 1, "processing_time": 0.995},
  {"machine_id": 2, "processing_time": 1.456}
]
<strong>Explanation:</strong>
Machine 0: ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
Machine 1: ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
Machine 2: ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li>The number of activities is between <code>2</code> and <code>100</code>.</li>
    <li>Each <code>(machine_id, process_id)</code> pair has exactly one 'start' and one 'end' activity.</li>
    <li>Processes on a machine do not overlap (for the purposes of this calculation, though this does not affect the formula).</li>
    <li>'start' activity always happens before 'end' activity.</li>
</ul>"""

    input_format = "A list of activity dictionaries, each with machine_id, process_id, activity_type, and timestamp."
    output_format = "A list of dictionaries containing machine_id and the average processing_time rounded to 3 decimal places."
    
    constraints = [
        "1 <= activities.length <= 100",
        "Each process on each machine has exactly one start and one end",
        "timestamp is a float",
        "Rounding to 3 decimal places required"
    ]
    
    explanation = """To solve this efficiently:
1. **Index Activities**: Group start and end times for each process. Use a dictionary with the key `(machine_id, process_id)` to store the start time when encountered.
2. **Calculate Durations**: When the 'end' activity for a process is encountered, calculate `duration = end_time - start_time`.
3. **Aggregate Per Machine**:
   - Maintain `machine_total_time[machine_id]` and `machine_process_count[machine_id]`.
   - For each completed process, add its duration to the total time and increment the count for that machine.
4. **Compute Average**: For each machine, calculate `average = total_time / process_count` and round to 3 decimal places.
5. **Complexity**:
   - **Time**: $O(N)$ where $N$ is the number of activities.
   - **Space**: $O(N)$ to store the intermediate process data."""
    
    answer = """def getAverageTime(activities):
    # key: (machine_id, process_id) -> start_timestamp
    process_starts = {}
    
    # machine_id -> [total_sum, count]
    machine_stats = {}
    
    for act in activities:
        mid = act['machine_id']
        pid = act['process_id']
        atype = act['activity_type']
        ts = act['timestamp']
        
        if atype == 'start':
            process_starts[(mid, pid)] = ts
        else:
            start_ts = process_starts.pop((mid, pid))
            duration = ts - start_ts
            
            if mid not in machine_stats:
                machine_stats[mid] = [0.0, 0]
            machine_stats[mid][0] += duration
            machine_stats[mid][1] += 1
            
    result = []
    for mid in machine_stats:
        avg = machine_stats[mid][0] / machine_stats[mid][1]
        result.append({
            "machine_id": mid,
            "processing_time": round(avg, 3)
        })
        
    return result"""

    boilerplate = {
        "python": "import sys, json\n\ndef getAverageTime(activities):\n    # implementation\n    pass\n\nif __name__ == '__main__':\n    data = json.loads(sys.stdin.read())\n    print(getAverageTime(data))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <map>\n#include <iomanip>\n\nusing namespace std;\n\nstruct Activity {\n    int machine_id;\n    int process_id;\n    string activity_type;\n    double timestamp;\n};\n\nclass Solution {\npublic:\n    // Standardizing as method\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    // Standardizing output as List of Map or custom class\n}",
        "javascript": "/**\n * @param {Object[]} activities\n * @return {Object[]}\n */\nvar getAverageTime = function(activities) {\n    \n};",
        "c": "// Not applicable for SQL - Standardizing as Algorithmic"
    }

    test_cases = [
        {"input": json.dumps([
            {"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 0.712},
            {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 1.520},
            {"machine_id": 0, "process_id": 1, "activity_type": "start", "timestamp": 3.140},
            {"machine_id": 0, "process_id": 1, "activity_type": "end", "timestamp": 4.120},
            {"machine_id": 1, "process_id": 0, "activity_type": "start", "timestamp": 0.550},
            {"machine_id": 1, "process_id": 0, "activity_type": "end", "timestamp": 1.550},
            {"machine_id": 1, "process_id": 1, "activity_type": "start", "timestamp": 0.430},
            {"machine_id": 1, "process_id": 1, "activity_type": "end", "timestamp": 1.420},
            {"machine_id": 2, "process_id": 0, "activity_type": "start", "timestamp": 4.100},
            {"machine_id": 2, "process_id": 0, "activity_type": "end", "timestamp": 4.512},
            {"machine_id": 2, "process_id": 1, "activity_type": "start", "timestamp": 2.500},
            {"machine_id": 2, "process_id": 1, "activity_type": "end", "timestamp": 5.000}
        ]), "expected_output": json.dumps([
            {"machine_id": 0, "processing_time": 0.894},
            {"machine_id": 1, "processing_time": 0.995},
            {"machine_id": 2, "processing_time": 1.456}
        ]), "is_sample": True},
        {"input": json.dumps([
            {"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 1.0},
            {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 2.0}
        ]), "expected_output": json.dumps([{"machine_id": 0, "processing_time": 1.0}]), "is_sample": False},
        {"input": json.dumps([
            {"machine_id": 1, "process_id": 1, "activity_type": "start", "timestamp": 10.5},
            {"machine_id": 1, "process_id": 1, "activity_type": "end", "timestamp": 11.5},
            {"machine_id": 1, "process_id": 2, "activity_type": "start", "timestamp": 12.0},
            {"machine_id": 1, "process_id": 2, "activity_type": "end", "timestamp": 14.0}
        ]), "expected_output": json.dumps([{"machine_id": 1, "processing_time": 1.5}]), "is_sample": False},
        {"input": json.dumps([
            {"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 0.0},
            {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 0.001}
        ]), "expected_output": json.dumps([{"machine_id": 0, "processing_time": 0.001}]), "is_sample": False},
        {"input": json.dumps([
            {"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 0.000},
            {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 0.33333333}
        ]), "expected_output": json.dumps([{"machine_id": 0, "processing_time": 0.333}]), "is_sample": False},
        {"input": json.dumps([
            {"machine_id": 5, "process_id": 5, "activity_type": "start", "timestamp": 100.0},
            {"machine_id": 5, "process_id": 5, "activity_type": "end", "timestamp": 200.0}
        ]), "expected_output": json.dumps([{"machine_id": 5, "processing_time": 100.0}]), "is_sample": False},
        {"input": json.dumps([
            {"machine_id": 1, "process_id": 1, "activity_type": "start", "timestamp": 1.0},
            {"machine_id": 1, "process_id": 1, "activity_type": "end", "timestamp": 2.0},
            {"machine_id": 2, "process_id": 1, "activity_type": "start", "timestamp": 1.0},
            {"machine_id": 2, "process_id": 1, "activity_type": "end", "timestamp": 3.0}
        ]), "expected_output": json.dumps([{"machine_id": 1, "processing_time": 1.0}, {"machine_id": 2, "processing_time": 2.0}]), "is_sample": False},
        {"input": '[]', "expected_output": '[]', "is_sample": False},
        {"input": json.dumps([{"machine_id": i, "process_id": 0, "activity_type": "start", "timestamp": 0.0} for i in range(50)] + [{"machine_id": i, "process_id": 0, "activity_type": "end", "timestamp": 1.2345} for i in range(50)]), "expected_output": json.dumps([{"machine_id": i, "processing_time": 1.235} for i in range(50)]), "is_sample": False},
        {"input": json.dumps([
            {"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 0.0},
            {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 1.0},
            {"machine_id": 0, "process_id": 1, "activity_type": "start", "timestamp": 1.0},
            {"machine_id": 0, "process_id": 1, "activity_type": "end", "timestamp": 3.0}
        ]), "expected_output": json.dumps([{"machine_id": 0, "processing_time": 1.5}]), "is_sample": False}
    ]

    # Note: Using sorted output for consistent expected output in test cases if needed, 
    # but the problem says order doesn't matter.

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
        "topics": ["Array", "Hash Table", "Simulation"],
        "companyIndex": 0
    }

    output_path = "1001-2000/1661_Average_Time_of_Process_per_Machine.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
