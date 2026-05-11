import json
import os

def generate_json():
    problem_id = 1169
    title = "Invalid Transactions"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1169. Invalid Transactions</h3>
<p>A transaction is possibly invalid if:</p>
<ul>
	<li>the amount exceeds <code>$1000</code>, or;</li>
	<li>if it occurs within (and including) <code>60</code> minutes of another transaction with the <strong>same name</strong> in a <strong>different city</strong>.</li>
</ul>

<p>You are given an array of strings <code>transaction</code> where <code>transactions[i]</code> consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.</p>

<p>Return a list of <code>transactions</code> that are possibly invalid. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
<strong>Output:</strong> ["alice,20,800,mtv","alice,50,100,beijing"]
<strong>Explanation:</strong> The first transaction is invalid because the second transaction occurs within 60 minutes, have the same name and is in a different city. Similarly the second one is invalid.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
<strong>Output:</strong> ["alice,50,1200,mtv"]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
<strong>Output:</strong> ["bob,50,1200,mtv"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>transactions.length &lt;= 1000</code></li>
	<li>Each <code>transactions[i]</code> takes the form <code>"{name},{time},{amount},{city}"</code></li>
	<li>Each <code>{name}</code> and <code>{city}</code> consist of lowercase English letters, and have lengths between <code>1</code> and <code>10</code>.</li>
	<li>Each <code>{time}</code> and <code>{amount}</code> are integers between <code>0</code> and <code>1000</code>.</li>
</ul>"""

    input_format = "A list of strings `transactions` representing each transaction."
    output_format = "A list of strings representing the invalid transactions."

    constraints = [
        "1 <= transactions.length <= 1000",
        "0 <= time, amount <= 1000"
    ]

    explanation = """To find invalid transactions:
1. Parse each transaction string into its components: name, time, amount, and city.
2. A transaction is invalid if its amount is > 1000.
3. A transaction is also invalid if there exists another transaction with the same name, but a different city, occurring within 60 minutes (inclusive).
4. Use a flag array to keep track of which transactions are invalid to avoid duplicate entries in the final list.
5. Return the list of transaction strings that were flagged."""

    answer = """class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        n = len(transactions)
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append({
                "name": name,
                "time": int(time),
                "amount": int(amount),
                "city": city,
                "raw": t
            })
            
        invalid = [False] * n
        for i in range(n):
            if parsed[i]["amount"] > 1000:
                invalid[i] = True
            for j in range(i + 1, n):
                if parsed[i]["name"] == parsed[j]["name"] and parsed[i]["city"] != parsed[j]["city"]:
                    if abs(parsed[i]["time"] - parsed[j]["time"]) <= 60:
                        invalid[i] = True
                        invalid[j] = True
                        
        res = []
        for i in range(n):
            if invalid[i]:
                res.append(transactions[i])
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        transactions = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.invalidTransactions(transactions)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<string> invalidTransactions(vector<string>& transactions) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<string> transactions = json::parse(line);
        Solution sol;
        vector<string> res = sol.invalidTransactions(transactions);
        cout << json(res).dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public List<String> invalidTransactions(String[] transactions) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            String[] transactions = mapper.readValue(sc.nextLine(), String[].class);
            List<String> res = new Solution().invalidTransactions(transactions);
            System.out.println(mapper.writeValueAsString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var invalidTransactions = function(transactions) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const res = invalidTransactions(JSON.parse(input));
    console.log(JSON.stringify(res).replace(/ /g, ""));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char ** invalidTransactions(char ** transactions, int transactionsSize, int* returnSize){
    // User logic here
    return NULL;
}

int main() {
    // Boilerplate for parsing string array
    return 0;
}"""
    }

    def solve(transactions):
        n = len(transactions)
        parsed = []
        for t in transactions:
            parts = t.split(',')
            parsed.append({"name": parts[0], "time": int(parts[1]), "amount": int(parts[2]), "city": parts[3]})
        invalid = [False] * n
        for i in range(n):
            if parsed[i]["amount"] > 1000:
                invalid[i] = True
            for j in range(n):
                if i == j: continue
                if parsed[i]["name"] == parsed[j]["name"] and parsed[i]["city"] != parsed[j]["city"]:
                    if abs(parsed[i]["time"] - parsed[j]["time"]) <= 60:
                        invalid[i] = True
        return [transactions[i] for i in range(n) if invalid[i]]

    test_cases_data = [
        ["alice,20,800,mtv","alice,50,100,beijing"], # Sample 1
        ["alice,20,800,mtv","alice,50,1200,mtv"],    # Sample 2
        ["alice,20,800,mtv","bob,50,1200,mtv"],      # Sample 3
        ["alice,20,800,mtv","alice,81,100,beijing"], # > 60 mins ok
        ["a,0,0,x","a,60,0,y"],                       # Edge 60 mins invalid
        ["a,0,0,x","a,61,0,y"],                       # Edge 61 mins valid
        ["z,1,2000,a"],                               # Single > 1000
        # Stress tests
        ["a,1,1,x"] * 10,                            # Same city
        ["a,1,1," + str(i) for i in range(10)],      # Diff cities same time
        ["name" + str(i) + ",1,1,city" + str(i) for i in range(100)] # All ok
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t)).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "String", "Sorting"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
