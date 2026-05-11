import json
import os

def generate_json():
    problem_id = 860
    title = "Lemonade Change"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>860. Lemonade Change</h3>
<p>At a lemonade stand, each lemonade costs <code>$5</code>. Customers are standing in a queue to buy from you and order one at a time (in the order specified by <code>bills</code>). Each customer will only buy one lemonade and pay with either a <code>$5</code>, <code>$10</code>, or <code>$20</code> bill. You must provide the correct change to each customer such that the net transaction is that the customer pays <code>$5</code>.</p>

<p>Note that you do not have any change in hand at first.</p>

<p>Given an integer array <code>bills</code> where <code>bills[i]</code> is the bill the <code>i<sup>th</sup></code> customer pays, return <code>true</code> <em>if you can provide every customer with the correct change, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> bills = [5,5,5,10,20]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5 bill.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> bills = [5,5,10,10,20]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= bills.length &lt;= 10<sup>5</sup></code></li>
    <li><code>bills[i]</code> is either <code>5</code>, <code>10</code>, or <code>20</code>.</li>
</ul>"""

    input_format = "A single line containing the JSON array `bills`."
    output_format = "A boolean string 'true' or 'false'."

    constraints = [
        "1 <= bills.length <= 100000",
        "bills[i] is 5, 10, or 20"
    ]

    explanation = """We keep track of the number of $5 and $10 bills in hand. When a customer pays:
- $5: Increment $5 count.
- $10: Decrement $5 count (need to check if we have one).
- $20: Decrement one $10 and one $5 (greedy choice) OR decrement three $5.
Return false if we don't have the necessary bills for change at any point."""

    answer = """class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        bills = json.loads(raw)
        sol = Solution()
        print('true' if sol.lemonadeChange(bills) else 'false')""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        // User logic here
        return false;
    }
};

vector<int> parseArray(string s) {
    auto res = vector<int>();
    size_t i = 1;
    while (i < s.length() - 1) {
        if (isdigit(s[i])) {
            int val = 0; int off=0;
            sscanf(s.c_str()+i, "%d%n", &val, &off);
            res.push_back(val); i += off;
        } else i++;
    }
    return res;
}

int main() {
    string input;
    if (cin >> input) {
        auto bills = parseArray(input);
        Solution sol;
        cout << (sol.lemonadeChange(bills) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean lemonadeChange(int[] bills) {
        // User logic here
        return false;
    }
}

public class Main {
    static int[] parseArray(String s) {
        s = s.substring(1, s.length()-1);
        if (s.isEmpty()) return new int[0];
        String[] parts = s.split(",");
        int[] res = new int[parts.length];
        for (int i=0; i<parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            int[] bills = parseArray(sc.next());
            Solution sol = new Solution();
            System.out.println(sol.lemonadeChange(bills));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function(bills) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(lemonadeChange(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool lemonadeChange(int* bills, int billsSize) {
    // User logic here
    return false;
}

int main() {
    char input[100000];
    if (scanf("%s", input) == 1) {
        int cap = 100, sz = 0;
        int* resArr = malloc(cap * sizeof(int));
        char* token = strtok(input + 1, ",]");
        while (token != NULL) {
            if (sz == cap) resArr = realloc(resArr, (cap *= 2) * sizeof(int));
            resArr[sz++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        printf("%s\\n", lemonadeChange(resArr, sz) ? "true" : "false");
        free(resArr);
    }
    return 0;
}"""
    }

    def solve(bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

    test_cases_data = [
        [5,5,5,10,20],
        [5,5,10,10,20],
        [5,5,5,10,10],
        [10,10],
        [5,5,5,5,20,20],
        [20],
        [5,10,20],
        [5,5,20,5,5,10,5,10,20],
        [5,5,5,20],
        [5,5,5,5,5,5,5,5,5,5]
    ]

    test_cases = []
    for i, bills in enumerate(test_cases_data):
        inp = json.dumps(bills).replace(" ", "")
        out = "true" if solve(bills) else "false"
        is_sample = i < 2
        test_cases.append({"input": inp, "expected_output": out, "is_sample": is_sample})

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
        "topics": ["Array", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
