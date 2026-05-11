import json
import os

def generate_json():
    problem_id = 195
    title = "Tenth Line"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>195. Tenth Line</h3>
<p>Given a text file <code>file.txt</code>, print&nbsp;just the 10th line of the file.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<p>Assume <code>file.txt</code> has the following content:</p>
<pre>
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
</pre>
<p>Your script should output the tenth line, which is:</p>
<pre>
Line 10
</pre>

<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ul>
	<li>If the file contains less than 10 lines, what should you output? Nothing.</li>
	<li>You may solve this using <code>sed</code>, <code>awk</code>, or shell commands.</li>
</ul>"""

    input_format = "A text file named file.txt."
    output_format = "The tenth line of the file, or nothing if the file has fewer than 10 lines."
    
    constraints = [
        "The file may contain any characters.",
        "Lines are separated by '\\n'.",
        "If line 10 is empty, output an empty line."
    ]
    
    explanation = """To print the 10th line of a file in Bash, there are several efficient ways:
1. **Using `sed`**:
   - `sed -n '10p' file.txt`
   - The `-n` flag suppresses automatic printing, and `10p` tells `sed` to print only the 10th line.
2. **Using `awk`**:
   - `awk 'NR == 10' file.txt`
   - `NR` is the built-in variable for the record number (line number).
3. **Using `tail` and `head`**:
   - `tail -n +10 file.txt | head -n 1`
   - `tail -n +10` prints starting from line 10, and `head -n 1` picks the first line of that output. Note that if the file has < 10 lines, `tail -n +10` returns nothing, which is the desired behavior."""
    
    answer = """# Using sed
sed -n '10p' file.txt

# Or using awk
# awk 'NR == 10' file.txt

# Or using tail/head
# tail -n +10 file.txt | head -n 1"""

    boilerplate = {
        "python": "# Bash script task. Equivalent Python logic:\nimport sys\n\ndef tenth_line(filename):\n    try:\n        with open(filename, 'r') as f:\n            for i, line in enumerate(f):\n                if i == 9:\n                    print(line.rstrip('\\n'))\n                    return\n    except FileNotFoundError: pass",
        "cpp": "// Bash script task.",
        "java": "// Bash script task.",
        "javascript": "// Bash script task.",
        "c": "// Bash script task."
    }

    test_cases = [
        {"input": "Line 1\\nLine 2\\nLine 3\\nLine 4\\nLine 5\\nLine 6\\nLine 7\\nLine 8\\nLine 9\\nLine 10", "expected_output": "Line 10", "is_sample": True},
        {"input": "1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9", "expected_output": "", "is_sample": True},
        {"input": "A\\nB\\nC\\nD\\nE\\nF\\nG\\nH\\nI\\nJ\\nK", "expected_output": "J", "is_sample": False},
        {"input": "\\n\\n\\n\\n\\n\\n\\n\\n\\nEmptyLine", "expected_output": "EmptyLine", "is_sample": False},
        {"input": "1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\n  Leading Spaces", "expected_output": "  Leading Spaces", "is_sample": False},
        {"input": "1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\nLine@#$!%", "expected_output": "Line@#$!%", "is_sample": False},
        {"input": "1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\n10\\n11\\n12\\n13\\n14\\n15", "expected_output": "10", "is_sample": False},
        # Stress/Edge
        {"input": "\\n" * 9 + "Tenth is Newline", "expected_output": "Tenth is Newline", "is_sample": False},
        {"input": "Nothing\\n" * 9, "expected_output": "", "is_sample": False},
        {"input": "Z" * 100 + "\\n" * 9 + "LongLine", "expected_output": "LongLine", "is_sample": False}
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
            "allowed_languages": ["bash"]
        },
        "topics": ["Shell"],
        "companyIndex": 0
    }

    output_path = "1-200/195_Tenth_Line.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
