import json
import os

def generate_json():
    problem_id = 914
    title = "X of a Kind in a Deck of Cards"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>914. X of a Kind in a Deck of Cards</h3>
<p>You are given an integer array <code>deck</code> where <code>deck[i]</code> represents the number written on the <code>i</code><sup>th</sup> card.</p>

<p>Partition the cards into <b>one or more</b> groups such that:</p>

<ul>
	<li>Each group has <b>exactly</b> <code>X</code> cards, where <code>X &gt; 1</code>.</li>
	<li>All the cards in <b>one group</b> have the same integer written on them.</li>
</ul>

<p>Return <code>true</code> <em>if such a partition is possible, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> deck = [1,2,3,4,4,3,2,1]
<strong>Output:</strong> true
<strong>Explanation</strong>: Possible partition [1,1],[2,2],[3,3],[4,4] with X = 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> deck = [1,1,1,2,2,2,3,3]
<strong>Output:</strong> false
<strong>Explanation</strong>: No possible partition with X > 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= deck.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= deck[i] &lt; 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers (deck of cards)."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "1 <= n <= 10,000",
        "0 <= deck[i] < 10,000",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To determine if a valid partition of size X > 1 exists:
1. **The Core Logic (GCD)**:
   - For a partition into groups of size X to be possible, where all cards in a group are identical, every type of card must appear a number of times that is divisible by X.
   - This means X must be a common divisor of the frequency of every distinct card in the deck.
   - For such an X > 1 to exist, the Greatest Common Divisor (GCD) of all card frequencies must be greater than or equal to 2.
2. **Algorithm Steps**:
   - Count the frequency of each card using a hash map or frequency array.
   - Calculate the GCD of all these frequencies.
   - If the result is >= 2, return `true`; otherwise, return `false`.
3. **Complexity**:
   - Time Complexity: O(N) to count frequencies, plus O(D log V) to calculate the GCD (where D is the number of distinct cards and V is the maximum value in the deck). Max frequency is N.
   - Space Complexity: O(D) to store the frequencies."""
    
    answer = """import math
from functools import reduce
from collections import Counter

def hasGroupsSizeX(deck: list[int]) -> bool:
    counts = Counter(deck).values()
    # Calculate GCD of all counts
    g = reduce(math.gcd, counts)
    return g >= 2"""

    boilerplate = {
        "python": "import sys\nimport math\nfrom collections import Counter\nfrom functools import reduce\n\ndef hasGroupsSizeX(deck):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        deck = list(map(int, line.split()))\n        print('true' if hasGroupsSizeX(deck) else 'false')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <numeric>\n#include <unordered_map>\n\nusing namespace std;\n\nint gcd(int a, int b) {\n    while (b) {\n        a %= b;\n        swap(a, b);\n    }\n    return a;\n}\n\nbool hasGroupsSizeX(vector<int>& deck) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int gcd(int a, int b) {\n        return b == 0 ? a : gcd(b, a % b);\n    }\n    \n    public boolean hasGroupsSizeX(int[] deck) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function hasGroupsSizeX(deck) {\n    // User logic\n}",
        "c": "bool hasGroupsSizeX(int* deck, int deckSize) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4 4 3 2 1", "expected_output": "true", "is_sample": True},
        {"input": "1 1 1 2 2 2 3 3", "expected_output": "false", "is_sample": True},
        {"input": "1 1", "expected_output": "true", "is_sample": False},
        {"input": "1 1 2 2 2 2", "expected_output": "true", "is_sample": False}, # GCD(2, 4) = 2
        {"input": "1 1 1 2 2 2", "expected_output": "true", "is_sample": False},
        {"input": "1 1 2 2 3 3", "expected_output": "true", "is_sample": False},
        {"input": "1", "expected_output": "false", "is_sample": False},
        {"input": "1 1 1 1 1", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"] * 10000), "expected_output": "true", "is_sample": False},
        {"input": " ".join([str(i % 100) for i in range(10000)]), "expected_output": "true", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Math", "Counting", "Number Theory"],
        "companyIndex": 0
    }

    output_path = "801-1000/914_X_of_a_Kind_in_a_Deck_of_Cards.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
