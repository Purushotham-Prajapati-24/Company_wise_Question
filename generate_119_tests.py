import json

def get_row(rowIndex):
    row = [1] * (rowIndex + 1)
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j - 1]
    return row

test_indices = [3, 0, 1, 10, 20, 33, 2, 4, 5, 13]
final_tcs = []

for idx in test_indices:
    expected = get_row(idx)
    final_tcs.append({
        "input": str(idx),
        "expected_output": json.dumps(expected).replace(" ", ""),
        "is_sample": idx in [3, 0, 1]
    })

file_path = 'd:/College Projects/MNC_based/companyWiseQuestions/Visa/119_Pascal_s_Triangle_II.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data['test_cases'] = final_tcs

if "<h3>119 " in data['question_text']:
     data['question_text'] = data['question_text'].replace("<h3>119 ", "<h3>119. ")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Updated 119 in Visa")
