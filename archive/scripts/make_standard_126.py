import json
import os

def generate_json():
    problem_id = 126
    title = "Word Ladder II"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>126. Word Ladder II</h3>
<p>A <strong>transformation sequence</strong> from word <code>beginWord</code> to word <code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words <code>beginWord -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub></code> such that:</p>

<ul>
	<li>Every adjacent pair of words differs by a single letter.</li>
	<li>Every <code>s<sub>i</sub></code> (for <code>1 &lt;= i &lt;= k</code>) is in <code>wordList</code>. Note that <code>beginWord</code> does not need to be in <code>wordList</code>.</li>
	<li><code>s<sub>k</sub> == endWord</code></li>
</ul>

<p>Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return <em>all the <strong>shortest transformation sequences</strong> from</em> <code>beginWord</code> <em>to</em> <code>endWord</code><em>, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words</em> <code>[beginWord, s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub>]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>Output:</strong> [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
<strong>Explanation:</strong>&nbsp;There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>Output:</strong> []
<strong>Explanation:</strong> The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= beginWord.length &lt;= 5</code></li>
	<li><code>endWord.length == beginWord.length</code></li>
	<li><code>1 &lt;= wordList.length &lt;= 500</code></li>
	<li><code>wordList[i].length == beginWord.length</code></li>
	<li><code>beginWord</code>, <code>endWord</code>, and <code>wordList[i]</code> consist of lowercase English letters.</li>
	<li><code>beginWord != endWord</code></li>
	<li>All the words in <code>wordList</code> are <strong>unique</strong>.</li>
	<li>The sum of all shortest transformation sequences does not exceed 10<sup>5</sup>.</li>
</ul>"""

    input_format = "Three lines. Line 1: beginWord. Line 2: endWord. Line 3: space-separated wordList."
    output_format = "A list of lists representing all shortest transformation sequences."
    
    constraints = [
        "1 <= beginWord.length <= 5",
        "1 <= wordList.length <= 500",
        "Shortest path results total count <= 10^5."
    ]
    
    explanation = """To find all shortest transformation sequences:
1. **BFS (Shortest Path & Graph Building)**:
   - Use BFS to find the minimum distance from `beginWord` to `endWord`.
   - Maintain a dictionary `dist` to store the distance of each word from `beginWord`.
   - Simultaneously build an adjacency list `adj` where `adj[u]` contains all words `v` such that `v` is one character away from `u` and `dist[v] == dist[u] + 1`. This ensures we only store edges that are part of a shortest path.
2. **DFS (Backtracking/Path Reconstruction)**:
   - Use DFS starting from `beginWord` to explore paths in the `adj` graph.
   - Stop when `endWord` is reached and add the current path to the result.
3. **Complexity**:
   - Time Complexity: O(N * L^2 + PathCount * L), where N is wordList size, L is word length.
   - Space Complexity: O(N * L) for storing the distance map, adjacency list, and queue."""
    
    answer = """from collections import deque, defaultdict

def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []
    
    # BFS to find the shortest distance and build a layered graph (parent pointers)
    adj = defaultdict(list)
    dist = {beginWord: 0}
    queue = deque([beginWord])
    found = False
    
    while queue and not found:
        # Process level-by-level
        level_size = len(queue)
        visited_this_level = {}
        for _ in range(level_size):
            curr = queue.popleft()
            
            for i in range(len(curr)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = curr[:i] + char + curr[i+1:]
                    if next_word in wordSet:
                        # If next_word is new or was found at this exact level
                        if next_word not in dist or dist[next_word] == dist[curr] + 1:
                            if next_word not in dist:
                                dist[next_word] = dist[curr] + 1
                                queue.append(next_word)
                            adj[curr].append(next_word)
                            if next_word == endWord:
                                found = True
        
    if not found:
        return []

    # DFS/Backtracking to find all paths using the layered graph
    res = []
    
    def backtrack(curr, path):
        if curr == endWord:
            res.append(list(path))
            return
        
        for neighbor in adj[curr]:
            path.append(neighbor)
            backtrack(neighbor, path)
            path.pop()
            
    backtrack(beginWord, [beginWord])
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque, defaultdict\n\ndef findLadders(beginWord, endWord, wordList):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        begin = lines[0].strip()\n        end = lines[1].strip()\n        words = lines[2].split()\n        print(json.dumps(findLadders(begin, end, words)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_set>\n#include <unordered_map>\n#include <queue>\nusing namespace std;\nvector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {\n    // User logic\n    return {};\n}\nint main() {\n    string begin,end,wline;\n    if(!getline(cin,begin)||!getline(cin,end)||!getline(cin,wline)) return 0;\n    istringstream ss(wline); vector<string> wl; string w;\n    while(ss>>w) wl.push_back(w);\n    auto res=findLadders(begin,end,wl);\n    cout<<\"[\";\n    for(int i=0;i<(int)res.size();i++){\n        cout<<\"[\";\n        for(int j=0;j<(int)res[i].size();j++){cout<<\"\\\"\"<<res[i][j]<<\"\\\"\";if(j+1<(int)res[i].size())cout<<\", \";}\n        cout<<\"]\";if(i+1<(int)res.size())cout<<\", \";\n    }\n    cout<<\"]\"<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {\n        // User logic\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String begin=br.readLine().trim(), end=br.readLine().trim();\n        String[] wArr=br.readLine().trim().split(\"\\\\s+\");\n        List<String> wl=Arrays.asList(wArr);\n        List<List<String>> res=findLadders(begin,end,wl);\n        StringBuilder sb=new StringBuilder(\"[\");\n        for(int i=0;i<res.size();i++){sb.append(\"[\");List<String> path=res.get(i);for(int j=0;j<path.size();j++){sb.append(\"\\\"\").append(path.get(j)).append(\"\\\"\");if(j+1<path.size())sb.append(\", \");}sb.append(\"]\");if(i+1<res.size())sb.append(\", \");}\n        sb.append(\"]\"); System.out.println(sb);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction findLadders(beginWord,endWord,wordList){\n    // User logic\n    return [];\n}\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=3){\n  const begin=lines[0].trim(),end=lines[1].trim(),wl=lines[2].trim().split(/\\s+/);\n  const res=findLadders(begin,end,wl);\n  console.log('['+res.map(p=>'['+p.map(w=>'\"'+w+'\"').join(', ')+']').join(', ')+']');\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nchar*** findLadders(char*beginWord,char*endWord,char**wordList,int wordListSize,int*returnSize,int**returnColumnSizes){\n    // User logic\n    *returnSize=0; *returnColumnSizes=NULL; return NULL;\n}\nint main(){\n    char begin[20],end[20],wline[10000];\n    if(!fgets(begin,sizeof(begin),stdin)||!fgets(end,sizeof(end),stdin)||!fgets(wline,sizeof(wline),stdin)) return 0;\n    begin[strcspn(begin,\"\\r\\n\")]='\\0'; end[strcspn(end,\"\\r\\n\")]='\\0'; wline[strcspn(wline,\"\\r\\n\")]='\\0';\n    char*wl[600]; int wlsz=0; char*tok=strtok(wline,\" \");\n    while(tok&&wlsz<600){wl[wlsz++]=tok;tok=strtok(NULL,\" \");}\n    int returnSize=0; int*colSz=NULL;\n    char***res=findLadders(begin,end,wl,wlsz,&returnSize,&colSz);\n    printf(\"[\");\n    for(int i=0;i<returnSize;i++){printf(\"[\");for(int j=0;j<colSz[i];j++){printf(\"\\\"%s\\\"\",res[i][j]);if(j+1<colSz[i])printf(\", \");}printf(\"]\");if(i+1<returnSize)printf(\", \");}\n    printf(\"]\\n\"); return 0;\n}"
    }

    test_cases = [
        {"input": "hit\\ncog\\nhot dot dog lot log cog", "expected_output": "[[\"hit\", \"hot\", \"dot\", \"dog\", \"cog\"], [\"hit\", \"hot\", \"lot\", \"log\", \"cog\"]]", "is_sample": True},
        {"input": "hit\\ncog\\nhot dot dog lot log", "expected_output": "[]", "is_sample": True},
        {"input": "a\\nc\\na b c", "expected_output": "[[\"a\", \"c\"]]", "is_sample": False},
        {"input": "red\\ntax\\nted tex red tax", "expected_output": "[[\"red\", \"ted\", \"tex\", \"tax\"]]", "is_sample": False},
        {"input": "lost\\ncost\\nmost lost cost", "expected_output": "[[\"lost\", \"cost\"]]", "is_sample": False},
        {"input": "abc\\ndef\\nabc abd ade def ghi", "expected_output": "[[\"abc\", \"abd\", \"ade\", \"def\"]]", "is_sample": False},
        {"input": "hot\\ndog\\nhot dog dot", "expected_output": "[[\"hot\", \"dot\", \"dog\"]]", "is_sample": False},
        # Stress cases
        {"input": "hit\\ncog\\n" + " ".join(["hot", "dot", "dog", "lot", "log", "cog"]), "expected_output": "[[\"hit\", \"hot\", \"dot\", \"dog\", \"cog\"], [\"hit\", \"hot\", \"lot\", \"log\", \"cog\"]]", "is_sample": False},
        {"input": "a\\nz\\n" + " ".join([chr(ord('a')+i) for i in range(26)]), "expected_output": "[[\"a\", \"z\"]]", "is_sample": False},
        {"input": "abcd\\nefgh\\nabcd abce abfe efge efgh", "expected_output": "[[\"abcd\", \"abce\", \"abfe\", \"efge\", \"efgh\"]]", "is_sample": False}
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
        "topics": ["Array", "String", "Backtracking", "BFS"],
        "companyIndex": 0
    }

    output_path = "1-200/126_Word_Ladder_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
