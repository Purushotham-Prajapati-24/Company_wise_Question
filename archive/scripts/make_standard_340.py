import json
import os

def generate_json():
    problem_id = 340
    title = "Longest Substring with At Most K Distinct Characters"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>340. Longest Substring with At Most K Distinct Characters</h3>
<p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the length of the longest substring of </em><code>s</code><em> that contains at most </em><code>k</code><em> <strong>distinct</strong> characters</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "eceba", k = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring is "ece" with length 3.</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aa", k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The substring is "aa" with length 2.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 50</code></li>
</ul>"""

    input_format = "A string `s` and an integer `k`."
    output_format = "An integer representing the maximum substring length."
    
    constraints = [
        "1 <= s.length <= 50,000",
        "0 <= k <= 50"
    ]
    
    explanation = """To find the longest substring with at most $k$ distinct characters, we use the **Sliding Window** (Two Pointers) technique with a **Hash Map** to track character frequencies.

### Algorithm Steps:
1. **Initialize**: 
   - `left = 0`: Left pointer of the window.
   - `max_len = 0`: Best length found so far.
   - `counts = {}`: A hash map to store frequencies of characters in the current window.
2. **Iterate**:
   - For each character `s[right]` at index `right`:
     - Add `s[right]` to the `counts` map or increment its count.
     - **Shrink Window**: While the number of unique characters in the window (i.e., `len(counts)`) is greater than $k$:
       - Decrement the count of `s[left]`. If it becomes 0, remove it from the map.
       - Move `left` forward.
     - **Update Result**: After shrinking, the window `[left, right]` contains at most $k$ distinct characters. Update `max_len = max(max_len, right - left + 1)`.
3. **Terminate**: Return `max_len`.

### Complexity Analysis:
- **Time Complexity**: $O(N)$, where $N$ is the number of characters in the string. Each character is visited at most twice (once by `right` and once by `left`). Hash map operations are $O(1)$ on average.
- **Space Complexity**: $O(K)$, where $K$ is the number of distinct characters, as the hash map will store at most $k+1$ entries at any time."""
    
    answer = """class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
            
        counts = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        lines = raw_input.split('\\n')\n        s = json.loads(lines[0])\n        k = json.loads(lines[1])\n        sol = Solution()\n        print(json.dumps(sol.lengthOfLongestSubstringKDistinct(s, k)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int lengthOfLongestSubstringKDistinct(string s, int k) {\n        // Your logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        string s = line1.length() >= 2 ? line1.substr(1, line1.length() - 2) : \"\";\n        int k = stoi(line2);\n        Solution sol;\n        cout << sol.lengthOfLongestSubstringKDistinct(s, k) << \"\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int lengthOfLongestSubstringKDistinct(String s, int k) {\n        // Your logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        if (scanner.hasNextLine()) {\n            String line1 = scanner.nextLine();\n            String line2 = scanner.nextLine();\n            String s = line1.length() >= 2 ? line1.substring(1, line1.length() - 1) : \"\";\n            int k = Integer.parseInt(line2.trim());\n            Solution sol = new Solution();\n            System.out.println(sol.lengthOfLongestSubstringKDistinct(s, k));\n        }\n    }\n}",
        "javascript": "/**\n * @param {string} s\n * @param {number} k\n * @return {number}\n */\nvar lengthOfLongestSubstringKDistinct = function(s, k) {\n    // Your logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync('/dev/stdin', 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const s = JSON.parse(input[0]);\n    const k = JSON.parse(input[1]);\n    console.log(JSON.stringify(lengthOfLongestSubstringKDistinct(s, k)));\n}",
        "c": "#include <stdlib.h>\n#include <stdio.h>\n#include <string.h>\n\nint lengthOfLongestSubstringKDistinct(char * s, int k) {\n    // Your logic here\n    return 0;\n}\n\nint main() {\n    char line1[500000];\n    char line2[100];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        line1[strcspn(line1, \"\\r\\n\")] = 0;\n        char* s = line1;\n        if (strlen(s) >= 2 && s[0] == '\"' && s[strlen(s)-1] == '\"') {\n            s[strlen(s)-1] = '\\0';\n            s++;\n        }\n        int k = atoi(line2);\n        printf(\"%d\\n\", lengthOfLongestSubstringKDistinct(s, k));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '"eceba"\\n2', "expected_output": "3", "is_sample": True},
        {"input": '"aa"\\n1', "expected_output": "2", "is_sample": True},
        {"input": '"abcde"\\n5', "expected_output": "5", "is_sample": False},
        {"input": '"abcde"\\n1', "expected_output": "1", "is_sample": False},
        {"input": '"ccccccc"\\n1', "expected_output": "7", "is_sample": False},
        {"input": '"abaccc"\\n2', "expected_output": "4", "is_sample": False},
        {"input": '"kb"\\n10', "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": json.dumps("a"*50000) + "\\n1", "expected_output": "50000", "is_sample": False},
        {"input": json.dumps("abcdefghijklmnopqrstuvwxyz"*2000) + "\\n26", "expected_output": "52000", "is_sample": False},
        {"input": json.dumps("a"*25000 + "b"*25000) + "\\n1", "expected_output": "25000", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Sliding Window"],
        "companyIndex": 1
    }

    output_path = "301-500/340_Longest_Substring_with_At_Most_K_Distinct_Characters.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
