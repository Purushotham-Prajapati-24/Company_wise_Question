import json
import os

def generate_json():
    problem_id = 568
    title = "Maximum Vacation Days"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>568. Maximum Vacation Days</h3>
<p>LeetCode wants to give one of its best employees the option to travel among <code>n</code> cities to collect algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.</p>

<ol>
    <li>You can only travel among <code>n</code> cities, represented by indexes from <code>0</code> to <code>n - 1</code>. Initially, you are in the city indexed <code>0</code> on Monday.</li>
    <li>The cities are connected by flights. The flights are represented as an <code>n x n</code> matrix (not necessarily symmetrical), called <code>flights</code> representing the airline status from the city <code>i</code> to the city <code>j</code>. If there is no flight from the city <code>i</code> to the city <code>j</code>, <code>flights[i][j] == 0</code>; Otherwise, <code>flights[i][j] == 1</code>. Also, <code>flights[i][i] == 0</code> for all <code>i</code>.</li>
    <li>You totally have <code>k</code> weeks (each week has 7 days) to travel. You can only take flights at most once per week and can only take flights on each week's Monday morning. Since flight time is so short, we don't consider the impact of flight time.</li>
    <li>For each city, you can only have restricted vacation days in different weeks, given an <code>n x k</code> matrix called <code>days</code> representing this relationship. For the value of <code>days[i][j]</code>, it represents the maximum days you could take a vacation in the city <code>i</code> in the week <code>j</code>.</li>
</ol>

