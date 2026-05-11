import json
import os

def generate_json():
    problem_id = 159
    title = "Longest Substring with At Most Two Distinct Characters"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>159. Longest Substring with At Most Two Distinct Characters</h3>
<p>Given a string <code>s</code>, return <em>the length of the longest </em><span data-keyword="substring-nonempty"><em>substring</em></span><em> that contains at most <strong>two distinct characters</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "eceba"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring is "ece" which its length is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "ccaabbb"
<strong>Output:</strong> 5
<strong>Explanation:</strong> The substring is "aabbb" which its length is 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of English letters.</li>
</ul>"""

    input_format = "A single line containing the string s."
    output_format = "An integer representing the length of the longest substring with at most two distinct characters."
    
    constraints = [
        "1 <= s.length <= 10^5",
        "s consists of English letters."
    ]
    
    explanation = """To find the longest substring with at most two distinct characters:
1. **Sliding Window Approach**:
   - Maintain a "sliding window" defined by indices `left` and `right`.
   - Use a **Hash Map** (dictionary) to store the characters currently in the window and their frequencies.
2. **Logic**:
   - Iterate with `right` from `0` to `n - 1`.
   - Add the character at `s[right]` to the hash map.
   - If the number of distinct characters in the map exceeds 2:
     - Shrink the window from the `left` by removing characters at `s[left]` and incrementing `left`.
     - Continue until only 2 distinct characters remain in the map.
   - At each step, update the `max_length = max(max_length, right - left + 1)`.
3. **Complexity**:
   - Time Complexity: O(N) because each character is processed at most twice (once by `right` and once by `left`).
   - Space Complexity: O(1) because the hash map contains at most 3 characters at any time."""
    
    answer = """def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    n = len(s)
    if n < 3:
        return n
        
    left = 0
    right = 0
    char_map = {}
    max_len = 2
    
    while right < n:
        char_map[s[right]] = char_map.get(s[right], 0) + 1
        
        while len(char_map) > 2:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]
            left += 1
            
        max_len = max(max_len, right - left + 1)
        right += 1
        
    return max_len"""

    boilerplate = {
        "python": "import sys\n\ndef lengthOfLongestSubstringTwoDistinct(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip(\"\\n\\r\")\n    if data:\n        print(lengthOfLongestSubstringTwoDistinct(data))",
        "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\nint lengthOfLongestSubstringTwoDistinct(string s) {\n    // User logic here\n    return 0;\n}\nint main(){\n    string line; if(getline(cin,line)){if(line.size()>0&&line.back()=='\\r')line.pop_back();cout<<lengthOfLongestSubstringTwoDistinct(line)<<endl;}\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\npublic class Main {\n    public static int lengthOfLongestSubstringTwoDistinct(String s) {\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));\n        String line=br.readLine(); if(line!=null){System.out.println(lengthOfLongestSubstringTwoDistinct(line));}\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction lengthOfLongestSubstringTwoDistinct(s) {\n    // User logic here\n    return 0;\n}\nconst data=fs.readFileSync(0,'utf8').trim();\nif(data) console.log(lengthOfLongestSubstringTwoDistinct(data));",
        "c": "#include <stdio.h>\n#include <string.h>\nint lengthOfLongestSubstringTwoDistinct(char* s) {\n    // User logic here\n    return 0;\n}\nint main(){\n    char line[100005];\n    if(fgets(line,sizeof(line),stdin)){\n        int l=strlen(line); while(l>0&&(line[l-1]=='\\n'||line[l-1]=='\\r'))line[--l]='\\0';\n        if(l>0) printf(\"%d\\n\",lengthOfLongestSubstringTwoDistinct(line));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "eceba", "expected_output": "3", "is_sample": True},
        {"input": "ccaabbb", "expected_output": "5", "is_sample": True},
        {"input": "a", "expected_output": "1", "is_sample": False},
        {"input": "ab", "expected_output": "2", "is_sample": False},
        {"input": "abc", "expected_output": "2", "is_sample": False},
        {"input": "aaaaa", "expected_output": "5", "is_sample": False},
        {"input": "abacaba", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": "a"*50000 + "b"*50000, "expected_output": "100000", "is_sample": False},
        {"input": "abcde"*20000, "expected_output": "2", "is_sample": False},
        {"input": "a"*30000 + "b" + "c" + "a"*30000, "expected_output": "30001", "is_sample": False}
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
        "topics": ["String", "Sliding Window", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "1-200/159_Longest_Substring_with_At_Most_Two_Distinct_Characters.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
