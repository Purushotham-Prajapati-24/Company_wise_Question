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
        "python": "import sys\nimport json\nimport re\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef build_list(vals):\n    if not vals: return None\n    head = ListNode(vals[0])\n    curr = head\n    for v in vals[1:]: \n        curr.next = ListNode(v)\n        curr = curr.next\n    return head\n\nclass Solution:\n    def isPalindrome(self, head: ListNode) -> bool:\n        # User logic here\n        return True\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        # Extract array even if label 'head =' is present\n        match = re.search(r'\\[.*?\\]', input_data)\n        if match:\n            raw_list = match.group(0)\n            arr = json.loads(raw_list)\n            head = build_list(arr)\n            print(str(Solution().isPalindrome(head)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n#include <regex>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nListNode* buildList(vector<int>& vals) {\n    if (vals.empty()) return NULL;\n    ListNode* head = new ListNode(vals[0]);\n    ListNode* curr = head;\n    for (size_t i = 1; i < vals.size(); i++) {\n        curr->next = new ListNode(vals[i]);\n        curr = curr->next;\n    }\n    return head;\n}\n\nclass Solution {\npublic:\n    bool isPalindrome(ListNode* head) {\n        // User logic here\n        return true;\n    }\n};\n\nint main() {\n    string input;\n    char buffer[1000000];\n    if (fgets(buffer, sizeof(buffer), stdin)) {\n        input = buffer;\n        for (char &c : input) if (c == '[' || c == ']' || c == ',' || c == '=') c = ' ';\n        // Remove 'head' label if present\n        size_t pos = input.find(\"head\");\n        if (pos != string::npos) input.erase(pos, 4);\n        \n        stringstream ss(input);\n        int val;\n        vector<int> vals;\n        while (ss >> val) vals.push_back(val);\n        \n        Solution sol;\n        cout << (sol.isPalindrome(buildList(vals)) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public boolean isPalindrome(ListNode head) {\n        // User logic here\n        return true;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String input = br.readLine();\n        if (input != null) {\n            String clean = input.replaceAll(\".*=\", \"\").replaceAll(\"\\\\[|\\\\]|,|\\\"\", \" \");\n            Scanner sc = new Scanner(clean);\n            ListNode dummy = new ListNode(0);\n            ListNode curr = dummy;\n            while (sc.hasNextInt()) {\n                curr.next = new ListNode(sc.nextInt());\n                curr = curr.next;\n            }\n            System.out.println(new Solution().isPalindrome(dummy.next) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val);\n    this.next = (next===undefined ? null : next);\n}\n\nfunction buildList(arr) {\n    if (arr.length === 0) return null;\n    let head = new ListNode(arr[0]);\n    let curr = head;\n    for (let i = 1; i < arr.length; i++) {\n        curr.next = new ListNode(arr[i]);\n        curr = curr.next;\n    }\n    return head;\n}\n\n/**\n * @param {ListNode} head\n * @return {boolean}\n */\nvar isPalindrome = function(head) {\n    // User logic here\n    return true;\n};\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    const match = input.match(/\\[.*\\]/);\n    if (match) {\n        const arr = JSON.parse(match[0]);\n        console.log(isPalindrome(buildList(arr)) ? \"true\" : \"false\");\n    }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nbool isPalindrome(struct ListNode* head) {\n    // User logic here\n    return true;\n}\n\nstruct ListNode* createNode(int val) {\n    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));\n    node->val = val;\n    node->next = NULL;\n    return node;\n}\n\nint main() {\n    char line[1000000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* start = strchr(line, '[');\n        if (!start) start = line;\n        char* token = strtok(start, \"[], =\\r\\n\");\n        struct ListNode dummy = {0, NULL};\n        struct ListNode* curr = &dummy;\n        while (token) {\n            if (strcmp(token, \"head\") != 0) {\n                curr->next = createNode(atoi(token));\n                curr = curr->next;\n            }\n            token = strtok(NULL, \"[], =\\r\\n\");\n        }\n        printf(\"%s\\n\", isPalindrome(dummy.next) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
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
