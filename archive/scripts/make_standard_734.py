import json
import os

def generate_json():
    problem_id = 734
    title = "Sentence Similarity"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>734. Sentence Similarity</h3>
<p>We can represent a sentence as an array of words, for example, the sentence <code>"I am happy with leetcode"</code> can be represented as <code>["I","am","happy","with","leetcode"]</code>.</p>
<p>Given two sentences <code>sentence1</code> and <code>sentence2</code> each represented as a string array and given an array of string pairs <code>similarPairs</code> where <code>similarPairs[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates that the two words <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code> are similar.</p>
<p>Return <em><code>true</code> if <code>sentence1</code> and <code>sentence2</code> are similar, or <code>false</code> if they are not similar.</em></p>
<p>Two sentences are similar if:</p>
<ul>
	<li>They have <strong>the same length</strong> (i.e., the same number of words).</li>
	<li><code>sentence1[i]</code> and <code>sentence2[i]</code> are similar.</li>
</ul>
<p>Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words <code>a</code> and <code>b</code> are similar, and the words <code>b</code> and <code>c</code> are similar, <code>a</code> and <code>c</code> are <strong>not necessarily</strong> similar.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The two sentences have the same length and each word i of sentence1 is similar to the corresponding word in sentence2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
<strong>Output:</strong> true
<strong>Explanation:</strong> A word is always similar to itself.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]
<strong>Output:</strong> false
<strong>Explanation:</strong> The sentences have different lengths.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 <= sentence1.length, sentence2.length <= 1000</code></li>
	<li><code>1 <= sentence1[i].length, sentence2[i].length <= 20</code></li>
	<li><code>sentence1[i]</code> and <code>sentence2[i]</code> consist of lower-case and upper-case English letters.</li>
	<li><code>0 <= similarPairs.length <= 1000</code></li>
	<li><code>similarPairs[i].length == 2</code></li>
	<li><code>1 <= u<sub>i</sub>.length, v<sub>i</sub>.length <= 20</code></li>
	<li><code>u<sub>i</sub></code> and <code>v<sub>i</sub></code> consist of lower-case and upper-case English letters.</li>
	<li>All the pairs <code>(u<sub>i</sub>, v<sub>i</sub>)</code> are <strong>distinct</strong>.</li>
</ul>"""

    input_format = "Two string lists sentence1 and sentence2, and a 2D string list similarPairs."
    output_format = "Boolean true or false."
    
    constraints = ["1 <= s1.length", "s2.length <= 1000", "0 <= similarPairs.length <= 1000", "Similarity is NOT transitive"]
    
    explanation = """EASY problem on ."""
    
    answer = """def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False
    
    similar_set = set()
    for u, v in similarPairs:
        similar_set.add((u, v))
        similar_set.add((v, u))
        
    for w1, w2 in zip(sentence1, sentence2):
        if w1 != w2 and (w1, w2) not in similar_set:
            return False
    return True"""

    boilerplate = {
        "python": "import sys\n\ndef areSentencesSimilar(sentence1, sentence2, similarPairs):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    sentence1 = input_data[0].strip() if len(input_data) > 0 else \"\"\n    sentence2 = input_data[1].strip() if len(input_data) > 1 else \"\"\n    similarPairs = input_data[2].strip() if len(input_data) > 2 else \"\"\n    print(areSentencesSimilar(sentence1, sentence2, similarPairs))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint areSentencesSimilar(string sentence1, string sentence2, string similarPairs) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string sentence1; cin >> sentence1;\n    string sentence2; cin >> sentence2;\n    string similarPairs; cin >> similarPairs;\n    cout << areSentencesSimilar(sentence1, sentence2, similarPairs) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": '["great","acting","skills"]\\n["fine","drama","talent"]\\n[["great","fine"],["drama","acting"],["skills","talent"]]', "expected_output": "true", "is_sample": True},
        {"input": '["great"]\\n["great"]\\n[]', "expected_output": "true", "is_sample": True},
        {"input": '["great"]\\n["doubleplus","good"]\\n[["great","doubleplus"]]', "expected_output": "false", "is_sample": True},
        {"input": '["I","am","happy"]\\n["I","am","sad"]\\n[["happy","joyful"],["sad","unhappy"]]', "expected_output": "false", "is_sample": False},
        {"input": '["a","b"]\\n["b","a"]\\n[["a","b"]]', "expected_output": "true", "is_sample": False},
        {"input": '["abc","def"]\\n["abc","def"]\\n[]', "expected_output": "true", "is_sample": False},
        {"input": '["very","good"]\\n["too","well"]\\n[["very","too"],["good","well"]]', "expected_output": "true", "is_sample": False},
        {"input": '["A","B"]\\n["a","b"]\\n[["A","a"],["B","b"]]', "expected_output": "true", "is_sample": False},
        {"input": '["hot","cold"]\\n["cold","hot"]\\n[["hot","cold"]]', "expected_output": "true", "is_sample": False},
        {"input": '["x"]\\n["y"]\\n[["z","w"]]', "expected_output": "false", "is_sample": False}]

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

    output_path = "1-1000/734_Sentence_Similarity.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
