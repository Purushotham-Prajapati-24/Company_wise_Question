import json
import os

def generate_json():
    problem_id = 127
    title = "Word Ladder"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>127. Word Ladder</h3>
<p>A <strong>transformation sequence</strong> from word <code>beginWord</code> to word <code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words <code>beginWord -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub></code> such that:</p>

<ul>
	<li>Every adjacent pair of words differs by a single letter.</li>
	<li>Every <code>s<sub>i</sub></code> (for <code>1 &lt;= i &lt;= k</code>) is in <code>wordList</code>. Note that <code>beginWord</code> does not need to be in <code>wordList</code>.</li>
	<li><code>s<sub>k</sub> == endWord</code></li>
</ul>

<p>Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return <em>the <strong>number of words</strong> in the <strong>shortest transformation sequence</strong> from</em> <code>beginWord</code> <em>to</em> <code>endWord</code><em>, or </em><code>0</code><em> if no such sequence exists.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>Output:</strong> 5
<strong>Explanation:</strong> One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= beginWord.length &lt;= 10</code></li>
	<li><code>endWord.length == beginWord.length</code></li>
	<li><code>1 &lt;= wordList.length &lt;= 5000</code></li>
	<li><code>wordList[i].length == beginWord.length</code></li>
	<li><code>beginWord</code>, <code>endWord</code>, and <code>wordList[i]</code> consist of lowercase English letters.</li>
	<li><code>beginWord != endWord</code></li>
	<li>All the words in <code>wordList</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "Three lines. Line 1: beginWord. Line 2: endWord. Line 3: space-separated wordList."
    output_format = "An integer representing the length of the shortest transformation sequence."
    
    constraints = [
        "1 <= beginWord.length <= 10",
        "1 <= wordList.length <= 5000.",
        "beginWord != endWord."
    ]
    
    explanation = """To find the shortest transformation sequence length:
1. **BFS (Breadth-First Search)**:
   - This problem can be modeled as finding the shortest path in an unweighted graph where words are nodes and an edge exists between words that differ by one character.
   - Use a queue for BFS, starting with `(beginWord, 1)`.
   - Maintain a set `wordSet` from `wordList` for O(1) lookups and to track unvisited words (remove words from `wordSet` as they are added to the queue to mark them visited).
2. **Logic**:
   - For each word popped from the queue, try changing each character (from 'a' to 'z').
   - If the new word is in `wordSet`:
     - If it's the `endWord`, return current `length + 1`.
     - Otherwise, add it to the queue and remove it from `wordSet`.
3. **Complexity**:
   - Time Complexity: O(N * L^2), where N is the number of words in `wordList` and L is word length.
   - Space Complexity: O(N * L) for storing the word set and queue."""
    
    answer = """from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
        
    queue = deque([(beginWord, 1)])
    
    while queue:
        curr_word, dist = queue.popleft()
        
        if curr_word == endWord:
            return dist
            
        for i in range(len(curr_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = curr_word[:i] + c + curr_word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, dist + 1))
                    
    return 0"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\ndef ladderLength(beginWord, endWord, wordList):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        begin = lines[0].strip()\n        end = lines[1].strip()\n        words = lines[2].split()\n        print(ladderLength(begin, end, words))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_set>\n#include <queue>\n#include <sstream>\nusing namespace std;\nint ladderLength(string beginWord,string endWord,vector<string>&wordList){\n    // User logic\n    return 0;\n}\nint main(){\n    string begin,end,wline;\n    if(!getline(cin,begin)||!getline(cin,end)||!getline(cin,wline)) return 0;\n    istringstream ss(wline); vector<string> wl; string w;\n    while(ss>>w) wl.push_back(w);\n    cout<<ladderLength(begin,end,wl)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int ladderLength(String beginWord,String endWord,List<String> wordList){\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String begin=br.readLine().trim(),end=br.readLine().trim();\n        String[] wArr=br.readLine().trim().split(\"\\\\s+\");\n        System.out.println(ladderLength(begin,end,Arrays.asList(wArr)));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction ladderLength(beginWord,endWord,wordList){\n    // User logic\n    return 0;\n}\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=3){\n  const begin=lines[0].trim(),end=lines[1].trim(),wl=lines[2].trim().split(/\\s+/);\n  console.log(ladderLength(begin,end,wl));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint ladderLength(char*beginWord,char*endWord,char**wordList,int wordListSize){\n    // User logic\n    return 0;\n}\nint main(){\n    char begin[20],end[20],wline[100000];\n    if(!fgets(begin,sizeof(begin),stdin)||!fgets(end,sizeof(end),stdin)||!fgets(wline,sizeof(wline),stdin)) return 0;\n    begin[strcspn(begin,\"\\r\\n\")]='\\0'; end[strcspn(end,\"\\r\\n\")]='\\0'; wline[strcspn(wline,\"\\r\\n\")]='\\0';\n    char*wl[5001]; int wlsz=0; char*tok=strtok(wline,\" \");\n    while(tok&&wlsz<5001){wl[wlsz++]=tok;tok=strtok(NULL,\" \");}\n    printf(\"%d\\n\",ladderLength(begin,end,wl,wlsz)); return 0;\n}"
    }

    test_cases = [
        {"input": "hit\\ncog\\nhot dot dog lot log cog", "expected_output": "5", "is_sample": True},
        {"input": "hit\\ncog\\nhot dot dog lot log", "expected_output": "0", "is_sample": True},
        {"input": "a\\nc\\na b c", "expected_output": "2", "is_sample": False},
        {"input": "hot\\ndog\\nhot dog dot", "expected_output": "3", "is_sample": False},
        {"input": "lost\\ncost\\nmost lost cost", "expected_output": "2", "is_sample": False},
        {"input": "talk\\ntail\\ntall tail talk", "expected_output": "3", "is_sample": False},
        {"input": "ab\\ncd\\nab be de cd", "expected_output": "4", "is_sample": False},
        # Stress cases
        {"input": "a\\nz\\n" + " ".join([chr(ord('a')+i) for i in range(26)]), "expected_output": "2", "is_sample": False},
        {"input": "abcde\\nfghij\\nabcde abcjk abcde klmno", "expected_output": "0", "is_sample": False},
        {"input": "aaaaa\\neeeee\\naaaaa aaaae aaeee aeeee eeeee", "expected_output": "5", "is_sample": False}
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
        "topics": ["Array", "String", "BFS", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "1-200/127_Word_Ladder.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
