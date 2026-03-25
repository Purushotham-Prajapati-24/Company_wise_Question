import os
import json
import re

base_dir = r"d:\College Projects\MNC_based\companyWiseQuestions"
report = []

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".json"):
            match = re.match(r"^(\d{3})_", file)
            if match:
                problem_id = int(match.group(1))
                if 100 <= problem_id <= 130:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        q_text = data.get("question_text", "")
                        h3_match = re.search(r"<h3>(\d+)\s+", q_text)
                        has_period = False
                        if h3_match:
                            if q_text.startswith(f"<h3>{problem_id}. "):
                                has_period = True
                        
                        test_cases = data.get("test_cases", [])
                        num_test_cases = len(test_cases)
                        
                        report.append({
                            "id": problem_id,
                            "file": file_path,
                            "has_period": has_period,
                            "num_test_cases": num_test_cases
                        })
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

with open("audit_100_130.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4)

print(f"Audit complete. Total files: {len(report)}")
