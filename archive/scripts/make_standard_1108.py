import json
import os

def generate_json():
    problem_id = 1108
    title = "Defanging an IP Address"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1108. Defanging an IP Address</h3>
<p>Given a valid (IPv4) IP <code>address</code>, return a defanged version of that IP address.</p>

<p>A <em>defanged&nbsp;IP address</em> replaces every period <code>"."</code> with <code>"[.]"</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> address = "1.1.1.1"
<strong>Output:</strong> "1[.]1[.]1[.]1"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> address = "255.100.50.0"
<strong>Output:</strong> "255[.]100[.]50[.]0"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The given <code>address</code> is a valid IPv4 address.</li>
</ul>"""

    input_format = "A single line containing the IPv4 address string."
    output_format = "The defanged IPv4 address string."
    
    constraints = [
        "Address is a valid IPv4 address.",
        "O(N) time complexity.",
        "O(N) space complexity."
    ]
    
    explanation = """To defang an IP address:
1. **Definition**:
   - Defanging involves replacing all instances of a period `.` with the string `[.]`.
2. **Implementation**:
   - Most modern programming languages have a built-in `replace` method for strings.
   - Alternatively, you can iterate through the string and append to a result builder (like a list in Python or StringBuilder in Java).
   - For every character `c`, if `c == '.'`, append `[.]`. Otherwise, append `c`.
3. **Complexity**:
   - Time Complexity: O(N) where N is the length of the IP address (usually fixed to ~15, but string length is N).
   - Space Complexity: O(N) to store the new defanged string."""
    
    answer = """def defangIPaddr(address: str) -> str:
    return address.replace(".", "[.]")"""

    boilerplate = {
        "python": "import sys\n\ndef defangIPaddr(address):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(defangIPaddr(line))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nstring defangIPaddr(string address) {\n    // User logic\n    return \"\";\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public String defangIPaddr(String address) {\n        // User logic\n        return \"\";\n    }\n}",
        "javascript": "function defangIPaddr(address) {\n    // User logic\n}",
        "c": "char* defangIPaddr(char* address) {\n    // User logic\n    return \"\";\n}"
    }

    test_cases = [
        {"input": "1.1.1.1", "expected_output": "1[.]1[.]1[.]1", "is_sample": True},
        {"input": "255.100.50.0", "expected_output": "255[.]100[.]50[.]0", "is_sample": True},
        {"input": "0.0.0.0", "expected_output": "0[.]0[.]0[.]0", "is_sample": True},
        {"input": "192.168.1.1", "expected_output": "192[.]168[.]1[.]1", "is_sample": False},
        {"input": "127.0.0.1", "expected_output": "127[.]0[.]0[.]1", "is_sample": False},
        {"input": "10.0.0.1", "expected_output": "10[.]0[.]0[.]1", "is_sample": False},
        {"input": "8.8.8.8", "expected_output": "8[.]8[.]8[.]8", "is_sample": False},
        # Stress/Diverse cases
        {"input": "1.2.3.4", "expected_output": "1[.]2[.]3[.]4", "is_sample": False},
        {"input": "100.200.250.255", "expected_output": "100[.]200[.]250[.]255", "is_sample": False},
        {"input": "255.255.255.255", "expected_output": "255[.]255[.]255[.]255", "is_sample": False}
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
        "topics": ["String"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1108_Defanging_an_IP_Address.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
