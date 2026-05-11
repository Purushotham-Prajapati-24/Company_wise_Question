import json
import os

def generate_json():
    problem_id = 365
    title = "Water and Jug Problem"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>365. Water and Jug Problem</h3>
<p>You are given two jugs with capacities <code>jug1Capacity</code> and <code>jug2Capacity</code> liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly <code>targetCapacity</code> liters using these two jugs.</p>

<p>If <code>targetCapacity</code> liters of water are measurable, you must have <code>targetCapacity</code> liters of water contained <strong>within one or both buckets</strong> by the end.</p>

<p>Operations allowed:</p>

<ul>
	<li>Fill any of the jugs completely with water.</li>
	<li>Empty any of the jugs.</li>
	<li>Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> The famous Die Hard example.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= jug1Capacity, jug2Capacity, targetCapacity &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "Three integers: jug1Capacity, jug2Capacity, and targetCapacity."
    output_format = "A boolean value: true or false."
    
    constraints = ["1 <= jug1Capacity", "jug2Capacity", "targetCapacity <= 10^6"]
    
    explanation = """To determine if a `targetCapacity` is measurable using two jugs, we use the **Bézout's identity (GCD theory)**.

### Key Insights:
1. **Total Capacity**: You cannot measure more than the sum of both jugs.
2. **Measurability**: Any amount $z$ that can be measured using jugs $x$ and $y$ must be a multiple of the **Greatest Common Divisor (GCD)** of $x$ and $y$. This is because any pouring/emptying/filling operation effectively changes the total amount by a linear combination of $x$ and $y$ (i.e., $ax + by$).
3. **Bézout's Lemma**: For integers $x$ and $y$, there exist $a, b$ such that $ax + by = \gcd(x, y)$. This implies we can reach any multiple of $\gcd(x, y)$ that is less than or equal to $x + y$.

### Steps:
1. Check if `target` > `x + y`. If so, return `False`.
2. Check if `target` is 0. If so, return `True`.
3. Calculate `g = gcd(x, y)`.
4. Return `target % g == 0`.

### Complexity:
- **Time Complexity**: $O(\log(\min(x, y)))$ for the GCD calculation.
- **Space Complexity**: $O(1)$."""
    
    answer = """import math

def canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):
    if targetCapacity > jug1Capacity + jug2Capacity:
        return False
    if targetCapacity == 0:
        return True
    return targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0"""

    boilerplate = {
        "python": (
            "import sys\n"
            "import math\n\n"
            "def canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):\n"
            "    # User logic here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    parts = sys.stdin.read().strip().split()\n"
            "    if len(parts) >= 3:\n"
            "        j1, j2, t = int(parts[0]), int(parts[1]), int(parts[2])\n"
            "        print('true' if canMeasureWater(j1, j2, t) else 'false')\n"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <numeric>\n"
            "using namespace std;\n\n"
            "bool canMeasureWater(int j1, int j2, int target) {\n"
            "    // User logic here\n"
            "    return false;\n"
            "}\n\n"
            "int main() {\n"
            "    int j1, j2, t;\n"
            "    if (cin >> j1 >> j2 >> t) {\n"
            "        cout << (canMeasureWater(j1, j2, t) ? \"true\" : \"false\") << endl;\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        ),
        "java": (
            "import java.util.*;\n\n"
            "public class Main {\n"
            "    public static boolean canMeasureWater(int j1, int j2, int target) {\n"
            "        // User logic here\n"
            "        return false;\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextInt()) {\n"
            "            int j1 = sc.nextInt();\n"
            "            int j2 = sc.nextInt();\n"
            "            int t = sc.nextInt();\n"
            "            System.out.println(canMeasureWater(j1, j2, t) ? \"true\" : \"false\");\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "var canMeasureWater = function(jug1Capacity, jug2Capacity, targetCapacity) {\n"
            "    // User logic here\n"
            "    return false;\n"
            "};\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').trim();\n"
            "    if (!input) return;\n"
            "    const parts = input.split(/\\s+/);\n"
            "    if (parts.length >= 3) {\n"
            "        const j1 = parseInt(parts[0], 10);\n"
            "        const j2 = parseInt(parts[1], 10);\n"
            "        const t = parseInt(parts[2], 10);\n"
            "        console.log(canMeasureWater(j1, j2, t) ? 'true' : 'false');\n"
            "    }\n"
            "}\n"
            "main();\n"
        ),
        "c": (
            "#include <stdio.h>\n\n"
            "int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }\n\n"
            "int canMeasureWater(int j1, int j2, int target) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "}\n\n"
            "int main() {\n"
            "    int j1, j2, t;\n"
            "    if (scanf(\"%d %d %d\", &j1, &j2, &t) == 3) {\n"
            "        printf(\"%s\\n\", canMeasureWater(j1, j2, t) ? \"true\" : \"false\");\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        )
    }

    test_cases = [
        {"input": "3 5 4", "expected_output": "true", "is_sample": True},
        {"input": "2 6 5", "expected_output": "false", "is_sample": True},
        {"input": "1 2 3", "expected_output": "true", "is_sample": True},
        {"input": "34 5 6", "expected_output": "true", "is_sample": False},
        {"input": "10 20 5", "expected_output": "false", "is_sample": False},
        {"input": "1 1 0", "expected_output": "true", "is_sample": False},
        {"input": "1000000 1000000 1000000", "expected_output": "true", "is_sample": False},
        {"input": "1000000 2 999999", "expected_output": "false", "is_sample": False},
        {"input": "999999 1 1000000", "expected_output": "true", "is_sample": False},
        {"input": "1000000 999999 1", "expected_output": "true", "is_sample": False},
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
        "topics": ["Math", "Depth-First Search", "Breadth-First Search"],
        "companyIndex": 0
    }

    output_path = "301-500/365_Water_and_Jug_Problem.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
