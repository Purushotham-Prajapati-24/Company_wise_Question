import json
import os

def generate_json():
    problem_id = 460
    title = "LFU Cache"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>460. LFU Cache</h3>
<p>Design and implement a data structure for a <a href="https://en.wikipedia.org/wiki/Least_frequently_used" target="_blank">Least Frequently Used (LFU)</a> cache.</p>

<p>Implement the <code>LFUCache</code> class:</p>

<ul>
	<li><code>LFUCache(int capacity)</code> Initializes the object with the <code>capacity</code> of the data structure.</li>
	<li><code>int get(int key)</code> Gets the value of the <code>key</code> if the <code>key</code> exists in the cache. Otherwise, returns <code>-1</code>.</li>
	<li><code>void put(int key, int value)</code> Update the value of the <code>key</code> if present, or inserts the <code>key</code> if not already present. When the cache reaches its <code>capacity</code>, it should invalidate and remove the <strong>least frequently used</strong> key before inserting a new item. For this problem, when there is a <strong>tie</strong> (i.e., two or more keys with the same frequency), the <strong>least recently used</strong> key would be invalidated.</li>
</ul>

<p>To determine the least frequently used key, a <strong>use counter</strong> is maintained for each key in the cache. The key with the smallest <strong>use counter</strong> is the least frequently used key.</p>

<p>When a key is first inserted into the cache, its <strong>use counter</strong> is set to <code>1</code> (i.e., one use). The <strong>use counter</strong> for a key in the cache is incremented either a <code>get</code> or <code>put</code> operation is called on it.</p>

<p>The functions&nbsp;<code>get</code>&nbsp;and&nbsp;<code>put</code>&nbsp;must each run in <code>O(1)</code> average time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
<strong>Output</strong>
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

<strong>Explanation</strong>
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
lfu.put(4, 4);   // both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
lfu.get(4);      // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= capacity &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= key &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>get</code> and <code>put</code>.</li>
</ul>"""

    input_format = "Line 1: A JSON array of strings representing the operations.\\nLine 2: A JSON 2D array of integers representing the arguments for each operation."
    output_format = "A JSON array of results for each operation (null for void returns)."
    
    constraints = [
        "1 <= capacity <= 10^4",
        "0 <= key <= 10^5",
        "0 <= value <= 10^9",
        "At most 2 * 10^5 calls to get and put."
    ]
    
    explanation = "O(1) requirement for both get and put suggests using a combination of hash maps and doubly linked lists. We can maintain a map from frequency to a doubly linked list of nodes with that frequency. Each node stores its key, value, and frequency. A separate map from key to node allows quick access. When frequency changes, move the node to the next frequency's list."
    
    answer = """import collections

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.freq = 1
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
    def append(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = self.head.next = node
        self.size += 1
    def pop(self, node=None):
        if self.size == 0: return None
        if not node: node = self.tail.prev
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.cap, self.size, self.min_freq = capacity, 0, 0
        self.node_map = {}
        self.freq_map = collections.defaultdict(DoublyLinkedList)
    def _update(self, node):
        self.freq_map[node.freq].pop(node)
        if self.min_freq == node.freq and not self.freq_map[node.freq].size:
            self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].append(node)
    def get(self, key: int) -> int:
        if key not in self.node_map: return -1
        node = self.node_map[key]
        self._update(node)
        return node.val
    def put(self, key: int, value: int) -> None:
        if not self.cap: return
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self._update(node)
        else:
            if self.size == self.cap:
                node = self.freq_map[self.min_freq].pop()
                del self.node_map[node.key]
                self.size -= 1
            node = Node(key, value)
            self.node_map[key] = node
            self.freq_map[1].append(node)
            self.min_freq = 1
            self.size += 1"""

    boilerplate = {
        "python": r"""import sys
import json
import collections

class LFUCache:
    def __init__(self, capacity: int):
        # User Logic Here
        pass

    def get(self, key: int) -> int:
        # User Logic Here
        return -1

    def put(self, key: int, value: int) -> None:
        # User Logic Here
        pass

if __name__ == '__main__':
    lines = sys.stdin.read().strip().splitlines()
    if len(lines) >= 2:
        methods = json.loads(lines[0])
        args = json.loads(lines[1])
        obj = None
        results = []
        for m, a in zip(methods, args):
            if m == "LFUCache":
                obj = LFUCache(a[0])
                results.append(None)
            elif m == "get":
                results.append(obj.get(a[0]) if obj else -1)
            elif m == "put":
                if obj: obj.put(a[0], a[1])
                results.append(None)
        print(json.dumps(results))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <list>
#include <algorithm>

using namespace std;

class LFUCache {
public:
    LFUCache(int capacity) {
        // User Logic Here
    }
    int get(int key) {
        // User Logic Here
        return -1;
    }
    void put(int key, int value) {
        // User Logic Here
    }
};

