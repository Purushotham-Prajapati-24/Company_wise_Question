import json
import os
import collections

def generate_json():
    problem_id = 1086
    title = "High Five"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1086. High Five</h3>
<p>Given a list of scores of different students, return the average score of each student's <strong>top five scores</strong> in the <strong>order of each student's id</strong>.</p>

<p>Each entry <code>items[i]</code> has <code>items[i][0]</code> the student's id and <code>items[i][1]</code> the student's score.  The average score is calculated using integer division.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
<strong>Output:</strong> [[1,87],[2,88]]
<strong>Explanation:</strong> 
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five scores are 100, 92, 91, 87, and 65. Their average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five scores are 100, 97, 93, 77, and 76. Their average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average is 88.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= items.length &lt;= 1000</code></li>
	<li><code>items[i].length == 2</code></li>
	<li>The IDs of the students is between <code>1</code> to <code>1000</code></li>
	<li>The score of the students is between <code>1</code> to <code>100</code></li>
	<li>For each student, there are <strong>at least five scores</strong>.</li>
</ul>
"""

    input_format = "A 2D array `items` where each element is `[student_id, score]`, provided as `[items]` in JSON."
    output_format = "A 2D array of `[id, average]` sorted by `id`."

    constraints = [
        "1 <= items.length <= 1000",
        "items[i].length == 2",
        "1 <= ID <= 1000",
        "1 <= Score <= 100",
        "At least five scores per student"
    ]

    explanation = """To calculate the top five average for each student:
1. Store all scores for each student in a hash map where the key is the student ID and the value is a list of scores.
2. For each student, sort their scores in descending order.
3. Take the first five scores, calculate their sum, and then the average using integer division (`sum // 5`).
4. Collect the results as `[id, average]` pairs.
5. Sort the resulting list by student ID and return it."""

    answer = """class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        scores = collections.defaultdict(list)
        for sid, score in items:
            scores[sid].append(score)
        
        res = []
        for sid in sorted(scores.keys()):
            top5 = sorted(scores[sid], reverse=True)[:5]
            avg = sum(top5) // 5
            res.append([sid, avg])
        return res"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        items = json.loads(raw)
        if isinstance(items[0], list) and not isinstance(items[0][0], list):
             pass # Already [sid, score] list
        elif isinstance(items[0], list) and isinstance(items[0][0], list):
             items = items[0]
        sol = Solution()
        print(sol.highFive(items))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        vector<vector<int>> items;
        if (j.is_array() && j.size() > 0 && j[0][0].is_array()) items = j[0].get<vector<vector<int>>>();
        else items = j.get<vector<vector<int>>>();
        Solution sol;
        vector<vector<int>> res = sol.highFive(items);
        cout << json(res).dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int[][] highFive(int[][] items) {
        // User logic here
        return new int[0][0];
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object raw = mapper.readValue(sc.nextLine(), Object.class);
            int[][] items;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)((List)raw).get(0)).get(0) instanceof List) {
                items = mapper.convertValue(((List)raw).get(0), int[][].class);
            } else {
                items = mapper.convertValue(raw, int[][].class);
            }
            int[][] res = new Solution().highFive(items);
            System.out.println(Arrays.deepToString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var highFive = function(items) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let items = JSON.parse(input);
    if (Array.isArray(items[0]) && Array.isArray(items[0][0])) items = items[0];
    const res = highFive(items);
    console.log(JSON.stringify(res));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int** highFive(int** items, int itemsSize, int* itemsColSize, int* returnSize, int** returnColumnSizes) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 128, s = 0;
    int** items = malloc(cap * sizeof(int*));
    int* cols = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && c != '[' && c != ']');
        if (c == EOF || c == ']') break;
        int row_cap = 2, row_size = 0;
        int* row = malloc(row_cap * sizeof(int));
        while (1) {
            while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
            if (c == EOF || c == ']') break;
            ungetc(c, stdin);
            if (row_size >= row_cap) { row_cap *= 2; row = realloc(row, row_cap * sizeof(int)); }
            scanf("%d", &row[row_size++]);
        }
        if (s >= cap) { cap *= 2; items = realloc(items, cap * sizeof(int*)); cols = realloc(cols, cap * sizeof(int)); }
        items[s] = row;
        cols[s++] = row_size;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    int rs;
    int* rcs;
    int** res = highFive(items, s, cols, &rs, &rcs);
    printf("[");
    for (int i = 0; i < rs; i++) {
        printf("[");
        for (int j = 0; j < rcs[i]; j++) printf("%d%s", res[i][j], j == rcs[i] - 1 ? "" : ",");
        printf("]%s", i == rs - 1 ? "" : ",");
    }
    printf("]\\n");
    return 0;
}"""
    }

    def solve(items):
        d = collections.defaultdict(list)
        for sid, score in items:
            d[sid].append(score)
        res = []
        for sid in sorted(d.keys()):
            top5 = sorted(d[sid], reverse=True)[:5]
            res.append([sid, sum(top5) // 5])
        return res

    test_cases_data = [
        [[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]], # Sample 1
        [[[1,100],[1,100],[1,100],[1,100],[1,100],[2,90],[2,90],[2,90],[2,90],[2,90]]],
        [[[1,10],[1,20],[1,30],[1,40],[1,50],[1,60]]],
        [[[1,100],[1,0],[1,0],[1,0],[1,0],[1,0]]],
        [[[1,100],[1,100],[1,100],[1,100],[1,100],[1,100]]],
        [[[10,50],[10,60],[10,70],[10,80],[10,90],[10,100]]],
        [[[5,100],[5,100],[5,100],[5,100],[5,100]]],
        # Stress tests
        [[[1, i%100+1] for i in range(1000)]],
        [[[i//5+1, 100] for i in range(1000)]],
        [[[i+1, 100], [i+1, 90], [i+1, 80], [i+1, 70], [i+1, 60]] for i in range(200)] # Flatten this manually if needed, but the generator handles it
    ]
    # Flatten last test case
    test_cases_data[9] = [[item for sublist in test_cases_data[9] for item in sublist]]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 1})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "Sorting"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
