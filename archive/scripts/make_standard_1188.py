import json
import os

def generate_json():
    problem_id = 1188
    title = "Design Bounded Blocking Queue"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1188. Design Bounded Blocking Queue</h3>
<p>Implement a thread-safe bounded blocking queue that has the following methods:</p>

<ul>
	<li><code>BoundedBlockingQueue(int capacity)</code> The constructor initializes the queue with a maximum <code>capacity</code>.</li>
	<li><code>void enqueue(int element)</code> Adds an <code>element</code> to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.</li>
	<li><code>int dequeue()</code> Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.</li>
	<li><code>int size()</code> Returns the number of elements currently in the queue.</li>
</ul>

<p>Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer thread that only calls the <code>enqueue</code> method or a consumer thread that only calls the <code>dequeue</code> method. The <code>size</code> method will be called after every test case.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong>
["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"]
[[2],[1],[],[],[0],[2],[3],[4],[]]

<strong>Output:</strong>
[null,null,1,0,null,null,null,null,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= capacity &lt;= 100</code></li>
	<li><code>1 &lt;= element &lt;= 1000</code></li>
	<li><code>enqueue</code>, <code>dequeue</code>, and <code>size</code> will be called at most <code>5000</code> times total.</li>
</ul>"""

    input_format = "A list of method names and a list of arguments for each method."
    output_format = "A list of return values for each method."

    constraints = [
        "1 <= capacity <= 100",
        "1 <= element <= 1000",
        "Calls <= 5000"
    ]

    # For the standardization, we'll use a sequential simulation if possible, 
    # but the problem name implies thread-safety. In many online compilers, 
    # the judge runs multiple threads. We'll provide a thread-safe boilerplate.
    
    explanation = """To design a Bounded Blocking Queue:
1. Use a standard Queue (e.g., `collections.deque`) to store elements.
2. Use a Mutex (Lock) to ensure thread-safety for all shared state.
3. Use two Condition Variables (or a single one):
   - `not_full`: Threads calling `enqueue` wait on this if `size == capacity`.
   - `not_empty`: Threads calling `dequeue` wait on this if `size == 0`.
4. `enqueue(element)`: Lock -> Wait while full -> Append -> Signal `not_empty` -> Unlock.
5. `dequeue()`: Lock -> Wait while empty -> Pop -> Signal `not_full` -> Return -> Unlock.
6. `size()`: Lock -> Return length -> Unlock."""

    answer = """import threading
import collections

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = collections.deque()
        self.condition = threading.Condition()

    def enqueue(self, element: int) -> None:
        with self.condition:
            while len(self.queue) == self.capacity:
                self.condition.wait()
            self.queue.append(element)
            self.condition.notify_all()

    def dequeue(self) -> int:
        with self.condition:
            while not self.queue:
                self.condition.wait()
            val = self.queue.popleft()
            self.condition.notify_all()
            return val

    def size(self) -> int:
        with self.condition:
            return len(self.queue)"""

    boilerplate = {
        "python": """import sys
import json
import threading
import collections

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        pass
    def enqueue(self, element: int) -> None:
        pass
    def dequeue(self) -> int:
        return 0
    def size(self) -> int:
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        methods, args = json.loads(raw)
        obj = None
        results = []
        for m, a in zip(methods, args):
            if m == "BoundedBlockingQueue":
                obj = BoundedBlockingQueue(a[0])
                results.append(None)
            elif m == "enqueue":
                results.append(obj.enqueue(a[0]))
            elif m == "dequeue":
                results.append(obj.dequeue())
            elif m == "size":
                results.append(obj.size())
        print(json.dumps(results).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class BoundedBlockingQueue {
public:
    BoundedBlockingQueue(int capacity) {}
    void enqueue(int element) {}
    int dequeue() { return 0; }
    int size() { return 0; }
};

int main() {
    // Simulator logic here
    return 0;
}""",
        "java": """import java.util.*;
import java.util.concurrent.*;

class BoundedBlockingQueue {
    public BoundedBlockingQueue(int capacity) {}
    public void enqueue(int element) throws InterruptedException {}
    public int dequeue() throws InterruptedException { return 0; }
    public int size() { return 0; }
}

public class Main {
    public static void main(String[] args) throws Exception {
        // Simulator logic here
    }
}""",
        "javascript": """var BoundedBlockingQueue = function(capacity) {
    this.capacity = capacity;
};
BoundedBlockingQueue.prototype.enqueue = function(element) {};
BoundedBlockingQueue.prototype.dequeue = function() { return 0; };
BoundedBlockingQueue.prototype.size = function() { return 0; };

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    // Simulator logic...
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct {
} BoundedBlockingQueue;

BoundedBlockingQueue* constructor(int capacity) { return NULL; }
void enqueue(BoundedBlockingQueue *obj, int element) {}
int dequeue(BoundedBlockingQueue *obj) { return 0; }
int size(BoundedBlockingQueue *obj) { return 0; }

int main() {
    return 0;
}"""
    }

    def solve(methods, args):
        results = []
        q = collections.deque()
        cap = 0
        for m, a in zip(methods, args):
            if m == "BoundedBlockingQueue":
                cap = a[0]
                results.append(None)
            elif m == "enqueue":
                q.append(a[0])
                results.append(None)
            elif m == "dequeue":
                results.append(q.popleft())
            elif m == "size":
                results.append(len(q))
        return results

    import collections
    test_cases_data = [
        [["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"], [[2],[1],[],[],[0],[2],[3],[4],[]]], # Sample 1
        [["BoundedBlockingQueue","enqueue","dequeue","size"], [[1],[1],[],[]]], # Sample small
        [["BoundedBlockingQueue","enqueue","enqueue","size"], [[2],[1],[2],[]]],
        [["BoundedBlockingQueue","size"], [[5],[]]],
        # Design patterns often have complex interactive tests. We'll simplify for standardized test cases.
        [["BoundedBlockingQueue", "enqueue", "enqueue", "dequeue", "size"], [[2], [1], [2], [], []]],
        [["BoundedBlockingQueue", "enqueue", "size", "dequeue", "size"], [[10], [100], [], [], []]],
        [["BoundedBlockingQueue", "enqueue", "enqueue", "enqueue", "dequeue", "dequeue", "dequeue", "size"], [[3], [1], [2], [3], [], [], [], []]],
        # Stress tests (sequential simulation)
        [["BoundedBlockingQueue"] + ["enqueue"]*100 + ["dequeue"]*50 + ["size"], [[100]] + [[i] for i in range(100)] + [[]]*50 + [[]]],
        [["BoundedBlockingQueue"] + ["enqueue"]*10 + ["size"]*10, [[10]] + [[1]]*10 + [[]]*10],
        [["BoundedBlockingQueue", "enqueue", "dequeue"], [[1], [999], []]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 1})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Design", "Concurrency"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
