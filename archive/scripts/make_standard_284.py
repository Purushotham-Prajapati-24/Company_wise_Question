import json
import os

def generate_json():
    problem_id = 284
    title = "Peeking Iterator"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>284. Peeking Iterator</h3>
<p>Design an iterator that supports the <code>peek</code> operation on an existing iterator in addition to the <code>hasNext</code> and the <code>next</code> operations.</p>

<p>Implement the <code>PeekingIterator</code> class:</p>
<ul>
	<li><code>PeekingIterator(Iterator&lt;Integer&gt; iterator)</code> Initializes the object with the given integer iterator <code>iterator</code>.</li>
	<li><code>int next()</code> Returns the next element in the array and moves the pointer to the next element.</li>
	<li><code>boolean hasNext()</code> Returns <code>true</code> if there are still elements in the array.</li>
	<li><code>int peek()</code> Returns the next element in the array <strong>without</strong> moving the pointer.</li>
</ul>

<p><strong>Note:</strong> Each language may have a different implementation of the <code>Iterator</code> interface, but they all support the <code>next</code> and <code>hasNext</code> functions.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
<strong>Output:</strong>
[null, 1, 2, 2, 3, false]

<strong>Explanation:</strong>
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3].
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3].
peekingIterator.hasNext(); // return false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li>All the calls to <code>next</code> and <code>peek</code> are valid.</li>
	<li>At most <code>1000</code> calls will be made to <code>next</code>, <code>hasNext</code>, and <code>peek</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> How would you extend your design to be generic and work with all types, not just integer?"""

    input_format = "A list of commands and values for the iterator."
    output_format = "A stringified array of the results of each call."
    
    constraints = [
        "1 <= nums.length <= 1,000",
        "1 <= nums[i] <= 1,000",
        "At most 1000 calls total."
    ]
    
    explanation = """To add `peek()` support to an existing iterator:
1. **Caching mechanism**: We maintain a variable `next_val` to cache the value that we've retrieved from the underlying iterator but haven't "consumed" yet via `next()`.
2. **Flag**: We use a `has_peeked` boolean to track whether `next_val` contains a value.
3. **Logic**:
   - `peek()`: If `has_peeked` is false, retrieve the next value from the underlying iterator, store it in `next_val`, and set `has_peeked = true`. Return `next_val`.
   - `next()`: If `has_peeked` is true, set `has_peeked = false` and return `next_val`. Otherwise, just call and return the underlying iterator's `next()`.
   - `hasNext()`: Return true if `has_peeked` is true OR the underlying iterator `hasNext()`.
