import json
import os

def generate_json():
    problem_id = 1290
    title = "Convert Binary Number in a Linked List to Integer"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1290. Convert Binary Number in a Linked List to Integer</h3>
<p>Given <code>head</code> which is a reference node to a singly-linked list. The value of each node in the linked list is either <code>0</code> or <code>1</code>. The linked list holds the binary representation of a number.</p>

<p>Return the <em>decimal value</em> of the number in the linked list.</p>

<p>The <strong>most significant bit</strong> is at the head of the linked list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/05/graph-1.png" style="width: 426px; height: 108px;">
<pre><strong>Input:</strong> head = [1,0,1]
<strong>Output:</strong> 5
<strong>Explanation:</strong> (101) in base 2 = (5) in base 10
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> head = [0]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The Linked List is not empty.</li>
	<li>Number of nodes will not exceed <code>30</code>.</li>
	<li>Each node's value is either <code>0</code> or <code>1</code>.</li>
</ul>"""

    input_format = "A list of integers representing the linked list nodes."
    output_format = "An integer representing the decimal value."

    constraints = [
        "The Linked List is not empty",
        "Number of nodes <= 30",
        "Each node's value is 0 or 1"
    ]

    explanation = """To convert the binary linked list to a decimal integer:
1. Initialize `result = 0`.
2. Traverse the linked list starting from the `head`.
3. For each node, bit-shift the current `result` to the left by 1 (equivalent to `result * 2`) and add the current node's value (`result = (result << 1) | node.val`).
4. Repeat until the end of the list is reached.
5. Return the `result`."""

    answer = """class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = (res << 1) | head.val
            head = head.next
        return res"""

    boilerplate = {
        "python": """import sys
import json

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # User logic here
        return 0

def list_to_ln(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        arr = json.loads(raw)
        sol = Solution()
        print(sol.getDecimalValue(list_to_ln(arr)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int getDecimalValue(ListNode* head) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<int> arr = json::parse(line);
        // Linked list construction and solution call
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public int getDecimalValue(ListNode head) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            int[] arr = mapper.readValue(sc.nextLine(), int[].class);
            // Linked list construction and solution call
        }
    }
}""",
        "javascript": """function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

var getDecimalValue = function(head) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const arr = JSON.parse(input);
    // Linked list construction and solution call
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

int getDecimalValue(struct ListNode* head){
    // User logic here
    return 0;
}

int main() {
    // Linked list construction logic
    return 0;
}"""
    }

    def solve(arr):
        res = 0
        for x in arr:
            res = (res << 1) | x
        return res

    test_cases_data = [
        [1,0,1],    # Sample 1
        [0],        # Sample 2
        [1],        # Single 1
        [1,1,1],    # All 1s
        [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0], # Longer
        [0,0,0,1],  # Leading 0s
        [1]*30,     # Max nodes
        # Stress tests
        [1]*10,
        [0]*10 + [1],
        [1] + [0]*29
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Linked List", "Math"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
