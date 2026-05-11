import json
import os

def generate_json():
    problem_id = 140
    title = "Word Break II"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>140. Word Break II</h3>
<p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, add spaces in <code>s</code> to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in <strong>any order</strong>.</p>
<p><strong>Note:</strong> The same word in the dictionary may be reused multiple times in the segmentation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
<strong>Output:</strong> ["cats and dog","cat sand dog"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
<strong>Output:</strong> ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
<strong>Explanation:</strong> Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 10</code></li>
	<li><code>s</code> and <code>wordDict[i]</code> consist of only lowercase English letters.</li>
	<li>All the strings of <code>wordDict</code> are <strong>unique</strong>.</li>
	<li>The input is generated in a way that the length of the answer does not exceed 10<sup>5</sup>.</li>
</ul>"""

    input_format = "String s, followed by an integer K, and K space-separated words for wordDict."
    output_format = "A list of strings representing all possible valid sentences."
    
    constraints = [
        "1 <= s.length <= 20",
        "1 <= wordDict.length <= 1000",
        "1 <= wordDict[i].length <= 10",
        "Length of answer will not exceed 10^5."
    ]
    
    explanation = """To find all possible valid segmentations of string `s` using `wordDict`, we use Backtracking with Memoization:
1. **Recursion with Memoization**:
   - Define a function `solve(start)` that returns all possible sentence completions for the suffix `s[start:]`.
   - Store results in a cache (memoization) to avoid redundant computations.
2. **Transition**:
   - For a given `start` index, iterate through all possible prefixes `s[start:i]` where `i > start`.
   - If `s[start:i]` is in `wordDict`:
     - Recursively call `solve(i)` to get all possible ways to form the rest of the sentence.
     - Combine the current word with each completion from the recursive call.
3. **Complexity**:
   - Time Complexity: O(2^n) in the worst case (where n is the length of `s`), but the constraints ($n \le 20$) and memoization make it efficient.
   - Space Complexity: O(2^n) to store all combinations."""
    
    answer = """class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def solve(start):
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]
            
            res = []
            for i in range(start + 1, len(s) + 1):
                word = s[start:i]
                if word in word_set:
                    completions = solve(i)
                    for completion in completions:
                        if completion == "":
                            res.append(word)
                        else:
                            res.append(word + " " + completion)
                            
            memo[start] = res
            return res
            
        return solve(0)"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef wordBreak(s, wordDict):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    if not input_data: sys.exit()\n    s = input_data[0]\n    k = int(input_data[1])\n    wordDict = input_data[2:2+k]\n    result = wordBreak(s, wordDict)\n    print(json.dumps(sorted(result)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_set>\n#include <unordered_map>\n#include <algorithm>\nusing namespace std;\nvector<string> wordBreak(string s, vector<string>& wordDict){\n    // User logic here\n    return {};\n}\nint main(){\n    string s; int k;\n    cin>>s>>k;\n    vector<string> wd(k);\n    for(int i=0;i<k;i++) cin>>wd[i];\n    vector<string> res=wordBreak(s,wd);\n    sort(res.begin(),res.end());\n    cout<<\"[\";\n    for(int i=0;i<(int)res.size();i++){cout<<\"\\\"\"<<res[i]<<\"\\\"\";if(i+1<(int)res.size())cout<<\", \";}\n    cout<<\"]\"<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static List<String> wordBreak(String s, List<String> wordDict){\n        // User logic here\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in);\n        if(!sc.hasNext()) return;\n        String s=sc.next(); int k=sc.nextInt();\n        List<String> wd=new ArrayList<>();\n        for(int i=0;i<k;i++) wd.add(sc.next());\n        List<String> res=wordBreak(s,wd);\n        Collections.sort(res);\n        StringBuilder sb=new StringBuilder(\"[\");\n        for(int i=0;i<res.size();i++){sb.append(\"\\\"\").append(res.get(i)).append(\"\\\"\");if(i+1<res.size())sb.append(\", \");}\n        sb.append(\"]\"); System.out.println(sb);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction wordBreak(s,wordDict){\n    // User logic here\n    return [];\n}\nconst input=fs.readFileSync(0,'utf8').split(/\\s+/).filter(Boolean);\nif(input.length>0){\n  const s=input[0]; const k=parseInt(input[1]);\n  const wd=input.slice(2,2+k);\n  const res=wordBreak(s,wd).sort();\n  console.log('['+res.map(r=>'\"'+r+'\"').join(', ')+']');\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nchar** wordBreak(char* s, char** wordDict, int wordDictSize, int* returnSize){\n    // User logic here\n    *returnSize=0; return NULL;\n}\nint main(){\n    char s[25]; int k;\n    if(scanf(\"%s %d\",s,&k)!=2) return 0;\n    char*wd[1001]; static char bufs[1001][15]; int i;\n    for(i=0;i<k;i++){scanf(\"%s\",bufs[i]);wd[i]=bufs[i];}\n    int rsz=0; char**res=wordBreak(s,wd,k,&rsz);\n    printf(\"[\");\n    for(i=0;i<rsz;i++){printf(\"\\\"%s\\\"\",res[i]);if(i+1<rsz)printf(\", \");}\n    printf(\"]\\n\"); return 0;\n}"
    }

    test_cases = [
        {"input": "catsanddog 5 cat cats and sand dog", "expected_output": '["cat sand dog", "cats and dog"]', "is_sample": True},
        {"input": "pineapplepenapple 5 apple pen applepen pine pineapple", "expected_output": '["pine apple pen apple", "pine applepen apple", "pineapple pen apple"]', "is_sample": True},
        {"input": "catsandog 5 cats dog sand and cat", "expected_output": "[]", "is_sample": False},
        {"input": "a 1 a", "expected_output": '["a"]', "is_sample": False},
        {"input": "apple 1 apple", "expected_output": '["apple"]', "is_sample": False},
        {"input": "aaaaaaa 2 a aa", "expected_output": '["a a a a a a a", "a a a a a aa", "a a a a aa a", "a a a aa a a", "a a aa a a a", "a aa a a a a", "aa a a a a a", "a a aa aa a", "a aa a aa a", "aa a a aa a", "a aa aa a a", "aa a aa a a", "aa aa a a a", "aa aa aa a", "a aa aa aa", "aa a aa aa", "aa aa a aa", "a a a aa aa", "a a aa a aa", "a aa a a aa", "aa a a a aa"]', "is_sample": False},
        {"input": "nightmare 4 night mare nigh tm", "expected_output": '["night mare"]', "is_sample": False},
        {"input": "aaaaaaaaaaaaaaaaaaaa 2 a aa", "expected_output": "...", "is_sample": False}, # Stress 1
        {"input": "aaaaaaaaaaaaaaaaaaaa 1 b", "expected_output": "[]", "is_sample": False}, # Stress 2
        {"input": "abcdefghij 10 a b c d e f g h i j", "expected_output": '["a b c d e f g h i j"]', "is_sample": False} # Stress 3
    ]
    
    # Pre-solve stress case 8 if possible
    def _solve(s, words):
        wset = set(words); memo = {}
        def d(st):
            if st == len(s): return [""]
            if st in memo: return memo[st]
            r = []
            for e in range(st+1, len(s)+1):
                w = s[st:e]
                if w in wset:
                    comps = d(e)
                    for c in comps: r.append((w + (" " if c else "") + c).strip())
            memo[st] = r; return r
        return sorted(d(0))

    test_cases[7]["expected_output"] = json.dumps(_solve("aaaaaaaaaaaaaaaaaaaa", ["a","aa"]))

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
        "topics": ["Array", "String", "Dynamic Programming", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-200/140_Word_Break_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
