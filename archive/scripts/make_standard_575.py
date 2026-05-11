import json
import os

def generate_json():
    problem_id = 575
    title = "Distribute Candies"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>575. Distribute Candies</h3>
<p>Alice has <code>n</code> candies, where the <code>i<sup>th</sup></code> candy is of type <code>candyType[i]</code>. Alice noticed that she has <code>n</code> candies and <code>n</code> is always even. She wants to distribute these <code>n</code> candies equally between herself and her brother.</p>

<p>Alice wants to maximize the number of different types of candies she can eat while only eating <code>n / 2</code> of them.</p>

<p>Given the integer array <code>candyType</code> of length <code>n</code>, return <em>the <b>maximum</b> number of different types of candies she can eat if she only eats </em><code>n / 2</code><em> of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> candyType = [1,1,2,2,3,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> candyType = [1,1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still only eats 2 different types.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> candyType = [6,6,6,6]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == candyType.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>n</code> is even.</li>
	<li><code>-10<sup>5</sup> &lt;= candyType[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers for candyType."
    output_format = "A single integer representing the maximum number of different types Alice can eat."
    
    constraints = [
        "2 <= n <= 10^4 (n is even)",
        "-10^5 <= candyType[i] <= 10^5",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To determine the maximum number of different types of candies Alice can eat:
1. **The Constraints**:
   - Alice can eat exactly $n / 2$ candies.
   - She wants to eat as many *different* types as possible.
2. **Strategy**:
   - Count the total number of unique types in the array using a Set (let this be $T$).
   - The maximum number of types she can eat is limited by two values:
     - The total number of unique types available: $T$.
     - The capacity she is allowed to eat: $n / 2$.
   - Thus, the result is $\min(T, n / 2)$.
3. **Complexity**:
   - Time Complexity: O(N) to iterate through the array once and build the set.
   - Space Complexity: O(N) to store the set of unique types."""
    
    answer = """def distributeCandies(candyType: list[int]) -> int:
    unique_types = len(set(candyType))
    can_eat = len(candyType) // 2
    return min(unique_types, can_eat)"""

    boilerplate = {
        "python": "import sys\n\ndef distributeCandies(candyType):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        candyType = list(map(int, line.split()))\n        print(distributeCandies(candyType))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_set>\n#include <algorithm>\n\nusing namespace std;\n\nint distributeCandies(vector<int>& candyType) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int distributeCandies(int[] candyType) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function distributeCandies(candyType) {\n    // User logic\n}",
        "c": "int distributeCandies(int* candyType, int candyTypeSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 1 2 2 3 3", "expected_output": "3", "is_sample": True},
        {"input": "1 1 2 3", "expected_output": "2", "is_sample": True},
        {"input": "6 6 6 6", "expected_output": "1", "is_sample": True},
        {"input": "1 2 3 4 5 6", "expected_output": "3", "is_sample": False},
        {"input": "1 1 1 2 2 2", "expected_output": "2", "is_sample": False},
        {"input": "-100 100", "expected_output": "1", "is_sample": False},
        {"input": "10 20 10 20 10 20", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(10000)]), "expected_output": "5000", "is_sample": False},
        {"input": " ".join(["1"] * 10000), "expected_output": "1", "is_sample": False},
        {"input": " ".join([str(i//2) for i in range(10000)]), "expected_output": "5000", "is_sample": False}
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "401-600/575_Distribute_Candies.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
