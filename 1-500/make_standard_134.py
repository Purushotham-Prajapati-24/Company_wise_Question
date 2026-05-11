import json
import os

def generate_json():
    problem_id = 134
    title = "Gas Station"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>134. Gas Station</h3>
<p>There are <code>n</code> gas stations along a circular route, where the amount of gas at the <code>i<sup>th</sup></code> station is <code>gas[i]</code>.</p>

<p>You have a car with an unlimited gas tank and it costs <code>cost[i]</code> of gas to travel from the <code>i<sup>th</sup></code> station to its next <code>(i + 1)<sup>th</sup></code> station. You begin the journey with an empty tank at one of the gas stations.</p>

<p>Given two integer arrays <code>gas</code> and <code>cost</code>, return <em>the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return</em> <code>-1</code>. If there exists a solution, it is <strong>guaranteed</strong> to be <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> gas = [1,2,3,4,5], cost = [3,4,5,1,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your cost is 1. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your cost is 2. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your cost is 3. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your cost is 4. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your tank = 5 - 5 = 0.
Anyway, you now have 0 gas and arrive at station 3.
Therefore, return 3 as the starting index.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> gas = [2,3,4], cost = [3,4,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2. Fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your cost is 3. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your cost is 3. Your tank = 3 - 3 + 3 = 3
Travel to station 2. Your cost is 4. You need 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == gas.length == cost.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= gas[i], cost[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two lines: first, an array 'gas'; second, an array 'cost'."
    output_format = "An integer representing the unique starting index, or -1."
    
    constraints = [
        "1 <= n <= 10^5",
        "0 <= gas[i], cost[i] <= 10^4",
        "If a solution exists, it is unique."
    ]
    
    explanation = """To find the unique starting gas station:
1. **Total Sufficiency**: If `sum(gas) < sum(cost)`, it's impossible to complete the circuit. Return -1 immediately.
2. **Greedy Traversal**:
   - Start from index 0. Track `total_balance` and `current_balance`.
   - Iterate through stations. If `current_balance` drops below zero, it means the current `start_node` (and any node between it and the current index) cannot be the starting point.
   - Set `start_node = current_index + 1` and reset `current_balance = 0`.
3. **Complexity**:
   - Time Complexity: O(N) because we iterate through the list once.
   - Space Complexity: O(1) for balance and index pointers."""
    
    answer = """class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_balance = 0
        start_node = 0
        for i in range(len(gas)):
            total_balance += gas[i] - cost[i]
            if total_balance < 0:
                # Reset starting point
                total_balance = 0
                start_node = i + 1
        
        return start_node"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef canCompleteCircuit(gas, cost):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if not lines: sys.exit()\n    gas = json.loads(lines[0])\n    cost = json.loads(lines[1])\n    print(canCompleteCircuit(gas, cost))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nint canCompleteCircuit(vector<int>& gas,vector<int>& cost){\n    // User logic here\n    return -1;\n}\nint main(){\n    auto parseArr=[](string s){\n        vector<int> v; s=s.substr(1,s.size()-2);\n        stringstream ss(s); string t;\n        while(getline(ss,t,',')){if(!t.empty())v.push_back(stoi(t));}\n        return v;\n    };\n    string l1,l2;\n    if(!getline(cin,l1)||!getline(cin,l2)) return 0;\n    vector<int> gas=parseArr(l1), cost=parseArr(l2);\n    cout<<canCompleteCircuit(gas,cost)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int canCompleteCircuit(int[] gas, int[] cost) {\n        // User logic here\n        return -1;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String l1=br.readLine().trim(), l2=br.readLine().trim();\n        l1=l1.substring(1,l1.length()-1); l2=l2.substring(1,l2.length()-1);\n        String[] g=l1.split(\",\"), c=l2.split(\",\");\n        int[] gas=new int[g.length], cost=new int[c.length];\n        for(int i=0;i<g.length;i++) gas[i]=Integer.parseInt(g[i].trim());\n        for(int i=0;i<c.length;i++) cost[i]=Integer.parseInt(c[i].trim());\n        System.out.println(canCompleteCircuit(gas,cost));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction canCompleteCircuit(gas,cost){\n    // User logic here\n    return -1;\n}\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=2){\n  const gas=JSON.parse(lines[0]), cost=JSON.parse(lines[1]);\n  console.log(canCompleteCircuit(gas,cost));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize){\n    // User logic here\n    return -1;\n}\nint main(){\n    char buf[4000000];\n    if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    // parse JSON array\n    int arr[100001],cnt=0; char*tok=strtok(buf,\"[],\\n\\r \");\n    while(tok&&cnt<100001){arr[cnt++]=atoi(tok);tok=strtok(NULL,\"[],\\n\\r \");}\n    int gas[100001],cost[100001],g=0,c=0;\n    // second line\n    char buf2[4000000];\n    if(!fgets(buf2,sizeof(buf2),stdin)) return 0;\n    tok=strtok(buf2,\"[],\\n\\r \");\n    while(tok&&c<100001){cost[c++]=atoi(tok);tok=strtok(NULL,\"[],\\n\\r \");}\n    for(int i=0;i<cnt;i++) gas[i]=arr[i];\n    printf(\"%d\\n\",canCompleteCircuit(gas,cnt,cost,c)); return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,3,4,5]\\n[3,4,5,1,2]", "expected_output": "3", "is_sample": True},
        {"input": "[2,3,4]\\n[3,4,3]", "expected_output": "-1", "is_sample": True},
        {"input": "[5,1,2,3,4]\\n[4,4,1,5,1]", "expected_output": "4", "is_sample": False},
        {"input": "[1,2,3,4]\\n[1,2,3,4]", "expected_output": "0", "is_sample": False},
        {"input": "[0,0,0,5]\\n[1,1,1,2]", "expected_output": "3", "is_sample": False},
        {"input": "[10]\\n[5]", "expected_output": "0", "is_sample": False},
        {"input": "[2,0,0,0,0]\\n[0,1,0,0,0]", "expected_output": "0", "is_sample": False},
        # Stress Tests (N=10^5)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    # Stress 8: All equal but failure
    gas8 = [1] * 100000
    cost8 = [1] * 99999 + [2]
    test_cases[7] = {"input": json.dumps(gas8) + "\\n" + json.dumps(cost8), "expected_output": "-1", "is_sample": False}
    
    # Stress 9: Only the last one works
    gas9 = [1] * 99999 + [100000]
    cost9 = [2] * 99999 + [1]
    test_cases[8] = {"input": json.dumps(gas9) + "\\n" + json.dumps(cost9), "expected_output": "99999", "is_sample": False}
    
    # Stress 10: Big values
    gas10 = [10000] * 100000
    cost10 = [5000] * 100000
    test_cases[9] = {"input": json.dumps(gas10) + "\\n" + json.dumps(cost10), "expected_output": "0", "is_sample": False}

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
        "topics": ["Array", "Greedy"],
        "companyIndex": 0
    }

    output_path = "1-200/134_Gas_Station.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
