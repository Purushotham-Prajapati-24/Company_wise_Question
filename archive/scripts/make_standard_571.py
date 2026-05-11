import json
import os

def generate_json():
    problem_id = 571
    title = "Find Median Given Frequency of Numbers"
    difficulty = "Hard"
    marks = 30
    
    html_description = """<h3>571. Find Median Given Frequency of Numbers</h3>
<p>Table: <code>Numbers</code></p>
<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
| frequency   | int  |
+-------------+------+
num is the primary key column for this table.
Each row of this table contains the frequency of a number.
</pre>
<p>The <strong>median</strong> is the value separating the higher half from the lower half of a data sample.</p>
<p>Write a SQL query to report the <strong>median</strong> of all the numbers in the <code>Numbers</code> table. Round the median to <strong>one decimal point</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> 
Numbers table:
+-----+-----------+
| num | frequency |
+-----+-----------+
| 0   | 7         |
| 1   | 1         |
| 2   | 3         |
| 3   | 1         |
+-----+-----------+
<strong>Output:</strong> 
+--------+
| median |
+--------+
| 0.0    |
+--------+
<strong>Explanation:</strong> 
If we decompress the Numbers table, we get [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3], total 12 numbers. 
Since it is an even number, the median is the average of the 6th and 7th numbers, which are 0 and 0. 
So the median is (0 + 0) / 2 = 0.
</pre>"""

    input_format = "Multiple lines: 1) Integer n 2) n lines of two space-separated integers: number and frequency."
    output_format = "A single float representing the median rounded to one decimal place."
    
    constraints = [
        "1 <= n <= 10^5",
        "1 <= frequency <= 10^5",
        "Result should be float rounded to 1 decimal place.",
        "O(N log N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To find the median given frequencies:
1. **Sort the Data**:
   - First, sort the list of (number, frequency) pairs by the number in ascending order.
2. **Calculate Total Count**:
   - Calculate the total count of all numbers $N = \sum frequency_i$.
   - The target median indices are $mid1 = (N + 1) // 2$ and $mid2 = (N + 2) // 2$.
3. **Cumulative Frequency**:
   - Iterate through the sorted list and maintain a running sum of frequencies `cum_freq`.
   - Find the numbers at indices $mid1$ and $mid2$:
     - For $mid1$, it's the first number $x$ where `cum_freq >= mid1`.
     - Similarly for $mid2$.
4. **Final Calculation**:
   - Median = $(val(mid1) + val(mid2)) / 2.0$.
5. **Complexity**:
   - Time Complexity: O(N log N) for sorting.
   - Space Complexity: O(N) to store the pairs."""
    
    answer = """def findMedian(nums_freq: list[list[int]]) -> float:
    # nums_freq is list of [num, freq]
    nums_freq.sort()
    total_n = sum(f for n, f in nums_freq)
    
    mid1_idx = (total_n + 1) // 2
    mid2_idx = (total_n + 2) // 2
    
    val1 = val2 = None
    pref = 0
    for num, freq in nums_freq:
        pref += freq
        if val1 is None and pref >= mid1_idx:
            val1 = num
        if val2 is None and pref >= mid2_idx:
            val2 = num
        if val1 is not None and val2 is not None:
            break
            
    return (val1 + val2) / 2.0"""

    boilerplate = {
        "python": "import sys\n\ndef findMedian(nums_freq):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if lines:\n        n = int(lines[0].strip())\n        nums_freq = [list(map(int, line.split())) for line in lines[1:n+1]]\n        print(format(findMedian(nums_freq), '.1f'))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <iomanip>\n\nusing namespace std;\n\ndouble findMedian(vector<pair<int, int>>& nums_freq) {\n    // User logic\n    return 0.0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public double findMedian(int[][] nums_freq) {\n        // User logic\n        return 0.0;\n    }\n}",
        "javascript": "function findMedian(nums_freq) {\n    // User logic\n}",
        "c": "double findMedian(int** nums_freq, int nums_freqSize, int* nums_freqColSize) {\n    // User logic\n    return 0.0;\n}"
    }

    test_cases = [
        {"input": "4\\n0 7\\n1 1\\n2 3\\n3 1", "expected_output": "0.0", "is_sample": True},
        {"input": "4\\n0 1\\n1 1\\n2 1\\n3 1", "expected_output": "1.5", "is_sample": True},
        {"input": "1\\n5 10", "expected_output": "5.0", "is_sample": False},
        {"input": "2\\n1 1\\n2 1", "expected_output": "1.5", "is_sample": False},
        {"input": "2\\n1 2\\n2 1", "expected_output": "1.0", "is_sample": False},
        {"input": "3\\n1 5\\n2 5\\n3 5", "expected_output": "2.0", "is_sample": False},
        {"input": "4\\n-10 1\\n0 1\\n10 1\\n20 1", "expected_output": "5.0", "is_sample": False},
        # Stress cases
        {"input": "100000\\n" + "\\n".join([f"{i} 1" for i in range(100000)]), "expected_output": "49999.5", "is_sample": False},
        {"input": "1\\n" + "1000000000 100000", "expected_output": "1000000000.0", "is_sample": False},
        {"input": "2\\n-1000000000 1\\n1000000000 1", "expected_output": "0.0", "is_sample": False}
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
        "topics": ["Array", "Math", "Sorting"],
        "companyIndex": 0
    }

    output_path = "401-600/571_Find_Median_Given_Frequency_of_Numbers.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
