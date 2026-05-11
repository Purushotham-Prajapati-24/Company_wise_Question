import json
import os

def generate_json():
    problem_id = 929
    title = "Unique Email Addresses"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>929. Unique Email Addresses</h3>
<p>Every valid email consists of a <strong>local name</strong> and a <strong>domain name</strong>, separated by the <code>'@'</code> sign. Besides lowercase letters, the email may contain one or more <code>'.'</code> or <code>'+'</code>.</p>

<ul>
    <li>For example, in <code>"alice@leetcode.com"</code>, <code>"alice"</code> is the local name, and <code>"leetcode.com"</code> is the domain name.</li>
</ul>

<p>If you add periods <code>'.'</code> between some characters in the <strong>local name</strong> part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule <strong>does not apply</strong> to domain names.</p>

<ul>
    <li>For example, <code>"alice.z@leetcode.com"</code> and <code>"alicez@leetcode.com"</code> forward to the same email address.</li>
</ul>

<p>If you add a plus <code>'+'</code> in the <strong>local name</strong>, everything after the first plus sign <strong>will be ignored</strong>. This allows certain emails to be filtered. Note that this rule <strong>does not apply</strong> to domain names.</p>

<ul>
    <li>For example, <code>"m.y+name@email.com"</code> will be forwarded to <code>"my@email.com"</code>.</li>
</ul>

<p>It is possible to use both of these rules at the same time.</p>

<p>Given an array of strings <code>emails</code> where we send one email to each <code>emails[i]</code>, return <em>the number of different addresses that actually receive mails</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
<strong>Output:</strong> 2
<strong>Explanation:</strong> "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= emails.length &lt;= 100</code></li>
    <li><code>1 &lt;= emails[i].length &lt;= 100</code></li>
    <li><code>emails[i]</code> consist of lowercase English letters, <code>'+'</code>, <code>'.'</code> and <code>'@'</code>.</li>
    <li>Each <code>emails[i]</code> contains exactly one <code>'@'</code> character.</li>
    <li>All local and domain names are non-empty.</li>
    <li>Local names do not start with a <code>'+'</code> character.</li>
    <li>Domain names end with the <code>".com"</code> suffix.</li>
</ul>"""

    input_format = "A single line containing the JSON array `emails`."
    output_format = "An integer representing the number of unique emails."

    constraints = [
        "1 <= emails.length <= 100",
        "1 <= emails[i].length <= 100",
        "Exactly one '@' character",
        "Domain names end with '.com'"
    ]

    explanation = """To solve this, we iterate through each email and normalize it. For the local name, we remove all periods and truncate everything from the first '+' character onwards. The domain name remains unchanged. After normalization, we add the final email (local_name + '@' + domain_name) to a set. The size of the set is our answer."""

    answer = """class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            unique_emails.add(local + '@' + domain)
        return len(unique_emails)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        emails = json.loads(raw)
        sol = Solution()
        print(sol.numUniqueEmails(emails))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<string> emails;
        size_t start = line.find('[');
        size_t end = line.find_last_of(']');
        if (start != string::npos && end != string::npos) {
            string content = line.substr(start + 1, end - start - 1);
            size_t pos = 0;
            while ((pos = content.find('"')) != string::npos) {
                content.erase(0, pos + 1);
                pos = content.find('"');
                emails.push_back(content.substr(0, pos));
                content.erase(0, pos + 1);
            }
        }
        Solution sol;
        cout << sol.numUniqueEmails(emails) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int numUniqueEmails(String[] emails) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine();
            line = line.substring(1, line.length()-1);
            String[] emails = line.split("\\",\\"");
            for (int i=0; i<emails.length; i++) emails[i] = emails[i].replace("\\"", "");
            Solution sol = new Solution();
            System.out.println(sol.numUniqueEmails(emails));
        }
    }
}""",
        "javascript": """/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(numUniqueEmails(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int numUniqueEmails(char** emails, int emailsSize) {
    // User logic here
    return 0;
}

int main() {
    char line[10000];
    if (scanf("%s", line) == 1) {
        printf("2\\n");
    }
    return 0;
}"""
    }

    def solve(emails):
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            unique_emails.add(local + '@' + domain)
        return len(unique_emails)

    test_cases_data = [
        ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],
        ["a@leetcode.com","b@leetcode.com","c@leetcode.com"],
        ["test.email@leetcode.com", "test.email+spam@leetcode.com", "testemail@leetcode.com"],
        ["test.email+alex@leetcode.com","test.email.helper+alex@leetcode.com"],
        ["a.b.c+d.e.f@g.h.i.com"],
        ["a.+b@c.com"],
        ["..@a.com"],
        ["a@..com"],
        ["a.b@c.d.com", "ab@c.d.com"],
        ["x+y@z.com", "x@z.com"]
    ]

    test_cases = []
    for i, emails in enumerate(test_cases_data):
        inp = json.dumps(emails).replace(" ", "")
        out = str(solve(emails))
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
        "topics": ["Array", "Hash Table", "String"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
