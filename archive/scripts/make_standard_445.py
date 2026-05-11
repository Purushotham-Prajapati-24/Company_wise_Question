import json
import os

def generate_json():
    problem_id = 445
    title = "Add Two Numbers II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>445. Add Two Numbers II</h3>
<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/sumii-linked-list.jpg" style="width: 523px; height: 199px;" />
<pre><strong>Input:</strong> l1 = [7,2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,8,0,7]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [8,0,7]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve it without reversing the input lists?</p>"""

    input_format = "Two lines: l1 (JSON array) and l2 (JSON array)."
    output_format = "A JSON array representing the sum linked list."
    
    constraints = [
        "1 <= number of nodes <= 100",
        "0 <= Node.val <= 9",
        "No leading zeros."
    ]
    
    explanation = """To add two numbers represented by linked lists where the most significant digit comes first, we can use two stacks to store the digits of each list. We then pop values from the stacks to add them from least significant to most significant, keeping track of the carry and building the result list from back to front."""
    
    answer = """class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        dummy = None
        carry = 0
        while s1 or s2 or carry:
            v1 = s1.pop() if s1 else 0
            v2 = s2.pop() if s2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            
            node = ListNode(total % 10)
            node.next = dummy
            dummy = node
            
        return dummy"""

    boilerplate = {
        "python": """import sys
import json

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(data):
    if not data: return None
    dummy = ListNode(0)
    curr = dummy
    for v in data:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def list_to_array(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # User Logic Here
        pass

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        l1_data = json.loads(lines[0].strip())
        l2_data = json.loads(lines[1].strip())
        l1 = build_list(l1_data)
        l2 = build_list(l2_data)
        sol = Solution()
        res = sol.addTwoNumbers(l1, l2)
        print(json.dumps(list_to_array(res)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // User Logic Here
        return NULL;
    }
};

int main() {
    string line1, line2;
    if (getline(cin, line1) && getline(cin, line2)) {
        // Manual parsing for linked lists...
        // Solution sol;
        // ListNode* res = sol.addTwoNumbers(l1, l2);
        // Print linked list...
        cout << \"[]\" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // User Logic Here
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        // I/O parsing and building logic...
    }
}""",
        "javascript": """function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 2) {
    // Execution logic...
    console.log(\"[]\");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // User Logic Here
    return NULL;
}

int main() {
    return 0;
}"""
    }

    test_cases = [
        {"input": "[7,2,4,3]\\n[5,6,4]", "expected_output": "[7,8,0,7]", "is_sample": True},
        {"input": "[2,4,3]\\n[5,6,4]", "expected_output": "[8,0,7]", "is_sample": True},
        {"input": "[0]\\n[0]", "expected_output": "[0]", "is_sample": True},
        {"input": "[ 7, 2, 4, 3 ]\\n[ 5, 6, 4 ]", "expected_output": "[7,8,0,7]", "is_sample": False}, # Spaces
        {"input": "[9,9,9]\\n[1]", "expected_output": "[1,0,0,0]", "is_sample": False},
        {"input": "[1,2,3]\\n[9,8,7]", "expected_output": "[1,1,1,0]", "is_sample": False},
        {"input": "[5]\\n[5]", "expected_output": "[1,0]", "is_sample": False},
        {"input": "[1]\\n[9,9]", "expected_output": "[1,0,0]", "is_sample": False},
        # Stress
        {"input": json.dumps([9]*100) + "\\n[1]", "expected_output": "[1]" + str([0]*100).replace(" ", "").replace("[0,", "").replace(" ", ""), "is_sample": False},
        {"input": "[1,0,0]\\n[1]", "expected_output": "[1,0,1]", "is_sample": False}
    ]
    # Correcting expected output for stress case 9
    test_cases[8]["expected_output"] = "[1," + ",".join(["0"]*100) + "]"

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
        "topics": ["Linked List", "Math", "Stack"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Add_Two_Numbers_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
