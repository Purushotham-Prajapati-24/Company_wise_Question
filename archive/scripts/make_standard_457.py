import json
import os

def generate_json():
    problem_id = 457
    title = "Circular Array Loop"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>457. Circular Array Loop</h3>
<p>You are given a <strong>cyclic</strong> array <code>nums</code> of positive and negative integers. If a number <code>k</code> at an index is positive, then move forward <code>k</code> steps. Conversely, if it's negative (-<code>k</code>), move backward <code>k</code> steps. Since the array is cyclic, you may assume that moving forward from the last element puts you on the first element, and moving backward from the first element puts you on the last element.</p>

<p>A cycle in the array consists of a sequence of indices <code>seq</code> of length <code>k</code> where:</p>

<ul>
	<li>Following the movement rules above results in the repeating sequence of indices <code>seq[0] -&gt; seq[1] -&gt; ... -&gt; seq[k - 1] -&gt; seq[0] -&gt; ...</code></li>
	<li>Every <code>nums[seq[j]]</code> is either <strong>all positive</strong> or <strong>all negative</strong>.</li>
	<li><code>k &gt; 1</code></li>
</ul>

<p>Return <code>true</code><em> if there is a cycle in </em><code>nums</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,-1,1,2,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --&gt; 2 --&gt; 3 --&gt; 0, all nodes are positive.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-1,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
The node 0 jumps to node 1, and node 1 jumps to node 1. That is a self-cycle of length 1.
So it is not a cycle.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [-2,1,-1,-2,-2]
<strong>Output:</strong> false
<strong>Explanation:</strong> The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
The only cycle would be defferent direction nodes [1 -&gt; 2 -&gt; 1]. So it is not a cycle.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums[i] != 0</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve it in <code>O(n)</code> time complexity and <code>O(1)</code> extra space complexity?</p>"""

    input_format = "An integer array nums."
    output_format = "Boolean representing if a valid cycle exists."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def solve(nums):
    n = len(nums)
    
    def get_next(i):
        return (i + nums[i]) % n
    
    for i in range(n):
        if nums[i] == 0:
            continue
            
        slow = i
        fast = get_next(i)
        
        while nums[i] * nums[fast] > 0 and nums[i] * nums[get_next(fast)] > 0:
            if slow == fast:
                if slow == get_next(slow):
                    break
                return True
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        # Optimization: mark visited nodes as 0
        slow = i
        val = nums[i]
        while val * nums[slow] > 0:
            next_idx = get_next(slow)
            nums[slow] = 0
            slow = next_idx
            
    return False"""

    boilerplate = {
        "python": "import sys\n\ndef get_next(i):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    i = input_data[0] if len(input_data) > 0 else \"\"\n    print(get_next(i))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint get_next(string i) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string i; cin >> i;\n    cout << get_next(i) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
