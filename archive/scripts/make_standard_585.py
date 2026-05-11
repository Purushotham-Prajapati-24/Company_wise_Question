import json
import os

def generate_json():
    problem_id = 585
    title = "Investments in 2016"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>585. Investments in 2016</h3>
<p>Write a solution to report the sum of all total investment values in 2016 <code>tiv_2016</code> for all policyholders who:</p>

<ol>
	<li>have the same <code>tiv_2015</code> value as one or more other policyholders, and</li>
	<li>are not located in the same city as any other policyholder (i.e., the (<code>lat</code>, <code>lon</code>) attribute pairs must be unique).</li>
</ol>

<p>Round <code>tiv_2016</code> to <b>two decimal places</b>.</p>

<p>&nbsp;</p>
<p><strong>Table schema:</strong></p>
<pre>
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
pid is the primary key (column with unique values) for this table.
Each row of this table contains information about one insurance policy.
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
1,10,5,10,10
2,20,20,20,20
3,10,30,20,20
4,10,40,40,40

<strong>Output:</strong> 
45.00

<strong>Explanation:</strong> 
The first record in the table, with pid 1, and the last record, with pid 4, meet both of the two criteria.
The tiv_2015 value 10 is the same as the third and fourth records, and their (lat, lon) values are unique.

The second record does not meet the criteria because its tiv_2015 is not that of any other policyholders.

The third record does not meet the criteria because its (lat, lon) pair (20, 20) is the same as the second record.
Therefore, the result is the sum of tiv_2016 of the first and fourth record, which is 5 + 40 = 45.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of records is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>tiv_2015</code>, <code>tiv_2016</code>, <code>lat</code>, <code>lon</code> are in the range <code>[1, 1000]</code>.</li>
</ul>"""

    input_format = "Each line contains a record: 'pid,tiv_2015,tiv_2016,lat,lon'."
    output_format = "A single float value rounded to 2 decimal places."
    
    constraints = [
        "1 <= n_records <= 10^4",
        "Unique (lat, lon) required.",
        "Shared tiv_2015 required.",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To calculate the sum according to the criteria:
1. **The Strategy**:
   - We need to identify policies that satisfy two conditions.
   - **Condition 1**: `tiv_2015` count > 1.
   - **Condition 2**: `(lat, lon)` count == 1.
2. **Frequency Mapping**:
   - Use two hash maps (dictionaries):
     - `count_2015`: Maps each `tiv_2015` value to its total occurrences.
     - `count_lat_lon`: Maps each `(lat, lon)` tuple to its total occurrences.
3. **Calculating the Sum**:
   - Iterate through all records again.
   - Check if `count_2015[tiv_2015] > 1` AND `count_lat_lon[(lat, lon)] == 1`.
   - If both conditions are met, add `tiv_2016` to the total sum.
4. **Rounding**:
   - Return the sum rounded to 2 decimal places (e.g., `"{:.2f}".format(total)`).
5. **Complexity**:
   - Time Complexity: O(N) to build the maps and O(N) to sum the result.
   - Space Complexity: O(N) to store the maps."""
    
    answer = """from collections import defaultdict
def sumInvestments(records: list[dict]) -> float:
    count_2015 = defaultdict(int)
    count_loc = defaultdict(int)
    
    for r in records:
        count_2015[r['tiv_2015']] += 1
        count_loc[(r['lat'], r['lon'])] += 1
        
    total = 0.0
    for r in records:
        if count_2015[r['tiv_2015']] > 1 and count_loc[(r['lat'], r['lon'])] == 1:
            total += r['tiv_2016']
            
    return round(total, 2)"""

    boilerplate = {
        "python": "import sys\nfrom collections import defaultdict\n\ndef sumInvestments(records):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    records = []\n    for line in lines:\n        if not line: continue\n        parts = line.split(',')\n        records.append({\n            'pid': int(parts[0]),\n            'tiv_2015': float(parts[1]),\n            'tiv_2016': float(parts[2]),\n            'lat': float(parts[3]),\n            'lon': float(parts[4])\n        })\n    print(\"{:.2f}\".format(sumInvestments(records)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <iomanip>\n\nusing namespace std;\n\nstruct Record {\n    int pid;\n    double t2015, t2016, lat, lon;\n};\n\nint main() {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        // User logic\n    }\n}",
        "javascript": "function solve(records) {\n    // User logic\n}",
        "c": "void solve() {\n    // User logic\n}"
    }

    test_cases = [
        {"input": "1,10,5,10,10\\n2,20,20,20,20\\n3,10,30,20,20\\n4,10,40,40,40", "expected_output": "45.00", "is_sample": True},
        {"input": "1,10,10,10,10\\n2,20,20,20,20", "expected_output": "0.00", "is_sample": True},
        {"input": "1,10,10,10,10\\n2,10,10,20,20", "expected_output": "20.00", "is_sample": False},
        {"input": "1,10,10,10,10\\n2,10,20,10,10", "expected_output": "0.00", "is_sample": False},
        {"input": "1,5,5,1,1\\n2,5,10,2,2\\n3,5,15,3,3", "expected_output": "30.00", "is_sample": False},
        {"input": "1,5,5,1,1\\n2,6,10,2,2\\n3,7,15,3,3", "expected_output": "0.00", "is_sample": False},
        {"input": "1,10,10,1,1\\n2,10,10,1,1", "expected_output": "0.00", "is_sample": False},
        # Stress cases
        {"input": "\\n".join([f"{i},100,{float(i)},{float(i)},{float(i)}" for i in range(1, 5001)]), "expected_output": "12502500.00", "is_sample": False},
        {"input": "\\n".join([f"{i},{float(i)},{float(i)},10,10" for i in range(1, 5001)]), "expected_output": "0.00", "is_sample": False},
        {"input": "1,10.5,5.5,1.1,2.2\\n2,10.5,4.5,3.3,4.4", "expected_output": "10.00", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Math"],
        "companyIndex": 0
    }

    output_path = "401-600/585_Investments_in_2016.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
