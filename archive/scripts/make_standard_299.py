import json
import collections
import os

def generate_json():
    problem_id = 299
    title = "Bulls and Cows"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>299. Bulls and Cows</h3>
<p>You are playing the <strong>Bulls and Cows</strong> game with your friend.</p>

<p>You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:</p>

<ul>
	<li>The number of "bulls", which are digits in the guess that are in the correct position.</li>
	<li>The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.</li>
</ul>

<p>Given the secret number <code>secret</code> and your friend's guess <code>guess</code>, return <em>the hint for your friend's guess</em>.</p>

<p>The hint should be formatted as <code>"xAyB"</code>, where <code>x</code> is the number of bulls and <code>y</code> is the number of cows. Note that both <code>secret</code> and <code>guess</code> may contain duplicate digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> secret = "1807", guess = "7810"
<strong>Output:</strong> "1A3B"
<strong>Explanation:</strong> Bulls are connected with a '|', while cows are underlined:
"1807"
  |
"<u>7</u>8<u>10</u>"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> secret = "1123", guess = "0111"
<strong>Output:</strong> "1A1B"
<strong>Explanation:</strong> Bulls are connected with a '|', while cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= secret.length, guess.length &lt;= 1000</code></li>
	<li><code>secret.length == guess.length</code></li>
	<li><code>secret</code> and <code>guess</code> consist of digits only.</li>
</ul>"""

    input_format = "Two strings: `secret` and `guess`."
    output_format = "A string in the format 'xAyB'."
    
    constraints = [
        "1 <= secret.length, guess.length <= 1000",
        "secret.length == guess.length",
        "Both consist of only digits."
    ]
    
    explanation = """To calculate the number of Bulls and Cows:
1. **Pass 1: Count Bulls**: Iterate through both strings. If `secret[i] == guess[i]`, increment `bulls`.
2. **Handle Cows**:
   - For positions that are NOT bulls, record the frequency of digits in both strings.
   - Use two arrays (or hash maps) of size 10 to store counts of digits 0-9 for the remaining parts of `secret` and `guess`.
3. **Pass 2: Sum Minimums**: For each digit (0-9), the number of cows contributed by that digit is `min(count_secret[digit], count_guess[digit])`. Sum these minimums to get the total `cows`.
4. **Result**: Format the result as `f"{bulls}A{cows}B"`.
5. **Complexity Analysis**:
   - Time: O(N) where N is the length of the secret string.
   - Space: O(1) as we only use two arrays of fixed size (10)."""
    
    answer = """class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        rem_secret = [0] * 10
        rem_guess = [0] * 10
        
        # 1. First pass to count bulls and store remaining digit frequencies
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                rem_secret[int(secret[i])] += 1
                rem_guess[int(guess[i])] += 1
        
        # 2. Second pass to count cows (minimum overlap of frequencies)
        cows = 0
        for i in range(10):
            cows += min(rem_secret[i], rem_guess[i])
            
        return f"{bulls}A{cows}B\""""

    boilerplate = {
        "python": "import sys\n\ndef getHint(secret: str, guess: str) -> str:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        secret = input_data[0].strip()\n        guess = input_data[1].strip()\n        print(getHint(secret, guess))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nstring getHint(string secret, string guess) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    string secret, guess;\n    cin >> secret >> guess;\n    cout << getHint(secret, guess) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public String getHint(String secret, String guess) {\n        // User logic here\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String secret = sc.next();\n        String guess = sc.next();\n        System.out.println(new Solution().getHint(secret, guess));\n    }\n}",
        "javascript": "const fs = require('fs');\nconst parts = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nconst secret = parts[0];\nconst guess = parts[1];\n\nfunction getHint(secret, guess) {\n    // User logic here\n    return \"\";\n}\n\nconsole.log(getHint(secret, guess));",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nchar* getHint(char* secret, char* guess) {\n    // User logic here\n    return (char*)\"\";\n}\n\nint main() {\n    char secret[1005], guess[1005];\n    scanf(\"%s %s\", secret, guess);\n    char* res = getHint(secret, guess);\n    printf(\"%s\\n\", res);\n    return 0;\n}"
    }

    test_cases = [
        {"input": '"1807"\\n"7810"', "expected_output": '"1A3B"', "is_sample": True},
        {"input": '"1123"\\n"0111"', "expected_output": '"1A1B"', "is_sample": True},
        {"input": '"1"\\n"0"', "expected_output": '"0A0B"', "is_sample": False},
        {"input": '"1"\\n"1"', "expected_output": '"1A0B"', "is_sample": False},
        {"input": '"1111"\\n"1111"', "expected_output": '"4A0B"', "is_sample": False},
        {"input": '"1234"\\n"4321"', "expected_output": '"0A4B"', "is_sample": False},
        {"input": '"1122"\\n"2211"', "expected_output": '"0A4B"', "is_sample": False},
        # Stress cases
        {"input": '"0"*1000\\n"0"*1000', "expected_output": '"1000A0B"', "is_sample": False},
        {"input": '"0"*1000\\n"1"*1000', "expected_output": '"0A0B"', "is_sample": False},
        {"input": '"'.join(str(i%10) for i in range(1000)) + '"\\n"' + '"'.join(str((i+1)%10) for i in range(1000)) + '"', "expected_output": "...", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Counting"],
        "companyIndex": 0
    }

    output_path = "201-400/299_Bulls_and_Cows.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
