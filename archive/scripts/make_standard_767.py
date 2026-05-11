import json
import os

def generate_json():
    problem_id = 767
    title = "Reorganize String"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>767. Reorganize String</h3>
<p>Given a string <code>s</code>, rearrange the characters of <code>s</code> so that any two adjacent characters are not the same.</p>

<p>Return <em>any possible rearrangement of <code>s</code> or return <code>""</code> if not possible</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> "aba"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aaab"
<strong>Output:</strong> ""
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
"""

    input_format = "A string s."
    output_format = "A string representing the reorganized version or empty string."
    
    constraints = [
        "1 <= s.length <= 500",
        "s consists of lowercase English letters."
    ]
    
    explanation = """To reorganize the string such that no two adjacent characters are the same:
1. **The Feasibility Check**:
   - Count the frequency of each character.
   - If the most frequent character appears more than `(len(s) + 1) // 2` times, it's impossible to separate them all. In this case, return `""`.

2. **The Greedy Construction (Max-Heap)**:
   - Use a max-priority queue (heap) to store characters based on their frequencies.
   - In each step, extract the **two most frequent** characters.
   - Append one of each to the result string.
   - Decrement their frequencies and push them back into the heap if they are still positive.
   - This strategy ensures that the most frequent characters are spread out as much as possible.

3. **Alternative Approach (Filling Interleaved)**:
   - Sort characters by frequency.
   - Fill the most frequent character into even indices `(0, 2, 4...)`.
   - Fill the remaining characters into the next available positions (continuing with even indices, then switching to odd).

Complexity:
- Time: O(N log A) where A is the alphabet size (26). Since A is small, this is essentially O(N).
- Space: O(A) to store the character counts."""
    
    answer = """import heapq
from collections import Counter

def reorganizeString(s: str) -> str:
    res = []
    counts = Counter(s)
    max_heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(max_heap)
    
    if any(count > (len(s) + 1) // 2 for count in counts.values()):
        return ""
        
    while len(max_heap) >= 2:
        cnt1, char1 = heapq.heappop(max_heap)
        cnt2, char2 = heapq.heappop(max_heap)
        
        res.extend([char1, char2])
        
        if cnt1 + 1 < 0:
            heapq.heappush(max_heap, (cnt1 + 1, char1))
        if cnt2 + 1 < 0:
            heapq.heappush(max_heap, (cnt2 + 1, char2))
            
    if max_heap:
        res.append(max_heap[0][1])
        
    return "".join(res)"""

    boilerplate = {
        "python": "import sys\n\ndef reorganizeString(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    print(reorganizeString(s))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <unordered_map>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    string reorganizeString(string s) {\n        return \"\";\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public String reorganizeString(String s) {\n        return \"\";\n    }\n}",
        "javascript": "var reorganizeString = function(s) {\n    return \"\";\n};",
        "c": "char * reorganizeString(char * s){\n    return \"\";\n}"
    }

    test_cases = [
        {"input": "aab", "expected_output": "aba", "is_sample": True},
        {"input": "aaab", "expected_output": "", "is_sample": True},
        # Diverse cases
        {"input": "vvvlo", "expected_output": "vlvov", "is_sample": False},
        {"input": "aa", "expected_output": "", "is_sample": False},
        {"input": "a", "expected_output": "a", "is_sample": False},
        {"input": "baaba", "expected_output": "ababa", "is_sample": False},
        {"input": "abccba", "expected_output": "abcabc", "is_sample": False},
        # Stress cases
        {"input": "a"*250 + "b"*250, "expected_output": "abab... (valid)", "is_sample": False},
        {"input": "a"*251 + "b"*249, "expected_output": "", "is_sample": False},
        {"input": "abcdefghijklmnopqrstuvwxyz" * 19, "expected_output": "valid string", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Greedy", "Sorting", "Heap (Priority Queue)"],
        "companyIndex": 0
    }

    output_path = "601-800/767_Reorganize_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
