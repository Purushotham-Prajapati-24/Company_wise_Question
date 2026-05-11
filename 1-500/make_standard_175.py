import json
import os

def generate_json():
    problem_id = 175
    title = "Combine Two Tables"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>175. Combine Two Tables</h3>
<p>Table: <code>Person</code></p>
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.
</pre>

<p>Table: <code>Address</code></p>
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = personId.
</pre>

<p>Write a solution to report the first name, last name, city, and state of each person in the <code>Person</code> table. If the address of a <code>personId</code> is not present in the <code>Address</code> table, report <code>null</code> instead.</p>
<p>Return the result table in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+-------+
| addressId | personId | city          | state |
+-----------+----------+---------------+-------+
| 1         | 2        | New York City | New York |
+-----------+----------+---------------+-------+
<strong>Output:</strong> 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
<strong>Explanation:</strong> 
There is no address guide for personId = 1, so we return null for their city and state.
addressId = 1 contains information about the address of personId = 2.
</pre>"""

    input_format = "JSON containing 'Person' and 'Address' tables as lists of records."
    output_format = "A list of records containing 'firstName', 'lastName', 'city', and 'state'."
    
    constraints = [
        "Person table has personId as primary key.",
        "Address table has addressId as primary key.",
        "Must handle missing address records correctly (Left Join)."
    ]
    
    explanation = """To combine these two tables while ensuring all persons are included regardless of whether they have an address:
1. **Left Outer Join**: We join the `Person` table with the `Address` table using `personId`.
2. **Left Join Logic**: In SQL, a `LEFT JOIN` returns all records from the left table (`Person`), and the matched records from the right table (`Address`). If there is no match, the result is `NULL` for the columns of the right table.
3. **Query**:
   ```sql
   SELECT firstName, lastName, city, state
   FROM Person
   LEFT JOIN Address ON Person.personId = Address.personId;
   ```"""
    
    answer = """SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;"""

    boilerplate = {
        "python": "# SQL Problem: Use the query provided in the answer section.\nimport pandas as pd\n\ndef combine_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:\n    # Equivalent logic in Python (Pandas)\n    return pd.merge(person, address, on='personId', how='left')[['firstName', 'lastName', 'city', 'state']]",
        "cpp": "// SQL Problem: Solve using the query in the answer field.",
        "java": "// SQL Problem: Solve using the query in the answer field.",
        "javascript": "// SQL Problem: Solve using the query in the answer field.",
        "c": "// SQL Problem: Solve using the query in the answer field."
    }

    test_cases = [
        {"input": '{"Person": [{"personId": 1, "lastName": "Wang", "firstName": "Allen"}, {"personId": 2, "lastName": "Alice", "firstName": "Bob"}], "Address": [{"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"}]}', "expected_output": '[{"firstName": "Allen", "lastName": "Wang", "city": null, "state": null}, {"firstName": "Bob", "lastName": "Alice", "city": "New York City", "state": "New York"}]', "is_sample": True},
        {"input": '{"Person": [{"personId": 1, "lastName": "Doe", "firstName": "John"}], "Address": []}', "expected_output": '[{"firstName": "John", "lastName": "Doe", "city": null, "state": null}]', "is_sample": True},
        {"input": '{"Person": [], "Address": []}', "expected_output": "[]", "is_sample": False},
        {"input": '{"Person": [{"personId": 1, "lastName": "A", "firstName": "B"}], "Address": [{"addressId": 1, "personId": 1, "city": "X", "state": "Y"}]}', "expected_output": '[{"firstName": "B", "lastName": "A", "city": "X", "state": "Y"}]', "is_sample": False},
        {"input": '{"Person": [{"personId": 1, "lastName": "A", "firstName": "B"}, {"personId": 2, "lastName": "C", "firstName": "D"}], "Address": [{"addressId": 1, "personId": 1, "city": "X", "state": "Y"}, {"addressId": 2, "personId": 3, "city": "Z", "state": "W"}]}', "expected_output": '[{"firstName": "B", "lastName": "A", "city": "X", "state": "Y"}, {"firstName": "D", "lastName": "C", "city": null, "state": null}]', "is_sample": False},
        {"input": '{"Person": [{"personId": 5, "lastName": "E", "firstName": "F"}], "Address": [{"addressId": 10, "personId": 5, "city": "Dubai", "state": "UAE"}]}', "expected_output": '[{"firstName": "F", "lastName": "E", "city": "Dubai", "state": "UAE"}]', "is_sample": False},
        {"input": '{"Person": [{"personId": 1, "lastName": "L1", "firstName": "F1"}, {"personId": 2, "lastName": "L2", "firstName": "F2"}], "Address": [{"addressId": 1, "personId": 1, "city": "C1", "state": "S1"}, {"addressId": 2, "personId": 2, "city": "C2", "state": "S2"}]}', "expected_output": '[{"firstName": "F1", "lastName": "L1", "city": "C1", "state": "S1"}, {"firstName": "F2", "lastName": "L2", "city": "C2", "state": "S2"}]', "is_sample": False},
        # Stress Tests
        {"input": '{"Person": [{"personId": i, "lastName": "L"+str(i), "firstName": "F"+str(i)} for i in range(100)], "Address": []}', "expected_output": "...", "is_sample": False},
        {"input": '{"Person": [{"personId": i, "lastName": "L"+str(i), "firstName": "F"+str(i)} for i in range(100)], "Address": [{"addressId": i, "personId": i, "city": "C", "state": "S"} for i in range(100)]}', "expected_output": "...", "is_sample": False},
        {"input": '{"Person": [{"personId": 1, "lastName": "L", "firstName": "F"}], "Address": [{"addressId": i, "personId": 1, "city": "C"+str(i), "state": "S"} for i in range(10)]}', "expected_output": "...", "is_sample": False}
    ]

    # Helper to fix stringified JSON inputs in tests
    for i in [7, 8, 9]:
        p = eval(test_cases[i]["input"])
        test_cases[i]["input"] = json.dumps(p)
        if i == 7:
            ans = [{"firstName": r["firstName"], "lastName": r["lastName"], "city": None, "state": None} for r in p["Person"]]
            test_cases[i]["expected_output"] = json.dumps(ans)
        elif i == 8:
            ans = [{"firstName": r["firstName"], "lastName": r["lastName"], "city": "C", "state": "S"} for r in p["Person"]]
            test_cases[i]["expected_output"] = json.dumps(ans)
        elif i == 9:
            # Person 1 has many addresses? Wait, Person table has personId as PK. Address table has addressId as PK.
            # LEFT JOIN Person ON Person.personId = Address.personId will duplicate Person rows if multiple addresses exist.
            ans = [{"firstName": "F", "lastName": "L", "city": "C"+str(j), "state": "S"} for j in range(10)]
            test_cases[i]["expected_output"] = json.dumps(ans)

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
            "allowed_languages": ["sql"]
        },
        "topics": ["Database"],
        "companyIndex": 0
    }

    output_path = "1-200/175_Combine_Two_Tables.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
