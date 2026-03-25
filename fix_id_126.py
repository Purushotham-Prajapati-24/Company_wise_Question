import json
import os

def generate_test_cases():
    def findLadders(beginWord, endWord, wordList):
        from collections import defaultdict, deque
        wordSet = set(wordList)
        if endWord not in wordSet: return []
        res = []
        layer = {beginWord: [[beginWord]]}
        while layer:
            new_layer = defaultdict(list)
            for word, paths in layer.items():
                if word == endWord: res.extend(paths)
                else:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            next_word = word[:i] + c + word[i+1:]
                            if next_word in wordSet:
                                for path in paths:
                                    new_layer[next_word].append(path + [next_word])
            wordSet -= set(new_layer.keys())
            layer = new_layer
        return res

    cases = [
        {"input": '"hit"\\n"cog"\\n["hot","dot","dog","lot","log","cog"]', "expected_output": json.dumps([["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]), "is_sample": True},
        {"input": '"hit"\\n"cog"\\n["hot","dot","dog","lot","log"]', "expected_output": "[]", "is_sample": True},
        {"input": '"a"\\n"c"\\n["a","b","c"]', "expected_output": json.dumps([["a","c"]]), "is_sample": False},
    ]

    # Case 8: Multiple paths
    cases.append({
        "input": '"hot"\\n"dog"\\n["hot","dot","dog","lot","log"]',
        "expected_output": "[]", # No cog, no bridge
        "is_sample": False
    })

    # Case 9: 100 words
    words9 = ["hot","dot","dog","lot","log","cog"] + ["a"*5 for _ in range(100)]
    cases.append({
        "input": '"hit"\\n"cog"\\n' + json.dumps(words9),
        "expected_output": json.dumps([["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]),
        "is_sample": False
    })

    # Case 10: 2000 words (Peak Constraint)
    cases.append({
        "input": '"aaaaa"\\n"zzzzz"\\n' + json.dumps(["a"*5 for _ in range(2000)]),
        "expected_output": "[]",
        "is_sample": False
    })

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Jane Street/126_Word_Ladder_II.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>126 Word Ladder II</h3><p>A <strong>transformation sequence</strong> from word <code>beginWord</code> to word <code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words <code>beginWord -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub></code> such that:</p><ul><li>Every adjacent pair of words differs by a single letter.</li><li>Every <code>s<sub>i</sub></code> for <code>1 <= i <= k</code> is in <code>wordList</code>. Note that <code>beginWord</code> does not need to be in <code>wordList</code>.</li><li><code>s<sub>k</sub> == endWord</code></li></ul><p>Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return <em>all the <strong>shortest transformation sequences</strong> from</em> <code>beginWord</code> <em>to</em> <code>endWord</code><em>, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words </em><code>[beginWord, s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub>]</code>.</p>"
    d["difficulty"] = "HARD"
    d["marks"] = 25
    d["input_format"] = "Three lines: beginWord, endWord, and wordList (array)."
    d["output_format"] = "A list of lists of strings representing all shortest paths."
    
    d["metadata"] = {
        "time_limit_ms": 2000,
        "memory_limit_mb": 512,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet: return []
        res = []
        layer = {beginWord: [[beginWord]]}
        while layer:
            new_layer = defaultdict(list)
            for word, paths in layer.items():
                if word == endWord: res.extend(paths)
                else:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            next_word = word[:i] + c + word[i+1:]
                            if next_word in wordSet:
                                for path in paths:
                                    new_layer[next_word].append(path + [next_word])
            wordSet -= set(new_layer.keys())
            layer = new_layer
        return res"""

    d["boilerplate"]["python"] = """import sys, json
from collections import defaultdict, deque

def solve(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet: return []
    res = []
    layer = {beginWord: [[beginWord]]}
    while layer:
        new_layer = defaultdict(list)
        for word, paths in layer.items():
            if word == endWord: res.extend(paths)
            else:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordSet:
                            for path in paths:
                                new_layer[next_word].append(path + [next_word])
        wordSet -= set(new_layer.keys())
        layer = new_layer
    return res

if __name__ == '__main__':
    lines = sys.stdin.read().strip().split('\\n')
    if len(lines) >= 3:
        try:
            beginWord = json.loads(lines[0])
            endWord = json.loads(lines[1])
            wordList = json.loads(lines[2])
            print(json.dumps(solve(beginWord, endWord, wordList)))
        except:
            print("[]")
    else:
        print("[]")"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 126 in Jane Street")
