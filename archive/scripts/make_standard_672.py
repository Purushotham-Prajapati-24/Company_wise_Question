import json
import os

def generate_json():
    problem_id = 672
    title = "Bulb Switcher II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>672. Bulb Switcher II</h3>
<p>There is a room with <code>n</code> bulbs labeled from <code>1</code> to <code>n</code> that all are turned on initially, and four buttons on the wall. Each of the four buttons has a different functionality:</p>

<ol>
	<li><strong>Button 1:</strong> Flips the status of all the bulbs.</li>
	<li><strong>Button 2:</strong> Flips the status of all the bulbs with even labels (i.e., 2, 4, ...).</li>
	<li><strong>Button 3:</strong> Flips the status of all the bulbs with odd labels (i.e., 1, 3, ...).</li>
	<li><strong>Button 4:</strong> Flips the status of all the bulbs with a label <code>j = 3k + 1</code> where <code>k = 0, 1, 2, ...</code> (i.e., 1, 4, 7, 10, ...).</li>
</ol>

<p>You must return the number of different types of status that <code>n</code> bulbs could have after you make <strong>exactly</strong> <code>presses</code> button presses.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 1, presses = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> Status can be:
- [off] by pressing button 1
- [on] by pressing button 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2, presses = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> Status can be:
- [off, off] by pressing button 1
- [on, off] by pressing button 2
- [off, on] by pressing button 3
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 3, presses = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> Status can be:
- [off, off, off] by pressing button 1
- [off, on, off] by pressing button 2
- [on, off, on] by pressing button 3
- [off, on, on] by pressing button 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= presses &lt;= 1000</code></li>
</ul>"""

    input_format = "An integer `n` and an integer `presses`."
    output_format = "An integer representing the number of unique statuses."
    
    constraints = [
        "1 <= n <= 1000",
        "0 <= presses <= 1000"
    ]
    
    explanation = """To determine the number of distinct bulb statuses:
1. **Mathematical Observation**:
   - The status of any bulb depends on its index modulo 6 (the least common multiple of numbers involved: all, 2, and 1+3k).
   - For `n > 6`, additional bulbs don't add new unique combinations of statuses; only the first few bulbs matter.
2. **Special Cases for `n` and `presses`**:
   - If `presses == 0`, there is only 1 status (all on).
   - If `n == 1`:
     - With 1+ presses, either on or off, so 2 statuses.
   - If `n == 2`:
     - With 1 press: 3 statuses (All Flip, Even Flip, Odd Flip). Note that Button 4 (1, 4, ...) is same as odd flip for n=2.
     - With 2+ presses: 4 statuses (All on, All Flip, Even Flip, Odd Flip).
   - If `n >= 3`:
     - With 1 press: 4 statuses (All, Even, Odd, 3k+1).
     - With 2 presses: 7 statuses.
     - With 3+ presses: 8 statuses.
3. **Logic Tables**:
   - The values can be derived or simulated for small `n` and `presses`.
4. **Complexity Analysis**:
   - Time: O(1) by using constant time conditional logic.
   - Space: O(1)."""
    
    answer = """class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0: return 1
        if n == 1: return 2
        if n == 2:
            return 3 if presses == 1 else 4
        if n >= 3:
            if presses == 1: return 4
            if presses == 2: return 7
            return 8"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef flipLights(n, presses):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Process n, presses\n    pass",
        "cpp": "#include <iostream>\nusing namespace std;\n\nint flipLights(int n, int presses) {\n    // User logic here\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int flipLights(int n, int presses) {\n        // User logic\n    }\n}",
        "javascript": "/**\n * @param {number} n\n * @param {number} presses\n * @return {number}\n */\nvar flipLights = function(n, presses) {\n    // User logic here\n};",
        "c": "int flipLights(int n, int presses) {\n    // User logic here\n}"
    }

    test_cases = [
        {"input": "1\\n1", "expected_output": "2", "is_sample": True},
        {"input": "2\\n1", "expected_output": "3", "is_sample": True},
        {"input": "3\\n1", "expected_output": "4", "is_sample": True},
        {"input": "1\\n0", "expected_output": "1", "is_sample": False},
        {"input": "2\\n2", "expected_output": "4", "is_sample": False},
        {"input": "4\\n1", "expected_output": "4", "is_sample": False},
        {"input": "1000\\n3", "expected_output": "8", "is_sample": False},
        # Stress cases
        {"input": "1000\\n1000", "expected_output": "8", "is_sample": False},
        {"input": "3\\n1000", "expected_output": "8", "is_sample": False},
        {"input": "2\\n1000", "expected_output": "4", "is_sample": False}
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
        "topics": ["Math", "Bit Manipulation", "Simulation"],
        "companyIndex": 0
    }

    output_path = "601-800/672_Bulb_Switcher_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
