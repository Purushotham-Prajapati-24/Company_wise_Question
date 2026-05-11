import json
import os

def generate_json():
    # 358. Rearrange String k Distance Apart
    problem_id = 358
    title = "Rearrange String k Distance Apart"
    difficulty = "HARD"
    marks = 20
    
    html_description = """<h3>358. Rearrange String k Distance Apart</h3>
<p>Given a non-empty string <code>s</code> and an integer <code>k</code>, rearrange the string such that the same characters are at least <code>k</code> distance from each other.</p>

<p>All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string <code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aabbcc", k = 3
<strong>Output:</strong> "abcabc"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aaabc", k = 3
<strong>Output:</strong> ""
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "aaadbbcc", k = 2
<strong>Output:</strong> "abacabcd"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>"""

    input_format = "A string `s` and an integer `k`."
    output_format = "The rearranged string satisfying the distance constraint or an empty string."
    
    constraints = [
        "1 <= s.length <= 300,000",
        "0 <= k <= s.length",
        "Lowercase English letters only.",
        "Must handle large inputs efficiently."
    ]
    
    explanation = """### Comprehensive Explanation for 358. Rearrange String k Distance Apart

The goal is to rearrange a string so that any two identical characters are at least $k$ indices apart. This is a classic greedy problem that can be solved using a priority queue.

#### Optimization Strategy (Greedy with Max-Heap)
1. **Frequency Counting**: First, count the frequency of each character. The character with the highest frequency is the most "constrained" and should be placed as early as possible.
2. **Priority Queue**: Use a Max-Heap to always pick the character with the highest remaining frequency that is currently eligible for placement.
3. **Cool-down Mechanism**: 
   - Once a character is used, it becomes ineligible for the next $k-1$ placements.
   - We maintain a **Waiting Queue** (a deque) to store these "cooling" characters.
   - For each placement step, we pop from the Max-Heap, use the character, and add it to the wait queue with its updated count.
   - If the wait queue's size reaches $k$, the character at the front of the wait queue is now eligible to be placed again. We move it back to the Max-Heap if its count is still greater than 0.

#### Most Optimized Approach in Python
- **Heap Eligibility**: If at any step the Max-Heap is empty but we haven't finished the string, it means no characters are eligible to satisfy the $k$ distance. This implies the arrangement is impossible.
- **Time Complexity**: $O(N \log \Sigma)$, where $N$ is the string length and $\Sigma$ is the alphabet size (26). Since $\Sigma$ is constant, this is effectively $O(N)$.
- **Space Complexity**: $O(\Sigma)$ to store the frequencies and the heap.

#### Mathematical Intuition
If the most frequent character appears $F$ times, we need at least $(F-1) \times k + 1$ total characters if $k$ is large. However, other characters can fill the gaps. The greedy approach correctly handles these dependencies.

### Performance Analysis
- The solution scales linearly with the string length, handling the $3 \times 10^5$ constraint within the time limit easily.
"""

    answer = """import heapq
from collections import Counter, deque

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        \"\"\"
        Rearranges string s so that same characters are at least k distance apart.
        Uses a Greedy approach with a Max-Heap and a waiting queue.
        \"\"\"
        if k <= 1:
            return s
            
        # 1. Count frequencies
        counts = Counter(s)
        # 2. Max-Heap based on frequencies
        max_heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(max_heap)
        
        # 3. Waiting queue to manage the k-distance constraint
        wait_q = deque()
        res = []
        
        while len(res) < len(s):
            # If no eligible characters are available in the heap
            if not max_heap:
                return ""
            
            # Pick the character with the highest remaining frequency
            neg_count, char = heapq.heappop(max_heap)
            res.append(char)
            
            # The character used enters the 'wait' period
            wait_q.append((neg_count + 1, char))
            
            # If we've passed k steps, the first-in character is eligible again
            if len(wait_q) == k:
                f_count, f_char = wait_q.popleft()
                if f_count < 0:
                    heapq.heappush(max_heap, (f_count, f_char))
                    
        return "".join(res)"""

    boilerplate = {
        "python": "import sys\nimport json\nimport heapq\nfrom collections import Counter, deque\n\nclass Solution:\n    def rearrangeString(self, s: str, k: int) -> str:\n        pass\n\nif __name__ == '__main__':\n    # handle parsing\n    pass",
        "cpp": "class Solution {\npublic:\n    string rearrangeString(string s, int k) { return \"\"; }\n};",
        "java": "class Solution {\n    public String rearrangeString(String s, int k) { return \"\"; }\n}",
        "javascript": "/**\n * @param {string} s\n * @param {number} k\n * @return {string}\n */\nvar rearrangeString = function(s, k) { return \"\"; };",
        "c": "char* rearrangeString(char* s, int k) { return \"\"; }"
    }

    test_cases = [
        # 1. Sample 1
        {"input": '{"s": "aabbcc", "k": 3}', "expected_output": '"abcabc"', "is_sample": True},
        # 2. Sample 2 (Impossible)
        {"input": '{"s": "aaabc", "k": 3}', "expected_output": '""', "is_sample": True},
        # 3. Diverse: Single character
        {"input": '{"s": "a", "k": 1}', "expected_output": '"a"', "is_sample": False},
        # 4. Diverse: k = 0 (No constraint)
        {"input": '{"s": "aaabbb", "k": 0}', "expected_output": '"aaabbb"', "is_sample": False},
        # 5. Diverse: Impossible all same
        {"input": '{"s": "aaaa", "k": 2}', "expected_output": '""', "is_sample": False},
        # 6. Diverse: Large k with many distinct chars
        {"input": '{"s": "abcdef", "k": 6}', "expected_output": '"abcdef"', "is_sample": False},
        # 7. Diverse: k is string length
        {"input": '{"s": "aabb", "k": 4}', "expected_output": '""', "is_sample": False},
        # 8. Stress: Alternating pattern
        {"input": '{"s": "ababab", "k": 2}', "expected_output": '"ababab"', "is_sample": False},
        # 9. Stress: Sparse unique chars
        {"input": '{"s": "aaabbc", "k": 2}', "expected_output": '"ababac"', "is_sample": False},
        # 10. Stress: Max length, all unique
        {"input": '{"s": "abcdefghijklmnopqrstuvwxyz", "k": 26}', "expected_output": '"abcdefghijklmnopqrstuvwxyz"', "is_sample": False}
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
        "topics": ["Heap", "Greedy", "String", "Hash Table"],
        "companyIndex": 1
    }

    output_path = "301-500/358_Rearrange_String_k_Distance_Apart.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path} with 10 test cases.")

if __name__ == "__main__":
    generate_json()
