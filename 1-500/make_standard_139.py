import json
import os

def generate_json():
    problem_id = 139
    title = "Word Break"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>139. Word Break</h3>
<p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, return <code>true</code> if <code>s</code> can be segmented into a space-separated sequence of one or more dictionary words.</p>

<p><strong>Note</strong> that the same word in the dictionary may be reused multiple times in the segmentation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "leetcode", wordDict = ["leet","code"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because "leetcode" can be segmented as "leet code".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "applepenapple", wordDict = ["apple","pen"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 20</code></li>
	<li><code>s</code> and <code>wordDict[i]</code> consist of only lowercase English letters.</li>
	<li>All the strings of <code>wordDict</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "Two lines: first, the string s; second, a JSON array of words 'wordDict'."
    output_format = "true or false as a string."
    
    constraints = [
        "1 <= s.length <= 300",
        "1 <= wordDict.length <= 1000",
        "1 <= wordDict[i].length <= 20",
        "Linear or quadratic time complexity required."
    ]
    
    explanation = """To determine if string `s` can be segmented:
1. **Dynamic Programming**: Let `dp[i]` be `true` if the prefix `s[0...i]` can be segmented.
2. **Initialization**: `dp[0] = true` (empty string).
3. **Transition**: For each `i` from 1 to `len(s)`:
   - For each `j` from 0 to `i-1`:
     - If `dp[j]` is `true` AND the substring `s[j:i]` is in `wordDict`, then `dp[i] = true` and break.
4. **Optimization**: Convert `wordDict` to a `set` for O(1) lookups.
5. **Complexity**:
   - Time Complexity: O(N^2) where N is the length of `s`.
   - Space Complexity: O(N) for the DP array."""
    
    answer = """class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef wordBreak(s, wordDict):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if not lines: sys.exit()\n    s = lines[0].strip()\n    wordDict = json.loads(lines[1].strip())\n    print(str(wordBreak(s, wordDict)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_set>\n#include <sstream>\nusing namespace std;\nbool wordBreak(string s, vector<string>& wordDict){\n    // User logic here\n    return false;\n}\nint main(){\n    string s,wline;\n    if(!getline(cin,s)||!getline(cin,wline)) return 0;\n    // parse JSON array of strings\n    vector<string> wd;\n    wline=wline.substr(1,wline.size()-2); // remove []\n    int i=0; int n=wline.size();\n    while(i<n){\n        if(wline[i]=='\"'){i++;string w;while(i<n&&wline[i]!='\"')w+=wline[i++];wd.push_back(w);i++;}\n        else i++;\n    }\n    cout<<(wordBreak(s,wd)?\"true\":\"false\")<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static boolean wordBreak(String s, List<String> wordDict){\n        // User logic here\n        return false;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String s=br.readLine().trim();\n        String wline=br.readLine().trim();\n        wline=wline.substring(1,wline.length()-1);\n        List<String> wd=new ArrayList<>();\n        for(String part:wline.split(\",\")){String w=part.trim().replaceAll(\"\\\"\",\"\");if(!w.isEmpty())wd.add(w);}\n        System.out.println(wordBreak(s,wd)?\"true\":\"false\");\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction wordBreak(s,wordDict){\n    // User logic here\n    return false;\n}\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=2){\n  const s=lines[0].trim(),wd=JSON.parse(lines[1].trim());\n  console.log(wordBreak(s,wd)?'true':'false');\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\nbool wordBreak(char* s, char** wordDict, int wordDictSize){\n    // User logic here\n    return false;\n}\nint main(){\n    char s[400], wline[50000];\n    if(!fgets(s,sizeof(s),stdin)||!fgets(wline,sizeof(wline),stdin)) return 0;\n    s[strcspn(s,\"\\r\\n\")]='\\0';\n    // extract quoted words\n    char*wl[1001]; int wlsz=0;\n    char*p=wline; static char bufs[1001][25];\n    while((p=strchr(p,'\"'))!=NULL){\n        p++; int j=0;\n        while(*p&&*p!='\"') bufs[wlsz][j++]=*p++;\n        bufs[wlsz][j]='\\0'; wl[wlsz++]=bufs[wlsz]; p++;\n        if(wlsz>=1000) break;\n    }\n    printf(\"%s\\n\",wordBreak(s,wl,wlsz)?\"true\":\"false\"); return 0;\n}"
    }

    test_cases = [
        {"input": "leetcode\n[\"leet\",\"code\"]", "expected_output": "true", "is_sample": True},
        {"input": "applepenapple\n[\"apple\",\"pen\"]", "expected_output": "true", "is_sample": True},
        {"input": "catsandog\n[\"cats\",\"dog\",\"sand\",\"and\",\"cat\"]", "expected_output": "false", "is_sample": False},
        {"input": "a\n[\"a\"]", "expected_output": "true", "is_sample": False},
        {"input": "aaaaaaa\n[\"aaaa\",\"aaa\"]", "expected_output": "true", "is_sample": False},
        {"input": "cbca\n[\"bc\",\"ca\"]", "expected_output": "false", "is_sample": False},
        {"input": "bb\n[\"a\",\"b\",\"bbb\",\"bbbb\"]", "expected_output": "true", "is_sample": False},
        {"input": "", "expected_output": "", "is_sample": False}, # placeholders
        {"input": "", "expected_output": "", "is_sample": False},
        {"input": "", "expected_output": "", "is_sample": False}
    ]
    
    def _solve(s, d):
        ws = set(d)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in ws:
                    dp[i] = True; break
        return dp[len(s)]

    # Stress 8: Long string of 'a'
    s8 = "a" * 300
    d8 = ["aa"]
    test_cases[7] = {"input": s8 + "\n" + json.dumps(d8), "expected_output": str(_solve(s8, d8)).lower(), "is_sample": False}
    
    # Stress 9: Max length no matching
    s9 = "abcdef" * 50
    d9 = ["ghj", "klm", "xyz"]
    test_cases[8] = {"input": s9 + "\n" + json.dumps(d9), "expected_output": str(_solve(s9, d9)).lower(), "is_sample": False}
    
    # Stress 10: Fibonacci strings
    s10 = "aaaaab"
    d10 = ["a", "aa", "aaa", "aaaa", "aaaaa"]
    test_cases[9] = {"input": s10 + "\n" + json.dumps(d10), "expected_output": str(_solve(s10, d10)).lower(), "is_sample": False}

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
        "topics": ["String", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1-200/139_Word_Break.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
