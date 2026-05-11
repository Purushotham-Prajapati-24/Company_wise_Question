import json
import os

def generate_json():
    problem_id = 433
    title = "Minimum Genetic Mutation"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>433. Minimum Genetic Mutation</h3>
<p>A gene string can be represented by an 8-character long string, with choices from <code>'A'</code>, <code>'C'</code>, <code>'G'</code>, and <code>'T'</code>.</p>

<p>Suppose we need to investigate a mutation from a gene string <code>startGene</code> to a gene string <code>endGene</code>, where one mutation is defined as one single character changed in the gene string.</p>

<ul>
	<li>For example, <code>"AACCGGTT" --&gt; "AACCGGTA"</code> is one mutation.</li>
</ul>

<p>There is also a gene bank <code>bank</code> that records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.</p>

<p>Given the two gene strings <code>startGene</code> and <code>endGene</code> and the gene bank <code>bank</code>, return <em>the minimum number of mutations needed to mutate from </em><code>startGene</code><em> to </em><code>endGene</code>. If there is no such a mutation, return <code>-1</code>.</p>

<p>Note that the starting point is assumed to be valid, so it might not be included in the bank.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= bank.length &lt;= 10</code></li>
	<li><code>startGene.length == endGene.length == 8</code></li>
	<li><code>bank[i].length == 8</code></li>
	<li><code>startGene</code>, <code>endGene</code>, and <code>bank[i]</code> consist of characters <code>'A'</code>, <code>'C'</code>, <code>'G'</code>, and <code>'T'</code>.</li>
</ul>"""

    input_format = "Three lines: startGene, endGene, and bank (JSON array of strings)."
    output_format = "An integer representing the minimum number of mutations."
    
    constraints = [
        "0 <= bank.length <= 10",
        "startGene.length == endGene.length == 8",
        "bank[i].length == 8",
        "Genes consist of 'A', 'C', 'G', and 'T'."
    ]
    
    explanation = """Finding the minimum number of mutations is equivalent to finding the shortest path in an unweighted graph where each node is a valid gene string and an edge exists between two nodes if they differ by exactly one character. Breadth-First Search (BFS) is ideal for finding the shortest path in such a graph."""
    
    answer = """from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            curr, steps = queue.popleft()
            if curr == endGene:
                return steps
            
            for i in range(len(curr)):
                for char in 'ACGT':
                    if char == curr[i]: continue
                    mutation = curr[:i] + char + curr[i+1:]
                    if mutation in bank_set and mutation not in visited:
                        visited.add(mutation)
                        queue.append((mutation, steps + 1))
        return -1"""

    boilerplate = {
        "python": """import sys
import json
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        # User Logic Here
        pass

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 3:
        startGene = lines[0].strip()
        endGene = lines[1].strip()
        bank = json.loads(lines[2].strip())
        sol = Solution()
        print(sol.minMutation(startGene, endGene, bank))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        // User Logic Here
        return -1;
    }
};

int main() {
    string start, end, bankLine;
    if (cin >> start >> end) {
        cin.ignore();
        if (getline(cin, bankLine)) {
            vector<string> bank;
            string temp = \"\";
            for (char c : bankLine) {
                if (c == '\"') {
                    if (!temp.empty()) {
                        bank.push_back(temp);
                        temp = \"\";
                    } else {
                        temp = \" \"; // dummy to start
                        temp = \"\";
                    }
                } else if (temp.length() > 0 || isalpha(c)) {
                   // This is a bit simplified, but let's use a more robust one
                }
            }
            // Robust parsing for bank array of strings...
            vector<string> realBank;
            int i = 0;
            while(i < bankLine.length()){
                if(bankLine[i] == '\"'){
                    int j = i+1;
                    while(j < bankLine.length() && bankLine[j] != '\"') j++;
                    realBank.push_back(bankLine.substr(i+1, j-i-1));
                    i = j;
                }
                i++;
            }
            Solution sol;
            cout << sol.minMutation(start, end, realBank) << endl;
        }
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        // User Logic Here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String start = sc.nextLine().trim();
            if (sc.hasNextLine()) {
                String end = sc.nextLine().trim();
                if (sc.hasNextLine()) {
                    String bankLine = sc.nextLine().trim();
                    List<String> bank = new ArrayList<>();
                    int i = 0;
                    while(i < bankLine.length()){
                        if(bankLine.charAt(i) == '\"'){
                            int j = i+1;
                            while(j < bankLine.length() && bankLine.charAt(j) != '\"') j++;
                            bank.add(bankLine.substring(i+1, j));
                            i = j;
                        }
                        i++;
                    }
                    Solution sol = new Solution();
                    System.out.println(sol.minMutation(start, end, bank.toArray(new String[0])));
                }
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string} startGene
 * @param {string} endGene
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function(startGene, endGene, bank) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 3) {
    const start = input[0].trim();
    const end = input[1].trim();
    const bank = JSON.parse(input[2].trim());
    console.log(minMutation(start, end, bank));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minMutation(char* startGene, char* endGene, char** bank, int bankSize) {
    // User Logic Here
    return -1;
}

int main() {
    return 0;
}"""
    }

    test_cases = [
        {"input": "AACCGGTT\\nAACCGGTA\\n[\\\"AACCGGTA\\\"]", "expected_output": "1", "is_sample": True},
        {"input": "AACCGGTT\\nAAACGGTA\\n[\\\"AACCGGTA\\\",\\\"AACCGCTA\\\",\\\"AAACGGTA\\\"]", "expected_output": "2", "is_sample": True},
        {"input": "AACCGGTT\\nAACCGGTA\\n[]", "expected_output": "-1", "is_sample": False},
        {"input": "AAAAAAAA\\nCCCCCCCC\\n[\\\"AAAAAAAC\\\",\\\"AAAAAACC\\\",\\\"AAAAACCC\\\",\\\"AAAACCCC\\\",\\\"AAACCCCC\\\",\\\"AACCCCCC\\\",\\\"ACCCCCCC\\\",\\\"CCCCCCCC\\\"]", "expected_output": "8", "is_sample": False},
        {"input": "AACCGGTT\\nAACCGGTT\\n[\\\"AACCGGTT\\\"]", "expected_output": "0", "is_sample": False},
        {"input": "AAAAAAAA\\nAAAAAAAT\\n[ \\\"AAAAAAAT\\\" ]", "expected_output": "1", "is_sample": False}, # Spaces
        {"input": "AAAAAAAC\\nAAAAAAAT\\n[\\\"AAAAAAAT\\\"]", "expected_output": "1", "is_sample": False},
        {"input": "TTAAAAAA\\nAAAAAAAA\\n[\\\"TAAAAAAA\\\",\\\"AAAAAAAA\\\"]", "expected_output": "2", "is_sample": False},
        # Stress
        {"input": "AAAAAAAA\\nTTTTTTTT\\n[\\\"AAAAAAAT\\\",\\\"AAAAAATT\\\",\\\"AAAAATTT\\\",\\\"AAAATTTT\\\",\\\"AAATTTTT\\\",\\\"AATTTTTT\\\",\\\"ATTTTTTT\\\",\\\"TTTTTTTT\\\"]", "expected_output": "8", "is_sample": False},
        {"input": "AAAAAAAA\\nAAAAAAAA\\n[]", "expected_output": "0", "is_sample": False}
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
        "topics": ["Hash Table", "String", "BFS"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Minimum_Genetic_Mutation.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
