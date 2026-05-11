import json
import os

def generate_json():
    problem_id = 648
    title = "Replace Words"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>648. Replace Words</h3>
<p>In English, we have a concept called <b>root</b>, which can be followed by some other word to form another longer word - let's call this word <b>derivative</b>. For example, when the root <code>"help"</code> is followed by the word <code>"ful"</code>, we can form a new word <code>"helpful"</code>.</p>

<p>Given a <code>dictionary</code> consisting of many <b>roots</b> and a <code>sentence</code> consisting of words separated by spaces, replace all the derivatives in the sentence with the <b>root</b> forming it. If a derivative can be replaced by more than one <b>root</b>, replace it with the <b>root</b> that has the <b>shortest length</b>.</p>

<p>Return <em>the sentence after the replacement</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
<strong>Output:</strong> "the cat was rat by the bat"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
<strong>Output:</strong> "a a b c"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= dictionary.length &lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 100</code></li>
	<li><code>dictionary[i]</code> consists of only lower-case English letters.</li>
	<li><code>1 &lt;= sentence.length &lt;= 10<sup>6</sup></code></li>
	<li><code>sentence</code> consists of only lower-case English letters and spaces.</li>
	<li>The number of words in <code>sentence</code> is in the range <code>[1, 1000]</code>.</li>
	<li>The length of each word in <code>sentence</code> is in the range <code>[1, 1000]</code>.</li>
	<li>Every two consecutive words in <code>sentence</code> will be separated by exactly one space.</li>
	<li><code>sentence</code> does not have leading or trailing spaces.</li>
</ul>
"""

    input_format = "Two lines: first, string array for dictionary; second, string for sentence."
    output_format = "A string after replacement."
    
    constraints = [
        "1 <= dictionary.length <= 1000",
        "1 <= sentence.length <= 10^6",
        "Only lowercase lowercase letters and spaces.",
        "Shortest root replacement."
    ]
    
    explanation = """To replace words with the shortest root:
1. Use a Trie (Prefix Tree).
2. Insert all roots from the dictionary into the Trie.
3. For each word in the sentence:
   - Traverse the Trie character by character.
   - If a root is encountered (indicated by an specialized flag in the node), replace the word with this root and move to the next word.
   - If no root is found by the end of the word or we can't traverse further, keep the word as it is.
4. Join the resulting words with spaces and return."""
    
    answer = """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_root = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_root = True
    
    def find_shortest_root(self, word):
        node = self.root
        current_root = ""
        for char in word:
            if char not in node.children:
                return word
            node = node.children[char]
            current_root += char
            if node.is_root:
                return current_root
        return word

def replaceWords(dictionary, sentence):
    trie = Trie()
    for root in dictionary:
        trie.insert(root)
    
    words = sentence.split()
    res = [trie.find_shortest_root(word) for word in words]
    return " ".join(res)"""

    boilerplate = {
        "python": "import sys\\n\\ndef replaceWords(dictionary, sentence):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    # Custom input handler\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <string>\\n#include <sstream>\\n\\nusing namespace std;\\n\\nclass Solution { public: string replaceWords(vector<string>& dictionary, string sentence) { return \"\"; } };",
        "java": "class Solution { public String replaceWords(List<String> dictionary, String sentence) { return \"\"; } }",
        "javascript": "const fs = require('fs');",
        "c": "char* replaceWords(char** dictionary, int dictionarySize, char* sentence) { }"
    }

    test_cases = [
        {"input": "['cat','bat','rat']\\n'the cattle was rattled by the battery'", "expected_output": "'the cat was rat by the bat'", "is_sample": True},
        {"input": "['a','b','c']\\n'aadsfasf absbs bbab cadsfafs'", "expected_output": "'a a b c'", "is_sample": True},
        {"input": "['a', 'aa', 'aaa', 'aaaa']\\n'a aa aaa aaaa'", "expected_output": "'a a a a'", "is_sample": False},
        {"input": "['cattle', 'bat', 'rat']\\n'the cattle was rattled by the battery'", "expected_output": "'the cattle was rat by the bat'", "is_sample": False},
        {"input": "['any']\\n'nothing matches this sentence'", "expected_output": "'nothing matches this sentence'", "is_sample": False},
        {"input": "['p', 'pr', 'pre']\\n'prefix preferred'", "expected_output": "'p p'", "is_sample": False},
        {"input": "['word']\\n'word'", "expected_output": "'word'", "is_sample": False},
        {"input": "['a']*1000\\n" + "' '.join(['a'*1000]*1000)", "expected_output": "' '.join(['a']*1000)", "is_sample": False},
        {"input": str(["s"+str(i) for i in range(1000)]) + "\\n'sentence contains many words'", "expected_output": "'sentence contains many words'", "is_sample": False},
        {"input": "['longroot']*1000\\n'word1 word2 word3'", "expected_output": "'word1 word2 word3'", "is_sample": False}
    ]

    # Fixing large test case formatting
    test_cases[7]["input"] = "['a']\\n" + " ".join(["a"*1000 for _ in range(1000)])
    test_cases[7]["expected_output"] = " ".join(["a" for _ in range(1000)])

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
        "topics": ["Array", "Hash Table", "String", "Trie"],
        "companyIndex": 0
    }

    output_path = "401-600/648_Replace_Words.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
