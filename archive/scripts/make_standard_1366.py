import json
import os

def generate_json():
    problem_id = 1366
    title = "Rank Teams by Votes"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1366. Rank Teams by Votes</h3>
<p>In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.</p>

<p>The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to break the tie, if they still tie, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.</p>

<p>Given an array of strings <code>votes</code> which is the votes of all voters in the ranking system. Sort all teams according to the ranking system described above.</p>

<p>Return <em>a string of all teams</em> <strong>sorted</strong> by the ranking system.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> votes = ["ABC","ACB","ABC","ACB","ACB"]
<strong>Output:</strong> "ACB"
<strong>Explanation:</strong> Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and third by 3 voters.
Team C was ranked second by 3 voters and third by 2 voters.
As team C got more second place votes than team B, team C is ranked second and team B is ranked third.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> votes = ["WXYZ","XYZW"]
<strong>Output:</strong> "XWYZ"
<strong>Explanation:</strong> X is the winner due to tie-breaking rules. X has one first place vote, one second place vote, no third place vote, and no fourth place vote. W has one first place vote, no second place vote, no third place vote, and one fourth place vote. 
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
<strong>Output:</strong> "ZMNAGUEDSJYLBOPHRQICWFXTVK"
<strong>Explanation:</strong> Only one voter so his votes are used for the ranking.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= votes.length &lt;= 1000</code></li>
	<li><code>1 &lt;= votes[i].length &lt;= 26</code></li>
	<li><code>votes[i].length == votes[j].length</code> for all <code>0 &lt;= i, j &lt; votes.length</code>.</li>
	<li><code>votes[i]</code> contains all characters from <code>votes[0]</code>, each only once.</li>
</ul>"""

    input_format = "A list of strings `votes` as a JSON array."
    output_format = "A string of sorted teams."

    constraints = [
        "1 <= votes.length <= 1000",
        "1 <= votes[i].length <= 26",
        "Teams are uppercase English letters"
    ]

    explanation = """To rank the teams:
1. Identify all participating teams (characters in `votes[0]`).
2. Create a score table for each team. The score of a team is an array of length `L` (where `L` is nodes/teams count), where `score[i]` is the number of times the team was ranked at position `i`.
3. Sort the teams based on their score arrays:
   - Comparing score arrays directly will sort based on positions sequentially (higher position votes first).
   - Since we want higher votes to come first, we sort in descending order.
   - For tie-breaking, use the team character itself as the last element of the score (alphabetical order, ascending).
4. Combine the results into a string."""

    answer = """class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        n = len(votes[0])
        ranking = {c: [0] * n for c in votes[0]}
        for v in votes:
            for i, c in enumerate(v):
                ranking[c][i] += 1
        
        # Sort by: scores descending, then character ascending
        res = sorted(votes[0], key=lambda x: (ranking[x], [-ord(x)]), reverse=True)
        return "".join(res)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        votes = json.loads(raw)
        sol = Solution()
        print(sol.rankTeams(votes))""",
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
    string rankTeams(vector<string>& votes) {
        // User logic here
        return "";
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<string> votes = json::parse(line);
        Solution sol;
        cout << sol.rankTeams(votes) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public String rankTeams(String[] votes) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            String[] votes = mapper.readValue(sc.nextLine(), String[].class);
            System.out.println(new Solution().rankTeams(votes));
        }
    }
}""",
        "javascript": """var rankTeams = function(votes) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(rankTeams(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * rankTeams(char ** votes, int votesSize){
    // User logic here
    return "";
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    def solve(votes):
        n = len(votes[0])
        ranking = {c: [0] * n for c in votes[0]}
        for v in votes:
            for i, c in enumerate(v):
                ranking[c][i] += 1
        res = sorted(votes[0], key=lambda x: (ranking[x], [-ord(x)]), reverse=True)
        return "".join(res)

    test_cases_data = [
        ["ABC","ACB","ABC","ACB","ACB"],          # Sample 1
        ["WXYZ","XYZW"],                          # Sample 2
        ["ZMNAGUEDSJYLBOPHRQICWFXTVK"],           # Sample 3
        ["BCA","CAB","ABC"],                      # Complete tie
        ["M","M","M"],                            # Single team
        ["ABC", "ABC", "ABC"],                    # Clear winner
        ["A", "B", "C"],                          # Wrong logic (not possible per constraint, votes[i] contains all chars)
        # Stress tests
        ["A"*1, "A"*1],                           # (wait, length check)
        ["ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD"], # Rotation
        ["XYZ", "YZX", "ZXY"]
    ]

    # Adjustment for constraint: votes[i] contains ALL characters from votes[0]
    test_cases_data[6] = ["ABC", "BCA", "CAB"]
    test_cases_data[7] = ["A", "A"]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = solve(t)
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "String", "Hash Table", "Sorting"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
