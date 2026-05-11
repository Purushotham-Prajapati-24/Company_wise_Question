import json
import os

def generate_json():
    problem_id = 586
    title = "Customer Placing the Largest Number of Orders"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>586. Customer Placing the Largest Number of Orders</h3>
<p>Write a solution to find the <code>customer_number</code> for the customer who has placed the <b>largest number of orders</b>.</p>

<p>The test cases are generated such that <b>exactly one customer</b> will have placed more orders than any other customer.</p>

<p>&nbsp;</p>
<p><strong>Table schema:</strong></p>
<pre>
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
1,1
2,2
3,3
4,3

<strong>Output:</strong> 
3

<strong>Explanation:</strong> 
The customer with number 3 has two orders, which is greater than either customer 1 or 2, who each have one order. 
So the result is customer_number 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of orders is in the range <code>[1, 500]</code>.</li>
	<li>Wait, actual LeetCode constraints might be higher. Let's assume <code>10^4</code> for algorithmic robustness.</li>
</ul>"""

    input_format = "Each line contains an order: 'order_number,customer_number'."
    output_format = "A single integer or string representing the customer_number."
    
    constraints = [
        "1 <= n_orders <= 10^4",
        "Exactly one winner guaranteed.",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To find the customer with the most orders:
1. **The Strategy**:
   - We need to count the frequency of each `customer_number` appearing in the `Orders` table.
2. **Implementation**:
   - Use a hash map (dictionary) `counts` to store the tally of each customer.
   - Iterate through each line of the input.
   - For every `customer_number`, increment its count in `counts`.
   - Maintain a variable `max_orders` and `winner_customer` to track the one with the highest count so far.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of orders.
   - Space Complexity: O(U) where U is the number of unique customers."""
    
    answer = """from collections import Counter
def largestOrders(orders: list[tuple]) -> int:
    if not orders: return -1
    counts = Counter(o[1] for o in orders)
    # Since guaranteed exactly one winner
    return counts.most_common(1)[0][0]"""

    boilerplate = {
        "python": "import sys\nfrom collections import Counter\n\ndef largestOrders(orders):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    orders = []\n    for line in lines:\n        if not line: continue\n        parts = line.split(',')\n        orders.append((int(parts[0]), int(parts[1])))\n    print(largestOrders(orders))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n\nusing namespace std;\n\nint largestOrders(vector<pair<int, int>>& orders) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int largestOrders(List<int[]> orders) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function largestOrders(orders) {\n    // User logic\n}",
        "c": "int largestOrders(int** orders, int ordersSize, int* ordersColSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1,1\\n2,2\\n3,3\\n4,3", "expected_output": "3", "is_sample": True},
        {"input": "1,10", "expected_output": "10", "is_sample": True},
        {"input": "1,1\\n2,2\\n3,3\\n4,3\\n5,2\\n6,2", "expected_output": "2", "is_sample": False},
        {"input": "1,5\\n2,5\\n3,5", "expected_output": "5", "is_sample": False},
        {"input": "100,500\\n101,500\\n102,600", "expected_output": "500", "is_sample": False},
        {"input": "1,1\\n2,2\\n3,1\\n4,2\\n5,1", "expected_output": "1", "is_sample": False},
        {"input": "1,99\\n2,100\\n3,99", "expected_output": "99", "is_sample": False},
        # Stress cases
        {"input": "\\n".join([f"{i},1" for i in range(1, 10001)]), "expected_output": "1", "is_sample": False},
        {"input": "\\n".join([f"{i},{i}" for i in range(1, 10000)]) + "\\n10001,1", "expected_output": "1", "is_sample": False},
        {"input": "1,42", "expected_output": "42", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Counting"],
        "companyIndex": 0
    }

    output_path = "401-600/586_Customer_Placing_the_Largest_Number_of_Orders.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
