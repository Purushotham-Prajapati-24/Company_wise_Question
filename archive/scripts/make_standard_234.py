import json
import os

def generate_json():
    problem_id = 234
    title = "Palindrome Linked List"
    difficulty = "EASY"
    marks = 5
    
    html_description = """<h3>234. Palindrome Linked List</h3>
<p>Given the <code>head</code> of a singly linked list, return <code>true</code><em> if it is a </em><span data-keyword="palindrome-linked-list"><em>palindrome</em></span><em> or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
<pre><strong>Input:</strong> head = [1,2,2,1]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
<pre><strong>Input:</strong> head = [1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do it in <code>O(n)</code> time and <code>O(1)</code> space?
"""

    input_format = "A stringified 1D array representing the linked list."
    output_format = "A boolean (true/false)."
    
    constraints = [
        "1 <= n <= 100,000",
        "0 <= Node.val <= 9",
        "O(n) time and O(1) space preferred."
    ]
    
    explanation = """To check if a linked list is a palindrome in O(1) space:
1. **Find Middle**: Use slow and fast pointers to find the middle of the list.
2. **Reverse Second Half**: Reverse the second half of the linked list starting from the middle.
3. **Compare**: Compare the elements of the first half and the reversed second half.
4. **Restore (Optional but Good Practice)**: Reverse the second half back to original state.
5. **Complexity**:
   - Time: O(N) where N is the number of nodes.
   - Space: O(1) additionally (not counting recursion stack if using recursive reverse)."""
    
    answer = """class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # Compare
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef build_list(vals):\n    if not vals: return None\n    head = ListNode(vals[0])\n    curr = head\n    for v in vals[1:]: \n        curr.next = ListNode(v)\n        curr = curr.next\n    return head\n\ndef isPalindrome(head):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        try:\n            arr = json.loads(line)\n        except:\n            arr = [int(x) for x in line.replace('[', '').replace(']', '').replace(',', ' ').split()]\n        print(\"true\" if isPalindrome(build_list(arr)) else \"false\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nListNode* buildList(vector<int>& vals) {\n    if (vals.empty()) return NULL;\n    ListNode* head = new ListNode(vals[0]);\n    ListNode* curr = head;\n    for (size_t i = 1; i < vals.size(); i++) {\n        curr->next = new ListNode(vals[i]);\n        curr = curr->next;\n    }\n    return head;\n}\n\nbool isPalindrome(ListNode* head) {\n    // User logic\n    return false;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        int val;\n        vector<int> vals;\n        while (ss >> val) vals.push_back(val);\n        cout << (isPalindrome(buildList(vals)) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public boolean isPalindrome(ListNode head) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null && !line.trim().isEmpty()) {\n            line = line.replace(\"[\", \"\").replace(\"]\", \"\").replace(\",\", \" \");\n            String[] parts = line.trim().split(\"\\\\s+\");\n            ListNode head = buildList(parts);\n            System.out.println(new Solution().isPalindrome(head) ? \"true\" : \"false\");\n        }\n    }\n\n    static ListNode buildList(String[] vals) {\n        if (vals.length == 0 || vals[0].isEmpty()) return null;\n        ListNode head = new ListNode(Integer.parseInt(vals[0]));\n        ListNode curr = head;\n        for (int i = 1; i < vals.length; i++) {\n            curr.next = new ListNode(Integer.parseInt(vals[i]));\n            curr = curr.next;\n        }\n        return head;\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val);\n    this.next = (next===undefined ? null : next);\n}\n\nfunction buildList(arr) {\n    if (arr.length === 0) return null;\n    let head = new ListNode(arr[0]);\n    let curr = head;\n    for (let i = 1; i < arr.length; i++) {\n        curr.next = new ListNode(arr[i]);\n        curr = curr.next;\n    }\n    return head;\n}\n\nfunction isPalindrome(head) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    let arr = JSON.parse(input);\n    console.log(isPalindrome(buildList(arr)) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nbool isPalindrome(struct ListNode* head) {\n    // User logic\n    return false;\n}\n\nstruct ListNode* buildList(int* vals, int size) {\n    if (size == 0) return NULL;\n    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));\n    head->val = vals[0];\n    head->next = NULL;\n    struct ListNode* curr = head;\n    for (int i = 1; i < size; i++) {\n        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n        curr->next->val = vals[i];\n        curr->next->next = NULL;\n        curr = curr->next;\n    }\n    return head;\n}\n\nint main() {\n    char line[1000000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* token = strtok(line, \"[], \");\n        int* vals = (int*)malloc(100000 * sizeof(int));\n        int size = 0;\n        while (token) {\n            vals[size++] = atoi(token);\n            token = strtok(NULL, \"[], \");\n        }\n        printf(\"%s\\n\", isPalindrome(buildList(vals, size)) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,2,1]", "expected_output": "true", "is_sample": True},
        {"input": "[1,2]", "expected_output": "false", "is_sample": True},
        {"input": "[1]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,2,1]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,3,2,1]", "expected_output": "true", "is_sample": False},
        {"input": "[1,1,1,2,1,1,1]", "expected_output": "true", "is_sample": False},
        {"input": "[0,0]", "expected_output": "true", "is_sample": False},
        # Stress Tests (100,000 nodes)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_p(vals):
        return vals == vals[::-1]

    # Stress 8: 100,000 all same
    n8 = [1] * 100000
    test_cases[7] = {"input": json.dumps(n8), "expected_output": "true", "is_sample": False}
    # Stress 9: 100,000 alternating
    n9 = [1, 2] * 50000 + [2, 1] * 0 # not a palindrome
    n9 = list(range(50000)) + list(range(49999, -1, -1))
    test_cases[8] = {"input": json.dumps(n9), "expected_output": "true", "is_sample": False}
    # Stress 10: 100,000 not a palindrome (ends differently)
    n10 = list(range(50000)) + list(range(50000))
    test_cases[9] = {"input": json.dumps(n10), "expected_output": "false", "is_sample": False}

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
        "topics": ["Linked List", "Two Pointers", "Stack", "Recursion"],
        "companyIndex": 0
    }

    output_path = "201-400/234_Palindrome_Linked_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
