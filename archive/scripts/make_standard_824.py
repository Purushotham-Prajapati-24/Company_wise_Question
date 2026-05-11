import json
import os

def generate_json():
    problem_id = 824
    title = "Goat Latin"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>824. Goat Latin</h3>
<p>You are given a string <code>sentence</code> that consists of words separated by spaces. Each word consists of lowercase and uppercase letters only.</p>

<p>We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin). The rules of Goat Latin are as follows:</p>

<ul>
	<li>If a word begins with a vowel (<code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, or <code>'u'</code>), append <code>"ma"</code> to the end of the word.
	<ul>
		<li>For example, the word <code>"apple"</code> becomes <code>"applema"</code>.</li>
	</ul>
	</li>
	<li>If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then append <code>"ma"</code>.
	<ul>
		<li>For example, the word <code>"goat"</code> becomes <code>"oatgma"</code>.</li>
	</ul>
	</li>
	<li>Add one letter <code>'a'</code> to the end of each word per its 1-indexed position in the sentence.
	<ul>
		<li>For example, the first word gets <code>"a"</code> added to the end, the second word gets <code>"aa"</code> added to the end, and so on.</li>
	</ul>
	</li>
</ul>

<p>Return <em>the final sentence representing the conversion from sentence to Goat Latin</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> sentence = "I speak Goat Latin"
<strong>Output:</strong> "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> sentence = "The quick brown fox jumped over the lazy dog"
<strong>Output:</strong> "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 150</code></li>
	<li><code>sentence</code> consists of English letters and spaces.</li>
	<li><code>sentence</code> has no leading or trailing spaces.</li>
	<li>All the words in <code>sentence</code> are separated by a single space.</li>
</ul>"""

    input_format = "A single line containing the string sentence."
    output_format = "A single line containing the converted Goat Latin sentence."
    
    constraints = [
        "1 <= sentence.length <= 150",
        "Result length can grow significantly due to 'a's.",
        "O(N + M^2) time complexity.",
        "O(N + M^2) space complexity."
    ]
    
    explanation = """To convert a sentence to Goat Latin:
1. **Split the Sentence**:
   - Split the input string into individual words using spaces.
2. **Process Each Word**:
   - For each word at 1-indexed position `i`:
     - Check the first character (case-insensitive) for vowel vs consonant.
     - Rule 1 (Vowel): Append `"ma"`.
     - Rule 2 (Consonant): Move first char to end and append `"ma"`.
     - Rule 3 (Index): Append `i` instances of `'a'`.
3. **Join and Return**:
   - Join the processed words back with a single space.
4. **Complexity**:
   - Time Complexity: O(N + M^2) where N is the length of the sentence and M is the number of words (due to repeated 'a' appending).
   - Space Complexity: O(N + M^2) to store the result."""
    
    answer = """def toGoatLatin(sentence: str) -> str:
    vowels = set("aeiouAEIOU")
    words = sentence.split()
    res = []
    
    for i, word in enumerate(words):
        if word[0] in vowels:
            new_word = word + "ma"
        else:
            new_word = word[1:] + word[0] + "ma"
        
        new_word += "a" * (i + 1)
        res.append(new_word)
        
    return " ".join(res)"""

    boilerplate = {
        "python": "import sys\n\ndef toGoatLatin(sentence):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(toGoatLatin(line))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <sstream>\n#include <unordered_set>\n\nusing namespace std;\n\nstring toGoatLatin(string sentence) {\n    // User logic\n    return \"\";\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public String toGoatLatin(String sentence) {\n        // User logic\n        return \"\";\n    }\n}",
        "javascript": "function toGoatLatin(sentence) {\n    // User logic\n}",
        "c": "char* toGoatLatin(char* sentence) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "I speak Goat Latin", "expected_output": "Imaa peaksmaaa oatGmaaaa atinLmaaaaa", "is_sample": True},
        {"input": "The quick brown fox jumped over the lazy dog", "expected_output": "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa", "is_sample": True},
        {"input": "Apple", "expected_output": "Applemaa", "is_sample": True},
        {"input": "Banana", "expected_output": "ananaBmaa", "is_sample": False},
        {"input": "a", "expected_output": "amaa", "is_sample": False},
        {"input": "b", "expected_output": "bmaa", "is_sample": False},
        {"input": "Each word here", "expected_output": "Eachmaa ordwmaaa erehmaaaa", "is_sample": False},
        # Stress cases (within length 150)
        {"input": "a b c d e f g h i j k l m n o p q r s t u v w x y z", "expected_output": "amaa bmaaa cmaaaa dmaaaaa emaaaaaa fmaaaaaaa gmaaaaaaaa hmaaaaaaaaa imaaaaaaaaaa jmaaaaaaaaaaa kmaaaaaaaaaaaa lmaaaaaaaaaaaaa mmaaaaaaaaaaaaaa nmaaaaaaaaaaaaaaa omaaaaaaaaaaaaaaaa pmaaaaaaaaaaaaaaaaa qmaaaaaaaaaaaaaaaaaa rmaaaaaaaaaaaaaaaaaaa smaaaaaaaaaaaaaaaaaaaa umaaaaaaaaaaaaaaaaaaaaa vmaaaaaaaaaaaaaaaaaaaaaa wmaaaaaaaaaaaaaaaaaaaaaaa xmaaaaaaaaaaaaaaaaaaaaaaaa ymaaaaaaaaaaaaaaaaaaaaaaaaa zmaaaaaaaaaaaaaaaaaaaaaaaaaa", "is_sample": False},
        {"input": "A " * 74 + "A", "expected_output": " ".join(["Amaa" + "a"*i for i in range(75)]), "is_sample": False},
        {"input": "b " * 74 + "b", "expected_output": " ".join(["bmaa" + "a"*i for i in range(75)]), "is_sample": False}
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
        "topics": ["String"],
        "companyIndex": 0
    }

    output_path = "801-1000/824_Goat_Latin.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
