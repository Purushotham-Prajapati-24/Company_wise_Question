import json
import os

def generate_json():
    problem_id = 432
    title = "All O`one Data Structure"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>432. All O`one Data Structure</h3>
<p>Design a data structure that supports the following operations in <code>O(1)</code> time complexity for each:</p>

<ul>
	<li><code>inc(key)</code>: Inserts a new key with value 1 or increments an existing key's value by 1.</li>
	<li><code>dec(key)</code>: Decrements an existing key's value by 1. If its value is 0 after decrementing, remove it.</li>
	<li><code>getMaxKey()</code>: Returns any key with the maximum value. If no keys exist, return <code>""</code>.</li>
	<li><code>getMinKey()</code>: Returns any key with the minimum value. If no keys exist, return <code>""</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
<strong>Output:</strong> 
[null, null, null, "hello", "hello", null, "hello", "leet"]
<strong>Explanation:</strong>
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= key.length &lt;= 10</code></li>
	<li><code>key</code> consists of lowercase English letters.</li>
	<li>At most <code>5 * 10<sup>4</sup></code> calls will be made to <code>inc</code>, <code>dec</code>, <code>getMaxKey</code>, and <code>getMinKey</code>.</li>
</ul>"""

    input_format = "A list of strings representing operations and a list of arguments."
    output_format = "A list of results corresponding to the operations."
    
    constraints = ["1 <= key.length <= 10", "At most 5 * 10^4 calls.", "O(1) time complexity for each operation."]
    
    explanation = """HARD problem on ."""
    
    answer = """class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None
        
class AllOne:
    def __init__(self):
        self.root = Node()
        self.root.next = self.root
        self.root.prev = self.root
        self.map = {}
        
    def inc(self, key):
        if key not in self.map:
            if self.root.next == self.root or self.root.next.count > 1:
                node = Node(1)
                node.next = self.root.next
                node.prev = self.root
                self.root.next.prev = node
                self.root.next = node
            else:
                node = self.root.next
            node.keys.add(key)
            self.map[key] = node
        else:
            node = self.map[key]
            next_node = node.next
            if next_node == self.root or next_node.count > node.count + 1:
                new_node = Node(node.count + 1)
                new_node.next = next_node
                new_node.prev = node
                next_node.prev = new_node
                node.next = new_node
            else:
                new_node = next_node
            new_node.keys.add(key)
            self.map[key] = new_node
            self._remove_key(node, key)
            
    def dec(self, key):
        if key not in self.map: return
        node = self.map[key]
        if node.count == 1:
            del self.map[key]
        else:
            prev_node = node.prev
            if prev_node == self.root or prev_node.count < node.count - 1:
                new_node = Node(node.count - 1)
                new_node.next = node
                new_node.prev = prev_node
                prev_node.next = new_node
                node.prev = new_node
            else:
                new_node = prev_node
            new_node.keys.add(key)
            self.map[key] = new_node
        self._remove_key(node, key)
        
    def getMaxKey(self):
        return next(iter(self.root.prev.keys)) if self.root.prev != self.root else ""
        
    def getMinKey(self):
        return next(iter(self.root.next.keys)) if self.root.next != self.root else ""
        
    def _remove_key(self, node, key):
        node.keys.remove(key)
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev"""

    boilerplate = {
        "python": "import sys\n\ndef getMinKey():\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    print(getMinKey())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint getMinKey() {\n    // User logic\n    return 0;\n}\n\nint main() {\n    cout << getMinKey() << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": '["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]\\n[[], ["hello"], ["hello"], [], [], ["leet"], [], []]', "expected_output": '[null, null, null, "hello", "hello", null, "hello", "leet"]', "is_sample": True},
        {"input": '["AllOne", "getMaxKey", "getMinKey"]\\n[[], [], []]', "expected_output": '[null, "", ""]', "is_sample": True},
        {"input": '["AllOne", "inc", "inc", "dec", "getMaxKey", "getMinKey"]\\n[[], ["a"], ["a"], ["a"], [], []]', "expected_output": '[null, null, null, null, "a", "a"]', "is_sample": False},
        {"input": '["AllOne", "inc", "inc", "inc", "dec", "dec", "dec", "getMaxKey", "getMinKey"]\\n[[], ["a"], ["b"], ["c"], ["a"], ["b"], ["c"], [], []]', "expected_output": '[null, null, null, null, null, null, null, "", ""]', "is_sample": False},
        {"input": '["AllOne", "inc", "inc", "inc", "inc", "dec", "dec", "getMaxKey", "getMinKey"]\\n[[], ["a"], ["a"], ["a"], ["b"], ["a"], ["a"], [], []]', "expected_output": '[null, null, null, null, null, null, null, "a", "b"]', "is_sample": False},
        {"input": '["AllOne", "inc", "inc", "dec", "getMinKey"]\\n[[], ["a"], ["b"], ["a"], []]', "expected_output": '[null, null, null, null, "b"]', "is_sample": False},
        {"input": '["AllOne", "inc", "getMaxKey"]\\n[[], ["z"], []]', "expected_output": '[null, null, "z"]', "is_sample": False},
        # Stress tests]

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
