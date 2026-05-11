import json
import os

def generate_json():
    problem_id = 1029
    title = "Two City Scheduling"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1029. Two City Scheduling</h3>
<p>A company is planning to interview <code>2n</code> people. You are given an array <code>costs</code> where <code>costs[i] = [aCost<sub>i</sub>, bCost<sub>i</sub>]</code>, the cost to fly the <code>i<sup>th</sup></code> person to city <code>A</code> is <code>aCost<sub>i</sub></code>, and the cost to fly the <code>i<sup>th</sup></code> person to city <code>B</code> is <code>bCost<sub>i</sub></code>.</p>

<p>Return <em>the minimum cost to fly every person to a city</em> such that exactly <code>n</code> people arrive in each city.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> costs = [[10,20],[30,200],[400,50],[30,20]]
<strong>Output:</strong> 110
<strong>Explanation: </strong>
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
<strong>Output:</strong> 1859
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
<strong>Output:</strong> 3086
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 * n == costs.length</code></li>
	<li><code>2 &lt;= costs.length &lt;= 100</code></li>
	<li><code>costs.length</code> is even.</li>
	<li><code>1 &lt;= aCost<sub>i</sub>, bCost<sub>i</sub> &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line containing the 2D JSON array `costs`."
    output_format = "An integer representing the minimum cost."

    constraints = [
        "2 * n == costs.length",
        "2 <= costs.length <= 100",
        "costs.length is even",
        "1 <= aCost_i, bCost_i <= 1000"
    ]

    explanation = """To minimize total cost, calculate the difference `aCost - bCost` for each person. 
This difference represents how much more it costs to send someone to City A instead of City B.
Sort people by this difference. Send the first half (those with the most negative difference, i.e., cheapest for A relatively) to City A.
Send the second half to City B."""

    answer = """class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        total = 0
        n = len(costs) // 2
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        costs = json.loads(raw)
        sol = Solution()
        print(sol.twoCitySchedCost(costs))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        // User logic here
        return 0;
    }
};

vector<vector<int>> parse2DArray(string s) {
    vector<vector<int>> res;
    vector<int> current;
    string temp = "";
    int open = 0;
    for (char c : s) {
        if (c == '[') open++;
        else if (c == ']') {
            if (current.size() > 0 || temp != "") {
                if (temp != "") current.push_back(stoi(temp));
                res.push_back(current);
                current.clear();
                temp = "";
            }
            open--;
        } else if (c == ',') {
            if (open == 2 && temp != "") {
                current.push_back(stoi(temp));
                temp = "";
            }
        } else if (isdigit(c) || c == '-') {
            temp += c;
        }
    }
    return res;
}

int main() {
    string line;
    if (getline(cin, line)) {
        vector<vector<int>> costs = parse2DArray(line);
        Solution sol;
        cout << sol.twoCitySchedCost(costs) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int twoCitySchedCost(int[][] costs) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            int[][] costs = parse(sc.nextLine());
            System.out.println(new Solution().twoCitySchedCost(costs));
        }
    }
    private static int[][] parse(String s) {
        s = s.trim();
        if (s.equals("[]") || s.equals("[[]]")) return new int[0][0];
        s = s.substring(2, s.length() - 2);
        String[] rows = s.split("\\\\],\\\\[");
        int[][] res = new int[rows.length][];
        for (int i = 0; i < rows.length; i++) {
            String[] parts = rows[i].split(",");
            res[i] = new int[parts.length];
            for (int j = 0; j < parts.length; j++) res[i][j] = Integer.parseInt(parts[j].trim());
        }
        return res;
    }
}""",
        "javascript": """var twoCitySchedCost = function(costs) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(twoCitySchedCost(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int twoCitySchedCost(int** costs, int costsSize, int* costsColSize) {
    // User logic here
    return 0;
}

int** parse2DArray(int* rowSize, int** colSizes) {
    char c;
    while (scanf(" %c", &c) == 1 && c != '[');
    int capacity = 10, r = 0;
    int** arr = malloc(capacity * sizeof(int*));
    *colSizes = malloc(capacity * sizeof(int));
    while (scanf(" %c", &c) == 1 && c == '[') {
        int c_cap = 10, s = 0;
        int* current = malloc(c_cap * sizeof(int));
        int val;
        while (scanf("%d", &val) == 1) {
            if (s == c_cap) { c_cap *= 2; current = realloc(current, c_cap * sizeof(int)); }
            current[s++] = val;
            while (scanf(" %c", &c) == 1 && (c == ' ' || c == ','));
            if (c == ']') break;
            ungetc(c, stdin);
        }
        if (r == capacity) { 
            capacity *= 2; 
            arr = realloc(arr, capacity * sizeof(int*)); 
            *colSizes = realloc(*colSizes, capacity * sizeof(int));
        }
        arr[r] = current;
        (*colSizes)[r++] = s;
        while (scanf(" %c", &c) == 1 && (c == ' ' || c == ','));
        if (c == ']') break;
        ungetc(c, stdin);
    }
    *rowSize = r;
    return arr;
}

int main() {
    int rSize;
    int* colSizes;
    int** costs = parse2DArray(&rSize, &colSizes);
    printf("%d\\n", twoCitySchedCost(costs, rSize, colSizes));
    for (int i = 0; i < rSize; i++) free(costs[i]);
    free(costs); free(colSizes);
    return 0;
}"""
    }

    def solve(costs):
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum(c[0] for c in costs[:n]) + sum(c[1] for c in costs[n:])

    test_cases_data = [
        [[10,20],[30,200],[400,50],[30,20]], # LC Sample 1
        [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], # LC Sample 2
        [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]], # LC Sample 3
        [[10,10],[10,10]],
        [[1,2],[3,4],[5,6],[7,8]],
        [[100,10],[100,10]],
        [[10,100],[10,100]],
        # Stress tests (last 3)
        [[100,200],[200,100]] * 50,
        [[i, i+10] for i in range(100)],
        [[i+10, i] for i in range(100)]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Greedy", "Sorting"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