<p>You're given the <code>flights</code> matrix and <code>days</code> matrix, and you need to output the maximum vacation days you could take during <code>k</code> weeks.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
<strong>Output:</strong> 12
<strong>Explanation:</strong> 
One of the best strategies is:
1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day. 
2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
3rd week : stay at city 2, and play 3 days and work 4 days.
Ans = 6 + 3 + 3 = 12.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
Since there are no flights that enable you to move to another city, you have to stay at city 0 for the whole 3 weeks. 
For each week, you only have one day to play and six days to work. 
So the maximum number of vacation days is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == flights.length == flights[i].length == days.length</code></li>
    <li><code>k == days[i].length</code></li>
    <li><code>1 &lt;= n, k &lt;= 100</code></li>
    <li><code>flights[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
    <li><code>0 &lt;= days[i][j] &lt;= 7</code></li>
</ul>"""

    input_format = "Two lines: Line 1: A JSON 2D arrays of integers `flights`. Line 2: A JSON 2D array of integers `days`."
    output_format = "An integer: the maximum vacation days."

    constraints = [
        "n == flights.length == flights[i].length == days.length",
        "k == days[i].length",
        "1 <= n, k <= 100",
        "flights[i][j] is either 0 or 1",
        "0 <= days[i][j] <= 7"
    ]

    explanation = """Use dynamic programming. dp[i][w] is the max vacation days taking taking week w in city i. 
At week w, to be in city i, you must have been in some city j (where flights[j][i] == 1 or j == i) at week w - 1. 
dp[i][w] = max(dp[j][w-1]) + days[i][w] for all valid j. 
Initialize week 0 considering only valid flights from city 0, and then process week by week.
Since dp relies only on the previous week, we can use a 1D DP array."""

    answer = """class Solution:
    def maxVacationDays(self, flights: list[list[int]], days: list[list[int]]) -> int:
        n = len(flights)
        k = len(days[0])
        
        dp = [-1] * n
        dp[0] = 0
        
        for p in range(k):
            temp = [-1] * n
            for i in range(n):
                for j in range(n):
                    if dp[i] != -1 and (i == j or flights[i][j] == 1):
                        temp[j] = max(temp[j], dp[i] + days[j][p])
            dp = temp
            
        return max(dp)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def maxVacationDays(self, flights: list[list[int]], days: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        flights = json.loads(raw[0])
        days = json.loads(raw[1])
        sol = Solution()
        print(sol.maxVacationDays(flights, days))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxVacationDays(vector<vector<int>>& flights, vector<vector<int>>& days) {
        // User logic here
        return 0;
    }
};

vector<vector<int>> parse2D(string input) {
    vector<vector<int>> res;
    vector<int> row;
    int depth = 0;
    size_t p = 0;
    while (p < input.length()) {
        if (input[p] == '[') { depth++; p++; }
        else if (input[p] == ']') {
            depth--;
            if (depth == 1) { res.push_back(row); row.clear(); }
            p++;
        } else if (isdigit(input[p]) || input[p] == '-') {
            size_t next;
            row.push_back(stoi(input.substr(p), &next));
            p += next;
        } else p++;
    }
    return res;
}

int main() {
    string str1, str2;
    if (getline(cin, str1) && getline(cin, str2)) {
        vector<vector<int>> flights = parse2D(str1);
        vector<vector<int>> days = parse2D(str2);
        Solution sol;
        cout << sol.maxVacationDays(flights, days) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int maxVacationDays(int[][] flights, int[][] days) {
        // User logic here
        return 0;
    }
}

public class Main {
    static int[][] parse2D(String raw) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> row = new ArrayList<>();
        int depth = 0, i = 0;
        while (i < raw.length()) {
            char c = raw.charAt(i);
            if (c == '[') { depth++; i++; }
            else if (c == ']') {
                depth--;
                if (depth == 1) { res.add(new ArrayList<>(row)); row.clear(); }
                i++;
            } else if (Character.isDigit(c) || c == '-') {
                int end = i;
                while (end < raw.length() && (Character.isDigit(raw.charAt(end)) || raw.charAt(end) == '-')) end++;
                row.add(Integer.parseInt(raw.substring(i, end)));
                i = end;
            } else i++;
        }
        int[][] arr = new int[res.size()][];
        for (int r = 0; r < res.size(); r++) {
            arr[r] = new int[res.get(r).size()];
            for (int c = 0; c < res.get(r).size(); c++) arr[r][c] = res.get(r).get(c);
        }
        return arr;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String str1 = sc.nextLine().trim();
            if (sc.hasNextLine()) {
                String str2 = sc.nextLine().trim();
                int[][] flights = parse2D(str1);
                int[][] days = parse2D(str2);
                Solution sol = new Solution();
                System.out.println(sol.maxVacationDays(flights, days));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} flights
 * @param {number[][]} days
 * @return {number}
 */
var maxVacationDays = function(flights, days) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const flights = JSON.parse(input[0]);
    const days = JSON.parse(input[1]);
    console.log(maxVacationDays(flights, days));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int maxVacationDays(int** flights, int flightsSize, int* flightsColSize, int** days, int daysSize, int* daysColSize) {
    // User logic here
    return 0;
}

int** parse2D(char* input, int* outRows, int** outCols) {
    int nums[40000], ncount = 0;
    int rowSizes[1000], nrows = 0;
    int rowCount = 0;
    int depth = 0, i = 0;
    while (input[i]) {
        if (input[i] == '[') { depth++; if (depth == 2) rowCount = 0; i++; }
        else if (input[i] == ']') {
            depth--;
            if (depth == 1) rowSizes[nrows++] = rowCount;
            i++;
        } else if (isdigit(input[i]) || input[i] == '-') {
            int val, off = 0;
            sscanf(input + i, "%d%n", &val, &off);
            if (!off) { i++; continue; }
            nums[ncount++] = val;
            rowCount++;
            i += off;
        } else i++;
    }
    int** res = (int**)malloc(nrows * sizeof(int*));
    *outCols = (int*)malloc(nrows * sizeof(int));
    *outRows = nrows;
    int idx = 0;
    for (int r = 0; r < nrows; r++) {
        res[r] = (int*)malloc(rowSizes[r] * sizeof(int));
        (*outCols)[r] = rowSizes[r];
        for (int c = 0; c < rowSizes[r]; c++) res[r][c] = nums[idx++];
    }
    return res;
}

int main() {
    char str1[1000000], str2[1000000];
    if (fgets(str1, sizeof(str1), stdin) && fgets(str2, sizeof(str2), stdin)) {
        int r1, *c1; int** flights = parse2D(str1, &r1, &c1);
        int r2, *c2; int** days = parse2D(str2, &r2, &c2);
        printf("%d\\n", maxVacationDays(flights, r1, c1, days, r2, c2));
        for (int i = 0; i < r1; i++) free(flights[i]); free(flights); free(c1);
        for (int i = 0; i < r2; i++) free(days[i]); free(days); free(c2);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[[0,1,1],[1,0,1],[1,1,0]]\\n[[1,3,1],[6,0,3],[3,3,3]]", "expected_output": "12", "is_sample": True},
        {"input": "[[0,0,0],[0,0,0],[0,0,0]]\\n[[1,1,1],[7,7,7],[7,7,7]]", "expected_output": "3", "is_sample": True},
        {"input": "[[0,1,1],[1,0,1],[1,1,0]]\\n[[7,0,0],[0,7,0],[0,0,7]]", "expected_output": "21", "is_sample": False},
        {"input": "[[0,1,0],[0,0,1],[0,0,0]]\\n[[0,0,0],[0,7,0],[0,0,7]]", "expected_output": "14", "is_sample": False},
        {"input": "[[0,0,1],[1,0,0],[0,1,0]]\\n[[7,0,0],[0,7,0],[0,0,7]]", "expected_output": "14", "is_sample": False},
        {"input": "[[0,1],[1,0]]\\n[[2,2,2],[3,3,3]]", "expected_output": "9", "is_sample": False},
        {"input": "[[0]]\\n[[5]]", "expected_output": "5", "is_sample": False},
        {"input": "[[0,1],[0,0]]\\n[[0,0],[7,7]]", "expected_output": "14", "is_sample": False},
        
        {"input": "[[" + ",".join(["1"]*10) + "]]*10".replace("]*10", "]") + "\\n[[" + ",".join(["1"]*10) + "]]*10".replace("]*10", "]").replace("1]*10", "1], [1") , "expected_output": None, "is_sample": False},
        {"input": "[[" + ",".join(["1"]*10) + "]]*10".replace("]*10", "]") + "\\n[[" + ",".join(["1"]*10) + "]]*10".replace("]*10", "]").replace("1]*10", "1], [1") , "expected_output": None, "is_sample": False}
    ]

    r1_stress1 = "[" + ",".join(["[" + ",".join(["1" if i != j else "0" for j in range(50)]) + "]" for i in range(50)]) + "]"
    r2_stress1 = "[" + ",".join(["[" + ",".join(["7" for j in range(50)]) + "]" for i in range(50)]) + "]"
    test_cases[8] = {"input": f"{r1_stress1}\\n{r2_stress1}", "expected_output": str(50*7), "is_sample": False}

    r1_stress2 = "[" + ",".join(["[" + ",".join(["0" for j in range(100)]) + "]" for i in range(100)]) + "]"
    r2_stress2 = "[" + ",".join(["[" + ",".join(["5" for j in range(100)]) + "]" for i in range(100)]) + "]"
    test_cases[9] = {"input": f"{r1_stress2}\\n{r2_stress2}", "expected_output": str(100*5), "is_sample": False}


    data = {
        "question_id": problem_id,
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
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Dynamic Programming", "Matrix"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