int main() {
    // Simplified JSON-like parsing for method names and args
    string methodsLine, argsLine;
    if (getline(cin, methodsLine) && getline(cin, argsLine)) {
        // Parsing logic here... 
        // For simplicity in boilerplate, we'll output a dummy or valid JSON result.
        cout << "[null]" << endl; // Replacement by user
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class LFUCache {
    public LFUCache(int capacity) {
        // User Logic Here
    }
    public int get(int key) {
        // User Logic Here
        return -1;
    }
    public void put(int key, int value) {
        // User Logic Here
    }
}

public class Main {
    public static void main(String[] args) {
        // Driver code to execute get/put
        System.out.println("[null]");
    }
}""",
        "javascript": r"""class LFUCache {
    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        // User Logic Here
    };

    /** 
     * @param {number} key
     * @return {number}
     */
    get(key) {
        // User Logic Here
    };

    /** 
     * @param {number} key 
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        // User Logic Here
    };
}

const fs = require('fs');
console.log("[null]");""",
        "c": r"""#include <stdio.h>
#include <stdlib.h>

typedef struct {
    // User Logic Here
} LFUCache;

LFUCache* lFUCacheCreate(int capacity) {
    return NULL;
}

int lFUCacheGet(LFUCache* obj, int key) {
    return -1;
}

void lFUCachePut(LFUCache* obj, int key, int value) {
}

void lFUCacheFree(LFUCache* obj) {
}

int main() {
    printf("[null]\n");
    return 0;
}"""
    }

    test_cases = [
        {"input": "[\"LFUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"get\", \"put\", \"get\", \"get\", \"get\"]\\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]", "expected_output": "[null, null, null, 1, null, -1, 3, null, -1, 3, 4]", "is_sample": True},
        {"input": "[\"LFUCache\", \"put\", \"get\"]\\n[[0], [0, 0], [0]]", "expected_output": "[null, null, -1]", "is_sample": True},
        {"input": "[\"LFUCache\", \"put\", \"put\", \"put\", \"put\", \"get\"]\\n[[2], [1, 1], [2, 2], [3, 3], [4, 4], [3]]", "expected_output": "[null, null, null, null, null, -1]", "is_sample": False},
        {"input": "[\"LFUCache\", \"put\", \"get\", \"put\", \"get\"]\\n[[1], [1, 1], [1], [2, 2], [1]]", "expected_output": "[null, null, 1, null, -1]", "is_sample": False},
        {"input": "[\"LFUCache\", \"put\", \"put\", \"get\", \"get\", \"put\", \"get\"]\\n[[2], [1, 1], [2, 2], [1], [1], [3, 3], [2]]", "expected_output": "[null, null, null, 1, 1, null, -1]", "is_sample": False},
        {"input": "[\"LFUCache\", \"get\"]\\n[[2], [1]]", "expected_output": "[null, -1]", "is_sample": False},
        {"input": "[\"LFUCache\", \"put\", \"put\", \"put\", \"get\", \"get\"]\\n[[1], [1, 1], [2, 2], [3, 3], [1], [2]]", "expected_output": "[null, null, null, null, -1, -1]", "is_sample": False},
        {"input": "[\"LFUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"get\"]\\n[[2], [1, 1], [2, 2], [1], [2, 2], [1], [2]]", "expected_output": "[null, null, null, 1, null, 1, 2]", "is_sample": False},
        # Stress
        {"input": "[\"LFUCache\"] + [\"put\"] * 10\\n[[5]] + [[i, i] for i in range(10)]", "expected_output": "[null] + [null] * 10", "is_sample": False, "is_template": True},
        {"input": "[\"LFUCache\"] + [\"put\", \"get\"] * 5\\n[[2]] + [[1, 1], [1], [2, 2], [2], [3, 3], [1], [4, 4], [2], [5, 5], [3]]", "expected_output": "[null] + [null, 1, null, 2, null, -1, null, -1, null, -1]", "is_sample": False, "is_template": True}
    ]
    
    # Resolving templates
    actual_test_cases = []
    for tc in test_cases:
        if tc.get("is_template"):
            if "Stress" in str(tc): # Custom logic for complex cases
                pass # Already handled below
            else:
                actual_test_cases.append(tc)
        else:
            actual_test_cases.append(tc)
            
    # Cleanup stress cases
    test_cases = actual_test_cases[:8]
    test_cases.append({
        "input": "[\"LFUCache\", \"put\", \"put\", \"put\", \"put\", \"put\", \"get\", \"get\", \"get\", \"get\", \"get\"]\\n[[5], [0,0], [1,1], [2,2], [3,3], [4,4], [0], [1], [2], [3], [4]]",
        "expected_output": "[null, null, null, null, null, null, 0, 1, 2, 3, 4]",
        "is_sample": False
    })
    test_cases.append({
        "input": "[\"LFUCache\", \"put\", \"put\", \"put\", \"put\", \"put\", \"put\"]\\n[[2], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6]]",
        "expected_output": "[null, null, null, null, null, null, null]",
        "is_sample": False
    })

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
        "topics": ["Hash Table", "Linked List", "Design", "Doubly-Linked List"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_LFU_Cache.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
