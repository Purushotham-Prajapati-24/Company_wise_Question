import json
import os

def generate_json():
    problem_id = 638
    title = "Shopping Offers"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>638. Shopping Offers</h3>
<p>In LeetCode Store, there are <code>n</code> items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.</p>

<p>You are given an integer array <code>price</code> where <code>price[i]</code> is the price of the <code>i</code><sup>th</sup> item, and an integer array <code>needs</code> where <code>needs[i]</code> is the number of items of the <code>i</code><sup>th</sup> kind that you need to buy.</p>

<p>You are also given a 2D integer array <code>special</code> where <code>special[i]</code> is of size <code>n + 1</code> where <code>special[i][j]</code> is the number of items of the <code>j</code><sup>th</sup> kind included in the <code>i</code><sup>th</sup> offer and <code>special[i][n]</code> (the last integer in the array) is the price of the <code>i</code><sup>th</sup> offer.</p>

<p>Return <em>the lowest price you have to pay for <b>exactly</b> certain items as given, where you could make optimal use of the special offers</em>. You are not allowed to buy more items than you need, even if a special offer pays less than the price of the individual items.</p>

<p>Each special offer can be used as many times as you want.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
<strong>Output:</strong> 14
<strong>Explanation:</strong> There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3 of item A and 0 of item B. 
In special offer 2, you can pay $10 for 1 of item A and 2 of item B. 
You need to buy 3 of item A and 2 of item B, so you may pay $10 for 1*A and 2*B (special offer #2), and $4 for 2*A.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The price of A is $2, B is $3, and C is $4. 
Special offer 1: [1,1,0,4] - You can buy 1 of A and 1 of B for $4. 
Special offer 2: [2,2,1,9] - You can buy 2 of A, 2 of B and 1 of C for $9. 
You need 1 of A, 2 of B and 1 of C, so you can pay $4 for 1*A and 1*B (special offer #1), and $3 for 1*B and $4 for 1*C. 
You cannot use special offer 2 because you only need 1 of A.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == price.length == needs.length</code></li>
	<li><code>1 &lt;= n &lt;= 6</code></li>
	<li><code>0 &lt;= price[i], needs[i] &lt;= 10</code></li>
	<li><code>1 &lt;= special.length &lt;= 100</code></li>
	<li><code>special[i].length == n + 1</code></li>
	<li><code>0 &lt;= special[i][j] &lt;= 50</code></li>
</ul>"""

    input_format = "Arrays `price`, `special`, and `needs`."
    output_format = "An integer representing the minimum cost."
    
    constraints = [
        "1 <= n <= 6",
        "0 <= price[i], needs[i] <= 10",
        "1 <= special.length <= 100"
    ]
    
    explanation = """To find the lowest price to satisfy the `needs` exactly:
1. **DFS with Memoization**:
   - The state is defined by the current `needs` (a tuple of integers).
2. **Algorithm**:
   - Primary strategy: Buy all remaining items individually at their regular prices. This forms the upper bound: `sum(needs[i] * price[i])`.
   - Iterative strategy: Try applying each special offer one at a time.
     - An offer is valid **only if** its counts do not exceed the current `needs`.
     - If valid, recurse with the new `needs` (original `needs` minus offer counts).
     - The cost will be `offer_price + dfs(new_needs)`.
   - Take the minimum of all options.
3. **Complexity Analysis**:
   - Time: O(S * N^K) where S is the number of special offers, N is the max value of an item in `needs` (10), and K is the number of items (6). The total number of states is 11^6 ≈ 1.7 million, but many are unreachable.
   - Space: O(N^K) for the memoization map."""
    
    answer = """class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}
        
        def dfs(cur_needs):
            if cur_needs in memo:
                return memo[cur_needs]
            
            # Option 1: Buy individually
            res = sum(cur_needs[i] * price[i] for i in range(len(price)))
            
            # Option 2: Try special offers
            for offer in special:
                new_needs = []
                for i in range(len(cur_needs)):
                    if offer[i] > cur_needs[i]:
                        break
                    new_needs.append(cur_needs[i] - offer[i])
                
                # If offer was valid for all items
                if len(new_needs) == len(cur_needs):
                    res = min(res, offer[-1] + dfs(tuple(new_needs)))
            
            memo[cur_needs] = res
            return res
            
        return dfs(tuple(needs))"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef shoppingOffers(price, special, needs):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Handle input conversion\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <map>\nusing namespace std;\n\nint shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {\n    // User logic here\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {\n        // User logic here\n    }\n}",
        "javascript": "/**\n * @param {number[]} price\n * @param {number[][]} special\n * @param {number[]} needs\n * @return {number}\n */\nvar shoppingOffers = function(price, special, needs) {\n    // User logic here\n};",
        "c": "int shoppingOffers(int* price, int priceSize, int** special, int specialSize, int* specialColSize, int* needs, int needsSize) {\n    // User logic here\n}"
    }

    test_cases = [
        {"input": "[2,5]\\n[[3,0,5],[1,2,10]]\\n[3,2]", "expected_output": "14", "is_sample": True},
        {"input": "[2,3,4]\\n[[1,1,0,4],[2,2,1,9]]\\n[1,2,1]", "expected_output": "11", "is_sample": True},
        {"input": "[1,1,1]\\n[[1,1,0,2]]\\n[1,1,0]", "expected_output": "2", "is_sample": False},
        {"input": "[5,5,5]\\n[[1,0,0,1]]\\n[1,1,1]", "expected_output": "11", "is_sample": False},
        {"input": "[9,9]\\n[[1,1,1]]\\n[2,2]", "expected_output": "2", "is_sample": False},
        {"input": "[2,5]\\n[[3,0,100]]\\n[3,2]", "expected_output": "16", "is_sample": False},
        {"input": "[0,1]\\n[[1,0,0]]\\n[1,1]", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": "[1,1,1,1,1,1]\\n[[1,1,1,1,1,1,10]]\\n[10,10,10,10,10,10]", "expected_output": "...", "is_sample": False},
        {"input": "[1]*6\\n[[1 for _ in range(7)] for _ in range(100)]\\n[10]*6", "expected_output": "...", "is_sample": False},
        {"input": "[10]*6\\n[]\\n[10]*6", "expected_output": "60", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Backtracking", "Bit Manipulation", "Memoization", "Bitmask"],
        "companyIndex": 0
    }

    output_path = "601-800/638_Shopping_Offers.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
