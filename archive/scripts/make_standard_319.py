import json
import os

def generate_json():
    problem_id = 319
    title = "Bulb Switcher"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>319. Bulb Switcher</h3>
<p>There are <code>n</code> bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.</p>

<p>On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the <code>i<sup>th</sup></code> round, you toggle every <code>i<sup>th</sup></code> bulb. For the <code>n<sup>th</sup></code> round, you only toggle the last bulb.</p>

<p>Return <em>the number of bulbs that are on after <code>n</code> rounds</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg" style="width: 421px; height: 321px;" />
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "An integer `n` representing the number of bulbs."
    output_format = "An integer representing the count of bulbs that remain on."
    
    constraints = [
        "0 <= n <= 10^9"
    ]
    
    explanation = """The problem can be solved by understanding the toggling logic:
1. **Factor Analysis**: A bulb at position `i` is toggled in round `d` if and only if `d` is a divisor of `i`.
2. **On/Off State**: A bulb remains **on** if it is toggled an **odd** number of times. A bulb remains **off** if it is toggled an **even** number of times.
3. **Divisor Pairs**: Most numbers have an even number of divisors because divisors come in pairs $(a, b)$ such that $a \times b = i$. For example, divisors of 12 are (1, 12), (2, 6), and (3, 4).
4. **Perfect Squares**: A number has an odd number of divisors if and only if it is a **perfect square** (e.g., 1, 4, 9, 16...). In this case, one divisor pair consists of the same number $(a, a)$, so the total count is odd.
5. **Goal**: The problem reduces to counting how many perfect squares are less than or equal to `n`.
6. **Result**: The number of perfect squares up to `n` is simply the floor of the square root of `n`: $\lfloor \sqrt{n} \rfloor$.

### Complexity Analysis:
- **Time Complexity**: $O(1)$ or $O(\log n)$ depending on the implementation of `sqrt`.
- **Space Complexity**: $O(1)$."""
    
    answer = """import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # A bulb remains on if and only if it is toggled an odd number of times.
        # This happens if the bulb's position is a perfect square.
        # So we just need to find the number of perfect squares <= n.
        return int(math.sqrt(n))"""

    boilerplate = {
        "python": "import sys\nimport math\n\ndef bulbSwitch(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    n = int(sys.stdin.read().strip())\n    print(bulbSwitch(n))",
        "cpp": "#include <iostream>\n#include <cmath>\nusing namespace std;\n\nint bulbSwitch(int n) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int n;\n    cin >> n;\n    cout << bulbSwitch(n) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int bulbSwitch(int n) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        System.out.println(new Solution().bulbSwitch(n));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction bulbSwitch(n) {\n    // User logic here\n    return 0;\n}\n\nconst n = parseInt(fs.readFileSync(0, 'utf-8').trim(), 10);\nconsole.log(bulbSwitch(n));",
        "c": "#include <stdio.h>\n\nint bulbSwitch(int n) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int n;\n    scanf(\"%d\", &n);\n    printf(\"%d\\n\", bulbSwitch(n));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3", "expected_output": "1", "is_sample": True},
        {"input": "0", "expected_output": "0", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "4", "expected_output": "2", "is_sample": False},
        {"input": "9", "expected_output": "3", "is_sample": False},
        {"input": "10", "expected_output": "3", "is_sample": False},
        {"input": "99", "expected_output": "9", "is_sample": False},
        # Stress cases
        {"input": "1000000000", "expected_output": "31622", "is_sample": False},
        {"input": "10000", "expected_output": "100", "is_sample": False},
        {"input": "2147483647", "expected_output": "46340", "is_sample": False}
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
        "topics": ["Math", "Brainteaser"],
        "companyIndex": 1
    }

    output_path = "301-500/319_Bulb_Switcher.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
