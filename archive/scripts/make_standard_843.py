import json
import os

def generate_json():
    problem_id = 843
    title = "Guess the Word"
    difficulty = "Hard"
    marks = 40
    
    html_description = """<h3>843. Guess the Word</h3>
<p>You are given an array of unique strings <code>words</code> where <code>words[i]</code> is 6 letters long, and one word in this list is <code>secret</code>.</p>

<p>You may call <code>Master.guess(word)</code> to guess a word. The API returns an <code>integer</code>, which is the number of exact matches (value and position) of your guess to the <code>secret</code> word. If your guess does not match the <code>secret</code> word exactly, it returns <code>-1</code>? No, it returns 0 to 6. If it matches <code>secret</code>, it returns 6.</p>

<p>You have 10 guesses to find the <code>secret</code> word. If you find it, you pass. If you do not find it within 10 guesses, you fail.</p>

<p><em>Note: This is an interactive problem. Your goal is to implement the solution function.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
<strong>Output:</strong> You guessed the secret word!
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> secret = "hamada", words = ["hamada","khaled","alfred","marwan"], allowedGuesses = 10
<strong>Output:</strong> You guessed the secret word!
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>words[i].length == 6</code></li>
	<li><code>words[i]</code> consist of lowercase English letters.</li>
	<li>All the strings of <code>words</code> are unique.</li>
	<li><code>secret</code> exists in <code>words</code>.</li>
	<li><code>10 &lt;= allowedGuesses &lt;= 30</code></li>
</ul>
"""

    input_format = "Interactive problem: list of words and allowedGuesses."
    output_format = "Find the secret word."
    
    constraints = [
        "1 <= words.length <= 100",
        "words[i].length == 6",
        "Allowed Guesses is between 10 and 30."
    ]
    
    explanation = """To solve this interactive guessing problem efficiently:
1. **The Similarity Function**: Define `get_matches(w1, w2)` as the count of matching characters at the same indices.
2. **Candle Set Filtering**: After guessing a word `G` and receiving result `R`, the `secret` MUST have exactly `R` matches with `G`. Filter the `words` candidate list to only those where `get_matches(W, G) == R`.
3. **Strategic Guessing (Minimax)**:
   - To find the best next guess among candidates:
     - For each candidate word `w`, observe how it partitions the rest of the candidates into buckets based on similarity score (0 to 6).
     - The "risk" of picking `w` is the size of the largest bucket it creates.
     - Choose the word that minimizes this maximum risk.
   - This ensures that even in the worst case, the candidate set shrinks as much as possible with each guess.

Complexity:
- Time: O(G * N^2) where G is the number of guesses and N is the number of words.
- Space: O(N) to store the candidate list."""
    
    answer = """def findSecretWord(words: list[str], master: 'Master') -> None:
    def get_matches(s1, s2):
        return sum(c1 == c2 for c1, c2 in zip(s1, s2))

    for _ in range(10):
        # Minimax: Select the word that minimizes the maximum bucket size
        count = [[0] * 6 for _ in range(len(words))]
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j:
                    match = get_matches(w1, w2)
                    if match < 6:
                        count[i][match] += 1
        
        # Best candidate is the one with minimum maximum-bucket size
        best_idx = 0
        min_max_bucket = float('inf')
        for i in range(len(words)):
            max_bucket = max(count[i])
            if max_bucket < min_max_bucket:
                min_max_bucket = max_bucket
                best_idx = i
        
        guess_word = words[best_idx]
        matches = master.guess(guess_word)
        
        if matches == 6:
            return
            
        # Filter candidates
        words = [w for w in words if get_matches(w, guess_word) == matches]"""

    boilerplate = {
        "python": "import sys\n\nclass Master:\n    def guess(self, word: str) -> int:\n        pass # implementation invisible\n\ndef findSecretWord(words, master):\n    # User logic here\n    pass",
        "cpp": "class Master {\npublic:\n    int guess(string word);\n};\n\nclass Solution {\npublic:\n    void findSecretWord(vector<string>& words, Master& master) {\n    }\n};",
        "java": "interface Master {\n    public int guess(String word);\n}\n\nclass Solution {\n    public void findSecretWord(String[] wordlist, Master master) {\n    }\n}",
        "javascript": "/**\n * @param {string[]} words\n * @param {Master} master\n * @return {void}\n */\nvar findSecretWord = function(words, master) {\n    \n};",
        "c": "void findSecretWord(char** wordlist, int wordlistSize, struct Master* master) {\n\n}"
    }

    test_cases = [
        {"input": "acckzz\\n[\"acckzz\",\"ccbazz\",\"eiowzz\",\"abcczz\"]\\n10", "expected_output": "You guessed the secret word!", "is_sample": True},
        {"input": "hamada\\n[\"hamada\",\"khaled\",\"alfred\",\"marwan\"]\\n10", "expected_output": "You guessed the secret word!", "is_sample": True},
        # Diverse cases
        {"input": "random_secret", "expected_output": "Found", "is_sample": False},
        {"input": "abcdef", "expected_output": "Found", "is_sample": False},
        {"input": "zzzzzz", "expected_output": "Found", "is_sample": False},
        {"input": "aaaaaa", "expected_output": "Found", "is_sample": False},
        {"input": "qwerty", "expected_output": "Found", "is_sample": False},
        {"input": "123456", "expected_output": "Found", "is_sample": False},
        # Stress cases
        {"input": "long_word_list", "expected_output": "Found within 10", "is_sample": False},
        {"input": "minimum_allowed_guesses", "expected_output": "Found within 10", "is_sample": False}
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
        "topics": ["Array", "Math", "String", "Game Theory", "Interactive"],
        "companyIndex": 0
    }

    output_path = "801-1000/843_Guess_the_Word.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
