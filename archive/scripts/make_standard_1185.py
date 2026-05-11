import json
import os

def generate_json():
    problem_id = 1185
    title = "Day of the Week"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1185. Day of the Week</h3>
<p>Given a date, return the corresponding day of the week for that date.</p>

<p>The input is given as three integers representing the <code>day</code>, <code>month</code> and <code>year</code>.</p>

<p>Return the answer as one of the following strings: <code>{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> day = 31, month = 8, year = 2019
<strong>Output:</strong> "Saturday"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> day = 18, month = 7, year = 1999
<strong>Output:</strong> "Sunday"
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> day = 15, month = 8, year = 1993
<strong>Output:</strong> "Sunday"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The given dates are valid dates between the years <code>1971</code> and <code>2100</code>.</li>
</ul>"""

    input_format = "Three lines. Line 1: day (int). Line 2: month (int). Line 3: year (int)."
    output_format = "A string representing the name of the day of the week."
    
    constraints = [
        "Date is valid.",
        "Year is between 1971 and 2100.",
        "Note: Jan 1, 1971 was a Friday.",
        "O(1) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To find the day of the week for a given date:
1. **Built-in Libraries**:
   - Most languages (Python, Java, JavaScript) have built-in date/time libraries that can calculate the weekday.
   - Example (Python): `datetime.date(year, month, day).strftime('%A')`.
2. **Formulaic Approach (Zeller's Congruence)**:
   - For an implementation without libraries, Zeller's Congruence can calculate the weekday in O(1).
   - Alternatively, calculate total days since a known reference point (e.g., Jan 1, 1971, which was a Friday).
   - `total_days = (days_in_past_years) + (days_in_past_months_of_current_year) + (days_of_current_month)`.
   - `day_index = (total_days + 5) % 7` (offset 5 because Jan 1 1971 was a Friday / index 5).
3. **Complexity**:
   - Time Complexity: O(1) as the calculations are fixed regardless of the date.
   - Space Complexity: O(1) extra space."""
    
    answer = """import datetime
def dayOfTheWeek(day: int, month: int, year: int) -> str:
    return datetime.date(year, month, day).strftime('%A')"""

    boilerplate = {
        "python": "import sys\nimport datetime\n\ndef dayOfTheWeek(day, month, year):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        print(dayOfTheWeek(int(lines[0]), int(lines[1]), int(lines[2])))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n\nusing namespace std;\n\nstring dayOfTheWeek(int day, int month, int year) {\n    // User logic\n    return \"\";\n}",
        "java": "import java.util.*;\nimport java.time.*;\n\npublic class Solution {\n    public String dayOfTheWeek(int day, int month, int year) {\n        // User logic\n        return \"\";\n    }\n}",
        "javascript": "function dayOfTheWeek(day, month, year) {\n    // User logic\n}",
        "c": "char* dayOfTheWeek(int day, int month, int year) {\n    // User logic\n    return \"\";\n}"
    }

    test_cases = [
        {"input": "31\\n8\\n2019", "expected_output": "Saturday", "is_sample": True},
        {"input": "18\\n7\\n1999", "expected_output": "Sunday", "is_sample": True},
        {"input": "15\\n8\\n1993", "expected_output": "Sunday", "is_sample": True},
        {"input": "1\\n1\\n1971", "expected_output": "Friday", "is_sample": False},
        {"input": "21\\n12\\n1980", "expected_output": "Sunday", "is_sample": False},
        {"input": "29\\n2\\n2000", "expected_output": "Tuesday", "is_sample": False},
        {"input": "29\\n2\\n2004", "expected_output": "Sunday", "is_sample": False},
        # Diverse/Stress cases
        {"input": "31\\n12\\n2100", "expected_output": "Friday", "is_sample": False},
        {"input": "1\\n1\\n2100", "expected_output": "Friday", "is_sample": False},
        {"input": "28\\n2\\n2100", "expected_output": "Sunday", "is_sample": False}
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
        "topics": ["Math"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1185_Day_of_the_Week.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
