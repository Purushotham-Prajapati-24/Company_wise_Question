import json
import os
import heapq

def generate_json():
    problem_id = 23
    title = "Merge k Sorted Lists"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>23. Merge k Sorted Lists</h3>
<p>You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.</p>

<p><em>Merge all the linked-lists into one sorted linked-list and return it.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:</strong> The linked-lists are:
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
merging them into one sorted list:
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> lists = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>k == lists.length</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
	<li><code>-10<sup>4</sup> &lt;= lists[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>lists[i]</code> is sorted in <strong>ascending order</strong>.</li>
	<li>The sum of <code>lists[i].length</code> will not exceed <code>10<sup>4</sup></code>.</li>
</ul>
"""

    input_format = "Multiple lines. First line is an integer k. Then k lines follow, each containing space-separated integers for one list."
    output_format = "A string representing the merged sorted list as space-separated integers or a list."
    
    constraints = [
        "0 <= k <= 10^4",
        "0 <= lists[i].length <= 500",
        "Sum of lengths <= 10^4",
        "Each list is sorted in ascending order."
    ]
    
    explanation = """To merge k sorted linked lists efficiently:
1. Use a min-heap (priority queue) to store the heads of all k lists. Each entry in the heap should be a tuple (value, list_index, node_object). 
2. The `list_index` is included to handle cases where multiple nodes have the same value, providing a secondary comparison key and avoiding errors when comparing ListNode objects directly.
3. Initialize the heap by pushing the first node of every non-empty list.
4. While the heap is not empty:
   - Extract the smallest element (node) from the heap.
   - Attach this node to the end of your result list.
   - If the extracted node has a next node, push that next node into the heap.
5. This approach leverages the property that at any point, the overall smallest element must be among the heads of the current remaining lists.

Time Complexity: O(N log k), where N is the total number of nodes and k is the number of lists.
Space Complexity: O(k) for the heap."""
    
    answer = """import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        # This is a fallback, but we should use list_index in heap tuples
        return self.val < other.val

def mergeKLists(lists):
    h = []
    for i, l in enumerate(lists):
        if l:
            # push (value, list_index, node)
            heapq.heappush(h, (l.val, i, l))
    
    dummy = ListNode()
    curr = dummy
    while h:
        val, i, node = heapq.heappop(h)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(h, (node.next.val, i, node.next))
    return dummy.next"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef mergeKLists(lists):\n    # User logic here\n    pass\n\ndef to_list(node):\n    res = []\n    while node:\n        res.append(node.val)\n        node = node.next\n    return res\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if not input_data: print(\"[]\"); sys.exit()\n    k = int(input_data[0].strip())\n    lists = []\n    for i in range(1, k + 1):\n        if i < len(input_data):\n            nums = [int(x) for x in input_data[i].split() if x.strip()]\n            dummy = ListNode(0)\n            curr = dummy\n            for val in nums:\n                curr.next = ListNode(val)\n                curr = curr.next\n            lists.append(dummy.next)\n        else:\n            lists.append(None)\n    res = mergeKLists(lists)\n    print(json.dumps(to_list(res)).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode() : val(0), next(nullptr) {}\n    ListNode(int x) : val(x), next(nullptr) {}\n    ListNode(int x, ListNode *next) : val(x), next(next) {}\n};\n\nListNode* mergeKLists(vector<ListNode*>& lists) {\n    // User logic\n    return nullptr;\n}\n\nint main() {\n    string line;\n    if (!getline(cin, line)) return 0;\n    int k;\n    stringstream sk(line);\n    sk >> k;\n    vector<ListNode*> lists(k, nullptr);\n    for (int i = 0; i < k; ++i) {\n        if (!getline(cin, line)) break;\n        stringstream ss(line);\n        int val;\n        ListNode dummy(0);\n        ListNode* curr = &dummy;\n        while (ss >> val) {\n            curr->next = new ListNode(val);\n            curr = curr->next;\n        }\n        lists[i] = dummy.next;\n    }\n    \n    ListNode* res = mergeKLists(lists);\n    cout << \"[\";\n    while (res) {\n        cout << res->val;\n        if (res->next) cout << \", \";\n        res = res->next;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode() {}\n    ListNode(int val) { this.val = val; }\n    ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n}\n\npublic class Main {\n    public static ListNode mergeKLists(ListNode[] lists) {\n        // User logic\n        return null;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String firstLine = sc.nextLine().trim();\n        if (firstLine.isEmpty()) return;\n        int k = Integer.parseInt(firstLine);\n        ListNode[] lists = new ListNode[k];\n        for (int i = 0; i < k; i++) {\n            if (!sc.hasNextLine()) break;\n            String line = sc.nextLine().trim();\n            ListNode dummy = new ListNode(0);\n            ListNode curr = dummy;\n            if (!line.isEmpty()) {\n                String[] parts = line.split(\"\\\\s+\");\n                for (String p : parts) {\n                    curr.next = new ListNode(Integer.parseInt(p));\n                    curr = curr.next;\n                }\n            }\n            lists[i] = dummy.next;\n        }\n        ListNode res = mergeKLists(lists);\n        System.out.print(\"[\");\n        while (res != null) {\n            System.out.print(res.val);\n            if (res.next != null) System.out.print(\", \");\n            res = res.next;\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction mergeKLists(lists) {\n    // User logic\n    return null;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length > 0 && input[0].trim() !== '') {\n    const k = parseInt(input[0].trim());\n    let lists = [];\n    for (let i = 1; i <= k; i++) {\n        let dummy = new ListNode(0);\n        let curr = dummy;\n        if (i < input.length && input[i].trim() !== '') {\n            let nums = input[i].trim().split(/\\s+/).map(Number);\n            for (let val of nums) {\n                curr.next = new ListNode(val);\n                curr = curr.next;\n            }\n        }\n        lists.push(dummy.next);\n    }\n    let res = mergeKLists(lists);\n    let out = [];\n    while (res) {\n        out.push(res.val);\n        res = res.next;\n    }\n    console.log(JSON.stringify(out).replace(/,/g, \", \"));\n} else {\n    console.log(\"[]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {\n    // User logic\n    return NULL;\n}\n\nint main() {\n    char line[20000];\n    if (fgets(line, sizeof(line), stdin)) {\n        int k = atoi(line);\n        struct ListNode** lists = (struct ListNode**)malloc(k * sizeof(struct ListNode*));\n        for (int i = 0; i < k; i++) {\n            lists[i] = NULL;\n            if (fgets(line, sizeof(line), stdin)) {\n                struct ListNode dummy;\n                dummy.next = NULL;\n                struct ListNode* curr = &dummy;\n                char* token = strtok(line, \" \\r\\n\");\n                while (token != NULL) {\n                    curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n                    curr->next->val = atoi(token);\n                    curr->next->next = NULL;\n                    curr = curr->next;\n                    token = strtok(NULL, \" \\r\\n\");\n                }\n                lists[i] = dummy.next;\n            }\n        }\n        struct ListNode* res = mergeKLists(lists, k);\n        printf(\"[\");\n        while (res != NULL) {\n            printf(\"%d\", res->val);\n            if (res->next != NULL) printf(\", \");\n            res = res->next;\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    def _merge_ref(lists):
        merged = []
        for l in lists: merged.extend(l)
        return sorted(merged)

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "3\n1 4 5\n1 3 4\n2 6", "expected_output": str(_merge_ref([[1,4,5],[1,3,4],[2,6]])), "is_sample": True},
        {"input": "0", "expected_output": "[]", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1\n", "expected_output": "[]", "is_sample": False},
        {"input": "1\n1 2 3", "expected_output": "[1, 2, 3]", "is_sample": False},
        {"input": "2\n\n1 2 3", "expected_output": "[1, 2, 3]", "is_sample": False},
        {"input": "3\n1\n0\n-1", "expected_output": "[-1, 0, 1]", "is_sample": False},
        {"input": "2\n10 20\n5 15 25", "expected_output": "[5, 10, 15, 20, 25]", "is_sample": False},
        # Last three: Stress tests
        {"input": "100\n" + "\n".join(["1"]*100), "expected_output": str([1]*100), "is_sample": False},
        {"input": "1\n" + " ".join([str(i) for i in range(1000)]), "expected_output": str(list(range(1000))), "is_sample": False},
        {"input": "2\n" + " ".join([str(i*2) for i in range(500)]) + "\n" + " ".join([str(i*2+1) for i in range(500)]), "expected_output": str(list(range(1000))), "is_sample": False}
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
        "topics": ["Linked List", "Divide and Conquer", "Heap (Priority Queue)", "Merge Sort"],
        "companyIndex": 0
    }

    output_path = "1-200/23_Merge_k_Sorted_Lists.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
