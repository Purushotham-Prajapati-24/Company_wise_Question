import json
import os

def generate_json():
    problem_id = 367
    title = "Valid Perfect Square"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>367. Valid Perfect Square</h3>
<p>Given a positive integer <code>num</code>, return <code>true</code> if <code>num</code> is a perfect square or <code>false</code> otherwise.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer. In other words, it is the product of some integer with itself.</p>

<p>You must not use any built-in library function, such as <code>sqrt</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = 16
<strong>Output:</strong> true
<strong>Explanation:</strong> We return true because 4 * 4 = 16 and 4 is an integer.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A positive integer `num`."
    output_format = "A boolean representing if the number is a perfect square."
    
    constraints = [
        "1 <= num <= 2^31 - 1"
    ]
    
    explanation = """To determine if a number is a perfect square without using `sqrt()`, we can use **Binary Search**.

### Algorithm Steps:
1. **Initialize Boundaries**: `left = 1`, `right = num`.
2. **Loop**:
   - While `left <= right`:
     - Calculate `mid = left + (right - left) // 2`.
     - Calculate `square = mid * mid`.
     - If `square == num`: Return `true`.
     - If `square < num`: Move `left = mid + 1`.
     - If `square > num`: Move `right = mid - 1`.
3. **Result**: If the loop finishes without finding a match, return `false`.

### Alternative (Newton's Method):
Starting with $x = num$, iteratively update $x = (x + num//x) // 2$ until $x^2 \le num$. Then check if $x^2 == num$. This is often faster for large $n$.

### Complexity Analysis:
- **Time Complexity**: $O(\log N)$, where $N$ is the input number.
- **Space Complexity**: $O(1)$."""
    
    answer = """class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
            
        left, right = 2, num // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            guess = mid * mid
            if guess == num:
                return True
            if guess > num:
                right = mid - 1
            else:
                left = mid + 1
                
        return False"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def isPerfectSquare(self, num: int) -> bool:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        num = int(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.isPerfectSquare(num)))",
        "cpp": "class Solution {\npublic:\n    bool isPerfectSquare(int num) {\n        // Your logic here\n        return false;\n    }\n};",
        "java": "public class Solution {\n    public boolean isPerfectSquare(int num) {\n        // Your logic here\n        return false;\n    }\n}",
        "javascript": "/**\n * @param {number} num\n * @return {boolean}\n */\nvar isPerfectSquare = function(num) {\n    // Your logic here\n};",
        "c": "bool isPerfectSquare(int num) {\n    // Your logic here\n    return false;\n}"
    }

    test_cases = [
        {"input": "16", "expected_output": "true", "is_sample": True},
        {"input": "14", "expected_output": "false", "is_sample": True},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "2", "expected_output": "false", "is_sample": False},
        {"input": "4", "expected_output": "true", "is_sample": False},
        {"input": "8", "expected_output": "false", "is_sample": False},
        {"input": "9", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "2147395600", "expected_output": "true", "is_sample": False}, # 46340^2
        {"input": "2147483647", "expected_output": "false", "is_sample": False},
        {"input": "100000000", "expected_output": "true", "is_sample": False}
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
        "topics": ["Math", "Binary Search"],
        "companyIndex": 1
    }

    output_path = "301-500/367_Valid_Perfect_Square.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
