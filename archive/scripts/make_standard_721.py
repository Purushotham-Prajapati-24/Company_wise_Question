import json
import os
import collections

def generate_json():
    problem_id = 721
    title = "Accounts Merge"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>721. Accounts Merge</h3>
<p>Given a list of <code>accounts</code> where each element <code>accounts[i]</code> is a list of strings, where the first element <code>accounts[i][0]</code> is a name, and the rest of the elements are emails representing emails of the account.</p>
<p>Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.</p>
<p>After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in <b>sorted order</b>. The accounts themselves can be returned in <b>any order</b>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
<strong>Output:</strong> [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
<strong>Explanation:</strong>
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would also be accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Gabe","Gabe0@m.co","Gabe2@m.co"],["Gabe","Gabe4@m.co","Gabe5@m.co"],["Kevin","Kevin0@m.co","Kevin1@m.co"]]
<strong>Output:</strong> [["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe2@m.co","Gabe3@m.co"],["Gabe","Gabe4@m.co","Gabe5@m.co"],["Kevin","Kevin0@m.co","Kevin1@m.co","Kevin3@m.co","Kevin5@m.co"]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= accounts.length &lt;= 1000</code></li>
	<li><code>2 &lt;= accounts[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= accounts[i][j].length &lt;= 30</code></li>
	<li><code>accounts[i][0]</code> consists of English letters.</li>
	<li><code>accounts[i][j]</code> (for <code>j &gt; 0</code>) is a valid email.</li>
</ul>
"""

    input_format = "A JSON list of accounts."
    output_format = "A JSON list of merged accounts."
    
    constraints = [
        "1 <= accounts.length <= 1000",
        "Common email links accounts.",
        "Output emails must be sorted.",
        "O(N * L * log(N * L)) complexity is acceptable."
    ]
    
    explanation = """To merge accounts:
1. **Represent as a Graph**:
   - Each email is a node.
   - For every account, connect the first email to all other emails in that account.
   - Keep a mapping from `email` to `name`.
2. **Find Connected Components**:
   - Use DFS or Union Find to group all connected emails.
3. **Format Result**:
   - For each connected component:
     - Sort the emails.
     - Add the associated name at the beginning.
4. **Complexity**:
   - Building Graph: O(∑ L_i) where L_i is the length of each account.
   - Sorting: O(∑ L_i log ∑ L_i).
   - Overall: O(N * L log(N * L)).

Complexity:
- Time: O(N * L * α(N) + ∑ L_i log L_i).
- Space: O(N * L).
"""
    
    answer = """import collections
def accountsMerge(accounts):
    email_to_name = {}
    graph = collections.defaultdict(set)
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            graph[acc[1]].add(email)
            graph[email].add(acc[1])
            email_to_name[email] = name
            
    res = []
    visited = set()
    for email in email_to_name:
        if email not in visited:
            stack = [email]
            visited.add(email)
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            res.append([email_to_name[email]] + sorted(component))
    return res"""

    boilerplate = {
        "python": "import sys\\nimport json\\nimport collections\\n\\ndef accountsMerge(accounts):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    accounts = json.loads(sys.stdin.read().strip())\\n    print(json.dumps(accountsMerge(accounts)))",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <string>\\n#include <unordered_map>\\n#include <set>\\n#include <algorithm>\\nusing namespace std;\\n\\nvector<vector<string>> accountsMerge(vector<vector<string>>& accounts) { return {}; }",
        "java": "public class Main { public static void main(String[] args) { } }",
        "javascript": "const fs = require('fs');",
        "c": "char*** accountsMerge(char*** accounts, int accountsSize, int* accountsColSize, int* returnSize, int** returnColumnSizes) { }"
    }

    test_cases = [
        {"input": '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]', "expected_output": '[["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]', "is_sample": True},
        {"input": '[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Gabe","Gabe0@m.co","Gabe2@m.co"],["Gabe","Gabe4@m.co","Gabe5@m.co"],["Kevin","Kevin0@m.co","Kevin1@m.co"]]', "expected_output": '[["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe2@m.co", "Gabe3@m.co"], ["Gabe", "Gabe4@m.co", "Gabe5@m.co"], ["Kevin", "Kevin0@m.co", "Kevin1@m.co", "Kevin3@m.co", "Kevin5@m.co"]]', "is_sample": True},
        {"input": '[["Alex", "a@m.co"], ["Alex", "b@m.co"]]', "expected_output": '[["Alex", "a@m.co"], ["Alex", "b@m.co"]]', "is_sample": False},
        {"input": '[["Alex", "a@m.co"], ["Alex", "a@m.co"]]', "expected_output": '[["Alex", "a@m.co"]]', "is_sample": False},
        {"input": '[["A", "1@m.co", "2@m.co"], ["A", "2@m.co", "3@m.co"], ["A", "3@m.co", "4@m.co"]]', "expected_output": '[["A", "1@m.co", "2@m.co", "3@m.co", "4@m.co"]]', "is_sample": False},
        {"input": '[["A", "1@m.co"], ["B", "2@m.co"]]', "expected_output": '[["A", "1@m.co"], ["B", "2@m.co"]]', "is_sample": False},
        {"input": '[["A", "1@m.co"], ["A", "1@m.co"], ["A", "1@m.co"]]', "expected_output": '[["A", "1@m.co"]]', "is_sample": False},
        {"input": '[["Z", "z@m.co"], ["Y", "y@m.co"], ["X", "x@m.co"]]', "expected_output": '[["X", "x@m.co"], ["Y", "y@m.co"], ["Z", "z@m.co"]]', "is_sample": False},
        # Stress cases
        {"input": json.dumps([["User" + str(i), "email" + str(i) + "@m.co"] for i in range(1000)]), "expected_output": "1000 separate accounts", "is_sample": False},
        {"input": json.dumps([["SameUser"] + ["email" + str(i) + "@m.co" for i in range(100)] for _ in range(10)]), "expected_output": "1 merged account", "is_sample": False}
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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Hash Table", "String", "DFS", "Breadth-First Search", "Union Find"],
        "companyIndex": 0
    }

    output_path = "601-800/721_Accounts_Merge.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