4. **Complexity Analysis**:
   - Time: O(1) for all operations.
   - Space: O(1) for the cache."""
    
    answer = """class PeekingIterator:
    def __init__(self, iterator):
        # Initialize with the given iterator
        self.iterator = iterator
        self.next_val = None
        self.has_peeked = False

    def peek(self):
        # If we haven't peeked yet, grab the next value from the iterator
        if not self.has_peeked:
            self.next_val = self.iterator.next()
            self.has_peeked = True
        return self.next_val

    def next(self):
        # If we have a peeked value, return it and clear the peek flag
        if self.has_peeked:
            res = self.next_val
            self.has_peeked = False
            self.next_val = None
            return res
        return self.iterator.next()

    def hasNext(self):
        # True if we have a peeked value or the underlying iterator has more
        return self.has_peeked or self.iterator.hasNext()"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Iterator:\n    def __init__(self, nums):\n        self.nums = nums\n        self.idx = 0\n    def hasNext(self):\n        return self.idx < len(self.nums)\n    def next(self):\n        val = self.nums[self.idx]\n        self.idx += 1\n        return val\n\nclass PeekingIterator:\n    def __init__(self, iterator):\n        # User logic here\n        pass\n    def peek(self):\n        # User logic here\n        pass\n    def next(self):\n        # User logic here\n        pass\n    def hasNext(self):\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        cmds = json.loads(lines[0])\n        args = json.loads(lines[1])\n        obj = None\n        results = []\n        for i, cmd in enumerate(cmds):\n            if cmd == 'PeekingIterator':\n                obj = PeekingIterator(Iterator(args[i][0]))\n                results.append(None)\n            elif cmd == 'peek':\n                results.append(obj.peek())\n            elif cmd == 'next':\n                results.append(obj.next())\n            elif cmd == 'hasNext':\n                results.append(obj.hasNext())\n        print(json.dumps(results))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nclass Iterator {\n    vector<int> data;\n    int idx;\npublic:\n    Iterator(vector<int>& nums) : data(nums), idx(0) {}\n    bool hasNext() const { return idx < (int)data.size(); }\n    int next() { return data[idx++]; }\n};\n\nclass PeekingIterator {\npublic:\n    PeekingIterator(const vector<int>& nums) {\n        // User logic here\n    }\n    int peek() { return 0; }\n    int next() { return 0; }\n    bool hasNext() const { return false; }\n};\n\nint main() {\n    // Stub: full integration requires JSON command parsing\n    cout << \"[]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    static class PeekingIterator implements Iterator<Integer> {\n        private Iterator<Integer> iter;\n        private Integer peeked = null;\n        public PeekingIterator(Iterator<Integer> iterator) {\n            // User logic here\n            this.iter = iterator;\n        }\n        public Integer peek() {\n            // User logic here\n            return -1;\n        }\n        @Override\n        public Integer next() {\n            // User logic here\n            return -1;\n        }\n        @Override\n        public boolean hasNext() {\n            // User logic here\n            return false;\n        }\n    }\n    public static void main(String[] args) {\n        // Stub\n        System.out.println(\"[]\");\n    }\n}",
        "javascript": "const fs = require('fs');\nconst lines = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nconst cmds = JSON.parse(lines[0]);\nconst cmdArgs = JSON.parse(lines[1]);\n\nclass PeekingIterator {\n    constructor(iterator) {\n        // User logic here\n        this.iter = iterator;\n        this.peeked = undefined;\n    }\n    peek() { return 0; }\n    next() { return 0; }\n    hasNext() { return false; }\n}\n\nconst results = [];\nlet obj = null;\nfor (let i = 0; i < cmds.length; i++) {\n    if (cmds[i] === 'PeekingIterator') {\n        const nums = cmdArgs[i][0];\n        let idx = 0;\n        const iter = { hasNext: () => idx < nums.length, next: () => nums[idx++] };\n        obj = new PeekingIterator(iter);\n        results.push(null);\n    } else if (cmds[i] === 'peek') results.push(obj.peek());\n    else if (cmds[i] === 'next') results.push(obj.next());\n    else if (cmds[i] === 'hasNext') results.push(obj.hasNext());\n}\nconsole.log(JSON.stringify(results));",
        "c": "#include <stdio.h>\n\n// C stub for Peeking Iterator\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["PeekingIterator","next","peek","next","next","hasNext"]\\n[[[1,2,3]],[],[],[],[],[]]', "expected_output": '[null,1,2,2,3,false]', "is_sample": True},
        {"input": '["PeekingIterator","peek","peek","next","hasNext"]\\n[[[10]],[],[],[],[]]', "expected_output": "[null,10,10,10,false]", "is_sample": True},
        {"input": '["PeekingIterator","hasNext","next","hasNext"]\\n[[[5]],[],[],[]]', "expected_output": "[null,true,5,false]", "is_sample": False},
        {"input": '["PeekingIterator","next","next"]\\n[[[1,2]],[],[]]', "expected_output": "[null,1,2]", "is_sample": False},
        {"input": '["PeekingIterator","peek","next"]\\n[[[1,2]],[],[]]', "expected_output": "[null,1,1]", "is_sample": False},
        {"input": '["PeekingIterator","hasNext","peek","next","hasNext"]\\n[[[7,8]],[],[],[],[]]', "expected_output": "[null,true,7,7,true]", "is_sample": False},
        {"input": '["PeekingIterator","next","hasNext","peek","next"]\\n[[[100,200]],[],[],[],[]]', "expected_output": "[null,100,true,200,200]", "is_sample": False},
        # Stress cases
        {"input": '["PeekingIterator",' + ",".join(['"next"']*100) + ']\\n[[[' + ",".join([str(i) for i in range(100)]) + ']],' + ",".join(['[]']*100) + ']', "expected_output": '[null,' + ",".join([str(i) for i in range(100)]) + ']', "is_sample": False},
        {"input": '["PeekingIterator",' + ",".join(['"peek"']*50 + ['"next"']*50) + ']\\n[[[' + ",".join([str(i) for i in range(50)]) + ']],' + ",".join(['[]']*100) + ']', "expected_output": '[null,' + ",".join(['0']*50) + ',' + ",".join([str(i) for i in range(50)]) + ']', "is_sample": False},
        {"input": '["PeekingIterator",' + ",".join(['"hasNext"']*50 + ['"next"']*50) + ']\\n[[[' + ",".join([str(i) for i in range(50)]) + ']],' + ",".join(['[]']*100) + ']', "expected_output": '[null,' + ",".join(['true']*50) + ',' + ",".join([str(i) for i in range(50)]) + ']', "is_sample": False}
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
        "topics": ["Array", "Design", "Iterator"],
        "companyIndex": 0
    }

    output_path = "201-400/284_Peeking_Iterator.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
