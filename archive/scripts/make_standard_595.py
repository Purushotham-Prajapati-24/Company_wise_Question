import json
import os

def generate_json():
    problem_id = 595
    title = "Big Countries"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>595. Big Countries</h3>
<p>Table: <code>World</code></p>
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.
</pre>

<p>A country is <b>big</b> if:</p>
<ul>
	<li>it has an area of at least <b>three million</b> (i.e., <code>3,000,000 km<sup>2</sup></code>), or</li>
	<li>it has a population of at least <b>twenty-five million</b> (i.e., <code>25,000,000</code>).</li>
</ul>

<p>Write a solution to find the name, population, and area of the <b>big countries</b>.</p>

<p>Return the result table in <b>any order</b>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
Afghanistan,Asia,652230,25500100,20343000000
Albania,Europe,28748,2831741,12960000000
Algeria,Africa,2381741,37100000,188681000000
Andorra,Europe,468,78115,3712000000
Angola,Africa,1246700,20609294,100990000000

<strong>Output:</strong> 
Afghanistan 25500100 652230
Algeria 37100000 2381741
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of countries is in the range <code>[1, 1000]</code>.</li>
</ul>"""

    input_format = "Each line contains a country record: 'name,continent,area,population,gdp'."
    output_format = "Each line contains 'name population area' for big countries."
    
    constraints = [
        "area >= 3,000,000 or population >= 25,000,000.",
        "1 <= n_countries <= 1000.",
        "O(N) time complexity.",
        "O(1) extra space (beyond input)."
    ]
    
    explanation = """To identify "big" countries from a list:
1. **The Logic**:
   - For each country, we evaluate two conditions:
     - `area >= 3000000`
     - `population >= 25000000`
   - If either condition is true (`OR` logic), the country is "big".
2. **Implementation**:
   - Iterate through each row of the input.
   - Parse the name, population, and area fields.
   - If the logic holds, output the three fields in the required format.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of countries.
   - Space Complexity: O(1) auxiliary space."""
    
    answer = """def bigCountries(countries: list[dict]) -> list[tuple]:
    res = []
    for c in countries:
        if c['area'] >= 3000000 or c['population'] >= 25000000:
            res.append((c['name'], c['population'], c['area']))
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef bigCountries(countries):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    countries = []\n    for line in lines:\n        if not line: continue\n        parts = line.split(',')\n        countries.append({\n            'name': parts[0],\n            'continent': parts[1],\n            'area': int(parts[2]),\n            'population': int(parts[3]),\n            'gdp': int(parts[4])\n        })\n    res = bigCountries(countries)\n    for name, pop, area in res:\n        print(f\"{name} {pop} {area}\")",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n\nusing namespace std;\n\nstruct Country {\n    string name, continent;\n    int area, population;\n    long long gdp;\n};\n\nint main() {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        // User logic\n    }\n}",
        "javascript": "function solve(countries) {\n    // User logic\n}",
        "c": "void solve() {\n    // User logic\n}"
    }

    test_cases = [
        {"input": "Afghanistan,Asia,652230,25500100,20343000000\\nAlbania,Europe,28748,2831741,12960000000\\nAlgeria,Africa,2381741,37100000,188681000000\\nAndorra,Europe,468,78115,3712000000\\nAngola,Africa,1246700,20609294,100990000000", "expected_output": "Afghanistan 25500100 652230\\nAlgeria 37100000 2381741", "is_sample": True},
        {"input": "Brazil,South America,8515767,211000000,1847000000000", "expected_output": "Brazil 211000000 8515767", "is_sample": True},
        {"input": "India,Asia,3287263,1380004385,2875142000000", "expected_output": "India 1380004385 3287263", "is_sample": False},
        {"input": "China,Asia,9596961,1439323776,14342903000000", "expected_output": "China 1439323776 9596961", "is_sample": False},
        {"input": "USA,North America,9833517,331002651,21427700000000", "expected_output": "USA 331002651 9833517", "is_sample": False},
        {"input": "Small,Small,10,10,10", "expected_output": "", "is_sample": False},
        {"input": "PopOnly,Asia,1000,30000000,1000", "expected_output": "PopOnly 30000000 1000", "is_sample": False},
        {"input": "AreaOnly,Asia,5000000,1000,1000", "expected_output": "AreaOnly 1000 5000000", "is_sample": False},
        {"input": "BoundaryArea,Asia,3000000,1,1", "expected_output": "BoundaryArea 1 3000000", "is_sample": False},
        # Stress cases
        {"input": "\\n".join([f"C{i},Cont,10,10,10" for i in range(1000)]), "expected_output": "", "is_sample": False},
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
        "topics": ["Array", "Filtering"],
        "companyIndex": 0
    }

    output_path = "401-600/595_Big_Countries.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
