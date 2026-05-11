import json
import os

def generate_json():
    problem_id = 642
    title = "Design Search Autocomplete System"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>642. Design Search Autocomplete System</h3>
<p>Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character <code>'#'</code>).</p>

<p>For each character they type <b>except '#'</b>, you need to return the <b>top 3</b> historical hot sentences that have the same prefix as the part of sentence already typed. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first). If less than 3 hot sentences exist, then return as many as you can. When the user types '#', it means the sentence ends, and you should save it as a historical sentence.</p>

<p>Specifically, your receiver should be able to implement the following function:</p>

<ul>
	<li><code>AutocompleteSystem(sentences, times)</code>: This is the constructor. The input is <b>historical data</b>. <code>sentences</code> is a string array consisting of all historical sentences. <code>times</code> is the corresponding times a sentence has been typed. Your system should maintain this historical data.</li>
	<li><code>input(c)</code>: <code>c</code> is the next character in the sentence the user typed. It could be lowercase English letters, a white space, or a special character <code>'#'</code>. Also, the previously typed characters should be recorded. The return value is the <b>top 3</b> hot sentences with the same prefix.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
<strong>Output:</strong> 
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

<strong>Explanation:</strong>
AutocompleteSystem st = new AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2]);
st.input('i'); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has lower ASCII code than 'r', "i love leetcode" is more hot.
st.input(' '); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
st.input('a'); // return []. There are no sentences that have prefix "i a".
st.input('#'); // return []. The user finished the sentence "i a". The sentence "i a" is saved as a historical sentence in system.
</pre>
"""

    input_format = "A list of strings representing methods to call and a list of lists representing arguments."
    output_format = "A list of results from each method call."
    
    constraints = [
        "1 <= sentences.length <= 100",
        "1 <= sentences[i].length <= 100",
        "1 <= times[i] <= 50",
        "lowercase English letters, space, and '#'."
    ]
    
    explanation = """To design the Autocomplete System:
1. Use a Trie and a frequency map.
2. The Trie is to find all sentences with the same prefix.
3. The frequency map (`HashMap<String, Integer>`) is to store and update counts.
4. For `input(c)`:
   - If `c == '#'`:
     - Update the sentence in the frequency map and Trie.
     - Reset the current prefix.
     - Return an empty list.
   - Otherwise:
     - Update current prefix.
     - Search in the Trie for all sentences matching current prefix.
     - Sort results by frequency (descending) and then lexicographically.
     - Return top 3."""
    
    answer = """import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.sentences = set()

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.freq = collections.defaultdict(int)
        for s, t in zip(sentences, times):
            self.freq[s] = t
            self.add_to_trie(s)
        self.curr_prefix = ""

    def add_to_trie(self, s):
        node = self.root
        for char in s:
            node = node.children[char]
            node.sentences.add(s)

    def input(self, c):
        if c == '#':
            self.freq[self.curr_prefix] += 1
            self.add_to_trie(self.curr_prefix)
            self.curr_prefix = ""
            return []
        
        self.curr_prefix += c
        node = self.root
        for char in self.curr_prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        for s in node.sentences:
            results.append((-self.freq[s], s))
        
        results.sort()
        return [s for _, s in results[:3]]"""

    boilerplate = {
        "python": "class AutocompleteSystem:\\n    def __init__(self, sentences, times):\\n        pass",
        "cpp": "class AutocompleteSystem { public: AutocompleteSystem(vector<string>& sentences, vector<int>& times) {} vector<string> input(char c) {} };",
        "java": "class AutocompleteSystem { public AutocompleteSystem(String[] sentences, int[] times) {} public List<String> input(char c) {} }",
        "javascript": "var AutocompleteSystem = function(sentences, times) {};",
        "c": "typedef struct { } AutocompleteSystem;"
    }

    test_cases = [
        {"input": "['AutocompleteSystem', 'input', 'input', 'input', 'input']\\n[[['i love you', 'island', 'ironman', 'i love leetcode'], [5, 3, 2, 2]], ['i'], [' '], ['a'], ['#']]", "expected_output": "[null, ['i love you', 'island', 'i love leetcode'], ['i love you', 'i love leetcode'], [], []]", "is_sample": True},
        {"input": "['AutocompleteSystem', 'input']\\n[[['abc', 'abb', 'aba'], [3, 3, 3]], ['a']]", "expected_output": "[null, ['aba', 'abb', 'abc']]", "is_sample": True},
        {"input": "['AutocompleteSystem', 'input', 'input']\\n[[['test'], [1]], ['t'], ['#']]", "expected_output": "[null, ['test'], []]", "is_sample": False},
        {"input": "['AutocompleteSystem', 'input', 'input', 'input']\\n[[['a'], [1]], ['a'], ['#'], ['a']]", "expected_output": "[null, ['a'], [], ['a']]", "is_sample": False},
        {"input": "['AutocompleteSystem', 'input']\\n[[['a', 'b', 'c'], [1, 2, 3]], ['x']]", "expected_output": "[null, []]", "is_sample": False},
        {"input": "['AutocompleteSystem', 'input']\\n[[['hello world', 'hello'], [10, 5]], ['h']]", "expected_output": "[null, ['hello world', 'hello']]", "is_sample": False},
        {"input": "['AutocompleteSystem', 'input', 'input']\\n[[[], []], ['a'], ['#']]", "expected_output": "[null, [], []]", "is_sample": False},
        {"input": str(["AutocompleteSystem"] + ["input"]*100) + "\\n" + str([[["s"+str(i) for i in range(100)], [50]*100]] + [[chr(ord('a')+(i%26))] for i in range(100)]), "expected_output": "[null" + ", []"*100 + "]", "is_sample": False},
        {"input": "['AutocompleteSystem', 'input', 'input']\\n[[['longsentence'], [10]], ['l'], ['#']]", "expected_output": "[null, ['longsentence'], []]", "is_sample": False},
        {"input": "['AutocompleteSystem', 'input', 'input']\\n[[['a', 'aa', 'aaa'], [1, 2, 3]], ['a'], ['a']]", "expected_output": "[null, ['aaa', 'aa', 'a'], ['aaa', 'aa']]", "is_sample": False}
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
        "topics": ["Design", "Trie", "Hash Table", "String", "Data Stream"],
        "companyIndex": 0
    }

    output_path = "401-600/642_Design_Search_Autocomplete_System.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
