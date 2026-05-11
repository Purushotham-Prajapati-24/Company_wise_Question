import json
import os

def generate_json():
    problem_id = 292
    title = "Nim Game"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>292. Nim Game</h3>
<p>You are playing the following Nim Game with your friend:</p>

<ul>
	<li>Initially, there is a heap of stones on the table.</li>
	<li>You and your friend will alternate taking turns, and <strong>you go first</strong>.</li>
	<li>On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.</li>
	<li>The one who removes the last stone is the winner.</li>
</ul>

<p>Given <code>n</code>, the number of stones in the heap, return <code>true</code><em> if you can win the game assuming both you and your friend play optimally, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> false
<strong>Explanation:</strong> These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last one. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last one. Your friend wins.
3. You remove 3 stones. Your friend removes 1 stone, including the last one. Your friend wins.
In all outcomes, your friend wins.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "An integer `n` representing the number of stones."
    output_format = "A boolean value: true or false."
    
    constraints = [
        "1 <= n <= 2^31 - 1"
    ]
    
    explanation = """To determine if you can win the Nim Game:
1. **Analyze the patterns**:
   - if `n = 1, 2, 3`: You can take all stones and win. (Returns True)
   - if `n = 4`: No matter how many you take (1, 2, or 3), there will be 1 to 3 stones left for your friend. They take them all and win. (Returns False)
   - if `n = 5, 6, 7`: You can take 1, 2, or 3 stones to leave exactly 4 stones for your friend. As established, the player who faces 4 stones loses. (Returns True)
   - if `n = 8`: No matter how many you take (1, 2, or 3), you leave 5, 6, or 7 stones for your friend. They can then leave 4 stones for you. (Returns False)
2. **Mathematical Conclusion**: You will lose if and only if the number of stones `n` is a multiple of 4. Otherwise, you can always make a move that leaves your opponent with a multiple of 4.
3. **Complexity Analysis**:
   - Time: O(1) - constant time check.
   - Space: O(1) - no extra space used."""
    
    answer = """class Solution:
    def canWinNim(self, n: int) -> bool:
        # You lose if n is a multiple of 4
        return n % 4 != 0"""

    boilerplate = {
        "python": "import sys\n\ndef canWinNim(n: int) -> bool:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        n = int(input_data)\n        print('true' if canWinNim(n) else 'false')",
        "cpp": "#include <iostream>\nusing namespace std;\n\nbool canWinNim(int n) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    int n;\n    cin >> n;\n    cout << (canWinNim(n) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean canWinNim(int n) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        System.out.println(new Solution().canWinNim(n) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction canWinNim(n) {\n    // User logic here\n    return false;\n}\n\nconst n = parseInt(fs.readFileSync(0, 'utf-8').trim());\nconsole.log(canWinNim(n) ? 'true' : 'false');",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n\nbool canWinNim(int n) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    int n;\n    scanf(\"%d\", &n);\n    printf(\"%s\\n\", canWinNim(n) ? \"true\" : \"false\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "4", "expected_output": "false", "is_sample": True},
        {"input": "1", "expected_output": "true", "is_sample": True},
        {"input": "2", "expected_output": "true", "is_sample": True},
        {"input": "3", "expected_output": "true", "is_sample": False},
        {"input": "5", "expected_output": "true", "is_sample": False},
        {"input": "8", "expected_output": "false", "is_sample": False},
        {"input": "12", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": "2147483647", "expected_output": "true", "is_sample": False},
        {"input": "2147483644", "expected_output": "false", "is_sample": False},
        {"input": "1000000", "expected_output": "false", "is_sample": False}
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
        "topics": ["Math", "Brainteaser", "Game Theory"],
        "companyIndex": 0
    }

    output_path = "201-400/292_Nim_Game.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
