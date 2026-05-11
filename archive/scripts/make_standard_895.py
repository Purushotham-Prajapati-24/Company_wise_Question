import json
import collections
import os

def generate_json():
    problem_id = 895
    title = "Maximum Frequency Stack"
    difficulty = "Hard"
    marks = 30
    
    html_description = """<h3>895. Maximum Frequency Stack</h3>
<p>Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.</p>

<p>Implement the <code>FreqStack</code> class:</p>

<ul>
	<li><code>FreqStack()</code> constructs an empty frequency stack.</li>
	<li><code>void push(int val)</code> pushes an integer <code>val</code> onto the top of the stack.</li>
	<li><code>int pop()</code> removes and returns the most frequent element in the stack.
	<ul>
		<li>If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong>
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
<strong>Output:</strong>
[null, null, null, null, null, null, null, 5, 7, 5, 4]
<strong>Explanation:</strong>
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= val &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>2 * 10<sup>4</sup></code> calls will be made to <code>push</code> and <code>pop</code>.</li>
	<li>It is guaranteed that there will be at least one element in the stack before calling <code>pop</code>.</li>
</ul>
"""

    input_format = "List of operations and values."
    output_format = "List of operation results."
    
    constraints = [
        "0 <= val <= 10^9",
        "At most 20,000 calls."
    ]
    
    explanation = """To implement FreqStack efficiently (O(1) push and pop):
1. **Maintain Frequency Count**:
   - Use a hash map `freq` to store the frequency of each element in the stack.
2. **Group Elements by Frequency**:
   - Use another hash map `group` where each key is a frequency, and the value is a stack of elements that have at least that frequency.
   - For example, if we push `5, 7, 5`, then `group[1] = [5, 7]` and `group[2] = [5]`.
3. **Handle Ties**:
   - If there is a tie, we need the element closest to the top. Storing elements in stacks within the `group` map naturally handles this because the most recent element pushed for a given frequency is at the top of that specific stack.
4. **Operations**:
   - `push(val)`:
     - Increment `freq[val]`.
     - Update `max_freq` accordingly.
     - Push `val` to `group[freq[val]]`.
   - `pop()`:
     - Return the top element from `group[max_freq]`.
     - Decrement the target element frequency in the `freq` map.
     - If the stack at `group[max_freq]` becomes empty, decrement `max_freq`.

Complexity:
- Time: O(1) for both `push` and `pop`.
- Space: O(N) where N is the number of elements pushed."""
    
    answer = """class FreqStack:
    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(val)

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return x"""

    boilerplate = {
        "python": "import sys\nimport json\nimport collections\n\nclass FreqStack:\n    def __init__(self):\n        pass\n    def push(self, val):\n        pass\n    def pop(self):\n        pass\n\nif __name__ == '__main__':\n    # Test harness parsing logic goes here\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <stack>\n\nusing namespace std;\n\nclass FreqStack {\npublic:\n    FreqStack() {}\n    void push(int val) {}\n    int pop() {\n        return 0;\n    }\n};",
        "java": "import java.util.*;\n\nclass FreqStack {\n    public FreqStack() {}\n    public void push(int val) {}\n    public int pop() {\n        return 0;\n    }\n}",
        "javascript": "var FreqStack = function() {};\nFreqStack.prototype.push = function(val) {};\nFreqStack.prototype.pop = function() {};",
        "c": "typedef struct {\n} FreqStack;\nFreqStack* freqStackCreate() {\n}\nvoid freqStackPush(FreqStack* obj, int val) {\n}\nint freqStackPop(FreqStack* obj) {\n}\nvoid freqStackFree(FreqStack* obj) {\n}"
    }

    test_cases = [
        {"input": '["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]\\n[[], [5], [7], [5], [7], [4], [5], [], [], [], []]', "expected_output": "[null, null, null, null, null, null, null, 5, 7, 5, 4]", "is_sample": True},
        # Diverse cases
        {"input": '["FreqStack", "push", "push", "pop"]\\n[[], [1], [1], []]', "expected_output": "[null, null, null, 1]", "is_sample": False},
        {"input": '["FreqStack", "push", "pop", "push", "pop"]\\n[[], [10], [], [20], []]', "expected_output": "[null, null, 10, null, 20]", "is_sample": False},
        {"input": '["FreqStack", "push", "push", "push", "pop", "pop", "pop"]\\n[[], [1], [2], [3], [], [], []]', "expected_output": "[null, null, null, null, 3, 2, 1]", "is_sample": False},
        {"input": '["FreqStack", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]\\n[[], [1], [1], [2], [2], [], [], [], []]', "expected_output": "[null, null, null, null, null, 2, 1, 2, 1]", "is_sample": False},
        # Ties close to top
        {"input": '["FreqStack", "push", "push", "push", "pop", "pop"]\\n[[], [5], [5], [6], [], []]', "expected_output": "[null, null, null, null, 5, 6]", "is_sample": False},
        {"input": '["FreqStack", "push", "push", "push", "push", "pop", "pop"]\\n[[], [1], [2], [1], [2], [], []]', "expected_output": "[null, null, null, null, null, 2, 1]", "is_sample": False},
        # Repeating pattern
        {"input": '["FreqStack", "push", "push", "pop", "push", "pop"]\\n[[], [4], [4], [], [4], []]', "expected_output": "[null, null, null, 4, null, 4]", "is_sample": False},
        # Large values
        {"input": '["FreqStack", "push", "pop"]\\n[[], [1000000000], []]', "expected_output": "[null, null, 1000000000]", "is_sample": False},
        # Mix
        {"input": '["FreqStack", "push", "push", "push", "push", "pop", "push", "pop", "pop"]\\n[[], [1], [2], [3], [4], [], [5], [], []]', "expected_output": "[null, null, null, null, null, 4, null, 5, 3]", "is_sample": False}
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
        "topics": ["Hash Table", "Stack", "Design"],
        "companyIndex": 0
    }

    output_path = "standardized_json/801-1000/895_Maximum_Frequency_Stack.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
